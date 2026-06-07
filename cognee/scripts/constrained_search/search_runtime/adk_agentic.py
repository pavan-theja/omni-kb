from __future__ import annotations

import asyncio
import importlib.util
import time
from dataclasses import dataclass
from typing import Any, Awaitable, Callable

from .nodeset_contracts import SearchContract, SearchResult
from .search_state_machine import (
    CogneeSearchStateMachine,
    contract_signature,
    runtime_candidate_cards,
    terminal_evidence_status,
)
from .utils import write_json


@dataclass(frozen=True, slots=True)
class AgenticSkill:
    skill_id: str
    runner: str
    responsibility: str
    tools: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {
            "skill_id": self.skill_id,
            "runner": self.runner,
            "responsibility": self.responsibility,
            "tools": list(self.tools),
        }


@dataclass(slots=True)
class AgenticToolCall:
    skill_id: str
    name: str
    contract: SearchContract | None
    handler: Callable[[], Awaitable[Any]]


@dataclass(slots=True)
class AgenticToolResult:
    skill_id: str
    name: str
    contract_id: str | None
    output: Any = None
    error: str | None = None
    latency_seconds: float = 0.0


AGENTIC_SKILLS: tuple[AgenticSkill, ...] = (
    AgenticSkill(
        skill_id="query_anchor_skill",
        runner="sequential",
        responsibility="Extract the initial constrained search contracts from the user query and runtime scope.",
        tools=("extract_anchors",),
    ),
    AgenticSkill(
        skill_id="contract_execution_skill",
        runner="sequential",
        responsibility="Execute one validated NodeSet contract through Cognee and record branch evidence.",
        tools=("execute_contract",),
    ),
    AgenticSkill(
        skill_id="route_selection_skill",
        runner="sequential",
        responsibility="Choose platform accounts, bindings, domains, and tables from constrained candidate menus.",
        tools=("select_runtime_bindings", "plan_next_nodesets", "rank_bounded_candidates"),
    ),
    AgenticSkill(
        skill_id="evidence_profile_skill",
        runner="sequential",
        responsibility="Select evidence profiles and materialize table/domain-local evidence contracts.",
        tools=("select_evidence_profiles",),
    ),
    AgenticSkill(
        skill_id="profile_evidence_fanout_skill",
        runner="parallel",
        responsibility="Fetch independent profile evidence contracts after legal table finalization.",
        tools=("execute_profile_evidence_contract",),
    ),
    AgenticSkill(
        skill_id="handoff_skill",
        runner="sequential",
        responsibility="Assemble final evidence and write the SQL/search handoff.",
        tools=("write_sql_handoff",),
    ),
)


def skill_manifest() -> list[dict[str, Any]]:
    return [skill.to_dict() for skill in AGENTIC_SKILLS]


class AgenticSequentialRunner:
    """Small runner facade for the fixed ADK sequential control-plane shape."""

    def __init__(self, trace: list[dict[str, Any]]) -> None:
        self.trace = trace

    async def run_step(self, skill_id: str, tool_name: str, handler: Callable[[], Awaitable[Any]]) -> Any:
        started = time.perf_counter()
        self.trace.append(
            {
                "event": "adk_sequential_tool_started",
                "runner": "sequential",
                "skill_id": skill_id,
                "tool_name": tool_name,
            }
        )
        try:
            output = await handler()
        except Exception as exc:  # noqa: BLE001
            self.trace.append(
                {
                    "event": "adk_sequential_tool_failed",
                    "runner": "sequential",
                    "skill_id": skill_id,
                    "tool_name": tool_name,
                    "error": repr(exc),
                    "latency_seconds": elapsed_seconds(started),
                }
            )
            raise
        self.trace.append(
            {
                "event": "adk_sequential_tool_completed",
                "runner": "sequential",
                "skill_id": skill_id,
                "tool_name": tool_name,
                "latency_seconds": elapsed_seconds(started),
            }
        )
        return output


