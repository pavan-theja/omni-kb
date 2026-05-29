from __future__ import annotations

import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Mapping, Optional, Sequence, Set

from .canonical import validate_canonical
from .io_utils import write_json, write_jsonl


BLOCKING_REVIEW_SEVERITIES = {"blocking", "critical", "error", "high"}

PLATFORM_METRIC_PREFIXES = (
    "nykaa_fashion",
    "hdfc_bank",
    "icici_bank",
    "xpressbees",
    "shadowfax",
    "delhivery",
    "shiprocket",
    "flipkart",
    "myntra",
    "amazon",
    "nykaa",
    "dtdc",
    "ekart",
    "hdfc",
    "icici",
    "ecom",
)


@dataclass(frozen=True)
class PromotionResult:
    promoted_card_count: int
    promoted_edge_count: int
    blocked_card_count: int
    blocked_edge_count: int
    review_item_count: int
    blocking_review_item_count: int
    output_dir: str
    manifest_path: str


def promote_intermediate(
    candidate_cards: Sequence[Mapping[str, object]],
    candidate_edges: Sequence[Mapping[str, object]],
    review_items: Sequence[Mapping[str, object]],
    known_chunk_ids: Iterable[str],
    output_dir: Path,
    clean: bool = True,
) -> PromotionResult:
    blocked_chunk_ids = _blocking_review_chunk_ids(review_items)
    promoted_cards = [
        _promote_card(card)
        for card in candidate_cards
        if not _artifact_has_blocked_evidence(card, blocked_chunk_ids)
    ]
    promoted_card_ids = {str(card["canonical_id"]) for card in promoted_cards}
    promoted_edges = [
        _promote_edge(edge)
        for edge in candidate_edges
        if not _artifact_has_blocked_evidence(edge, blocked_chunk_ids)
        and edge.get("source_id") in promoted_card_ids
        and edge.get("target_id") in promoted_card_ids
    ]
    eligible_card_count = len(promoted_cards)
    eligible_edge_count = len(promoted_edges)

    promoted_cards, promoted_edges = _normalize_promoted_artifacts(promoted_cards, promoted_edges)

    validation = validate_canonical(promoted_cards, promoted_edges, known_chunk_ids)
    if not validation.ok:
        messages = "; ".join(
            f"{issue.artifact_id}: {issue.message}"
            for issue in validation.issues
            if issue.severity == "error"
        )
        raise ValueError(f"promoted canonical artifacts failed validation: {messages}")

    if clean and output_dir.exists():
        _clean_output_dir(output_dir)

    cards_dir = output_dir / "cards"
    for card in promoted_cards:
        card_type = str(card["card_type"])
        canonical_id = str(card["canonical_id"])
        write_json(card, cards_dir / card_type / f"{_file_slug(canonical_id)}.json")

    write_jsonl(promoted_cards, output_dir / "cards.jsonl")
    write_jsonl(promoted_edges, output_dir / "edges.jsonl")

    manifest = _manifest(
        promoted_cards,
        promoted_edges,
        candidate_cards,
        candidate_edges,
        eligible_card_count,
        eligible_edge_count,
        review_items,
        validation,
    )
    manifest_path = output_dir / "manifest.json"
    write_json(manifest, manifest_path)

    return PromotionResult(
        promoted_card_count=len(promoted_cards),
        promoted_edge_count=len(promoted_edges),
        blocked_card_count=len(candidate_cards) - eligible_card_count,
        blocked_edge_count=len(candidate_edges) - eligible_edge_count,
        review_item_count=len(review_items),
        blocking_review_item_count=sum(
            1 for item in review_items if _is_blocking_review_item(item)
        ),
        output_dir=str(output_dir),
        manifest_path=str(manifest_path),
    )


