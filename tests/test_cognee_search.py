import importlib.util
import unittest
from pathlib import Path


class CogneeSearchTest(unittest.TestCase):
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
