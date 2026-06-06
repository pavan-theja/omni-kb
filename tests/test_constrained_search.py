import unittest

from cognee.constrained_search.candidate_arbitrator import arbitrate_candidates
from cognee.constrained_search.evidence_merger import merge_evidence
from cognee.constrained_search.intent_router import route_intent
from cognee.constrained_search.models import EvidenceItem, RequestEnvelope, SearchAgentResult, SearchAgentSpec
from cognee.constrained_search.orchestrator import run_constrained_search
from cognee.constrained_search.prompt_loader import render_skill
from cognee.constrained_search.search_agent import run_search_agent
from cognee.constrained_search.search_fanout import build_search_fanout
from cognee.constrained_search.staged_planner import build_staged_search_fanout


SETTLEMENT_QUERY = (
    "Generate a report identifying channels that may face reconciliation delays "
    "due to marketplace-based settlements."
)


class ConstrainedSearchTest(unittest.TestCase):
    def test_intent_route_marks_settlement_as_primary(self):
        route = route_intent(RequestEnvelope(query=SETTLEMENT_QUERY))

        self.assertIn("settlement", route.primary_domains)
        self.assertIn("marketplace_reconciliation", route.primary_domains)
        self.assertIn("settlement_ledger", route.table_families)
        self.assertEqual("last_resort_only", route.proxy_policy["broad_order_proxy"])

    def test_fanout_has_domain_and_table_family_agents(self):
        request = RequestEnvelope(query=SETTLEMENT_QUERY)
        route = route_intent(request)
        fanout = build_search_fanout(route, request_id=request.request_id)

        agent_ids = {agent.agent_id for agent in fanout.agents}
        self.assertEqual("scope.marketplace_coverage", fanout.agents[0].agent_id)
        self.assertIn("domain.settlement", agent_ids)
        self.assertIn("domain.marketplace_reconciliation", agent_ids)
        self.assertIn("domain.settlement_normalization", agent_ids)
        self.assertIn("table_family.settlement_ledger", agent_ids)
        self.assertIn("table_family.order_ledger", agent_ids)

    def test_fanout_includes_tenant_marketplace_scope_queries(self):
        request = RequestEnvelope(query=SETTLEMENT_QUERY, explicit_scope={"tenant": "Mensa Brands"})
        route = route_intent(request)
        fanout = build_search_fanout(route, request_id=request.request_id)

        scope_agent = fanout.agents[0]
        self.assertEqual("scope.marketplace_coverage", scope_agent.agent_id)
        self.assertEqual("scope_coverage_agent", scope_agent.skill_name)
        self.assertIn("Mensa Brands", " ".join(scope_agent.search_queries))
        self.assertIn("account_data_binding", " ".join(scope_agent.search_queries))

    def test_logistics_query_uses_logistics_coverage_not_marketplace_coverage(self):
        request = RequestEnvelope(
            query="For Mensa Brands, compare courier freight and shipment delays by AWB.",
            explicit_scope={"tenant": "Mensa Brands"},
        )
        route = route_intent(request)
        fanout = build_search_fanout(route, request_id=request.request_id)

        agent_ids = {agent.agent_id for agent in fanout.agents}
        self.assertIn("scope.logistics_coverage", agent_ids)
        self.assertNotIn("scope.marketplace_coverage", agent_ids)
        logistics_agent = next(agent for agent in fanout.agents if agent.agent_id == "scope.logistics_coverage")
        query_text = " ".join(logistics_agent.search_queries).lower()
        self.assertIn("courier", query_text)
        self.assertIn("awb", query_text)
        self.assertIn("shipment", query_text)

    def test_merger_downgrades_broad_proxy_when_settlement_exists(self):
        route = route_intent(RequestEnvelope(query=SETTLEMENT_QUERY))
        settlement = EvidenceItem(
            id="column.zs_observe.meesho_settlement.payment_date",
            evidence_type="field",
            evidence_family="primary",
            why="settlement timing field",
            source_agent="table_family.settlement_ledger",
        )
        proxy = EvidenceItem(
            id="table.zs_observe.increff_sales",
            evidence_type="table",
            evidence_family="supporting",
            why="broad order table with channel fields",
            source_agent="table_family.order_ledger",
        )
        merge = merge_evidence(
            route,
            [
                SearchAgentResult("table_family.settlement_ledger", "table_family", "completed", accepted=[settlement]),
                SearchAgentResult("table_family.order_ledger", "table_family", "completed", accepted=[proxy]),
            ],
        )

        self.assertEqual([proxy], list(merge.downgraded))
        arbitration = arbitrate_candidates(route, merge)
        self.assertIn(settlement, arbitration.primary_candidates)
        self.assertIn(proxy, arbitration.rejected_proxies)
        self.assertEqual("multi_section_report_plan", arbitration.status)

    def test_merger_does_not_add_union_block_when_normalization_evidence_exists(self):
        route = route_intent(RequestEnvelope(query=SETTLEMENT_QUERY))
        settlement = EvidenceItem(
            id="column.zs_observe.meesho_settlement.payment_date",
            evidence_type="field",
            evidence_family="primary",
            why="settlement timing field",
            source_agent="table_family.settlement_ledger",
        )
        normalization = EvidenceItem(
            id="output_contract.marketplace.normalized_settlement_delay_report",
            evidence_type="rule",
            evidence_family="supporting",
            why="Defines normalized settlement schema mapping, deduplication, and source precedence.",
            source_agent="domain.settlement_normalization",
        )

        merge = merge_evidence(
            route,
            [
                SearchAgentResult("table_family.settlement_ledger", "table_family", "completed", accepted=[settlement]),
                SearchAgentResult("domain.settlement_normalization", "domain", "completed", accepted=[normalization]),
            ],
        )

        self.assertNotIn("cross-marketplace schema mapping must be grounded before global SQL union", merge.unresolved)
        self.assertNotIn("deduplication/source precedence must be grounded before global SQL union", merge.unresolved)

    def test_skill_prompt_is_loaded_from_constrained_search_folder(self):
        prompt = render_skill(
            "table_search_agent",
            {
                "user_query": SETTLEMENT_QUERY,
                "agent_id": "table_family.settlement_ledger",
                "mission": "Find settlement evidence.",
                "search_query": "settlement payment_date",
                "scope": "none",
                "evidence_family": "primary",
            },
        )

        self.assertIn("# Table-Family Search Agent", prompt)
        self.assertIn("settlement payment_date", prompt)
        self.assertNotIn("{{", prompt)

    def test_orchestrator_runs_with_fake_cognee_client(self):
        result = run_constrained_search(
            SETTLEMENT_QUERY,
            client=_FakeCogneeClient(),
            search_type="RAG_COMPLETION",
            timeout=1,
        )

        self.assertEqual("multi_section_report_plan", result.sql_packet.status)
        self.assertTrue(result.validation.ok)
        downgraded_ids = {item.id for item in result.evidence_merge.downgraded}
        self.assertIn("table.zs_observe.increff_sales", downgraded_ids)
        primary_ids = {item.id for item in result.arbitration.primary_candidates}
        self.assertIn("column.zs_observe.meesho_settlement.payment_date", primary_ids)

    def test_staged_planner_profiles_selected_tables_without_cartesian_relationships(self):
        route = route_intent(RequestEnvelope(query=SETTLEMENT_QUERY))
        settlement_items = [
            EvidenceItem(
                id=f"table.zs_observe.marketplace_{index}_settlement",
                evidence_type="table",
                evidence_family="primary",
                why="marketplace settlement table",
                source_agent="table_family.settlement_ledger",
            )
            for index in range(5)
        ]
        support_items = [
            EvidenceItem(
                id=f"table.zs_observe.order_support_{index}",
                evidence_type="table",
                evidence_family="supporting",
                why="order/channel support table",
                source_agent="table_family.order_ledger",
            )
            for index in range(10)
        ]
        merge = merge_evidence(
            route,
            [
                SearchAgentResult(
                    "table_family.settlement_ledger",
                    "table_family",
                    "completed",
                    accepted=settlement_items,
                ),
                SearchAgentResult(
                    "table_family.order_ledger",
                    "table_family",
                    "completed",
                    accepted=support_items,
                ),
            ],
        )

        staged = build_staged_search_fanout(route, merge, request_id="req_test")

        agent_types = [agent.agent_type for agent in staged.agents]
        self.assertEqual(15, agent_types.count("table_profile"))
        self.assertLessEqual(agent_types.count("relationship"), 10)
        self.assertEqual(1, agent_types.count("normalization"))

    def test_max_agents_caps_total_discovery_and_staged_agents(self):
        result = run_constrained_search(
            SETTLEMENT_QUERY,
            client=_FakeCogneeClient(),
            search_type="RAG_COMPLETION",
            timeout=1,
            max_agents=1,
        )

        self.assertEqual(1, len(result.agent_results))
        self.assertEqual(1, len(result.fanout_plan.agents))
        self.assertEqual(0, len(result.staged_fanout_plan.agents))

    def test_search_agent_extracts_legacy_sql_handoff_shape(self):
        spec = SearchAgentSpec(
            agent_id="domain.marketplace_reconciliation",
            agent_type="domain",
            mission="Find settlement evidence.",
            search_queries=["settlement delay"],
            skill_name="domain_search_agent",
            top_k=10,
            evidence_family="primary",
            primary=True,
        )

        result = run_search_agent(spec, RequestEnvelope(query=SETTLEMENT_QUERY), _LegacyShapeCogneeClient())

        accepted_ids = {item.id for item in result.accepted}
        rejected_ids = {item.id for item in result.rejected}
        self.assertIn("table.zs_observe.meesho_settlement", accepted_ids)
        self.assertIn("column.zs_observe.meesho_settlement.payment_date", accepted_ids)
        self.assertIn("table.zs_observe.ajio_settlement", accepted_ids)
        self.assertIn("table.zs_observe.increff_sales", rejected_ids)


