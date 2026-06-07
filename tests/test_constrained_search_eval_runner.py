import argparse
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CONSTRAINED_SEARCH_DIR = REPO_ROOT / "cognee" / "scripts" / "constrained_search"
if str(CONSTRAINED_SEARCH_DIR) not in sys.path:
    sys.path.insert(0, str(CONSTRAINED_SEARCH_DIR))

from search_runtime.eval_runner import EVAL_QUERIES, metrics_from_record, run_eval  # noqa: E402
from search_runtime.utils import read_json  # noqa: E402


class ConstrainedSearchEvalRunnerTest(unittest.TestCase):
    def test_default_eval_query_set_matches_plan_size(self):
        self.assertEqual(24, len(EVAL_QUERIES))
        self.assertEqual("List the top 5 selling SKUs for Amazon and Flipkart", EVAL_QUERIES[0])
        self.assertEqual("Return trend across all the marketplaces.", EVAL_QUERIES[-1])

    def test_metrics_extract_trace_and_branch_fields(self):
        record = {
            "query": "Top SKUs",
            "status": "best_effort",
            "duration_seconds": 1.25,
            "result": _fake_result(),
        }

        metrics = metrics_from_record(record)

        self.assertEqual("best_effort", metrics["status"])
        self.assertEqual("best_effort", metrics["completion_policy"])
        self.assertEqual("ok", metrics["handoff_status"])
        self.assertEqual(2, metrics["llm_call_count"])
        self.assertEqual(1, metrics["cognee_recall_count"])
        self.assertEqual(1, metrics["contract_repair_count"])
        self.assertEqual(1, metrics["contract_rejection_count"])
        self.assertEqual(0, metrics["invalid_contract_executed_count"])
        self.assertEqual(["account_data_binding.one.amazon.oms"], metrics["selected_runtime_bindings"])
        self.assertEqual(["table.zs_observe.amazon_oms"], metrics["selected_tables"])
        self.assertEqual(["query_pattern.amazon_oms.top_skus"], metrics["selected_query_patterns"])
        self.assertEqual(["max_steps_exhausted_before_pending_contracts_completed"], metrics["blocked_reasons"])

    def test_run_eval_writes_phase5_artifacts(self):
        async def fake_search(args):
            print(f"running {args.query}")
            print("no stderr noise", file=sys.stderr)
            return _fake_result(query=args.query)

        with tempfile.TemporaryDirectory() as tmp:
            args = _args(Path(tmp))
            result = self.assertAsyncResult(run_eval(args, search_callable=fake_search))
            run_dir = Path(result["run_dir"])

            self.assertEqual("complete", result["status"])
            self.assertTrue((run_dir / "manifest.json").exists())
            self.assertTrue((run_dir / "aggregate_metrics.json").exists())
            self.assertTrue((run_dir / "summary.md").exists())
            query_dir = run_dir / "queries" / "001"
            for name in (
                "query.txt",
                "result.json",
                "raw_result.json",
                "trace.json",
                "stdout.log",
                "stderr.log",
                "metrics.json",
                "summary.md",
                "final_output.md",
                "sql_handoff.json",
                "sql_handoff.yaml",
                "rendered.sql",
            ):
                self.assertTrue((query_dir / name).exists(), name)

            manifest = read_json(run_dir / "manifest.json")
            aggregate = read_json(run_dir / "aggregate_metrics.json")
            metrics = read_json(query_dir / "metrics.json")
            result_json = read_json(query_dir / "result.json")
            raw_result = read_json(query_dir / "raw_result.json")
            sql_handoff = read_json(query_dir / "sql_handoff.json")
            trace = read_json(query_dir / "trace.json")
            final_output = (query_dir / "final_output.md").read_text(encoding="utf-8")
            rendered_sql = (query_dir / "rendered.sql").read_text(encoding="utf-8")

        self.assertEqual(1, manifest["completed_query_count"])
        self.assertEqual({"best_effort": 1}, aggregate["status_counts"])
        self.assertEqual([], aggregate["acceptance_failures"])
        self.assertEqual("best_effort", metrics["status"])
        self.assertIn("final_output", manifest["queries"][0])
        self.assertIn("sql_handoff", manifest["queries"][0])
        self.assertIn("rendered_sql", manifest["queries"][0])
        self.assertIn("raw_result", manifest["queries"][0])
        self.assertNotIn("result", result_json)
        self.assertEqual("raw_result.json", result_json["artifacts"]["raw_result"])
        self.assertIn("result", raw_result)
        self.assertEqual("ok", sql_handoff["handoff_status"])
        self.assertEqual(3, len(trace["trace"]))
        self.assertIn("SELECT 1", final_output)
        self.assertIn("SELECT 1", rendered_sql)

    def assertAsyncResult(self, awaitable):
        import asyncio

        return asyncio.run(awaitable)


