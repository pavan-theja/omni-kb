import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


class CogneeSearchTest(unittest.TestCase):
    def test_build_search_payload_omits_optional_fields_by_default(self):
        module = _load_search_module()

        payload = module.build_search_payload(
            query="hello",
            datasets=["zenstatement_canonical"],
            search_type="RAG_COMPLETION",
        )

        self.assertEqual(
            {
                "query": "hello",
                "datasets": ["zenstatement_canonical"],
                "search_type": "RAG_COMPLETION",
            },
            payload,
        )

    def test_build_search_payload_adds_optional_fields_when_requested(self):
        module = _load_search_module()

        payload = module.build_search_payload(
            query="hello",
            datasets=["zenstatement_canonical"],
            search_type="RAG_COMPLETION",
            top_k=3,
            only_context=True,
            verbose=True,
            system_prompt="Use context only.",
            node_names=["tenant.mensa"],
        )

        self.assertEqual(3, payload["top_k"])
        self.assertIs(True, payload["only_context"])
        self.assertIs(True, payload["verbose"])
        self.assertEqual("Use context only.", payload["system_prompt"])
        self.assertEqual(["tenant.mensa"], payload["node_name"])

    def test_selected_search_types_keeps_both_to_rag_and_graph(self):
        module = _load_search_module()

        self.assertEqual(
            ["GRAPH_COMPLETION_COT", "RAG_COMPLETION", "GRAPH_COMPLETION"],
            module.selected_search_types("GRAPH_COMPLETION_COT", include_both=True),
        )

    def test_build_result_record_keeps_raw_and_parsed_results(self):
        module = _load_search_module()

        record = module.build_result_record(
            query="hello",
            scoped_query="hello\n\nScope:\n- tenant: Mensa",
            scope={"tenant": "Mensa", "platform": None},
            datasets=["zenstatement_ca"],
            search_types=["RAG_COMPLETION"],
            search_options={"top_k": 2, "only_context": True},
            results={"RAG_COMPLETION": ["raw"]},
            parsed_results={"RAG_COMPLETION": [{"content": "parsed"}]},
        )

        self.assertEqual({"tenant": "Mensa"}, record["scope"])
        self.assertEqual(["raw"], record["results"]["RAG_COMPLETION"])
        self.assertEqual([{"content": "parsed"}], record["parsed_results"]["RAG_COMPLETION"])

    def test_write_json_creates_parent_directory(self):
        module = _load_search_module()

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "nested" / "result.json"

            module.write_json({"ok": True}, path)

            self.assertEqual({"ok": True}, json.loads(path.read_text(encoding="utf-8")))

    def test_resolve_output_path_makes_relative_paths_repo_root_relative(self):
        module = _load_search_module()

        self.assertEqual(module.REPO_ROOT / "eval_runs" / "result.json", module.resolve_output_path(Path("eval_runs/result.json")))

    def test_resolve_output_path_keeps_absolute_paths_absolute(self):
        module = _load_search_module()
        absolute_path = Path("/tmp/cognee_search_result.json")

        self.assertEqual(absolute_path, module.resolve_output_path(absolute_path))

    def test_parse_response_items_parses_every_json_string_in_list(self):
        module = _load_search_module()

        items = module.parse_response_items(
            [
                '{"selected_source":"table.one","sql_skeleton":"select 1"}',
                '{"selected_source":"table.two","sql_skeleton":"select 2"}',
            ]
        )

        self.assertEqual(
            [
                {"selected_source": "table.one", "sql_skeleton": "select 1"},
                {"selected_source": "table.two", "sql_skeleton": "select 2"},
            ],
            items,
        )

    def test_format_response_numbers_multiple_parsed_items(self):
        module = _load_search_module()

        formatted = module.format_response(
            [
                '{"selected_source":"table.one"}',
                '{"selected_source":"table.two"}',
            ]
        )

        self.assertIn("#### Response 1", formatted)
        self.assertIn("#### Response 2", formatted)
        self.assertIn('"selected_source": "table.one"', formatted)
        self.assertIn('"selected_source": "table.two"', formatted)

    def test_parse_response_items_accepts_fenced_json(self):
        module = _load_search_module()

        items = module.parse_response_items(['```json\n{"selected_source":"table.one"}\n```'])

        self.assertEqual([{"selected_source": "table.one"}], items)

    def test_parse_response_items_unwraps_cognee_content_string(self):
        module = _load_search_module()

        items = module.parse_response_items(
            [
                '{"content":"{\\"selected_source\\":\\"table.one\\",\\"sql_skeleton\\":\\"select 1\\"}"}',
            ]
        )

        self.assertEqual([{"selected_source": "table.one", "sql_skeleton": "select 1"}], items)

    def test_parse_response_items_tolerates_invalid_content_object(self):
        module = _load_search_module()

        items = module.parse_response_items(
            [
                '{"content":{"selected_source":"table.one","sql_skeleton":"select 1"}}',
            ]
        )

        self.assertEqual([{"selected_source": "table.one", "sql_skeleton": "select 1"}], items)


def _load_search_module():
    path = Path(__file__).resolve().parents[1] / "cognee" / "scripts" / "cognee_search.py"
    spec = importlib.util.spec_from_file_location("cognee_search_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