def _promote_card(card: Mapping[str, object]) -> Dict[str, object]:
    promoted = dict(card)
    extraction = dict(promoted.get("extraction") or {})
    extraction["promoted_from"] = "build/intermediate"
    promoted["extraction"] = extraction
    promoted.setdefault("review_status", "unreviewed")
    promoted.setdefault("status", "draft")
    promoted.setdefault("confidence", "unknown")
    if not promoted.get("source_documents"):
        promoted["source_documents"] = _source_documents_for(promoted)
    promoted.setdefault("created_by", "kb_pipeline.cleaned_v2")
    promoted.setdefault("updated_by", "kb_pipeline.cleaned_v2")
    promoted.setdefault("created_at", _today())
    promoted.setdefault("updated_at", promoted.get("created_at") or _today())
    promoted["evidence_refs"] = _canonical_evidence_refs(promoted)
    return promoted


def _promote_edge(edge: Mapping[str, object]) -> Dict[str, object]:
    promoted = dict(edge)
    extraction = dict(promoted.get("extraction") or {})
    extraction["promoted_from"] = "build/intermediate"
    promoted["extraction"] = extraction
    promoted.setdefault("review_status", "unreviewed")
    promoted.setdefault("confidence", "unknown")
    promoted["evidence_refs"] = _canonical_evidence_refs(promoted)
    return promoted


def _today() -> str:
    return datetime.now(timezone.utc).date().isoformat()


def _source_documents_for(artifact: Mapping[str, object]) -> List[str]:
    values = _as_list(artifact.get("source_documents"))
    values.extend(_as_list(artifact.get("source_path")))
    values.extend(_as_list(artifact.get("source_paths")))
    return sorted({value for value in values if value}) or ["processed_kb_docs/cleaned"]


def _canonical_evidence_refs(artifact: Mapping[str, object]) -> List[Dict[str, object]]:
    refs: List[Dict[str, object]] = []
    seen = set()
    source_doc = str(artifact.get("source_path") or artifact.get("source_doc") or "")
    source_line = artifact.get("source_line")

    raw_refs = artifact.get("evidence_refs")
    if raw_refs in (None, "", []):
        raw_refs = artifact.get("evidence_ids")
    for ref in raw_refs or []:
        if isinstance(ref, Mapping):
            clean = {str(key): value for key, value in ref.items() if value not in (None, "", [])}
        else:
            clean = {"evidence_id": str(ref)}
        if source_doc and "source_doc" not in clean:
            clean["source_doc"] = source_doc
        if source_line and "source_line" not in clean:
            clean["source_line"] = source_line
        key = tuple(sorted((str(k), str(v)) for k, v in clean.items()))
        if key not in seen:
            refs.append(clean)
            seen.add(key)

    if not refs and source_doc:
        clean = {"source_doc": source_doc}
        if source_line:
            clean["source_line"] = source_line
        refs.append(clean)
    return refs


def _normalize_promoted_artifacts(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
) -> tuple[List[Dict[str, object]], List[Dict[str, object]]]:
    table_aliases = _table_aliases(cards)
    normalized_cards = [_normalize_card_ids(card, table_aliases) for card in cards]
    normalized_edges = [_normalize_edge_ids(edge, table_aliases) for edge in edges]
    normalized_cards = _ensure_metric_parents(normalized_cards)
    normalized_cards = _infer_metric_implementation_tables(normalized_cards)
    card_ids = {str(card.get("canonical_id")) for card in normalized_cards}
    normalized_edges.extend(_inferred_metric_edges(normalized_cards, normalized_edges, card_ids))
    normalized_edges.extend(_inferred_metric_table_edges(normalized_cards, normalized_edges, card_ids))
    normalized_edges = [
        edge for edge in normalized_edges
        if edge.get("source_id") in card_ids and edge.get("target_id") in card_ids
    ]
    normalized_cards = _merge_cards(normalized_cards)
    card_ids = {str(card.get("canonical_id")) for card in normalized_cards}
    normalized_edges = _dedupe_edges(
        edge for edge in normalized_edges
        if edge.get("source_id") in card_ids and edge.get("target_id") in card_ids
    )
    normalized_cards = _attach_denormalized_refs(normalized_cards, normalized_edges)
    return (
        sorted(normalized_cards, key=lambda item: str(item["canonical_id"])),
        sorted(
            normalized_edges,
            key=lambda item: (
                str(item["source_id"]),
                str(item["edge_type"]),
                str(item["target_id"]),
            ),
        ),
    )


