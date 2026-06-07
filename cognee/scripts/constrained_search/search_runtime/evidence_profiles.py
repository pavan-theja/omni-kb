from __future__ import annotations

from typing import Any

from .nodeset_contracts import SearchContract
from .utils import first_node_set, unique_in_order


CARD_TYPE_PURPOSE_REGISTRY: dict[str, dict[str, str]] = {
    "tenant": {"family": "runtime_scope", "purpose": "Tenant/client root."},
    "group": {"family": "runtime_scope", "purpose": "Tenant group or group-level runtime scope."},
    "platform": {"family": "runtime_scope", "purpose": "Source system or platform."},
    "platform_context": {"family": "runtime_scope", "purpose": "Source context such as geography, currency, or fulfilment mode."},
    "platform_account": {"family": "runtime_scope", "purpose": "Tenant/group-specific connected source account."},
    "account_data_binding": {"family": "runtime_scope", "purpose": "Runtime proof that a tenant/group/platform account can use a table/domain/source role."},
    "business_scope_set": {"family": "runtime_scope", "purpose": "Runtime scope bundle across accounts and bindings."},
    "business_flow_binding": {"family": "runtime_scope", "purpose": "Runtime binding of a tenant/group to a business flow."},
    "domain": {"family": "source_domain_table", "purpose": "Business domain bucket under a source/system."},
    "table": {"family": "source_domain_table", "purpose": "Physical/source table contract."},
    "column": {"family": "source_domain_table", "purpose": "Field-level semantics, data type, and grain/filter/join/metric roles."},
    "relationship": {"family": "source_domain_table", "purpose": "Table join/link evidence and join-safety guidance."},
    "metric": {"family": "metrics_reporting", "purpose": "Global business metric definition."},
    "metric_implementation": {"family": "metrics_reporting", "purpose": "Table-specific implementation of a metric."},
    "metric_dependency": {"family": "metrics_reporting", "purpose": "Dependency between metrics or metric components."},
    "formula_template": {"family": "metrics_reporting", "purpose": "Reusable formula or calculation template."},
    "query_pattern": {"family": "metrics_reporting", "purpose": "Query/report blueprint."},
    "output_contract": {"family": "metrics_reporting", "purpose": "Expected output shape or report contract."},
    "execution_constraint_set": {"family": "metrics_reporting", "purpose": "Constraints required for safe execution."},
    "value_profile": {"family": "values_rules_quality", "purpose": "Known values, status semantics, normalization, and null/value interpretation."},
    "rule": {"family": "values_rules_quality", "purpose": "Business rule, guardrail, or deterministic action."},
    "validation_test": {"family": "values_rules_quality", "purpose": "Data quality or correctness test."},
    "state_transition": {"family": "values_rules_quality", "purpose": "Lifecycle/status transition semantics."},
    "business_process": {"family": "process_operations", "purpose": "Process flow definition."},
    "workflow_step": {"family": "process_operations", "purpose": "Operational step within a process."},
    "process_variant": {"family": "process_operations", "purpose": "Special case or variant of a process."},
    "reconciliation_profile": {"family": "reconciliation", "purpose": "Overall reconciliation scenario."},
    "reconciliation_side": {"family": "reconciliation", "purpose": "One side of a reconciliation."},
    "reconciliation_unit": {"family": "reconciliation", "purpose": "Grain/unit of matching."},
    "matching_logic": {"family": "reconciliation", "purpose": "Matching keys, tolerances, and strategy."},
    "mismatch_category": {"family": "reconciliation", "purpose": "Mismatch classification and likely causes."},
    "reconciliation_variant": {"family": "reconciliation", "purpose": "Special case or variant of a reconciliation profile."},
}


