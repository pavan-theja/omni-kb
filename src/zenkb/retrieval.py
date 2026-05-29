from __future__ import annotations

import json
import os
import re
import urllib.error
import urllib.request
from collections import defaultdict, deque
from datetime import datetime, timezone
from typing import DefaultDict, Dict, Iterable, List, Mapping, Optional, Sequence, Set, Tuple


SQL_RELEVANT_CARD_TYPES = {
    "account_data_binding",
    "business_flow_binding",
    "column",
    "execution_constraint_set",
    "matching_logic",
    "metric",
    "metric_implementation",
    "mismatch_category",
    "output_contract",
    "query_pattern",
    "reconciliation_profile",
    "reconciliation_side",
    "reconciliation_unit",
    "reconciliation_variant",
    "relationship",
    "rule",
    "table",
    "validation_test",
}

FLOW_EVIDENCE_CARD_TYPES = {
    "business_flow_binding",
    "query_pattern",
    "reconciliation_variant",
    "relationship",
    "rule",
    "table",
}

SCOPE_CARD_TYPES = {
    "business_scope_set",
    "group",
    "platform",
    "platform_account",
    "tenant",
}

SQL_CONTEXT_GROUPS = {
    "account_data_binding": "account_data_bindings",
    "business_flow_binding": "business_flow_bindings",
    "column": "columns",
    "execution_constraint_set": "execution_constraints",
    "matching_logic": "matching_logic",
    "metric": "metrics",
    "metric_implementation": "metric_implementations",
    "mismatch_category": "mismatch_categories",
    "output_contract": "output_contracts",
    "query_pattern": "query_patterns",
    "reconciliation_variant": "reconciliation_variants",
    "reconciliation_profile": "reconciliation_profiles",
    "reconciliation_side": "reconciliation_sides",
    "reconciliation_unit": "reconciliation_units",
    "relationship": "relationships",
    "rule": "rules",
    "table": "tables",
    "validation_test": "validation_tests",
}

FORMULA_TEXT_FIELDS = (
    "formula_sql",
    "formula_expression",
    "formula_text",
    "sql_pattern",
    "sql_template",
    "formula_description",
)

SEARCH_FIELDS = (
    "canonical_id",
    "name",
    "description",
    "source_identifier",
    "tenant_name",
    "tenant_code",
    "group_name",
    "platform_name",
    "context_name",
    "account_name",
    "binding_name",
    "table_name",
    "full_reference",
    "column_name",
    "metric_name",
    "business_definition",
    "implementation_name",
    "metric_id",
    "formula_text",
    "formula_expression",
    "sql_pattern",
    "sql_template",
    "formula_description",
    "formula_sql",
    "source_tables",
    "source_columns",
    "required_filters",
    "process_name",
    "profile_name",
    "category_name",
    "logic_name",
    "pattern_name",
    "rule_name",
    "test_name",
    "tags",
    "aliases",
)

DIRECT_REFERENCE_FIELDS = (
    "metric_id",
    "base_tables",
    "tables",
    "source_tables",
    "columns",
    "source_columns",
    "source_table_id",
    "target_table_id",
    "table_id",
    "account_data_binding_id",
)

PLATFORM_HINTS = {
    "amazon": {"amazon"},
    "flipkart": {"flipkart"},
    "myntra": {"myntra"},
    "nykaa": {"nykaa", "nykaa_fashion"},
    "razorpay": {"razorpay"},
    "shiprocket": {"shiprocket"},
    "shopify": {"shopify", "shopify_in"},
    "delhivery": {"delhivery"},
    "dtdc": {"dtdc"},
    "ekart": {"ekart"},
    "xpressbees": {"xpressbees"},
    "hdfc_bank": {"hdfc", "hdfc_bank"},
    "icici_bank": {"icici", "icici_bank"},
}


def build_sql_context_bundle(
    query: str,
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
    *,
    max_seed_cards: int = 12,
    graph_depth: int = 2,
    max_cards: int = 80,
    cognee_base_url: str = "http://localhost:8000",
    cognee_dataset: str = "zenstatement_canonical",
    timeout: float = 30.0,
    scope_overrides: Optional[Mapping[str, str]] = None,
) -> Dict[str, object]:
    cards_by_id = {
        str(card.get("canonical_id")): card
        for card in cards
        if card.get("canonical_id")
    }
    outgoing = _edges_by(edges, "source_id")
    incoming = _edges_by(edges, "target_id")

    scope_resolution = _resolve_scope(query, cards, scope_overrides=scope_overrides)
    scope_constraints = _scope_constraints(scope_resolution, cards_by_id)
    request_facets = _request_facets(query, scope_resolution)

    cognee_results = _cognee_discovery_results(
        cognee_base_url,
        cognee_dataset,
        query,
        request_facets=request_facets,
        timeout=timeout,
    )
    if _cognee_candidate_discovery_failed(cognee_results):
        raise RuntimeError(
            "Cognee candidate discovery failed; refusing to produce a retrieval bundle without Cognee discovery. "
            "Start the local Cognee instance and ingest the canonical export, or check --cognee-base-url."
        )
    candidate_discovery_results = _candidate_discovery_results(cognee_results)
    discovered_candidate_ids = list(_ids_from_cognee_results(candidate_discovery_results, cards_by_id))
    candidate_facets = _candidate_facets_from_cognee_results(candidate_discovery_results, cards_by_id)
    unrecognized_mentions = _unrecognized_canonical_mentions(cognee_results, cards_by_id)
    seed_ids: List[str] = []
    for card_id in discovered_candidate_ids:
        if (
            card_id not in seed_ids
            and _candidate_card_type_allowed(card_id, cards_by_id)
            and _card_id_scope_compatible(card_id, cards_by_id, scope_constraints)
        ):
            seed_ids.append(card_id)
        if len(seed_ids) >= max_seed_cards:
            break
    cognee_candidates = _cognee_candidate_records(
        discovered_candidate_ids,
        seed_ids,
        cards_by_id,
        outgoing,
        incoming,
        scope_constraints,
        candidate_facets,
        unrecognized_mentions,
    )
    seed_records = [
        {
            "canonical_id": card_id,
            "reason": "cognee canonical candidate discovery",
            "source": "cognee",
        }
        for card_id in seed_ids
    ]
    exact_matches: List[Dict[str, object]] = []

    expanded_ids = _expand_graph_scoped(seed_ids, outgoing, incoming, graph_depth, cards_by_id, scope_constraints)
    expanded_ids.update(_direct_reference_ids(set(seed_ids) | expanded_ids, cards_by_id, scope_constraints))
    expanded_ids.update(_scope_support_ids(scope_resolution, cards_by_id))
    expanded_ids = _scope_filter_ids(expanded_ids, cards_by_id, scope_constraints)
    ordered_ids = _ordered_card_ids(seed_ids, expanded_ids, cards_by_id, max_cards)
    selected_cards = _prune_dependent_cards(
        [cards_by_id[card_id] for card_id in ordered_ids if card_id in cards_by_id],
        keep_ids=set(seed_ids),
    )
    selected_id_set = {str(card.get("canonical_id")) for card in selected_cards}
    selected_edges = _selected_edges(edges, selected_id_set)

    sql_context = _sql_context(selected_cards, cards_by_id)
    scope_context = _scope_context(scope_resolution, selected_cards, cards_by_id)
    handoff_contract = _sql_handoff_contract(
        query,
        selected_cards,
        sql_context,
        scope_resolution,
        cards_by_id,
        request_facets,
    )
    warnings = _completeness_warnings(
        query,
        selected_cards,
        sql_context,
        cards_by_id,
        scope_resolution,
        handoff_contract,
    )
    warnings.extend(_cognee_candidate_warnings(cognee_candidates))
    handoff_contract["can_generate_sql"] = not any(
        warning.get("severity") == "blocking" for warning in warnings
    )
    handoff_contract["readiness"] = _downstream_readiness_flags(
        handoff_contract,
        warnings,
    )

    return {
        "bundle_type": "sql_generation_context",
        "bundle_version": "0.1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "generated_by": "zenkb.retrieval",
        "query": query,
        "retrieval_policy": {
            "canonical_is_source_of_truth": True,
            "discovery_runtime": "local_cognee",
            "cognee_required_for_discovery": True,
            "returns_context_not_answer": True,
            "intended_downstream": "sql_generation",
        },
        "match_summary": {
            "seed_card_count": len(seed_ids),
            "selected_card_count": len(selected_cards),
            "selected_edge_count": len(selected_edges),
            "exact_match_count": len(exact_matches),
            "metadata_filter_count": len(scope_resolution["applied_filters"]),
        },
        "metadata_filters": scope_resolution,
        "request_facets": request_facets,
        "seeds": seed_records,
        "exact_matches": exact_matches,
        "cognee_candidates": cognee_candidates,
        "cognee_semantic_discovery": {
            "enabled": True,
            "base_url": cognee_base_url,
            "dataset": cognee_dataset,
            "results": cognee_results,
        },
        "cards": [_card_record(card) for card in selected_cards],
        "edges": [_edge_record(edge) for edge in selected_edges],
        "sql_context": sql_context,
        "scope_context": scope_context,
        "sql_handoff_contract": handoff_contract,
        "completeness_warnings": warnings,
        "unsafe_for_sql_generation": any(
            warning.get("severity") == "blocking" for warning in warnings
        ),
    }


def build_cognee_candidate_handoff(bundle: Mapping[str, object]) -> Dict[str, object]:
    metadata_filters = bundle.get("metadata_filters")
    if not isinstance(metadata_filters, Mapping):
        metadata_filters = {}
    discovery = bundle.get("cognee_semantic_discovery")
    if not isinstance(discovery, Mapping):
        discovery = {}
    candidates = bundle.get("cognee_candidates")
    if not isinstance(candidates, Mapping):
        candidates = {}
    handoff_contract = bundle.get("sql_handoff_contract")
    if not isinstance(handoff_contract, Mapping):
        handoff_contract = {}

    return {
        "bundle_type": "cognee_candidate_handoff",
        "bundle_version": "0.1",
        "source_bundle_type": bundle.get("bundle_type"),
        "source_bundle_version": bundle.get("bundle_version"),
        "query": bundle.get("query"),
        "scope": {
            "query_hints": metadata_filters.get("query_hints", {}),
            "applied_filters": metadata_filters.get("applied_filters", []),
            "required_scope": handoff_contract.get("required_scope", {}),
        },
        "request_facets": bundle.get("request_facets", {}),
        "candidate_coverage": handoff_contract.get("intent_coverage", {}),
        "readiness": handoff_contract.get("readiness", {}),
        "warnings": _compact_warnings(bundle),
        "cognee_raw_results": discovery.get("results", []),
        "cognee_candidates": {
            "accepted": candidates.get("accepted", []),
            "excluded_by_scope": candidates.get("excluded_by_scope", []),
            "unrecognized_canonical_mentions": candidates.get("unrecognized_canonical_mentions", []),
        },
        "handoff_rules": [
            "Use accepted Cognee candidates as scoped canonical evidence candidates.",
            "Do not use excluded_by_scope candidates for SQL generation.",
            "Do not use unrecognized canonical mentions unless they are promoted to real canonical cards.",
            "Canonical cards and edges remain the source of truth for IDs, scope, formulas, tables, and bindings.",
            "SQL generation owns joins, grouping, ranking, denominator logic, and final SQL.",
        ],
    }


def build_sql_handoff_brief(
    bundle: Mapping[str, object],
    *,
    max_items_per_group: int = 12,
) -> Dict[str, object]:
    sql_context = bundle.get("sql_context")
    if not isinstance(sql_context, Mapping):
        sql_context = {}
    handoff_contract = bundle.get("sql_handoff_contract")
    if not isinstance(handoff_contract, Mapping):
        handoff_contract = {}
    metadata_filters = bundle.get("metadata_filters")
    if not isinstance(metadata_filters, Mapping):
        metadata_filters = {}

    return {
        "bundle_type": "sql_generation_handoff_brief",
        "bundle_version": "0.1",
        "source_bundle_type": bundle.get("bundle_type"),
        "source_bundle_version": bundle.get("bundle_version"),
        "query": bundle.get("query"),
        "paraphrased_request": _paraphrased_request(str(bundle.get("query") or ""), metadata_filters),
        "safety": {
            "can_generate_sql": handoff_contract.get("can_generate_sql"),
            "unsafe_for_sql_generation": bundle.get("unsafe_for_sql_generation"),
            "blocking_warning_codes": [
                warning.get("code")
                for warning in _warnings(bundle)
                if warning.get("severity") == "blocking"
            ],
        },
        "scope": {
            "query_hints": metadata_filters.get("query_hints", {}),
            "applied_filters": metadata_filters.get("applied_filters", []),
            "required_scope": handoff_contract.get("required_scope", {}),
        },
        "canonical_inputs": {
            "metrics": _compact_records(sql_context.get("metrics"), max_items_per_group),
            "metric_implementations": _compact_records(
                sql_context.get("metric_implementations"),
                max_items_per_group,
            ),
            "account_data_bindings": _compact_records(
                sql_context.get("account_data_bindings"),
                max_items_per_group,
            ),
            "tables": _compact_records(sql_context.get("tables"), max_items_per_group),
            "columns": _compact_records(sql_context.get("columns"), max_items_per_group),
            "relationships": _compact_records(sql_context.get("relationships"), max_items_per_group),
            "query_patterns": _compact_records(sql_context.get("query_patterns"), max_items_per_group),
            "reconciliation_variants": _compact_records(
                sql_context.get("reconciliation_variants"),
                max_items_per_group,
            ),
            "rules": _compact_records(sql_context.get("rules"), max_items_per_group),
        },
        "sql_requirements": {
            "intent_coverage": handoff_contract.get("intent_coverage", {}),
            "required_table_ids": sql_context.get("required_table_ids", []),
            "unresolved_table_refs": sql_context.get("unresolved_table_refs", []),
            "binding_coverage": handoff_contract.get("binding_coverage", {}),
            "business_flow_coverage": handoff_contract.get("business_flow_coverage", {}),
            "reconciliation_coverage": handoff_contract.get("reconciliation_coverage", {}),
            "metric_dependencies": handoff_contract.get("metric_dependencies", []),
        },
        "completeness_warnings": _compact_warnings(bundle),
        "handoff_rules": handoff_contract.get("handoff_rules", []),
    }


def _expand_graph_scoped(
    seed_ids: Sequence[str],
    outgoing: Mapping[str, Sequence[Mapping[str, object]]],
    incoming: Mapping[str, Sequence[Mapping[str, object]]],
    graph_depth: int,
    cards_by_id: Mapping[str, Mapping[str, object]],
    scope_constraints: Mapping[str, Set[str]],
) -> Set[str]:
    scoped_seed_ids = [
        card_id for card_id in seed_ids if _card_id_scope_compatible(card_id, cards_by_id, scope_constraints)
    ]
    seen = set(scoped_seed_ids)
    queue = deque((card_id, 0) for card_id in scoped_seed_ids)
    while queue:
        card_id, depth = queue.popleft()
        if depth >= graph_depth:
            continue
        for edge in list(outgoing.get(card_id, [])) + list(incoming.get(card_id, [])):
            neighbor = str(edge.get("target_id") if edge.get("source_id") == card_id else edge.get("source_id"))
            if not neighbor or neighbor in seen:
                continue
            if not _card_id_scope_compatible(neighbor, cards_by_id, scope_constraints):
                continue
            seen.add(neighbor)
            queue.append((neighbor, depth + 1))
    return seen