def _normalize_card_ids(
    card: Mapping[str, object],
    table_aliases: Mapping[str, str],
) -> Dict[str, object]:
    item = dict(card)
    canonical_id = str(item.get("canonical_id") or "")
    card_type = str(item.get("card_type") or "")
    if card_type == "metric":
        item["canonical_id"] = _generic_metric_id(canonical_id)
        item["evidence_table_ids"] = _canonicalize_table_refs(item.get("evidence_table_ids"), table_aliases)
        if not item.get("business_definition"):
            metric_name = str(item.get("metric_name") or item.get("name") or _titleize(str(item["canonical_id"]).removeprefix("metric.")))
            description = str(item.get("description") or "")
            if description.startswith("Explicit canonical reference"):
                description = f"Generic metric concept for {metric_name}."
            item["business_definition"] = description or f"Generic metric concept for {metric_name}."
    elif card_type == "metric_implementation":
        metric_id = str(item.get("metric_id") or "")
        if metric_id:
            item["metric_id"] = _generic_metric_id(metric_id)
        else:
            item["metric_id"] = _metric_id_from_impl(canonical_id)
        item["base_tables"] = _canonicalize_table_refs(item.get("base_tables"), table_aliases)
        scope = canonical_id.split(".")
        if len(scope) >= 3 and not item.get("implementation_scope"):
            item["implementation_scope"] = scope[1]
        platform_code = _platform_code_from_scope(str(item.get("implementation_scope") or ""))
        if platform_code and not item.get("platform_code"):
            item["platform_code"] = platform_code
    elif card_type == "column":
        table_id = str(item.get("table_id") or "")
        if table_id:
            item["table_id"] = table_aliases.get(table_id, table_id)
    elif card_type == "account_data_binding":
        table_id = str(item.get("table_id") or "")
        if table_id:
            item["table_id"] = table_aliases.get(table_id, table_id)
    elif card_type == "business_flow_binding":
        item["evidence_table_ids"] = _canonicalize_table_refs(item.get("evidence_table_ids"), table_aliases)
    elif card_type == "relationship":
        source_table = str(item.get("source_table") or "")
        target_table = str(item.get("target_table") or "")
        if source_table:
            item["source_table"] = table_aliases.get(source_table, source_table)
        if target_table:
            item["target_table"] = table_aliases.get(target_table, target_table)
    elif card_type == "value_profile":
        table_id = str(item.get("table_id") or "")
        column_id = str(item.get("column_id") or "")
        if table_id:
            normalized_table_id = table_aliases.get(table_id, table_id)
            item["table_id"] = normalized_table_id
            if column_id.startswith(f"column.{table_id.removeprefix('table.')}"):
                item["column_id"] = column_id.replace(
                    f"column.{table_id.removeprefix('table.')}",
                    f"column.{normalized_table_id.removeprefix('table.')}",
                    1,
                )
    return item


def _normalize_edge_ids(
    edge: Mapping[str, object],
    table_aliases: Mapping[str, str],
) -> Dict[str, object]:
    item = dict(edge)
    source_id = str(item.get("source_id") or "")
    target_id = str(item.get("target_id") or "")
    item["source_id"] = _normalize_reference_id(source_id, table_aliases)
    item["target_id"] = _normalize_reference_id(target_id, table_aliases)
    return item


def _normalize_reference_id(value: str, table_aliases: Mapping[str, str]) -> str:
    if value.startswith("metric."):
        return _generic_metric_id(value)
    if value.startswith("table."):
        return table_aliases.get(value, value)
    return value


def _generic_metric_id(metric_id: str) -> str:
    if not metric_id.startswith("metric."):
        return metric_id
    slug = metric_id.removeprefix("metric.")
    for prefix in PLATFORM_METRIC_PREFIXES:
        marker = f"{prefix}_"
        if slug.startswith(marker) and len(slug) > len(marker):
            return f"metric.{slug[len(marker):]}"
    return metric_id