EVIDENCE_PROFILE_REGISTRY: dict[str, dict[str, Any]] = {
    "runtime_scope_resolution": {
        "purpose": "Resolve legal tenant/group runtime sources.",
        "card_types": [
            "tenant",
            "group",
            "platform",
            "platform_context",
            "platform_account",
            "account_data_binding",
            "business_scope_set",
            "business_flow_binding",
        ],
        "default_scope": "runtime",
        "column_strategy": "none",
    },
    "source_domain_resolution": {
        "purpose": "Resolve relevant domains and source areas within legal runtime scope.",
        "card_types": ["domain", "account_data_binding", "table"],
        "default_scope": "domain",
        "column_strategy": "none",
    },
    "table_contract_resolution": {
        "purpose": "Resolve table contracts and table-level source semantics.",
        "card_types": ["table", "column", "relationship"],
        "default_scope": "table",
        "column_strategy": "targeted",
    },
    "field_semantics_resolution": {
        "purpose": "Resolve fields, values, statuses, filters, grouping, joins, and value semantics.",
        "card_types": ["column", "value_profile", "state_transition", "rule"],
        "default_scope": "table",
        "column_strategy": "targeted",
    },
    "measure_calculation_resolution": {
        "purpose": "Resolve counts, amounts, rates, ratios, trends, and derived measures.",
        "card_types": ["metric", "metric_implementation", "metric_dependency", "formula_template", "column", "value_profile"],
        "default_scope": "mixed",
        "column_strategy": "targeted",
    },
    "query_shape_resolution": {
        "purpose": "Resolve report/query shape, required fields, grouping, filters, ordering, and expected output.",
        "card_types": ["query_pattern", "output_contract", "execution_constraint_set", "column", "metric_implementation"],
        "default_scope": "mixed",
        "column_strategy": "targeted",
    },
    "relationship_join_resolution": {
        "purpose": "Resolve joins, relationship safety, cardinality, and pre-aggregation requirements.",
        "card_types": ["relationship", "table", "column"],
        "default_scope": "table",
        "column_strategy": "targeted",
    },
    "process_flow_resolution": {
        "purpose": "Resolve operational process flow, workflow steps, variants, and lifecycle states.",
        "card_types": ["business_process", "workflow_step", "process_variant", "state_transition", "table", "column"],
        "default_scope": "mixed",
        "column_strategy": "targeted",
    },
    "reconciliation_resolution": {
        "purpose": "Resolve reconciliation sides, units, matching logic, mismatch categories, and variants.",
        "card_types": [
            "reconciliation_profile",
            "reconciliation_side",
            "reconciliation_unit",
            "matching_logic",
            "mismatch_category",
            "reconciliation_variant",
            "relationship",
            "rule",
            "validation_test",
        ],
        "default_scope": "mixed",
        "column_strategy": "targeted",
    },
    "validation_guardrail_resolution": {
        "purpose": "Resolve data quality checks, execution guardrails, mandatory filters, and blocking/warning constraints.",
        "card_types": ["rule", "validation_test", "execution_constraint_set", "value_profile", "column"],
        "default_scope": "mixed",
        "column_strategy": "targeted",
    },
}


TABLE_LOCAL_CARD_TYPES = {
    "column",
    "metric_implementation",
    "value_profile",
    "query_pattern",
    "workflow_step",
    "rule",
    "mismatch_category",
    "validation_test",
    "reconciliation_side",
    "state_transition",
    "formula_template",
    "relationship",
    "reconciliation_unit",
    "matching_logic",
    "output_contract",
    "reconciliation_profile",
    "metric_dependency",
    "execution_constraint_set",
    "reconciliation_variant",
    "process_variant",
}

DOMAIN_LOCAL_CARD_TYPES = set(CARD_TYPE_PURPOSE_REGISTRY) - {
    "tenant",
    "group",
    "platform_account",
    "account_data_binding",
    "business_scope_set",
    "business_flow_binding",
    "table",
    "column",
}


def generic_stage_template(stage: str) -> dict[str, Any] | None:
    parsed = parse_generic_profile_stage(stage)
    if parsed is None:
        return None
    scope_type, card_type = parsed
    if scope_type == "table" and card_type not in TABLE_LOCAL_CARD_TYPES:
        return None
    if scope_type == "domain" and card_type not in DOMAIN_LOCAL_CARD_TYPES:
        return None
    required_key = "table_id" if scope_type == "table" else "domain_id"
    return {"card_type": card_type, "required_node_set_keys": ["card_type", required_key]}


def parse_generic_profile_stage(stage: str) -> tuple[str, str] | None:
    if stage.startswith("table_local_") and stage.endswith("_search"):
        return "table", stage.removeprefix("table_local_").removesuffix("_search")
    if stage.startswith("domain_local_") and stage.endswith("_search"):
        return "domain", stage.removeprefix("domain_local_").removesuffix("_search")
    return None


