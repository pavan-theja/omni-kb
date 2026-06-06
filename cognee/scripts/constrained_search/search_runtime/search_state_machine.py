from __future__ import annotations

from pathlib import Path
from typing import Any

from .branch_ledger import BranchLedger, branch_id_for_scope, scope_from_contract
from .catalogs import CatalogBundle
from .cognee_client import CogneeClient
from .contract_repair import ContractRepairResult, repair_contract
from .contract_validator import validate_contract, validate_returned_cards
from .llm_plane import LLMPlane
from .nodeset_contracts import SearchContract, SearchResult
from .utils import unique_in_order, write_json


COMPLETION_POLICIES = {"strict", "partial", "best_effort"}


class CogneeSearchStateMachine:
    """Sequential Cognee NodeSet search orchestrator."""

    def __init__(
        self,
        cognee_client: CogneeClient,
        llm_plane: LLMPlane,
        trace_dir: str | Path,
        catalogs: CatalogBundle | None = None,
        max_steps: int = 30,
        branch_max_steps: int = 8,
        max_pending: int = 32,
        completion_policy: str = "best_effort",
    ):
        if completion_policy not in COMPLETION_POLICIES:
            raise ValueError(f"completion_policy must be one of {sorted(COMPLETION_POLICIES)}")
        self.cognee_client = cognee_client
        self.llm_plane = llm_plane
        self.trace_dir = Path(trace_dir)
        self.trace_dir.mkdir(parents=True, exist_ok=True)
        self.catalogs = catalogs
        self.max_steps = max_steps
        self.branch_max_steps = branch_max_steps
        self.max_pending = max_pending
        self.completion_policy = completion_policy
        self.trace: list[dict[str, Any]] = []
        self.branch_ledger = BranchLedger()

    async def execute_contract(self, contract: SearchContract) -> SearchResult:
        repair = repair_contract(contract, self.catalogs)
        self._trace_repair_result("contract_execution", contract, repair)
        if not repair.ok or repair.contract is None:
            raise ValueError(f"Contract repair rejected execution contract: {repair.rejections}")

        contract = repair.contract
        routed_contract = self.cognee_client.with_routed_datasets(contract)
        self.branch_ledger.record_contract_started(routed_contract)
        contract_validation = validate_contract(routed_contract, self.catalogs)
        self.trace.append(
            {
                "event": "contract_validated",
                "contract": routed_contract.to_dict(),
                "dataset_routing": {
                    "requested_dataset_count": len(contract.datasets),
                    "effective_dataset_count": len(routed_contract.datasets),
                    "datasets": routed_contract.datasets,
                },
                "validation": contract_validation,
            }
        )
        if not contract_validation["ok"]:
            self.branch_ledger.record_contract_validation_rejected(routed_contract, contract_validation)
            raise ValueError(f"Invalid contract: {contract_validation['errors']}")

        try:
            cards = await self.cognee_client.search(routed_contract)
        except Exception as exc:  # noqa: BLE001
            self.branch_ledger.record_contract_failed(routed_contract, "cognee_search_failed", repr(exc))
            raise
        if not cards:
            fallback_cards = local_exact_catalog_cards_for_contract(routed_contract, self.catalogs)
            if fallback_cards:
                self.trace.append(
                    {
                        "event": "local_exact_catalog_fallback",
                        "contract_id": routed_contract.contract_id,
                        "stage": routed_contract.stage,
                        "card_ids": card_ids(fallback_cards),
                    }
                )
                cards = fallback_cards

        result_validation = validate_returned_cards(routed_contract, cards, self.catalogs)
        result = SearchResult(
            result_id=f"result.{routed_contract.contract_id}",
            contract_id=routed_contract.contract_id,
            stage=routed_contract.stage,
            returned_cards=cards,
            validation=result_validation,
        )
        touched_branch_ids = self.branch_ledger.record_result(routed_contract, result)
        self.trace.append({"event": "cognee_result_validated", "result": result.to_dict()})
        self.trace.append(
            {
                "event": "branch_ledger_result_recorded",
                "contract_id": routed_contract.contract_id,
                "result_id": result.result_id,
                "branch_ids": touched_branch_ids,
            }
        )
        if not result_validation["ok"]:
            self.branch_ledger.record_contract_failed(
                routed_contract,
                "returned_card_validation_failed",
                repr(result_validation["errors"]),
            )
            raise ValueError(f"Cognee returned cards outside contract boundary: {result_validation['errors']}")
        return result

    def _coerce_contracts(
        self,
        raw_contracts: list[dict[str, Any]],
        source_event: str,
        query_text: str = "",
        predecessor_cards: list[dict[str, Any]] | None = None,
        predecessor_contract: SearchContract | None = None,
    ) -> list[SearchContract]:
        contracts: list[SearchContract] = []
        for idx, raw in enumerate(raw_contracts):
            try:
                contract = SearchContract(**raw)
            except TypeError as exc:
                self.trace.append(
                    {
                        "event": "invalid_llm_contract_shape",
                        "source_event": source_event,
                        "index": idx,
                        "raw": raw,
                        "error": repr(exc),
                    }
                )
                continue
            if predecessor_contract is not None:
                contract = inherit_required_carry_forward(contract, predecessor_contract)
            raw_contract = contract.to_dict()
            raw_node_sets = list(contract.node_sets)
            repair = repair_contract(contract, self.catalogs, predecessor_cards=predecessor_cards or [])
            self._trace_repair_result(source_event, contract, repair, index=idx)
            if not repair.ok or repair.contract is None:
                continue
            contract = repair.contract
            for expanded_contract in self._expand_runtime_platform_account_contract(contract, source_event, query_text):
                validation = validate_contract(expanded_contract, self.catalogs)
                self.trace.append(
                    {
                        "event": "llm_contract_candidate_validated",
                        "source_event": source_event,
                        "contract": expanded_contract.to_dict(),
                        "normalization": {
                            "stage_changed": raw_contract["stage"] != expanded_contract.stage,
                            "node_sets_changed": raw_node_sets != expanded_contract.node_sets,
                            "raw_node_sets": raw_node_sets,
                            "canonical_node_sets": expanded_contract.node_sets,
                        },
                        "validation": validation,
                    }
                )
                if validation["ok"]:
                    branch_id = self.branch_ledger.record_contract_discovered(expanded_contract)
                    self.trace.append(
                        {
                            "event": "branch_ledger_contract_discovered",
                            "source_event": source_event,
                            "contract_id": expanded_contract.contract_id,
                            "branch_id": branch_id,
                        }
                    )
                    contracts.append(expanded_contract)
                else:
                    self.branch_ledger.record_contract_validation_rejected(expanded_contract, validation)
                    self.trace.append(
                        {
                            "event": "llm_contract_candidate_rejected",
                            "source_event": source_event,
                            "index": idx,
                            "contract": expanded_contract.to_dict(),
                            "validation": validation,
                        }
                    )
        return contracts

    def _trace_repair_result(
        self,
        source_event: str,
        original_contract: SearchContract,
        repair: ContractRepairResult,
        *,
        index: int | None = None,
    ) -> None:
        self.branch_ledger.record_contract_repairs(original_contract, repair.contract, repair.repairs, repair.rejections)
        if repair.repairs:
            self.trace.append(
                {
                    "event": "contract_repaired",
                    "source_event": source_event,
                    "index": index,
                    "original_contract": original_contract.to_dict(),
                    "repaired_contract": repair.contract.to_dict() if repair.contract else None,
                    "repairs": repair.repairs,
                }
            )
        if repair.rejections:
            self.trace.append(
                {
                    "event": "contract_repair_rejected",
                    "source_event": source_event,
                    "index": index,
                    "contract": original_contract.to_dict(),
                    "repairs": repair.repairs,
                    "rejections": repair.rejections,
                }
            )

    def _expand_runtime_platform_account_contract(
        self,
        contract: SearchContract,
        source_event: str,
        query_text: str,
    ) -> list[SearchContract]:
        if not should_expand_runtime_platform_account_contract(contract):
            return [contract]

        platform_ids = runtime_platform_account_platform_ids(self.catalogs, contract, query_text)
        if not platform_ids:
            self.trace.append(
                {
                    "event": "runtime_platform_account_contract_expansion_failed",
                    "source_event": source_event,
                    "contract": contract.to_dict(),
                    "reason": "no_matching_platform_account_rows_in_catalog",
                }
            )
            return [contract]

        expanded: list[SearchContract] = []
        base_node_sets = [node_set for node_set in contract.node_sets if not str(node_set).startswith("platform_id:")]
        for platform_id in platform_ids:
            suffix = platform_id.replace("platform.", "").replace(".", "_")
            expanded.append(
                SearchContract(
                    **{
                        **contract.to_dict(),
                        "contract_id": f"{contract.contract_id}.{suffix}",
                        "query_text": f"{contract.query_text} ({platform_id})",
                        "node_sets": base_node_sets + [f"platform_id:{platform_id}"],
                    }
                )
            )

        self.trace.append(
            {
                "event": "runtime_platform_account_contract_expanded",
                "source_event": source_event,
                "original_contract": contract.to_dict(),
                "expanded_platform_ids": platform_ids,
                "expanded_contract_ids": [item.contract_id for item in expanded],
            }
        )
        return expanded

    async def run_query(self, query_text: str, runtime_context: dict[str, Any]) -> dict[str, Any]:
        try:
            anchor = await self.llm_plane.extract_anchors(query_text, runtime_context)
        except Exception as exc:  # noqa: BLE001
            return self._blocked("anchor_extractor_failed", {"error": repr(exc)})

        anchor_decision = anchor.to_dict()
        self.trace.append({"event": "llm_anchor_decision", "decision": anchor_decision})

        pending = self._coerce_contracts(
            anchor.validated_output.get("next_search_contracts", []),
            "anchor_extractor",
            query_text,
        )
        if not pending:
            return self._blocked("anchor_extractor_did_not_emit_valid_runtime_nodeset_contracts")

        results: list[SearchResult] = []
        executed_signatures: set[tuple[Any, ...]] = set()
        pending = self._prepare_pending(pending, query_text, results, executed_signatures)
        steps = 0
        while pending and steps < self.max_steps:
            contract = pending.pop(0)
            signature = contract_signature(contract)
            if signature in executed_signatures:
                continue
            executed_signatures.add(signature)
            steps += 1
            try:
                result = await self.execute_contract(contract)
            except Exception as exc:  # noqa: BLE001
                return self._blocked("contract_execution_failed", {"contract": contract.to_dict(), "error": repr(exc)})
            results.append(result)

            route_selection = await self._select_route_next_contracts(
                query_text,
                runtime_context,
                anchor_decision,
                result,
                contract,
            )
            if route_selection is not None:
                route_results, route_contracts = route_selection
                results.extend(route_results)
                pending.extend(route_contracts)
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)
                continue

            runtime_candidates = runtime_candidate_cards(result.returned_cards)
            if runtime_candidates:
                try:
                    selector_decision = await self.llm_plane.select_runtime_bindings(
                        query_text,
                        anchor_decision,
                        runtime_candidates,
                    )
                except Exception as exc:  # noqa: BLE001
                    self.trace.append(
                        {
                            "event": "llm_runtime_binding_decision_failed",
                            "result": result.to_dict(),
                            "error": repr(exc),
                            "continuing_with_pending_count": len(pending),
                        }
                    )
                else:
                    self.trace.append({"event": "llm_runtime_binding_decision", "decision": selector_decision.to_dict()})
                    pending.extend(
                        self._coerce_contracts(
                            selector_decision.validated_output.get("next_search_contracts", []),
                            "runtime_binding_selector",
                            query_text,
                            predecessor_cards=result.returned_cards,
                            predecessor_contract=contract,
                        )
                    )
                    pending = self._prepare_pending(pending, query_text, results, executed_signatures)

            try:
                planner_decision = await self.llm_plane.plan_next_nodesets(
                    query_text,
                    {
                        **result.to_dict(),
                        "predecessor_contract": contract.to_dict(),
                    },
                )
            except Exception as exc:  # noqa: BLE001
                self.trace.append(
                    {
                        "event": "llm_next_nodeset_decision_failed",
                        "result": result.to_dict(),
                        "error": repr(exc),
                        "continuing_with_pending_count": len(pending),
                    }
                )
            else:
                self.trace.append({"event": "llm_next_nodeset_decision", "decision": planner_decision.to_dict()})
                pending.extend(
                    self._coerce_contracts(
                        planner_decision.validated_output.get("next_search_contracts", []),
                        "next_nodeset_planner",
                        query_text,
                        predecessor_cards=result.returned_cards,
                        predecessor_contract=contract,
                    )
                )
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)

            try:
                rank_decision = await self.llm_plane.rank_bounded_candidates(query_text, contract, result.returned_cards)
            except Exception as exc:  # noqa: BLE001
                self.trace.append(
                    {
                        "event": "llm_bounded_rank_decision_failed",
                        "contract": contract.to_dict(),
                        "error": repr(exc),
                        "continuing_with_pending_count": len(pending),
                    }
                )
            else:
                self.trace.append({"event": "llm_bounded_rank_decision", "decision": rank_decision.to_dict()})
                pending.extend(
                    self._coerce_contracts(
                        rank_decision.validated_output.get("next_search_contracts", []),
                        "bounded_candidate_ranker",
                        query_text,
                        predecessor_cards=result.returned_cards,
                        predecessor_contract=contract,
                    )
                )
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)

        if pending:
            terminal = terminal_evidence_status(query_text, runtime_context, results)
            return await self._complete_or_block(
                "max_steps_exhausted_before_pending_contracts_completed",
                {
                    "steps_executed": steps,
                    "global_step_count": steps,
                    "terminal_evidence": terminal,
                    "pending_count": len(pending),
                    "pending_contracts": [contract.to_dict() for contract in pending[:20]],
                },
                query_text,
                runtime_context,
                results,
                steps,
                terminal,
                pending,
            )

        terminal = terminal_evidence_status(query_text, runtime_context, results)
        if not terminal["ready"]:
            return await self._complete_or_block(
                "search_exhausted_without_terminal_evidence",
                {
                    "steps_executed": steps,
                    "global_step_count": steps,
                    "terminal_evidence": terminal,
                },
                query_text,
                runtime_context,
                results,
                steps,
                terminal,
                pending,
            )

        return await self._complete(query_text, runtime_context, results, steps, terminal, pending)

    def _prepare_pending(
        self,
        pending: list[SearchContract],
        query_text: str,
        results: list[SearchResult],
        executed_signatures: set[tuple[Any, ...]],
    ) -> list[SearchContract]:
        prepared = prune_and_rank_pending(
            pending,
            query_text,
            results,
            executed_signatures,
            max_pending=self.max_pending,
            branch_ledger=self.branch_ledger,
            branch_max_steps=self.branch_max_steps,
        )
        pending_branch_ids = [scheduler_branch_id(contract, self.branch_ledger) for contract in prepared[:20]]
        branch_snapshot = self.branch_ledger.snapshot()
        self.trace.append(
            {
                "event": "pending_queue_prepared",
                "pending_count": len(prepared),
                "max_pending": self.max_pending,
                "branch_max_steps": self.branch_max_steps,
                "pending_contract_ids": [contract.contract_id for contract in prepared[:20]],
                "pending_branch_ids": pending_branch_ids,
                "pending_branch_status": {
                    branch_id: branch_snapshot["branch_status"].get(branch_id)
                    for branch_id in pending_branch_ids
                    if branch_id
                },
                "pending_branch_step_counts": {
                    branch_id: branch_snapshot["branch_step_counts"].get(branch_id, 0)
                    for branch_id in pending_branch_ids
                    if branch_id
                },
            }
        )
        return prepared

    def _can_finalize_on_terminal(self) -> bool:
        if self.completion_policy != "strict":
            return True
        return not incomplete_branch_ids(self.branch_ledger.snapshot())

    async def _complete_or_block(
        self,
        blocked_reason: str,
        extra: dict[str, Any],
        query_text: str,
        runtime_context: dict[str, Any],
        results: list[SearchResult],
        steps: int,
        terminal: dict[str, Any],
        pending: list[SearchContract],
    ) -> dict[str, Any]:
        decision = completion_decision(self.completion_policy, self.branch_ledger.snapshot())
        if decision["status"] in {"complete", "best_effort", "partial"}:
            return await self._complete(query_text, runtime_context, results, steps, terminal, pending)
        return self._blocked(blocked_reason, extra)

    async def _complete(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        results: list[SearchResult],
        steps: int,
        terminal: dict[str, Any],
        pending: list[SearchContract],
    ) -> dict[str, Any]:
        branch_snapshot = self.branch_ledger.snapshot()
        decision = completion_decision(self.completion_policy, branch_snapshot)
        evidence_pack = build_evidence_pack(
            query_text,
            runtime_context,
            results,
            terminal,
            branch_snapshot=branch_snapshot,
            usable_branch_ids=decision["usable_branch_ids"],
        )
        if decision["write_handoff"]:
            try:
                handoff = await self.llm_plane.write_sql_handoff(query_text, evidence_pack)
                handoff_payload = handoff.to_dict()
            except Exception as exc:  # noqa: BLE001
                handoff_payload = {"error": repr(exc)}
        else:
            handoff_payload = {"status": "skipped", "reason": decision["handoff_skip_reason"]}

        output = {
            "status": decision["status"],
            "blocked_reason": decision["blocked_reason"],
            "completion_reason": decision["completion_reason"],
            "completion_policy": self.completion_policy,
            "steps_executed": steps,
            "global_step_count": steps,
            "terminal_evidence": terminal,
            "handoff": handoff_payload,
            "evidence_pack": evidence_pack,
            "usable_branch_ids": decision["usable_branch_ids"],
            "incomplete_branch_ids": decision["incomplete_branch_ids"],
            "best_effort_warnings": decision["warnings"],
            "pending_count_at_completion": len(pending),
            "results": [result.to_dict() for result in results],
            "trace_path": str(self.trace_dir / "last_search_trace.json"),
            "trace": self.trace,
        }
        output.update(branch_snapshot)
        output["usable_branch_count"] = len(decision["usable_branch_ids"])
        output["incomplete_branch_count"] = len(decision["incomplete_branch_ids"])
        write_json(output["trace_path"], output)
        return output

    async def _select_route_next_contracts(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        anchor_decision: dict[str, Any],
        result: SearchResult,
        predecessor_contract: SearchContract,
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        if result.stage == "runtime_platform_account_search":
            platform_account_cards = cards_of_type(result.returned_cards, "platform_account")
            route_selection = await self._select_platform_accounts_for_bindings(
                query_text,
                anchor_decision,
                result,
                platform_account_cards,
            )
            return route_selection or self._empty_route_selection(result, "platform_account_selection")

        if result.stage == "runtime_account_binding_search":
            binding_cards = cards_of_type(result.returned_cards, "account_data_binding")
            route_selection = await self._select_bindings_for_domains(
                query_text,
                runtime_context,
                anchor_decision,
                result,
                predecessor_contract,
                binding_cards,
            )
            return route_selection or self._empty_route_selection(result, "binding_selection")

        if result.stage == "semantic_domain_search":
            domain_cards = cards_of_type(result.returned_cards, "domain")
            route_selection = await self._select_domains_for_tables(
                query_text,
                result,
                predecessor_contract,
                domain_cards,
            )
            return route_selection or self._empty_route_selection(result, "domain_selection")

        if result.stage == "semantic_domain_table_search":
            table_cards = cards_of_type(result.returned_cards, "table")
            route_selection = await self._finalize_tables_from_domain_result(
                query_text,
                runtime_context,
                result,
                predecessor_contract,
                table_cards,
            )
            return route_selection or self._empty_route_selection(result, "domain_table_finalization")

        return None

    def _empty_route_selection(self, result: SearchResult, source_event: str) -> tuple[list[SearchResult], list[SearchContract]]:
        self.trace.append(
            {
                "event": "route_stage_no_next_contracts",
                "source_event": source_event,
                "result_id": result.result_id,
                "contract_id": result.contract_id,
                "stage": result.stage,
                "returned_count": len(result.returned_cards),
            }
        )
        return [], []

    async def _select_platform_accounts_for_bindings(
        self,
        query_text: str,
        anchor_decision: dict[str, Any],
        result: SearchResult,
        platform_account_cards: list[dict[str, Any]],
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        try:
            selector_decision = await self.llm_plane.select_runtime_bindings(
                query_text,
                anchor_decision,
                [compact_route_candidate(card) for card in platform_account_cards],
            )
        except Exception as exc:  # noqa: BLE001
            self.trace.append(
                {
                    "event": "llm_platform_account_selection_failed",
                    "result": result.to_dict(),
                    "error": repr(exc),
                }
            )
            return None

        selected_ids = selector_decision.validated_output.get("selected_platform_account_ids") or []
        selected_cards = select_cards_by_id(platform_account_cards, selected_ids)
        binding_contracts = binding_search_contracts_from_platform_accounts(selected_cards, query_text)
        self.trace.append(
            {
                "event": "platform_accounts_selected_for_binding_search",
                "decision": selector_decision.to_dict(),
                "selected_platform_account_ids": [card_id(card) for card in selected_cards],
                "binding_contract_ids": [contract.contract_id for contract in binding_contracts],
            }
        )
        for contract in binding_contracts:
            validation = validate_contract(contract, self.catalogs)
            self.trace.append(
                {
                    "event": "route_contract_validated",
                    "source_event": "platform_account_selection",
                    "contract": contract.to_dict(),
                    "validation": validation,
                }
            )
            if validation["ok"]:
                branch_id = self.branch_ledger.record_contract_discovered(contract)
                self.trace.append(
                    {
                        "event": "branch_ledger_contract_discovered",
                        "source_event": "platform_account_selection",
                        "contract_id": contract.contract_id,
                        "branch_id": branch_id,
                    }
                )
            else:
                self.branch_ledger.record_contract_validation_rejected(contract, validation)
        binding_contracts = [contract for contract in binding_contracts if validate_contract(contract, self.catalogs)["ok"]]
        if not binding_contracts:
            return None
        return [], binding_contracts

    async def _select_bindings_for_domains(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        anchor_decision: dict[str, Any],
        result: SearchResult,
        predecessor_contract: SearchContract,
        binding_cards: list[dict[str, Any]],
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        candidates = runtime_binding_inventory_candidates(
            self.catalogs,
            binding_cards,
            runtime_context,
        )
        if not candidates:
            return None

        try:
            selector_decision = await self.llm_plane.select_runtime_bindings(
                query_text,
                anchor_decision,
                [binding_route_candidate(candidate) for candidate in candidates],
            )
        except Exception as exc:  # noqa: BLE001
            self.trace.append(
                {
                    "event": "llm_binding_selection_failed",
                    "result": result.to_dict(),
                    "error": repr(exc),
                }
            )
            return None

        selected_candidates = selected_binding_candidates_from_ids(
            selector_decision.validated_output.get("selected_binding_ids") or [],
            candidates,
        )
        selected_binding_results = self._record_runtime_binding_inventory_selection(selected_candidates)
        domain_contracts = domain_search_contracts_from_binding_candidates(selected_candidates, query_text)
        self.trace.append(
            {
                "event": "runtime_bindings_selected_for_domain_search",
                "decision": selector_decision.to_dict(),
                "selected_binding_ids": [candidate["account_data_binding_id"] for candidate in selected_candidates],
                "domain_contract_ids": [contract.contract_id for contract in domain_contracts],
            }
        )
        for contract in domain_contracts:
            validation = validate_contract(contract, self.catalogs)
            self.trace.append(
                {
                    "event": "route_contract_validated",
                    "source_event": "binding_selection",
                    "contract": contract.to_dict(),
                    "validation": validation,
                }
            )
            if validation["ok"]:
                branch_id = self.branch_ledger.record_contract_discovered(contract)
                self.trace.append(
                    {
                        "event": "branch_ledger_contract_discovered",
                        "source_event": "binding_selection",
                        "contract_id": contract.contract_id,
                        "branch_id": branch_id,
                    }
                )
            else:
                self.branch_ledger.record_contract_validation_rejected(contract, validation)
        domain_contracts = [contract for contract in domain_contracts if validate_contract(contract, self.catalogs)["ok"]]
        if not domain_contracts:
            return None
        return selected_binding_results, domain_contracts

    async def _select_domains_for_tables(
        self,
        query_text: str,
        result: SearchResult,
        predecessor_contract: SearchContract,
        domain_cards: list[dict[str, Any]],
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        try:
            rank_decision = await self.llm_plane.rank_bounded_candidates(query_text, predecessor_contract, domain_cards)
        except Exception as exc:  # noqa: BLE001
            self.trace.append(
                {
                    "event": "llm_domain_selection_failed",
                    "result": result.to_dict(),
                    "error": repr(exc),
                }
            )
            return None

        selected_cards = domains_compatible_with_carry_table(
            select_cards_by_id(domain_cards, rank_decision.validated_output.get("selected_card_ids") or []),
            predecessor_contract.required_carry_forward,
        )
        table_contracts = domain_table_search_contracts_from_domain_cards(selected_cards, predecessor_contract)
        self.trace.append(
            {
                "event": "domains_selected_for_table_search",
                "decision": rank_decision.to_dict(),
                "selected_domain_ids": [card_id(card) for card in selected_cards],
                "table_contract_ids": [contract.contract_id for contract in table_contracts],
            }
        )
        for contract in table_contracts:
            validation = validate_contract(contract, self.catalogs)
            self.trace.append(
                {
                    "event": "route_contract_validated",
                    "source_event": "domain_selection",
                    "contract": contract.to_dict(),
                    "validation": validation,
                }
            )
            if validation["ok"]:
                branch_id = self.branch_ledger.record_contract_discovered(contract)
                self.trace.append(
                    {
                        "event": "branch_ledger_contract_discovered",
                        "source_event": "domain_selection",
                        "contract_id": contract.contract_id,
                        "branch_id": branch_id,
                    }
                )
            else:
                self.branch_ledger.record_contract_validation_rejected(contract, validation)
        table_contracts = [contract for contract in table_contracts if validate_contract(contract, self.catalogs)["ok"]]
        if not table_contracts:
            return None
        return [], table_contracts

    async def _finalize_tables_from_domain_result(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        result: SearchResult,
        predecessor_contract: SearchContract,
        table_cards: list[dict[str, Any]],
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        if len(table_cards) == 1:
            selected_cards = table_cards
            selection_mode = "deterministic_single_table"
            decision_payload = None
        else:
            try:
                rank_decision = await self.llm_plane.rank_bounded_candidates(query_text, predecessor_contract, table_cards)
            except Exception as exc:  # noqa: BLE001
                self.trace.append(
                    {
                        "event": "llm_table_selection_failed",
                        "result": result.to_dict(),
                        "error": repr(exc),
                    }
                )
                return None
            selected_cards = select_cards_by_id(table_cards, rank_decision.validated_output.get("selected_card_ids") or [])
            selection_mode = "llm_multi_table"
            decision_payload = rank_decision.to_dict()

        verified_candidates, rejected = verify_table_cards_have_runtime_bindings(
            self.catalogs,
            selected_cards,
            runtime_context,
            predecessor_contract,
        )
        table_contracts = table_frame_contracts_from_binding_candidates(verified_candidates)
        self.trace.append(
            {
                "event": "domain_tables_finalized",
                "selection_mode": selection_mode,
                "decision": decision_payload,
                "selected_table_ids": [card_id(card) for card in selected_cards],
                "verified_binding_ids": [candidate["account_data_binding_id"] for candidate in verified_candidates],
                "verified_table_ids": [candidate["table_id"] for candidate in verified_candidates],
                "rejected": rejected,
                "table_contract_ids": [contract.contract_id for contract in table_contracts],
            }
        )
        for contract in table_contracts:
            validation = validate_contract(contract, self.catalogs)
            self.trace.append(
                {
                    "event": "route_contract_validated",
                    "source_event": "domain_table_finalization",
                    "contract": contract.to_dict(),
                    "validation": validation,
                }
            )
            if validation["ok"]:
                branch_id = self.branch_ledger.record_contract_discovered(contract)
                self.trace.append(
                    {
                        "event": "branch_ledger_contract_discovered",
                        "source_event": "domain_table_finalization",
                        "contract_id": contract.contract_id,
                        "branch_id": branch_id,
                    }
                )
            else:
                self.branch_ledger.record_contract_validation_rejected(contract, validation)
        table_contracts = [contract for contract in table_contracts if validate_contract(contract, self.catalogs)["ok"]]
        if not table_contracts:
            return None
        return [], table_contracts

    async def _select_runtime_binding_inventory(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        anchor_decision: dict[str, Any],
        result: SearchResult,
    ) -> tuple[list[SearchResult], list[SearchContract]] | None:
        candidates = runtime_binding_inventory_candidates(
            self.catalogs,
            result.returned_cards,
            runtime_context,
        )
        if not candidates:
            return None

        self.trace.append(
            {
                "event": "runtime_binding_inventory_candidates",
                "source_result_id": result.result_id,
                "candidate_count": len(candidates),
                "candidate_ids": [candidate["account_data_binding_id"] for candidate in candidates[:50]],
            }
        )
        try:
            selector_decision = await self.llm_plane.select_runtime_bindings(
                query_text,
                anchor_decision,
                [llm_binding_inventory_candidate(candidate) for candidate in candidates],
            )
        except Exception as exc:  # noqa: BLE001
            self.trace.append(
                {
                    "event": "llm_runtime_binding_inventory_decision_failed",
                    "result": result.to_dict(),
                    "error": repr(exc),
                }
            )
            return None

        decision = selector_decision.to_dict()
        self.trace.append({"event": "llm_runtime_binding_inventory_decision", "decision": decision})
        selected_candidates = selected_binding_inventory_candidates(selector_decision.validated_output, candidates)
        selected_binding_results = self._record_runtime_binding_inventory_selection(selected_candidates)
        table_contracts = table_frame_contracts_from_binding_candidates(selected_candidates)
        for table_contract in table_contracts:
            validation = validate_contract(table_contract, self.catalogs)
            self.trace.append(
                {
                    "event": "inventory_table_frame_contract_validated",
                    "source_event": "runtime_binding_inventory_selector",
                    "contract": table_contract.to_dict(),
                    "validation": validation,
                }
            )
            if validation["ok"]:
                branch_id = self.branch_ledger.record_contract_discovered(table_contract)
                self.trace.append(
                    {
                        "event": "branch_ledger_contract_discovered",
                        "source_event": "runtime_binding_inventory_selector",
                        "contract_id": table_contract.contract_id,
                        "branch_id": branch_id,
                    }
                )
            else:
                self.branch_ledger.record_contract_validation_rejected(table_contract, validation)

        table_contracts = [contract for contract in table_contracts if validate_contract(contract, self.catalogs)["ok"]]
        self.trace.append(
            {
                "event": "runtime_binding_inventory_selected",
                "selected_binding_ids": [candidate["account_data_binding_id"] for candidate in selected_candidates],
                "table_contract_ids": [contract.contract_id for contract in table_contracts],
            }
        )
        return selected_binding_results, table_contracts

    def _record_runtime_binding_inventory_selection(self, candidates: list[dict[str, Any]]) -> list[SearchResult]:
        results: list[SearchResult] = []
        for candidate in candidates:
            binding_card = candidate.get("binding_card")
            if not isinstance(binding_card, dict):
                continue
            contract = runtime_binding_inventory_contract(candidate)
            validation = validate_contract(contract, self.catalogs)
            self.trace.append(
                {
                    "event": "inventory_binding_contract_validated",
                    "contract": contract.to_dict(),
                    "validation": validation,
                }
            )
            if not validation["ok"]:
                self.branch_ledger.record_contract_validation_rejected(contract, validation)
                continue
            self.branch_ledger.record_contract_discovered(contract)
            result_validation = validate_returned_cards(contract, [binding_card], self.catalogs)
            result = SearchResult(
                result_id=f"result.{contract.contract_id}",
                contract_id=contract.contract_id,
                stage=contract.stage,
                returned_cards=[binding_card],
                validation=result_validation,
            )
            touched_branch_ids = self.branch_ledger.record_result(contract, result)
            self.trace.append({"event": "runtime_binding_inventory_result_recorded", "result": result.to_dict()})
            self.trace.append(
                {
                    "event": "branch_ledger_result_recorded",
                    "contract_id": contract.contract_id,
                    "result_id": result.result_id,
                    "branch_ids": touched_branch_ids,
                }
            )
            results.append(result)
        return results

    def _blocked(self, reason: str, extra: dict[str, Any] | None = None) -> dict[str, Any]:
        branch_snapshot = self.branch_ledger.snapshot()
        decision = completion_decision(self.completion_policy, branch_snapshot)
        output = {
            "status": "blocked",
            "blocked_reason": reason,
            "completion_policy": self.completion_policy,
            "usable_branch_ids": decision["usable_branch_ids"],
            "incomplete_branch_ids": decision["incomplete_branch_ids"],
            "best_effort_warnings": decision["warnings"],
            "trace_path": str(self.trace_dir / "last_search_trace.json"),
            "trace": self.trace,
        }
        if extra:
            output.update(extra)
        output.update(branch_snapshot)
        output["usable_branch_count"] = len(decision["usable_branch_ids"])
        output["incomplete_branch_count"] = len(decision["incomplete_branch_ids"])
        write_json(output["trace_path"], output)
        return output


def runtime_candidate_cards(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [card for card in cards if card.get("card_type") in {"platform_account", "account_data_binding"}]


def cards_of_type(cards: list[dict[str, Any]], card_type: str) -> list[dict[str, Any]]:
    return [card for card in cards if card.get("card_type") == card_type]


def compact_route_candidate(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "candidate_id": card_id(card),
        "canonical_id": card_id(card),
        "canonical_name": card.get("canonical_name"),
        "card_type": card.get("card_type"),
        "node_sets": card_node_sets(card),
        "fields": compact_value(card.get("fields"), limit=700),
        "semantic": compact_value(card.get("semantic"), limit=700),
        "traversal": compact_value(card.get("traversal"), limit=700),
    }


def select_cards_by_id(cards: list[dict[str, Any]], selected_ids: list[Any]) -> list[dict[str, Any]]:
    by_id = {card_id(card): card for card in cards if card_id(card)}
    selected: list[dict[str, Any]] = []
    for raw_id in selected_ids:
        card = by_id.get(str(raw_id))
        if card and card not in selected:
            selected.append(card)
    return selected


def binding_search_contracts_from_platform_accounts(platform_account_cards: list[dict[str, Any]], query_text: str) -> list[SearchContract]:
    contracts: list[SearchContract] = []
    for card in platform_account_cards:
        node_sets = card_node_sets(card)
        platform_account_id = first_node_value(node_sets, "platform_account_id") or card_id(card)
        tenant_id = first_node_value(node_sets, "tenant_id")
        group_id = first_node_value(node_sets, "group_id")
        if not platform_account_id or not tenant_id or not group_id:
            continue
        platform_id = first_node_value(node_sets, "platform_id")
        platform_context_id = first_node_value(node_sets, "platform_context_id")
        search_node_sets = [
            "domain_family:client_runtime",
            "card_type:account_data_binding",
            f"tenant_id:{tenant_id}",
            f"group_id:{group_id}",
            f"platform_account_id:{platform_account_id}",
        ]
        if platform_id:
            search_node_sets.append(f"platform_id:{platform_id}")
        contracts.append(
            SearchContract(
                contract_id=f"q2.runtime.bindings.{safe_contract_suffix(platform_account_id)}",
                stage="runtime_account_binding_search",
                query_text=f"{query_text} | Runtime account data bindings for selected platform account {platform_account_id}",
                node_sets=search_node_sets,
                top_k=30,
                allowed_card_types=["account_data_binding"],
                required_carry_forward={
                    "tenant_id": tenant_id,
                    "group_id": group_id,
                    "platform_account_id": platform_account_id,
                    **({"platform_id": platform_id} if platform_id else {}),
                    **({"platform_context_id": platform_context_id} if platform_context_id else {}),
                },
            )
        )
    return contracts


def binding_route_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    binding = candidate.get("binding") if isinstance(candidate.get("binding"), dict) else {}
    return {
        "candidate_type": "runtime_binding_table_candidate",
        "canonical_id": candidate.get("account_data_binding_id"),
        "candidate_id": candidate.get("account_data_binding_id"),
        "account_data_binding_id": candidate.get("account_data_binding_id"),
        "card_type": "account_data_binding",
        "canonical_name": binding.get("canonical_name"),
        "node_sets": binding.get("node_sets") or [],
        "platform_account_id": candidate.get("platform_account_id"),
        "platform_id": candidate.get("platform_id"),
        "platform_context_id": candidate.get("platform_context_id"),
        "runtime_source_family": candidate.get("runtime_source_family"),
        "domain_id": candidate.get("domain_id"),
        "source_role": candidate.get("source_role"),
        "table_id": candidate.get("table_id"),
        "scope_keys": candidate.get("scope_keys") or [],
        "binding": binding,
        "table": candidate.get("table"),
        "columns": candidate.get("columns") or [],
        "metric_implementations": candidate.get("metric_implementations") or [],
        "query_patterns": candidate.get("query_patterns") or [],
    }


def selected_binding_candidates_from_ids(
    selected_ids: list[Any],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_id = {str(candidate.get("account_data_binding_id") or ""): candidate for candidate in candidates}
    selected: list[dict[str, Any]] = []
    for raw_id in selected_ids:
        candidate = by_id.get(str(raw_id))
        if candidate and candidate not in selected:
            selected.append(candidate)
    return selected


def domain_search_contracts_from_binding_candidates(candidates: list[dict[str, Any]], query_text: str) -> list[SearchContract]:
    contracts: list[SearchContract] = []
    seen: set[tuple[str, str, str, str]] = set()
    for candidate in candidates:
        binding_id = str(candidate.get("account_data_binding_id") or "")
        platform_id = str(candidate.get("platform_id") or "")
        platform_context_id = str(candidate.get("platform_context_id") or "")
        domain_id = str(candidate.get("domain_id") or "")
        if not binding_id or not platform_id:
            continue
        signature = (binding_id, platform_id, platform_context_id, domain_id)
        if signature in seen:
            continue
        seen.add(signature)
        node_sets = ["card_type:domain", f"platform_id:{platform_id}"]
        if platform_context_id:
            node_sets.append(f"platform_context_id:{platform_context_id}")
        if domain_id:
            node_sets.append(f"domain_id:{domain_id}")
        contracts.append(
            SearchContract(
                contract_id=f"q3.semantic.domains.{safe_contract_suffix(binding_id)}",
                stage="semantic_domain_search",
                query_text=f"{query_text} | Domains relevant to selected runtime binding {binding_id}",
                node_sets=node_sets,
                top_k=20,
                allowed_card_types=["domain"],
                required_carry_forward=carry_forward_from_binding_candidate(candidate),
            )
        )
    return contracts


def domain_table_search_contracts_from_domain_cards(
    domain_cards: list[dict[str, Any]],
    predecessor_contract: SearchContract,
) -> list[SearchContract]:
    contracts: list[SearchContract] = []
    carry = dict(predecessor_contract.required_carry_forward)
    for card in domain_cards:
        node_sets = card_node_sets(card)
        domain_id = first_node_value(node_sets, "domain_id") or card_id(card)
        platform_id = first_node_value(node_sets, "platform_id") or carry.get("platform_id")
        if not domain_id:
            continue
        search_node_sets = ["card_type:table", f"domain_id:{domain_id}"]
        if platform_id:
            search_node_sets.append(f"platform_id:{platform_id}")
        table_id = exact_table_id_for_domain_card(card, carry)
        if table_id:
            search_node_sets.append(f"table_id:{table_id}")
        next_carry = dict(carry)
        next_carry["domain_id"] = domain_id
        contracts.append(
            SearchContract(
                contract_id=f"q4.semantic.domain_tables.{safe_contract_suffix(domain_id)}.{safe_contract_suffix(str(carry.get('account_data_binding_id') or 'binding'))}",
                stage="semantic_domain_table_search",
                query_text=f"Tables in selected domain {domain_id}",
                node_sets=search_node_sets,
                top_k=20,
                allowed_card_types=["table"],
                required_carry_forward=next_carry,
            )
        )
    return contracts


def exact_table_id_for_domain_card(domain_card: dict[str, Any], carry: dict[str, Any]) -> str | None:
    included_tables = domain_card_included_table_ids(domain_card)
    carry_table_id = str(carry.get("table_id") or "")
    if carry_table_id and (not included_tables or carry_table_id in included_tables):
        return carry_table_id
    if len(included_tables) == 1:
        return included_tables[0]
    return None


def domains_compatible_with_carry_table(domain_cards: list[dict[str, Any]], carry: dict[str, Any]) -> list[dict[str, Any]]:
    carry_table_id = str(carry.get("table_id") or "")
    if not carry_table_id:
        return domain_cards
    compatible: list[dict[str, Any]] = []
    for card in domain_cards:
        included_tables = domain_card_included_table_ids(card)
        if not included_tables or carry_table_id in included_tables:
            compatible.append(card)
    return compatible


def domain_card_included_table_ids(domain_card: dict[str, Any]) -> list[str]:
    fields = domain_card.get("fields") if isinstance(domain_card.get("fields"), dict) else {}
    table_ids = fields.get("included_tables") or []
    if not isinstance(table_ids, list):
        return []
    return [str(table_id) for table_id in table_ids if table_id]


def verify_table_cards_have_runtime_bindings(
    catalogs: CatalogBundle | None,
    table_cards: list[dict[str, Any]],
    runtime_context: dict[str, Any],
    predecessor_contract: SearchContract,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if catalogs is None:
        return [], [{"reason": "missing_catalogs"}]

    verified: list[dict[str, Any]] = []
    rejected: list[dict[str, Any]] = []
    carry = predecessor_contract.required_carry_forward
    for table_card in table_cards:
        table_id = first_node_value(card_node_sets(table_card), "table_id") or card_id(table_card)
        if not table_id:
            rejected.append({"table_id": card_id(table_card), "reason": "missing_table_id"})
            continue
        candidate = runtime_binding_candidate_for_table(
            catalogs,
            table_id,
            runtime_context,
            carry,
        )
        if candidate is None:
            rejected.append({"table_id": table_id, "reason": "no_active_tenant_group_binding_for_table"})
            continue
        verified.append(candidate)
    return verified, rejected


def runtime_binding_candidate_for_table(
    catalogs: CatalogBundle,
    table_id: str,
    runtime_context: dict[str, Any],
    carry: dict[str, Any],
) -> dict[str, Any] | None:
    tenant_id = str(runtime_context.get("tenant_id") or carry.get("tenant_id") or "")
    group_id = str(runtime_context.get("group_id") or carry.get("group_id") or "")
    platform_account_id = str(carry.get("platform_account_id") or "")
    platform_id = str(carry.get("platform_id") or "")
    preferred_binding_id = str(carry.get("account_data_binding_id") or "")

    matches: list[tuple[int, dict[str, Any]]] = []
    for row in catalogs.runtime_binding_catalog:
        row_node_sets = [str(node_set) for node_set in row.get("node_sets") or []]
        row_id = str(row.get("canonical_id") or "")
        if f"table_id:{table_id}" not in row_node_sets:
            continue
        if tenant_id and f"tenant_id:{tenant_id}" not in row_node_sets:
            continue
        if group_id and f"group_id:{group_id}" not in row_node_sets:
            continue
        if platform_account_id and f"platform_account_id:{platform_account_id}" not in row_node_sets:
            continue
        if platform_id and f"platform_id:{platform_id}" not in row_node_sets:
            continue
        status = catalogs.binding_status(row_id) or {}
        if status.get("binding_status") != "active":
            continue
        if status.get("missing_scope_columns") or status.get("missing_scope_columns_despite_table_loaded"):
            continue
        binding_card = catalogs.card_for_id(row_id)
        if not binding_card:
            continue
        score = 0 if row_id == preferred_binding_id else 1
        matches.append((score, enrich_runtime_binding_candidate(catalogs, binding_card, row)))
    for _, candidate in sorted(matches, key=lambda item: item[0]):
        if candidate:
            return candidate
    return None


def inherit_required_carry_forward(contract: SearchContract, predecessor_contract: SearchContract) -> SearchContract:
    if not predecessor_contract.required_carry_forward:
        return contract
    inheritable_stages = ("semantic_table", "table_local_", "metric_", "relationship", "reconciliation")
    if not contract.stage.startswith(inheritable_stages):
        return contract
    inherited = dict(predecessor_contract.required_carry_forward)
    inherited.update(contract.required_carry_forward)
    if inherited == contract.required_carry_forward:
        return contract
    return SearchContract(**{**contract.to_dict(), "required_carry_forward": inherited})


def runtime_binding_inventory_candidates(
    catalogs: CatalogBundle | None,
    cards: list[dict[str, Any]],
    runtime_context: dict[str, Any],
) -> list[dict[str, Any]]:
    if catalogs is None:
        return []

    tenant_id = str(runtime_context.get("tenant_id") or "")
    group_id = str(runtime_context.get("group_id") or "")
    direct_binding_ids = [
        card_id(card)
        for card in cards
        if card.get("card_type") == "account_data_binding" and card_id(card)
    ]
    platform_account_ids = [
        first_node_value(card_node_sets(card), "platform_account_id") or card_id(card)
        for card in cards
        if card.get("card_type") == "platform_account"
    ]
    platform_account_ids.extend(
        first_node_value(card_node_sets(card), "platform_account_id")
        for card in cards
        if card.get("card_type") == "account_data_binding"
    )
    platform_account_ids = unique_in_order(platform_account_ids)
    if not direct_binding_ids and not platform_account_ids:
        return []

    candidates: list[dict[str, Any]] = []
    seen: set[str] = set()
    for binding_card, binding_row in runtime_binding_inventory_cards(catalogs, direct_binding_ids, platform_account_ids, tenant_id, group_id):
        binding_id = card_id(binding_card)
        if not binding_id or binding_id in seen:
            continue
        candidate = enrich_runtime_binding_candidate(catalogs, binding_card, binding_row)
        if candidate:
            candidates.append(candidate)
            seen.add(binding_id)
    return candidates


def runtime_binding_inventory_cards(
    catalogs: CatalogBundle,
    direct_binding_ids: list[str],
    platform_account_ids: list[str],
    tenant_id: str,
    group_id: str,
) -> list[tuple[dict[str, Any], dict[str, Any]]]:
    direct_set = set(direct_binding_ids)
    account_set = set(platform_account_ids)
    rows_by_id = {
        str(row.get("canonical_id") or ""): row
        for row in catalogs.runtime_binding_catalog
        if row.get("canonical_id")
    }
    matches: list[tuple[dict[str, Any], dict[str, Any]]] = []

    for binding_id in direct_binding_ids:
        card = catalogs.card_for_id(binding_id)
        if card:
            matches.append((card, rows_by_id.get(binding_id, {})))

    for row in catalogs.runtime_binding_catalog:
        row_id = str(row.get("canonical_id") or "")
        if not row_id or row_id in direct_set:
            continue
        node_sets = [str(node_set) for node_set in row.get("node_sets") or []]
        if tenant_id and f"tenant_id:{tenant_id}" not in node_sets:
            continue
        if group_id and f"group_id:{group_id}" not in node_sets:
            continue
        platform_account_id = first_node_value(node_sets, "platform_account_id")
        if account_set and platform_account_id not in account_set:
            continue
        card = catalogs.card_for_id(row_id)
        if card:
            matches.append((card, row))
    return matches


def enrich_runtime_binding_candidate(
    catalogs: CatalogBundle,
    binding_card: dict[str, Any],
    binding_row: dict[str, Any],
) -> dict[str, Any] | None:
    binding_id = card_id(binding_card)
    node_sets = card_node_sets(binding_card)
    table_id = first_node_value(node_sets, "table_id") or str(binding_row.get("table_id") or "")
    if not binding_id or not table_id:
        return None

    table_card = catalogs.card_for_id(table_id) or {}
    table_node_sets = card_node_sets(table_card)
    platform_id = first_node_value(node_sets, "platform_id") or first_node_value(table_node_sets, "platform_id")
    platform_context_id = first_node_value(node_sets, "platform_context_id") or first_node_value(table_node_sets, "platform_context_id")
    domain_id = first_node_value(node_sets, "domain_id") or first_node_value(table_node_sets, "domain_id")
    source_role = first_node_value(node_sets, "source_role") or str(binding_row.get("source_role") or "")
    runtime_source_family = first_node_value(node_sets, "runtime_source_family")
    platform_account_id = first_node_value(node_sets, "platform_account_id") or str(binding_row.get("platform_account_id") or "")

    return {
        "candidate_type": "runtime_binding_table_candidate",
        "candidate_id": binding_id,
        "account_data_binding_id": binding_id,
        "platform_account_id": platform_account_id,
        "platform_id": platform_id,
        "platform_context_id": platform_context_id,
        "runtime_source_family": runtime_source_family,
        "domain_id": domain_id,
        "source_role": source_role,
        "table_id": table_id,
        "scope_keys": binding_row.get("scope_keys") or [],
        "binding": compact_card_for_inventory(binding_card),
        "table": compact_card_for_inventory(table_card) if table_card else None,
        "columns": table_local_card_summaries(catalogs, table_id, "column", limit=24),
        "metric_implementations": table_local_card_summaries(catalogs, table_id, "metric_implementation", limit=16),
        "query_patterns": table_local_card_summaries(catalogs, table_id, "query_pattern", limit=16),
        "binding_card": binding_card,
    }


def compact_card_for_inventory(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "canonical_id": card_id(card),
        "canonical_name": card.get("canonical_name"),
        "card_type": card.get("card_type"),
        "node_sets": card_node_sets(card),
        "fields": compact_value(card.get("fields"), limit=500),
        "semantic": compact_value(card.get("semantic"), limit=500),
    }


def table_local_card_summaries(
    catalogs: CatalogBundle,
    table_id: str,
    card_type: str,
    *,
    limit: int,
) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    for card in catalogs.card_catalog.values():
        if not isinstance(card, dict) or card.get("card_type") != card_type:
            continue
        node_sets = card_node_sets(card)
        if f"table_id:{table_id}" not in node_sets:
            continue
        cards.append(
            {
                "canonical_id": card_id(card),
                "canonical_name": card.get("canonical_name"),
                "node_sets": compact_inventory_node_sets(node_sets),
            }
        )
    cards.sort(key=lambda card: str(card.get("canonical_id") or ""))
    return cards[:limit]


def compact_inventory_node_sets(node_sets: list[str]) -> list[str]:
    keep_prefixes = (
        "domain_family:",
        "domain_id:",
        "source_role:",
        "applicable_source_role:",
        "table_id:",
        "column_id:",
        "metric_id:",
        "query_pattern_id:",
        "relationship_id:",
    )
    return [node_set for node_set in node_sets if node_set.startswith(keep_prefixes)]


def llm_binding_inventory_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in candidate.items() if key != "binding_card"}


def selected_binding_inventory_candidates(
    decision: dict[str, Any],
    candidates: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_binding_id = {str(candidate["account_data_binding_id"]): candidate for candidate in candidates}
    by_table_id: dict[str, list[dict[str, Any]]] = {}
    for candidate in candidates:
        by_table_id.setdefault(str(candidate.get("table_id") or ""), []).append(candidate)

    selected: list[dict[str, Any]] = []
    for binding_id in decision.get("selected_binding_ids") or []:
        candidate = by_binding_id.get(str(binding_id))
        if candidate:
            selected.append(candidate)

    for table_id in decision.get("selected_table_ids") or []:
        for candidate in by_table_id.get(str(table_id), []):
            if candidate not in selected:
                selected.append(candidate)
    return selected


def runtime_binding_inventory_contract(candidate: dict[str, Any]) -> SearchContract:
    binding_card = candidate["binding_card"]
    binding_id = str(candidate["account_data_binding_id"])
    return SearchContract(
        contract_id=f"q2.inventory.binding.{safe_contract_suffix(binding_id)}",
        stage="runtime_account_binding_search",
        query_text=f"Selected runtime binding inventory card {binding_id}",
        node_sets=card_node_sets(binding_card),
        top_k=1,
        allowed_card_types=["account_data_binding"],
        required_carry_forward=carry_forward_from_binding_candidate(candidate),
    )


def table_frame_contracts_from_binding_candidates(candidates: list[dict[str, Any]]) -> list[SearchContract]:
    contracts: list[SearchContract] = []
    seen: set[tuple[str, str]] = set()
    for candidate in candidates:
        table_id = str(candidate.get("table_id") or "")
        binding_id = str(candidate.get("account_data_binding_id") or "")
        if not table_id or not binding_id:
            continue
        signature = (binding_id, table_id)
        if signature in seen:
            continue
        seen.add(signature)
        contracts.append(
            SearchContract(
                contract_id=f"q3.inventory.table_frame.{safe_contract_suffix(binding_id)}",
                stage="semantic_table_frame_search",
                query_text=f"Table frame for selected runtime binding {binding_id} ({table_id})",
                node_sets=["card_type:table", f"table_id:{table_id}"],
                top_k=3,
                allowed_card_types=["table"],
                required_carry_forward=carry_forward_from_binding_candidate(candidate),
            )
        )
    return contracts


def carry_forward_from_binding_candidate(candidate: dict[str, Any]) -> dict[str, Any]:
    carry: dict[str, Any] = {}
    binding_card = candidate.get("binding_card") if isinstance(candidate.get("binding_card"), dict) else {}
    node_sets = card_node_sets(binding_card)
    for key in (
        "tenant_id",
        "group_id",
        "runtime_source_family",
        "platform_id",
        "platform_context_id",
        "platform_account_id",
        "source_role",
        "table_id",
    ):
        value = candidate.get(key) or first_node_value(node_sets, key)
        if value not in (None, "", []):
            carry[key] = value
    binding_id = candidate.get("account_data_binding_id")
    if binding_id:
        carry["account_data_binding_id"] = binding_id
    if candidate.get("scope_keys") is not None:
        carry["scope_keys"] = candidate.get("scope_keys")
    return carry


def safe_contract_suffix(value: str) -> str:
    return "".join(ch if ch.isalnum() else "_" for ch in value).strip("_").lower()[:120]


def has_runtime_binding_result(results: list[SearchResult]) -> bool:
    return any(card.get("card_type") == "account_data_binding" for card in result_cards(results))


def prune_and_rank_pending(
    pending: list[SearchContract],
    query_text: str,
    results: list[SearchResult],
    executed_signatures: set[tuple[Any, ...]],
    max_pending: int = 32,
    branch_ledger: BranchLedger | None = None,
    branch_max_steps: int = 8,
) -> list[SearchContract]:
    preferred_tables = preferred_table_ids(query_text, results)
    has_runtime_binding = has_runtime_binding_result(results)
    deduped: list[SearchContract] = []
    seen: set[tuple[Any, ...]] = set()
    for contract in pending:
        signature = contract_signature(contract)
        if signature in seen or signature in executed_signatures:
            continue
        if should_drop_contract(contract, preferred_tables, has_runtime_binding):
            continue
        branch_id = scheduler_branch_id(contract, branch_ledger)
        if branch_ledger is not None and branch_step_count(branch_ledger, branch_id) >= branch_max_steps:
            continue
        seen.add(signature)
        deduped.append(contract)
    deduped.sort(key=lambda contract: contract_priority(contract, query_text, preferred_tables))
    if branch_ledger is None:
        return deduped[:max_pending]
    return interleave_branch_contracts(deduped, query_text, preferred_tables, branch_ledger, max_pending)


def interleave_branch_contracts(
    contracts: list[SearchContract],
    query_text: str,
    preferred_tables: set[str],
    branch_ledger: BranchLedger,
    max_pending: int,
) -> list[SearchContract]:
    grouped: dict[str, list[SearchContract]] = {}
    for contract in contracts:
        branch_id = scheduler_branch_id(contract, branch_ledger)
        grouped.setdefault(branch_id, []).append(contract)

    for branch_contracts in grouped.values():
        branch_contracts.sort(key=lambda contract: contract_priority(contract, query_text, preferred_tables))

    branch_ids = sorted(
        grouped,
        key=lambda branch_id: active_branch_contract_priority(
            grouped[branch_id],
            query_text,
            preferred_tables,
            branch_ledger,
            branch_id,
        ),
    )
    ordered: list[SearchContract] = []
    while branch_ids and len(ordered) < max_pending:
        branch_ids = sorted(
            branch_ids,
            key=lambda branch_id: active_branch_contract_priority(
                grouped[branch_id],
                query_text,
                preferred_tables,
                branch_ledger,
                branch_id,
            ),
        )
        next_branch_ids: list[str] = []
        for branch_id in branch_ids:
            branch_contracts = grouped[branch_id]
            if branch_contracts:
                ordered.append(branch_contracts.pop(0))
                if len(ordered) >= max_pending:
                    break
            if branch_contracts:
                next_branch_ids.append(branch_id)
        branch_ids = next_branch_ids
    return ordered


def active_branch_contract_priority(
    branch_contracts: list[SearchContract],
    query_text: str,
    preferred_tables: set[str],
    branch_ledger: BranchLedger,
    branch_id: str,
) -> tuple[Any, ...]:
    if not branch_contracts:
        return ((999, branch_id), branch_priority(branch_ledger, branch_id))
    return (
        contract_priority(branch_contracts[0], query_text, preferred_tables),
        branch_priority(branch_ledger, branch_id),
    )


def scheduler_branch_id(contract: SearchContract, branch_ledger: BranchLedger | None) -> str:
    if branch_ledger is None:
        return f"branch.untracked.{contract.contract_id}"
    existing_branch_id = branch_ledger.contract_branches.get(contract.contract_id)
    if existing_branch_id:
        return existing_branch_id
    return branch_id_for_scope(scope_from_contract(contract))


def branch_priority(branch_ledger: BranchLedger, branch_id: str) -> tuple[int, int, int, str]:
    branch = branch_ledger.branches.get(branch_id)
    status_priority = {
        "partial": 0,
        "in_progress": 1,
        "pending": 2,
        "usable": 3,
        "blocked": 4,
        "failed": 5,
    }
    if branch is None:
        return (6, 0, len(branch_ledger.branch_order), branch_id)
    try:
        order_index = branch_ledger.branch_order.index(branch_id)
    except ValueError:
        order_index = len(branch_ledger.branch_order)
    return (
        status_priority.get(branch.status, 6),
        branch.executed_step_count,
        order_index,
        branch_id,
    )


def branch_step_count(branch_ledger: BranchLedger, branch_id: str) -> int:
    branch = branch_ledger.branches.get(branch_id)
    return branch.executed_step_count if branch is not None else 0


def completion_decision(completion_policy: str, branch_snapshot: dict[str, Any]) -> dict[str, Any]:
    usable_branch_ids = [
        branch_id
        for branch_id in branch_snapshot.get("branch_order", [])
        if branch_snapshot.get("branch_status", {}).get(branch_id) == "usable"
    ]
    incomplete_ids = incomplete_branch_ids(branch_snapshot)
    warnings = best_effort_warnings(branch_snapshot)

    if not usable_branch_ids:
        return {
            "status": "blocked",
            "blocked_reason": "no_usable_branch_evidence",
            "completion_reason": None,
            "usable_branch_ids": [],
            "incomplete_branch_ids": incomplete_ids,
            "warnings": warnings,
            "write_handoff": False,
            "handoff_skip_reason": "no_usable_branch_evidence",
        }

    if completion_policy == "strict" and incomplete_ids:
        return {
            "status": "blocked",
            "blocked_reason": "strict_completion_requires_all_branches_usable",
            "completion_reason": None,
            "usable_branch_ids": usable_branch_ids,
            "incomplete_branch_ids": incomplete_ids,
            "warnings": warnings,
            "write_handoff": False,
            "handoff_skip_reason": "strict_completion_requires_all_branches_usable",
        }

    if completion_policy == "partial" and incomplete_ids:
        return {
            "status": "partial",
            "blocked_reason": None,
            "completion_reason": "partial_usable_branch_evidence",
            "usable_branch_ids": usable_branch_ids,
            "incomplete_branch_ids": incomplete_ids,
            "warnings": warnings,
            "write_handoff": False,
            "handoff_skip_reason": "completion_policy_partial_incomplete_branches",
        }

    if incomplete_ids:
        return {
            "status": "best_effort",
            "blocked_reason": None,
            "completion_reason": "best_effort_usable_branch_evidence",
            "usable_branch_ids": usable_branch_ids,
            "incomplete_branch_ids": incomplete_ids,
            "warnings": warnings,
            "write_handoff": True,
            "handoff_skip_reason": None,
        }

    return {
        "status": "complete",
        "blocked_reason": None,
        "completion_reason": "all_discovered_branches_usable",
        "usable_branch_ids": usable_branch_ids,
        "incomplete_branch_ids": [],
        "warnings": [],
        "write_handoff": True,
        "handoff_skip_reason": None,
    }


def incomplete_branch_ids(branch_snapshot: dict[str, Any]) -> list[str]:
    incomplete_statuses = {"pending", "in_progress", "partial", "blocked", "failed"}
    branch_status = branch_snapshot.get("branch_status", {})
    branches = branch_snapshot.get("branches", {})
    evidence_scopes = [
        branch.get("scope", {})
        for branch in branches.values()
        if branch_has_evidence(branch)
    ]
    return [
        branch_id
        for branch_id in branch_snapshot.get("branch_order", [])
        if branch_status.get(branch_id) in incomplete_statuses
        and not evidence_less_ancestor_branch(branches.get(branch_id, {}), evidence_scopes)
    ]


def best_effort_warnings(branch_snapshot: dict[str, Any]) -> list[dict[str, Any]]:
    warnings: list[dict[str, Any]] = []
    branches = branch_snapshot.get("branches", {})
    branch_status = branch_snapshot.get("branch_status", {})
    for branch_id in incomplete_branch_ids(branch_snapshot):
        branch = branches.get(branch_id, {})
        warnings.append(
            {
                "warning": "branch_incomplete",
                "branch_id": branch_id,
                "status": branch_status.get(branch_id),
                "scope": branch.get("scope", {}),
                "missing_evidence": branch.get("missing_evidence", []),
                "branch_warnings": branch.get("warnings", []),
                "blocked_reasons": branch.get("blocked_reasons", []),
            }
        )
    return warnings


def usable_evidence_card_ids(branch_snapshot: dict[str, Any], usable_branch_ids: list[str]) -> set[str]:
    branches = branch_snapshot.get("branches", {})
    evidence_ids: set[str] = set()
    evidence_fields = (
        "platform_account_cards",
        "account_data_binding_cards",
        "table_cards",
        "column_cards",
        "query_pattern_cards",
        "metric_implementation_cards",
    )
    for branch_id in usable_branch_ids:
        branch = branches.get(branch_id, {})
        for field_name in evidence_fields:
            evidence_ids.update(str(card_id) for card_id in branch.get(field_name, []) if card_id)
    return evidence_ids


def evidence_less_ancestor_branch(branch: dict[str, Any], evidence_scopes: list[dict[str, str]]) -> bool:
    if branch_has_evidence(branch):
        return False
    scope = branch.get("scope", {})
    if not scope:
        return False
    return any(scope_is_subset(scope, evidence_scope) for evidence_scope in evidence_scopes if evidence_scope != scope)


def branch_has_evidence(branch: dict[str, Any]) -> bool:
    evidence_fields = (
        "platform_account_cards",
        "account_data_binding_cards",
        "table_cards",
        "column_cards",
        "query_pattern_cards",
        "metric_implementation_cards",
    )
    return any(branch.get(field_name) for field_name in evidence_fields)


def scope_is_subset(candidate: dict[str, str], expanded: dict[str, str]) -> bool:
    return all(expanded.get(key) == value for key, value in candidate.items())


def should_drop_contract(contract: SearchContract, preferred_tables: set[str], has_runtime_binding: bool) -> bool:
    if not has_runtime_binding and contract.stage.startswith(("semantic_", "table_local_")):
        return True
    if not preferred_tables:
        return False
    table_id = first_contract_node_value(contract, "table_id")
    if not table_id:
        return False
    if table_id in preferred_tables:
        return False
    return contract.stage.startswith(("semantic_", "table_local_", "metric_", "runtime_table_"))


def contract_priority(contract: SearchContract, query_text: str, preferred_tables: set[str]) -> tuple[int, str]:
    stage_priority = {
        "runtime_platform_account_search": 10,
        "runtime_account_binding_search": 20,
        "semantic_table_frame_search": 30,
        "table_local_query_pattern_search": 35,
        "table_local_metric_implementation_search": 40,
        "table_local_column_search": 55,
    }
    score = stage_priority.get(contract.stage, 70)
    table_id = first_contract_node_value(contract, "table_id")
    if table_id and table_id in preferred_tables:
        score -= 15
    text = f"{contract.contract_id} {contract.query_text} {' '.join(contract.node_sets)}".lower()
    for token in query_relevance_tokens(query_text):
        if token and token in text:
            score -= 2
    if "settlement_cash_position" in text or "cash_position" in text:
        score -= 10
    return (score, contract.contract_id)


def terminal_evidence_status(
    query_text: str,
    runtime_context: dict[str, Any],
    results: list[SearchResult],
) -> dict[str, Any]:
    cards = result_cards(results)
    binding_cards = [card for card in cards if card.get("card_type") == "account_data_binding"]
    table_cards = [card for card in cards if card.get("card_type") == "table"]
    query_pattern_cards = [card for card in cards if card.get("card_type") == "query_pattern"]
    metric_impl_cards = [card for card in cards if card.get("card_type") == "metric_implementation"]
    preferred_tables = preferred_table_ids(query_text, results)

    relevant_query_patterns = relevant_cards(query_pattern_cards, query_text, preferred_tables)
    relevant_metric_impls = relevant_cards(metric_impl_cards, query_text, preferred_tables)
    relevant_tables = relevant_cards(table_cards, query_text, preferred_tables)
    relevant_bindings = relevant_cards(binding_cards, query_text, preferred_tables)

    checks = {
        "runtime_binding": bool(relevant_bindings or binding_cards),
        "table_frame": bool(relevant_tables or table_cards),
        "query_pattern": bool(relevant_query_patterns),
    }
    ready = all(checks.values())
    return {
        "ready": ready,
        "checks": checks,
        "preferred_table_ids": sorted(preferred_tables),
        "tenant_id": runtime_context.get("tenant_id"),
        "group_id": runtime_context.get("group_id"),
        "binding_card_ids": card_ids(relevant_bindings or binding_cards),
        "table_card_ids": card_ids(relevant_tables or table_cards),
        "query_pattern_card_ids": card_ids(relevant_query_patterns),
        "metric_implementation_card_ids": card_ids(relevant_metric_impls),
    }


def build_evidence_pack(
    query_text: str,
    runtime_context: dict[str, Any],
    results: list[SearchResult],
    terminal: dict[str, Any],
    branch_snapshot: dict[str, Any] | None = None,
    usable_branch_ids: list[str] | None = None,
) -> dict[str, Any]:
    use_usable_branch_filter = branch_snapshot is not None and bool(usable_branch_ids)
    evidence_ids = usable_evidence_card_ids(branch_snapshot, usable_branch_ids or []) if branch_snapshot else set()
    if not evidence_ids:
        evidence_ids = set(
            terminal.get("binding_card_ids", [])
            + terminal.get("table_card_ids", [])
            + terminal.get("query_pattern_card_ids", [])
            + terminal.get("metric_implementation_card_ids", [])
        )
    packed_results: list[dict[str, Any]] = []
    for result in results:
        cards = [
            summarize_card(card)
            for card in result.returned_cards
            if card_id(card) in evidence_ids
            or (
                not use_usable_branch_filter
                and card.get("card_type") in {"account_data_binding", "table", "query_pattern", "metric_implementation"}
            )
        ]
        if cards:
            packed_results.append(
                {
                    "result_id": result.result_id,
                    "contract_id": result.contract_id,
                    "stage": result.stage,
                    "cards": cards,
                }
            )
    return {
        "query_text": query_text,
        "runtime_context": runtime_context,
        "terminal_evidence": terminal,
        "usable_branch_ids": usable_branch_ids or [],
        "results": packed_results,
    }


def summarize_card(card: dict[str, Any]) -> dict[str, Any]:
    return {
        "canonical_id": card_id(card),
        "canonical_name": card.get("canonical_name"),
        "card_type": card.get("card_type"),
        "node_sets": card.get("node_sets") or card.get("ingestion_node_sets") or [],
        "fields": compact_value(card.get("fields")),
        "semantic": compact_value(card.get("semantic")),
        "traversal": compact_value(card.get("traversal")),
    }


def compact_value(value: Any, *, limit: int = 1200) -> Any:
    if isinstance(value, dict):
        return {str(k): compact_value(v, limit=limit) for k, v in value.items()}
    if isinstance(value, list):
        return [compact_value(item, limit=limit) for item in value[:20]]
    if isinstance(value, str) and len(value) > limit:
        return value[:limit] + "...[truncated]"
    return value


def preferred_table_ids(query_text: str, results: list[SearchResult]) -> set[str]:
    selected_binding_tables: set[str] = set()
    for result in results:
        if not result.contract_id.startswith("q2.inventory.binding."):
            continue
        for card in result.returned_cards:
            table_id = first_node_value(card_node_sets(card), "table_id")
            if table_id:
                selected_binding_tables.add(table_id)
    if selected_binding_tables:
        return selected_binding_tables

    roles = source_roles_from_query(query_text)
    tables: set[str] = set()
    for card in result_cards(results):
        if card.get("card_type") != "account_data_binding":
            continue
        node_sets = card_node_sets(card)
        source_role = first_node_value(node_sets, "source_role")
        table_id = first_node_value(node_sets, "table_id")
        if table_id and (not roles or source_role in roles):
            tables.add(table_id)
    if tables:
        return tables

    query = query_text.lower()
    for card in result_cards(results):
        table_id = first_node_value(card_node_sets(card), "table_id")
        if table_id and any(token in table_id.lower() for token in query_relevance_tokens(query)):
            tables.add(table_id)
    return tables


def source_roles_from_query(query_text: str) -> set[str]:
    query = query_text.lower()
    roles: set[str] = set()
    if "settlement" in query or "payout" in query or "cash" in query:
        roles.add("settlement")
    if "return" in query or "refund" in query:
        roles.add("returns")
    if "fee" in query:
        roles.add("fee_preview")
    if "disbursement" in query:
        roles.add("disbursement")
    if "order" in query or "oms" in query:
        roles.add("oms_sales")
    return roles


def query_relevance_tokens(query_text: str) -> list[str]:
    tokens: list[str] = []
    query = query_text.lower()
    for token in ("amazon", "flipkart", "myntra", "nykaa", "meesho", "settlement", "cash", "position", "returns", "fees", "fee", "orders", "oms"):
        if token in query:
            tokens.append(token.rstrip("s"))
    if "cash" in query and "settlement" in query:
        tokens.extend(["settlement_cash_position", "cash_position"])
    return tokens


def relevant_cards(cards: list[dict[str, Any]], query_text: str, preferred_tables: set[str]) -> list[dict[str, Any]]:
    relevant: list[dict[str, Any]] = []
    tokens = query_relevance_tokens(query_text)
    for card in cards:
        node_sets = card_node_sets(card)
        table_id = first_node_value(node_sets, "table_id")
        text = card_search_text(card)
        if preferred_tables and table_id in preferred_tables:
            relevant.append(card)
            continue
        if any(token in text for token in tokens):
            relevant.append(card)
    return relevant


def result_cards(results: list[SearchResult]) -> list[dict[str, Any]]:
    cards: list[dict[str, Any]] = []
    seen: set[str] = set()
    for result in results:
        for card in result.returned_cards:
            cid = card_id(card)
            if cid and cid in seen:
                continue
            cards.append(card)
            if cid:
                seen.add(cid)
    return cards


def card_ids(cards: list[dict[str, Any]]) -> list[str]:
    return [cid for card in cards if (cid := card_id(card))]


def local_exact_catalog_cards_for_contract(
    contract: SearchContract,
    catalogs: CatalogBundle | None,
) -> list[dict[str, Any]]:
    if catalogs is None:
        return []
    expected_card_type = first_node_value(contract.node_sets, "card_type")
    node_set_ids = [
        value
        for key in ("canonical_id", "domain_id", "table_id", "account_data_binding_id")
        if (value := first_node_value(contract.node_sets, key))
    ]
    candidate_ids = unique_in_order([*contract.exact_dereference_ids, *contract.candidate_seed_ids, *node_set_ids])
    cards: list[dict[str, Any]] = []
    for candidate_id in candidate_ids:
        card = catalogs.card_for_id(candidate_id)
        if not card:
            continue
        if expected_card_type and card.get("card_type") != expected_card_type:
            continue
        if card_id(card) not in card_ids(cards):
            cards.append(card)
    return cards


def card_id(card: dict[str, Any]) -> str:
    return str(card.get("canonical_id") or card.get("id") or "")


def card_node_sets(card: dict[str, Any]) -> list[str]:
    return [str(node_set) for node_set in card.get("node_sets") or card.get("ingestion_node_sets") or []]


def card_search_text(card: dict[str, Any]) -> str:
    parts = [
        card_id(card),
        str(card.get("canonical_name") or ""),
        " ".join(card_node_sets(card)),
        str(card.get("fields") or ""),
        str(card.get("semantic") or ""),
    ]
    return " ".join(parts).lower()


def first_contract_node_value(contract: SearchContract, key: str) -> str | None:
    return first_node_value(contract.node_sets, key)


def first_node_value(node_sets: list[str], key: str) -> str | None:
    prefix = f"{key}:"
    for node_set in node_sets:
        if str(node_set).startswith(prefix):
            return str(node_set).split(":", 1)[1]
    return None


def should_expand_runtime_platform_account_contract(contract: SearchContract) -> bool:
    return False


def runtime_platform_account_platform_ids(
    catalogs: CatalogBundle | None,
    contract: SearchContract,
    query_text: str = "",
) -> list[str]:
    if catalogs is None:
        return []
    tenant_id = first_contract_node_value(contract, "tenant_id")
    group_id = first_contract_node_value(contract, "group_id")
    if not tenant_id or not group_id:
        return []

    source_family = requested_runtime_source_family(contract, query_text)
    platform_ids: list[str] = []
    seen: set[str] = set()
    for row in catalogs.node_set_registry:
        if row.get("card_type") != "platform_account":
            continue
        row_node_sets = [str(node_set) for node_set in row.get("node_sets") or []]
        if f"tenant_id:{tenant_id}" not in row_node_sets or f"group_id:{group_id}" not in row_node_sets:
            continue
        if not runtime_source_family_matches(row_node_sets, str(row.get("canonical_id") or ""), source_family):
            continue
        platform_id = first_node_value(row_node_sets, "platform_id")
        if platform_id and platform_id not in seen:
            seen.add(platform_id)
            platform_ids.append(platform_id)
    return platform_ids


def requested_runtime_source_family(contract: SearchContract, query_text: str = "") -> str | None:
    explicit_family = first_contract_node_value(contract, "runtime_source_family")
    if explicit_family:
        return explicit_family
    search_text = f"{contract.query_text} {query_text}".lower()
    if "marketplace" in search_text:
        return "marketplace"
    if "payment gateway" in search_text or "payment_gateway" in search_text:
        return "payment_gateway"
    if "logistics" in search_text:
        return "logistics"
    if "wms" in search_text:
        return "wms"
    if "oms" in search_text:
        return "oms"
    return None


def runtime_source_family_matches(node_sets: list[str], canonical_id: str, source_family: str | None) -> bool:
    if source_family is None:
        return True
    runtime_source_family = first_node_value(node_sets, "runtime_source_family")
    if runtime_source_family:
        return runtime_source_family == source_family
    if source_family == "marketplace":
        account_id = first_node_value(node_sets, "platform_account_id") or canonical_id
        return account_id.endswith(".marketplace")
    return False


def contract_signature(contract: SearchContract) -> tuple[Any, ...]:
    return (
        contract.stage,
        tuple(sorted(str(node_set) for node_set in contract.node_sets)),
        tuple(sorted(str(card_type) for card_type in contract.allowed_card_types)),
        tuple(
            sorted(
                (str(key), signature_value(value))
                for key, value in contract.required_carry_forward.items()
                if value not in (None, "", [])
            )
        ),
        tuple(sorted(str(dataset) for dataset in contract.datasets)),
        tuple(sorted(str(candidate_id) for candidate_id in contract.candidate_seed_ids)),
        tuple(sorted(str(exact_id) for exact_id in contract.exact_dereference_ids)),
    )


def signature_value(value: Any) -> Any:
    if isinstance(value, dict):
        return tuple(sorted((str(key), signature_value(item)) for key, item in value.items()))
    if isinstance(value, list):
        return tuple(signature_value(item) for item in value)
    if isinstance(value, tuple):
        return tuple(signature_value(item) for item in value)
    if isinstance(value, set):
        return tuple(sorted(signature_value(item) for item in value))
    return str(value)