def _metric_id_from_impl(impl_id: str) -> str:
    if not impl_id.startswith("metric_impl."):
        return ""
    parts = impl_id.split(".")
    if len(parts) < 3:
        return ""
    return _generic_metric_id(f"metric.{parts[-1]}")


def _table_aliases(cards: Sequence[Mapping[str, object]]) -> Dict[str, str]:
    qualified_by_name: DefaultDict[str, List[str]] = defaultdict(list)
    table_ids = {
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") == "table" and card.get("canonical_id")
    }
    for table_id in table_ids:
        tail = table_id.removeprefix("table.").split(".")[-1]
        if "." in table_id.removeprefix("table."):
            qualified_by_name[tail].append(table_id)
    aliases: Dict[str, str] = {}
    for table_id in table_ids:
        full = table_id.removeprefix("table.")
        if "." in full:
            continue
        qualified = sorted(qualified_by_name.get(full, []))
        if len(qualified) == 1:
            aliases[table_id] = qualified[0]
    return aliases


def _canonicalize_table_refs(value: object, table_aliases: Mapping[str, str]) -> List[str]:
    refs = _as_list(value)
    return sorted({table_aliases.get(ref, ref) for ref in refs if ref})


def _ensure_metric_parents(cards: Sequence[Mapping[str, object]]) -> List[Dict[str, object]]:
    by_id = {str(card.get("canonical_id")): dict(card) for card in cards if card.get("canonical_id")}
    for card in cards:
        if str(card.get("card_type") or "") != "metric_implementation":
            continue
        metric_id = str(card.get("metric_id") or "")
        if not metric_id or metric_id in by_id:
            continue
        by_id[metric_id] = _metric_parent_from_impl(metric_id, card)
    return list(by_id.values())


def _infer_metric_implementation_tables(cards: Sequence[Mapping[str, object]]) -> List[Dict[str, object]]:
    table_ids = {
        str(card.get("canonical_id") or "")
        for card in cards
        if str(card.get("card_type") or "") == "table" and card.get("canonical_id")
    }
    enriched: List[Dict[str, object]] = []
    for card in cards:
        item = dict(card)
        if str(item.get("card_type") or "") != "metric_implementation":
            enriched.append(item)
            continue
        if _as_list(item.get("base_tables")):
            enriched.append(item)
            continue
        scope = str(item.get("implementation_scope") or "")
        if not scope:
            parts = str(item.get("canonical_id") or "").split(".")
            if len(parts) >= 3:
                scope = parts[1]
        candidates = [
            f"table.{scope}",
            f"table.zs_observe.{scope}",
            f"table.zs_recon_processor.{scope}",
            f"table.zs_refined.{scope}",
        ]
        matches = [candidate for candidate in candidates if candidate in table_ids]
        if len(matches) == 1:
            item["base_tables"] = matches
        enriched.append(item)
    return enriched


def _metric_parent_from_impl(
    metric_id: str,
    impl: Mapping[str, object],
) -> Dict[str, object]:
    name = _titleize(metric_id.removeprefix("metric."))
    evidence_refs = list(impl.get("evidence_refs") or [])
    source_documents = list(impl.get("source_documents") or [])
    created_at = str(impl.get("created_at") or "")
    updated_at = str(impl.get("updated_at") or created_at)
    return {
        "card_type": "metric",
        "canonical_id": metric_id,
        "name": name,
        "metric_name": name,
        "description": str(impl.get("description") or f"Generic metric concept for {name}."),
        "business_definition": str(impl.get("description") or f"Generic metric concept for {name}."),
        "status": str(impl.get("status") or "draft"),
        "confidence": str(impl.get("confidence") or "inferred"),
        "source_documents": sorted({str(item) for item in source_documents if item}),
        "created_by": str(impl.get("created_by") or "kb_pipeline.promoter"),
        "updated_by": "kb_pipeline.promoter",
        "created_at": created_at,
        "updated_at": updated_at,
        "review_status": str(impl.get("review_status") or "unreviewed"),
        "version": str(impl.get("version") or "0.1"),
        "tags": sorted(set(_as_list(impl.get("tags"))) | {"generic_metric", "inferred_metric_parent"}),
        "aliases": _metric_aliases_from_slug(metric_id.removeprefix("metric.")),
        "business_concepts": list(impl.get("business_concepts") or []),
        "evidence_refs": evidence_refs,
        "extraction": {
            **dict(impl.get("extraction") or {}),
            "normalized_by": "zenkb.promoter",
        },
    }


