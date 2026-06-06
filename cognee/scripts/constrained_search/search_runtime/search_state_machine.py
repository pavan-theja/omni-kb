from __future__ import annotations

from pathlib import Path
from typing import Any

from .catalogs import CatalogBundle
from .cognee_client import CogneeClient
from .contract_validator import canonicalize_contract, validate_contract, validate_returned_cards
from .llm_plane import LLMPlane
from .nodeset_contracts import SearchContract, SearchResult
from .utils import write_json


class CogneeSearchStateMachine:
    """Sequential Cognee NodeSet search orchestrator."""

    def __init__(
        self,
        cognee_client: CogneeClient,
        llm_plane: LLMPlane,
        trace_dir: str | Path,
        catalogs: CatalogBundle | None = None,
        max_steps: int = 30,
    ):
        self.cognee_client = cognee_client
        self.llm_plane = llm_plane
        self.trace_dir = Path(trace_dir)
        self.trace_dir.mkdir(parents=True, exist_ok=True)
        self.catalogs = catalogs
        self.max_steps = max_steps
        self.trace: list[dict[str, Any]] = []

    async def execute_contract(self, contract: SearchContract) -> SearchResult:
        routed_contract = self.cognee_client.with_routed_datasets(contract)
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
            raise ValueError(f"Invalid contract: {contract_validation['errors']}")

        cards = await self.cognee_client.search(routed_contract)
        result_validation = validate_returned_cards(routed_contract, cards, self.catalogs)
        result = SearchResult(
            result_id=f"result.{routed_contract.contract_id}",
            contract_id=routed_contract.contract_id,
            stage=routed_contract.stage,
            returned_cards=cards,
            validation=result_validation,
        )
        self.trace.append({"event": "cognee_result_validated", "result": result.to_dict()})
        if not result_validation["ok"]:
            raise ValueError(f"Cognee returned cards outside contract boundary: {result_validation['errors']}")
        return result

    def _coerce_contracts(
        self,
        raw_contracts: list[dict[str, Any]],
        source_event: str,
        query_text: str = "",
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
            raw_node_sets = list(contract.node_sets)
            contract = canonicalize_contract(contract, self.catalogs)
            for expanded_contract in self._expand_runtime_platform_account_contract(contract, source_event, query_text):
                validation = validate_contract(expanded_contract, self.catalogs)
                self.trace.append(
                    {
                        "event": "llm_contract_candidate_validated",
                        "source_event": source_event,
                        "contract": expanded_contract.to_dict(),
                        "normalization": {
                            "node_sets_changed": raw_node_sets != expanded_contract.node_sets,
                            "raw_node_sets": raw_node_sets,
                            "canonical_node_sets": expanded_contract.node_sets,
                        },
                        "validation": validation,
                    }
                )
                if validation["ok"]:
                    contracts.append(expanded_contract)
        return contracts

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
            terminal = terminal_evidence_status(query_text, runtime_context, results)
            if terminal["ready"]:
                return await self._complete(query_text, runtime_context, results, steps, terminal, pending)

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
                        )
                    )
                    pending = self._prepare_pending(pending, query_text, results, executed_signatures)

            try:
                planner_decision = await self.llm_plane.plan_next_nodesets(query_text, result.to_dict())
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
                    )
                )
                pending = self._prepare_pending(pending, query_text, results, executed_signatures)

        if pending:
            terminal = terminal_evidence_status(query_text, runtime_context, results)
            return self._blocked(
                "max_steps_exhausted_before_pending_contracts_completed",
                {
                    "steps_executed": steps,
                    "terminal_evidence": terminal,
                    "pending_count": len(pending),
                    "pending_contracts": [contract.to_dict() for contract in pending[:20]],
                },
            )

        terminal = terminal_evidence_status(query_text, runtime_context, results)
        if not terminal["ready"]:
            return self._blocked(
                "search_exhausted_without_terminal_evidence",
                {
                    "steps_executed": steps,
                    "terminal_evidence": terminal,
                },
            )

        return await self._complete(query_text, runtime_context, results, steps, terminal, pending)

    def _prepare_pending(
        self,
        pending: list[SearchContract],
        query_text: str,
        results: list[SearchResult],
        executed_signatures: set[tuple[Any, ...]],
    ) -> list[SearchContract]:
        prepared = prune_and_rank_pending(pending, query_text, results, executed_signatures)
        self.trace.append(
            {
                "event": "pending_queue_prepared",
                "pending_count": len(prepared),
                "pending_contract_ids": [contract.contract_id for contract in prepared[:20]],
            }
        )
        return prepared

    async def _complete(
        self,
        query_text: str,
        runtime_context: dict[str, Any],
        results: list[SearchResult],
        steps: int,
        terminal: dict[str, Any],
        pending: list[SearchContract],
    ) -> dict[str, Any]:
        evidence_pack = build_evidence_pack(query_text, runtime_context, results, terminal)
        try:
            handoff = await self.llm_plane.write_sql_handoff(query_text, evidence_pack)
            handoff_payload = handoff.to_dict()
        except Exception as exc:  # noqa: BLE001
            handoff_payload = {"error": repr(exc)}

        output = {
            "status": "complete",
            "blocked_reason": None,
            "completion_reason": "terminal_evidence_ready",
            "steps_executed": steps,
            "terminal_evidence": terminal,
            "handoff": handoff_payload,
            "pending_count_at_completion": len(pending),
            "results": [result.to_dict() for result in results],
            "trace_path": str(self.trace_dir / "last_search_trace.json"),
            "trace": self.trace,
        }
        write_json(output["trace_path"], output)
        return output

    def _blocked(self, reason: str, extra: dict[str, Any] | None = None) -> dict[str, Any]:
        output = {
            "status": "blocked",
            "blocked_reason": reason,
            "trace_path": str(self.trace_dir / "last_search_trace.json"),
            "trace": self.trace,
        }
        if extra:
            output.update(extra)
        write_json(output["trace_path"], output)
        return output


def runtime_candidate_cards(cards: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [card for card in cards if card.get("card_type") in {"platform_account", "account_data_binding"}]


def has_runtime_binding_result(results: list[SearchResult]) -> bool:
    return any(card.get("card_type") == "account_data_binding" for card in result_cards(results))


def prune_and_rank_pending(
    pending: list[SearchContract],
    query_text: str,
    results: list[SearchResult],
    executed_signatures: set[tuple[Any, ...]],
    max_pending: int = 16,
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
        seen.add(signature)
        deduped.append(contract)
    deduped.sort(key=lambda contract: contract_priority(contract, query_text, preferred_tables))
    return deduped[:max_pending]


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
        "runtime_account_data_binding_search": 20,
        "semantic_table_frame_search": 30,
        "semantic_query_pattern_search": 35,
        "table_local_query_pattern_search": 36,
        "semantic_metric_implementation_search": 40,
        "table_local_metric_search": 45,
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
) -> dict[str, Any]:
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
            if card_id(card) in evidence_ids or card.get("card_type") in {"account_data_binding", "table", "query_pattern", "metric_implementation"}
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
    return (
        contract.stage == "runtime_platform_account_search"
        and first_contract_node_value(contract, "card_type") == "platform_account"
        and first_contract_node_value(contract, "tenant_id") is not None
        and first_contract_node_value(contract, "group_id") is not None
        and first_contract_node_value(contract, "platform_id") is None
    )


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
    )
