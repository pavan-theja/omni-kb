from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .catalogs import CatalogBundle
from .nodeset_contracts import SearchContract
from .utils import first_node_set, node_set_map, unique_in_order


STAGE_ALIASES = {
    "runtime_account_data_binding_search": "runtime_account_binding_search",
    "table_local_metric_search": "table_local_metric_implementation_search",
}

CARD_TYPE_ALIASES = {
    "metric": "metric_implementation",
}

CONTEXT_CARRY_FORWARD_KEYS = {
    "tenant_id",
    "group_id",
    "platform_account_id",
    "account_data_binding_id",
    "source_role",
    "table_id",
}


@dataclass(slots=True)
class ContractRepairResult:
    contract: SearchContract | None
    repairs: list[dict[str, Any]] = field(default_factory=list)
    rejections: list[dict[str, Any]] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.contract is not None and not self.rejections


def repair_contract(
    contract: SearchContract,
    catalogs: CatalogBundle | None = None,
    *,
    predecessor_cards: list[dict[str, Any]] | None = None,
) -> ContractRepairResult:
    """Apply deterministic SearchContract repairs before strict validation."""

    repairs: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []
    repaired = contract

    repaired, stage_repairs = repair_stage_alias(repaired)
    repairs.extend(stage_repairs)

    repaired, canonical_repairs = repair_canonical_node_sets(repaired, catalogs)
    repairs.extend(canonical_repairs)

    repaired, template_card_type_repairs = repair_template_card_type_alias(repaired, catalogs)
    repairs.extend(template_card_type_repairs)

    repaired, card_type_repairs, card_type_rejections = repair_missing_card_type(repaired, catalogs)
    repairs.extend(card_type_repairs)
    rejections.extend(card_type_rejections)

    repaired, carry_repairs, carry_rejections = repair_carry_forward(
        repaired,
        catalogs,
        predecessor_cards=predecessor_cards or [],
    )
    repairs.extend(carry_repairs)
    rejections.extend(carry_rejections)

    if rejections:
        return ContractRepairResult(contract=None, repairs=repairs, rejections=rejections)
    return ContractRepairResult(contract=repaired, repairs=repairs, rejections=rejections)


def repair_stage_alias(contract: SearchContract) -> tuple[SearchContract, list[dict[str, Any]]]:
    canonical_stage = STAGE_ALIASES.get(contract.stage)
    if not canonical_stage:
        return contract, []
    repaired = replace_contract(contract, stage=canonical_stage)
    return repaired, [
        {
            "repair": "stage_alias",
            "from": contract.stage,
            "to": canonical_stage,
        }
    ]


def repair_canonical_node_sets(
    contract: SearchContract,
    catalogs: CatalogBundle | None,
) -> tuple[SearchContract, list[dict[str, Any]]]:
    if catalogs is None:
        return contract, []

    repaired_node_sets: list[str] = []
    repairs: list[dict[str, Any]] = []
    for node_set in contract.node_sets:
        text = str(node_set)
        canonical = catalogs.canonicalize_node_set(text)
        repaired_node_sets.append(canonical)
        if canonical != text:
            repairs.append(
                {
                    "repair": "canonical_nodeset",
                    "from": text,
                    "to": canonical,
                }
            )

    repaired_node_sets = unique_in_order(repaired_node_sets)
    if repaired_node_sets == contract.node_sets:
        return contract, repairs
    return replace_contract(contract, node_sets=repaired_node_sets), repairs


def repair_template_card_type_alias(
    contract: SearchContract,
    catalogs: CatalogBundle | None,
) -> tuple[SearchContract, list[dict[str, Any]]]:
    if catalogs is None:
        return contract, []
    template_type = catalogs.card_type_for_contract_stage(contract.stage)
    if not template_type:
        return contract, []

    repairs: list[dict[str, Any]] = []
    node_sets: list[str] = []
    node_sets_changed = False
    for node_set in contract.node_sets:
        text = str(node_set)
        if text.startswith("card_type:"):
            value = text.split(":", 1)[1]
            repaired_value = CARD_TYPE_ALIASES.get(value, value)
            if value != template_type and repaired_value == template_type:
                text = f"card_type:{template_type}"
                node_sets_changed = True
                repairs.append(
                    {
                        "repair": "card_type_alias_nodeset",
                        "from": f"card_type:{value}",
                        "to": text,
                        "stage": contract.stage,
                    }
                )
        node_sets.append(text)

    allowed_card_types = list(contract.allowed_card_types)
    repaired_allowed_card_types: list[str] = []
    allowed_changed = False
    for card_type in allowed_card_types:
        repaired_card_type = CARD_TYPE_ALIASES.get(str(card_type), str(card_type))
        if str(card_type) != template_type and repaired_card_type == template_type:
            allowed_changed = True
            repairs.append(
                {
                    "repair": "allowed_card_type_alias",
                    "from": str(card_type),
                    "to": template_type,
                    "stage": contract.stage,
                }
            )
        repaired_allowed_card_types.append(repaired_card_type)

    if not node_sets_changed and not allowed_changed:
        return contract, repairs
    return replace_contract(
        contract,
        node_sets=unique_in_order(node_sets),
        allowed_card_types=unique_in_order(repaired_allowed_card_types),
    ), repairs