def missing_card_type_purposes(catalogs: Any) -> list[str]:
    observed = {
        str(card.get("card_type"))
        for card in getattr(catalogs, "card_catalog", {}).values()
        if isinstance(card, dict) and card.get("card_type")
    }
    return sorted(observed - set(CARD_TYPE_PURPOSE_REGISTRY))


def invalid_profile_card_types() -> dict[str, list[str]]:
    valid = set(CARD_TYPE_PURPOSE_REGISTRY)
    invalid: dict[str, list[str]] = {}
    for profile_id, profile in EVIDENCE_PROFILE_REGISTRY.items():
        missing = [card_type for card_type in profile.get("card_types") or [] if card_type not in valid]
        if missing:
            invalid[profile_id] = missing
    return invalid


def build_evidence_manifest(
    catalogs: Any,
    table_cards: list[dict[str, Any]],
    predecessor_contract: SearchContract,
    *,
    max_candidates_per_type: int = 24,
) -> dict[str, Any]:
    tables: list[dict[str, Any]] = []
    for table_card in table_cards:
        table_scope = table_scope_from_card(table_card, predecessor_contract.required_carry_forward)
        table_id = table_scope.get("table_id")
        if not table_id:
            continue
        table_local = scoped_cards_by_type(
            catalogs,
            scope_type="table",
            scope_id=table_id,
            table_scope=table_scope,
            max_candidates_per_type=max_candidates_per_type,
        )
        domain_local: dict[str, Any] = {}
        domain_id = table_scope.get("domain_id")
        if domain_id:
            domain_local = scoped_cards_by_type(
                catalogs,
                scope_type="domain",
                scope_id=domain_id,
                table_scope=table_scope,
                exclude_card_ids=manifest_card_ids(table_local),
                max_candidates_per_type=max_candidates_per_type,
            )
        tables.append(
            {
                **table_scope,
                "table_card": compact_manifest_card(table_card),
                "table_local": table_local,
                "domain_local": domain_local,
                "available_card_types": sorted(set(table_local) | set(domain_local)),
            }
        )
    return {
        "tables": tables,
        "card_type_purpose_registry": CARD_TYPE_PURPOSE_REGISTRY,
        "evidence_profile_registry": EVIDENCE_PROFILE_REGISTRY,
    }


def table_scope_from_card(table_card: dict[str, Any], carry: dict[str, Any]) -> dict[str, str]:
    node_sets = card_node_sets(table_card)
    scope: dict[str, str] = {}
    for key in (
        "tenant_id",
        "group_id",
        "runtime_source_family",
        "platform_id",
        "platform_context_id",
        "platform_account_id",
        "account_data_binding_id",
        "source_role",
        "domain_id",
        "table_id",
    ):
        value = first_node_value(node_sets, key) or carry.get(key)
        if value not in (None, "", []):
            scope[key] = str(value)
    table_id = scope.get("table_id") or card_id(table_card)
    if table_id:
        scope["table_id"] = table_id
    return scope


def scoped_cards_by_type(
    catalogs: Any,
    *,
    scope_type: str,
    scope_id: str,
    table_scope: dict[str, str],
    exclude_card_ids: set[str] | None = None,
    max_candidates_per_type: int,
) -> dict[str, Any]:
    exclude_card_ids = exclude_card_ids or set()
    prefix = "table_id" if scope_type == "table" else "domain_id"
    supported_types = TABLE_LOCAL_CARD_TYPES if scope_type == "table" else DOMAIN_LOCAL_CARD_TYPES
    grouped: dict[str, list[dict[str, Any]]] = {}
    for card in getattr(catalogs, "card_catalog", {}).values():
        if not isinstance(card, dict):
            continue
        canonical_id = card_id(card)
        if canonical_id in exclude_card_ids:
            continue
        card_type = str(card.get("card_type") or "")
        if card_type not in supported_types:
            continue
        node_sets = card_node_sets(card)
        if f"{prefix}:{scope_id}" not in node_sets:
            continue
        if not card_scope_is_compatible(node_sets, table_scope):
            continue
        grouped.setdefault(card_type, []).append(compact_manifest_card(card))

    out: dict[str, Any] = {}
    for card_type, cards in sorted(grouped.items()):
        cards.sort(key=lambda item: str(item.get("canonical_id") or ""))
        out[card_type] = {
            "count": len(cards),
            "candidates": cards[:max_candidates_per_type],
        }
    return out


