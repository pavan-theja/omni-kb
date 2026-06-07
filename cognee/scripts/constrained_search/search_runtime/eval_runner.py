from __future__ import annotations

import argparse
import asyncio
import contextlib
import io
import json
import re
import time
from collections.abc import Awaitable, Callable, Mapping, Sequence
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from runtime_env import PROVIDER_CHOICES, REPO_ROOT

from .search_state_machine import COMPLETION_POLICIES
from .search_trace import (
    DEFAULT_ENV_FILE,
    DEFAULT_GROUP_ID,
    DEFAULT_PACK_DIR,
    DEFAULT_TENANT_ID,
    run as run_search_trace,
)
from .utils import write_json


DEFAULT_OUTPUT_DIR = REPO_ROOT / "eval_runs" / "constrained_search"
SUCCESS_STATUSES = {"complete", "best_effort", "partial", "blocked"}
LLM_CALL_EVENTS = {
    "llm_anchor_decision",
    "llm_runtime_binding_decision",
    "llm_runtime_binding_decision_failed",
    "llm_next_nodeset_decision",
    "llm_next_nodeset_decision_failed",
    "llm_bounded_rank_decision",
    "llm_bounded_rank_decision_failed",
    "llm_evidence_profile_decision",
    "llm_evidence_profile_selection_failed",
}

EVAL_QUERIES = [
    "List the top 5 selling SKUs for Amazon and Flipkart",
    "What is the difference between Amazon and Flipkart sales metrics and settlement amounts?",
    "Which channel has the highest order volume share?",
    "Generate a report of all channels using Manual CSV integration.",
    "List all marketplaces handled through Unicommerce.",
    "Generate a courier-wise channel mapping report.",
    "Which courier handles the own website shipments?",
    "Generate a report showing COD remittance type by courier.",
    "Which channels use marketplace-managed returns?",
    "Generate a summary report of OMS systems and their connected marketplaces.",
    "Calculate the combined marketplace contribution vs own website contribution.",
    "Identify channels with higher operational dependency on manual processes.",
    "Create a marketplace risk report showing which channels depend on the same OMS.",
    "Generate a logistics dependency matrix showing courier concentration across marketplaces.",
    "Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.",
    "Compare return handling models between own website and marketplace channels.",
    "Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.",
    "Create a sales concentration analysis report to determine dependency on top 2 marketplaces.",
    "Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.",
    "Design a profitability analysis report estimating operational complexity cost per marketplace.",
    "Build a SKU profitability report.",
    "Build an Average order value report per channel.",
    "Gross sales trend across all marketplaces.",
    "Return trend across all the marketplaces.",
]

SearchCallable = Callable[[argparse.Namespace], Awaitable[dict[str, Any]]]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        result = asyncio.run(run_eval(args))
    except (RuntimeError, ValueError) as exc:
        print(f"constrained search eval failed: {exc}")
        return 1

    print(result["status"])
    print(result["run_dir"])
    return 0 if result["status"] in {"complete", "complete_with_failures"} else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run live constrained-search E2E evals and persist artifacts.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--tenant-id", default=DEFAULT_TENANT_ID)
    parser.add_argument("--group-id", default=DEFAULT_GROUP_ID)
    parser.add_argument("--dataset", action="append", help="Dataset to search. Defaults to datasets from the pack.")
    parser.add_argument("--all-datasets", action="store_true", help="Disable add-batch dataset routing.")
    parser.add_argument(
        "--prompted-recall",
        action="store_true",
        help="Experimental: run search_trace with prompted constrained Cognee recall.",
    )
    parser.add_argument("--llm-callable", help="Dotted path for a JSON LLM callable.")
    parser.add_argument("--max-steps", type=int, default=30)
    parser.add_argument("--branch-max-steps", type=int, default=8)
    parser.add_argument("--max-pending", type=int, default=32)
    parser.add_argument("--completion-policy", choices=sorted(COMPLETION_POLICIES), default="best_effort")
    parser.add_argument("--orchestrator", choices=("serial", "adk"), default="serial")
    parser.add_argument("--evidence-concurrency", type=int, default=4)
    parser.add_argument("--questions", type=Path, help="txt/json/jsonl file with eval questions.")
    parser.add_argument("--query", action="append", help="Run one query. Repeat for several. Overrides the default query set.")
    parser.add_argument("--limit", type=int, help="Run only the first N selected questions.")
    parser.add_argument("--offset", type=int, default=0, help="Skip the first N selected questions.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--run-id", help="Optional run directory name. Defaults to UTC timestamp.")
    parser.add_argument("--overwrite", action="store_true", help="Allow replacing an existing run directory.")
    parser.add_argument("--fail-fast", action="store_true", help="Stop after the first runtime exception.")
    return parser


