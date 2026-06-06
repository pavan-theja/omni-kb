from __future__ import annotations

from collections import Counter
from typing import Any

from .utils import flatten_strings


FULL_PROFILE = "full"
MARKETPLACE_RUNTIME_PROFILE = "marketplace_runtime"
PROFILE_CHOICES = (FULL_PROFILE, MARKETPLACE_RUNTIME_PROFILE, "marketplace-runtime")
MARKETPLACE_PLATFORM_IDS = {
    "platform.amazon",
    "platform.flipkart",
    "platform.meesho",
    "platform.myntra",
    "platform.nykaa",
}


def canonical_profile(value: str) -> str:
    return value.replace("-", "_")


def apply_slice_profile(
    cards: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    *,
    profile: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, Any]]:
    profile = canonical_profile(profile)
    if profile == FULL_PROFILE:
        return cards, edges, build_slice_manifest(profile, cards, edges, cards, edges)
    if profile == MARKETPLACE_RUNTIME_PROFILE:
        selected_cards = marketplace_runtime_cards(cards)
        selected_ids = {str(card.get("canonical_id")) for card in selected_cards if card.get("canonical_id")}
        selected_edges = [
            edge
            for edge in edges
            if edge_source_id(edge) in selected_ids and edge_target_id(edge) in selected_ids
        ]
        return selected_cards, selected_edges, build_slice_manifest(profile, cards, edges, selected_cards, selected_edges)
    raise ValueError(f"Unknown constrained-search build profile: {profile}")


