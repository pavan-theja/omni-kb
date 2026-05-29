import json
import unittest
from unittest.mock import patch

from zenkb import retrieval as retrieval_module
from zenkb.retrieval import build_cognee_candidate_handoff, build_sql_context_bundle, build_sql_handoff_brief


class RetrievalTest(unittest.TestCase):
    def test_semantic_parser_output_is_schema_normalized_and_scope_authoritative(self):
        semantic_response = {
            "entities": ["orders", "tenant"],
            "dimensions": ["channel"],
            "metrics": ["order_volume", "order_volume_share"],
            "ranking": ["highest"],
            "filters": {"tenant_codes": ["wrong_tenant"]},
            "output_type": ["answer_or_sql_context"],
            "requested_action": "answer",
            "evidence_requirements": ["channel column", "order identifier column"],
            "derived_metrics": [
                {
                    "name": "order_volume_share",
                    "base_metric": "order_volume",
                    "interpretation": "share of order volume by requested dimension",
                }
            ],
        }
        cards = [_card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion")]
        scope_resolution = retrieval_module._resolve_scope(
            "Which channel has the highest order volume share?",
            cards,
            scope_overrides={"tenant": "tenant.prism_fashion"},
        )

        with patch.dict(
            "os.environ",
            {
                "AZURE_API_BASE": "https://example.openai.azure.com",
                "AZURE_API_KEY": "test-key",
                "AZURE_API_VERSION": "2024-02-15-preview",
                "AZURE_OPENAI_DEPLOYMENT": "gpt-4o-mini",
            },
        ), patch("zenkb.retrieval._azure_chat_json", return_value=semantic_response):
            facets = retrieval_module._request_facets(
                "Which channel has the highest order volume share?",
                scope_resolution,
            )

        self.assertEqual(facets["parser"]["source"], "azure_openai")
        self.assertEqual(facets["dimensions"], ["channel"])
        self.assertEqual(facets["metrics"], ["order_volume", "order_volume_share"])
        self.assertEqual(facets["ranking"], ["highest"])
        self.assertIn("prism_fashion", facets["filters"]["tenant_codes"])
        self.assertNotIn("wrong_tenant", facets["filters"]["tenant_codes"])
        self.assertEqual(facets["derived_metrics"][0]["name"], "order_volume_share")

    def test_cognee_discovery_runs_separate_queries_per_requested_facet(self):
        facets = {
            "entities": ["orders", "tenant"],
            "dimensions": ["channel"],
            "metrics": ["order_volume", "order_volume_share"],
            "relationships": ["oms_to_marketplace"],
            "ranking": ["highest"],
            "filters": {"tenant_codes": ["prism_fashion"]},
            "evidence_requirements": ["channel column", "order identifier column"],
        }
        calls = []

        def fake_search(base_url, dataset, query, *, timeout):
            calls.append(query)
            return [query]

        with patch("zenkb.retrieval._cognee_search", side_effect=fake_search):
            results = retrieval_module._cognee_discovery_results(
                "http://localhost:8000",
                "zenstatement_canonical",
                "Which channel has the highest order volume share?",
                request_facets=facets,
                timeout=1.0,
            )

        discovery_facets = {
            item.get("facet")
            for item in results
            if item.get("query_type") == "canonical_candidate_discovery"
        }
        self.assertEqual(discovery_facets, {"entities", "dimensions", "metrics", "relationships", "ranking"})
        self.assertEqual(len(calls), 6)
        self.assertIn("Facet: dimensions", " ".join(calls))
        self.assertIn("Facet: metrics", " ".join(calls))

    def test_metric_query_returns_sql_context_bundle(self):
        cards = [
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE transaction_type = 'forward'",
            ),
            _card("metric.flipkart_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle("Amazon gross sales GMV SQL", cards, edges, ["metric.amazon_gross_sales_gmv"])

        card_ids = {card["canonical_id"] for card in bundle["cards"]}
        self.assertIn("metric.amazon_gross_sales_gmv", card_ids)
        self.assertIn("metric_impl.amazon_oms.gross_sales_gmv", card_ids)
        self.assertIn("table.amazon_oms", card_ids)
        self.assertNotIn("metric.flipkart_gross_sales_gmv", card_ids)
        self.assertFalse(bundle["unsafe_for_sql_generation"])
        self.assertEqual(bundle["sql_context"]["required_table_ids"], ["table.amazon_oms"])

    def test_missing_table_context_blocks_sql_generation(self):
        cards = [
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV")
        ]

        bundle = _bundle("Amazon gross sales GMV SQL", cards, [], ["metric.amazon_gross_sales_gmv"])

        self.assertTrue(bundle["unsafe_for_sql_generation"])
        codes = {warning["code"] for warning in bundle["completeness_warnings"]}
        self.assertIn("missing_metric_implementation", codes)
        self.assertIn("missing_table_context", codes)

    def test_tenant_platform_scope_selects_matching_account_binding(self):
        cards = [
            _card("tenant.nimbus_retail", "tenant", name="Nimbus Retail", tenant_name="Nimbus Retail"),
            _card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion"),
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE transaction_type = 'forward'",
            ),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
            _card(
                "account_data_binding.nimbus.amazon_in.primary.amazon_settlement",
                "account_data_binding",
                name="Amazon Settlement",
                binding_name="Amazon Settlement",
            ),
            _card(
                "account_data_binding.prism.flipkart_in.seller.flipkart_settlement",
                "account_data_binding",
                name="Flipkart Settlement",
                binding_name="Flipkart Settlement",
            ),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle("Nimbus Amazon gross sales GMV SQL", cards, edges, ["metric.amazon_gross_sales_gmv"])

        card_ids = {card["canonical_id"] for card in bundle["cards"]}
        self.assertIn("account_data_binding.nimbus.amazon_in.primary.amazon_settlement", card_ids)
        self.assertNotIn("account_data_binding.prism.flipkart_in.seller.flipkart_settlement", card_ids)
        self.assertIn("nimbus", bundle["metadata_filters"]["query_hints"]["tenant_codes"])
        self.assertIn("amazon", bundle["metadata_filters"]["query_hints"]["platform_codes"])
        filter_values = {
            (item["dimension"], item["value"])
            for item in bundle["metadata_filters"]["applied_filters"]
        }
        self.assertIn(("tenant", "nimbus_retail"), filter_values)
        self.assertIn(("platform", "amazon"), filter_values)

    def test_explicit_scope_overrides_do_not_require_query_scope_words(self):
        cards = [
            _card("tenant.nimbus_retail", "tenant", name="Nimbus Retail", tenant_name="Nimbus Retail"),
            _card("group.nimbus_india_d2c", "group", name="Nimbus India D2C", group_name="Nimbus India D2C"),
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card(
                "platform_account.nimbus.amazon_in.primary",
                "platform_account",
                name="Primary",
                account_name="Primary",
            ),
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE transaction_type = 'forward'",
            ),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
            _card(
                "account_data_binding.nimbus.amazon_in.primary.amazon_settlement",
                "account_data_binding",
                name="Amazon Settlement",
                binding_name="Amazon Settlement",
            ),
            _card(
                "account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement",
                "account_data_binding",
                name="Shiprocket Settlement",
                binding_name="Shiprocket Settlement",
            ),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle(
            "what are my gross sales",
            cards,
            edges,
            ["metric.amazon_gross_sales_gmv"],
            scope_overrides={
                "tenant": "tenant.nimbus_retail",
                "group": "group.nimbus_india_d2c",
                "platform": "platform.amazon",
                "account": "platform_account.nimbus.amazon_in.primary",
            },
        )

        card_ids = {card["canonical_id"] for card in bundle["cards"]}
        self.assertIn("account_data_binding.nimbus.amazon_in.primary.amazon_settlement", card_ids)
        self.assertNotIn("account_data_binding.nimbus.shiprocket.primary.shiprocket_settlement", card_ids)
        hints = bundle["metadata_filters"]["query_hints"]
        self.assertIn("nimbus", hints["tenant_codes"])
        self.assertIn("nimbus_india_d2c", hints["group_codes"])
        self.assertIn("amazon", hints["platform_codes"])
        self.assertIn("primary", hints["account_codes"])
        self.assertTrue(
            any(item["source"] == "explicit" for item in bundle["metadata_filters"]["applied_filters"])
        )

    def test_my_query_blocks_without_required_tenant_scope(self):
        cards = [
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE transaction_type = 'forward'",
            ),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle("what are my gross sales SQL", cards, edges, ["metric.amazon_gross_sales_gmv"])

        self.assertTrue(bundle["unsafe_for_sql_generation"])
        codes = {warning["code"] for warning in bundle["completeness_warnings"]}
        self.assertIn("missing_required_tenant_scope", codes)
        self.assertFalse(bundle["sql_handoff_contract"]["can_generate_sql"])

    def test_scoped_query_blocks_without_matching_account_binding(self):
        cards = [
            _card("tenant.nimbus_retail", "tenant", name="Nimbus Retail", tenant_name="Nimbus Retail"),
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card(
                "platform_account.nimbus.amazon_in.primary",
                "platform_account",
                name="Primary",
                account_name="Primary",
            ),
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE transaction_type = 'forward'",
            ),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle(
            "what are my gross sales from Amazon",
            cards,
            edges,
            ["metric.amazon_gross_sales_gmv"],
            scope_overrides={
                "tenant": "tenant.nimbus_retail",
                "platform": "platform.amazon",
                "account": "platform_account.nimbus.amazon_in.primary",
            },
        )

        self.assertTrue(bundle["unsafe_for_sql_generation"])
        codes = {warning["code"] for warning in bundle["completeness_warnings"]}
        self.assertIn("missing_account_data_binding", codes)

    def test_handoff_contract_exposes_metric_tables_columns_and_filters(self):
        cards = [
            _card("tenant.nimbus_retail", "tenant", name="Nimbus Retail", tenant_name="Nimbus Retail"),
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card("metric.amazon_gross_sales_gmv", "metric", name="Gross sales / GMV", metric_name="Gross sales / GMV"),
            _card(
                "metric_impl.amazon_oms.gross_sales_gmv",
                "metric_implementation",
                name="Gross sales / GMV (amazon)",
                metric_id="metric.amazon_gross_sales_gmv",
                base_tables=["table.amazon_oms"],
                formula_description="SUM(amazon_oms.charged_amount) WHERE is_active = true AND transaction_type = 'forward'",
            ),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
            _card(
                "account_data_binding.nimbus.amazon_in.primary.amazon_orders",
                "account_data_binding",
                name="Amazon Orders",
                binding_name="Amazon Orders",
            ),
        ]
        edges = [
            {
                "source_id": "metric.amazon_gross_sales_gmv",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.amazon_oms.gross_sales_gmv",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle(
            "what are my gross sales from Amazon",
            cards,
            edges,
            ["metric.amazon_gross_sales_gmv"],
            scope_overrides={"tenant": "tenant.nimbus_retail", "platform": "platform.amazon"},
        )

        self.assertFalse(bundle["unsafe_for_sql_generation"])
        dependency = bundle["sql_handoff_contract"]["metric_dependencies"][0]
        self.assertEqual(dependency["required_table_ids"], ["table.amazon_oms"])
        self.assertIn("amazon_oms.charged_amount", dependency["required_columns"])
        self.assertIn("is_active = true", dependency["required_filters"])
        self.assertIn("transaction_type = 'forward'", dependency["required_filters"])

    def test_cognee_candidate_discovery_can_add_semantic_metric_without_metric_intent(self):
        cards = [
            _card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion"),
            _card("platform.flipkart", "platform", name="Flipkart", platform_name="Flipkart"),
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card("metric.amazon_distinct_orders_units_and_line_items", "metric", name="Distinct orders, units, and line items"),
            _card(
                "metric.flipkart_distinct_orders_and_line_items",
                "metric",
                name="Distinct orders and line items",
                metric_name="Distinct orders and line items",
            ),
            _card(
                "metric_impl.flipkart_oms.distinct_orders_and_line_items",
                "metric_implementation",
                name="Distinct orders and line items (flipkart)",
                metric_id="metric.flipkart_distinct_orders_and_line_items",
                base_tables=["table.flipkart_oms"],
                formula_description="COUNT(DISTINCT order_id) AS distinct_orders FROM flipkart_oms WHERE transaction_type = 'forward'",
            ),
            _card("table.flipkart_oms", "table", name="flipkart_oms", table_name="flipkart_oms"),
        ]
        edges = [
            {
                "source_id": "metric.flipkart_distinct_orders_and_line_items",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.flipkart_oms.distinct_orders_and_line_items",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle(
            "Which channel has the highest order volume share?",
            cards,
            edges,
            [
                "metric.amazon_distinct_orders_units_and_line_items",
                "metric.flipkart_distinct_orders_and_line_items",
                "metric_impl.flipkart_oms.distinct_orders_and_line_items",
            ],
            scope_overrides={"tenant": "tenant.prism_fashion", "platform": "platform.flipkart"},
        )

        card_ids = {card["canonical_id"] for card in bundle["cards"]}
        candidate_handoff = build_cognee_candidate_handoff(bundle)
        self.assertIn("metric.flipkart_distinct_orders_and_line_items", card_ids)
        self.assertIn("metric_impl.flipkart_oms.distinct_orders_and_line_items", card_ids)
        self.assertIn("table.flipkart_oms", card_ids)
        accepted_ids = {
            item["canonical_id"]
            for item in candidate_handoff["cognee_candidates"]["accepted"]
        }
        excluded_ids = {
            item["canonical_id"]
            for item in candidate_handoff["cognee_candidates"]["excluded_by_scope"]
        }
        impl_candidate = next(
            item
            for item in candidate_handoff["cognee_candidates"]["accepted"]
            if item["canonical_id"] == "metric_impl.flipkart_oms.distinct_orders_and_line_items"
        )
        metric_candidate = next(
            item
            for item in candidate_handoff["cognee_candidates"]["accepted"]
            if item["canonical_id"] == "metric.flipkart_distinct_orders_and_line_items"
        )
        self.assertEqual(candidate_handoff["bundle_type"], "cognee_candidate_handoff")
        self.assertIn("metric.flipkart_distinct_orders_and_line_items", accepted_ids)
        self.assertIn("metric_impl.flipkart_oms.distinct_orders_and_line_items", accepted_ids)
        self.assertIn("metric.amazon_distinct_orders_units_and_line_items", excluded_ids)
        self.assertIn("table.flipkart_oms", impl_candidate["base_tables"])
        self.assertIn("transaction_type = 'forward'", impl_candidate["formula_filters"])
        self.assertIn("metric_impl.flipkart_oms.distinct_orders_and_line_items", metric_candidate["related_canonical_ids"])
        self.assertNotIn("cards", candidate_handoff)
        self.assertNotIn("edges", candidate_handoff)
        self.assertEqual(
            bundle["sql_handoff_contract"]["intent_coverage"]["facets"]["metrics"]["status"],
            "partial",
        )
        self.assertEqual(
            bundle["sql_handoff_contract"]["intent_coverage"]["facets"]["dimensions"]["status"],
            "missing",
        )

    def test_candidate_handoff_reports_unknown_canonical_mentions_as_untrusted(self):
        cards = [
            _card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion"),
            _card("table.zs_observe.myntra_oms", "table", name="myntra_oms", table_name="myntra_oms"),
        ]

        bundle = _bundle(
            "Generate a summary report of OMS systems and their connected marketplaces.",
            cards,
            [],
            ["table.zs_observe.myntra_oms", "table.myntra_table"],
            scope_overrides={"tenant": "tenant.prism_fashion"},
        )
        candidate_handoff = build_cognee_candidate_handoff(bundle)
        unknown_ids = {
            item["canonical_id"]
            for item in candidate_handoff["cognee_candidates"]["unrecognized_canonical_mentions"]
        }
        warning_codes = {warning["code"] for warning in candidate_handoff["warnings"]}

        self.assertIn("table.myntra_table", unknown_ids)
        self.assertIn("candidate_not_canonical", warning_codes)
        self.assertNotIn(
            "table.myntra_table",
            {
                item["canonical_id"]
                for item in candidate_handoff["cognee_candidates"]["accepted"]
            },
        )

    def test_exact_dimension_column_candidate_is_promoted_to_sql_context(self):
        cards = [
            _card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion"),
            _card(
                "column.zs_observe.shiprocket_oms.channel",
                "column",
                name="channel",
                column_name="channel",
                table_id="table.zs_observe.shiprocket_oms",
            ),
        ]

        bundle = _bundle(
            "Which channel has the highest order volume share?",
            cards,
            [],
            ["column.zs_observe.shiprocket_oms.channel"],
            scope_overrides={"tenant": "tenant.prism_fashion"},
        )
        column_ids = {
            item["canonical_id"]
            for item in bundle["sql_context"]["columns"]
        }
        dimension_coverage = bundle["sql_handoff_contract"]["intent_coverage"]["facets"]["dimensions"]

        self.assertIn("column.zs_observe.shiprocket_oms.channel", column_ids)
        self.assertEqual(dimension_coverage["status"], "resolved")
        self.assertIn("column.zs_observe.shiprocket_oms.channel", dimension_coverage["evidence_ids"])

    def test_cross_platform_flow_blocks_without_flow_evidence(self):
        cards = [
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card("platform.shiprocket", "platform", name="Shiprocket", platform_name="Shiprocket"),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
            _card("table.shiprocket_oms", "table", name="shiprocket_oms", table_name="shiprocket_oms"),
        ]

        bundle = _bundle(
            "Amazon Shiprocket reconciliation SQL",
            cards,
            [],
            ["table.amazon_oms", "table.shiprocket_oms"],
        )

        self.assertTrue(bundle["unsafe_for_sql_generation"])
        codes = {warning["code"] for warning in bundle["completeness_warnings"]}
        self.assertIn("missing_business_flow_binding", codes)
        flow = bundle["sql_handoff_contract"]["business_flow_coverage"]
        self.assertTrue(flow["required"])
        self.assertEqual(flow["selected_flow_evidence_ids"], [])

    def test_cross_platform_flow_passes_with_relationship_evidence(self):
        cards = [
            _card("platform.amazon", "platform", name="Amazon", platform_name="Amazon"),
            _card("platform.shiprocket", "platform", name="Shiprocket", platform_name="Shiprocket"),
            _card("table.amazon_oms", "table", name="amazon_oms", table_name="amazon_oms"),
            _card("table.shiprocket_oms", "table", name="shiprocket_oms", table_name="shiprocket_oms"),
            _card(
                "relationship.amazon_oms_to_shiprocket_oms",
                "relationship",
                name="Amazon Oms To Shiprocket Oms",
                description="Cross-domain relationship between Amazon OMS and Shiprocket OMS.",
            ),
        ]

        bundle = _bundle(
            "Amazon Shiprocket reconciliation SQL",
            cards,
            [],
            [
                "table.amazon_oms",
                "table.shiprocket_oms",
                "relationship.amazon_oms_to_shiprocket_oms",
            ],
        )

        self.assertFalse(bundle["unsafe_for_sql_generation"])
        flow = bundle["sql_handoff_contract"]["business_flow_coverage"]
        self.assertTrue(flow["required"])
        self.assertIn(
            "relationship.amazon_oms_to_shiprocket_oms",
            flow["selected_flow_evidence_ids"],
        )

    def test_reconciliation_profile_blocks_when_incomplete(self):
        cards = [
            _card(
                "reconciliation_profile.cod_reconciliation",
                "reconciliation_profile",
                name="COD Reconciliation",
                profile_name="COD Reconciliation",
            )
        ]

        bundle = _bundle(
            "Shiprocket COD settlement reconciliation profile SQL",
            cards,
            [],
            ["reconciliation_profile.cod_reconciliation"],
        )

        self.assertTrue(bundle["unsafe_for_sql_generation"])
        coverage = bundle["sql_handoff_contract"]["reconciliation_coverage"]
        self.assertTrue(coverage["required"])
        self.assertIn("sides", coverage["missing"])
        self.assertIn("units", coverage["missing"])
        self.assertIn("matching_logic", coverage["missing"])
        self.assertIn("mismatch_categories", coverage["missing"])
        codes = {warning["code"] for warning in bundle["completeness_warnings"]}
        self.assertIn("incomplete_reconciliation_profile", codes)

    def test_reconciliation_profile_passes_with_profile_evidence(self):
        cards = [
            _card(
                "reconciliation_profile.cod_reconciliation",
                "reconciliation_profile",
                name="COD Reconciliation",
                profile_name="COD Reconciliation",
                description="COD remittance reconciliation between shipment and settlement at AWB grain.",
            ),
            _card(
                "relationship.shiprocket_oms.shiprocket_settlement.awb",
                "relationship",
                name="Shiprocket OMS To Shiprocket Settlement AWB",
                description="Match shiprocket_oms.awb_code to shiprocket_settlement.awb for COD remittance.",
            ),
            _card(
                "mismatch_category.missing_cod_remittance",
                "mismatch_category",
                name="Missing COD Remittance",
                category_name="Missing COD Remittance",
            ),
            _card("table.shiprocket_oms", "table", name="shiprocket_oms", table_name="shiprocket_oms"),
            _card("table.shiprocket_settlement", "table", name="shiprocket_settlement", table_name="shiprocket_settlement"),
        ]

        bundle = _bundle(
            "Shiprocket COD settlement reconciliation profile SQL",
            cards,
            [],
            [
                "reconciliation_profile.cod_reconciliation",
                "relationship.shiprocket_oms.shiprocket_settlement.awb",
                "mismatch_category.missing_cod_remittance",
                "table.shiprocket_oms",
                "table.shiprocket_settlement",
            ],
        )

        self.assertFalse(bundle["unsafe_for_sql_generation"])
        coverage = bundle["sql_handoff_contract"]["reconciliation_coverage"]
        self.assertTrue(coverage["required"])
        self.assertEqual(coverage["missing"], [])
        self.assertIn("reconciliation_profile.cod_reconciliation", coverage["profile_ids"])
        self.assertIn("relationship.shiprocket_oms.shiprocket_settlement.awb", coverage["matching_logic_ids"])
        self.assertIn("mismatch_category.missing_cod_remittance", coverage["mismatch_category_ids"])

    def test_handoff_brief_compacts_context_for_downstream_sql_generation(self):
        cards = [
            _card("tenant.prism_fashion", "tenant", name="Prism Fashion", tenant_name="Prism Fashion"),
            _card("platform.flipkart", "platform", name="Flipkart", platform_name="Flipkart"),
            _card(
                "metric.flipkart_seller_realization_rate",
                "metric",
                name="Seller Realization Rate",
                metric_name="Seller Realization Rate",
            ),
            _card(
                "metric_impl.flipkart_settlement.seller_realization_rate",
                "metric_implementation",
                name="Seller Realization Rate (Flipkart)",
                metric_id="metric.flipkart_seller_realization_rate",
                base_tables=["table.flipkart_settlement"],
                formula_description=(
                    "SUM(net_settlement_amount) / SUM(gross_sales_amount) "
                    "WHERE transaction_type = 'forward'"
                ),
            ),
            _card(
                "account_data_binding.prism.flipkart_in.seller.flipkart_settlement",
                "account_data_binding",
                name="Flipkart Settlement",
                binding_name="Flipkart Settlement",
            ),
            _card(
                "table.flipkart_settlement",
                "table",
                name="flipkart_settlement",
                table_name="flipkart_settlement",
            ),
        ]
        edges = [
            {
                "source_id": "metric.flipkart_seller_realization_rate",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.flipkart_settlement.seller_realization_rate",
                "confidence": "inferred",
            }
        ]

        bundle = _bundle(
            "Generate a summary report of OMS systems and their connected marketplaces on seller realization rate.",
            cards,
            edges,
            ["metric.flipkart_seller_realization_rate"],
            scope_overrides={"tenant": "tenant.prism_fashion"},
        )
        brief = build_sql_handoff_brief(bundle)
        coverage = bundle["sql_handoff_contract"]["intent_coverage"]
        warning_codes = {warning["code"] for warning in bundle["completeness_warnings"]}

        self.assertEqual(brief["bundle_type"], "sql_generation_handoff_brief")
        self.assertIn("compact SQL-ready summary", brief["paraphrased_request"])
        self.assertEqual(coverage["facets"]["metrics"]["status"], "resolved")
        self.assertIn(coverage["facets"]["relationships"]["status"], {"missing", "partial"})
        self.assertIn("relationships", coverage["missing_required_facets"])
        self.assertIn("incomplete_intent_coverage", warning_codes)
        self.assertTrue(bundle["unsafe_for_sql_generation"])
        self.assertFalse(brief["safety"]["can_generate_sql"])
        self.assertIn(
            "metric_impl.flipkart_settlement.seller_realization_rate",
            {
                item["canonical_id"]
                for item in brief["canonical_inputs"]["metric_implementations"]
            },
        )
        self.assertNotIn("cards", brief)
        self.assertNotIn("edges", brief)
        self.assertNotIn("evidence_refs", str(brief))

    def test_handoff_brief_preserves_payout_ratio_sql_context_without_observed_values(self):
        cards = [
            _card("tenant.mensa", "tenant", name="Mensa", tenant_name="Mensa"),
            _card("platform.meesho", "platform", name="Meesho", platform_name="Meesho"),
            _card(
                "metric.seller_realization_rate",
                "metric",
                name="Effective payout ratio",
                canonical_name="Seller Realization Rate",
                colloquial_names=["seller realization", "payout ratio", "effective payout rate"],
            ),
            _card(
                "metric_impl.meesho.effective_payout_ratio",
                "metric_implementation",
                name="Meesho implementation - Effective Payout Ratio",
                display_name="Meesho implementation - Effective Payout Ratio",
                metric_id="metric.seller_realization_rate",
                source_tables=["zs_observe.meesho_settlement"],
                formula_text=(
                    "SELECT\n"
                    "  ROUND(100.0 * SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0), 2) "
                    "AS payout_ratio_pct\n"
                    "FROM zs_observe.meesho_settlement\n"
                    "WHERE is_active = true AND order_status = 'Delivered';\n"
                    "-- Observed: 77.4%"
                ),
            ),
            _card(
                "query_pattern.meesho.011.7_5_effective_payout_ratio",
                "query_pattern",
                name="Meesho query pattern - 7.5 Effective Payout Ratio",
                source_tables=["zs_observe.meesho_settlement"],
                sql_template=(
                    "SELECT SUM(settled_amount) / NULLIF(SUM(sale_settled_amount), 0) AS payout_ratio\n"
                    "FROM zs_observe.meesho_settlement\n"
                    "WHERE is_active = true AND order_status = 'Delivered';\n"
                    "-- Observed: 77.4%"
                ),
            ),
            _card(
                "table.zs_observe.meesho_settlement",
                "table",
                name="meesho_settlement",
                table_name="meesho_settlement",
            ),
        ]
        edges = [
            {
                "source_id": "metric.seller_realization_rate",
                "edge_type": "HAS_IMPLEMENTATION",
                "target_id": "metric_impl.meesho.effective_payout_ratio",
                "confidence": "curated",
            },
            {
                "source_id": "query_pattern.meesho.011.7_5_effective_payout_ratio",
                "edge_type": "PRODUCES_METRIC",
                "target_id": "metric.seller_realization_rate",
                "confidence": "curated",
            },
        ]

        bundle = _bundle(
            "What is my Meesho effective payout ratio and seller realization from sales and settlement?",
            cards,
            edges,
            [
                "metric_impl.meesho.effective_payout_ratio",
                "query_pattern.meesho.011.7_5_effective_payout_ratio",
            ],
            scope_overrides={"tenant": "tenant.mensa", "platform": "platform.meesho"},
        )
        brief = build_sql_handoff_brief(bundle)
        serialized_brief = json.dumps(brief, sort_keys=True)
        dependency = bundle["sql_handoff_contract"]["metric_dependencies"][0]
        impl = brief["canonical_inputs"]["metric_implementations"][0]

        self.assertIn("effective_payout_ratio", bundle["request_facets"]["metrics"])
        self.assertIn("seller_realization_rate", bundle["request_facets"]["metrics"])
        self.assertTrue(dependency["has_formula"])
        self.assertIn("table.zs_observe.meesho_settlement", dependency["required_table_ids"])
        self.assertIn("settled_amount", dependency["required_columns"])
        self.assertIn("sale_settled_amount", dependency["required_columns"])
        self.assertIn("is_active = true", dependency["required_filters"])
        self.assertIn("order_status = 'Delivered'", dependency["required_filters"])
        self.assertIn("formula_preview", impl)
        self.assertIn("sale_settled_amount", impl["formula_columns"])
        self.assertIn("order_status = 'Delivered'", impl["formula_filters"])
        self.assertNotIn("Observed", serialized_brief)
        self.assertNotIn("77.4", serialized_brief)


def _bundle(query, cards, edges, candidate_ids, **kwargs):
    with patch(
        "zenkb.retrieval._cognee_discovery_results",
        return_value=_cognee_discovery_payload(candidate_ids),
    ):
        return build_sql_context_bundle(query, cards, edges, **kwargs)


def _cognee_discovery_payload(candidate_ids):
    candidate_text = "Relevant canonical IDs: " + ", ".join(candidate_ids)
    return [
        {
            "query_type": "answer_context",
            "query": "test answer context",
            "results": ["No final answer; use canonical candidates."],
        },
        {
            "query_type": "canonical_candidate_discovery",
            "query": "test candidate discovery",
            "results": [candidate_text],
        },
    ]


def _card(canonical_id, card_type, **extra):
    card = {
        "canonical_id": canonical_id,
        "card_type": card_type,
        "name": canonical_id.split(".")[-1].replace("_", " ").title(),
        "description": "Test card.",
        "status": "draft",
        "confidence": "inferred",
        "review_status": "unreviewed",
        "source_documents": ["Source/Test.md"],
        "evidence_refs": [
            {
                "source_doc": "Source/Test.md",
                "source_span": "lines 1-2",
                "chunk_id": "chunk-1",
            }
        ],
    }
    card.update(extra)
    return card


if __name__ == "__main__":
    unittest.main()
