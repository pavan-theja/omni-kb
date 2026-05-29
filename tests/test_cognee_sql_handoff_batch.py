import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


class CogneeSqlHandoffBatchTest(unittest.TestCase):
    def test_run_question_records_success_and_validation(self):
        module = _load_batch_module()
        handoff = _FakeHandoff()

        record = module.run_question(
            handoff,
            object(),
            question_index=1,
            question="Which channel has the highest order volume share?",
            datasets=["zenstatement_canonical"],
            scope={"tenant": "Mensa Brands"},
            search_types=["GRAPH_COMPLETION"],
            timeout=1,
            context_chars=1000,
        )

        self.assertIsNone(record["error"])
        self.assertEqual(True, module.validation_ok(record))
        self.assertEqual("Which channel has the highest order volume share?", handoff.calls[0]["query"])
        self.assertEqual(["GRAPH_COMPLETION"], handoff.calls[0]["search_types"])
        self.assertEqual({"tenant": "Mensa Brands"}, record["scope"])

    def test_render_question_markdown_records_error(self):
        module = _load_batch_module()
        record = {
            "question_index": 2,
            "question": "Broken?",
            "started_at": "2026-05-27T00:00:00+00:00",
            "timing": {"duration_seconds": 1.2},
            "error": "boom",
            "result": None,
        }

        markdown = module.render_question_markdown(record, _FakeHandoff())

        self.assertIn("## 002. Broken?", markdown)
        self.assertIn("### Error", markdown)
        self.assertIn("boom", markdown)

    def test_load_questions_supports_json_list(self):
        module = _load_batch_module()
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "questions.json"
            path.write_text(json.dumps([{"question": "One?"}, "Two?"]), encoding="utf-8")

            questions = module.load_questions(path)

        self.assertEqual(["One?", "Two?"], questions)


class _FakeHandoff:
    DEFAULT_BASE_URL = "http://localhost:8000"
    DEFAULT_DATASET = "zenstatement_canonical"
    DEFAULT_TIMEOUT_SECONDS = 300.0

    def __init__(self):
        self.calls = []

    def run_sql_handoff(self, client, *, query, datasets, scope, search_types, timeout, context_chars):
        self.calls.append(
            {
                "query": query,
                "datasets": datasets,
                "scope": scope,
                "search_types": search_types,
                "timeout": timeout,
                "context_chars": context_chars,
            }
        )
        return {
            "query": query,
            "validation": {"ok": True, "errors": [], "warnings": []},
            "stages": {"sql_handoff": {"sql_skeleton": "SELECT 1 FROM zs_observe.orders"}},
            "timing": {"duration_seconds": None},
        }

    @staticmethod
    def render_markdown(result):
        return "# Result\n\n" + result["query"]


def _load_batch_module():
    path = Path(__file__).resolve().parents[1] / "build" / "cognee_sql_handoff_batch.py"
    spec = importlib.util.spec_from_file_location("cognee_sql_handoff_batch_for_test", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    unittest.main()