def marketplace_runtime_cards(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    by_id = {str(card.get("canonical_id")): card for card in cards if card.get("canonical_id")}
    selected_ids: set[str] = set()

    for card in cards:
        cid = str(card.get("canonical_id") or "")
        if semantic_marketplace_card(card):
            selected_ids.add(cid)
        elif marketplace_runtime_card(card):
            selected_ids.add(cid)

    selected_ids.update(runtime_reference_closure(selected_ids, by_id))
    selected_ids.update(semantic_table_dependencies(selected_ids, by_id, cards))
    selected_ids.update(probe_required_ids(by_id))

    return [card for card in cards if str(card.get("canonical_id") or "") in selected_ids]


def semantic_marketplace_card(card: dict[str, Any]) -> bool:
    if source_layer(card) != "semantic":
        return False
    meta = card.get("_meta") if isinstance(card.get("_meta"), dict) else {}
    if meta.get("source_family") != "marketplace" and "domain_family:marketplace" not in node_sets(card):
        return False
    platform_ids = card_platform_ids(card)
    return not platform_ids or bool(platform_ids & MARKETPLACE_PLATFORM_IDS)


def marketplace_runtime_card(card: dict[str, Any]) -> bool:
    if source_layer(card) != "runtime":
        return False
    cid = str(card.get("canonical_id") or "")
    ctype = str(card.get("card_type") or "")
    if ctype in {"tenant", "group"}:
        return False

    haystack = " ".join(flatten_strings([cid, card.get("fields"), card.get("traversal"), card.get("retrieval")])).lower()
    if ctype in {"account_data_binding", "platform_account"}:
        if not (".marketplace" in haystack or "marketplace_seller_account" in haystack):
            return False
        return bool(card_platform_ids(card) & MARKETPLACE_PLATFORM_IDS)
    if ctype in {"business_scope_set", "business_flow_binding"}:
        return "marketplace" in haystack
    return False


def runtime_reference_closure(selected_ids: set[str], by_id: dict[str, dict[str, Any]]) -> set[str]:
    out = set(selected_ids)
    changed = True
    while changed:
        changed = False
        for cid in list(out):
            card = by_id.get(cid)
            if not card or source_layer(card) != "runtime":
                continue
            for ref in card_references(card):
                target = by_id.get(ref)
                if target and source_layer(target) == "runtime" and runtime_dependency_allowed(target) and ref not in out:
                    out.add(ref)
                    changed = True
    return out


def runtime_dependency_allowed(card: dict[str, Any]) -> bool:
    ctype = str(card.get("card_type") or "")
    if ctype in {"tenant", "group"}:
        return True
    return marketplace_runtime_card(card)


def semantic_table_dependencies(
    selected_ids: set[str],
    by_id: dict[str, dict[str, Any]],
    cards: list[dict[str, Any]],
) -> set[str]:
    table_ids: set[str] = set()
    direct_semantic_ids: set[str] = set()
    for cid in selected_ids:
        card = by_id.get(cid)
        if not card or source_layer(card) != "runtime":
            continue
        if card.get("card_type") != "account_data_binding":
            continue
        for ref in card_references(card):
            target = by_id.get(ref)
            if ref.startswith("table."):
                table_ids.add(ref)
            if target and source_layer(target) == "semantic":
                direct_semantic_ids.add(ref)

    out = set(direct_semantic_ids)
    for card in cards:
        if source_layer(card) != "semantic":
            continue
        cid = str(card.get("canonical_id") or "")
        if cid in table_ids or card_value(card, "table_id") in table_ids:
            out.add(cid)
    return out


def probe_required_ids(by_id: dict[str, dict[str, Any]]) -> set[str]:
    ids = {
        "platform.amazon",
        "table.zs_observe.amazon_oms",
        "table.zs_observe.amazon_settlement",
        "tenant.mensa_brand_technologies_private_limited",
        "group.mensa_brand_technologies_private_limited.g8.gl22",
    }
    return {cid for cid in ids if cid in by_id}


def card_references(card: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for value in flatten_strings([card.get("fields"), card.get("traversal")]):
        if value.startswith(("tenant.", "group.", "platform.", "platform_context.", "platform_account.", "table.", "business_scope_set.", "business_flow_binding.", "account_data_binding.")):
            refs.add(value)
    return refs


def edge_source_id(edge: dict[str, Any]) -> str:
    return str(edge.get("source_id") or edge.get("source_card_id") or "")


def edge_target_id(edge: dict[str, Any]) -> str:
    return str(edge.get("target_id") or edge.get("target_card_id") or "")


def source_layer(card: dict[str, Any]) -> str:
    meta = card.get("_meta") if isinstance(card.get("_meta"), dict) else {}
    return str(meta.get("pack_layer_hint") or "")


def node_sets(card: dict[str, Any]) -> set[str]:
    return {str(item) for item in card.get("ingestion_node_sets") or []}


def card_platform_ids(card: dict[str, Any]) -> set[str]:
    values = {card_value(card, "platform_id")}
    values.update(item.removeprefix("platform_id:") for item in node_sets(card) if item.startswith("platform_id:"))
    return {value for value in values if value.startswith("platform.")}


def card_value(card: dict[str, Any], key: str) -> str:
    for holder in (card.get("traversal"), card.get("fields"), card):
        if isinstance(holder, dict) and holder.get(key):
            return str(holder[key])
    return ""


def build_slice_manifest(
    profile: str,
    all_cards: list[dict[str, Any]],
    all_edges: list[dict[str, Any]],
    selected_cards: list[dict[str, Any]],
    selected_edges: list[dict[str, Any]],
) -> dict[str, Any]:
    selected_ids = {str(card.get("canonical_id")) for card in selected_cards if card.get("canonical_id")}
    return {
        "profile": canonical_profile(profile),
        "card_count": len(selected_cards),
        "edge_count": len(selected_edges),
        "excluded_card_count": len(all_cards) - len(selected_cards),
        "excluded_edge_count": len(all_edges) - len(selected_edges),
        "source_layer_counts": dict(sorted(Counter(source_layer(card) or "unknown" for card in selected_cards).items())),
        "card_type_counts": dict(sorted(Counter(str(card.get("card_type") or "unknown") for card in selected_cards).items())),
        "selection_rules": selection_rules(canonical_profile(profile)),
        "marketplace_platform_ids": sorted(MARKETPLACE_PLATFORM_IDS) if profile == MARKETPLACE_RUNTIME_PROFILE else [],
        "selected_runtime_binding_count": sum(1 for card in selected_cards if card.get("card_type") == "account_data_binding"),
        "selected_table_count": sum(1 for card in selected_cards if card.get("card_type") == "table"),
        "sample_ids": sorted(selected_ids)[:25],
    }


def selection_rules(profile: str) -> list[str]:
    if profile == MARKETPLACE_RUNTIME_PROFILE:
        return [
            "include semantic marketplace cards for Amazon, Flipkart, Meesho, Myntra, Nykaa, plus shared marketplace cards",
            "include runtime marketplace accounts and bindings only for the selected marketplace platforms",
            "include marketplace runtime scope sets and flow bindings without pulling disallowed platform bindings",
            "include tenant/group/runtime owner cards referenced by selected marketplace runtime cards",
            "include table-local semantic dependencies referenced by selected runtime bindings",
            "include Amazon probe seed cards",
            "keep only edges whose source and target are both selected",
        ]
    return ["include all normalized cards and edges"]