class AgenticParallelRunner:
    """Bounded parallel runner for independent evidence tool calls."""

    def __init__(self, concurrency: int, trace: list[dict[str, Any]]) -> None:
        self.concurrency = max(1, int(concurrency))
        self.trace = trace

    async def run(self, calls: list[AgenticToolCall]) -> list[AgenticToolResult]:
        semaphore = asyncio.Semaphore(self.concurrency)

        async def run_one(call: AgenticToolCall) -> AgenticToolResult:
            async with semaphore:
                started = time.perf_counter()
                contract_id = call.contract.contract_id if call.contract else None
                self.trace.append(
                    {
                        "event": "adk_parallel_tool_started",
                        "runner": "parallel",
                        "skill_id": call.skill_id,
                        "tool_name": call.name,
                        "contract_id": contract_id,
                    }
                )
                try:
                    output = await call.handler()
                except Exception as exc:  # noqa: BLE001
                    latency = elapsed_seconds(started)
                    self.trace.append(
                        {
                            "event": "adk_parallel_tool_failed",
                            "runner": "parallel",
                            "skill_id": call.skill_id,
                            "tool_name": call.name,
                            "contract_id": contract_id,
                            "error": repr(exc),
                            "latency_seconds": latency,
                        }
                    )
                    return AgenticToolResult(
                        skill_id=call.skill_id,
                        name=call.name,
                        contract_id=contract_id,
                        error=repr(exc),
                        latency_seconds=latency,
                    )
                latency = elapsed_seconds(started)
                self.trace.append(
                    {
                        "event": "adk_parallel_tool_completed",
                        "runner": "parallel",
                        "skill_id": call.skill_id,
                        "tool_name": call.name,
                        "contract_id": contract_id,
                        "latency_seconds": latency,
                    }
                )
                return AgenticToolResult(
                    skill_id=call.skill_id,
                    name=call.name,
                    contract_id=contract_id,
                    output=output,
                    latency_seconds=latency,
                )

        return await asyncio.gather(*(run_one(call) for call in calls))


