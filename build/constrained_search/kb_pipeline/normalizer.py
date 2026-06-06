from __future__ import annotations

from typing import Any

from .utils import dedupe, first_present, infer_table_id_from_column_id, listify


def normalize_cards(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for card in cards:
        normalized = normalize_card(card)
        cid = normalized.get("canonical_id")
        if not cid or cid in seen:
            continue
        seen.add(str(cid))
        out.append(normalized)
    return out


def normalize_card(card: dict[str, Any]) -> dict[str, Any]:
    c = dict(card)
    c.setdefault("canonical_id", c.get("id") or c.get("source_card_id"))
    c.setdefault("card_type", "unknown")
    c.setdefault("retrieval", {})
    c.setdefault("traversal", {})
    c.setdefault("fields", {})
    c["retrieval"] = c["retrieval"] if isinstance(c.get("retrieval"), dict) else {}
    c["traversal"] = c["traversal"] if isinstance(c.get("traversal"), dict) else {}
    c["fields"] = c["fields"] if isinstance(c.get("fields"), dict) else {}
    c["ingestion_node_sets"] = build_ingestion_node_sets(c)
    return c


def normalize_edges(edges: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[tuple[str, str, str]] = set()
    out: list[dict[str, Any]] = []
    for edge in edges:
        source_id = str(edge.get("source_id") or "")
        target_id = str(edge.get("target_id") or "")
        edge_type = str(edge.get("edge_type") or edge.get("canonical_edge_type") or "")
        if not source_id or not target_id or not edge_type:
            out.append(edge)
            continue
        key = (source_id, edge_type, target_id)
        if key in seen:
            continue
        seen.add(key)
        out.append(edge)
    return out


def build_ingestion_node_sets(card: dict[str, Any]) -> list[str]:
    retrieval = card.get("retrieval") if isinstance(card.get("retrieval"), dict) else {}
    traversal = card.get("traversal") if isinstance(card.get("traversal"), dict) else {}
    fields = card.get("fields") if isinstance(card.get("fields"), dict) else {}
    meta = card.get("_meta") if isinstance(card.get("_meta"), dict) else {}
    ctype = str(card.get("card_type") or "unknown")
    cid = str(card.get("canonical_id") or "")
    node_sets = listify(retrieval.get("node_sets"))

    node_sets.extend([f"card_type:{ctype}", f"canonical_id:{cid}"])
    source_family = meta.get("source_family")
    domain_family = (
        traversal.get("domain_family")
        or fields.get("domain_family")
        or (card.get("ownership") or {}).get("domain_family")
        or source_family
    )
    if domain_family:
        node_sets.append(f"domain_family:{domain_family}")

    for key in (
        "tenant_id",
        "group_id",
        "platform_id",
        "platform_context_id",
        "platform_account_id",
        "table_id",
        "domain_id",
        "source_role",
    ):
        value = traversal.get(key) or fields.get(key) or card.get(key)
        if value:
            node_sets.append(f"{key}:{value}")

    if ctype == "table" and cid:
        node_sets.append(f"table_id:{cid}")
    if ctype in {"column", "metric_implementation", "query_pattern", "value_profile", "relationship"}:
        table_id = first_present(
            traversal.get("table_id"),
            fields.get("table_id"),
            card.get("table_id"),
            infer_table_id_from_column_id(cid),
        )
        if table_id:
            node_sets.append(f"table_id:{table_id}")

    layer = meta.get("pack_layer_hint")
    if layer:
        node_sets.append(f"source_layer:{layer}")
    return dedupe(str(item) for item in node_sets if item)