def _args(output_dir: Path) -> argparse.Namespace:
    return argparse.Namespace(
        pack_dir=Path("build/constrained_search/build"),
        env_file=Path("cognee/.env.vertex.gemini352"),
        provider="vertex",
        tenant_id="tenant.one",
        group_id="group.one",
        dataset=None,
        all_datasets=False,
        prompted_recall=False,
        llm_callable=None,
        max_steps=30,
        branch_max_steps=8,
        max_pending=32,
        completion_policy="best_effort",
        orchestrator="serial",
        evidence_concurrency=4,
        questions=None,
        query=["List the top 5 selling SKUs for Amazon and Flipkart"],
        limit=None,
        offset=0,
        output_dir=output_dir,
        run_id="unit_run",
        overwrite=False,
        fail_fast=False,
    )


def _fake_result(query: str = "Top SKUs") -> dict:
    return {
        "status": "best_effort",
        "blocked_reason": None,
        "completion_policy": "best_effort",
        "global_step_count": 3,
        "handoff": {
            "validated_output": {
                "handoff_status": "ok",
                "source_blocks": [{"table_id": "table.zs_observe.amazon_oms"}],
                "blocked_reasons": [],
                "open_questions": [],
                "sql_blueprints": [{"draft_sql": "SELECT 1"}],
            }
        },
        "results": [{"result_id": "result.one"}],
        "trace": [
            {
                "event": "llm_anchor_decision",
                "decision": {"validated_output": {}},
            },
            {
                "event": "contract_repaired",
                "repairs": [{"repair": "missing_card_type_nodeset"}],
            },
            {
                "event": "cognee_result_validated",
                "result": {"validation": {"ok": True}},
            },
        ],
        "branches": {
            "branch.amazon": {
                "status": "usable",
                "scope": {"platform_id": "platform.amazon"},
                "account_data_binding_cards": ["account_data_binding.one.amazon.oms"],
                "table_cards": ["table.zs_observe.amazon_oms"],
                "query_pattern_cards": ["query_pattern.amazon_oms.top_skus"],
                "metric_implementation_cards": [],
                "contract_rejections": [{"rejection": "unit_rejection"}],
                "blocked_reasons": [],
            },
            "branch.flipkart": {
                "status": "partial",
                "scope": {"platform_id": "platform.flipkart"},
                "account_data_binding_cards": ["account_data_binding.one.flipkart.oms"],
                "table_cards": [],
                "query_pattern_cards": [],
                "metric_implementation_cards": [],
                "contract_rejections": [],
                "blocked_reasons": ["max_steps_exhausted_before_pending_contracts_completed"],
            },
        },
        "branch_order": ["branch.amazon", "branch.flipkart"],
        "branch_status": {"branch.amazon": "usable", "branch.flipkart": "partial"},
        "usable_branch_ids": ["branch.amazon"],
        "incomplete_branch_ids": ["branch.flipkart"],
        "usable_branch_count": 1,
        "incomplete_branch_count": 1,
        "best_effort_warnings": [
            {
                "warning": "branch_incomplete",
                "branch_id": "branch.flipkart",
                "missing_evidence": ["table_frame", "query_pattern_or_metric_implementation"],
            }
        ],
        "evidence_pack": {"query_text": query},
    }


if __name__ == "__main__":
    unittest.main()
