#!/usr/bin/env python3
"""Run a list of scoped Cognee searches and save the results."""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
SEARCH_SCRIPT = REPO_ROOT / "cognee" / "scripts" / "cognee_search.py"

# Optional inline questions for quick local runs. If --questions is provided,
# the file wins; otherwise this list is used.
QUESTIONS: list[str] = [
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
    "Return trend across all the marketplaces."
]



def main(argv: Optional[Sequence[str]] = None) -> int:
    search = _load_search_module()

    parser = argparse.ArgumentParser(description="Run batch Cognee searches from a question list.")
    parser.add_argument(
        "--questions",
        type=Path,
        help="txt/json/jsonl file with questions. Omit to use QUESTIONS in this script.",
    )
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory where results should be written.")
    parser.add_argument("--base-url", default=search.DEFAULT_BASE_URL)
    parser.add_argument("--dataset", action="append", help="Dataset name. Repeat for multiple datasets.")
    parser.add_argument("--search-type", choices=search.SEARCH_TYPES, default="RAG_COMPLETION")
    parser.add_argument("--both", action="store_true", help="Run both RAG_COMPLETION and GRAPH_COMPLETION.")
    parser.add_argument("--top-k", type=int, help="Maximum number of Cognee results/context items to request.")
    parser.add_argument(
        "--only-context",
        action="store_true",
        help="Ask Cognee to return retrieved context instead of calling the LLM for completion searches.",
    )
    parser.add_argument("--verbose", action="store_true", help="Ask Cognee for verbose search output.")
    parser.add_argument("--system-prompt", help="Optional Cognee system prompt for completion searches.")
    parser.add_argument("--node-name", action="append", help="Restrict search to a Cognee node set. Repeat for many.")
    parser.add_argument("--timeout", type=float, default=search.DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--tenant")
    parser.add_argument("--group")
    parser.add_argument("--platform")
    parser.add_argument("--account")
    parser.add_argument("--business-domain")
    parser.add_argument("--workflow")
    parser.add_argument("--table")
    parser.add_argument("--metric")
    parser.add_argument("--no-sql-context", action="store_true")
    parser.add_argument("--fail-fast", action="store_true", help="Stop on the first failed question.")
    args = parser.parse_args(argv)

    questions = load_questions(args.questions) if args.questions else [question.strip() for question in QUESTIONS if question.strip()]
    if not questions:
        raise SystemExit("No questions found. Pass --questions or edit QUESTIONS in this script.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    datasets = args.dataset or [search.DEFAULT_DATASET]
    search_types = search.selected_search_types(args.search_type, include_both=args.both)
    search_options = {
        "top_k": args.top_k,
        "only_context": args.only_context,
        "verbose": args.verbose,
        "system_prompt": args.system_prompt,
        "node_names": args.node_name or [],
    }
    scope = {
        "tenant": args.tenant,
        "group": args.group,
        "platform": args.platform,
        "account": args.account,
        "business_domain": args.business_domain,
        "workflow": args.workflow,
        "table": args.table,
        "metric": args.metric,
    }

    client = search.CogneeClient(args.base_url)
    run_started_at = datetime.now(timezone.utc).replace(microsecond=0)
    run_started = time.perf_counter()
    index_records = []
    all_markdown = [
        "# Cognee Batch Search Results",
        "",
        f"- started_at: `{run_started_at.isoformat()}`",
        f"- source_questions: `{args.questions or 'inline QUESTIONS'}`",
        f"- datasets: `{', '.join(datasets)}`",
        f"- search_types: `{', '.join(search_types)}`",
        "",
    ]

    for question_index, question in enumerate(questions, start=1):
        question_started = time.perf_counter()
        question_started_at = datetime.now(timezone.utc).replace(microsecond=0)
        slug = _slugify(question)[:64] or f"question_{question_index:03d}"
        stem = f"{question_index:03d}_{slug}"
        scoped_query = search.build_scoped_query(
            question,
            scope,
            include_sql_context=not args.no_sql_context,
        )
        print(f"[{question_index}/{len(questions)}] {question}", flush=True)

        result_record = {
            "question_index": question_index,
            "question": question,
            "scoped_query": scoped_query,
            "datasets": datasets,
            "search_types": search_types,
            "search_options": search_options,
            "results": {},
            "parsed_results": {},
            "errors": {},
            "timing": {
                "started_at": question_started_at.isoformat(),
                "duration_seconds": None,
                "search_seconds": {},
            },
        }
        for search_type in search_types:
            search_started = time.perf_counter()
            try:
                response = search.search_cognee(
                    client,
                    query=scoped_query,
                    datasets=datasets,
                    search_type=search_type,
                    timeout=args.timeout,
                    top_k=args.top_k,
                    only_context=args.only_context,
                    verbose=args.verbose,
                    system_prompt=args.system_prompt,
                    node_names=args.node_name,
                )
                result_record["results"][search_type] = response
                result_record["parsed_results"][search_type] = search.parse_response_items(response)
            except Exception as exc:  # Keep batch runs inspectable even if one query fails.
                result_record["errors"][search_type] = str(exc)
                if args.fail_fast:
                    raise
            finally:
                result_record["timing"]["search_seconds"][search_type] = _elapsed_seconds(search_started)

        result_record["timing"]["duration_seconds"] = _elapsed_seconds(question_started)

        json_path = args.output_dir / f"{stem}.json"
        md_path = args.output_dir / f"{stem}.md"
        write_json(result_record, json_path)
        md_text = render_question_markdown(result_record, search)
        md_path.write_text(md_text, encoding="utf-8")

        index_records.append(
            {
                "question_index": question_index,
                "question": question,
                "json": json_path.name,
                "markdown": md_path.name,
                "duration_seconds": result_record["timing"]["duration_seconds"],
                "search_seconds": result_record["timing"]["search_seconds"],
                "errors": result_record["errors"],
            }
        )
        all_markdown.append(md_text)
        all_markdown.append("\n---\n")

    run_completed_at = datetime.now(timezone.utc).replace(microsecond=0)
    total_duration_seconds = _elapsed_seconds(run_started)
    all_markdown[3:3] = [
        f"- completed_at: `{run_completed_at.isoformat()}`",
        f"- duration_seconds: `{total_duration_seconds}`",
    ]
    write_json(
        {
            "started_at": run_started_at.isoformat(),
            "completed_at": run_completed_at.isoformat(),
            "duration_seconds": total_duration_seconds,
            "questions": str(args.questions) if args.questions else "inline QUESTIONS",
            "datasets": datasets,
            "search_types": search_types,
            "count": len(index_records),
            "results": index_records,
        },
        args.output_dir / "index.json",
    )
    (args.output_dir / "all_results.md").write_text("\n".join(all_markdown), encoding="utf-8")
    print(f"Saved {len(index_records)} result(s) under {args.output_dir}", flush=True)
    return 0


def load_questions(path: Path) -> list[str]:
    if not path.exists():
        raise RuntimeError(f"Missing questions file: {path}")
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        payload = json.loads(text)
        if isinstance(payload, list):
            return [_question_from_item(item) for item in payload if _question_from_item(item)]
        if isinstance(payload, Mapping):
            items = payload.get("questions", [])
            if isinstance(items, list):
                return [_question_from_item(item) for item in items if _question_from_item(item)]
            question = _question_from_item(payload)
            return [question] if question else []
        if isinstance(payload, str):
            return [payload.strip()] if payload.strip() else []
        return []
    if suffix == ".jsonl":
        questions = []
        for line in text.splitlines():
            if not line.strip():
                continue
            question = _question_from_item(json.loads(line))
            if question:
                questions.append(question)
        return questions
    return [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    ]


def _question_from_item(item: object) -> str:
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, Mapping):
        for key in ("question", "query", "text"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def render_question_markdown(record: Mapping[str, object], search_module: object) -> str:
    lines = [
        f"## {record['question_index']:03d}. {record['question']}",
        "",
        "### Timing",
        "",
        *_timing_markdown_lines(record.get("timing", {})),
        "",
        "### Query",
        "",
        "```text",
        str(record["scoped_query"]),
        "```",
        "",
    ]
    results = record.get("results", {})
    if isinstance(results, Mapping):
        for search_type, response in results.items():
            lines.extend(
                [
                    f"### {search_type}",
                    "",
                    search_module.format_response(response),
                    "",
                ]
            )
    errors = record.get("errors", {})
    if errors:
        lines.extend(["### Errors", "", "```json", json.dumps(errors, indent=2, sort_keys=True), "```", ""])
    return "\n".join(lines)


def write_json(value: object, path: Path) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "question"


def _elapsed_seconds(started: float) -> float:
    return round(time.perf_counter() - started, 3)


def _timing_markdown_lines(timing: object) -> list[str]:
    if not isinstance(timing, Mapping):
        return ["- duration_seconds: `unknown`"]
    lines = []
    started_at = timing.get("started_at")
    duration = timing.get("duration_seconds")
    if started_at:
        lines.append(f"- started_at: `{started_at}`")
    lines.append(f"- duration_seconds: `{duration if duration is not None else 'unknown'}`")
    search_seconds = timing.get("search_seconds")
    if isinstance(search_seconds, Mapping):
        for search_type, seconds in search_seconds.items():
            lines.append(f"- {search_type}_seconds: `{seconds}`")
    return lines


def _load_search_module():
    spec = importlib.util.spec_from_file_location("cognee_search_helper", SEARCH_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {SEARCH_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    raise SystemExit(main())