def _direct_reference_ids(
    selected_ids: Iterable[str],
    cards_by_id: Mapping[str, Mapping[str, object]],
    scope_constraints: Optional[Mapping[str, Set[str]]] = None,
) -> Set[str]:
    found: Set[str] = set()
    for card_id in selected_ids:
        card = cards_by_id.get(card_id)
        if not card:
            continue
        for field in DIRECT_REFERENCE_FIELDS:
            value = card.get(field)
            for ref_id in _iter_reference_values(value):
                candidates = _table_ref_candidates(ref_id) if "table" in field else [ref_id]
                for candidate_id in candidates:
                    if candidate_id in cards_by_id and _card_id_scope_compatible(candidate_id, cards_by_id, scope_constraints):
                        found.add(candidate_id)
        for ref_id in _ids_from_text(str(card.get("formula_description") or ""), cards_by_id):
            if _card_id_scope_compatible(ref_id, cards_by_id, scope_constraints):
                found.add(ref_id)
        for ref_id in _ids_from_text(str(card.get("formula_sql") or ""), cards_by_id):
            if _card_id_scope_compatible(ref_id, cards_by_id, scope_constraints):
                found.add(ref_id)
    return found


def _request_facets(
    query: str,
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    semantic_facets = _semantic_request_facets(query, scope_resolution)
    if semantic_facets:
        return semantic_facets
    return _rule_request_facets(query, scope_resolution)


def _semantic_request_facets(
    query: str,
    scope_resolution: Mapping[str, object],
) -> Optional[Dict[str, object]]:
    config = _azure_parser_config()
    if not config:
        return None
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}
    prompt = {
        "task": "Parse this analytics retrieval request into structured facets for canonical KB retrieval.",
        "rules": [
            "Return JSON only.",
            "Do not invent canonical IDs.",
            "Use concise semantic labels, not SQL.",
            "Ranking, denominator logic, joins, and final SQL are downstream SQL-generator responsibilities.",
            "For derived metrics, emit evidence requirements and semantic metric labels only.",
            "CLI scope filters are authoritative and must be copied into filters.",
        ],
        "query": query,
        "authoritative_scope_filters": {
            "tenant_codes": sorted(_hint_values(hints, "tenant_codes")),
            "group_codes": sorted(_hint_values(hints, "group_codes")),
            "platform_codes": sorted(_hint_values(hints, "platform_codes")),
            "account_codes": sorted(_hint_values(hints, "account_codes")),
        },
        "output_schema": {
            "entities": ["tenant", "orders", "oms_systems", "marketplaces", "platform_accounts", "tables"],
            "dimensions": ["channel"],
            "metrics": ["order_volume", "order_volume_share"],
            "relationships": ["oms_to_marketplace"],
            "filters": {
                "tenant_codes": [],
                "group_codes": [],
                "platform_codes": [],
                "account_codes": [],
                "time_period": [],
            },
            "ranking": ["highest"],
            "output_type": ["answer_or_sql_context"],
            "requested_action": "answer",
            "evidence_requirements": [
                "channel column",
                "order identifier column",
                "tenant filter",
            ],
            "derived_metrics": [
                {
                    "name": "order_volume_share",
                    "base_metric": "order_volume",
                    "interpretation": "share of order volume by requested dimension",
                }
            ],
        },
    }
    messages = [
        {
            "role": "system",
            "content": (
                "You are a strict intent parser for analytics retrieval. "
                "Emit compact JSON with the requested facets. Never emit SQL or a narrative answer."
            ),
        },
        {"role": "user", "content": json.dumps(prompt, ensure_ascii=False)},
    ]
    try:
        parsed = _azure_chat_json(config, messages)
    except Exception:
        return None
    return _normalize_request_facets(parsed, scope_resolution, parser="azure_openai")


def _rule_request_facets(
    query: str,
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    tokens = set(_tokens(query))
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}

    output_types = []
    if tokens & {"summary", "summarize", "report"}:
        output_types.append("summary_report")
    if tokens & {"sql", "query"}:
        output_types.append("sql")

    requested_entities = []
    if _hint_values(hints, "tenant_codes"):
        requested_entities.append("tenant")
    if _hint_values(hints, "platform_codes") or tokens & {"marketplace", "marketplaces"}:
        requested_entities.append("marketplaces")
    if tokens & {"oms", "order", "orders"}:
        requested_entities.append("oms_systems")
    if tokens & {"order", "orders"}:
        requested_entities.append("orders")
    if tokens & {"account", "seller"}:
        requested_entities.append("platform_accounts")
    if tokens & {"table", "tables"}:
        requested_entities.append("tables")

    dimensions = []
    for dimension in ("channel", "marketplace", "courier_partner", "payment_mode"):
        dimension_tokens = set(_tokens(dimension.replace("_", " ")))
        if dimension_tokens and dimension_tokens <= tokens:
            dimensions.append(dimension)

    relationship_requests = []
    if tokens & {"connected", "connection", "connections", "connect", "linked", "link"}:
        if (tokens & {"oms", "order", "orders"}) and (tokens & {"marketplace", "marketplaces"}):
            relationship_requests.append("oms_to_marketplace")
        else:
            relationship_requests.append("entity_connection")
    elif _mentions_cross_platform_flow(tokens):
        relationship_requests.append("cross_platform_flow")

    metric_requests = []
    if {"effective", "payout", "ratio"} <= tokens:
        metric_requests.append("effective_payout_ratio")
    elif {"payout", "ratio"} <= tokens:
        metric_requests.append("payout_ratio")
    if {"seller", "realization"} <= tokens:
        metric_requests.append("seller_realization_rate")
    if "share" in tokens and tokens & {"order", "orders", "volume"}:
        metric_requests.append("order_volume_share")
        metric_requests.append("order_volume")
    elif tokens & {"order", "orders"} and tokens & {"volume", "count"}:
        metric_requests.append("order_volume")
    elif _mentions_metric_intent(tokens) and not _requires_reconciliation_profile(tokens):
        metric_requests.append("metric")

    ranking = []
    if tokens & {"highest", "top", "maximum", "max", "largest"}:
        ranking.append("highest")
    if tokens & {"lowest", "minimum", "min", "smallest"}:
        ranking.append("lowest")

    time_terms = sorted(tokens & {"today", "yesterday", "week", "month", "quarter", "year", "last", "current"})
    action = "generate"
    if tokens & {"why", "explain"}:
        action = "explain"
    elif tokens & {"compare", "match", "reconcile"}:
        action = "reconcile"

    facets = {
        "entities": sorted(set(requested_entities)),
        "dimensions": sorted(set(dimensions)),
        "relationships": relationship_requests,
        "metrics": sorted(set(metric_requests)),
        "filters": {
            "tenant_codes": sorted(_hint_values(hints, "tenant_codes")),
            "group_codes": sorted(_hint_values(hints, "group_codes")),
            "platform_codes": sorted(_hint_values(hints, "platform_codes")),
            "account_codes": sorted(_hint_values(hints, "account_codes")),
            "time_period": time_terms,
        },
        "ranking": sorted(set(ranking)),
        "time_period": {
            "requested": bool(time_terms),
            "terms": time_terms,
        },
        "output_type": output_types or ["context_bundle"],
        "requested_action": action,
        "evidence_requirements": _rule_evidence_requirements(tokens, dimensions, metric_requests),
        "derived_metrics": _rule_derived_metrics(metric_requests),
        "parser": {
            "source": "rules_fallback",
            "schema_version": "0.1",
        },
    }
    return _normalize_request_facets(facets, scope_resolution, parser="rules_fallback") or facets


def _normalize_request_facets(
    raw: object,
    scope_resolution: Mapping[str, object],
    *,
    parser: str,
) -> Optional[Dict[str, object]]:
    if not isinstance(raw, Mapping):
        return None
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}

    filters = raw.get("filters")
    if not isinstance(filters, Mapping):
        filters = {}
    normalized_filters = {
        "tenant_codes": sorted(_hint_values(hints, "tenant_codes")),
        "group_codes": sorted(_hint_values(hints, "group_codes")),
        "platform_codes": sorted(_hint_values(hints, "platform_codes")),
        "account_codes": sorted(_hint_values(hints, "account_codes")),
        "time_period": _strings(filters.get("time_period")),
    }
    time_terms = sorted(
        set(normalized_filters["time_period"])
        | set(_strings(_mapping(raw.get("time_period")).get("terms")))
    )

    output_type = _strings(raw.get("output_type")) or ["context_bundle"]
    requested_action = str(raw.get("requested_action") or "")
    if not requested_action:
        requested_action = "generate"

    return {
        "entities": _unique_strings(raw.get("entities")),
        "dimensions": _unique_strings(raw.get("dimensions")),
        "relationships": _unique_strings(raw.get("relationships")),
        "metrics": _unique_strings(raw.get("metrics")),
        "filters": normalized_filters,
        "ranking": _unique_strings(raw.get("ranking") or raw.get("sorting")),
        "time_period": {
            "requested": bool(time_terms),
            "terms": time_terms,
        },
        "output_type": output_type,
        "requested_action": requested_action,
        "evidence_requirements": _unique_strings(raw.get("evidence_requirements")),
        "derived_metrics": _normalize_derived_metrics(raw.get("derived_metrics")),
        "parser": {
            "source": parser,
            "schema_version": "0.1",
        },
    }


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _strings(value: object) -> List[str]:
    if value in (None, "", []):
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if item not in (None, "")]
    return [str(value)]


def _unique_strings(value: object) -> List[str]:
    return sorted({item.strip() for item in _strings(value) if item.strip()})


def _normalize_derived_metrics(value: object) -> List[Dict[str, object]]:
    if not isinstance(value, list):
        return []
    normalized: List[Dict[str, object]] = []
    for item in value:
        if isinstance(item, Mapping):
            name = str(item.get("name") or "").strip()
            if not name:
                continue
            normalized.append(
                {
                    key: item.get(key)
                    for key in ("name", "base_metric", "interpretation", "requires_dimension")
                    if item.get(key) not in (None, "", [])
                }
            )
        elif item:
            normalized.append({"name": str(item)})
    return normalized


def _rule_evidence_requirements(
    tokens: Set[str],
    dimensions: Sequence[str],
    metric_requests: Sequence[str],
) -> List[str]:
    requirements: List[str] = []
    for dimension in dimensions:
        requirements.append(f"{dimension} column")
    if any(metric in {"order_volume", "order_volume_share"} for metric in metric_requests):
        requirements.extend(["order identifier column", "order or OMS table"])
    if "share" in tokens:
        requirements.append("base metric evidence for share calculation")
    if tokens & {"highest", "top", "maximum", "max", "largest", "lowest", "minimum", "min", "smallest"}:
        requirements.append("ranking intent")
    return sorted(set(requirements))


def _rule_derived_metrics(metric_requests: Sequence[str]) -> List[Dict[str, object]]:
    if "order_volume_share" not in set(metric_requests):
        return []
    return [
        {
            "name": "order_volume_share",
            "base_metric": "order_volume",
            "interpretation": "share of order volume by requested dimension",
        }
    ]


def _azure_parser_config() -> Optional[Dict[str, str]]:
    enabled = os.environ.get("ZENKB_ENABLE_LLM_PARSER", "1").strip().lower()
    if enabled in {"0", "false", "no", "off"}:
        return None
    values = {
        "api_base": _env_value("AZURE_API_BASE"),
        "api_key": _env_value("AZURE_API_KEY"),
        "api_version": _env_value("AZURE_API_VERSION"),
        "deployment": _env_value("AZURE_OPENAI_DEPLOYMENT"),
    }
    if not all(values.values()):
        return None
    return values


def _env_value(name: str) -> str:
    value = os.environ.get(name)
    if value:
        return value
    if os.environ.get("ZENKB_LOAD_COGNEE_ENV_FOR_PARSER", "").strip().lower() not in {"1", "true", "yes", "on"}:
        return ""
    env_path = os.path.join(os.getcwd(), "cognee", ".env")
    try:
        with open(env_path, "r", encoding="utf-8") as handle:
            for line in handle:
                stripped = line.strip()
                if not stripped or stripped.startswith("#") or "=" not in stripped:
                    continue
                key, raw_value = stripped.split("=", 1)
                if key.strip() == name:
                    return raw_value.strip().strip('"').strip("'")
    except OSError:
        return ""
    return ""


def _azure_chat_json(config: Mapping[str, str], messages: Sequence[Mapping[str, str]]) -> object:
    base = str(config["api_base"]).rstrip("/")
    deployment = str(config["deployment"])
    api_version = str(config["api_version"])
    url = f"{base}/openai/deployments/{deployment}/chat/completions?api-version={api_version}"
    payload = {
        "messages": list(messages),
        "temperature": 0,
        "max_tokens": 900,
        "response_format": {"type": "json_object"},
    }
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "api-key": str(config["api_key"]),
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=20.0) as response:
        decoded = json.loads(response.read().decode("utf-8"))
    choices = decoded.get("choices") if isinstance(decoded, Mapping) else None
    if not isinstance(choices, list) or not choices:
        return None
    message = choices[0].get("message") if isinstance(choices[0], Mapping) else None
    content = message.get("content") if isinstance(message, Mapping) else None
    if not isinstance(content, str):
        return None
    return json.loads(content)