def card_scope_is_compatible(node_sets: list[str], table_scope: dict[str, str]) -> bool:
    for key in ("platform_id", "platform_context_id", "source_role"):
        card_value = first_node_value(node_sets, key)
        scope_value = table_scope.get(key)
        if card_value and scope_value and card_value != scope_value:
            return False
    return True


def manifest_card_ids(scoped_cards: dict[str, Any]) -> set[str]:
    ids: set[str] = set()
    for payload in scoped_cards.values():
        for card in payload.get("candidates") or []:
            canonical_id = str(card.get("canonical_id") or "")
            if canonical_id:
                ids.add(canonical_id)
    return ids


def profile_contracts_from_decision(
    decision: dict[str, Any],
    manifest: dict[str, Any],
    predecessor_contract: SearchContract,
    query_text: str,
) -> tuple[list[SearchContract], list[dict[str, Any]]]:
    normalized_requests = normalize_profile_requests(decision, manifest)
    contracts: list[SearchContract] = []
    rejected: list[dict[str, Any]] = []
    seen: set[tuple[str, str, str, str]] = set()

    for index, request in enumerate(normalized_requests, start=1):
        profile_id = str(request.get("profile_id") or "")
        card_type = str(request.get("card_type") or "")
        scope_type = str(request.get("scope_type") or "")
        scope_id = str(request.get("scope_id") or "")
        if profile_id not in EVIDENCE_PROFILE_REGISTRY:
            rejected.append({"request": request, "reason": "unknown_profile_id"})
            continue
        if card_type not in CARD_TYPE_PURPOSE_REGISTRY:
            rejected.append({"request": request, "reason": "unknown_card_type"})
            continue
        if scope_type not in {"table", "domain"}:
            rejected.append({"request": request, "reason": "unsupported_scope_type"})
            continue
        scope_payload = manifest_scope_payload(manifest, scope_type, scope_id, card_type)
        if scope_payload is None:
            rejected.append({"request": request, "reason": "card_type_not_available_in_manifest_scope"})
            continue
        stage = f"{scope_type}_local_{card_type}_search"
        if generic_stage_template(stage) is None:
            rejected.append({"request": request, "reason": "unsupported_generic_stage"})
            continue
        signature = (profile_id, scope_type, scope_id, card_type)
        if signature in seen:
            continue
        seen.add(signature)
        required = bool(request.get("required", True))
        node_key = "table_id" if scope_type == "table" else "domain_id"
        carry = dict(predecessor_contract.required_carry_forward)
        carry.update(
            {
                "evidence_profile_id": profile_id,
                "evidence_profile_ids": [profile_id],
                "evidence_scope_type": scope_type,
                "evidence_scope_id": scope_id,
            }
        )
        if required:
            carry["required_evidence_card_types"] = [card_type]
        else:
            carry["optional_evidence_card_types"] = [card_type]
        contracts.append(
            SearchContract(
                contract_id=f"q5.profile.{safe_contract_suffix(profile_id)}.{scope_type}.{safe_contract_suffix(scope_id)}.{safe_contract_suffix(card_type)}.{index}",
                stage=stage,
                query_text=f"{query_text} | {profile_id} evidence: {card_type} within {scope_type} {scope_id}",
                node_sets=[f"card_type:{card_type}", f"{node_key}:{scope_id}"],
                top_k=int(request.get("top_k") or default_top_k(card_type)),
                allowed_card_types=[card_type],
                required_carry_forward=carry,
                candidate_seed_ids=manifest_candidate_ids(scope_payload),
                reason=str(request.get("answer_obligation") or request.get("reason") or profile_id),
            )
        )
    return contracts, rejected


