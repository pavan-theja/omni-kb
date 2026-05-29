import importlib.util
import unittest
from pathlib import Path


class CogneeSqlHandoffTest(unittest.TestCase):
    def test_parse_response_items_unwraps_content_string(self):
        module = _load_module()

        items = module.parse_response_items(
            ['{"content":"{\\"selected_source\\":\\"zs_observe.orders\\",\\"sql_skeleton\\":\\"SELECT * FROM zs_observe.orders\\"}"}']
        )

        self.assertEqual(
            [
                {
                    "selected_source": "zs_observe.orders",
                    "sql_skeleton": "SELECT * FROM zs_observe.orders",
                }
            ],
            items,
        )

    def test_validator_rejects_literal_metadata_sql(self):
        module = _load_module()

        validation = module.validate_handoff(
            {
                "selected_source": None,
                "require_tables": [],
                "sql_skeleton": "SELECT 'Meesho' AS channel_name",
            }
        )

        self.assertFalse(validation["ok"])
        self.assertIn("literal metadata rows", validation["errors"][0])

    def test_validator_accepts_physical_table_sql(self):
        module = _load_module()

        validation = module.validate_handoff(
            {
                "selected_source": "zs_observe.orders",
                "require_tables": [
                    {
                        "field": "zs_observe.orders",
                        "selected?": "Yes",
                    }
                ],
                "sql_skeleton": "SELECT order_id FROM zs_observe.orders",
            }
        )

        self.assertTrue(validation["ok"])
        self.assertEqual([], validation["errors"])

    def test_validator_rejects_canonical_metadata_sql(self):
        module = _load_module()

        validation = module.validate_handoff(
            {
                "selected_source": "metadata.account_data_bindings",
                "require_tables": [],
                "sql_skeleton": "SELECT * FROM metadata.account_data_bindings",
            }
        )

        self.assertFalse(validation["ok"])
        self.assertTrue(any("canonical metadata" in error for error in validation["errors"]))

    def test_validator_allows_selected_metadata_evidence_with_commented_sql(self):
        module = _load_module()

        validation = module.validate_handoff(
            {
                "answer_mode": "metadata_inventory",
                "selected_source": None,
                "require_tables": [
                    {
                        "field": "account_data_binding.mensa.amazon_in.primary.amazon_oms",
                        "selected?": "Yes",
                        "role": "Selected Metadata Evidence",
                    }
                ],
                "sql_skeleton": "-- Metadata inventory handoff; no runtime SQL table is queried.",
            }
        )

        self.assertTrue(validation["ok"])
        self.assertEqual([], validation["errors"])

    def test_parse_response_items_recovers_json_prefix(self):
        module = _load_module()

        items = module.parse_response_items(['{"selected_sources":[]} trailing prose'])

        self.assertEqual([{"selected_sources": []}], items)

    def test_run_stage_uses_configured_search_type(self):
        module = _load_module()
        client = _FakeClient()

        result = module.run_stage(
            client,
            stage="intent",
            prompt="{}",
            datasets=["zenstatement_canonical"],
            timeout=1,
            search_type="GRAPH_COMPLETION",
        )

        self.assertEqual({"ok": True}, result)
        self.assertEqual("GRAPH_COMPLETION", client.calls[0]["search_type"])

    def test_run_sql_handoff_uses_search_type_for_stages(self):
        module = _load_module()
        client = _FakeClient()

        result = module.run_sql_handoff(
            client,
            query="Which channel has the highest order volume share?",
            datasets=["zenstatement_canonical"],
            scope={"tenant": "Mensa Brands"},
            timeout=1,
            context_chars=1000,
            search_types=["GRAPH_COMPLETION"],
        )

        self.assertEqual(["GRAPH_COMPLETION"], result["search_types"])
        self.assertIn("raw_intent", result["stages"])
        self.assertIn("grounded_intent", result["stages"])
        self.assertTrue(client.calls)
        self.assertTrue(all(call["search_type"] == "GRAPH_COMPLETION" for call in client.calls))
        self.assertIn("Raw Intent JSON", client.calls[0]["query"])
        self.assertIn("metric", client.calls[0]["query"])

    def test_classify_raw_intent_identifies_metadata_inventory(self):
        module = _load_module()

        intent = module.classify_raw_intent(
            "List all marketplaces handled through Unicommerce.",
            {"tenant": "Mensa Brands"},
        )

        self.assertEqual("metadata_inventory", intent["answer_mode_hint"])
        self.assertIn("source_mapping", intent["query_families"])
        self.assertTrue(intent["must_enumerate_sources"])

    def test_ordered_search_types_keeps_primary_first_when_both(self):
        module = _load_module()

        search_types = module.ordered_search_types("GRAPH_COMPLETION", include_both=True)

        self.assertEqual(["GRAPH_COMPLETION", "RAG_COMPLETION"], search_types)

    def test_render_skill_loads_external_prompt(self):
        module = _load_module()

        prompt = module.render_skill(
            "source_resolver",
            query="List all marketplaces handled through Unicommerce",
            scope="Scope:\n- tenant: Mensa Brands",
            intent_json='{"grain":"channel"}',
            context="table.zs_observe.unicommerce",
        )

        self.assertIn("# Source Resolver Skill", prompt)
        self.assertIn("List all marketplaces handled through Unicommerce", prompt)
        self.assertIn("table.zs_observe.unicommerce", prompt)
        self.assertNotIn("{{", prompt)

    def test_discovery_skill_receives_raw_intent(self):
        module = _load_module()

        prompt = module.render_skill(
            "discovery",
            query="List all marketplaces handled through Unicommerce",
            scope="Scope:\n- tenant: Mensa Brands",
            raw_intent_json='{"answer_mode_hint":"metadata_inventory"}',
        )

        self.assertIn("Raw Intent JSON", prompt)
        self.assertIn("metadata_inventory", prompt)
        self.assertNotIn("{{", prompt)

    def test_grounded_intent_skill_receives_raw_intent_and_context(self):
        module = _load_module()

        prompt = module.render_skill(
            "grounded_intent",
            query="List all marketplaces handled through Unicommerce",
            scope="Scope:\n- tenant: Mensa Brands",
            raw_intent_json='{"answer_mode_hint":"metadata_inventory"}',
            context="account_data_binding.example",
        )

        self.assertIn("Raw Intent JSON", prompt)
        self.assertIn("Retrieved context", prompt)
        self.assertIn("account_data_binding.example", prompt)
        self.assertNotIn("{{", prompt)


class _FakeClient:
    def __init__(self):
        self.calls = []

    def search(self, query, *, datasets, search_type, timeout):
        self.calls.append(
            {
                "query": query,
                "datasets": datasets,
                "search_type": search_type,
                "timeout": timeout,
            }
        )
        return ['{"content":"{\\"ok\\":true}"}']


def _load_module():
    path = Path(__file__).resolve().parents[1] / "cognee" / "scripts" / "cognee_sql_handoff.py"
    spec = importlib.util.spec_from_file_location("cognee_sql_handoff_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