async def run_eval(args: argparse.Namespace, search_callable: SearchCallable | None = None) -> dict[str, Any]:
    validate_args(args)
    queries = selected_queries(args)
    if not queries:
        raise ValueError("No eval queries selected.")

    started_at = utc_now()
    started = time.perf_counter()
    run_id = args.run_id or started_at.strftime("%Y%m%dT%H%M%SZ")
    run_dir = resolve_output_dir(args.output_dir) / run_id
    if run_dir.exists() and not args.overwrite:
        raise RuntimeError(f"Eval run directory already exists: {run_dir}. Pass --overwrite or choose --run-id.")
    run_dir.mkdir(parents=True, exist_ok=True)
    queries_dir = run_dir / "queries"
    queries_dir.mkdir(parents=True, exist_ok=True)

    manifest = build_manifest(args, run_id, started_at, queries)
    write_json(run_dir / "manifest.json", manifest)

    query_records: list[dict[str, Any]] = []
    aggregate_inputs: list[dict[str, Any]] = []
    runner = search_callable or run_search_trace
    for index, query in enumerate(queries, start=1):
        query_dir = queries_dir / f"{index:03d}"
        print(f"[{index}/{len(queries)}] {query}", flush=True)
        record = await run_one_query(args, runner, index, query, query_dir)
        query_records.append(query_index_record(record, query_dir, run_dir))
        aggregate_inputs.append(record)
        if record.get("error") and args.fail_fast:
            break

    completed_at = utc_now()
    aggregate = aggregate_metrics(aggregate_inputs, started_at, completed_at, elapsed_seconds(started))
    manifest["completed_at"] = completed_at.isoformat()
    manifest["duration_seconds"] = aggregate["duration_seconds"]
    manifest["completed_query_count"] = len(query_records)
    manifest["queries"] = query_records
    write_json(run_dir / "manifest.json", manifest)
    write_json(run_dir / "aggregate_metrics.json", aggregate)
    (run_dir / "summary.md").write_text(render_run_summary(manifest, aggregate), encoding="utf-8")

    return {
        "status": "complete_with_failures" if aggregate["acceptance_failures"] else "complete",
        "run_dir": str(run_dir),
        "manifest": str(run_dir / "manifest.json"),
        "aggregate_metrics": str(run_dir / "aggregate_metrics.json"),
        "summary": str(run_dir / "summary.md"),
    }


async def run_one_query(
    args: argparse.Namespace,
    search_callable: SearchCallable,
    index: int,
    query: str,
    query_dir: Path,
) -> dict[str, Any]:
    query_dir.mkdir(parents=True, exist_ok=True)
    started_at = utc_now()
    started = time.perf_counter()
    stdout = io.StringIO()
    stderr = io.StringIO()
    result: dict[str, Any] | None = None
    error: str | None = None

    search_args = search_args_for_query(args, query)
    with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
        try:
            result = await search_callable(search_args)
        except Exception as exc:  # Keep eval runs inspectable even when one query fails.
            error = repr(exc)

    completed_at = utc_now()
    duration = elapsed_seconds(started)
    record = {
        "query_index": index,
        "query": query,
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": duration,
        "status": result.get("status") if isinstance(result, dict) else "error",
        "error": error,
        "result": result,
    }
    metrics = metrics_from_record(record)
    acceptance_failures = acceptance_failures_for_record(record, metrics)
    metrics["acceptance_failures"] = acceptance_failures
    record["metrics"] = metrics

    write_query_artifacts(query_dir, query, record, result, metrics, stdout.getvalue(), stderr.getvalue())
    return record


def write_query_artifacts(
    query_dir: Path,
    query: str,
    record: dict[str, Any],
    result: dict[str, Any] | None,
    metrics: dict[str, Any],
    stdout: str,
    stderr: str,
) -> None:
    handoff_payload = sql_handoff_payload(result)
    rendered_sql = render_sql_from_handoff(handoff_payload)
    slim_record = slim_result_record(record, metrics)

    (query_dir / "query.txt").write_text(query + "\n", encoding="utf-8")
    (query_dir / "stdout.log").write_text(stdout, encoding="utf-8")
    (query_dir / "stderr.log").write_text(stderr, encoding="utf-8")
    write_json(query_dir / "result.json", slim_record)
    write_json(query_dir / "raw_result.json", record)
    write_json(query_dir / "trace.json", {"trace": result.get("trace", [])} if isinstance(result, dict) else {"trace": [], "error": record.get("error")})
    write_json(query_dir / "metrics.json", metrics)
    write_json(query_dir / "sql_handoff.json", handoff_payload)
    (query_dir / "sql_handoff.yaml").write_text(to_yaml(handoff_payload), encoding="utf-8")
    (query_dir / "rendered.sql").write_text(rendered_sql, encoding="utf-8")
    (query_dir / "final_output.md").write_text(render_final_output(record, metrics, handoff_payload, rendered_sql), encoding="utf-8")
    (query_dir / "summary.md").write_text(render_query_summary(record, metrics), encoding="utf-8")


