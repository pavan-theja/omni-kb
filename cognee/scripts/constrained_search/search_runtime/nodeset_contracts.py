from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class SearchContract:
    """One legal Cognee NodeSet search request."""

    contract_id: str
    stage: str
    query_text: str
    node_sets: list[str]
    top_k: int = 10
    datasets: list[str] = field(default_factory=list)
    predecessor_contract_id: str | None = None
    predecessor_result_id: str | None = None
    allowed_card_types: list[str] = field(default_factory=list)
    closed_gates: list[str] = field(default_factory=list)
    required_carry_forward: dict[str, Any] = field(default_factory=dict)
    candidate_seed_ids: list[str] = field(default_factory=list)
    exact_dereference_ids: list[str] = field(default_factory=list)
    llm_decision_id: str | None = None
    reason: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "contract_id": self.contract_id,
            "stage": self.stage,
            "query_text": self.query_text,
            "node_sets": self.node_sets,
            "top_k": self.top_k,
            "datasets": self.datasets,
            "predecessor_contract_id": self.predecessor_contract_id,
            "predecessor_result_id": self.predecessor_result_id,
            "allowed_card_types": self.allowed_card_types,
            "closed_gates": self.closed_gates,
            "required_carry_forward": self.required_carry_forward,
            "candidate_seed_ids": self.candidate_seed_ids,
            "exact_dereference_ids": self.exact_dereference_ids,
            "llm_decision_id": self.llm_decision_id,
            "reason": self.reason,
        }


@dataclass(slots=True)
class SearchResult:
    result_id: str
    contract_id: str
    stage: str
    returned_cards: list[dict[str, Any]]
    validation: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "result_id": self.result_id,
            "contract_id": self.contract_id,
            "stage": self.stage,
            "returned_cards": self.returned_cards,
            "validation": self.validation,
        }