def _scope_constraints(
    scope_resolution: Mapping[str, object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Dict[str, Set[str]]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}
    tenant_codes = set(_hint_values(hints, "tenant_codes"))
    tenant_codes.update(_tenant_short_code(str(code)) for code in list(tenant_codes))
    group_codes = set(_hint_values(hints, "group_codes"))
    platform_codes: Set[str] = set()
    for code in _hint_values(hints, "platform_codes"):
        platform_codes.update(_platform_scope_codes(str(code)))
    explicit_platform_codes: Set[str] = set()
    applied_filters = scope_resolution.get("applied_filters")
    if isinstance(applied_filters, list):
        for item in applied_filters:
            if not isinstance(item, Mapping):
                continue
            if item.get("dimension") != "platform" or item.get("source") != "explicit":
                continue
            value = item.get("value")
            if isinstance(value, str) and value:
                explicit_platform_codes.update(_platform_scope_codes(value))
    account_codes = set(_hint_values(hints, "account_codes"))
    tenant_platform_codes: Set[str] = set()
    if tenant_codes and cards_by_id:
        for card in cards_by_id.values():
            card_scope = _card_scope(card)
            if card_scope.get("tenant") and card_scope["tenant"] & tenant_codes:
                for code in card_scope.get("platform", set()):
                    tenant_platform_codes.update(_platform_scope_codes(code))
    return {
        "tenant_codes": tenant_codes,
        "group_codes": group_codes,
        "platform_codes": platform_codes,
        "explicit_platform_codes": explicit_platform_codes,
        "account_codes": account_codes,
        "tenant_platform_codes": tenant_platform_codes,
    }


def _card_id_scope_compatible(
    card_id: str,
    cards_by_id: Mapping[str, Mapping[str, object]],
    scope_constraints: Optional[Mapping[str, Set[str]]],
) -> bool:
    card = cards_by_id.get(card_id)
    if not card:
        return False
    return _card_scope_compatible(card, scope_constraints)


def _candidate_card_type_allowed(
    card_id: str,
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> bool:
    card = cards_by_id.get(card_id)
    if not card:
        return False
    card_type = str(card.get("card_type") or "")
    return card_type in SQL_RELEVANT_CARD_TYPES or card_type in SCOPE_CARD_TYPES


def _card_scope_compatible(
    card: Mapping[str, object],
    scope_constraints: Optional[Mapping[str, Set[str]]],
) -> bool:
    if not scope_constraints:
        return True
    card_scope = _card_scope(card)
    tenant_codes = set(scope_constraints.get("tenant_codes", set()))
    group_codes = set(scope_constraints.get("group_codes", set()))
    platform_codes = set(scope_constraints.get("platform_codes", set()))
    explicit_platform_codes = set(scope_constraints.get("explicit_platform_codes", set()))
    account_codes = set(scope_constraints.get("account_codes", set()))
    tenant_platform_codes = set(scope_constraints.get("tenant_platform_codes", set()))

    if tenant_codes and card_scope.get("tenant") and not (card_scope["tenant"] & tenant_codes):
        return False
    if group_codes and card_scope.get("group") and not (card_scope["group"] & group_codes):
        return False
    if account_codes and card_scope.get("account") and not (card_scope["account"] & account_codes):
        return False
    card_platforms = set()
    for code in card_scope.get("platform", set()):
        card_platforms.update(_platform_scope_codes(code))
    if tenant_platform_codes and card_platforms and not card_platforms <= tenant_platform_codes:
        return False
    if explicit_platform_codes and card_platforms and not (card_platforms & explicit_platform_codes):
        return False
    return True


def _scope_filter_ids(
    card_ids: Iterable[str],
    cards_by_id: Mapping[str, Mapping[str, object]],
    scope_constraints: Mapping[str, Set[str]],
) -> Set[str]:
    return {
        card_id
        for card_id in card_ids
        if _card_id_scope_compatible(card_id, cards_by_id, scope_constraints)
    }


def _prune_dependent_cards(
    cards: Sequence[Mapping[str, object]],
    *,
    keep_ids: Optional[Set[str]] = None,
) -> List[Mapping[str, object]]:
    keep_ids = keep_ids or set()
    selected_ids = {str(card.get("canonical_id")) for card in cards if card.get("canonical_id")}
    pruned: List[Mapping[str, object]] = []
    for card in cards:
        card_type = str(card.get("card_type") or "")
        canonical_id = str(card.get("canonical_id") or "")
        if canonical_id in keep_ids:
            pruned.append(card)
            continue
        if card_type == "column":
            table_id = str(card.get("table_id") or "")
            if not table_id and canonical_id.startswith("column."):
                parts = canonical_id.split(".")
                if len(parts) > 2:
                    table_id = "table." + ".".join(parts[1:-1])
            if table_id and table_id not in selected_ids:
                continue
        pruned.append(card)
    return pruned


def _sql_context(
    cards: Sequence[Mapping[str, object]],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Dict[str, object]:
    grouped: Dict[str, List[Dict[str, object]]] = {
        group: [] for group in sorted(set(SQL_CONTEXT_GROUPS.values()))
    }
    required_table_ids: Set[str] = set()
    unresolved_table_refs: Set[str] = set()

    for card in cards:
        card_type = str(card.get("card_type") or "")
        group = SQL_CONTEXT_GROUPS.get(card_type)
        if group:
            grouped[group].append(_sql_card_record(card))
        if card_type == "metric_implementation":
            for table_id in _table_refs_for_card(card):
                if table_id in cards_by_id:
                    required_table_ids.add(table_id)
                elif table_id:
                    unresolved_table_refs.add(table_id)

    for table_id in sorted(required_table_ids):
        if not any(record.get("canonical_id") == table_id for record in grouped["tables"]):
            grouped["tables"].append(_sql_card_record(cards_by_id[table_id]))

    return {
        **grouped,
        "required_table_ids": sorted(required_table_ids),
        "unresolved_table_refs": sorted(unresolved_table_refs),
    }


def _sql_handoff_contract(
    query: str,
    cards: Sequence[Mapping[str, object]],
    sql_context: Mapping[str, object],
    scope_resolution: Mapping[str, object],
    cards_by_id: Mapping[str, Mapping[str, object]],
    request_facets: Mapping[str, object],
) -> Dict[str, object]:
    query_tokens = set(_tokens(query))
    required_scope = _required_scope_contract(query_tokens, scope_resolution)
    metric_dependencies = _metric_dependency_contract(cards)
    binding_coverage = _binding_coverage_contract(
        cards,
        sql_context,
        scope_resolution,
        required_scope,
        cards_by_id,
    )
    business_flow_coverage = _business_flow_coverage_contract(query_tokens, cards, scope_resolution)
    reconciliation_coverage = _reconciliation_coverage_contract(query_tokens, cards)
    intent_coverage = _intent_coverage_contract(
        request_facets,
        cards,
        sql_context,
        scope_resolution,
        business_flow_coverage,
    )

    return {
        "contract_version": "0.1",
        "can_generate_sql": False,
        "intent_coverage": intent_coverage,
        "required_scope": required_scope,
        "binding_coverage": binding_coverage,
        "business_flow_coverage": business_flow_coverage,
        "reconciliation_coverage": reconciliation_coverage,
        "metric_dependencies": metric_dependencies,
        "handoff_rules": [
            "Use canonical cards and edges as source of truth.",
            "Use Cognee output only as discovery context.",
            "Do not generate SQL when a blocking completeness warning is present.",
            "Ask for clarification when required tenant scope is missing.",
            "Prefer selected account data bindings when applying tenant/platform/account filters.",
            "Require business flow evidence before generating cross-platform SQL.",
            "Require reconciliation profile evidence before generating profile/playbook reconciliation SQL.",
        ],
    }


def _required_scope_contract(
    query_tokens: Set[str],
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}

    tenant_codes = _hint_values(hints, "tenant_codes")
    group_codes = _hint_values(hints, "group_codes")
    platform_codes = _hint_values(hints, "platform_codes")
    account_codes = _hint_values(hints, "account_codes")
    tenant_required = _requires_tenant_scope(query_tokens)

    return {
        "tenant": {
            "required": tenant_required,
            "resolved": bool(tenant_codes),
            "codes": sorted(tenant_codes),
        },
        "group": {
            "required": False,
            "resolved": bool(group_codes),
            "codes": sorted(group_codes),
        },
        "platform": {
            "required": False,
            "resolved": bool(platform_codes),
            "codes": sorted(platform_codes),
        },
        "account": {
            "required": False,
            "resolved": bool(account_codes),
            "codes": sorted(account_codes),
        },
    }


def _metric_dependency_contract(
    cards: Sequence[Mapping[str, object]],
) -> List[Dict[str, object]]:
    dependencies: List[Dict[str, object]] = []
    for card in cards:
        if str(card.get("card_type") or "") != "metric_implementation":
            continue
        formula_text = _formula_text(card)
        table_refs = _table_refs_for_card(card)
        required_table_ids = [
            table_ref for table_ref in table_refs if table_ref.startswith("table.")
        ]
        dependencies.append(
            {
                "metric_implementation_id": card.get("canonical_id"),
                "metric_id": card.get("metric_id"),
                "has_formula": bool(formula_text.strip()),
                "requires_tables": True,
                "required_table_ids": required_table_ids,
                "required_table_refs": table_refs,
                "requires_columns": bool(formula_text.strip()),
                "required_columns": _columns_from_formula(formula_text),
                "required_filters": _filters_from_formula(formula_text),
            }
        )
    return dependencies


def _binding_coverage_contract(
    cards: Sequence[Mapping[str, object]],
    sql_context: Mapping[str, object],
    scope_resolution: Mapping[str, object],
    required_scope: Mapping[str, object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Dict[str, object]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}
    tenant_codes = _hint_values(hints, "tenant_codes")
    platform_codes = _hint_values(hints, "platform_codes")
    account_codes = _hint_values(hints, "account_codes")
    scoped = bool(
        tenant_codes
        or account_codes
        or (isinstance(required_scope.get("tenant"), Mapping) and required_scope["tenant"].get("required"))
    )

    bindings = [
        card for card in cards if str(card.get("card_type") or "") == "account_data_binding"
    ]
    matching_bindings = [
        card for card in bindings if _binding_matches_scope(card, tenant_codes, platform_codes, account_codes)
    ]

    required_table_ids = [
        str(table_id)
        for table_id in sql_context.get("required_table_ids", [])
        if isinstance(table_id, str)
    ]
    table_bindings = []
    for table_id in required_table_ids:
        table_card = cards_by_id.get(table_id)
        binding_ids = [
            str(binding.get("canonical_id"))
            for binding in matching_bindings
            if _binding_covers_table(binding, table_card)
        ]
        table_bindings.append(
            {
                "table_id": table_id,
                "required": scoped,
                "binding_ids": sorted(binding_ids),
            }
        )

    return {
        "required": scoped,
        "matching_binding_ids": sorted(
            str(binding.get("canonical_id")) for binding in matching_bindings if binding.get("canonical_id")
        ),
        "required_table_bindings": table_bindings,
    }


def _business_flow_coverage_contract(
    query_tokens: Set[str],
    cards: Sequence[Mapping[str, object]],
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    involved_platforms = _involved_platform_codes(cards, scope_resolution)
    primary_platforms = sorted({_primary_platform_code(code) for code in involved_platforms})
    required = len(primary_platforms) >= 2 and _mentions_cross_platform_flow(query_tokens)
    evidence_cards = [
        card for card in cards if _is_flow_evidence_card(card, set(primary_platforms))
    ]
    return {
        "required": required,
        "involved_platform_codes": sorted(involved_platforms),
        "primary_platform_codes": primary_platforms,
        "selected_flow_evidence_ids": sorted(
            str(card.get("canonical_id")) for card in evidence_cards if card.get("canonical_id")
        ),
        "evidence_card_types": sorted(
            {str(card.get("card_type")) for card in evidence_cards if card.get("card_type")}
        ),
    }


def _reconciliation_coverage_contract(
    query_tokens: Set[str],
    cards: Sequence[Mapping[str, object]],
) -> Dict[str, object]:
    profile_cards = [
        card for card in cards if str(card.get("card_type") or "") == "reconciliation_profile"
    ]
    variant_cards = [
        card for card in cards if str(card.get("card_type") or "") == "reconciliation_variant"
    ]
    required = bool(profile_cards or variant_cards or _requires_reconciliation_profile(query_tokens))
    evidence_text = _selected_reconciliation_text(cards)
    side_evidence = _reconciliation_sides(cards, evidence_text)
    unit_evidence = _reconciliation_units(cards, evidence_text)
    matching_logic_ids = _reconciliation_matching_logic_ids(cards, evidence_text)
    mismatch_category_ids = [
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") == "mismatch_category" and card.get("canonical_id")
    ]
    if not mismatch_category_ids:
        mismatch_category_ids = _mismatch_category_ids_from_text(evidence_text)

    missing: List[str] = []
    if required and not profile_cards:
        missing.append("profile")
    if required and len(side_evidence) < 2:
        missing.append("sides")
    if required and not unit_evidence:
        missing.append("units")
    if required and not matching_logic_ids:
        missing.append("matching_logic")
    if required and not mismatch_category_ids:
        missing.append("mismatch_categories")

    return {
        "required": required,
        "profile_ids": sorted(str(card.get("canonical_id")) for card in profile_cards if card.get("canonical_id")),
        "variant_ids": sorted(str(card.get("canonical_id")) for card in variant_cards if card.get("canonical_id")),
        "side_evidence": sorted(side_evidence),
        "unit_evidence": sorted(unit_evidence),
        "matching_logic_ids": sorted(matching_logic_ids),
        "mismatch_category_ids": sorted(mismatch_category_ids),
        "missing": missing,
    }


def _intent_coverage_contract(
    facets: Mapping[str, object],
    cards: Sequence[Mapping[str, object]],
    sql_context: Mapping[str, object],
    scope_resolution: Mapping[str, object],
    business_flow_coverage: Mapping[str, object],
) -> Dict[str, object]:
    facet_coverage = {
        "entities": _entity_facet_coverage(facets, cards, scope_resolution),
        "dimensions": _dimension_facet_coverage(facets, cards),
        "relationships": _relationship_facet_coverage(facets, cards, business_flow_coverage),
        "metrics": _metric_facet_coverage(facets, cards),
        "filters": _filter_facet_coverage(facets, scope_resolution),
        "ranking": _ranking_facet_coverage(facets),
        "time_period": _time_period_facet_coverage(facets),
        "output_type": _output_type_facet_coverage(facets),
        "requested_action": _requested_action_facet_coverage(facets),
    }
    missing_required = [
        name
        for name, coverage in facet_coverage.items()
        if coverage.get("required") and coverage.get("status") in {"missing", "partial", "unsupported"}
    ]
    sql_ready = not missing_required
    report_ready = sql_ready and facet_coverage["time_period"].get("status") != "missing"
    safe_actions = ["generate_context_summary"]
    if sql_ready:
        safe_actions.append("generate_sql")
    if report_ready:
        safe_actions.append("generate_final_report")
    if missing_required or facet_coverage["time_period"].get("status") == "missing":
        safe_actions.append("ask_clarifying_question")

    unsafe_actions = []
    if not sql_ready:
        unsafe_actions.append("generate_final_sql")
    if not report_ready:
        unsafe_actions.append("generate_final_report")

    return {
        "facets": facet_coverage,
        "missing_required_facets": sorted(missing_required),
        "safe_downstream_actions": safe_actions,
        "unsafe_downstream_actions": unsafe_actions,
        "sql_generation_ready": sql_ready,
        "report_generation_ready": report_ready,
        "note": "Coverage reports retrieval evidence only; SQL planning remains downstream.",
    }


def _downstream_readiness_flags(
    handoff_contract: Mapping[str, object],
    warnings: Sequence[Mapping[str, object]],
) -> Dict[str, bool]:
    intent_coverage = handoff_contract.get("intent_coverage")
    if not isinstance(intent_coverage, Mapping):
        intent_coverage = {}
    facets = intent_coverage.get("facets")
    if not isinstance(facets, Mapping):
        facets = {}

    blocking = any(warning.get("severity") == "blocking" for warning in warnings)
    missing_required = intent_coverage.get("missing_required_facets")
    if not isinstance(missing_required, list):
        missing_required = []
    metrics = facets.get("metrics") if isinstance(facets.get("metrics"), Mapping) else {}
    relationships = facets.get("relationships") if isinstance(facets.get("relationships"), Mapping) else {}
    metric_ready = not blocking and not missing_required and metrics.get("status") in {"resolved", "not_requested"}
    relationship_ready = (
        not blocking
        and relationships.get("status") in {"resolved", "not_requested"}
        and "relationships" not in missing_required
    )
    context_summary_ready = not any(
        warning.get("severity") == "blocking" and warning.get("code") == "missing_required_tenant_scope"
        for warning in warnings
    )
    production_sql_ready = not blocking and not missing_required
    return {
        "can_generate_context_summary": context_summary_ready,
        "can_generate_metric_sql": metric_ready,
        "can_generate_relationship_report": relationship_ready,
        "can_generate_final_answer": context_summary_ready and not missing_required,
        "can_generate_production_sql": production_sql_ready,
    }


def _entity_facet_coverage(
    facets: Mapping[str, object],
    cards: Sequence[Mapping[str, object]],
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    requested = facets.get("entities")
    if not isinstance(requested, list) or not requested:
        return _facet_not_requested()

    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}

    resolved: List[str] = []
    partial: List[str] = []
    missing: List[str] = []
    evidence_ids: Set[str] = set()
    card_ids = {str(card.get("canonical_id")) for card in cards if card.get("canonical_id")}

    if "tenant" in requested:
        tenant_codes = _hint_values(hints, "tenant_codes")
        if tenant_codes:
            resolved.extend(f"tenant:{code}" for code in sorted(tenant_codes))
            evidence_ids.update(card_id for card_id in card_ids if card_id.startswith("tenant."))
        else:
            missing.append("tenant")
    if "marketplaces" in requested:
        platform_ids = [card_id for card_id in card_ids if card_id.startswith("platform.")]
        account_ids = [card_id for card_id in card_ids if card_id.startswith("platform_account.")]
        platform_codes = _hint_values(hints, "platform_codes")
        if platform_ids or account_ids or platform_codes:
            resolved.extend(sorted(platform_ids + account_ids))
            resolved.extend(f"platform:{code}" for code in sorted(platform_codes))
            evidence_ids.update(platform_ids + account_ids)
        else:
            missing.append("marketplaces")
    if "platform_accounts" in requested:
        account_ids = [card_id for card_id in card_ids if card_id.startswith("platform_account.")]
        if account_ids:
            resolved.extend(sorted(account_ids))
            evidence_ids.update(account_ids)
        else:
            missing.append("platform_accounts")
    if "oms_systems" in requested:
        oms_ids = _selected_ids_with_terms(cards, {"oms"}, {"table", "account_data_binding"})
        order_ids = _selected_ids_with_terms(cards, {"orders"}, {"table", "account_data_binding"})
        if oms_ids:
            resolved.extend(sorted(oms_ids))
            evidence_ids.update(oms_ids)
        elif order_ids:
            partial.extend(sorted(order_ids))
            evidence_ids.update(order_ids)
            missing.append("explicit_oms_system_entities")
        else:
            missing.append("oms_systems")

    status = _coverage_status(resolved, partial, missing)
    return {
        "required": True,
        "status": status,
        "requested": requested,
        "resolved": sorted(set(resolved)),
        "partial": sorted(set(partial)),
        "missing": sorted(set(missing)),
        "evidence_ids": sorted(evidence_ids),
    }


def _relationship_facet_coverage(
    facets: Mapping[str, object],
    cards: Sequence[Mapping[str, object]],
    business_flow_coverage: Mapping[str, object],
) -> Dict[str, object]:
    requested = facets.get("relationships")
    if not isinstance(requested, list) or not requested:
        return _facet_not_requested()

    relationship_ids = [
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") == "relationship" and card.get("canonical_id")
    ]
    flow_ids = business_flow_coverage.get("selected_flow_evidence_ids")
    if not isinstance(flow_ids, list):
        flow_ids = []
    flow_ids = sorted(
        set(str(item) for item in flow_ids)
        | {
            str(card.get("canonical_id"))
            for card in cards
            if str(card.get("card_type") or "") == "business_flow_binding" and card.get("canonical_id")
        }
    )

    resolved = sorted(set(relationship_ids + [str(item) for item in flow_ids]))
    partial = []
    missing = []
    if "oms_to_marketplace" in requested and not _has_oms_marketplace_relationship(cards) and not flow_ids:
        binding_ids = [
            str(card.get("canonical_id"))
            for card in cards
            if str(card.get("card_type") or "") == "account_data_binding" and card.get("canonical_id")
        ]
        if binding_ids:
            partial = sorted(binding_ids)
        missing.append("oms_to_marketplace_relationship_evidence")
        resolved = []
    elif not resolved:
        missing.append("relationship_evidence")

    return {
        "required": True,
        "status": _coverage_status(resolved, partial, missing),
        "requested": requested,
        "resolved": resolved,
        "partial": partial,
        "missing": missing,
        "evidence_ids": sorted(set(resolved + partial)),
    }


def _dimension_facet_coverage(
    facets: Mapping[str, object],
    cards: Sequence[Mapping[str, object]],
) -> Dict[str, object]:
    requested = facets.get("dimensions")
    if not isinstance(requested, list) or not requested:
        return _facet_not_requested()
    requested_dimensions = [str(item) for item in requested if item]
    resolved: List[str] = []
    missing: List[str] = []
    evidence_ids: Set[str] = set()
    for dimension in requested_dimensions:
        matches = _dimension_column_ids(cards, dimension)
        if matches:
            resolved.extend(matches)
            evidence_ids.update(matches)
        else:
            missing.append(dimension)
    return {
        "required": True,
        "status": _coverage_status(resolved, [], missing),
        "requested": sorted(set(requested_dimensions)),
        "resolved": sorted(set(resolved)),
        "partial": [],
        "missing": sorted(set(missing)),
        "evidence_ids": sorted(evidence_ids),
    }


def _dimension_column_ids(cards: Sequence[Mapping[str, object]], dimension: str) -> List[str]:
    dimension_norm = _normalize_text(dimension)
    matches = []
    for card in cards:
        if str(card.get("card_type") or "") != "column":
            continue
        canonical_id = str(card.get("canonical_id") or "")
        candidates = [
            canonical_id,
            str(card.get("column_name") or ""),
            str(card.get("full_reference") or ""),
            str(card.get("name") or ""),
        ]
        if any(_normalize_text(candidate).endswith(dimension_norm) for candidate in candidates if candidate):
            matches.append(canonical_id)
            continue
        if any(_phrase_in_text(dimension_norm, _normalize_text(candidate)) for candidate in candidates if candidate):
            matches.append(canonical_id)
    return sorted(set(matches))


def _metric_facet_coverage(
    facets: Mapping[str, object],
    cards: Sequence[Mapping[str, object]],
) -> Dict[str, object]:
    requested = facets.get("metrics")
    if not isinstance(requested, list) or not requested:
        return _facet_not_requested()
    requested_metrics = [str(item) for item in requested if item]
    matched_by_metric: Dict[str, List[str]] = {}
    for metric in requested_metrics:
        matched_by_metric[metric] = [
            str(card.get("canonical_id"))
            for card in cards
            if str(card.get("card_type") or "") in {"metric", "metric_implementation"}
            and card.get("canonical_id")
            and _metric_card_matches_request(card, metric, cards)
        ]
    matched_ids = sorted({card_id for ids in matched_by_metric.values() for card_id in ids})
    derived = facets.get("derived_metrics")
    derived_names = {
        str(item.get("name"))
        for item in derived
        if isinstance(item, Mapping) and item.get("name")
    } if isinstance(derived, list) else set()

    resolved: List[str] = []
    partial: List[str] = []
    missing: List[str] = []
    for metric in requested_metrics:
        matches = matched_by_metric.get(metric, [])
        if matches and metric not in derived_names:
            resolved.extend(matches)
        elif matches:
            partial.extend(matches)
            missing.append(f"canonical_derived_metric:{metric}")
        elif metric in derived_names:
            partial.append(f"derived_metric:{metric}")
            missing.append(f"base_metric_evidence:{metric}")
        else:
            missing.append(f"metric_evidence:{metric}")

    if derived and not matched_ids:
        partial.extend(
            f"derived_metric:{item.get('name')}"
            for item in derived
            if isinstance(item, Mapping) and item.get("name")
        )
        if "derived_metric_canonical_evidence" not in missing:
            missing.append("derived_metric_canonical_evidence")
    return {
        "required": True,
        "status": _coverage_status(resolved, partial, missing),
        "requested": requested,
        "resolved": sorted(set(resolved)),
        "partial": sorted(set(partial)),
        "missing": sorted(set(missing)),
        "evidence_ids": matched_ids,
        "matched_by_metric": {
            metric: sorted(set(ids))
            for metric, ids in matched_by_metric.items()
            if ids
        },
    }


def _metric_card_matches_request(
    card: Mapping[str, object],
    requested_metric: str,
    selected_cards: Sequence[Mapping[str, object]],
) -> bool:
    if _normalize_text(str(requested_metric or "")) == "metric":
        return True
    request_terms = _semantic_label_terms(requested_metric)
    if not request_terms:
        return False

    candidates = _metric_semantic_candidates(card, selected_cards)
    return any(_semantic_terms_compatible(request_terms, candidate) for candidate in candidates)


def _metric_semantic_candidates(
    card: Mapping[str, object],
    selected_cards: Sequence[Mapping[str, object]],
) -> List[Set[str]]:
    candidates: List[Set[str]] = []
    for field in (
        "canonical_id",
        "name",
        "metric_name",
        "business_definition",
        "implementation_name",
        "display_name",
        "canonical_name",
        "description",
    ):
        candidates.append(_semantic_label_terms(card.get(field)))
    for alias_field in ("aliases", "colloquial_names"):
        aliases = card.get(alias_field)
        if isinstance(aliases, list):
            candidates.extend(_semantic_label_terms(alias) for alias in aliases)

    metric_id = str(card.get("metric_id") or "")
    if metric_id:
        candidates.append(_semantic_label_terms(metric_id))
        parent = _selected_card_by_id(selected_cards, metric_id)
        if parent:
            candidates.extend(_metric_semantic_candidates(parent, []))
    return [candidate for candidate in candidates if candidate]


def _selected_card_by_id(
    cards: Sequence[Mapping[str, object]],
    canonical_id: str,
) -> Optional[Mapping[str, object]]:
    for card in cards:
        if str(card.get("canonical_id") or "") == canonical_id:
            return card
    return None


def _semantic_label_terms(value: object) -> Set[str]:
    if value in (None, "", []):
        return set()
    text = str(value)
    if "." in text:
        text = text.split(".")[-1]
    tokens = set(_tokens(text.replace("_", " ").replace("-", " ")))
    return {
        token
        for token in tokens
        if token
        and token
        not in {
            "metric",
            "metric_impl",
            "implementation",
            "impl",
            "rate",
            "value",
            "amount",
            "the",
            "and",
            "or",
            "of",
        }
    }


def _semantic_terms_compatible(request_terms: Set[str], candidate_terms: Set[str]) -> bool:
    if not request_terms or not candidate_terms:
        return False
    return request_terms <= candidate_terms


def _filter_facet_coverage(
    facets: Mapping[str, object],
    scope_resolution: Mapping[str, object],
) -> Dict[str, object]:
    filters = facets.get("filters")
    if not isinstance(filters, Mapping) or not any(filters.values()):
        return _facet_not_requested()
    applied = scope_resolution.get("applied_filters")
    resolved = []
    if isinstance(applied, list):
        resolved = [
            f"{item.get('dimension')}={item.get('value')}"
            for item in applied
            if isinstance(item, Mapping)
        ]
    return {
        "required": False,
        "status": "resolved" if resolved else "missing",
        "requested": filters,
        "resolved": sorted(resolved),
        "partial": [],
        "missing": [] if resolved else ["scope_filters"],
        "evidence_ids": [
            str(item.get("canonical_id"))
            for item in applied
            if isinstance(item, Mapping) and item.get("canonical_id")
        ] if isinstance(applied, list) else [],
    }


def _time_period_facet_coverage(facets: Mapping[str, object]) -> Dict[str, object]:
    time_period = facets.get("time_period")
    output_types = facets.get("output_type")
    metrics = facets.get("metrics")
    requested_report = isinstance(output_types, list) and "summary_report" in output_types
    requested_metric = isinstance(metrics, list) and bool(metrics)
    if not isinstance(time_period, Mapping) or not time_period.get("requested"):
        return {
            "required": False,
            "status": "missing" if requested_report and requested_metric else "not_requested",
            "requested": [],
            "resolved": [],
            "partial": [],
            "missing": ["time_period"] if requested_report and requested_metric else [],
            "evidence_ids": [],
        }
    terms = [str(term) for term in time_period.get("terms", [])]
    return {
        "required": False,
        "status": "resolved" if terms else "missing",
        "requested": terms,
        "resolved": terms,
        "partial": [],
        "missing": [] if terms else ["time_period"],
        "evidence_ids": [],
    }


def _ranking_facet_coverage(facets: Mapping[str, object]) -> Dict[str, object]:
    ranking = facets.get("ranking")
    if not isinstance(ranking, list) or not ranking:
        return _facet_not_requested()
    return {
        "required": False,
        "status": "resolved",
        "requested": sorted(str(item) for item in ranking if item),
        "resolved": sorted(str(item) for item in ranking if item),
        "partial": [],
        "missing": [],
        "evidence_ids": [],
        "note": "Ranking intent is parsed for downstream SQL planning; retrieval does not implement ranking.",
    }


def _output_type_facet_coverage(facets: Mapping[str, object]) -> Dict[str, object]:
    output_types = facets.get("output_type")
    if not isinstance(output_types, list) or not output_types:
        return _facet_not_requested()
    return {
        "required": False,
        "status": "resolved",
        "requested": output_types,
        "resolved": output_types,
        "partial": [],
        "missing": [],
        "evidence_ids": [],
    }


def _requested_action_facet_coverage(facets: Mapping[str, object]) -> Dict[str, object]:
    action = str(facets.get("requested_action") or "")
    if not action:
        return _facet_not_requested()
    return {
        "required": False,
        "status": "resolved",
        "requested": [action],
        "resolved": [action],
        "partial": [],
        "missing": [],
        "evidence_ids": [],
    }


def _facet_not_requested() -> Dict[str, object]:
    return {
        "required": False,
        "status": "not_requested",
        "requested": [],
        "resolved": [],
        "partial": [],
        "missing": [],
        "evidence_ids": [],
    }


def _coverage_status(
    resolved: Sequence[str],
    partial: Sequence[str],
    missing: Sequence[str],
) -> str:
    if missing and (resolved or partial):
        return "partial"
    if missing:
        return "missing"
    if partial and not resolved:
        return "partial"
    if resolved:
        return "resolved"
    return "unsupported"


def _selected_ids_with_terms(
    cards: Sequence[Mapping[str, object]],
    terms: Set[str],
    card_types: Set[str],
) -> List[str]:
    ids = []
    for card in cards:
        if str(card.get("card_type") or "") not in card_types:
            continue
        text_tokens = set(_tokens(_searchable_text(card).replace("_", " ")))
        if terms <= text_tokens and card.get("canonical_id"):
            ids.append(str(card.get("canonical_id")))
    return ids


def _has_oms_marketplace_relationship(cards: Sequence[Mapping[str, object]]) -> bool:
    for card in cards:
        if str(card.get("card_type") or "") not in {"relationship", "table", "query_pattern", "rule"}:
            continue
        text_tokens = set(_tokens(_searchable_text(card).replace("_", " ")))
        if "oms" in text_tokens and text_tokens & {"marketplace", "marketplaces", "platform", "seller"}:
            return True
    return False


def _completeness_warnings(
    query: str,
    cards: Sequence[Mapping[str, object]],
    sql_context: Mapping[str, object],
    cards_by_id: Mapping[str, Mapping[str, object]],
    scope_resolution: Mapping[str, object],
    handoff_contract: Mapping[str, object],
) -> List[Dict[str, str]]:
    warnings: List[Dict[str, str]] = []
    card_types = {str(card.get("card_type")) for card in cards}
    query_tokens = set(_tokens(query))

    metric_impls = [
        card for card in cards if str(card.get("card_type")) == "metric_implementation"
    ]
    if (
        _mentions_metric_intent(query_tokens)
        and "metric_implementation" not in card_types
        and "reconciliation_profile" not in card_types
    ):
        warnings.append(
            {
                "severity": "blocking",
                "code": "missing_metric_implementation",
                "message": "Metric-like query did not resolve to a metric implementation card.",
            }
        )

    if metric_impls:
        for card in metric_impls:
            if not _formula_text(card):
                warnings.append(
                    {
                        "severity": "blocking",
                        "code": "missing_metric_formula",
                        "message": f"{card.get('canonical_id')} has no formula or SQL pattern context.",
                    }
                )
            if not _table_refs_for_card(card):
                warnings.append(
                    {
                        "severity": "warning",
                        "code": "missing_base_tables",
                        "message": f"{card.get('canonical_id')} has no base_tables; SQL generation must infer tables from formula text or ask for clarification.",
                    }
                )

    tables = sql_context.get("tables") or []
    if _mentions_sql_intent(query_tokens) and not tables and not sql_context.get("required_table_ids"):
        warnings.append(
            {
                "severity": "blocking",
                "code": "missing_table_context",
                "message": "No table context resolved for a SQL-generation query.",
            }
        )

    unresolved = sql_context.get("unresolved_table_refs") or []
    for table_ref in unresolved if isinstance(unresolved, list) else []:
        if table_ref not in cards_by_id:
            warnings.append(
                {
                    "severity": "warning",
                    "code": "unresolved_table_reference",
                    "message": f"Referenced base table is not present as a canonical table card: {table_ref}.",
                }
            )

    if _mentions_tenant_scope(query_tokens) and not sql_context.get("account_data_bindings"):
        warnings.append(
            {
                "severity": "warning",
                "code": "tenant_scope_not_bound",
                "message": "Query appears tenant/account scoped but no account data binding was selected.",
            }
        )

    required_scope = handoff_contract.get("required_scope")
    if isinstance(required_scope, Mapping):
        tenant_scope = required_scope.get("tenant")
        if isinstance(tenant_scope, Mapping) and tenant_scope.get("required") and not tenant_scope.get("resolved"):
            warnings.append(
                {
                    "severity": "blocking",
                    "code": "missing_required_tenant_scope",
                    "message": "Scoped product SQL query requires a resolved tenant scope.",
                }
            )

    binding_coverage = handoff_contract.get("binding_coverage")
    if isinstance(binding_coverage, Mapping):
        if binding_coverage.get("required") and not binding_coverage.get("matching_binding_ids"):
            warnings.append(
                {
                    "severity": "blocking",
                    "code": "missing_account_data_binding",
                    "message": "Scoped SQL handoff has no account data binding matching the resolved tenant/platform/account scope.",
                }
            )
        table_bindings = binding_coverage.get("required_table_bindings")
        if isinstance(table_bindings, list):
            for item in table_bindings:
                if isinstance(item, Mapping) and item.get("required") and not item.get("binding_ids"):
                    warnings.append(
                        {
                            "severity": "warning",
                            "code": "table_without_binding",
                            "message": f"Required table {item.get('table_id')} has no matching account data binding in the selected context.",
                        }
                    )

    business_flow_coverage = handoff_contract.get("business_flow_coverage")
    if isinstance(business_flow_coverage, Mapping):
        if business_flow_coverage.get("required") and not business_flow_coverage.get("selected_flow_evidence_ids"):
            warnings.append(
                {
                    "severity": "blocking",
                    "code": "missing_business_flow_binding",
                    "message": "Cross-platform SQL handoff requires selected business flow evidence for the involved platforms.",
                }
            )

    reconciliation_coverage = handoff_contract.get("reconciliation_coverage")
    if isinstance(reconciliation_coverage, Mapping) and reconciliation_coverage.get("required"):
        missing_parts = reconciliation_coverage.get("missing")
        if isinstance(missing_parts, list) and missing_parts:
            warnings.append(
                {
                    "severity": "blocking",
                    "code": "incomplete_reconciliation_profile",
                    "message": "Reconciliation SQL handoff is missing profile completeness evidence: "
                    + ", ".join(str(part) for part in missing_parts),
                }
            )

    intent_coverage = handoff_contract.get("intent_coverage")
    if isinstance(intent_coverage, Mapping):
        missing_facets = intent_coverage.get("missing_required_facets")
        if isinstance(missing_facets, list) and missing_facets:
            warnings.append(
                {
                    "severity": "blocking",
                    "code": "incomplete_intent_coverage",
                    "message": "Compound request is missing required facet coverage: "
                    + ", ".join(str(facet) for facet in missing_facets),
                }
            )
        facets = intent_coverage.get("facets")
        if isinstance(facets, Mapping):
            dimensions = facets.get("dimensions")
            if isinstance(dimensions, Mapping) and dimensions.get("status") in {"missing", "partial"}:
                warnings.append(
                    {
                        "severity": "blocking",
                        "code": "dimension_column_not_resolved",
                        "message": "Requested dimension facet did not resolve to canonical column evidence.",
                    }
                )
            metrics = facets.get("metrics")
            if isinstance(metrics, Mapping) and metrics.get("status") in {"missing", "unsupported"}:
                warnings.append(
                    {
                        "severity": "blocking",
                        "code": "metric_not_resolved",
                        "message": "Requested metric facet did not resolve to canonical metric evidence.",
                    }
                )
            if isinstance(metrics, Mapping) and metrics.get("status") == "partial":
                warnings.append(
                    {
                        "severity": "warning",
                        "code": "derived_metric_inferred_without_card",
                        "message": "A derived metric requirement was inferred, but canonical implementation evidence is incomplete.",
                    }
                )

    dependencies = handoff_contract.get("metric_dependencies")
    if isinstance(dependencies, list):
        for item in dependencies:
            if not isinstance(item, Mapping):
                continue
            if item.get("requires_tables") and not item.get("required_table_ids"):
                warnings.append(
                    {
                        "severity": "warning",
                        "code": "metric_tables_not_resolved",
                        "message": f"{item.get('metric_implementation_id')} did not resolve required table IDs.",
                    }
                )
            if item.get("requires_columns") and not item.get("required_columns"):
                warnings.append(
                    {
                        "severity": "warning",
                        "code": "metric_columns_not_resolved",
                        "message": f"{item.get('metric_implementation_id')} did not expose required columns from formula context.",
                    }
                )

    for ambiguity in scope_resolution.get("ambiguous_filters", []):
        if isinstance(ambiguity, Mapping):
            warnings.append(
                {
                    "severity": "warning",
                    "code": "ambiguous_scope_filter",
                    "message": f"Scope hint {ambiguity.get('dimension')}={ambiguity.get('value')} matched multiple canonical options.",
                }
            )

    return warnings


def _cognee_candidate_warnings(cognee_candidates: Mapping[str, object]) -> List[Dict[str, str]]:
    warnings: List[Dict[str, str]] = []
    unrecognized = cognee_candidates.get("unrecognized_canonical_mentions")
    if isinstance(unrecognized, list):
        for item in unrecognized:
            if not isinstance(item, Mapping):
                continue
            warnings.append(
                {
                    "severity": "warning",
                    "code": "candidate_not_canonical",
                    "message": f"Cognee mentioned an unknown canonical-looking ID: {item.get('canonical_id')}.",
                }
            )
    excluded = cognee_candidates.get("excluded_by_scope")
    if isinstance(excluded, list) and excluded:
        warnings.append(
            {
                "severity": "warning",
                "code": "tenant_scope_over_retrieved",
                "message": "Cognee returned candidates that were excluded by tenant/platform/account scope.",
            }
        )
    return warnings


def _selected_edges(
    edges: Sequence[Mapping[str, object]],
    selected_ids: Set[str],
) -> List[Mapping[str, object]]:
    selected = [
        edge
        for edge in edges
        if str(edge.get("source_id")) in selected_ids and str(edge.get("target_id")) in selected_ids
    ]
    return sorted(
        selected,
        key=lambda edge: (
            str(edge.get("source_id")),
            str(edge.get("edge_type")),
            str(edge.get("target_id")),
        ),
    )


def _ordered_card_ids(
    seed_ids: Sequence[str],
    expanded_ids: Set[str],
    cards_by_id: Mapping[str, Mapping[str, object]],
    max_cards: int,
) -> List[str]:
    seed_order = {card_id: index for index, card_id in enumerate(seed_ids)}
    seed_set = set(seed_ids)
    return sorted(
        (
            card_id
            for card_id in expanded_ids
            if card_id in cards_by_id
            and (
                card_id in seed_set
                or str(cards_by_id[card_id].get("card_type")) in SQL_RELEVANT_CARD_TYPES
                or str(cards_by_id[card_id].get("card_type")) in SCOPE_CARD_TYPES
            )
        ),
        key=lambda card_id: (
            0 if card_id in seed_set else 1,
            seed_order.get(card_id, 999999),
            str(cards_by_id[card_id].get("card_type")),
            card_id,
        ),
    )[:max_cards]


def _cognee_candidate_records(
    discovered_candidate_ids: Sequence[str],
    accepted_candidate_ids: Sequence[str],
    cards_by_id: Mapping[str, Mapping[str, object]],
    outgoing: Mapping[str, Sequence[Mapping[str, object]]],
    incoming: Mapping[str, Sequence[Mapping[str, object]]],
    scope_constraints: Mapping[str, Set[str]],
    candidate_facets: Optional[Mapping[str, Sequence[str]]] = None,
    unrecognized_mentions: Optional[Sequence[str]] = None,
) -> Dict[str, List[Dict[str, object]]]:
    accepted_set = set(accepted_candidate_ids)
    candidate_facets = candidate_facets or {}
    accepted: List[Dict[str, object]] = []
    excluded: List[Dict[str, object]] = []
    seen: Set[str] = set()
    for card_id in discovered_candidate_ids:
        if card_id in seen:
            continue
        seen.add(card_id)
        card = cards_by_id.get(card_id)
        if not card:
            continue
        if card_id in accepted_set:
            accepted.append(
                _cognee_candidate_record(
                    card,
                    "accepted",
                    outgoing,
                    incoming,
                    candidate_facets.get(card_id, []),
                )
            )
        elif not _card_scope_compatible(card, scope_constraints):
            excluded.append(
                _cognee_candidate_record(
                    card,
                    "excluded_by_scope",
                    outgoing,
                    incoming,
                    candidate_facets.get(card_id, []),
                )
            )
    return {
        "accepted": accepted,
        "excluded_by_scope": excluded,
        "unrecognized_canonical_mentions": [
            {
                "canonical_id": mention,
                "validation_status": "unresolved_candidate",
                "warning": "Cognee mentioned a canonical-looking ID that is not present in canonical cards.",
            }
            for mention in sorted(set(unrecognized_mentions or []))
        ],
    }


def _cognee_candidate_record(
    card: Mapping[str, object],
    scope_status: str,
    outgoing: Mapping[str, Sequence[Mapping[str, object]]],
    incoming: Mapping[str, Sequence[Mapping[str, object]]],
    facets: Sequence[str] = (),
) -> Dict[str, object]:
    canonical_id = str(card.get("canonical_id") or "")
    card_type = str(card.get("card_type") or "")
    record: Dict[str, object] = {
        "canonical_id": canonical_id,
        "card_type": card_type,
        "scope_status": scope_status,
        "validation_status": "canonical_resolved" if scope_status == "accepted" else "rejected",
    }
    if facets:
        record["facets"] = sorted(set(str(facet) for facet in facets if facet))
    for key in (
        "name",
        "metric_name",
        "business_definition",
        "implementation_name",
        "metric_id",
        "base_tables",
        "source_tables",
        "source_columns",
        "required_filters",
        "filters",
        "table_name",
        "full_reference",
        "column_name",
        "binding_name",
        "tenant_name",
        "group_name",
        "platform_name",
        "account_name",
    ):
        value = card.get(key)
        if value not in (None, "", []):
            record[key] = value

    aliases = card.get("aliases")
    if isinstance(aliases, list) and aliases:
        record["aliases"] = aliases[:5]

    formula_text = _formula_text(card)
    if formula_text:
        record["formula_preview"] = _truncate_text(formula_text, 320)
        columns = _columns_from_formula(formula_text)
        filters = _filters_from_formula(formula_text)
        if columns:
            record["formula_columns"] = columns
        if filters:
            record["formula_filters"] = filters

    relationship_ids = _candidate_relationship_ids(canonical_id, outgoing, incoming)
    if relationship_ids:
        record["related_canonical_ids"] = relationship_ids[:12]

    source_documents = card.get("source_documents")
    if isinstance(source_documents, list) and source_documents:
        record["source_documents"] = source_documents[:3]
    return record


def _candidate_relationship_ids(
    canonical_id: str,
    outgoing: Mapping[str, Sequence[Mapping[str, object]]],
    incoming: Mapping[str, Sequence[Mapping[str, object]]],
) -> List[str]:
    related: List[str] = []
    for edge in outgoing.get(canonical_id, []):
        target_id = str(edge.get("target_id") or "")
        if target_id and target_id not in related:
            related.append(target_id)
    for edge in incoming.get(canonical_id, []):
        source_id = str(edge.get("source_id") or "")
        if source_id and source_id not in related:
            related.append(source_id)
    return related


def _formula_text(card: Mapping[str, object]) -> str:
    for field in FORMULA_TEXT_FIELDS:
        value = card.get(field)
        if value in (None, "", []):
            continue
        return _sanitize_formula_text(str(value))
    return ""


def _sanitize_formula_text(value: str) -> str:
    without_block_comments = re.sub(r"/\*.*?\*/", "", value, flags=re.DOTALL)
    lines = []
    for line in without_block_comments.splitlines():
        if "--" in line:
            line = line.split("--", 1)[0]
        stripped = line.rstrip()
        if stripped:
            lines.append(stripped)
    return "\n".join(lines).strip()


def _table_refs_for_card(card: Mapping[str, object]) -> List[str]:
    refs: List[str] = []
    for field in ("base_tables", "source_table_id", "source_tables", "tables", "table_id"):
        for ref in _iter_reference_values(card.get(field)):
            for candidate in _table_ref_candidates(ref):
                if candidate not in refs:
                    refs.append(candidate)
    return refs


def _table_ref_candidates(ref: str) -> List[str]:
    value = str(ref).strip()
    if not value:
        return []
    candidates = [value]
    if "." in value and not value.startswith("table."):
        candidates.append(f"table.{value}")
    return candidates


def _truncate_text(text: str, max_length: int) -> str:
    normalized = " ".join(str(text).split())
    if len(normalized) <= max_length:
        return normalized
    return normalized[: max_length - 3].rstrip() + "..."


def _card_record(card: Mapping[str, object]) -> Dict[str, object]:
    keep = (
        "canonical_id",
        "card_type",
        "name",
        "display_name",
        "canonical_name",
        "description",
        "status",
        "confidence",
        "review_status",
        "source_documents",
        "tags",
        "colloquial_names",
        "evidence_refs",
        "table_name",
        "full_reference",
        "column_name",
        "metric_name",
        "business_definition",
        "implementation_name",
        "metric_id",
        "base_tables",
        "formula_description",
        "formula_sql",
        "binding_name",
        "tenant_name",
        "group_name",
        "platform_name",
        "account_name",
        "scope_name",
        "profile_name",
        "category_name",
        "rule_name",
        "test_name",
    )
    record = {key: card[key] for key in keep if key in card and card[key] not in (None, "", [])}
    evidence_refs = record.get("evidence_refs")
    if isinstance(evidence_refs, list):
        record["evidence_refs"] = evidence_refs[:5]
    return record


def _compact_records(value: object, limit: int) -> List[Dict[str, object]]:
    if not isinstance(value, list):
        return []
    compact: List[Dict[str, object]] = []
    keep = (
        "canonical_id",
        "card_type",
        "name",
        "display_name",
        "canonical_name",
        "colloquial_names",
        "metric_name",
        "metric_id",
        "implementation_name",
        "base_tables",
        "source_tables",
        "source_columns",
        "required_filters",
        "filters",
        "formula_preview",
        "formula_columns",
        "formula_filters",
        "formula_description",
        "formula_sql",
        "binding_name",
        "table_name",
        "full_reference",
        "column_name",
        "table_id",
        "profile_name",
        "variant_name",
        "rule_name",
        "pattern_name",
        "sql_ref",
        "sql_pattern_id",
        "sql_pattern_ref",
    )
    for item in value[:limit]:
        if not isinstance(item, Mapping):
            continue
        record = {
            key: _truncate_compact_value(item[key])
            for key in keep
            if key in item and item[key] not in (None, "", [])
        }
        if record:
            compact.append(record)
    return compact


def _compact_warnings(bundle: Mapping[str, object]) -> List[Dict[str, object]]:
    return [
        {
            "severity": warning.get("severity"),
            "code": warning.get("code"),
            "message": warning.get("message"),
        }
        for warning in _warnings(bundle)
    ]


def _warnings(bundle: Mapping[str, object]) -> List[Mapping[str, object]]:
    warnings = bundle.get("completeness_warnings")
    if not isinstance(warnings, list):
        return []
    return [warning for warning in warnings if isinstance(warning, Mapping)]


def _truncate_compact_value(value: object) -> object:
    if isinstance(value, str):
        return value if len(value) <= 320 else value[:317].rstrip() + "..."
    if isinstance(value, list):
        return value[:12]
    return value


def _paraphrased_request(query: str, metadata_filters: Mapping[str, object]) -> str:
    hints = metadata_filters.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}
    tenant_codes = _hint_values(hints, "tenant_codes")
    platform_codes = _hint_values(hints, "platform_codes")
    query_tokens = set(_tokens(query))

    scope_text = ""
    if tenant_codes:
        scope_text = f" for tenant {', '.join(sorted(tenant_codes))}"
    platform_text = ""
    if platform_codes:
        platform_text = f" across {', '.join(sorted(platform_codes))}"

    if {"seller", "realization", "rate"} <= query_tokens and "oms" in query_tokens:
        return (
            "Generate a compact SQL-ready summary of OMS/source systems and connected marketplaces"
            f"{scope_text}{platform_text} for seller realization rate, using only canonical metric, "
            "table, account binding, and relationship evidence."
        )
    if {"seller", "realization", "rate"} <= query_tokens:
        return (
            "Generate a compact SQL-ready summary"
            f"{scope_text}{platform_text} for seller realization rate, using canonical metric "
            "implementations and account binding evidence."
        )
    return f"Prepare a compact SQL-ready handoff{scope_text}{platform_text}: {query}"


def _sql_card_record(card: Mapping[str, object]) -> Dict[str, object]:
    record = _card_record(card)
    evidence_refs = record.get("evidence_refs")
    if isinstance(evidence_refs, list):
        record["evidence_refs"] = evidence_refs[:5]
    for formula_field in ("formula_sql", "formula_description"):
        if formula_field in record:
            sanitized = _sanitize_formula_text(str(record[formula_field]))
            if sanitized:
                record[formula_field] = sanitized
            else:
                record.pop(formula_field, None)
    for key in (
        "display_name",
        "source_tables",
        "source_columns",
        "required_filters",
        "filters",
        "sql_ref",
        "sql_pattern_id",
        "sql_pattern_ref",
    ):
        value = card.get(key)
        if value not in (None, "", []):
            record[key] = value
    formula_text = _formula_text(card)
    if formula_text:
        record["formula_preview"] = _truncate_text(formula_text, 640)
        columns = _columns_from_formula(formula_text)
        filters = _filters_from_formula(formula_text)
        if columns:
            record["formula_columns"] = columns
        if filters:
            record["formula_filters"] = filters
    return record


def _edge_record(edge: Mapping[str, object]) -> Dict[str, object]:
    keep = ("source_id", "edge_type", "target_id", "confidence", "review_status", "evidence_refs")
    return {key: edge[key] for key in keep if key in edge and edge[key] not in (None, "", [])}


def _edges_by(
    edges: Iterable[Mapping[str, object]],
    key: str,
) -> DefaultDict[str, List[Mapping[str, object]]]:
    grouped: DefaultDict[str, List[Mapping[str, object]]] = defaultdict(list)
    for edge in edges:
        value = edge.get(key)
        if value:
            grouped[str(value)].append(edge)
    return grouped


def _searchable_text(card: Mapping[str, object]) -> str:
    values: List[str] = []
    for field in SEARCH_FIELDS:
        value = card.get(field)
        if value in (None, "", []):
            continue
        if isinstance(value, list):
            values.extend(str(item) for item in value)
        else:
            values.append(str(value))
    return " ".join(values)


def _tokens(text: str) -> List[str]:
    return [token for token in re.findall(r"[a-z0-9_]+", text.lower()) if len(token) > 1]


def _normalize_text(text: str) -> str:
    return " ".join(_tokens(text))


def _mentions_sql_intent(tokens: Set[str]) -> bool:
    return bool(tokens & {"sql", "query", "table", "column", "join", "metric", "gmv", "recon", "reconciliation"})


def _mentions_metric_intent(tokens: Set[str]) -> bool:
    return bool(tokens & {"metric", "gmv", "rate", "ratio", "amount", "revenue", "sales", "settlement", "payout", "realization"})


def _mentions_tenant_scope(tokens: Set[str]) -> bool:
    return bool(tokens & {"tenant", "account", "binding", "nimbus", "prism", "bank", "seller"})


def _mentions_cross_platform_flow(tokens: Set[str]) -> bool:
    return bool(
        tokens
        & {
            "awb",
            "bank",
            "bridge",
            "cod",
            "compare",
            "courier",
            "cross",
            "delivery",
            "flow",
            "freight",
            "join",
            "logistics",
            "match",
            "payout",
            "recon",
            "reconcile",
            "reconciliation",
            "remittance",
            "settlement",
            "shipment",
            "shipping",
            "utr",
            "vs",
        }
    )


def _requires_reconciliation_profile(tokens: Set[str]) -> bool:
    if not (tokens & {"recon", "reconcile", "reconciliation", "mismatch", "playbook", "exception"}):
        return False
    return bool(tokens & {"profile", "variant", "mismatch", "playbook", "cod", "freight", "invoice", "bank", "awb", "exception"})


def _requires_tenant_scope(tokens: Set[str]) -> bool:
    return bool(tokens & {"my", "our", "tenant"}) and (
        _mentions_sql_intent(tokens) or _mentions_metric_intent(tokens)
    )


def _platform_hints(tokens: Set[str]) -> Set[str]:
    hints: Set[str] = set()
    for token, aliases in PLATFORM_HINTS.items():
        if token in tokens:
            hints.update(aliases)
    return hints


def _hint_values(hints: Mapping[str, object], key: str) -> Set[str]:
    value = hints.get(key)
    if not isinstance(value, list):
        return set()
    return {str(item) for item in value if item not in (None, "")}


def _columns_from_formula(formula_text: str) -> List[str]:
    columns = {
        f"{table}.{column}"
        for table, column in re.findall(
            r"\b([a-zA-Z][a-zA-Z0-9_]*)\.([a-zA-Z][a-zA-Z0-9_]*)\b",
            formula_text,
        )
    }
    columns.update(_bare_columns_from_formula(formula_text))
    return sorted(columns)


def _filters_from_formula(formula_text: str) -> List[str]:
    filters: Set[str] = set()
    for pattern in (
        r"\bis_active\s*=\s*(?:true|false)",
        r"\btransaction_type\s*=\s*'[^']+'",
        r"\btype\s*=\s*'[^']+'",
        r"\bgroup_level_id\s*=\s*\d+",
        r"\b[a-zA-Z][a-zA-Z0-9_]*\s*=\s*(?:'[^']+'|true|false|\d+(?:\.\d+)?)",
        r"\b[a-zA-Z][a-zA-Z0-9_]*\s+IN\s*\([^)]*\)",
    ):
        filters.update(match.group(0) for match in re.finditer(pattern, formula_text, flags=re.IGNORECASE))
    return sorted(filters)


def _bare_columns_from_formula(formula_text: str) -> Set[str]:
    text = _strip_sql_literals(_sanitize_formula_text(formula_text))
    skip = {
        "and",
        "as",
        "asc",
        "avg",
        "by",
        "case",
        "cast",
        "coalesce",
        "count",
        "count_if",
        "date_trunc",
        "desc",
        "distinct",
        "else",
        "end",
        "false",
        "from",
        "group",
        "in",
        "is",
        "left",
        "lower",
        "null",
        "nullif",
        "on",
        "or",
        "order",
        "round",
        "select",
        "sum",
        "then",
        "true",
        "union",
        "upper",
        "when",
        "where",
    }
    columns: Set[str] = set()
    for match in re.finditer(r"\b[a-zA-Z][a-zA-Z0-9_]*\b", text):
        token = match.group(0)
        lowered = token.lower()
        if lowered in skip:
            continue
        before = text[: match.start()].rstrip()
        after = text[match.end():].lstrip()
        if before.endswith(".") or after.startswith("."):
            continue
        previous_word = re.search(r"\b([a-zA-Z][a-zA-Z0-9_]*)\s*$", before)
        if previous_word and previous_word.group(1).lower() == "as":
            continue
        columns.add(token)
    return columns


def _strip_sql_literals(value: str) -> str:
    return re.sub(r"'(?:''|[^'])*'", "''", value)


def _binding_matches_scope(
    binding: Mapping[str, object],
    tenant_codes: Set[str],
    platform_codes: Set[str],
    account_codes: Set[str],
) -> bool:
    binding_scope = _card_scope(binding)
    if tenant_codes and binding_scope.get("tenant") and not (binding_scope["tenant"] & tenant_codes):
        return False
    if platform_codes and binding_scope.get("platform") and not (binding_scope["platform"] & platform_codes):
        return False
    if account_codes and binding_scope.get("account") and not (binding_scope["account"] & account_codes):
        return False
    return True


def _binding_covers_table(
    binding: Mapping[str, object],
    table: Optional[Mapping[str, object]],
) -> bool:
    if table is None:
        return False
    binding_scope = _card_scope(binding)
    table_scope = _card_scope(table)
    if table_scope.get("platform") and binding_scope.get("platform"):
        return bool(table_scope["platform"] & binding_scope["platform"])
    table_name = _normalize_text(str(table.get("table_name") or table.get("name") or ""))
    binding_name = _normalize_text(str(binding.get("binding_name") or binding.get("name") or ""))
    return bool(table_name and binding_name and table_name in binding_name)


def _involved_platform_codes(
    cards: Sequence[Mapping[str, object]],
    scope_resolution: Mapping[str, object],
) -> Set[str]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        hints = {}
    platforms = set(_hint_values(hints, "platform_codes"))
    if platforms:
        return {code for code in platforms if code}
    for card in cards:
        platforms.update(_card_scope(card).get("platform", set()))
    return {code for code in platforms if code}


def _is_flow_evidence_card(
    card: Mapping[str, object],
    primary_platforms: Set[str],
) -> bool:
    card_type = str(card.get("card_type") or "")
    if card_type not in FLOW_EVIDENCE_CARD_TYPES:
        return False
    card_platforms = {_primary_platform_code(code) for code in _card_scope(card).get("platform", set())}
    if len(card_platforms & primary_platforms) < 2:
        return False
    if card_type == "table" and not _looks_like_flow_relation(card):
        return False
    return True


def _looks_like_flow_relation(card: Mapping[str, object]) -> bool:
    text = _normalize_text(
        " ".join(
            str(card.get(field) or "")
            for field in ("canonical_id", "name", "description", "table_name", "full_reference")
        )
    )
    return any(
        token in text
        for token in (
            " to ",
            "bridge",
            "cross",
            "flow",
            "join",
            "relationship",
            "reconciliation",
        )
    )


def _primary_platform_code(code: str) -> str:
    if code.endswith("_in"):
        code = code[:-3]
    if code == "nykaa_fashion":
        return "nykaa"
    if code in {"hdfc_bank", "icici_bank"}:
        return code
    return code


def _selected_reconciliation_text(cards: Sequence[Mapping[str, object]]) -> str:
    fields = (
        "canonical_id",
        "name",
        "description",
        "profile_name",
        "variant_name",
        "category_name",
        "rule_name",
        "test_name",
        "table_name",
        "full_reference",
    )
    parts: List[str] = []
    for card in cards:
        card_type = str(card.get("card_type") or "")
        if card_type not in {
            "column",
            "matching_logic",
            "mismatch_category",
            "query_pattern",
            "reconciliation_profile",
            "reconciliation_side",
            "reconciliation_unit",
            "reconciliation_variant",
            "relationship",
            "rule",
            "table",
            "validation_test",
        }:
            continue
        for field in fields:
            value = card.get(field)
            if isinstance(value, str) and value:
                parts.append(value)
    return " ".join(parts)


def _reconciliation_sides(
    cards: Sequence[Mapping[str, object]],
    evidence_text: str,
) -> Set[str]:
    sides = {
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") == "reconciliation_side" and card.get("canonical_id")
    }
    text = _normalize_text(evidence_text.replace("_", " "))
    side_patterns = {
        "shipment": ("shipment", "shiprocket oms", "logistics shipment", "awb"),
        "invoice": ("invoice", "freight invoice", "courier bill"),
        "cod_remittance": ("cod remittance", "cod settlement", "settlement"),
        "bank_credit": ("bank credit", "bank statement", "bank"),
        "marketplace_settlement": ("marketplace settlement", "amazon settlement", "flipkart settlement", "settlement"),
        "order": ("order", "oms", "channel order"),
    }
    for side, phrases in side_patterns.items():
        if any(_phrase_in_text(_normalize_text(phrase), text) for phrase in phrases):
            sides.add(side)
    return sides


def _reconciliation_units(
    cards: Sequence[Mapping[str, object]],
    evidence_text: str,
) -> Set[str]:
    units = {
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") == "reconciliation_unit" and card.get("canonical_id")
    }
    text = _normalize_text(evidence_text.replace("_", " "))
    unit_patterns = {
        "awb": ("awb", "awbs", "waybill", "waybills", "tracking id", "tracking", "cod remittance", "cod settlement", "shipment to cod settlement"),
        "order_id": ("order id", "order"),
        "utr": ("utr", "bank reference", "remittance reference"),
        "batch": ("batch", "batch reference"),
        "amount_date_bank_account": ("amount date bank account", "amount", "date", "bank account"),
    }
    for unit, phrases in unit_patterns.items():
        if any(_phrase_in_text(_normalize_text(phrase), text) for phrase in phrases):
            units.add(unit)
    return units


def _reconciliation_matching_logic_ids(
    cards: Sequence[Mapping[str, object]],
    evidence_text: str,
) -> Set[str]:
    ids = {
        str(card.get("canonical_id"))
        for card in cards
        if str(card.get("card_type") or "") in {"matching_logic", "relationship"}
        and card.get("canonical_id")
    }
    text = _normalize_text(evidence_text.replace("_", " "))
    if any(token in text for token in (" join ", " matching ", " matched ", " reconcile ", " to ")):
        ids.add("inferred_from_selected_reconciliation_text")
    if "awb" in text and ("invoice" in text or "settlement" in text):
        ids.add("awb_based_matching")
    if "utr" in text or "bank reference" in text:
        ids.add("utr_based_matching")
    return ids


def _mismatch_category_ids_from_text(evidence_text: str) -> List[str]:
    found = {
        f"mismatch_category.{match}"
        for match in re.findall(r"mismatch_category\.([a-z0-9_]+)", evidence_text.lower())
    }
    text = _normalize_text(evidence_text.replace("_", " "))
    keyword_map = {
        "mismatch_category.missing_invoice": ("missing invoice", "uninvoiced"),
        "mismatch_category.orphan_invoice": ("orphan invoice", "invoice without shipment"),
        "mismatch_category.freight_amount_mismatch": ("freight amount mismatch",),
        "mismatch_category.cod_amount_mismatch": ("cod amount mismatch",),
        "mismatch_category.missing_cod_remittance": ("missing cod remittance", "cod not remitted"),
        "mismatch_category.unidentified_bank_credit": ("unidentified bank credit",),
        "mismatch_category.grain_mismatch": ("grain mismatch", "batch grain"),
        "mismatch_category.schema_only_source": ("schema only",),
    }
    for mismatch_id, phrases in keyword_map.items():
        if any(_phrase_in_text(_normalize_text(phrase), text) for phrase in phrases):
            found.add(mismatch_id)
    return sorted(found)


def _resolve_scope(
    query: str,
    cards: Sequence[Mapping[str, object]],
    *,
    scope_overrides: Optional[Mapping[str, str]] = None,
) -> Dict[str, object]:
    query_norm = _normalize_text(query)
    raw_matches = {
        "tenants": _matched_scope_entities(query_norm, cards, "tenant"),
        "groups": _matched_scope_entities(query_norm, cards, "group"),
        "platforms": _matched_scope_entities(query_norm, cards, "platform"),
        "accounts": _matched_scope_entities(query_norm, cards, "account"),
    }
    raw_matches["platforms"] = _merge_scope_matches(
        raw_matches["platforms"],
        _static_platform_matches(query_norm),
    )
    explicit_matches = _explicit_scope_matches(cards, scope_overrides or {})
    for key, matches in explicit_matches.items():
        raw_matches[key] = _merge_scope_matches(raw_matches[key], matches)

    narrowed_accounts = _narrow_account_matches(
        raw_matches["accounts"],
        raw_matches["tenants"],
        raw_matches["platforms"],
    )
    raw_matches["accounts"] = narrowed_accounts["matches"]

    derived_tenant_codes = {
        str(match.get("tenant_code"))
        for match in raw_matches["accounts"]
        if match.get("tenant_code")
    }
    derived_tenant_codes.update(
        _tenant_short_code(str(match.get("code")))
        for match in raw_matches["groups"]
        if match.get("code")
    )
    derived_platform_codes = {
        code
        for match in raw_matches["accounts"]
        for code in _platform_scope_codes(str(match.get("platform_code") or ""))
        if code
    }

    query_hints = {
        "tenant_codes": sorted(
            {
                code
                for match in raw_matches["tenants"]
                for code in (str(match["code"]), _tenant_short_code(str(match["code"])))
            }
            | derived_tenant_codes
        ),
        "group_codes": sorted({str(match["code"]) for match in raw_matches["groups"]}),
        "platform_codes": sorted(
            {
                code
                for match in raw_matches["platforms"]
                for code in _platform_scope_codes(str(match["code"]))
            }
            | derived_platform_codes
        ),
        "account_codes": sorted({str(match["account_code"]) for match in raw_matches["accounts"]}),
    }
    applied_filters: List[Dict[str, object]] = []
    for dimension, matches in raw_matches.items():
        for match in matches:
            applied_filters.append(
                {
                    "dimension": dimension[:-1] if dimension.endswith("s") else dimension,
                    "value": match.get("code") or match.get("account_code"),
                    "canonical_id": match.get("canonical_id"),
                    "matched_alias": match.get("matched_alias"),
                    "source": match.get("source", "query"),
                }
            )

    return {
        "query_hints": query_hints,
        "applied_filters": sorted(
            applied_filters,
            key=lambda item: (
                str(item.get("dimension")),
                str(item.get("value")),
                str(item.get("canonical_id")),
            ),
        ),
        "ambiguous_filters": narrowed_accounts["ambiguous_filters"],
        "unresolved_filters": [],
    }


def _explicit_scope_matches(
    cards: Sequence[Mapping[str, object]],
    scope_overrides: Mapping[str, str],
) -> Dict[str, List[Dict[str, object]]]:
    matches = {"tenants": [], "groups": [], "platforms": [], "accounts": []}
    dimension_map = {
        "tenant": ("tenant", "tenants"),
        "group": ("group", "groups"),
        "platform": ("platform", "platforms"),
        "account": ("account", "accounts"),
    }
    for override_key, raw_value in scope_overrides.items():
        if raw_value in (None, ""):
            continue
        dimension, match_key = dimension_map[override_key]
        value = str(raw_value)
        for entity in _scope_entities(cards, dimension):
            if _scope_override_matches(value, entity):
                match = dict(entity)
                match["matched_alias"] = value
                match["source"] = "explicit"
                matches[match_key].append(match)
                break
    return matches


def _merge_scope_matches(
    query_matches: Sequence[Mapping[str, object]],
    explicit_matches: Sequence[Mapping[str, object]],
) -> List[Dict[str, object]]:
    merged: Dict[Tuple[str, str], Dict[str, object]] = {}
    for match in list(query_matches) + list(explicit_matches):
        key = (str(match.get("canonical_id")), str(match.get("code") or match.get("account_code")))
        if key not in merged or match.get("source") == "explicit":
            merged[key] = dict(match)
    return sorted(
        merged.values(),
        key=lambda item: (
            str(item.get("code") or item.get("account_code")),
            str(item.get("canonical_id")),
        ),
    )


def _scope_override_matches(value: str, entity: Mapping[str, object]) -> bool:
    value_norm = _normalize_text(value)
    if value == entity.get("canonical_id"):
        return True
    candidates = {
        str(entity.get("code") or ""),
        str(entity.get("account_code") or ""),
        str(entity.get("canonical_id") or ""),
    }
    candidates.update(str(alias) for alias in entity.get("aliases", set()))
    return any(value_norm == _normalize_text(candidate) for candidate in candidates if candidate)


def _matched_scope_entities(
    query_norm: str,
    cards: Sequence[Mapping[str, object]],
    dimension: str,
) -> List[Dict[str, object]]:
    matches: List[Dict[str, object]] = []
    seen: Set[Tuple[str, str]] = set()
    for entity in _scope_entities(cards, dimension):
        for alias in entity["aliases"]:
            alias_norm = _normalize_text(str(alias))
            if not alias_norm:
                continue
            if _phrase_in_text(alias_norm, query_norm):
                key = (str(entity["canonical_id"]), str(entity.get("code") or entity.get("account_code")))
                if key in seen:
                    continue
                seen.add(key)
                match = dict(entity)
                match["matched_alias"] = alias
                matches.append(match)
                break
    return sorted(
        matches,
        key=lambda item: (
            str(item.get("code") or item.get("account_code")),
            str(item.get("canonical_id")),
        ),
    )


def _scope_entities(
    cards: Sequence[Mapping[str, object]],
    dimension: str,
) -> Iterable[Dict[str, object]]:
    for card in cards:
        card_type = str(card.get("card_type") or "")
        canonical_id = str(card.get("canonical_id") or "")
        if not canonical_id:
            continue
        parts = canonical_id.split(".")

        if dimension == "tenant" and card_type == "tenant" and len(parts) >= 2:
            code = parts[1]
            aliases = _scope_aliases(code, card.get("tenant_name"), card.get("name"))
            aliases.add(_tenant_short_code(code))
            yield {
                "canonical_id": canonical_id,
                "code": code,
                "aliases": aliases,
            }

        if dimension == "group" and card_type == "group" and len(parts) >= 2:
            code = parts[1]
            yield {
                "canonical_id": canonical_id,
                "code": code,
                "aliases": _scope_aliases(code, card.get("group_name"), card.get("name")),
            }

        if dimension == "platform" and card_type == "platform" and len(parts) >= 2:
            code = parts[1]
            aliases = _scope_aliases(code, card.get("platform_name"), card.get("name"))
            aliases.update(PLATFORM_HINTS.get(code, set()))
            if code.endswith("_bank"):
                aliases.add(code[: -len("_bank")])
            yield {
                "canonical_id": canonical_id,
                "code": code,
                "aliases": aliases,
            }

        if dimension == "account" and card_type == "platform_account" and len(parts) >= 4:
            tenant_code, platform_code, account_code = parts[1], parts[2], parts[3]
            yield {
                "canonical_id": canonical_id,
                "code": account_code,
                "tenant_code": tenant_code,
                "platform_code": platform_code,
                "account_code": account_code,
                "aliases": _scope_aliases(account_code, card.get("account_name"), card.get("name")),
            }


def _static_platform_matches(query_norm: str) -> List[Dict[str, object]]:
    matches: List[Dict[str, object]] = []
    for platform_code, aliases in PLATFORM_HINTS.items():
        for alias in {platform_code, *aliases}:
            alias_norm = _normalize_text(alias)
            if alias_norm and _phrase_in_text(alias_norm, query_norm):
                matches.append(
                    {
                        "canonical_id": f"platform.{platform_code}",
                        "code": platform_code,
                        "aliases": {platform_code, *aliases},
                        "matched_alias": alias,
                        "source": "query",
                    }
                )
                break
    return matches


def _narrow_account_matches(
    account_matches: Sequence[Mapping[str, object]],
    tenant_matches: Sequence[Mapping[str, object]],
    platform_matches: Sequence[Mapping[str, object]],
) -> Dict[str, object]:
    tenant_codes = {_tenant_short_code(str(match.get("code"))) for match in tenant_matches}
    platform_codes = {str(match.get("code")) for match in platform_matches}
    narrowed = []
    for match in account_matches:
        tenant_ok = not tenant_codes or str(match.get("tenant_code")) in tenant_codes
        match_platform_codes = _platform_scope_codes(str(match.get("platform_code") or ""))
        platform_ok = not platform_codes or bool(match_platform_codes & platform_codes)
        if tenant_ok and platform_ok:
            narrowed.append(dict(match))

    ambiguous_filters = []
    by_account: DefaultDict[str, List[Mapping[str, object]]] = defaultdict(list)
    for match in narrowed:
        by_account[str(match.get("account_code"))].append(match)
    for account_code, matches in by_account.items():
        if len(matches) > 1:
            ambiguous_filters.append(
                {
                    "dimension": "account",
                    "value": account_code,
                    "candidate_ids": [str(match.get("canonical_id")) for match in matches],
                }
            )

    return {"matches": narrowed, "ambiguous_filters": ambiguous_filters}


def _scope_score(
    card: Mapping[str, object],
    scope_resolution: Mapping[str, object],
) -> Tuple[float, List[str], bool]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        return 0.0, [], False
    card_scope = _card_scope(card)
    score = 0.0
    reasons: List[str] = []
    hard_conflict = False

    for dimension, hint_key in (
        ("tenant", "tenant_codes"),
        ("group", "group_codes"),
        ("platform", "platform_codes"),
        ("account", "account_codes"),
    ):
        hint_values = {str(value) for value in hints.get(hint_key, [])} if isinstance(hints.get(hint_key), list) else set()
        if not hint_values:
            continue
        card_values = card_scope.get(dimension, set())
        if not card_values:
            continue
        if card_values & hint_values:
            score += 18.0 if dimension in {"tenant", "platform"} else 10.0
            reasons.append(f"{dimension} scope match")
        elif dimension in {"tenant", "platform"}:
            hard_conflict = True
            reasons.append(f"{dimension} scope conflict")

    return score, reasons, hard_conflict


def _scope_support_ids(
    scope_resolution: Mapping[str, object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Set[str]:
    hints = scope_resolution.get("query_hints")
    if not isinstance(hints, Mapping):
        return set()

    tenant_codes = {_tenant_short_code(str(value)) for value in hints.get("tenant_codes", [])}
    group_codes = {str(value) for value in hints.get("group_codes", [])}
    platform_codes = {str(value) for value in hints.get("platform_codes", [])}
    account_codes = {str(value) for value in hints.get("account_codes", [])}
    if not (tenant_codes or group_codes or platform_codes or account_codes):
        return set()

    support_ids: Set[str] = set()
    for card_id, card in cards_by_id.items():
        card_scope = _card_scope(card)
        card_type = str(card.get("card_type") or "")
        if card_type not in SCOPE_CARD_TYPES and card_type != "account_data_binding":
            continue
        if tenant_codes and card_scope.get("tenant") and not (card_scope["tenant"] & tenant_codes):
            continue
        if group_codes and card_scope.get("group") and not (card_scope["group"] & group_codes):
            continue
        if platform_codes and card_scope.get("platform") and not (card_scope["platform"] & platform_codes):
            continue
        if account_codes and card_scope.get("account") and not (card_scope["account"] & account_codes):
            continue
        if (
            (tenant_codes and card_scope.get("tenant"))
            or (group_codes and card_scope.get("group"))
            or (platform_codes and card_scope.get("platform"))
            or (account_codes and card_scope.get("account"))
        ):
            support_ids.add(card_id)
    return support_ids


def _scope_context(
    scope_resolution: Mapping[str, object],
    selected_cards: Sequence[Mapping[str, object]],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Dict[str, object]:
    selected_ids = {str(card.get("canonical_id")) for card in selected_cards}
    support_ids = _scope_support_ids(scope_resolution, cards_by_id)
    scope_cards = [
        _card_record(cards_by_id[card_id])
        for card_id in sorted(support_ids)
        if card_id in cards_by_id and card_id in selected_ids
    ]
    return {
        "query_hints": scope_resolution.get("query_hints", {}),
        "applied_filters": scope_resolution.get("applied_filters", []),
        "ambiguous_filters": scope_resolution.get("ambiguous_filters", []),
        "scope_cards": scope_cards,
    }


def _card_scope(card: Mapping[str, object]) -> Dict[str, Set[str]]:
    canonical_id = str(card.get("canonical_id") or "")
    card_type = str(card.get("card_type") or "")
    parts = canonical_id.split(".")
    scope: Dict[str, Set[str]] = {
        "tenant": set(),
        "group": set(),
        "platform": set(),
        "account": set(),
    }

    if card_type == "tenant" and len(parts) >= 2:
        scope["tenant"].add(parts[1])
        scope["tenant"].add(_tenant_short_code(parts[1]))
    elif card_type == "group" and len(parts) >= 2:
        scope["group"].add(parts[1])
        scope["tenant"].add(_tenant_short_code(parts[1]))
    elif card_type == "business_scope_set" and len(parts) >= 2:
        scope["group"].add(parts[1])
        scope["tenant"].add(_tenant_short_code(parts[1]))
    elif card_type == "platform" and len(parts) >= 2:
        scope["platform"].add(parts[1])
    elif card_type == "platform_account" and len(parts) >= 4:
        scope["tenant"].add(parts[1])
        scope["platform"].update(_platform_scope_codes(parts[2]))
        scope["account"].add(parts[3])
    elif card_type == "account_data_binding" and len(parts) >= 5:
        scope["tenant"].add(parts[1])
        scope["platform"].update(_platform_scope_codes(parts[2]))
        scope["account"].add(parts[3])
    elif card_type == "business_flow_binding":
        tenant_id = str(card.get("tenant_id") or "")
        group_id = str(card.get("group_id") or "")
        if tenant_id.startswith("tenant."):
            scope["tenant"].add(tenant_id.split(".", 1)[1])
            scope["tenant"].add(_tenant_short_code(tenant_id.split(".", 1)[1]))
        if group_id.startswith("group."):
            scope["group"].add(group_id.split(".", 1)[1])
            scope["tenant"].add(_tenant_short_code(group_id.split(".", 1)[1]))
        for account_id in _strings(card.get("platform_account_ids")):
            account_parts = account_id.split(".")
            if len(account_parts) >= 4 and account_parts[0] == "platform_account":
                scope["tenant"].add(account_parts[1])
                scope["platform"].update(_platform_scope_codes(account_parts[2]))
                scope["account"].add(account_parts[3])

    scope["platform"].update(_infer_platform_codes(card))

    for field, dimension in (
        ("tenant_name", "tenant"),
        ("group_name", "group"),
        ("platform_name", "platform"),
        ("account_name", "account"),
    ):
        value = card.get(field)
        if isinstance(value, str) and value:
            scope[dimension].add(_slug(value))

    return scope


def _infer_platform_codes(card: Mapping[str, object]) -> Set[str]:
    text_parts = [
        str(card.get("canonical_id") or ""),
        str(card.get("name") or ""),
        str(card.get("description") or ""),
        str(card.get("source_identifier") or ""),
        str(card.get("table_name") or ""),
        str(card.get("full_reference") or ""),
    ]
    text = _normalize_text(" ".join(text_parts).replace("_", " "))
    found: Set[str] = set()
    for platform_code, aliases in PLATFORM_HINTS.items():
        candidates = {platform_code, *aliases}
        for candidate in candidates:
            candidate_norm = _normalize_text(candidate)
            if candidate_norm and _phrase_in_text(candidate_norm, text):
                found.update(_platform_scope_codes(platform_code))
    return found


def _scope_aliases(code: str, *values: object) -> Set[str]:
    aliases = {code, code.replace("_", " ")}
    for value in values:
        if isinstance(value, str) and value:
            aliases.add(value)
            aliases.add(_slug(value))
            aliases.add(_slug(value).replace("_", " "))
    return {alias for alias in aliases if alias}


def _tenant_short_code(code: str) -> str:
    if code.startswith("nimbus"):
        return "nimbus"
    if code.startswith("prism"):
        return "prism"
    return code.split("_", 1)[0]


def _platform_scope_codes(code: str) -> Set[str]:
    codes = {code}
    if code.endswith("_in"):
        codes.add(code[:-3])
    if code.startswith("nykaa"):
        codes.add("nykaa")
    if code.endswith("_bank"):
        codes.add(code[: -len("_bank")])
    if code in {"hdfc", "hdfc_bank"}:
        codes.update({"hdfc", "hdfc_bank"})
    if code in {"icici", "icici_bank"}:
        codes.update({"icici", "icici_bank"})
    return codes


def _slug(value: str) -> str:
    return "_".join(_tokens(value))


def _phrase_in_text(phrase_norm: str, text_norm: str) -> bool:
    if not phrase_norm or not text_norm:
        return False
    return f" {phrase_norm} " in f" {text_norm} "


def _iter_reference_values(value: object) -> Iterable[str]:
    if value in (None, "", []):
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [str(item) for item in value if item not in (None, "")]
    return [str(value)]


def _ids_from_text(text: str, cards_by_id: Mapping[str, Mapping[str, object]]) -> Iterable[str]:
    found: Set[str] = set()
    norm = _normalize_text(text)
    for card_id, card in cards_by_id.items():
        if str(card.get("card_type")) not in {"table", "column"}:
            continue
        candidates = [card_id, str(card.get("full_reference") or ""), str(card.get("table_name") or "")]
        for candidate in candidates:
            if candidate and _normalize_text(candidate) in norm:
                found.add(card_id)
    return found


def _ids_from_cognee_results(
    results: Sequence[object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Iterable[str]:
    text = json.dumps(results, ensure_ascii=False).lower()
    return [card_id for card_id in cards_by_id if card_id.lower() in text]


def _candidate_discovery_results(results: Sequence[object]) -> List[object]:
    return [
        item
        for item in results
        if isinstance(item, Mapping) and item.get("query_type") == "canonical_candidate_discovery"
    ]


def _candidate_facets_from_cognee_results(
    results: Sequence[object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> Dict[str, List[str]]:
    facets: DefaultDict[str, Set[str]] = defaultdict(set)
    for item in results:
        if not isinstance(item, Mapping):
            continue
        facet = str(item.get("facet") or item.get("query_type") or "")
        if not facet:
            continue
        ids = _ids_from_cognee_results([item.get("results", [])], cards_by_id)
        for card_id in ids:
            facets[card_id].add(facet)
    return {card_id: sorted(values) for card_id, values in facets.items()}


def _unrecognized_canonical_mentions(
    results: Sequence[object],
    cards_by_id: Mapping[str, Mapping[str, object]],
) -> List[str]:
    text = json.dumps(results, ensure_ascii=False)
    known_lower = {card_id.lower() for card_id in cards_by_id}
    mentions = []
    for raw in re.findall(
        r"\b(?:tenant|group|platform|platform_account|account_data_binding|business_flow_binding|"
        r"metric_impl|metric|table|column|relationship|query_pattern|reconciliation_variant|"
        r"reconciliation_profile|reconciliation_side|reconciliation_unit|matching_logic|"
        r"mismatch_category|rule|validation_test|output_contract|execution_constraint_set)"
        r"\.[A-Za-z0-9_.-]+",
        text,
    ):
        mention = raw.rstrip(".,;:)]}'\"")
        if mention.lower() not in known_lower:
            mentions.append(mention)
    return sorted(set(mentions))


def _cognee_discovery_results(
    base_url: str,
    dataset: str,
    query: str,
    *,
    request_facets: Optional[Mapping[str, object]] = None,
    timeout: float,
) -> List[object]:
    raw_results = _cognee_search(base_url, dataset, query, timeout=timeout)
    discovery_results = [
        {
            "query_type": "answer_context",
            "query": query,
            "results": raw_results,
        }
    ]
    for facet, candidate_query in _cognee_facet_candidate_queries(query, request_facets or {}).items():
        candidate_results = _cognee_search(base_url, dataset, candidate_query, timeout=timeout)
        discovery_results.append(
            {
                "query_type": "canonical_candidate_discovery",
                "facet": facet,
                "query": candidate_query,
                "results": candidate_results,
            }
        )
    return discovery_results


def _cognee_candidate_discovery_failed(results: Sequence[object]) -> bool:
    saw_discovery = False
    saw_success = False
    for item in results:
        if not isinstance(item, Mapping):
            continue
        if item.get("query_type") != "canonical_candidate_discovery":
            continue
        saw_discovery = True
        candidate_results = item.get("results")
        if not _contains_cognee_error(candidate_results):
            saw_success = True
    return not saw_discovery or not saw_success


def _contains_cognee_error(value: object) -> bool:
    if isinstance(value, Mapping):
        if value.get("error"):
            return True
        return any(_contains_cognee_error(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_cognee_error(item) for item in value)
    return False


def _cognee_candidate_query(query: str) -> str:
    return (
        "Find canonical metric, metric_implementation, column, table, relationship, "
        "and account_data_binding cards relevant to this analytics request. "
        "Return canonical_id values when available. "
        f"User request: {query}"
    )


def _cognee_facet_candidate_queries(
    query: str,
    facets: Mapping[str, object],
) -> Dict[str, str]:
    queries: Dict[str, str] = {}
    entities = _strings(facets.get("entities"))
    dimensions = _strings(facets.get("dimensions"))
    metrics = _strings(facets.get("metrics"))
    relationships = _strings(facets.get("relationships"))
    ranking = _strings(facets.get("ranking"))
    evidence_requirements = _strings(facets.get("evidence_requirements"))
    filters = _mapping(facets.get("filters"))
    scope_text = _facet_scope_text(filters)

    if entities:
        queries["entities"] = _facet_query(
            query,
            "entities",
            [
                "Find canonical entity evidence for requested tenants, OMS/order systems, marketplaces, platform accounts, tables, and account_data_bindings.",
                "Prefer table, platform_account, account_data_binding, business_flow_binding, tenant, group, and platform cards.",
                "Do not return metric cards unless the user explicitly asks for a metric.",
            ],
            entities,
            scope_text,
            evidence_requirements,
        )
    if dimensions:
        queries["dimensions"] = _facet_query(
            query,
            "dimensions",
            [
                "Find canonical column cards for requested dimensions.",
                "Return exact column canonical_id values and their table canonical_id values when available.",
            ],
            dimensions,
            scope_text,
            evidence_requirements,
        )
    if metrics:
        queries["metrics"] = _facet_query(
            query,
            "metrics",
            [
                "Find canonical metric and metric_implementation cards for requested metrics.",
                "Return implementation cards with formulas and base table references when available.",
                "For derived metric phrases, return base metric evidence; do not invent a metric card.",
            ],
            metrics,
            scope_text,
            evidence_requirements,
        )
    if relationships:
        queries["relationships"] = _facet_query(
            query,
            "relationships",
            [
                "Find canonical relationship, business_flow_binding, account_data_binding, platform_account, and table evidence for requested connections.",
                "For OMS to marketplace requests, prioritize OMS tables, marketplace platform accounts, and account_data_bindings.",
                "Do not return unrelated metrics unless the query asks for them.",
            ],
            relationships,
            scope_text,
            evidence_requirements,
        )
    if ranking:
        queries["ranking"] = _facet_query(
            query,
            "ranking",
            [
                "Find canonical metric, dimension, and column evidence needed by the downstream SQL generator for the requested ranking.",
                "Do not implement sorting or SQL; only return evidence canonical IDs.",
            ],
            ranking,
            scope_text,
            evidence_requirements,
        )

    if not queries:
        queries["general"] = _cognee_candidate_query(query)
    return queries


def _facet_query(
    user_query: str,
    facet: str,
    instructions: Sequence[str],
    requested_values: Sequence[str],
    scope_text: str,
    evidence_requirements: Sequence[str],
) -> str:
    return (
        "You are retrieving canonical KB evidence, not answering the user. "
        "Return canonical_id values when available and label unknown hints separately. "
        "Do not invent canonical IDs. "
        f"Facet: {facet}. "
        f"Requested values: {', '.join(requested_values) or 'none'}. "
        f"Scope: {scope_text}. "
        f"Evidence requirements: {', '.join(evidence_requirements) or 'canonical evidence for this facet'}. "
        f"Instructions: {' '.join(instructions)} "
        f"User request: {user_query}"
    )


def _facet_scope_text(filters: Mapping[str, object]) -> str:
    parts = []
    for key in ("tenant_codes", "group_codes", "platform_codes", "account_codes"):
        values = _strings(filters.get(key))
        if values:
            parts.append(f"{key}={','.join(values)}")
    return "; ".join(parts) if parts else "no explicit scope"


def _cognee_search(
    base_url: str,
    dataset: str,
    query: str,
    *,
    timeout: float,
) -> List[object]:
    payload = {
        "query": query,
        "search_type": "GRAPH_COMPLETION",
        "datasets": [dataset],
    }
    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}/api/v1/search",
        data=body,
        headers={"Accept": "application/json", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except (urllib.error.URLError, TimeoutError) as exc:
        return [{"error": f"Cognee search failed: {exc}"}]
    if not raw:
        return []
    try:
        decoded = json.loads(raw)
    except json.JSONDecodeError:
        return [raw]
    if isinstance(decoded, list):
        return decoded
    return [decoded]
