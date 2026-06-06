from __future__ import annotations

from typing import Any

from .catalogs import CatalogBundle
from .nodeset_contracts import SearchContract
from .utils import first_node_set, node_set_map


class ContractValidationError(ValueError):
    pass


def validate_contract(contract: SearchContract, catalogs: CatalogBundle | None = None) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    ns_map = node_set_map(contract.node_sets)
    keys = set(ns_map)

    if not contract.node_sets:
        errors.append("contract_has_no_node_sets")
    if "__malformed__" in keys:
        errors.append(f"contract_has_malformed_nodesets:{ns_map['__malformed__']}")
    if not contract.query_text.strip() and not contract.exact_dereference_ids:
        errors.append("contract_has_empty_query_text")
    if contract.top_k <= 0:
        errors.append("contract_top_k_must_be_positive")
    if contract.allowed_card_types and "card_type" not in keys:
        errors.append("allowed_card_types_present_but_no_card_type_nodeset")
    if contract.allowed_card_types and first_node_set(contract.node_sets, "card_type") not in contract.allowed_card_types:
        errors.append("card_type_nodeset_not_in_allowed_card_types")

    if contract.stage.startswith("runtime_"):
        for key in ["domain_family", "card_type", "tenant_id", "group_id"]:
            if key not in keys:
                errors.append(f"runtime_contract_missing_{key}")
    if contract.stage.startswith("table_local_") or contract.stage.startswith("semantic_table_"):
        for key in ["card_type", "table_id"]:
            if key not in keys:
                errors.append(f"table_contract_missing_{key}")
    if "relationship" in contract.closed_gates and "relationship" in contract.stage:
        errors.append("relationship_stage_requested_while_gate_closed")
    if "reconciliation" in contract.closed_gates and "reconciliation" in contract.stage:
        errors.append("reconciliation_stage_requested_while_gate_closed")

    if catalogs is not None:
        for node_set in contract.node_sets:
            if ":" in node_set and not catalogs.known_node_set(node_set):
                errors.append(f"unknown_nodeset_in_contract:{node_set}")

        template = catalogs.template_for_stage(contract.stage)
        if template:
            for key in effective_required_node_set_keys(contract, template):
                if key not in keys:
                    errors.append(f"contract_missing_template_required_nodeset_key:{key}")
            template_card_type = template.get("card_type")
            if template_card_type and first_node_set(contract.node_sets, "card_type") != template_card_type:
                errors.append(f"contract_card_type_does_not_match_template:{template_card_type}")
        else:
            errors.append(f"unknown_stage_in_contract:{contract.stage}")

        table_id = first_node_set(contract.node_sets, "table_id")
        if table_id and not catalogs.known_table_id(table_id):
            errors.append(f"unknown_table_id_in_contract:{table_id}")

        binding_id = contract.required_carry_forward.get("account_data_binding_id")
        if binding_id:
            binding = catalogs.binding_status(str(binding_id))
            if not binding:
                errors.append(f"unknown_account_data_binding_id_in_carry_forward:{binding_id}")
            elif binding.get("binding_status") != "active":
                errors.append(f"blocked_account_data_binding_in_carry_forward:{binding_id}:{binding.get('binding_status')}")

        for cid in contract.candidate_seed_ids + contract.exact_dereference_ids:
            if cid and not catalogs.known_card_id(cid):
                errors.append(f"unknown_canonical_id_in_contract:{cid}")

    return {"ok": not errors, "errors": errors, "warnings": warnings, "node_set_keys": sorted(k for k in keys if k != "__malformed__")}


def effective_required_node_set_keys(contract: SearchContract, template: dict[str, Any]) -> list[str]:
    required = list(template.get("required_node_set_keys") or [])
    if contract.stage == "runtime_platform_account_search" and "platform_id" not in node_set_map(contract.node_sets):
        return [key for key in required if key != "platform_id"]
    return required


def canonicalize_contract(contract: SearchContract, catalogs: CatalogBundle | None = None) -> SearchContract:
    if catalogs is None:
        return contract
    node_sets = [catalogs.canonicalize_node_set(str(node_set)) for node_set in contract.node_sets]
    if node_sets == contract.node_sets:
        return contract
    return SearchContract(**{**contract.to_dict(), "node_sets": node_sets})


def validate_or_raise(contract: SearchContract, catalogs: CatalogBundle | None = None) -> None:
    validation = validate_contract(contract, catalogs)
    if not validation["ok"]:
        raise ContractValidationError(f"Invalid SearchContract {contract.contract_id}: {validation['errors']}")


def validate_returned_cards(contract: SearchContract, cards: list[dict[str, Any]], catalogs: CatalogBundle | None = None) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    required = set(contract.node_sets)
    for card in cards:
        cid = card.get("canonical_id") or card.get("id")
        ctype = card.get("card_type")
        node_sets = set(card.get("node_sets") or card.get("ingestion_node_sets") or [])
        missing = sorted(required - node_sets)
        if missing:
            errors.append({"canonical_id": cid, "error": "returned_card_missing_required_nodesets", "missing": missing})
        if contract.allowed_card_types and ctype not in contract.allowed_card_types:
            errors.append({"canonical_id": cid, "error": "returned_card_type_not_allowed", "card_type": ctype})
        if catalogs is not None and cid:
            if not catalogs.known_card_id(str(cid)):
                warnings.append({"canonical_id": cid, "warning": "returned_card_not_in_generated_catalog"})
            else:
                authored = catalogs.authored_node_sets_for_card(str(cid))
                authored_missing = sorted(required - authored)
                if authored_missing:
                    errors.append(
                        {
                            "canonical_id": cid,
                            "error": "returned_card_catalog_node_sets_do_not_match_contract",
                            "missing_from_catalog": authored_missing,
                        }
                    )
    return {"ok": not errors, "errors": errors, "warnings": warnings, "returned_count": len(cards)}
