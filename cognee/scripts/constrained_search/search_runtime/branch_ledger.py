from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any

from .nodeset_contracts import SearchContract, SearchResult
from .utils import node_set_map, unique_in_order


BRANCH_SCOPE_KEYS = (
    "tenant_id",
    "group_id",
    "runtime_source_family",
    "platform_id",
    "platform_context_id",
    "platform_account_id",
    "account_data_binding_id",
    "source_role",
    "table_id",
)

EVIDENCE_FIELDS_BY_CARD_TYPE = {
    "platform_account": "platform_account_cards",
    "account_data_binding": "account_data_binding_cards",
    "table": "table_cards",
    "column": "column_cards",
    "query_pattern": "query_pattern_cards",
    "metric_implementation": "metric_implementation_cards",
}


@dataclass(slots=True)
class BranchState:
    branch_id: str
    scope: dict[str, str]
    status: str = "pending"
    missing_evidence: list[str] = field(default_factory=list)
    contract_ids: list[str] = field(default_factory=list)
    result_ids: list[str] = field(default_factory=list)
    stages: list[str] = field(default_factory=list)
    platform_account_cards: list[str] = field(default_factory=list)
    account_data_binding_cards: list[str] = field(default_factory=list)
    table_cards: list[str] = field(default_factory=list)
    column_cards: list[str] = field(default_factory=list)
    query_pattern_cards: list[str] = field(default_factory=list)
    metric_implementation_cards: list[str] = field(default_factory=list)
    contract_repairs: list[dict[str, Any]] = field(default_factory=list)
    contract_rejections: list[dict[str, Any]] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    blocked_reasons: list[str] = field(default_factory=list)
    executed_step_count: int = 0
    discovered_contract_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return {
            "branch_id": self.branch_id,
            "scope": self.scope,
            "status": self.status,
            "missing_evidence": self.missing_evidence,
            "contract_ids": self.contract_ids,
            "result_ids": self.result_ids,
            "stages": self.stages,
            "platform_account_cards": self.platform_account_cards,
            "account_data_binding_cards": self.account_data_binding_cards,
            "table_cards": self.table_cards,
            "column_cards": self.column_cards,
            "query_pattern_cards": self.query_pattern_cards,
            "metric_implementation_cards": self.metric_implementation_cards,
            "contract_repairs": self.contract_repairs,
            "contract_rejections": self.contract_rejections,
            "warnings": self.warnings,
            "blocked_reasons": self.blocked_reasons,
            "executed_step_count": self.executed_step_count,
            "discovered_contract_count": self.discovered_contract_count,
        }


class BranchLedger:
    """Tracks runtime-source branch lineage while the executor remains serial."""

    def __init__(self) -> None:
        self.branches: dict[str, BranchState] = {}
        self.branch_order: list[str] = []
        self.contract_branches: dict[str, str] = {}

    def record_contract_discovered(self, contract: SearchContract) -> str:
        branch = self._branch_for_scope(scope_from_contract(contract))
        branch.discovered_contract_count += 1
        add_unique(branch.contract_ids, contract.contract_id)
        add_unique(branch.stages, contract.stage)
        self.contract_branches[contract.contract_id] = branch.branch_id
        self._refresh_status(branch)
        return branch.branch_id

    def record_contract_started(self, contract: SearchContract) -> str:
        branch = self._branch_for_scope(scope_from_contract(contract))
        branch.executed_step_count += 1
        add_unique(branch.contract_ids, contract.contract_id)
        add_unique(branch.stages, contract.stage)
        self.contract_branches[contract.contract_id] = branch.branch_id
        if branch.status == "pending":
            branch.status = "in_progress"
        self._refresh_status(branch)
        return branch.branch_id

    def record_result(self, contract: SearchContract, result: SearchResult) -> list[str]:
        touched: list[str] = []
        started_branch_id = self.contract_branches.get(contract.contract_id) or branch_id_for_scope(scope_from_contract(contract))
        if not result.returned_cards:
            branch = self._branch_for_scope(scope_from_contract(contract))
            add_unique(branch.warnings, "contract_returned_no_cards")
            add_unique(branch.contract_ids, contract.contract_id)
            add_unique(branch.result_ids, result.result_id)
            self._refresh_status(branch)
            return [branch.branch_id]

        for card in result.returned_cards:
            card_scope = merged_scope(scope_from_contract(contract), scope_from_card(card))
            branch = self._branch_for_scope(card_scope)
            if branch.branch_id != started_branch_id:
                branch.executed_step_count += 1
            add_unique(branch.contract_ids, contract.contract_id)
            add_unique(branch.result_ids, result.result_id)
            add_unique(branch.stages, result.stage)
            self._record_card(branch, card)
            self._refresh_status(branch)
            add_unique(touched, branch.branch_id)
        return touched

    def record_contract_repairs(
        self,
        original_contract: SearchContract,
        repaired_contract: SearchContract | None,
        repairs: list[dict[str, Any]],
        rejections: list[dict[str, Any]],
    ) -> None:
        if not repairs and not rejections:
            return
        contract = repaired_contract or original_contract
        branch = self._branch_for_scope(scope_from_contract(contract))
        for repair in repairs:
            branch.contract_repairs.append(dict(repair))
        for rejection in rejections:
            branch.contract_rejections.append(dict(rejection))
            add_unique(branch.blocked_reasons, str(rejection.get("rejection") or "contract_repair_rejected"))
        add_unique(branch.contract_ids, original_contract.contract_id)
        if repaired_contract is not None:
            add_unique(branch.contract_ids, repaired_contract.contract_id)
        self._refresh_status(branch)

    def record_contract_validation_rejected(self, contract: SearchContract, validation: dict[str, Any]) -> None:
        branch = self._branch_for_scope(scope_from_contract(contract))
        branch.contract_rejections.append(
            {
                "rejection": "contract_validation_failed",
                "errors": list(validation.get("errors") or []),
                "warnings": list(validation.get("warnings") or []),
            }
        )
        for error in validation.get("errors") or []:
            add_unique(branch.blocked_reasons, str(error))
        add_unique(branch.contract_ids, contract.contract_id)
        self._refresh_status(branch)

    def record_contract_failed(self, contract: SearchContract, reason: str, error: str | None = None) -> None:
        branch = self._branch_for_scope(scope_from_contract(contract))
        payload = {"rejection": reason}
        if error:
            payload["error"] = error
        branch.contract_rejections.append(payload)
        add_unique(branch.blocked_reasons, reason)
        add_unique(branch.contract_ids, contract.contract_id)
        self._refresh_status(branch)

    def snapshot(self) -> dict[str, Any]:
        branch_dicts = {branch_id: self.branches[branch_id].to_dict() for branch_id in self.branch_order}
        branch_status = {branch_id: branch["status"] for branch_id, branch in branch_dicts.items()}
        branch_step_counts = {branch_id: branch["executed_step_count"] for branch_id, branch in branch_dicts.items()}
        usable_count = sum(1 for status in branch_status.values() if status == "usable")
        incomplete_count = sum(1 for status in branch_status.values() if status in {"pending", "in_progress", "partial", "blocked", "failed"})
        return {
            "branches": branch_dicts,
            "branch_status": branch_status,
            "branch_order": list(self.branch_order),
            "branch_step_counts": branch_step_counts,
            "usable_branch_count": usable_count,
            "incomplete_branch_count": incomplete_count,
        }

    def _branch_for_scope(self, scope: dict[str, str]) -> BranchState:
        branch_id = branch_id_for_scope(scope)
        branch = self.branches.get(branch_id)
        if branch is None:
            branch = BranchState(branch_id=branch_id, scope=scope)
            self.branches[branch_id] = branch
            self.branch_order.append(branch_id)
        else:
            branch.scope = merged_scope(branch.scope, scope)
        return branch

    def _record_card(self, branch: BranchState, card: dict[str, Any]) -> None:
        card_id = str(card.get("canonical_id") or card.get("id") or "")
        if not card_id:
            return
        card_type = str(card.get("card_type") or "")
        field_name = EVIDENCE_FIELDS_BY_CARD_TYPE.get(card_type)
        if not field_name:
            return
        add_unique(getattr(branch, field_name), card_id)

    def _refresh_status(self, branch: BranchState) -> None:
        branch.missing_evidence = missing_evidence(branch)
        if branch.contract_rejections and not has_any_evidence(branch):
            branch.status = "failed"
        elif has_usable_evidence(branch):
            branch.status = "usable"
        elif has_any_evidence(branch):
            branch.status = "partial"
        elif branch.executed_step_count:
            branch.status = "in_progress"
        else:
            branch.status = "pending"