def _inferred_metric_edges(
    cards: Sequence[Mapping[str, object]],
    existing_edges: Sequence[Mapping[str, object]],
    card_ids: Set[str],
) -> List[Dict[str, object]]:
    existing = {
        (str(edge.get("source_id")), str(edge.get("edge_type")), str(edge.get("target_id")))
        for edge in existing_edges
    }
    edges: List[Dict[str, object]] = []
    for card in cards:
        if str(card.get("card_type") or "") != "metric_implementation":
            continue
        impl_id = str(card.get("canonical_id") or "")
        metric_id = str(card.get("metric_id") or "")
        key = (metric_id, "HAS_IMPLEMENTATION", impl_id)
        if not metric_id or metric_id not in card_ids or not impl_id or key in existing:
            continue
        edges.append(
            {
                "source_id": metric_id,
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": impl_id,
                "confidence": str(card.get("confidence") or "inferred"),
                "review_status": str(card.get("review_status") or "unreviewed"),
                "evidence_refs": list(card.get("evidence_refs") or []),
                "extraction": {
                    **dict(card.get("extraction") or {}),
                    "inferred_by": "zenkb.promoter",
                },
            }
        )
    return edges


def _inferred_metric_table_edges(
    cards: Sequence[Mapping[str, object]],
    existing_edges: Sequence[Mapping[str, object]],
    card_ids: Set[str],
) -> List[Dict[str, object]]:
    existing = {
        (str(edge.get("source_id")), str(edge.get("edge_type")), str(edge.get("target_id")))
        for edge in existing_edges
    }
    edges: List[Dict[str, object]] = []
    for card in cards:
        if str(card.get("card_type") or "") != "metric_implementation":
            continue
        impl_id = str(card.get("canonical_id") or "")
        for table_id in _as_list(card.get("base_tables")):
            key = (impl_id, "USES_TABLE", table_id)
            if not impl_id or table_id not in card_ids or key in existing:
                continue
            edges.append(
                {
                    "source_id": impl_id,
                    "edge_type": "USES_TABLE",
                    "target_id": table_id,
                    "confidence": str(card.get("confidence") or "inferred"),
                    "review_status": str(card.get("review_status") or "unreviewed"),
                    "evidence_refs": list(card.get("evidence_refs") or []),
                    "extraction": {
                        **dict(card.get("extraction") or {}),
                        "inferred_by": "zenkb.promoter",
                    },
                }
            )
    return edges


def _merge_cards(cards: Sequence[Mapping[str, object]]) -> List[Dict[str, object]]:
    merged: Dict[str, Dict[str, object]] = {}
    for card in cards:
        canonical_id = str(card.get("canonical_id") or "")
        if canonical_id not in merged:
            merged[canonical_id] = dict(card)
            continue
        _merge_card_into(merged[canonical_id], card)
    return list(merged.values())


def _merge_card_into(existing: Dict[str, object], incoming: Mapping[str, object]) -> None:
    for key in ("source_documents", "aliases", "business_concepts", "tags", "base_tables"):
        values = set(_as_list(existing.get(key)))
        values.update(_as_list(incoming.get(key)))
        if values:
            existing[key] = sorted(values)
    evidence_refs = existing.setdefault("evidence_refs", [])
    if isinstance(evidence_refs, list):
        seen = {
            (str(ref.get("source_doc")), str(ref.get("chunk_id")), str(ref.get("source_span")))
            for ref in evidence_refs
            if isinstance(ref, Mapping)
        }
        for ref in incoming.get("evidence_refs", []) or []:
            if not isinstance(ref, Mapping):
                continue
            key = (str(ref.get("source_doc")), str(ref.get("chunk_id")), str(ref.get("source_span")))
            if key not in seen:
                evidence_refs.append(ref)
                seen.add(key)
    if existing.get("confidence") != "curated" and incoming.get("confidence") == "curated":
        existing["confidence"] = "curated"
    for key in ("business_definition", "description"):
        current = str(existing.get(key) or "")
        candidate = str(incoming.get(key) or "")
        if len(candidate) > len(current):
            existing[key] = candidate