def normalize_profile_requests(decision: dict[str, Any], manifest: dict[str, Any]) -> list[dict[str, Any]]:
    raw_requests = decision.get("evidence_requests")
    if isinstance(raw_requests, list) and raw_requests:
        return [request for request in raw_requests if isinstance(request, dict)]

    requests: list[dict[str, Any]] = []
    selected_profiles = decision.get("selected_profiles") or decision.get("profiles") or []
    for profile in selected_profiles:
        if isinstance(profile, str):
            profile = {"profile_id": profile}
        if not isinstance(profile, dict):
            continue
        profile_id = str(profile.get("profile_id") or "")
        registry_entry = EVIDENCE_PROFILE_REGISTRY.get(profile_id)
        if not registry_entry:
            continue
        requested_card_types = profile.get("required_card_types") or registry_entry.get("card_types") or []
        answer_obligation = profile.get("answer_obligation") or registry_entry.get("purpose")
        for table in manifest.get("tables") or []:
            for card_type in requested_card_types:
                request = request_for_available_scope(
                    table,
                    profile_id=profile_id,
                    card_type=str(card_type),
                    answer_obligation=str(answer_obligation or ""),
                )
                if request:
                    requests.append(request)
    return requests


def request_for_available_scope(
    table: dict[str, Any],
    *,
    profile_id: str,
    card_type: str,
    answer_obligation: str,
) -> dict[str, Any] | None:
    table_id = str(table.get("table_id") or "")
    domain_id = str(table.get("domain_id") or "")
    if table_id and card_type in (table.get("table_local") or {}):
        return {
            "profile_id": profile_id,
            "scope_type": "table",
            "scope_id": table_id,
            "card_type": card_type,
            "required": True,
            "answer_obligation": answer_obligation,
        }
    if domain_id and card_type in (table.get("domain_local") or {}):
        return {
            "profile_id": profile_id,
            "scope_type": "domain",
            "scope_id": domain_id,
            "card_type": card_type,
            "required": True,
            "answer_obligation": answer_obligation,
        }
    return None


def manifest_scope_payload(manifest: dict[str, Any], scope_type: str, scope_id: str, card_type: str) -> dict[str, Any] | None:
    key = "table_local" if scope_type == "table" else "domain_local"
    id_key = "table_id" if scope_type == "table" else "domain_id"
    for table in manifest.get("tables") or []:
        if str(table.get(id_key) or "") != scope_id:
            continue
        payload = (table.get(key) or {}).get(card_type)
        if payload:
            return payload
    return None


def manifest_candidate_ids(scope_payload: dict[str, Any]) -> list[str]:
    return unique_in_order(
        str(card.get("canonical_id") or "")
        for card in scope_payload.get("candidates") or []
        if card.get("canonical_id")
    )


def default_top_k(card_type: str) -> int:
    if card_type == "column":
        return 24
    if card_type in {"query_pattern", "metric_implementation", "relationship", "value_profile"}:
        return 12
    return 8


def compact_manifest_card(card: dict[str, Any]) -> dict[str, Any]:
    fields = card.get("fields") if isinstance(card.get("fields"), dict) else {}
    return {
        "canonical_id": card_id(card),
        "canonical_name": card.get("canonical_name"),
        "card_type": card.get("card_type"),
        "node_sets": compact_node_sets(card_node_sets(card)),
        "field_keys": sorted(str(key) for key in fields.keys())[:20],
    }


def compact_node_sets(node_sets: list[str]) -> list[str]:
    keep_prefixes = (
        "card_type:",
        "domain_family:",
        "tenant_id:",
        "group_id:",
        "platform_id:",
        "platform_context_id:",
        "platform_account_id:",
        "account_data_binding_id:",
        "runtime_source_family:",
        "domain_id:",
        "source_role:",
        "table_id:",
        "column_id:",
        "metric_id:",
        "query_pattern_id:",
        "relationship_id:",
        "reconciliation_profile_id:",
        "process_id:",
        "canonical_id:",
    )
    return [node_set for node_set in node_sets if node_set.startswith(keep_prefixes)]


def card_id(card: dict[str, Any]) -> str:
    return str(card.get("canonical_id") or card.get("id") or "")


def card_node_sets(card: dict[str, Any]) -> list[str]:
    return [str(node_set) for node_set in card.get("node_sets") or card.get("ingestion_node_sets") or []]


def first_node_value(node_sets: list[str], key: str) -> str | None:
    return first_node_set(node_sets, key)


def safe_contract_suffix(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in str(value)).strip("_").lower()[:120]