def scope_from_contract(contract: SearchContract) -> dict[str, str]:
    values = scope_from_node_sets(contract.node_sets)
    for key in BRANCH_SCOPE_KEYS:
        value = contract.required_carry_forward.get(key)
        if value not in (None, "", []) and key not in values:
            values[key] = str(value)
    return values


def scope_from_card(card: dict[str, Any]) -> dict[str, str]:
    values = scope_from_node_sets(card.get("node_sets") or card.get("ingestion_node_sets") or [])
    canonical_id = str(card.get("canonical_id") or card.get("id") or "")
    card_type = str(card.get("card_type") or "")
    if canonical_id and card_type == "platform_account":
        values.setdefault("platform_account_id", canonical_id)
    if canonical_id and card_type == "account_data_binding":
        values.setdefault("account_data_binding_id", canonical_id)
    return values


def scope_from_node_sets(node_sets: list[str]) -> dict[str, str]:
    ns_map = node_set_map([str(node_set) for node_set in node_sets])
    values: dict[str, str] = {}
    for key in BRANCH_SCOPE_KEYS:
        node_values = unique_in_order(str(value) for value in ns_map.get(key) or [] if value)
        if len(node_values) == 1:
            values[key] = node_values[0]
    return values


def branch_id_for_scope(scope: dict[str, str]) -> str:
    if not scope:
        return "branch.unscoped"
    parts = [f"{key}={scope[key]}" for key in BRANCH_SCOPE_KEYS if scope.get(key)]
    digest = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()[:12]
    return f"branch.{digest}"


def merged_scope(base: dict[str, str], extra: dict[str, str]) -> dict[str, str]:
    merged = dict(base)
    for key in BRANCH_SCOPE_KEYS:
        value = extra.get(key)
        if value and key not in merged:
            merged[key] = value
    return merged


def has_any_evidence(branch: BranchState) -> bool:
    return any(
        [
            branch.platform_account_cards,
            branch.account_data_binding_cards,
            branch.table_cards,
            branch.column_cards,
            branch.query_pattern_cards,
            branch.metric_implementation_cards,
        ]
    )


def has_usable_evidence(branch: BranchState) -> bool:
    return bool(
        branch.account_data_binding_cards
        and branch.table_cards
        and (branch.query_pattern_cards or branch.metric_implementation_cards or branch.column_cards)
    )


def missing_evidence(branch: BranchState) -> list[str]:
    missing: list[str] = []
    if not branch.account_data_binding_cards:
        missing.append("runtime_binding")
    if not branch.table_cards:
        missing.append("table_frame")
    if not branch.query_pattern_cards and not branch.metric_implementation_cards and not branch.column_cards:
        missing.append("query_pattern_metric_or_columns")
    return missing


def add_unique(values: list[str], value: str) -> None:
    if value and value not in values:
        values.append(value)