def _dedupe_edges(edges: Iterable[Mapping[str, object]]) -> List[Dict[str, object]]:
    deduped: Dict[tuple[str, str, str], Dict[str, object]] = {}
    for edge in edges:
        key = (
            str(edge.get("source_id") or ""),
            str(edge.get("edge_type") or ""),
            str(edge.get("target_id") or ""),
        )
        if key not in deduped:
            deduped[key] = dict(edge)
            continue
        existing = deduped[key]
        evidence_refs = existing.setdefault("evidence_refs", [])
        if isinstance(evidence_refs, list):
            seen = {str(ref.get("chunk_id")) for ref in evidence_refs if isinstance(ref, Mapping)}
            for ref in edge.get("evidence_refs", []) or []:
                if isinstance(ref, Mapping) and str(ref.get("chunk_id")) not in seen:
                    evidence_refs.append(ref)
                    seen.add(str(ref.get("chunk_id")))
    return list(deduped.values())


def _attach_denormalized_refs(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
) -> List[Dict[str, object]]:
    columns_by_table: DefaultDict[str, Set[str]] = defaultdict(set)
    implementations_by_metric: DefaultDict[str, Set[str]] = defaultdict(set)
    metric_impls_by_table: DefaultDict[str, Set[str]] = defaultdict(set)
    relationships_by_table: DefaultDict[str, Set[str]] = defaultdict(set)
    business_flows_by_table: DefaultDict[str, Set[str]] = defaultdict(set)

    for edge in edges:
        source = str(edge.get("source_id") or "")
        target = str(edge.get("target_id") or "")
        edge_type = str(edge.get("edge_type") or "")
        if edge_type == "HAS_COLUMN":
            columns_by_table[source].add(target)
        elif edge_type == "HAS_IMPLEMENTATION":
            implementations_by_metric[source].add(target)
        elif edge_type in {"USES_TABLE", "APPLIES_TO_TABLE"}:
            if source.startswith("metric_impl."):
                metric_impls_by_table[target].add(source)
            elif source.startswith("relationship."):
                relationships_by_table[target].add(source)
            elif source.startswith("business_flow_binding."):
                business_flows_by_table[target].add(source)

    for card in cards:
        if str(card.get("card_type") or "") == "metric_implementation":
            impl_id = str(card.get("canonical_id") or "")
            for table_id in _as_list(card.get("base_tables")):
                metric_impls_by_table[table_id].add(impl_id)

    enriched = []
    for card in cards:
        item = dict(card)
        canonical_id = str(item.get("canonical_id") or "")
        card_type = str(item.get("card_type") or "")
        if card_type == "table":
            _set_sorted_if_present(item, "column_ids", columns_by_table.get(canonical_id))
            _set_sorted_if_present(item, "metric_implementation_ids", metric_impls_by_table.get(canonical_id))
            _set_sorted_if_present(item, "relationship_ids", relationships_by_table.get(canonical_id))
            _set_sorted_if_present(item, "business_flow_binding_ids", business_flows_by_table.get(canonical_id))
        elif card_type == "metric":
            _set_sorted_if_present(item, "implementation_ids", implementations_by_metric.get(canonical_id))
        enriched.append(item)
    return enriched


def _set_sorted_if_present(item: Dict[str, object], key: str, values: Optional[Iterable[str]]) -> None:
    clean = sorted({str(value) for value in values or [] if value})
    if clean:
        item[key] = clean


def _platform_code_from_scope(scope: str) -> str:
    if not scope:
        return ""
    for prefix in PLATFORM_METRIC_PREFIXES:
        if scope == prefix or scope.startswith(f"{prefix}_"):
            return prefix
    return scope.split("_", 1)[0]


