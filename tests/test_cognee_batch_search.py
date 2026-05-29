import importlib.util
import unittest
from pathlib import Path


class CogneeBatchSearchTest(unittest.TestCase):
    def test_render_question_markdown_includes_timing(self):
        module = _load_batch_module()
        record = {
            "question_index": 1,
            "question": "Which channel has the highest order volume share?",
            "scoped_query": "Which channel has the highest order volume share?",
            "results": {},
            "errors": {},
            "timing": {
                "started_at": "2026-05-27T00:00:00+00:00",
                "duration_seconds": 12.345,
                "search_seconds": {"RAG_COMPLETION": 12.0},
            },
        }

        markdown = module.render_question_markdown(record, _SearchModule())

        self.assertIn("### Timing", markdown)
        self.assertIn("- duration_seconds: `12.345`", markdown)
        self.assertIn("- RAG_COMPLETION_seconds: `12.0`", markdown)


class _SearchModule:
    @staticmethod
    def format_response(response):
        return str(response)


def _load_batch_module():
    path = Path(__file__).resolve().parents[1] / "build" / "cognee_batch_search.py"
    spec = importlib.util.spec_from_file_location("cognee_batch_search_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