def slim_result_record(record: Mapping[str, Any], metrics: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "query_index": record.get("query_index"),
        "query": record.get("query"),
        "started_at": record.get("started_at"),
        "completed_at": record.get("completed_at"),
        "duration_seconds": record.get("duration_seconds"),
        "status": record.get("status"),
        "error": record.get("error"),
        "metrics": dict(metrics),
        "artifacts": {
            "final_output": "final_output.md",
            "sql_handoff_json": "sql_handoff.json",
            "sql_handoff_yaml": "sql_handoff.yaml",
            "rendered_sql": "rendered.sql",
            "metrics": "metrics.json",
            "summary": "summary.md",
            "trace": "trace.json",
            "raw_result": "raw_result.json",
            "stdout": "stdout.log",
            "stderr": "stderr.log",
        },
    }


def sql_handoff_payload(result: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {
            "type": "sql_handoff",
            "handoff_status": "missing",
            "source_blocks": [],
            "sql_blueprints": [],
            "blocked_reasons": ["search_result_missing"],
            "open_questions": [],
        }

    handoff = result.get("handoff")
    if not isinstance(handoff, Mapping):
        return {
            "type": "sql_handoff",
            "handoff_status": "missing",
            "source_blocks": [],
            "sql_blueprints": [],
            "blocked_reasons": ["sql_handoff_missing"],
            "open_questions": [],
        }

    validated = handoff.get("validated_output")
    payload = dict(validated) if isinstance(validated, Mapping) else dict(handoff)
    payload.pop("input_payload", None)
    payload.setdefault("type", "sql_handoff")
    payload.setdefault("handoff_status", handoff_status(handoff))
    payload.setdefault("readiness", payload.get("handoff_status"))
    payload.setdefault("semantic_intent", {})
    payload.setdefault("bindings", {})
    payload.setdefault("resolved_columns", [])
    payload.setdefault("sql_ast", {})
    payload.setdefault("rendered_sql", "")
    payload.setdefault("source_blocks", [])
    payload.setdefault("required_runtime_filters", [])
    payload.setdefault("sql_blueprints", [])
    payload.setdefault("blocked_reasons", [])
    payload.setdefault("open_questions", [])
    return payload


def metrics_from_record(record: Mapping[str, Any]) -> dict[str, Any]:
    result = record.get("result") if isinstance(record.get("result"), Mapping) else {}
    trace = result.get("trace", []) if isinstance(result, Mapping) and isinstance(result.get("trace"), list) else []
    branches = result.get("branches", {}) if isinstance(result, Mapping) and isinstance(result.get("branches"), Mapping) else {}
    usable_branch_ids = result.get("usable_branch_ids", []) if isinstance(result, Mapping) and isinstance(result.get("usable_branch_ids"), list) else []
    handoff = result.get("handoff") if isinstance(result, Mapping) else None

    return {
        "query": record.get("query"),
        "status": record.get("status"),
        "completion_policy": result.get("completion_policy") if isinstance(result, Mapping) else None,
        "orchestrator": result.get("orchestrator", "serial") if isinstance(result, Mapping) else "serial",
        "evidence_concurrency": result.get("evidence_concurrency") if isinstance(result, Mapping) else None,
        "handoff_status": handoff_status(handoff),
        "total_latency_seconds": record.get("duration_seconds"),
        "search_total_latency_seconds": result.get("total_latency_seconds") if isinstance(result, Mapping) else None,
        "slowest_phases": slowest_phases(result.get("phase_timings", []) if isinstance(result, Mapping) else []),
        "llm_call_count": llm_call_count(trace, handoff),
        "cognee_recall_count": cognee_recall_count(result, trace),
        "adk_sequential_tool_count": event_count(trace, "adk_sequential_tool_completed"),
        "adk_parallel_evidence_run_count": event_count(trace, "adk_parallel_evidence_completed"),
        "adk_parallel_tool_count": event_count(trace, "adk_parallel_tool_completed"),
        "adk_parallel_evidence_contract_count": adk_parallel_evidence_contract_count(trace),
        "adk_parallel_evidence_failure_count": adk_parallel_evidence_failure_count(trace),
        "contract_repair_count": contract_repair_count(trace),
        "contract_rejection_count": contract_rejection_count(result, trace),
        "invalid_contract_executed_count": invalid_contract_executed_count(trace),
        "global_step_count": result.get("global_step_count") or result.get("steps_executed") if isinstance(result, Mapping) else None,
        "usable_branch_count": result.get("usable_branch_count") if isinstance(result, Mapping) else 0,
        "incomplete_branch_count": result.get("incomplete_branch_count") if isinstance(result, Mapping) else 0,
        "selected_runtime_bindings": selected_branch_cards(branches, "account_data_binding_cards", usable_branch_ids),
        "selected_tables": selected_branch_cards(branches, "table_cards", usable_branch_ids),
        "selected_query_patterns": selected_branch_cards(branches, "query_pattern_cards", usable_branch_ids),
        "selected_metric_implementations": selected_branch_cards(branches, "metric_implementation_cards", usable_branch_ids),
        "warnings": result.get("best_effort_warnings", []) if isinstance(result, Mapping) else [],
        "blocked_reasons": blocked_reasons(result, branches),
    }


def slowest_phases(phase_timings: Sequence[Any], limit: int = 8) -> list[dict[str, Any]]:
    rows = [dict(row) for row in phase_timings if isinstance(row, Mapping)]
    rows.sort(key=lambda row: float(row.get("latency_seconds") or 0), reverse=True)
    return [
        {
            "phase": row.get("phase"),
            "status": row.get("status"),
            "latency_seconds": row.get("latency_seconds"),
            "contract_id": row.get("contract_id"),
            "stage": row.get("stage"),
        }
        for row in rows[:limit]
    ]


def aggregate_metrics(records: Sequence[Mapping[str, Any]], started_at: datetime, completed_at: datetime, duration: float) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    acceptance_failures: list[dict[str, Any]] = []
    metrics = []
    for record in records:
        query_metrics = record.get("metrics", {})
        status = str(query_metrics.get("status") or "unknown")
        status_counts[status] = status_counts.get(status, 0) + 1
        metrics.append(query_metrics)
        failures = query_metrics.get("acceptance_failures") or []
        if failures:
            acceptance_failures.append(
                {
                    "query_index": record.get("query_index"),
                    "query": record.get("query"),
                    "failures": failures,
                }
            )
    return {
        "started_at": started_at.isoformat(),
        "completed_at": completed_at.isoformat(),
        "duration_seconds": duration,
        "query_count": len(records),
        "status_counts": status_counts,
        "acceptance_failures": acceptance_failures,
        "metrics": metrics,
    }


def acceptance_failures_for_record(record: Mapping[str, Any], metrics: Mapping[str, Any]) -> list[str]:
    failures: list[str] = []
    result = record.get("result") if isinstance(record.get("result"), Mapping) else None
    if record.get("error"):
        failures.append("runtime_crashed")
    if not result:
        failures.append("result_artifact_missing")
        return failures
    if not isinstance(result.get("trace"), list):
        failures.append("trace_missing")
    if metrics.get("invalid_contract_executed_count"):
        failures.append("invalid_contract_executed")
    if metrics.get("incomplete_branch_count") and not metrics.get("warnings"):
        failures.append("incomplete_branches_without_warnings")
    if metrics.get("status") == "blocked" and not metrics.get("blocked_reasons") and not metrics.get("warnings"):
        failures.append("blocked_without_actionable_missing_evidence")
    return failures


def search_args_for_query(args: argparse.Namespace, query: str) -> argparse.Namespace:
    return argparse.Namespace(
        pack_dir=args.pack_dir,
        env_file=args.env_file,
        provider=args.provider,
        query=query,
        tenant_id=args.tenant_id,
        group_id=args.group_id,
        dataset=args.dataset,
        all_datasets=args.all_datasets,
        prompted_recall=args.prompted_recall,
        llm_callable=args.llm_callable,
        max_steps=args.max_steps,
        branch_max_steps=args.branch_max_steps,
        max_pending=args.max_pending,
        completion_policy=args.completion_policy,
        orchestrator=args.orchestrator,
        evidence_concurrency=args.evidence_concurrency,
        dry_run=False,
        llm_dry_run=False,
    )


def selected_queries(args: argparse.Namespace) -> list[str]:
    if args.query:
        queries = [query.strip() for query in args.query if query.strip()]
    elif args.questions:
        queries = load_questions(args.questions)
    else:
        queries = list(EVAL_QUERIES)
    offset = max(args.offset or 0, 0)
    if offset:
        queries = queries[offset:]
    if args.limit is not None:
        queries = queries[: args.limit]
    return queries


def load_questions(path: Path) -> list[str]:
    if not path.exists():
        raise RuntimeError(f"Missing questions file: {path}")
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(text)
        if isinstance(payload, list):
            return [question for item in payload if (question := question_from_item(item))]
        if isinstance(payload, Mapping):
            items = payload.get("questions")
            if isinstance(items, list):
                return [question for item in items if (question := question_from_item(item))]
            question = question_from_item(payload)
            return [question] if question else []
        question = question_from_item(payload)
        return [question] if question else []
    if suffix == ".jsonl":
        questions: list[str] = []
        for line in text.splitlines():
            if line.strip():
                question = question_from_item(json.loads(line))
                if question:
                    questions.append(question)
        return questions
    return [line.strip() for line in text.splitlines() if line.strip() and not line.lstrip().startswith("#")]


def question_from_item(item: object) -> str:
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, Mapping):
        for key in ("question", "query", "text"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def build_manifest(args: argparse.Namespace, run_id: str, started_at: datetime, queries: Sequence[str]) -> dict[str, Any]:
    return {
        "run_id": run_id,
        "started_at": started_at.isoformat(),
        "completed_at": None,
        "duration_seconds": None,
        "pack_dir": str(args.pack_dir),
        "env_file": str(args.env_file),
        "provider": args.provider,
        "tenant_id": args.tenant_id,
        "group_id": args.group_id,
        "datasets": args.dataset or [],
        "all_datasets": args.all_datasets,
        "prompted_recall": args.prompted_recall,
        "max_steps": args.max_steps,
        "branch_max_steps": args.branch_max_steps,
        "max_pending": args.max_pending,
        "completion_policy": args.completion_policy,
        "orchestrator": args.orchestrator,
        "evidence_concurrency": args.evidence_concurrency,
        "query_count": len(queries),
        "completed_query_count": 0,
        "questions_source": str(args.questions) if args.questions else ("--query" if args.query else "default EVAL_QUERIES"),
        "queries": [],
    }


def query_index_record(record: Mapping[str, Any], query_dir: Path, run_dir: Path) -> dict[str, Any]:
    metrics = record.get("metrics", {})
    return {
        "query_index": record.get("query_index"),
        "query": record.get("query"),
        "status": metrics.get("status"),
        "duration_seconds": metrics.get("total_latency_seconds"),
        "acceptance_failures": metrics.get("acceptance_failures", []),
        "result": relative_path(query_dir / "result.json", run_dir),
        "final_output": relative_path(query_dir / "final_output.md", run_dir),
        "sql_handoff": relative_path(query_dir / "sql_handoff.yaml", run_dir),
        "rendered_sql": relative_path(query_dir / "rendered.sql", run_dir),
        "trace": relative_path(query_dir / "trace.json", run_dir),
        "raw_result": relative_path(query_dir / "raw_result.json", run_dir),
        "metrics": relative_path(query_dir / "metrics.json", run_dir),
        "summary": relative_path(query_dir / "summary.md", run_dir),
        "stdout": relative_path(query_dir / "stdout.log", run_dir),
        "stderr": relative_path(query_dir / "stderr.log", run_dir),
    }


def render_query_summary(record: Mapping[str, Any], metrics: Mapping[str, Any]) -> str:
    lines = [
        f"# Query {int(record['query_index']):03d}",
        "",
        f"Query: `{record['query']}`",
        "",
        "## Outcome",
        "",
        f"- status: `{metrics.get('status')}`",
        f"- completion_policy: `{metrics.get('completion_policy')}`",
        f"- orchestrator: `{metrics.get('orchestrator')}`",
        f"- handoff_status: `{metrics.get('handoff_status')}`",
        f"- total_latency_seconds: `{metrics.get('total_latency_seconds')}`",
        f"- global_step_count: `{metrics.get('global_step_count')}`",
        f"- usable_branch_count: `{metrics.get('usable_branch_count')}`",
        f"- incomplete_branch_count: `{metrics.get('incomplete_branch_count')}`",
        "",
        "## Evidence",
        "",
        f"- runtime_bindings: `{', '.join(metrics.get('selected_runtime_bindings') or []) or 'none'}`",
        f"- tables: `{', '.join(metrics.get('selected_tables') or []) or 'none'}`",
        f"- query_patterns: `{', '.join(metrics.get('selected_query_patterns') or []) or 'none'}`",
        f"- metric_implementations: `{', '.join(metrics.get('selected_metric_implementations') or []) or 'none'}`",
        "",
        "## Health",
        "",
        f"- llm_call_count: `{metrics.get('llm_call_count')}`",
        f"- cognee_recall_count: `{metrics.get('cognee_recall_count')}`",
        f"- adk_sequential_tool_count: `{metrics.get('adk_sequential_tool_count')}`",
        f"- adk_parallel_evidence_run_count: `{metrics.get('adk_parallel_evidence_run_count')}`",
        f"- adk_parallel_tool_count: `{metrics.get('adk_parallel_tool_count')}`",
        f"- adk_parallel_evidence_contract_count: `{metrics.get('adk_parallel_evidence_contract_count')}`",
        f"- adk_parallel_evidence_failure_count: `{metrics.get('adk_parallel_evidence_failure_count')}`",
        f"- contract_repair_count: `{metrics.get('contract_repair_count')}`",
        f"- contract_rejection_count: `{metrics.get('contract_rejection_count')}`",
        f"- invalid_contract_executed_count: `{metrics.get('invalid_contract_executed_count')}`",
        f"- acceptance_failures: `{', '.join(metrics.get('acceptance_failures') or []) or 'none'}`",
        "",
        "## Artifacts",
        "",
        "- final_output: `final_output.md`",
        "- sql_handoff: `sql_handoff.yaml`",
        "- rendered_sql: `rendered.sql`",
        "- slim_result: `result.json`",
        "- debug_trace: `trace.json`",
        "- raw_result: `raw_result.json`",
        "",
    ]
    blocked = metrics.get("blocked_reasons") or []
    if blocked:
        lines.extend(["## Blocked Reasons", "", *[f"- `{reason}`" for reason in blocked], ""])
    warnings = metrics.get("warnings") or []
    if warnings:
        lines.extend(["## Warnings", "", "```json", json.dumps(warnings, indent=2, ensure_ascii=False), "```", ""])
    return "\n".join(lines)


def render_final_output(
    record: Mapping[str, Any],
    metrics: Mapping[str, Any],
    handoff: Mapping[str, Any],
    rendered_sql: str,
) -> str:
    lines = [
        f"# Query {int(record['query_index']):03d} Final Output",
        "",
        f"Query: {record.get('query')}",
        "",
        "## Outcome",
        "",
        f"- status: `{metrics.get('status')}`",
        f"- handoff_status: `{handoff.get('handoff_status')}`",
        f"- readiness: `{handoff.get('readiness') or handoff.get('handoff_status')}`",
        f"- latency_seconds: `{metrics.get('total_latency_seconds')}`",
        "",
    ]
    semantic_intent = handoff.get("semantic_intent")
    if semantic_intent:
        lines.extend(["## Semantic Intent", "", "```json", json.dumps(semantic_intent, indent=2, ensure_ascii=False), "```", ""])
    bindings = handoff.get("bindings")
    if bindings:
        lines.extend(["## Bindings", "", "```json", json.dumps(bindings, indent=2, ensure_ascii=False), "```", ""])
    resolved_columns = handoff.get("resolved_columns") or []
    if resolved_columns:
        lines.extend(["## Resolved Columns", "", "```json", json.dumps(resolved_columns, indent=2, ensure_ascii=False), "```", ""])
    source_blocks = handoff.get("source_blocks") or []
    lines.extend(["## Resolved Sources", ""])
    if source_blocks:
        for index, source in enumerate(source_blocks, start=1):
            lines.append(f"### Source {index}")
            lines.append("")
            lines.extend(render_source_block_lines(source))
            lines.append("")
    else:
        lines.extend(["- none", ""])
    filters = handoff.get("required_runtime_filters") or []
    if filters:
        lines.extend(["## Runtime Filters", "", "```json", json.dumps(filters, indent=2, ensure_ascii=False), "```", ""])
    blocked = handoff.get("blocked_reasons") or []
    if blocked:
        lines.extend(["## Blocked Reasons", "", *[f"- {reason}" for reason in blocked], ""])
    questions = handoff.get("open_questions") or []
    if questions:
        lines.extend(["## Open Questions", "", *[f"- {question}" for question in questions], ""])
    blueprints = handoff.get("sql_blueprints") or []
    lines.extend(["## SQL Blueprints", ""])
    if blueprints:
        for index, blueprint in enumerate(blueprints, start=1):
            lines.append(f"### Blueprint {index}")
            lines.append("")
            lines.extend(render_sql_blueprint_lines(blueprint))
            lines.append("")
    else:
        lines.extend(["- none", ""])
    sql_ast = handoff.get("sql_ast") or {}
    if sql_ast:
        lines.extend(["## SQL AST", "", "```json", json.dumps(sql_ast, indent=2, ensure_ascii=False), "```", ""])
    lines.extend(["## Rendered SQL", "", "```sql", rendered_sql.strip(), "```", ""])
    return "\n".join(lines)


def render_source_block_lines(source: Any) -> list[str]:
    if isinstance(source, str):
        return [f"- source: `{source}`"]
    if not isinstance(source, Mapping):
        return ["```json", json.dumps(source, indent=2, ensure_ascii=False), "```"]
    preferred = [
        "platform_id",
        "platform_account_id",
        "account_data_binding_id",
        "table_id",
        "source_role",
        "role",
        "purpose",
        "evidence_summary",
    ]
    lines = []
    rendered_keys: set[str] = set()
    for key in preferred:
        if key in source:
            lines.append(f"- {key}: `{source[key]}`")
            rendered_keys.add(key)
    remainder = {key: value for key, value in source.items() if key not in rendered_keys}
    if remainder:
        lines.extend(["", "```json", json.dumps(remainder, indent=2, ensure_ascii=False), "```"])
    return lines


def render_sql_blueprint_lines(blueprint: Any) -> list[str]:
    if isinstance(blueprint, str):
        return ["```sql", blueprint, "```"]
    if not isinstance(blueprint, Mapping):
        return ["```json", json.dumps(blueprint, indent=2, ensure_ascii=False), "```"]
    lines: list[str] = []
    for key in ("intent", "description", "purpose", "table_id", "readiness"):
        if blueprint.get(key):
            lines.append(f"- {key}: `{blueprint[key]}`")
    sql = sql_text_from_blueprint(blueprint)
    if sql:
        lines.extend(["", "```sql", sql, "```"])
    extra = {
        key: value
        for key, value in blueprint.items()
        if key not in {"draft_sql", "rendered_sql", "sql", "conceptual_logic", "intent", "description", "purpose", "table_id", "readiness"}
    }
    if extra:
        lines.extend(["", "```json", json.dumps(extra, indent=2, ensure_ascii=False), "```"])
    return lines or ["- empty"]


def render_sql_from_handoff(handoff: Mapping[str, Any]) -> str:
    lines: list[str] = [
        f"-- handoff_status: {handoff.get('handoff_status', 'unknown')}",
    ]
    blocked = handoff.get("blocked_reasons") or []
    for reason in blocked:
        lines.append(f"-- blocked_reason: {reason}")
    questions = handoff.get("open_questions") or []
    for question in questions:
        lines.append(f"-- open_question: {question}")

    rendered_sql = handoff.get("rendered_sql")
    if isinstance(rendered_sql, str) and rendered_sql.strip():
        lines.extend(["", rendered_sql.strip().rstrip(";") + ";"])
        return "\n".join(lines) + "\n"

    blueprints = handoff.get("sql_blueprints") or []
    sql_count = 0
    for index, blueprint in enumerate(blueprints, start=1):
        sql = sql_text_from_blueprint(blueprint)
        if not sql:
            continue
        sql_count += 1
        lines.extend(["", f"-- blueprint {index}", sql.rstrip().rstrip(";") + ";"])

    if sql_count == 0:
        lines.extend(["", "-- No rendered SQL was produced by this handoff."])
    return "\n".join(lines) + "\n"


def sql_text_from_blueprint(blueprint: Any) -> str:
    if isinstance(blueprint, str):
        return blueprint.strip()
    if not isinstance(blueprint, Mapping):
        return ""
    for key in ("rendered_sql", "draft_sql", "sql"):
        value = blueprint.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
    value = blueprint.get("conceptual_logic")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return ""


def to_yaml(value: Any, *, indent: int = 0) -> str:
    rendered = yaml_lines(value, indent)
    return "\n".join(rendered) + "\n"


def yaml_lines(value: Any, indent: int = 0) -> list[str]:
    prefix = " " * indent
    if isinstance(value, Mapping):
        if not value:
            return [prefix + "{}"]
        lines: list[str] = []
        for key, item in value.items():
            key_text = str(key)
            if isinstance(item, (Mapping, list)):
                lines.append(f"{prefix}{key_text}:")
                lines.extend(yaml_lines(item, indent + 2))
            elif isinstance(item, str) and "\n" in item:
                lines.append(f"{prefix}{key_text}: |")
                lines.extend(f"{' ' * (indent + 2)}{line}" for line in item.splitlines())
            else:
                lines.append(f"{prefix}{key_text}: {yaml_scalar(item)}")
        return lines
    if isinstance(value, list):
        if not value:
            return [prefix + "[]"]
        lines = []
        for item in value:
            if isinstance(item, Mapping):
                lines.append(prefix + "-")
                lines.extend(yaml_lines(item, indent + 2))
            elif isinstance(item, list):
                lines.append(prefix + "-")
                lines.extend(yaml_lines(item, indent + 2))
            elif isinstance(item, str) and "\n" in item:
                lines.append(prefix + "- |")
                lines.extend(f"{' ' * (indent + 2)}{line}" for line in item.splitlines())
            else:
                lines.append(f"{prefix}- {yaml_scalar(item)}")
        return lines
    return [prefix + yaml_scalar(value)]


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if text == "":
        return '""'
    if re.search(r"[\s:#,\[\]{}]|^(true|false|null|yes|no|on|off)$", text, re.IGNORECASE):
        return json.dumps(text, ensure_ascii=False)
    return text


def render_run_summary(manifest: Mapping[str, Any], aggregate: Mapping[str, Any]) -> str:
    lines = [
        "# Constrained Search E2E Eval Summary",
        "",
        f"- run_id: `{manifest.get('run_id')}`",
        f"- started_at: `{aggregate.get('started_at')}`",
        f"- completed_at: `{aggregate.get('completed_at')}`",
        f"- duration_seconds: `{aggregate.get('duration_seconds')}`",
        f"- query_count: `{aggregate.get('query_count')}`",
        f"- completion_policy: `{manifest.get('completion_policy')}`",
        f"- orchestrator: `{manifest.get('orchestrator', 'serial')}`",
        f"- evidence_concurrency: `{manifest.get('evidence_concurrency', 4)}`",
        "",
        "## Status Counts",
        "",
    ]
    status_counts = aggregate.get("status_counts") or {}
    if status_counts:
        lines.extend(f"- {status}: `{count}`" for status, count in sorted(status_counts.items()))
    else:
        lines.append("- none")
    failures = aggregate.get("acceptance_failures") or []
    lines.extend(["", "## Acceptance Failures", ""])
    if not failures:
        lines.append("- none")
    else:
        for failure in failures:
            lines.append(f"- {failure.get('query_index'):03d}: `{', '.join(failure.get('failures') or [])}` - {failure.get('query')}")
    lines.extend(["", "## Queries", ""])
    for row in manifest.get("queries", []):
        lines.append(
            f"- {int(row['query_index']):03d}. `{row.get('status')}` "
            f"({row.get('duration_seconds')}s): {row.get('query')}"
        )
    return "\n".join(lines) + "\n"


def handoff_status(handoff: Any) -> str:
    if isinstance(handoff, Mapping):
        validated = handoff.get("validated_output")
        if isinstance(validated, Mapping) and validated.get("handoff_status"):
            return str(validated["handoff_status"])
        if handoff.get("handoff_status"):
            return str(handoff["handoff_status"])
        if handoff.get("status"):
            return str(handoff["status"])
        if handoff.get("error"):
            return "error"
        return "present"
    if handoff:
        return "present"
    return "missing"


def llm_call_count(trace: Sequence[Mapping[str, Any]], handoff: Any) -> int:
    count = sum(1 for event in trace if event.get("event") in LLM_CALL_EVENTS)
    if isinstance(handoff, Mapping) and handoff and handoff.get("status") != "skipped":
        count += 1
    return count


def cognee_recall_count(result: Mapping[str, Any], trace: Sequence[Mapping[str, Any]]) -> int:
    if isinstance(result.get("results"), list):
        return len(result["results"])
    return sum(1 for event in trace if event.get("event") == "cognee_result_validated")


def contract_repair_count(trace: Sequence[Mapping[str, Any]]) -> int:
    total = 0
    for event in trace:
        if event.get("event") == "contract_repaired":
            repairs = event.get("repairs")
            total += len(repairs) if isinstance(repairs, list) else 1
    return total


def contract_rejection_count(result: Mapping[str, Any], trace: Sequence[Mapping[str, Any]]) -> int:
    total = sum(1 for event in trace if event.get("event") in {"contract_repair_rejected", "llm_contract_candidate_rejected"})
    branches = result.get("branches", {}) if isinstance(result.get("branches"), Mapping) else {}
    for branch in branches.values():
        if isinstance(branch, Mapping):
            total += len(branch.get("contract_rejections") or [])
    return total


def invalid_contract_executed_count(trace: Sequence[Mapping[str, Any]]) -> int:
    invalid = 0
    for event in trace:
        if event.get("event") not in {"contract_validated", "cognee_result_validated"}:
            continue
        validation = event.get("validation")
        if validation is None and isinstance(event.get("result"), Mapping):
            validation = event["result"].get("validation")
        if isinstance(validation, Mapping) and validation.get("ok") is False:
            invalid += 1
    return invalid


def event_count(trace: Sequence[Mapping[str, Any]], event_name: str) -> int:
    return sum(1 for event in trace if event.get("event") == event_name)


def adk_parallel_evidence_contract_count(trace: Sequence[Mapping[str, Any]]) -> int:
    total = 0
    for event in trace:
        if event.get("event") != "adk_parallel_evidence_completed":
            continue
        contract_ids = event.get("contract_ids")
        if isinstance(contract_ids, list):
            total += len(contract_ids)
    return total


def adk_parallel_evidence_failure_count(trace: Sequence[Mapping[str, Any]]) -> int:
    total = 0
    for event in trace:
        if event.get("event") != "adk_parallel_evidence_completed":
            continue
        failures = event.get("failures")
        if isinstance(failures, list):
            total += len(failures)
    return total


def selected_branch_cards(branches: Mapping[str, Any], field_name: str, branch_ids: Sequence[str] | None = None) -> list[str]:
    selected: list[str] = []
    branch_values = [branches[branch_id] for branch_id in branch_ids if branch_id in branches] if branch_ids else branches.values()
    for branch in branch_values:
        if not isinstance(branch, Mapping):
            continue
        for card_id in branch.get(field_name) or []:
            if card_id and card_id not in selected:
                selected.append(str(card_id))
    return selected


def blocked_reasons(result: Any, branches: Mapping[str, Any]) -> list[str]:
    reasons: list[str] = []
    if isinstance(result, Mapping) and result.get("blocked_reason"):
        reasons.append(str(result["blocked_reason"]))
    for branch in branches.values():
        if isinstance(branch, Mapping):
            for reason in branch.get("blocked_reasons") or []:
                if reason and reason not in reasons:
                    reasons.append(str(reason))
    return reasons


def validate_args(args: argparse.Namespace) -> None:
    if args.max_steps < 1:
        raise ValueError("--max-steps must be >= 1")
    if args.branch_max_steps < 1:
        raise ValueError("--branch-max-steps must be >= 1")
    if args.max_pending < 1:
        raise ValueError("--max-pending must be >= 1")
    if args.evidence_concurrency < 1:
        raise ValueError("--evidence-concurrency must be >= 1")
    if args.limit is not None and args.limit < 1:
        raise ValueError("--limit must be >= 1")
    if args.offset < 0:
        raise ValueError("--offset must be >= 0")


def resolve_output_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def relative_path(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def utc_now() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def elapsed_seconds(start: float) -> float:
    return round(time.perf_counter() - start, 3)


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.lower()).strip("_")
    return slug or "query"