def _metric_aliases_from_slug(slug: str) -> List[str]:
    label = slug.replace("_", " ")
    aliases = {label, label.title()}
    if "gmv" in slug or "gross_sales" in slug:
        aliases.update({"GMV", "gross merchandise value", "gross sales"})
    if "average_order_value" in slug:
        aliases.add("AOV")
    if "seller_realization" in slug:
        aliases.update({"seller realization", "realization rate"})
    return sorted(aliases, key=str.lower)


def _titleize(value: str) -> str:
    return value.replace(".", " ").replace("_", " ").title()


def _as_list(value: object) -> List[str]:
    if value in (None, "", []):
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if item not in (None, "")]
    return [str(value)]


def _blocking_review_chunk_ids(review_items: Sequence[Mapping[str, object]]) -> Set[str]:
    return {
        str(item.get("chunk_id"))
        for item in review_items
        if _is_blocking_review_item(item) and item.get("chunk_id")
    }


def _is_blocking_review_item(item: Mapping[str, object]) -> bool:
    return str(item.get("severity", "")).lower() in BLOCKING_REVIEW_SEVERITIES


def _artifact_has_blocked_evidence(
    artifact: Mapping[str, object],
    blocked_chunk_ids: Set[str],
) -> bool:
    for ref in artifact.get("evidence_refs", []) or []:
        if isinstance(ref, Mapping) and str(ref.get("chunk_id")) in blocked_chunk_ids:
            return True
    return False


def _clean_output_dir(output_dir: Path) -> None:
    for path in (output_dir / "cards", output_dir / "cards.jsonl", output_dir / "edges.jsonl", output_dir / "manifest.json"):
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def _manifest(
    promoted_cards: Sequence[Mapping[str, object]],
    promoted_edges: Sequence[Mapping[str, object]],
    candidate_cards: Sequence[Mapping[str, object]],
    candidate_edges: Sequence[Mapping[str, object]],
    eligible_card_count: int,
    eligible_edge_count: int,
    review_items: Sequence[Mapping[str, object]],
    validation,
) -> Dict[str, object]:
    card_types = Counter(str(card.get("card_type")) for card in promoted_cards)
    review_by_severity = Counter(str(item.get("severity", "unknown")) for item in review_items)
    review_by_type = Counter(str(item.get("review_type", "unknown")) for item in review_items)

    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "generator": "zenkb.promoter",
        "source_artifacts": {
            "candidate_cards": "build/intermediate/candidate_cards.jsonl",
            "candidate_edges": "build/intermediate/candidate_edges.jsonl",
            "review_items": "build/intermediate/review_items.jsonl",
        },
        "promotion_policy": {
            "blocking_review_severities": sorted(BLOCKING_REVIEW_SEVERITIES),
            "promote_non_blocking_review_items": True,
            "requires_canonical_validation": True,
        },
        "counts": {
            "candidate_cards": len(candidate_cards),
            "candidate_edges": len(candidate_edges),
            "promoted_cards": len(promoted_cards),
            "promoted_edges": len(promoted_edges),
            "blocked_cards": len(candidate_cards) - eligible_card_count,
            "blocked_edges": len(candidate_edges) - eligible_edge_count,
            "normalization_added_cards": len(promoted_cards) - eligible_card_count,
            "normalization_added_edges": len(promoted_edges) - eligible_edge_count,
            "review_items": len(review_items),
            "validation_issues": len(validation.issues),
        },
        "card_types": dict(sorted(card_types.items())),
        "review_items": {
            "by_severity": dict(sorted(review_by_severity.items())),
            "by_type": dict(sorted(review_by_type.items())),
        },
        "validation": {
            "ok": validation.ok,
            "issues": [
                {
                    "severity": issue.severity,
                    "artifact_id": issue.artifact_id,
                    "message": issue.message,
                }
                for issue in validation.issues
            ],
        },
    }


def _file_slug(canonical_id: str) -> str:
    return canonical_id.replace(".", "__").replace("/", "_")
