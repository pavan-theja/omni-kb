import asyncio
import tempfile
import unittest
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CONSTRAINED_SEARCH_DIR = REPO_ROOT / "cognee" / "scripts" / "constrained_search"
if str(CONSTRAINED_SEARCH_DIR) not in sys.path:
    sys.path.insert(0, str(CONSTRAINED_SEARCH_DIR))

from search_runtime.branch_ledger import BranchLedger
from search_runtime.catalogs import CatalogBundle
from search_runtime.contract_repair import repair_contract
from search_runtime.contract_validator import validate_contract
from search_runtime.evidence_profiles import (
    build_evidence_manifest,
    invalid_profile_card_types,
    missing_card_type_purposes,
    profile_contracts_from_decision,
)
from search_runtime.nodeset_contracts import SearchContract, SearchResult
from search_runtime.search_state_machine import CogneeSearchStateMachine, contract_signature, prune_and_rank_pending


class ConstrainedSearchRuntimeHardeningTest(unittest.TestCase):
    def test_stage_alias_and_missing_card_type_are_repaired(self):
        contract = SearchContract(
            contract_id="q1.binding",
            stage="runtime_account_data_binding_search",
            query_text="bindings for selected account",
            node_sets=[
                "domain_family:client_runtime",
                "tenant_id:tenant.one",
                "group_id:group.one",
                "platform_account_id:platform_account.one.amazon.marketplace",
            ],
            allowed_card_types=["account_data_binding"],
        )

        result = repair_contract(contract, _catalog())

        self.assertTrue(result.ok)
        self.assertEqual("runtime_account_binding_search", result.contract.stage)
        self.assertIn("card_type:account_data_binding", result.contract.node_sets)
        self.assertEqual(["stage_alias", "missing_card_type_nodeset"], [row["repair"] for row in result.repairs])

    def test_platform_alias_nodeset_is_canonicalized_from_catalog(self):
        contract = SearchContract(
            contract_id="q1.platform",
            stage="runtime_platform_account_search",
            query_text="Amazon account",
            node_sets=[
                "domain_family:client_runtime",
                "card_type:platform_account",
                "tenant_id:tenant.one",
                "group_id:group.one",
                "platform_id:amazon",
            ],
            allowed_card_types=["platform_account"],
        )

        result = repair_contract(contract, _catalog())

        self.assertTrue(result.ok)
        self.assertIn("platform_id:platform.amazon", result.contract.node_sets)
        self.assertNotIn("platform_id:amazon", result.contract.node_sets)
        self.assertEqual("canonical_nodeset", result.repairs[0]["repair"])

    def test_unknown_stage_is_strict_validation_error_after_repair(self):
        contract = SearchContract(
            contract_id="q1.bad",
            stage="metric_search",
            query_text="bad stage",
            node_sets=["card_type:metric_implementation", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["metric_implementation"],
        )

        result = repair_contract(contract, _catalog())
        validation = validate_contract(result.contract, _catalog())

        self.assertTrue(result.ok)
        self.assertFalse(validation["ok"])
        self.assertIn("unknown_stage_in_contract:metric_search", validation["errors"])

    def test_metric_card_type_alias_is_repaired_after_stage_alias(self):
        contract = SearchContract(
            contract_id="q4.metrics",
            stage="table_local_metric_search",
            query_text="metrics for selected table",
            node_sets=["card_type:metric", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["metric"],
        )

        result = repair_contract(contract, _catalog())
        validation = validate_contract(result.contract, _catalog())

        self.assertTrue(result.ok)
        self.assertEqual("table_local_metric_implementation_search", result.contract.stage)
        self.assertIn("card_type:metric_implementation", result.contract.node_sets)
        self.assertNotIn("card_type:metric", result.contract.node_sets)
        self.assertEqual(["metric_implementation"], result.contract.allowed_card_types)
        self.assertTrue(validation["ok"])
        self.assertEqual(
            ["stage_alias", "card_type_alias_nodeset", "allowed_card_type_alias"],
            [row["repair"] for row in result.repairs],
        )

    def test_actual_catalog_card_types_are_covered_when_pack_exists(self):
        pack_dir = REPO_ROOT / "build" / "constrained_search" / "build"
        if not (pack_dir / "resolver_catalog" / "card_catalog.json").exists():
            self.skipTest("constrained-search build catalog is not present")

        self.assertEqual([], missing_card_type_purposes(CatalogBundle.load(pack_dir)))

    def test_evidence_profile_registry_references_known_card_types(self):
        self.assertEqual({}, invalid_profile_card_types())

    def test_generic_profile_stage_validates_for_table_and_domain_local_cards(self):
        table_contract = SearchContract(
            contract_id="q5.profile.value_profile",
            stage="table_local_value_profile_search",
            query_text="value profile evidence",
            node_sets=["card_type:value_profile", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["value_profile"],
        )
        domain_contract = SearchContract(
            contract_id="q5.profile.metric",
            stage="domain_local_metric_search",
            query_text="metric evidence",
            node_sets=["card_type:metric", "domain_id:domain.amazon.orders"],
            allowed_card_types=["metric"],
        )

        catalog = _catalog_with_profile_cards()

        self.assertTrue(validate_contract(table_contract, catalog)["ok"])
        self.assertTrue(validate_contract(domain_contract, catalog)["ok"])

    def test_evidence_manifest_exposes_table_and_domain_local_cards(self):
        manifest = build_evidence_manifest(
            _catalog_with_profile_cards(),
            [_table_card()],
            _table_contract("q.table"),
        )
        table = manifest["tables"][0]

        self.assertIn("query_pattern", table["table_local"])
        self.assertIn("value_profile", table["table_local"])
        self.assertIn("metric", table["domain_local"])
        self.assertEqual("table.zs_observe.amazon_oms", table["table_id"])
        self.assertEqual("domain.amazon.orders", table["domain_id"])

    def test_profile_decision_builds_generic_profile_contracts(self):
        manifest = build_evidence_manifest(
            _catalog_with_profile_cards(),
            [_table_card()],
            _table_contract("q.table"),
        )

        contracts, rejected = profile_contracts_from_decision(
            {
                "selected_profiles": [
                    {
                        "profile_id": "field_semantics_resolution",
                        "answer_obligation": "Resolve value semantics.",
                    }
                ],
                "evidence_requests": [
                    {
                        "profile_id": "field_semantics_resolution",
                        "scope_type": "table",
                        "scope_id": "table.zs_observe.amazon_oms",
                        "card_type": "value_profile",
                        "required": True,
                    }
                ],
                "blocked_reasons": [],
            },
            manifest,
            _table_contract("q.table"),
            "Resolve field values",
        )

        self.assertEqual([], rejected)
        self.assertEqual(1, len(contracts))
        self.assertEqual("table_local_value_profile_search", contracts[0].stage)
        self.assertEqual(["card_type:value_profile", "table_id:table.zs_observe.amazon_oms"], contracts[0].node_sets)
        self.assertEqual(["value_profile"], contracts[0].required_carry_forward["required_evidence_card_types"])

    def test_branch_ledger_uses_profile_required_card_types(self):
        ledger = BranchLedger()
        for contract, card in (
            (_runtime_binding_contract(), _binding_card()),
            (_table_contract("q.table"), _table_card()),
        ):
            ledger.record_contract_discovered(contract)
            ledger.record_contract_started(contract)
            ledger.record_result(
                contract,
                SearchResult(
                    result_id=f"result.{contract.contract_id}",
                    contract_id=contract.contract_id,
                    stage=contract.stage,
                    returned_cards=[card],
                    validation={"ok": True},
                ),
            )

        profile_contract = SearchContract(
            contract_id="q5.profile.field.values",
            stage="table_local_value_profile_search",
            query_text="value profile evidence",
            node_sets=["card_type:value_profile", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["value_profile"],
            required_carry_forward={
                **_branch_carry_forward(),
                "evidence_profile_id": "field_semantics_resolution",
                "required_evidence_card_types": ["value_profile"],
            },
        )
        ledger.record_contract_discovered(profile_contract)
        ledger.record_contract_started(profile_contract)
        ledger.record_result(
            profile_contract,
            SearchResult(
                result_id="result.q5.profile.field.values",
                contract_id=profile_contract.contract_id,
                stage=profile_contract.stage,
                returned_cards=[_value_profile_card()],
                validation={"ok": True},
            ),
        )

        snapshot = ledger.snapshot()
        usable = [branch for branch in snapshot["branches"].values() if branch["status"] == "usable"]
        self.assertEqual(1, len(usable))
        self.assertEqual(["field_semantics_resolution"], usable[0]["selected_evidence_profiles"])
        self.assertEqual(["value_profile"], usable[0]["required_evidence_card_types"])
        self.assertEqual(["value_profile.amazon_oms.order_status"], usable[0]["evidence_cards_by_type"]["value_profile"])

    def test_unambiguous_carry_forward_fills_missing_required_nodeset(self):
        contract = SearchContract(
            contract_id="q2.bindings",
            stage="runtime_account_binding_search",
            query_text="bindings for selected account",
            node_sets=[
                "domain_family:client_runtime",
                "card_type:account_data_binding",
                "tenant_id:tenant.one",
                "group_id:group.one",
            ],
            allowed_card_types=["account_data_binding"],
        )

        result = repair_contract(contract, _catalog(), predecessor_cards=[_platform_account("amazon")])

        self.assertTrue(result.ok)
        self.assertIn("platform_account_id:platform_account.one.amazon.marketplace", result.contract.node_sets)
        self.assertIn("platform_account_id", result.contract.required_carry_forward)

    def test_ambiguous_carry_forward_rejects_contract(self):
        contract = SearchContract(
            contract_id="q2.bindings",
            stage="runtime_account_binding_search",
            query_text="bindings for selected account",
            node_sets=[
                "domain_family:client_runtime",
                "card_type:account_data_binding",
                "tenant_id:tenant.one",
                "group_id:group.one",
            ],
            allowed_card_types=["account_data_binding"],
        )

        result = repair_contract(
            contract,
            _catalog(),
            predecessor_cards=[_platform_account("amazon"), _platform_account("flipkart")],
        )

        self.assertFalse(result.ok)
        self.assertIsNone(result.contract)
        self.assertEqual("ambiguous_carry_forward", result.rejections[0]["rejection"])
        self.assertEqual("platform_account_id", result.rejections[0]["key"])

    def test_state_machine_traces_repairs_and_validation_rejections(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                _UnusedLLM(),
                Path(tmp),
                catalogs=_catalog(),
            )
            contracts = machine._coerce_contracts(
                [
                    {
                        "contract_id": "q1.binding",
                        "stage": "runtime_account_data_binding_search",
                        "query_text": "bindings",
                        "node_sets": [
                            "domain_family:client_runtime",
                            "tenant_id:tenant.one",
                            "group_id:group.one",
                            "platform_account_id:platform_account.one.amazon.marketplace",
                        ],
                        "allowed_card_types": ["account_data_binding"],
                    },
                    {
                        "contract_id": "q1.bad",
                        "stage": "table_schema_search",
                        "query_text": "bad",
                        "node_sets": ["card_type:table", "table_id:table.zs_observe.amazon_oms"],
                        "allowed_card_types": ["table"],
                    },
                ],
                "unit_test",
                "Amazon bindings",
            )

            events = [row["event"] for row in machine.trace]
        self.assertEqual(1, len(contracts))
        self.assertIn("contract_repaired", events)
        self.assertIn("llm_contract_candidate_rejected", events)
        self.assertIn("branch_ledger_contract_discovered", events)

    def test_branch_ledger_tracks_branch_evidence_and_status(self):
        ledger = BranchLedger()
        binding_contract = _runtime_binding_contract()
        ledger.record_contract_discovered(binding_contract)
        ledger.record_contract_started(binding_contract)
        ledger.record_result(
            binding_contract,
            SearchResult(
                result_id="result.binding",
                contract_id=binding_contract.contract_id,
                stage=binding_contract.stage,
                returned_cards=[_binding_card()],
                validation={"ok": True},
            ),
        )

        binding_snapshot = ledger.snapshot()
        partial_branches = [
            branch
            for branch in binding_snapshot["branches"].values()
            if branch["account_data_binding_cards"]
        ]
        self.assertEqual(1, len(partial_branches))
        self.assertEqual("partial", partial_branches[0]["status"])
        self.assertIn("table_frame", partial_branches[0]["missing_evidence"])

        table_contract = _table_contract("q3.table")
        ledger.record_contract_discovered(table_contract)
        ledger.record_contract_started(table_contract)
        ledger.record_result(
            table_contract,
            SearchResult(
                result_id="result.table",
                contract_id=table_contract.contract_id,
                stage=table_contract.stage,
                returned_cards=[_table_card()],
                validation={"ok": True},
            ),
        )

        pattern_contract = _query_pattern_contract("q4.query_pattern")
        ledger.record_contract_discovered(pattern_contract)
        ledger.record_contract_started(pattern_contract)
        ledger.record_result(
            pattern_contract,
            SearchResult(
                result_id="result.query_pattern",
                contract_id=pattern_contract.contract_id,
                stage=pattern_contract.stage,
                returned_cards=[_query_pattern_card()],
                validation={"ok": True},
            ),
        )

        snapshot = ledger.snapshot()
        usable = [branch for branch in snapshot["branches"].values() if branch["status"] == "usable"]
        self.assertEqual(1, len(usable))
        self.assertEqual([], usable[0]["missing_evidence"])
        self.assertEqual(["account_data_binding.one.amazon.oms"], usable[0]["account_data_binding_cards"])
        self.assertEqual(["table.zs_observe.amazon_oms"], usable[0]["table_cards"])
        self.assertEqual(["query_pattern.amazon_oms.top_skus"], usable[0]["query_pattern_cards"])

    def test_blocked_output_includes_branch_snapshot(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                _UnusedLLM(),
                Path(tmp),
                catalogs=_catalog(),
            )
            branch_id = machine.branch_ledger.record_contract_discovered(_runtime_binding_contract())
            output = machine._blocked("unit_blocked")

        self.assertEqual("blocked", output["status"])
        self.assertIn(branch_id, output["branches"])
        self.assertEqual(["pending"], list(output["branch_status"].values()))
        self.assertEqual(0, output["usable_branch_count"])

    def test_scheduler_rotates_across_branches(self):
        ledger = BranchLedger()
        pending = [
            _scheduler_runtime_contract("q.amazon.first", "amazon", "first"),
            _scheduler_runtime_contract("q.amazon.second", "amazon", "second"),
            _scheduler_runtime_contract("q.flipkart.first", "flipkart", "first"),
            _scheduler_runtime_contract("q.flipkart.second", "flipkart", "second"),
        ]
        for contract in pending:
            ledger.record_contract_discovered(contract)

        ordered = prune_and_rank_pending(
            pending,
            "top SKUs across marketplaces",
            [],
            set(),
            max_pending=4,
            branch_ledger=ledger,
            branch_max_steps=8,
        )

        self.assertEqual(4, len(ordered))
        self.assertEqual(
            2,
            len({ledger.contract_branches[contract.contract_id] for contract in ordered[:2]}),
        )
        self.assertEqual(
            ["q.amazon.first", "q.flipkart.first", "q.amazon.second", "q.flipkart.second"],
            [contract.contract_id for contract in ordered],
        )

    def test_scheduler_drops_branch_over_step_cap(self):
        ledger = BranchLedger()
        executed = _scheduler_runtime_contract("q.amazon.executed", "amazon", "executed")
        pending = _scheduler_runtime_contract("q.amazon.pending", "amazon", "pending")
        ledger.record_contract_discovered(executed)
        ledger.record_contract_started(executed)
        ledger.record_contract_discovered(pending)

        ordered = prune_and_rank_pending(
            [pending],
            "top SKUs across marketplaces",
            [],
            set(),
            max_pending=4,
            branch_ledger=ledger,
            branch_max_steps=1,
        )

        self.assertEqual([], ordered)

    def test_scheduler_honors_max_pending(self):
        ledger = BranchLedger()
        pending = [
            _scheduler_runtime_contract("q.amazon", "amazon", "one"),
            _scheduler_runtime_contract("q.flipkart", "flipkart", "one"),
            _scheduler_runtime_contract("q.myntra", "myntra", "one"),
        ]
        for contract in pending:
            ledger.record_contract_discovered(contract)

        ordered = prune_and_rank_pending(
            pending,
            "top SKUs across marketplaces",
            [],
            set(),
            max_pending=2,
            branch_ledger=ledger,
            branch_max_steps=8,
        )

        self.assertEqual(2, len(ordered))

    def test_scheduler_prioritizes_breadth_before_deep_table_work(self):
        ledger = BranchLedger()
        binding_contract = _runtime_binding_contract()
        ledger.record_contract_discovered(binding_contract)
        ledger.record_contract_started(binding_contract)
        binding_result = SearchResult(
            result_id="result.amazon.binding",
            contract_id=binding_contract.contract_id,
            stage=binding_contract.stage,
            returned_cards=[_binding_card()],
            validation={"ok": True},
        )
        ledger.record_result(binding_contract, binding_result)

        deep_table_work = _query_pattern_contract("q.amazon.deep")
        pending_platform = SearchContract(
            contract_id="q.flipkart.platform",
            stage="runtime_platform_account_search",
            query_text="Flipkart platform account",
            node_sets=[
                "domain_family:client_runtime",
                "card_type:platform_account",
                "tenant_id:tenant.one",
                "group_id:group.one",
                "platform_id:platform.flipkart",
            ],
            allowed_card_types=["platform_account"],
        )
        ledger.record_contract_discovered(deep_table_work)
        ledger.record_contract_discovered(pending_platform)

        ordered = prune_and_rank_pending(
            [deep_table_work, pending_platform],
            "top SKUs across marketplaces",
            [binding_result],
            set(),
            max_pending=2,
            branch_ledger=ledger,
            branch_max_steps=8,
        )

        self.assertEqual(["q.flipkart.platform", "q.amazon.deep"], [contract.contract_id for contract in ordered])

    def test_scheduler_keeps_required_profile_contract_at_branch_step_limit(self):
        ledger = BranchLedger()
        starter_contract = _table_contract("q.table.starter")
        binding_contract = _runtime_binding_contract()
        ledger.record_contract_discovered(starter_contract)
        for _ in range(8):
            ledger.record_contract_started(starter_contract)

        required = SearchContract(
            contract_id="q.required.columns",
            stage="table_local_column_search",
            query_text="Required column evidence",
            node_sets=["card_type:column", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["column"],
            required_carry_forward={
                **_branch_carry_forward(),
                "evidence_profile_id": "table_contract_resolution",
                "required_evidence_card_types": ["column"],
            },
        )
        optional = SearchContract(
            contract_id="q.optional.metric",
            stage="domain_local_metric_search",
            query_text="Optional metric evidence",
            node_sets=["card_type:metric", "domain_id:domain.amazon.orders"],
            allowed_card_types=["metric"],
            required_carry_forward={
                **_branch_carry_forward(),
                "domain_id": "domain.amazon.orders",
                "evidence_profile_id": "measure_calculation_resolution",
                "optional_evidence_card_types": ["metric"],
            },
        )
        ledger.record_contract_discovered(required)
        ledger.record_contract_discovered(optional)

        ordered = prune_and_rank_pending(
            [optional, required],
            "Top selling SKUs on Amazon",
            [
                SearchResult(
                    result_id="result.binding",
                    contract_id=binding_contract.contract_id,
                    stage=binding_contract.stage,
                    returned_cards=[_binding_card()],
                    validation={"ok": True},
                )
            ],
            set(),
            max_pending=4,
            branch_ledger=ledger,
            branch_max_steps=8,
        )

        self.assertEqual(["q.required.columns"], [contract.contract_id for contract in ordered])

    def test_serialized_run_does_not_finalize_while_platform_branch_is_pending(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = _SerializedNoEarlyCompleteMachine(
                _UnusedClient(),
                _SerializedNoEarlyCompleteLLM(),
                Path(tmp),
                catalogs=_catalog(),
                completion_policy="best_effort",
            )

            output = asyncio.run(
                machine.run_query(
                    "Top selling SKUs across marketplaces",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                )
        )

        self.assertEqual("best_effort", output["status"])
        self.assertIn("q.flipkart.pending", machine.executed_contract_ids)
        self.assertIn("q.amazon.query_pattern", machine.executed_contract_ids)

    def test_same_table_nodeset_is_not_deduped_across_runtime_bindings(self):
        first = SearchContract(
            contract_id="q.table.first",
            stage="semantic_table_frame_search",
            query_text="shared table for first binding",
            node_sets=["card_type:table", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["table"],
            required_carry_forward={
                "tenant_id": "tenant.one",
                "group_id": "group.one",
                "platform_account_id": "platform_account.one.amazon_india.marketplace",
                "account_data_binding_id": "account_data_binding.one.amazon_india.oms",
                "table_id": "table.zs_observe.amazon_oms",
            },
        )
        second = SearchContract(
            contract_id="q.table.second",
            stage="semantic_table_frame_search",
            query_text="shared table for second binding",
            node_sets=["card_type:table", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["table"],
            required_carry_forward={
                "tenant_id": "tenant.one",
                "group_id": "group.one",
                "platform_account_id": "platform_account.one.amazon_us.marketplace",
                "account_data_binding_id": "account_data_binding.one.amazon_us.oms",
                "table_id": "table.zs_observe.amazon_oms",
            },
        )
        binding_results = [
            SearchResult(
                result_id="result.bindings",
                contract_id="q.bindings",
                stage="runtime_account_binding_search",
                returned_cards=[
                    {
                        "canonical_id": "account_data_binding.one.amazon_india.oms",
                        "card_type": "account_data_binding",
                        "node_sets": [
                            "card_type:account_data_binding",
                            "tenant_id:tenant.one",
                            "group_id:group.one",
                            "platform_account_id:platform_account.one.amazon_india.marketplace",
                            "account_data_binding_id:account_data_binding.one.amazon_india.oms",
                            "source_role:oms_sales",
                            "table_id:table.zs_observe.amazon_oms",
                        ],
                    },
                    {
                        "canonical_id": "account_data_binding.one.amazon_us.oms",
                        "card_type": "account_data_binding",
                        "node_sets": [
                            "card_type:account_data_binding",
                            "tenant_id:tenant.one",
                            "group_id:group.one",
                            "platform_account_id:platform_account.one.amazon_us.marketplace",
                            "account_data_binding_id:account_data_binding.one.amazon_us.oms",
                            "source_role:oms_sales",
                            "table_id:table.zs_observe.amazon_oms",
                        ],
                    },
                ],
                validation={"ok": True},
            )
        ]

        prepared = prune_and_rank_pending(
            [first, second],
            "Top selling SKUs across marketplaces",
            binding_results,
            set(),
            max_pending=4,
            branch_ledger=BranchLedger(),
        )

        self.assertNotEqual(contract_signature(first), contract_signature(second))
        self.assertCountEqual(["q.table.first", "q.table.second"], [contract.contract_id for contract in prepared])

    def test_runtime_binding_inventory_selects_table_frame_without_binding_recall(self):
        with tempfile.TemporaryDirectory() as tmp:
            llm = _InventorySelectionLLM(["account_data_binding.one.amazon.oms"])
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                llm,
                Path(tmp),
                catalogs=_catalog(),
            )
            result = SearchResult(
                result_id="result.platform.amazon",
                contract_id="q1.platform.amazon",
                stage="runtime_platform_account_search",
                returned_cards=[_platform_account("amazon")],
                validation={"ok": True},
            )

            selected_results, table_contracts = asyncio.run(
                machine._select_runtime_binding_inventory(
                    "Top selling SKUs",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                    {"validated_output": {}},
                    result,
                )
            )

        self.assertEqual(["account_data_binding.one.amazon.oms"], [card["canonical_id"] for card in selected_results[0].returned_cards])
        self.assertEqual(1, len(table_contracts))
        self.assertEqual("semantic_table_frame_search", table_contracts[0].stage)
        self.assertEqual(["card_type:table", "table_id:table.zs_observe.amazon_oms"], table_contracts[0].node_sets)
        self.assertEqual("account_data_binding.one.amazon.oms", table_contracts[0].required_carry_forward["account_data_binding_id"])
        self.assertEqual("oms_sales", table_contracts[0].required_carry_forward["source_role"])
        self.assertEqual("platform_account.one.amazon.marketplace", table_contracts[0].required_carry_forward["platform_account_id"])
        self.assertEqual("table.zs_observe.amazon_oms", table_contracts[0].required_carry_forward["table_id"])
        self.assertEqual(
            ["account_data_binding.one.amazon.oms", "account_data_binding.one.amazon.returns"],
            llm.selected_binding_ids_seen,
        )
        self.assertTrue(any(row["event"] == "runtime_binding_inventory_selected" for row in machine.trace))

    def test_constrained_route_reaches_platform_sales_table(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = _ConstrainedRouteMachine(
                _UnusedClient(),
                _ConstrainedRouteLLM(),
                Path(tmp),
                catalogs=_catalog(),
                max_steps=8,
            )

            output = asyncio.run(
                machine.run_query(
                    "Top selling SKUs on Amazon",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                )
            )

        self.assertEqual("blocked", output["status"])
        self.assertIn("table.zs_observe.amazon_oms", _finalized_table_ids(machine.trace))
        self.assertIn("q2.runtime.bindings.platform_account_one_amazon_marketplace", machine.executed_contract_ids)
        self.assertTrue(any(row["event"] == "domains_selected_for_table_search" for row in machine.trace))

    def test_profile_selector_drives_post_table_evidence_contracts(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = _ConstrainedRouteMachine(
                _UnusedClient(),
                _ProfileSelectionLLM(),
                Path(tmp),
                catalogs=_catalog(),
                max_steps=12,
            )

            output = asyncio.run(
                machine.run_query(
                    "Top selling SKUs on Amazon",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                )
            )

        self.assertEqual("best_effort", output["status"])
        self.assertTrue(any(contract_id.startswith("q5.profile.query_shape_resolution") for contract_id in machine.executed_contract_ids))
        self.assertTrue(any(row["event"] == "table_evidence_manifest_built" for row in machine.trace))
        self.assertTrue(any(row["event"] == "llm_evidence_profile_decision" for row in machine.trace))
        self.assertEqual(
            "query_shape_resolution",
            output["evidence_pack"]["evidence_profile_decisions"][0]["validated_output"]["selected_profiles"][0]["profile_id"],
        )

    def test_constrained_route_reaches_multiple_domain_tables(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = _ConstrainedRouteMachine(
                _UnusedClient(),
                _ConstrainedRouteLLM(),
                Path(tmp),
                catalogs=_catalog(),
                max_steps=20,
            )

            output = asyncio.run(
                machine.run_query(
                    "Compare Amazon sales and returns",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                )
            )

        self.assertEqual("blocked", output["status"])
        finalized_tables = _finalized_table_ids(machine.trace)
        self.assertIn("table.zs_observe.amazon_oms", finalized_tables)
        self.assertIn("table.zs_observe.amazon_returns", finalized_tables)
        self.assertGreaterEqual(finalized_tables.count("table.zs_observe.amazon_oms"), 1)
        self.assertGreaterEqual(finalized_tables.count("table.zs_observe.amazon_returns"), 1)

    def test_best_effort_completion_uses_only_usable_branch_evidence(self):
        with tempfile.TemporaryDirectory() as tmp:
            llm = _RecordingLLM()
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                llm,
                Path(tmp),
                catalogs=_catalog(),
                completion_policy="best_effort",
            )
            results = _record_usable_amazon_branch(machine.branch_ledger)
            results.extend(_record_partial_flipkart_branch(machine.branch_ledger))
            terminal = {
                "ready": False,
                "checks": {},
                "binding_card_ids": [],
                "table_card_ids": [],
                "query_pattern_card_ids": [],
                "metric_implementation_card_ids": [],
            }

            output = asyncio.run(
                machine._complete_or_block(
                    "unit_exhausted",
                    {"steps_executed": 4},
                    "Top SKUs across marketplaces",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                    results,
                    4,
                    terminal,
                    [],
                )
            )

        packed_ids = _packed_card_ids(llm.evidence_pack)
        self.assertEqual("best_effort", output["status"])
        self.assertEqual(1, output["usable_branch_count"])
        self.assertEqual(1, output["incomplete_branch_count"])
        self.assertEqual(["account_data_binding.one.flipkart.oms"], output["branches"][output["incomplete_branch_ids"][0]]["account_data_binding_cards"])
        self.assertIn("account_data_binding.one.amazon.oms", packed_ids)
        self.assertIn("table.zs_observe.amazon_oms", packed_ids)
        self.assertIn("query_pattern.amazon_oms.top_skus", packed_ids)
        self.assertNotIn("account_data_binding.one.flipkart.oms", packed_ids)
        self.assertEqual(output["usable_branch_ids"], llm.evidence_pack["usable_branch_ids"])
        self.assertEqual("branch_incomplete", output["best_effort_warnings"][0]["warning"])

    def test_branch_with_table_columns_is_usable_without_query_pattern(self):
        ledger = BranchLedger()
        binding_contract = _runtime_binding_contract()
        ledger.record_contract_discovered(binding_contract)
        ledger.record_contract_started(binding_contract)
        ledger.record_result(
            binding_contract,
            SearchResult(
                result_id="result.binding",
                contract_id=binding_contract.contract_id,
                stage=binding_contract.stage,
                returned_cards=[_binding_card()],
                validation={"ok": True},
            ),
        )
        table_contract = _table_contract("q.table")
        ledger.record_contract_discovered(table_contract)
        ledger.record_contract_started(table_contract)
        ledger.record_result(
            table_contract,
            SearchResult(
                result_id="result.table",
                contract_id=table_contract.contract_id,
                stage=table_contract.stage,
                returned_cards=[_table_card()],
                validation={"ok": True},
            ),
        )
        column_contract = SearchContract(
            contract_id="q.columns",
            stage="table_local_column_search",
            query_text="columns",
            node_sets=["card_type:column", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["column"],
            required_carry_forward=_branch_carry_forward(),
        )
        ledger.record_contract_discovered(column_contract)
        ledger.record_contract_started(column_contract)
        ledger.record_result(
            column_contract,
            SearchResult(
                result_id="result.columns",
                contract_id=column_contract.contract_id,
                stage=column_contract.stage,
                returned_cards=[_column_card()],
                validation={"ok": True},
            ),
        )

        snapshot = ledger.snapshot()
        usable = [branch for branch in snapshot["branches"].values() if branch["status"] == "usable"]
        self.assertEqual(1, len(usable))
        self.assertEqual([], usable[0]["missing_evidence"])

    def test_no_usable_branch_still_blocks(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                _RecordingLLM(),
                Path(tmp),
                catalogs=_catalog(),
                completion_policy="best_effort",
            )
            machine.branch_ledger.record_contract_discovered(_scheduler_runtime_contract("q.flipkart.pending", "flipkart", "pending"))

            output = asyncio.run(
                machine._complete_or_block(
                    "search_exhausted_without_terminal_evidence",
                    {"steps_executed": 1},
                    "Top SKUs across marketplaces",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                    [],
                    1,
                    {"ready": False, "checks": {}},
                    [],
                )
            )

        self.assertEqual("blocked", output["status"])
        self.assertEqual("search_exhausted_without_terminal_evidence", output["blocked_reason"])
        self.assertEqual(0, output["usable_branch_count"])
        self.assertEqual(1, output["incomplete_branch_count"])

    def test_strict_completion_blocks_when_any_branch_is_incomplete(self):
        with tempfile.TemporaryDirectory() as tmp:
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                _RecordingLLM(),
                Path(tmp),
                catalogs=_catalog(),
                completion_policy="strict",
            )
            results = _record_usable_amazon_branch(machine.branch_ledger)
            machine.branch_ledger.record_contract_discovered(_scheduler_runtime_contract("q.flipkart.pending", "flipkart", "pending"))

            output = asyncio.run(
                machine._complete_or_block(
                    "max_steps_exhausted_before_pending_contracts_completed",
                    {"steps_executed": 4},
                    "Top SKUs across marketplaces",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                    results,
                    4,
                    {"ready": True, "checks": {"runtime_binding": True, "table_frame": True, "query_pattern": True}},
                    [],
                )
            )

        self.assertEqual("blocked", output["status"])
        self.assertEqual("max_steps_exhausted_before_pending_contracts_completed", output["blocked_reason"])
        self.assertEqual("strict", output["completion_policy"])

    def test_partial_completion_policy_skips_sql_handoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            llm = _RecordingLLM()
            machine = CogneeSearchStateMachine(
                _UnusedClient(),
                llm,
                Path(tmp),
                catalogs=_catalog(),
                completion_policy="partial",
            )
            results = _record_usable_amazon_branch(machine.branch_ledger)
            machine.branch_ledger.record_contract_discovered(_scheduler_runtime_contract("q.flipkart.pending", "flipkart", "pending"))

            output = asyncio.run(
                machine._complete_or_block(
                    "unit_exhausted",
                    {"steps_executed": 4},
                    "Top SKUs across marketplaces",
                    {"tenant_id": "tenant.one", "group_id": "group.one"},
                    results,
                    4,
                    {"ready": True, "checks": {"runtime_binding": True, "table_frame": True, "query_pattern": True}},
                    [],
                )
            )

        self.assertEqual("partial", output["status"])
        self.assertIsNone(llm.evidence_pack)
        self.assertEqual("skipped", output["handoff"]["status"])
        self.assertEqual("completion_policy_partial_incomplete_branches", output["handoff"]["reason"])


class _UnusedClient:
    pass


class _UnusedLLM:
    pass


class _RecordingLLM:
    def __init__(self):
        self.evidence_pack = None

    async def write_sql_handoff(self, query_text, evidence_pack):
        self.evidence_pack = evidence_pack
        return _HandoffResult({"status": "ok", "query_text": query_text})


class _InventorySelectionLLM:
    def __init__(self, selected_binding_ids):
        self.selected_binding_ids = selected_binding_ids
        self.selected_binding_ids_seen = []

    async def select_runtime_bindings(self, query_text, anchor_decision, runtime_candidates):
        self.selected_binding_ids_seen = [candidate["account_data_binding_id"] for candidate in runtime_candidates]
        return _Decision(
            {
                "selected_platform_account_ids": [],
                "selected_binding_ids": self.selected_binding_ids,
                "selected_table_ids": ["table.zs_observe.amazon_oms"],
                "rejected_candidate_ids": [],
                "selection_reasons": {},
                "next_search_contracts": [],
                "blocked_reasons": [],
            }
        )


class _SerializedNoEarlyCompleteLLM:
    async def extract_anchors(self, query_text, runtime_context):
        return _Decision(
            {
                "platform_mentions": [],
                "source_role_mentions": [],
                "operation_shape": "comparison",
                "requires_relationship_search": False,
                "requires_reconciliation_search": False,
                "next_search_contracts": [
                    _runtime_binding_contract().to_dict(),
                    _runtime_binding_contract_for("q.flipkart.pending", "flipkart").to_dict(),
                ],
            }
        )

    async def select_runtime_bindings(self, query_text, anchor_decision, runtime_candidates):
        if runtime_candidates and runtime_candidates[0].get("candidate_type") == "runtime_binding_table_candidate":
            return _Decision(
                {
                    "selected_platform_account_ids": [],
                    "selected_binding_ids": ["account_data_binding.one.amazon.oms"],
                    "selected_table_ids": [],
                    "rejected_candidate_ids": [],
                    "selection_reasons": {},
                    "next_search_contracts": [],
                    "blocked_reasons": [],
                }
            )
        return _Decision(
            {
                "selected_platform_account_ids": [],
                "selected_binding_ids": [],
                "selected_table_ids": [],
                "rejected_candidate_ids": [],
                "selection_reasons": {},
                "next_search_contracts": [],
                "blocked_reasons": [],
            }
        )

    async def plan_next_nodesets(self, query_text, predecessor_result):
        if predecessor_result["stage"] == "semantic_table_frame_search":
            return _Decision(
                {
                    "next_search_contracts": [_query_pattern_contract("q.amazon.query_pattern").to_dict()],
                    "closed_gates": [],
                    "blocked_reasons": [],
                }
            )
        return _Decision({"next_search_contracts": [], "closed_gates": [], "blocked_reasons": []})

    async def rank_bounded_candidates(self, query_text, contract, returned_cards):
        card_type = returned_cards[0].get("card_type") if returned_cards else None
        selected = []
        if card_type == "domain":
            selected = ["domain.amazon.orders"]
        elif card_type == "table":
            selected = ["table.zs_observe.amazon_oms"]
        return _Decision(
            {
                "selected_card_ids": selected,
                "rejected_card_ids": [],
                "selection_reasons": {},
                "next_search_contracts": [],
                "exact_dereference_requests": [],
                "blocked_reasons": [],
            }
        )

    async def write_sql_handoff(self, query_text, evidence_pack):
        return _HandoffResult({"handoff_status": "ok", "source_blocks": [], "blocked_reasons": []})


class _SerializedNoEarlyCompleteMachine(CogneeSearchStateMachine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executed_contract_ids = []

    async def _select_runtime_binding_inventory(self, query_text, runtime_context, anchor_decision, result):
        return None

    async def execute_contract(self, contract):
        self.executed_contract_ids.append(contract.contract_id)
        self.branch_ledger.record_contract_started(contract)
        cards_by_contract = {"q.amazon.query_pattern": [_query_pattern_card()]}
        if contract.stage == "runtime_account_binding_search" and contract.contract_id == "q2.bindings":
            cards = [_binding_card()]
        elif contract.stage == "semantic_domain_search":
            cards = [_domain_card("orders")]
        elif contract.stage == "semantic_domain_table_search":
            cards = [_table_card()]
        elif contract.stage == "semantic_table_frame_search":
            cards = [_table_card()]
        else:
            cards = cards_by_contract.get(contract.contract_id, [])
        result = SearchResult(
            result_id=f"result.{contract.contract_id}",
            contract_id=contract.contract_id,
            stage=contract.stage,
            returned_cards=cards,
            validation={"ok": True},
        )
        self.branch_ledger.record_result(contract, result)
        return result


class _ConstrainedRouteLLM:
    async def extract_anchors(self, query_text, runtime_context):
        return _Decision(
            {
                "platform_mentions": [],
                "source_role_mentions": [],
                "operation_shape": "comparison",
                "requires_relationship_search": False,
                "requires_reconciliation_search": False,
                "next_search_contracts": [
                    SearchContract(
                        contract_id="q1.runtime.platform_accounts.scoped",
                        stage="runtime_platform_account_search",
                        query_text="Relevant platform accounts",
                        node_sets=[
                            "domain_family:client_runtime",
                            "card_type:platform_account",
                            "tenant_id:tenant.one",
                            "group_id:group.one",
                        ],
                        top_k=10,
                        allowed_card_types=["platform_account"],
                    ).to_dict()
                ],
            }
        )

    async def select_runtime_bindings(self, query_text, anchor_decision, runtime_candidates):
        if runtime_candidates and runtime_candidates[0].get("card_type") == "platform_account":
            return _Decision(
                {
                    "selected_platform_account_ids": ["platform_account.one.amazon.marketplace"],
                    "selected_binding_ids": [],
                    "selected_table_ids": [],
                    "rejected_candidate_ids": [],
                    "selection_reasons": {},
                    "next_search_contracts": [],
                    "blocked_reasons": [],
                }
            )

        selected = ["account_data_binding.one.amazon.oms"]
        if "return" in query_text.lower():
            selected.append("account_data_binding.one.amazon.returns")
        return _Decision(
            {
                "selected_platform_account_ids": [],
                "selected_binding_ids": selected,
                "selected_table_ids": [],
                "rejected_candidate_ids": [],
                "selection_reasons": {},
                "next_search_contracts": [],
                "blocked_reasons": [],
            }
        )

    async def plan_next_nodesets(self, query_text, predecessor_result):
        return _Decision({"next_search_contracts": [], "closed_gates": [], "blocked_reasons": []})

    async def rank_bounded_candidates(self, query_text, contract, returned_cards):
        card_type = returned_cards[0].get("card_type") if returned_cards else None
        query = query_text.lower()
        selected: list[str] = []
        if card_type == "account_data_binding":
            for card in returned_cards:
                cid = card["canonical_id"]
                if "return" in query and "returns" in cid:
                    selected.append(cid)
                if any(token in query for token in ("sales", "selling", "sku")) and cid.endswith("amazon.oms"):
                    selected.append(cid)
        elif card_type == "domain":
            for card in returned_cards:
                cid = card["canonical_id"]
                if "return" in query and "returns" in cid:
                    selected.append(cid)
                if any(token in query for token in ("sales", "selling", "sku")) and "orders" in cid:
                    selected.append(cid)
        elif card_type == "table":
            for card in returned_cards:
                cid = card["canonical_id"]
                if "return" in query and "returns" in cid:
                    selected.append(cid)
                if any(token in query for token in ("sales", "selling", "sku")) and cid.endswith("amazon_oms"):
                    selected.append(cid)
        return _Decision(
            {
                "selected_card_ids": selected,
                "rejected_card_ids": [],
                "selection_reasons": {},
                "next_search_contracts": [],
                "exact_dereference_requests": [],
                "blocked_reasons": [],
            }
        )

    async def write_sql_handoff(self, query_text, evidence_pack):
        return _HandoffResult({"handoff_status": "blocked", "source_blocks": [], "blocked_reasons": []})


class _ProfileSelectionLLM(_ConstrainedRouteLLM):
    async def select_evidence_profiles(self, query_text, runtime_context, evidence_manifest):
        table_id = evidence_manifest["tables"][0]["table_id"]
        return _Decision(
            {
                "selected_profiles": [
                    {
                        "profile_id": "query_shape_resolution",
                        "answer_obligation": "Resolve query/report shape evidence for the selected legal table.",
                        "required_card_types": ["query_pattern"],
                        "optional_card_types": [],
                        "column_strategy": "none",
                    }
                ],
                "evidence_requests": [
                    {
                        "request_id": "req.query_pattern",
                        "profile_id": "query_shape_resolution",
                        "scope_type": "table",
                        "scope_id": table_id,
                        "card_type": "query_pattern",
                        "required": True,
                        "top_k": 8,
                        "answer_obligation": "Resolve the query pattern for the selected table.",
                    }
                ],
                "selection_reasons": {},
                "blocked_reasons": [],
            }
        )


class _ConstrainedRouteMachine(CogneeSearchStateMachine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.executed_contract_ids = []

    async def execute_contract(self, contract):
        self.executed_contract_ids.append(contract.contract_id)
        self.branch_ledger.record_contract_started(contract)
        cards = self._cards_for_contract(contract)
        result = SearchResult(
            result_id=f"result.{contract.contract_id}",
            contract_id=contract.contract_id,
            stage=contract.stage,
            returned_cards=cards,
            validation={"ok": True},
        )
        self.branch_ledger.record_result(contract, result)
        self.trace.append({"event": "contract_validated", "contract": contract.to_dict(), "validation": {"ok": True}})
        self.trace.append({"event": "cognee_result_validated", "result": result.to_dict()})
        return result

    def _cards_for_contract(self, contract):
        node_sets = contract.node_sets
        if contract.stage == "runtime_platform_account_search":
            return [_platform_account("amazon"), _platform_account("flipkart")]
        if contract.stage == "runtime_account_binding_search":
            return [_binding_card(), _returns_binding_card()]
        if contract.stage == "semantic_domain_search":
            binding_id = contract.required_carry_forward.get("account_data_binding_id")
            if binding_id == "account_data_binding.one.amazon.returns":
                return [_domain_card("returns")]
            return [_domain_card("orders"), _domain_card("returns")]
        if contract.stage == "semantic_domain_table_search":
            if "domain_id:domain.amazon.returns" in node_sets:
                return [_returns_table_card()]
            if "domain_id:domain.amazon.orders" in node_sets:
                return [_table_card()]
        if contract.stage == "semantic_table_frame_search":
            if "table_id:table.zs_observe.amazon_returns" in node_sets:
                return [_returns_table_card()]
            return [_table_card()]
        if contract.stage == "table_local_query_pattern_search":
            return [_query_pattern_card()]
        if contract.stage == "table_local_value_profile_search":
            return [_value_profile_card()]
        return []


class _HandoffResult:
    def __init__(self, payload):
        self.payload = payload

    def to_dict(self):
        return self.payload


class _Decision:
    def __init__(self, payload):
        self.validated_output = payload

    def to_dict(self):
        return {"validated_output": self.validated_output}


def _catalog() -> CatalogBundle:
    node_sets = {
        "domain_family:client_runtime",
        "card_type:platform_account",
        "card_type:account_data_binding",
        "card_type:table",
        "card_type:column",
        "card_type:metric_implementation",
        "tenant_id:tenant.one",
        "group_id:group.one",
        "platform_id:platform.amazon",
        "platform_id:platform.flipkart",
        "platform_account_id:platform_account.one.amazon.marketplace",
        "platform_account_id:platform_account.one.flipkart.marketplace",
        "account_data_binding_id:account_data_binding.one.amazon.oms",
        "account_data_binding_id:account_data_binding.one.amazon.returns",
        "source_role:oms_sales",
        "source_role:returns",
        "table_id:table.zs_observe.amazon_oms",
        "table_id:table.zs_observe.amazon_returns",
        "card_type:domain",
        "domain_family:marketplace",
        "platform_context_id:platform_context.amazon.in",
        "domain_id:domain.amazon.orders",
        "domain_id:domain.amazon.returns",
        "card_type:query_pattern",
        "canonical_id:account_data_binding.one.amazon.oms",
        "canonical_id:account_data_binding.one.amazon.returns",
        "canonical_id:table.zs_observe.amazon_oms",
        "canonical_id:table.zs_observe.amazon_returns",
        "canonical_id:domain.amazon.orders",
        "canonical_id:domain.amazon.returns",
        "canonical_id:column.zs_observe.amazon_oms.sku_id",
        "canonical_id:query_pattern.amazon_oms.top_skus",
    }
    binding_card = _binding_card()
    returns_binding_card = _returns_binding_card()
    table_card = _table_card()
    returns_table_card = _returns_table_card()
    orders_domain_card = _domain_card("orders")
    returns_domain_card = _domain_card("returns")
    column_card = {
        "canonical_id": "column.zs_observe.amazon_oms.sku_id",
        "canonical_name": "amazon_oms.sku_id",
        "card_type": "column",
        "node_sets": [
            "card_type:column",
            "table_id:table.zs_observe.amazon_oms",
        ],
    }
    query_pattern_card = _query_pattern_card()
    return CatalogBundle(
        pack_dir=Path("unused"),
        card_catalog={
            binding_card["canonical_id"]: binding_card,
            returns_binding_card["canonical_id"]: returns_binding_card,
            table_card["canonical_id"]: table_card,
            returns_table_card["canonical_id"]: returns_table_card,
            orders_domain_card["canonical_id"]: orders_domain_card,
            returns_domain_card["canonical_id"]: returns_domain_card,
            column_card["canonical_id"]: column_card,
            query_pattern_card["canonical_id"]: query_pattern_card,
        },
        search_contract_templates={
            "runtime_platform_account_search": {
                "required_node_set_keys": ["domain_family", "card_type", "tenant_id", "group_id", "platform_id"],
                "card_type": "platform_account",
            },
            "runtime_account_binding_search": {
                "required_node_set_keys": ["domain_family", "card_type", "tenant_id", "group_id", "platform_account_id"],
                "card_type": "account_data_binding",
            },
            "semantic_table_frame_search": {
                "required_node_set_keys": ["card_type", "table_id"],
                "card_type": "table",
            },
            "table_local_query_pattern_search": {
                "required_node_set_keys": ["card_type", "table_id"],
                "card_type": "query_pattern",
            },
            "table_local_metric_implementation_search": {
                "required_node_set_keys": ["card_type", "table_id"],
                "card_type": "metric_implementation",
            },
        },
        runtime_binding_catalog=[
            {
                "canonical_id": "account_data_binding.one.amazon.oms",
                "node_sets": binding_card["node_sets"],
                "platform_account_id": "platform_account.one.amazon.marketplace",
                "platform_id": "platform.amazon",
                "source_role": "oms_sales",
                "table_id": "table.zs_observe.amazon_oms",
                "scope_keys": [
                    {"business_key": "group_id", "runtime_value": "1"},
                ],
            },
            {
                "canonical_id": "account_data_binding.one.amazon.returns",
                "node_sets": returns_binding_card["node_sets"],
                "platform_account_id": "platform_account.one.amazon.marketplace",
                "platform_id": "platform.amazon",
                "source_role": "returns",
                "table_id": "table.zs_observe.amazon_returns",
                "scope_keys": [
                    {"business_key": "group_id", "runtime_value": "1"},
                ],
            }
        ],
        runtime_binding_status_catalog={
            "account_data_binding.one.amazon.oms": {
                "binding_status": "active",
            },
            "account_data_binding.one.amazon.returns": {
                "binding_status": "active",
            }
        },
        table_contract_catalog={
            "table.zs_observe.amazon_oms": {"canonical_id": "table.zs_observe.amazon_oms"},
            "table.zs_observe.amazon_returns": {"canonical_id": "table.zs_observe.amazon_returns"},
        },
        node_set_values=node_sets,
        platform_alias_map={"amazon": "platform.amazon", "flipkart": "platform.flipkart"},
    )


def _catalog_with_profile_cards() -> CatalogBundle:
    catalog = _catalog()
    for card in (_value_profile_card(), _metric_card()):
        catalog.card_catalog[card["canonical_id"]] = card
        catalog.node_set_values.update(card["node_sets"])
        catalog.node_set_values.add(f"canonical_id:{card['canonical_id']}")
    return catalog


def _platform_account(platform: str) -> dict:
    platform_account_id = f"platform_account.one.{platform}.marketplace"
    return {
        "canonical_id": platform_account_id,
        "card_type": "platform_account",
        "node_sets": [
            "domain_family:client_runtime",
            "card_type:platform_account",
            "tenant_id:tenant.one",
            "group_id:group.one",
            f"platform_id:platform.{platform}",
            f"platform_context_id:platform_context.{platform}.in",
            f"platform_account_id:{platform_account_id}",
        ],
    }


def _runtime_binding_contract() -> SearchContract:
    return _runtime_binding_contract_for("q2.bindings", "amazon")


def _runtime_binding_contract_for(contract_id: str, platform: str) -> SearchContract:
    return SearchContract(
        contract_id=contract_id,
        stage="runtime_account_binding_search",
        query_text=f"{platform} OMS binding",
        node_sets=[
            "domain_family:client_runtime",
            "card_type:account_data_binding",
            "tenant_id:tenant.one",
            "group_id:group.one",
            f"platform_id:platform.{platform}",
            f"platform_account_id:platform_account.one.{platform}.marketplace",
        ],
        allowed_card_types=["account_data_binding"],
    )


def _scheduler_runtime_contract(contract_id: str, platform: str, marker: str) -> SearchContract:
    return SearchContract(
        contract_id=contract_id,
        stage="runtime_account_binding_search",
        query_text=f"{platform} runtime binding {marker}",
        node_sets=[
            "domain_family:client_runtime",
            "card_type:account_data_binding",
            "tenant_id:tenant.one",
            "group_id:group.one",
            f"platform_id:platform.{platform}",
            f"platform_account_id:platform_account.one.{platform}.marketplace",
            f"scheduler_marker:{marker}",
        ],
        allowed_card_types=["account_data_binding"],
    )


def _table_contract(contract_id: str) -> SearchContract:
    return SearchContract(
        contract_id=contract_id,
        stage="semantic_table_frame_search",
        query_text="Amazon OMS table frame",
        node_sets=[
            "card_type:table",
            "table_id:table.zs_observe.amazon_oms",
        ],
        allowed_card_types=["table"],
        required_carry_forward=_branch_carry_forward(),
    )


def _query_pattern_contract(contract_id: str) -> SearchContract:
    return SearchContract(
        contract_id=contract_id,
        stage="table_local_query_pattern_search",
        query_text="Top SKU query pattern",
        node_sets=[
            "card_type:query_pattern",
            "table_id:table.zs_observe.amazon_oms",
        ],
        allowed_card_types=["query_pattern"],
        required_carry_forward=_branch_carry_forward(),
    )


def _branch_carry_forward() -> dict:
    return {
        "tenant_id": "tenant.one",
        "group_id": "group.one",
        "platform_id": "platform.amazon",
        "platform_context_id": "platform_context.amazon.in",
        "platform_account_id": "platform_account.one.amazon.marketplace",
        "account_data_binding_id": "account_data_binding.one.amazon.oms",
        "source_role": "oms_sales",
        "table_id": "table.zs_observe.amazon_oms",
    }


def _binding_card() -> dict:
    return _binding_card_for("amazon")


def _binding_card_for(platform: str) -> dict:
    binding_id = f"account_data_binding.one.{platform}.oms"
    table_id = f"table.zs_observe.{platform}_oms"
    return {
        "canonical_id": binding_id,
        "card_type": "account_data_binding",
        "node_sets": [
            "domain_family:client_runtime",
            "card_type:account_data_binding",
            "tenant_id:tenant.one",
            "group_id:group.one",
            f"platform_id:platform.{platform}",
            f"platform_context_id:platform_context.{platform}.in",
            f"platform_account_id:platform_account.one.{platform}.marketplace",
            "source_role:oms_sales",
            f"table_id:{table_id}",
        ],
    }


def _returns_binding_card() -> dict:
    return {
        "canonical_id": "account_data_binding.one.amazon.returns",
        "card_type": "account_data_binding",
        "node_sets": [
            "domain_family:client_runtime",
            "card_type:account_data_binding",
            "tenant_id:tenant.one",
            "group_id:group.one",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            "platform_account_id:platform_account.one.amazon.marketplace",
            "source_role:returns",
            "table_id:table.zs_observe.amazon_returns",
        ],
    }


def _domain_card(domain: str) -> dict:
    return {
        "canonical_id": f"domain.amazon.{domain}",
        "canonical_name": f"Amazon {domain.title()}",
        "card_type": "domain",
        "node_sets": [
            "card_type:domain",
            "domain_family:marketplace",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            f"domain_id:domain.amazon.{domain}",
        ],
        "fields": {
            "included_tables": [f"table.zs_observe.amazon_{'oms' if domain == 'orders' else 'returns'}"],
        },
    }


def _table_card() -> dict:
    return {
        "canonical_id": "table.zs_observe.amazon_oms",
        "card_type": "table",
        "node_sets": [
            "card_type:table",
            "domain_family:marketplace",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            "domain_id:domain.amazon.orders",
            "source_role:oms_sales",
            "table_id:table.zs_observe.amazon_oms",
        ],
    }


def _returns_table_card() -> dict:
    return {
        "canonical_id": "table.zs_observe.amazon_returns",
        "card_type": "table",
        "node_sets": [
            "card_type:table",
            "domain_family:marketplace",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            "domain_id:domain.amazon.returns",
            "source_role:returns",
            "table_id:table.zs_observe.amazon_returns",
        ],
    }


def _query_pattern_card() -> dict:
    return {
        "canonical_id": "query_pattern.amazon_oms.top_skus",
        "card_type": "query_pattern",
        "node_sets": [
            "card_type:query_pattern",
            "table_id:table.zs_observe.amazon_oms",
        ],
    }


def _value_profile_card() -> dict:
    return {
        "canonical_id": "value_profile.amazon_oms.order_status",
        "canonical_name": "Amazon OMS Order Status",
        "card_type": "value_profile",
        "node_sets": [
            "card_type:value_profile",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            "domain_id:domain.amazon.orders",
            "table_id:table.zs_observe.amazon_oms",
            "column_id:column.zs_observe.amazon_oms.order_status",
        ],
        "fields": {
            "known_values": ["shipped", "cancelled"],
            "value_type": "status",
        },
    }


def _metric_card() -> dict:
    return {
        "canonical_id": "metric.gross_sales",
        "canonical_name": "Gross Sales",
        "card_type": "metric",
        "node_sets": [
            "card_type:metric",
            "platform_id:platform.amazon",
            "platform_context_id:platform_context.amazon.in",
            "domain_id:domain.amazon.orders",
            "metric_id:metric.gross_sales",
        ],
        "fields": {
            "business_definition": "Gross sales amount before deductions.",
        },
    }


def _column_card() -> dict:
    return {
        "canonical_id": "column.zs_observe.amazon_oms.sku_id",
        "card_type": "column",
        "node_sets": [
            "card_type:column",
            "table_id:table.zs_observe.amazon_oms",
        ],
    }


def _record_usable_amazon_branch(ledger: BranchLedger) -> list[SearchResult]:
    results: list[SearchResult] = []
    binding_contract = _runtime_binding_contract()
    ledger.record_contract_discovered(binding_contract)
    ledger.record_contract_started(binding_contract)
    binding_result = SearchResult(
        result_id="result.amazon.binding",
        contract_id=binding_contract.contract_id,
        stage=binding_contract.stage,
        returned_cards=[_binding_card()],
        validation={"ok": True},
    )
    ledger.record_result(binding_contract, binding_result)
    results.append(binding_result)

    table_contract = _table_contract("q.amazon.table")
    ledger.record_contract_discovered(table_contract)
    ledger.record_contract_started(table_contract)
    table_result = SearchResult(
        result_id="result.amazon.table",
        contract_id=table_contract.contract_id,
        stage=table_contract.stage,
        returned_cards=[_table_card()],
        validation={"ok": True},
    )
    ledger.record_result(table_contract, table_result)
    results.append(table_result)

    pattern_contract = _query_pattern_contract("q.amazon.query_pattern")
    ledger.record_contract_discovered(pattern_contract)
    ledger.record_contract_started(pattern_contract)
    pattern_result = SearchResult(
        result_id="result.amazon.query_pattern",
        contract_id=pattern_contract.contract_id,
        stage=pattern_contract.stage,
        returned_cards=[_query_pattern_card()],
        validation={"ok": True},
    )
    ledger.record_result(pattern_contract, pattern_result)
    results.append(pattern_result)
    return results


def _record_partial_flipkart_branch(ledger: BranchLedger) -> list[SearchResult]:
    contract = _scheduler_runtime_contract("q.flipkart.binding", "flipkart", "binding")
    ledger.record_contract_discovered(contract)
    ledger.record_contract_started(contract)
    result = SearchResult(
        result_id="result.flipkart.binding",
        contract_id=contract.contract_id,
        stage=contract.stage,
        returned_cards=[_binding_card_for("flipkart")],
        validation={"ok": True},
    )
    ledger.record_result(contract, result)
    return [result]


def _packed_card_ids(evidence_pack: dict) -> set[str]:
    ids: set[str] = set()
    for result in evidence_pack.get("results", []):
        for card in result.get("cards", []):
            ids.add(card["canonical_id"])
    return ids


def _finalized_table_ids(trace: list[dict]) -> list[str]:
    table_ids: list[str] = []
    for row in trace:
        if row.get("event") != "domain_tables_finalized":
            continue
        for table_id in row.get("verified_table_ids") or []:
            table_ids.append(table_id)
    return table_ids


if __name__ == "__main__":
    unittest.main()