class _FakeCogneeClient:
    def post_json(self, path_or_url, payload, *, timeout):
        query = payload["query"].lower()
        if "settlement" in query and "order/channel" not in query:
            return [
                {
                    "content": (
                        '{"accepted":['
                        '{"id":"column.zs_observe.meesho_settlement.payment_date",'
                        '"evidence_type":"field","evidence_family":"primary",'
                        '"table":"zs_observe.meesho_settlement","field":"payment_date",'
                        '"why":"settlement timing field"},'
                        '{"id":"column.zs_observe.ajio_settlement.payment_status",'
                        '"evidence_type":"field","evidence_family":"primary",'
                        '"table":"zs_observe.ajio_settlement","field":"payment_status",'
                        '"why":"payment status supports overdue classification"}'
                        '],"rejected":[],"ambiguous":[],"missing":[]}'
                    )
                }
            ]
        return [
            {
                "content": (
                    '{"accepted":['
                    '{"id":"table.zs_observe.increff_sales",'
                    '"evidence_type":"table","evidence_family":"supporting",'
                    '"table":"zs_observe.increff_sales",'
                    '"why":"broad order table with channel fields"}'
                    '],"rejected":[],"ambiguous":[],"missing":[]}'
                )
            }
        ]


class _LegacyShapeCogneeClient:
    def post_json(self, path_or_url, payload, *, timeout):
        return [
            {
                "content": (
                    '{"selected_source":"zs_observe.meesho_settlement",'
                    '"require_tables":['
                    '{"field":"zs_observe.meesho_settlement","role":"Primary Source",'
                    '"selected?":"Yes","reason":"Grounded physical settlement table for Meesho."},'
                    '{"field":"zs_observe.ajio_settlement","role":"Risky Candidate",'
                    '"selected?":"No","reason":"Grounded physical settlement table for Ajio with payment_status."},'
                    '{"field":"zs_observe.increff_sales","role":"Irrelevant Candidate",'
                    '"selected?":"No","reason":"Operational warehouse sales table, not settlement-authoritative."}'
                    '],'
                    '"required_fields":['
                    '{"field":"payment_date","table":"zs_observe.meesho_settlement","role":"Date Field",'
                    '"selected?":"Yes","reason":"Date payment was credited."}'
                    ']}'
                )
            }
        ]


if __name__ == "__main__":
    unittest.main()