class ADKAgenticCogneeSearchStateMachine(CogneeSearchStateMachine):
    """Agentic constrained-search runner with sequential control and parallel evidence tools."""

    def __init__(self, *args: Any, evidence_concurrency: int = 4, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.evidence_concurrency = max(1, int(evidence_concurrency))
        self.sequential_runner = AgenticSequentialRunner(self.trace)
        self.parallel_runner = AgenticParallelRunner(self.evidence_concurrency, self.trace)

    async def run_query(self, query_text: str, runtime_context: dict[str, Any]) -> dict[str, Any]:
        self._start_run_timing()
        self.trace.append(
            {
                "event": "adk_agentic_runtime_started",
                "orchestrator": "adk",
                "google_adk_available": google_adk_available(),
                "evidence_concurrency": self.evidence_concurrency,
                "skills": skill_manifest(),
            }
        )

        try:
            started = time.perf_counter()
            anchor = await self.sequential_runner.run_step(
                "query_anchor_skill",
                "extract_anchors",
                lambda: self.llm_plane.extract_anchors(query_text, runtime_context),
            )
        except Exception as exc:  # noqa: BLE001
            self._record_phase_timing("anchor_extractor", started, status="failed", orchestrator="adk", error=repr(exc))
            return self._blocked("anchor_extractor_failed", {"error": repr(exc), "orchestrator": "adk"})
        self._record_phase_timing("anchor_extractor", started, orchestrator="adk")

        anchor_decision = anchor.to_dict()
        self.trace.append({"event": "llm_anchor_decision", "decision": anchor_decision})

        started = time.perf_counter()
        pending = self._coerce_contracts(
            anchor.validated_output.get("next_search_contracts", []),
            "anchor_extractor",
            query_text,
        )
        self._record_phase_timing(
            "contract_coercion",
            started,
            source_event="anchor_extractor",
            emitted_count=len(anchor.validated_output.get("next_search_contracts", [])),
            valid_count=len(pending),
            orchestrator="adk",
        )
        if not pending:
            return self._blocked(
                "anchor_extractor_did_not_emit_valid_runtime_nodeset_contracts",
                {"orchestrator": "adk"},
            )

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
                result = await self.sequential_runner.run_step(
                    "contract_execution_skill",
                    "execute_contract",
                    lambda contract=contract: self.execute_contract(contract),
                )
            except Exception as exc:  # noqa: BLE001
                return self._blocked(
                    "contract_execution_failed",
                    {
                        "contract": contract.to_dict(),
                        "error": repr(exc),
                        "orchestrator": "adk",
                    },
                )
            results.append(result)

            started = time.perf_counter()
            route_selection = await self._select_route_next_contracts(
                query_text,
                runtime_context,
                anchor_decision,
                result,
                contract,
            )
            self._record_phase_timing(
                "route_selection",
                started,
                contract_id=contract.contract_id,
                stage=result.stage,
                routed=route_selection is not None,
                orchestrator="adk",
            )
            if route_selection is not None:
                route_results, route_contracts = route_selection
                results.extend(route_results)
                if route_contracts and should_parallelize_evidence_contracts(result, route_contracts):
                    try:
                        profile_results = await self._execute_evidence_contracts_parallel(route_contracts)
                    except Exception as exc:  # noqa: BLE001
                        return self._blocked(
                            "parallel_evidence_contract_execution_failed",
                            {
                                "contract_ids": [item.contract_id for item in route_contracts],
                                "error": repr(exc),
                                "orchestrator": "adk",
                            },
                        )
                    results.extend(profile_results)
                else:
                    pending.extend(route_contracts)
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)
                continue

            if is_profile_evidence_contract(contract):
                self.trace.append(
                    {
                        "event": "adk_profile_evidence_followup_suppressed",
                        "contract_id": contract.contract_id,
                        "stage": contract.stage,
                    }
                )
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)
                continue

            runtime_candidates = runtime_candidate_cards(result.returned_cards)
            if runtime_candidates:
                try:
                    started = time.perf_counter()
                    selector_decision = await self.sequential_runner.run_step(
                        "route_selection_skill",
                        "select_runtime_bindings",
                        lambda: self.llm_plane.select_runtime_bindings(
                            query_text,
                            anchor_decision,
                            runtime_candidates,
                        ),
                    )
                except Exception as exc:  # noqa: BLE001
                    self._record_phase_timing("runtime_binding_selector", started, status="failed", orchestrator="adk", error=repr(exc))
                    self.trace.append(
                        {
                            "event": "llm_runtime_binding_decision_failed",
                            "result": result.to_dict(),
                            "error": repr(exc),
                            "continuing_with_pending_count": len(pending),
                        }
                    )
                else:
                    self._record_phase_timing(
                        "runtime_binding_selector",
                        started,
                        candidate_count=len(runtime_candidates),
                        orchestrator="adk",
                    )
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
                started = time.perf_counter()
                planner_decision = await self.sequential_runner.run_step(
                    "route_selection_skill",
                    "plan_next_nodesets",
                    lambda: self.llm_plane.plan_next_nodesets(
                        query_text,
                        {
                            **result.to_dict(),
                            "predecessor_contract": contract.to_dict(),
                        },
                    ),
                )
            except Exception as exc:  # noqa: BLE001
                self._record_phase_timing("next_nodeset_planner", started, status="failed", orchestrator="adk", error=repr(exc))
                self.trace.append(
                    {
                        "event": "llm_next_nodeset_decision_failed",
                        "result": result.to_dict(),
                        "error": repr(exc),
                        "continuing_with_pending_count": len(pending),
                    }
                )
            else:
                self._record_phase_timing(
                    "next_nodeset_planner",
                    started,
                    contract_id=contract.contract_id,
                    stage=result.stage,
                    orchestrator="adk",
                )
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
                started = time.perf_counter()
                rank_decision = await self.sequential_runner.run_step(
                    "route_selection_skill",
                    "rank_bounded_candidates",
                    lambda: self.llm_plane.rank_bounded_candidates(query_text, contract, result.returned_cards),
                )
            except Exception as exc:  # noqa: BLE001
                self._record_phase_timing("bounded_candidate_ranker", started, status="failed", orchestrator="adk", error=repr(exc))
                self.trace.append(
                    {
                        "event": "llm_bounded_rank_decision_failed",
                        "contract": contract.to_dict(),
                        "error": repr(exc),
                        "continuing_with_pending_count": len(pending),
                    }
                )
            else:
                self._record_phase_timing(
                    "bounded_candidate_ranker",
                    started,
                    contract_id=contract.contract_id,
                    stage=result.stage,
                    returned_count=len(result.returned_cards),
                    orchestrator="adk",
                )
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
                    "orchestrator": "adk",
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
                    "orchestrator": "adk",
                },
                query_text,
                runtime_context,
                results,
                steps,
                terminal,
                pending,
            )

        output = await self._complete(query_text, runtime_context, results, steps, terminal, pending)
        return output

    async def _complete(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        results: list[SearchResult],
        steps: int,
        terminal: dict[str, Any],
        pending: list[SearchContract],
    ) -> dict[str, Any]:
        output = await super()._complete(query_text, runtime_context, results, steps, terminal, pending)
        output["orchestrator"] = "adk"
        output["evidence_concurrency"] = self.evidence_concurrency
        write_json(output["trace_path"], output)
        return output

    async def _write_sql_handoff(self, query_text: str, evidence_pack: dict[str, Any]) -> Any:
        return await self.sequential_runner.run_step(
            "handoff_skill",
            "write_sql_handoff",
            lambda: self.llm_plane.write_sql_handoff(query_text, evidence_pack),
        )

    async def _select_evidence_profiles(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        evidence_manifest: dict[str, Any],
    ) -> Any:
        started = time.perf_counter()
        try:
            decision = await self.sequential_runner.run_step(
                "evidence_profile_skill",
                "select_evidence_profiles",
                lambda: self.llm_plane.select_evidence_profiles(query_text, runtime_context, evidence_manifest),
            )
        except Exception as exc:  # noqa: BLE001
            self._record_phase_timing("evidence_profile_selector", started, status="failed", orchestrator="adk", error=repr(exc))
            raise
        self._record_phase_timing(
            "evidence_profile_selector",
            started,
            table_count=len(evidence_manifest.get("tables") or []),
            orchestrator="adk",
        )
        return decision

    def _blocked(self, reason: str, extra: dict[str, Any] | None = None) -> dict[str, Any]:
        output = super()._blocked(reason, extra)
        output["orchestrator"] = "adk"
        output["evidence_concurrency"] = self.evidence_concurrency
        write_json(output["trace_path"], output)
        return output

    async def _execute_evidence_contracts_parallel(self, contracts: list[SearchContract]) -> list[SearchResult]:
        started = time.perf_counter()
        self.trace.append(
            {
                "event": "adk_parallel_evidence_started",
                "concurrency": self.evidence_concurrency,
                "contract_ids": [contract.contract_id for contract in contracts],
            }
        )
        tool_results = await self.parallel_runner.run(
            [
                AgenticToolCall(
                    skill_id="profile_evidence_fanout_skill",
                    name="execute_profile_evidence_contract",
                    contract=contract,
                    handler=lambda contract=contract: self.execute_contract(contract),
                )
                for contract in contracts
            ]
        )

        failures = [
            {
                "contract_id": result.contract_id,
                "error": result.error,
                "latency_seconds": result.latency_seconds,
            }
            for result in tool_results
            if result.error
        ]
        self.trace.append(
            {
                "event": "adk_parallel_evidence_completed",
                "concurrency": self.evidence_concurrency,
                "contract_ids": [result.contract_id for result in tool_results],
                "result_count": sum(1 for result in tool_results if result.output is not None),
                "failures": failures,
                "latency_seconds_by_contract": {
                    str(result.contract_id): result.latency_seconds for result in tool_results if result.contract_id
                },
            }
        )
        if failures:
            self._record_phase_timing(
                "parallel_evidence_fanout",
                started,
                status="failed",
                orchestrator="adk",
                contract_count=len(contracts),
                failure_count=len(failures),
            )
            raise RuntimeError(f"Parallel evidence contract failures: {failures}")
        self._record_phase_timing(
            "parallel_evidence_fanout",
            started,
            orchestrator="adk",
            contract_count=len(contracts),
            result_count=sum(1 for result in tool_results if result.output is not None),
            failure_count=0,
        )
        return [result.output for result in tool_results if isinstance(result.output, SearchResult)]


def should_parallelize_evidence_contracts(result: SearchResult, contracts: list[SearchContract]) -> bool:
    return result.stage == "semantic_table_frame_search" and all(is_profile_evidence_contract(contract) for contract in contracts)


def is_profile_evidence_contract(contract: SearchContract) -> bool:
    carry = contract.required_carry_forward or {}
    return bool(
        carry.get("evidence_profile_id")
        or carry.get("evidence_profile_ids")
        or carry.get("required_evidence_card_types")
        or carry.get("optional_evidence_card_types")
    )


def google_adk_available() -> bool:
    return importlib.util.find_spec("google.adk") is not None


def elapsed_seconds(started: float) -> float:
    return round(time.perf_counter() - started, 3)