def repair_missing_card_type(
    contract: SearchContract,
    catalogs: CatalogBundle | None,
) -> tuple[SearchContract, list[dict[str, Any]], list[dict[str, Any]]]:
    if first_node_set(contract.node_sets, "card_type") is not None:
        return contract, [], []
    if not contract.allowed_card_types:
        return contract, [], []
    if len(contract.allowed_card_types) != 1:
        return contract, [], [
            {
                "rejection": "ambiguous_card_type_repair",
                "allowed_card_types": list(contract.allowed_card_types),
            }
        ]

    allowed_type = str(contract.allowed_card_types[0])
    template_type = catalogs.card_type_for_contract_stage(contract.stage) if catalogs else None
    if template_type is None:
        return contract, [], []
    if template_type != allowed_type:
        return contract, [], [
            {
                "rejection": "card_type_repair_conflicts_with_stage_template",
                "allowed_card_type": allowed_type,
                "template_card_type": template_type,
            }
        ]

    repaired = replace_contract(contract, node_sets=unique_in_order([*contract.node_sets, f"card_type:{allowed_type}"]))
    return repaired, [
        {
            "repair": "missing_card_type_nodeset",
            "added": f"card_type:{allowed_type}",
            "allowed_card_type": allowed_type,
            "stage": contract.stage,
        }
    ], []


def repair_carry_forward(
    contract: SearchContract,
    catalogs: CatalogBundle | None,
    *,
    predecessor_cards: list[dict[str, Any]],
) -> tuple[SearchContract, list[dict[str, Any]], list[dict[str, Any]]]:
    if not predecessor_cards:
        return contract, [], []

    required_node_keys = required_node_set_keys(contract, catalogs)
    keys_to_fill = set(required_node_keys) & CONTEXT_CARRY_FORWARD_KEYS
    keys_to_fill.update(
        key
        for key, value in contract.required_carry_forward.items()
        if key in CONTEXT_CARRY_FORWARD_KEYS and value in (None, "", [])
    )
    if not keys_to_fill:
        return contract, [], []

    context_values = carry_forward_values(predecessor_cards)
    ns_map = node_set_map(contract.node_sets)
    node_sets = list(contract.node_sets)
    carry_forward = dict(contract.required_carry_forward)
    repairs: list[dict[str, Any]] = []
    rejections: list[dict[str, Any]] = []

    for key in sorted(keys_to_fill):
        values = sorted(context_values.get(key) or [])
        if not values:
            continue
        has_node_set = key in ns_map
        has_carry_value = carry_forward.get(key) not in (None, "", [])
        if has_node_set and has_carry_value:
            continue
        if len(values) > 1:
            rejections.append(
                {
                    "rejection": "ambiguous_carry_forward",
                    "key": key,
                    "values": values,
                }
            )
            continue
        value = values[0]
        if not has_node_set and key in required_node_keys:
            node_set = f"{key}:{value}"
            node_sets.append(node_set)
            repairs.append(
                {
                    "repair": "carry_forward_nodeset",
                    "key": key,
                    "added": node_set,
                }
            )
        if not has_carry_value:
            carry_forward[key] = value
            repairs.append(
                {
                    "repair": "carry_forward_metadata",
                    "key": key,
                    "value": value,
                }
            )

    if rejections:
        return contract, repairs, rejections
    if node_sets == contract.node_sets and carry_forward == contract.required_carry_forward:
        return contract, repairs, []
    return replace_contract(contract, node_sets=unique_in_order(node_sets), required_carry_forward=carry_forward), repairs, []


def required_node_set_keys(contract: SearchContract, catalogs: CatalogBundle | None) -> set[str]:
    if catalogs is None:
        return set()
    template = catalogs.template_for_stage(contract.stage) or {}
    return set(str(key) for key in template.get("required_node_set_keys") or [])


def carry_forward_values(cards: list[dict[str, Any]]) -> dict[str, set[str]]:
    values: dict[str, set[str]] = {key: set() for key in CONTEXT_CARRY_FORWARD_KEYS}
    for card in cards:
        node_sets = [str(node_set) for node_set in card.get("node_sets") or card.get("ingestion_node_sets") or []]
        ns_map = node_set_map(node_sets)
        for key in CONTEXT_CARRY_FORWARD_KEYS:
            for value in ns_map.get(key) or []:
                if value:
                    values[key].add(str(value))

        card_id = str(card.get("canonical_id") or card.get("id") or "")
        card_type = str(card.get("card_type") or "")
        if card_id and card_type == "platform_account":
            values["platform_account_id"].add(card_id)
        if card_id and card_type == "account_data_binding":
            values["account_data_binding_id"].add(card_id)

    return {key: value for key, value in values.items() if value}


def replace_contract(contract: SearchContract, **updates: Any) -> SearchContract:
    return SearchContract(**{**contract.to_dict(), **updates})
