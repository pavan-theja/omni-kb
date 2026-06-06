#!/usr/bin/env python3
"""Run staged Cognee SQL handoff for a list of questions and save results."""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
HANDOFF_SCRIPT = REPO_ROOT / "cognee" / "scripts" / "cognee_sql_handoff.py"

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
    "Return trend across all the marketplaces.",
]


def main(argv: Optional[Sequence[str]] = None) -> int:
    handoff = _load_handoff_module()

    parser = argparse.ArgumentParser(description="Run staged Cognee SQL handoff over a question list.")
    parser.add_argument(
        "--questions",
        type=Path,
        help="txt/json/jsonl file with questions. Omit to use QUESTIONS in this script.",
    )
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory where results should be written.")
    parser.add_argument("--base-url", default=handoff.DEFAULT_BASE_URL)
    parser.add_argument("--dataset", action="append", help="Cognee dataset name. Repeat for multiple datasets.")
    parser.add_argument("--search-type", choices=handoff.SEARCH_TYPES, default="RAG_COMPLETION")
    parser.add_argument("--both", action="store_true", help="Use both RAG_COMPLETION and GRAPH_COMPLETION for discovery.")
    parser.add_argument("--timeout", type=float, default=handoff.DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--tenant")
    parser.add_argument("--group")
    parser.add_argument("--platform")
    parser.add_argument("--account")
    parser.add_argument("--context-chars", type=int, default=32000)
    parser.add_argument("--fail-fast", action="store_true", help="Stop on the first failed question.")
    args = parser.parse_args(argv)

    questions = load_questions(args.questions) if args.questions else [question.strip() for question in QUESTIONS if question.strip()]
    if not questions:
        raise SystemExit("No questions found. Pass --questions or edit QUESTIONS in this script.")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    datasets = args.dataset or [handoff.DEFAULT_DATASET]
    search_types = handoff.ordered_search_types(args.search_type, include_both=args.both)
    scope = {
        "tenant": args.tenant,
        "group": args.group,
        "platform": args.platform,
        "account": args.account,
    }
    client = handoff.CogneeHttpClient(args.base_url)

    run_started_at = datetime.now(timezone.utc).replace(microsecond=0)
    run_started = time.perf_counter()
    index_records = []
    all_markdown = [
        "# Cognee SQL Handoff Batch Results",
        "",
        f"- started_at: `{run_started_at.isoformat()}`",
        f"- source_questions: `{args.questions or 'inline QUESTIONS'}`",
        f"- datasets: `{', '.join(datasets)}`",
        f"- search_types: `{', '.join(search_types)}`",
        "",
    ]

    for question_index, question in enumerate(questions, start=1):
        print(f"[{question_index}/{len(questions)}] {question}", flush=True)
        record = run_question(
            handoff,
            client,
            question_index=question_index,
            question=question,
            datasets=datasets,
            scope=scope,
            search_types=search_types,
            timeout=args.timeout,
            context_chars=args.context_chars,
        )
        if record["error"] and args.fail_fast:
            raise RuntimeError(str(record["error"]))

        slug = _slugify(question)[:64] or f"question_{question_index:03d}"
        stem = f"{question_index:03d}_{slug}"
        json_path = args.output_dir / f"{stem}.json"
        md_path = args.output_dir / f"{stem}.md"
        write_json(record, json_path)
        md_text = render_question_markdown(record, handoff)
        md_path.write_text(md_text, encoding="utf-8")

        index_records.append(
            {
                "question_index": question_index,
                "question": question,
                "json": json_path.name,
                "markdown": md_path.name,
                "duration_seconds": record["timing"]["duration_seconds"],
                "validation_ok": validation_ok(record),
                "error": record["error"],
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
    print(f"Saved {len(index_records)} SQL handoff result(s) under {args.output_dir}", flush=True)
    return 0


def run_question(
    handoff: object,
    client: object,
    *,
    question_index: int,
    question: str,
    datasets: Sequence[str],
    scope: Mapping[str, Optional[str]],
    search_types: Sequence[str],
    timeout: float,
    context_chars: int,
) -> dict[str, object]:
    started_at = datetime.now(timezone.utc).replace(microsecond=0)
    started = time.perf_counter()
    result = None
    error = None
    try:
        result = handoff.run_sql_handoff(
            client,
            query=question,
            datasets=datasets,
            scope=scope,
            search_types=search_types,
            timeout=timeout,
            context_chars=context_chars,
        )
        if isinstance(result, dict) and isinstance(result.get("timing"), dict):
            result["timing"]["duration_seconds"] = _elapsed_seconds(started)
    except Exception as exc:  # Keep batch runs inspectable even if one query fails.
        error = str(exc)

    return {
        "question_index": question_index,
        "question": question,
        "datasets": list(datasets),
        "search_types": list(search_types),
        "scope": {key: value for key, value in scope.items() if value},
        "started_at": started_at.isoformat(),
        "timing": {"duration_seconds": _elapsed_seconds(started)},
        "error": error,
        "result": result,
    }


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


def render_question_markdown(record: Mapping[str, object], handoff: object) -> str:
    lines = [
        f"## {int(record['question_index']):03d}. {record['question']}",
        "",
        "### Timing",
        "",
        f"- started_at: `{record.get('started_at')}`",
        f"- duration_seconds: `{(record.get('timing') or {}).get('duration_seconds') if isinstance(record.get('timing'), Mapping) else 'unknown'}`",
        f"- validation_ok: `{validation_ok(record)}`",
        "",
    ]
    if record.get("error"):
        lines.extend(
            [
                "### Error",
                "",
                "```text",
                str(record["error"]),
                "```",
                "",
            ]
        )
        return "\n".join(lines)

    result = record.get("result")
    if isinstance(result, Mapping):
        rendered = handoff.render_markdown(result)
        lines.extend(["### Result", "", rendered, ""])
    else:
        lines.extend(["### Result", "", "No result.", ""])
    return "\n".join(lines)


def validation_ok(record: Mapping[str, object]) -> object:
    result = record.get("result")
    if not isinstance(result, Mapping):
        return False
    validation = result.get("validation")
    if not isinstance(validation, Mapping):
        return False
    return validation.get("ok")


def write_json(value: object, path: Path) -> None:
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def _question_from_item(item: object) -> str:
    if isinstance(item, str):
        return item.strip()
    if isinstance(item, Mapping):
        for key in ("question", "query", "text"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                return value.strip()
    return ""


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", value.strip().lower()).strip("_")
    return slug or "question"


def _elapsed_seconds(started: float) -> float:
    return round(time.perf_counter() - started, 3)


def _load_handoff_module():
    spec = importlib.util.spec_from_file_location("cognee_sql_handoff_helper", HANDOFF_SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load {HANDOFF_SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == "__main__":
    raise SystemExit(main())
