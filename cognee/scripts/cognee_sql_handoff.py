#!/usr/bin/env python3
"""Single-query staged SQL handoff built on top of Cognee search.

This script intentionally stays self-contained. Cognee is used for context
discovery and staged LLM calls, while the final validation happens locally.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Mapping, Optional, Sequence


DEFAULT_BASE_URL = "http://localhost:8000"
DEFAULT_DATASET = "zenstatement_canonical"
DEFAULT_TIMEOUT_SECONDS = 300.0
SEARCH_TYPES = ("RAG_COMPLETION", "GRAPH_COMPLETION")
SKILLS_DIR = Path(__file__).resolve().parents[1] / "skills" / "sql_handoff"

FORBIDDEN_SQL_NAMES = (
    "account_data_binding",
    "business_flow_binding",
    "workflow_step",
    "business_process",
    "query_pattern",
    "relationship.",
    "state_transition",
    "platform_account",
    "metadata.account_data_bindings",
    "account_data_bindings",
    "canonical.cards",
)
CANONICAL_REFERENCE_PREFIXES = (
    "account_data_binding.",
    "business_flow_binding.",
    "workflow_step.",
    "business_process.",
    "query_pattern.",
    "relationship.",
    "state_transition.",
    "platform_account.",
    "metric.",
    "metric_dependency.",
    "evidence.",
    "rule.",
    "validation_test.",
    "value_profile.",
    "reconciliation_profile.",
    "reconciliation_side.",
    "reconciliation_unit.",
    "business_scope_set.",
    "execution_constraint_set.",
    "platform_context.",
    "table.",
    "column.",
)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Build a staged SQL handoff for one question.")
    parser.add_argument("query", nargs="?", help="Question to resolve.")
    parser.add_argument("--query", dest="query_flag", help="Question to resolve.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--dataset", action="append", help="Cognee dataset name. Repeat for multiple datasets.")
    parser.add_argument("--search-type", choices=SEARCH_TYPES, default="RAG_COMPLETION")
    parser.add_argument("--both", action="store_true", help="Use both RAG_COMPLETION and GRAPH_COMPLETION for discovery.")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--tenant")
    parser.add_argument("--group")
    parser.add_argument("--platform")
    parser.add_argument("--account")
    parser.add_argument("--context-chars", type=int, default=32000)
    parser.add_argument("--output", type=Path, help="Optional JSON output path.")
    parser.add_argument("--markdown-output", type=Path, help="Optional markdown output path.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of markdown summary.")
    args = parser.parse_args(argv)

    query = args.query_flag or args.query
    if not query:
        parser.error("provide a query as positional text or --query")

    started = time.perf_counter()
    datasets = args.dataset or [DEFAULT_DATASET]
    search_types = ordered_search_types(args.search_type, include_both=args.both)
    scope = {
        "tenant": args.tenant,
        "group": args.group,
        "platform": args.platform,
        "account": args.account,
    }
    client = CogneeHttpClient(args.base_url)

    try:
        result = run_sql_handoff(
            client,
            query=query,
            datasets=datasets,
            scope=scope,
            timeout=args.timeout,
            context_chars=args.context_chars,
            search_types=search_types,
        )
    except RuntimeError as exc:
        print(f"cognee SQL handoff failed: {exc}", file=sys.stderr)
        return 1

    result["timing"]["duration_seconds"] = round(time.perf_counter() - started, 3)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    markdown = render_markdown(result)
    if args.markdown_output:
        args.markdown_output.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_output.write_text(markdown, encoding="utf-8")
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    else:
        print(markdown)
    return 0


def run_sql_handoff(
    client: "CogneeHttpClient",
    *,
    query: str,
    datasets: Sequence[str],
    scope: Mapping[str, Optional[str]],
    timeout: float,
    context_chars: int,
    search_types: Sequence[str] = SEARCH_TYPES,
) -> dict[str, object]:
    completion_search_type = search_types[0] if search_types else "RAG_COMPLETION"
    raw_intent = classify_raw_intent(query, scope)
    discovery: dict[str, object] = {}
    discovery_items: dict[str, list[object]] = {}
    discovery_query = render_skill(
        "discovery",
        query=query,
        scope=scope_text(scope),
        raw_intent_json=json.dumps(raw_intent, ensure_ascii=False, sort_keys=True),
    )
    for search_type in search_types:
        response = client.search(discovery_query, datasets=datasets, search_type=search_type, timeout=timeout)
        discovery[search_type] = response
        discovery_items[search_type] = parse_response_items(response)

    context = compact_context(discovery_items, max_chars=context_chars)
    grounded_intent = run_stage(
        client,
        stage="grounded_intent",
        prompt=render_skill(
            "grounded_intent",
            query=query,
            scope=scope_text(scope),
            raw_intent_json=json.dumps(raw_intent, ensure_ascii=False, sort_keys=True),
            context=context,
        ),
        datasets=datasets,
        timeout=timeout,
        search_type=completion_search_type,
    )
    sources = run_stage(
        client,
        stage="source_resolution",
        prompt=render_skill(
            "source_resolver",
            query=query,
            scope=scope_text(scope),
            context=context,
            intent_json=json.dumps(grounded_intent, ensure_ascii=False, sort_keys=True),
        ),
        datasets=datasets,
        timeout=timeout,
        search_type=completion_search_type,
    )
    fields = run_stage(
        client,
        stage="field_join_resolution",
        prompt=render_skill(
            "field_join_resolver",
            query=query,
            scope=scope_text(scope),
            context=context,
            intent_json=json.dumps(grounded_intent, ensure_ascii=False, sort_keys=True),
            source_json=json.dumps(sources, ensure_ascii=False, sort_keys=True),
        ),
        datasets=datasets,
        timeout=timeout,
        search_type=completion_search_type,
    )
    handoff = run_stage(
        client,
        stage="sql_builder",
        prompt=render_skill(
            "sql_builder",
            query=query,
            scope=scope_text(scope),
            intent_json=json.dumps(grounded_intent, ensure_ascii=False, sort_keys=True),
            source_json=json.dumps(sources, ensure_ascii=False, sort_keys=True),
            field_join_json=json.dumps(fields, ensure_ascii=False, sort_keys=True),
        ),
        datasets=datasets,
        timeout=timeout,
        search_type=completion_search_type,
    )
    validation = validate_handoff(handoff)

    return {
        "query": query,
        "scope": {key: value for key, value in scope.items() if value},
        "datasets": list(datasets),
        "search_types": list(search_types),
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "discovery": discovery,
        "stages": {
            "raw_intent": raw_intent,
            "grounded_intent": grounded_intent,
            "source_resolution": sources,
            "field_join_resolution": fields,
            "sql_handoff": handoff,
        },
        "validation": validation,
        "timing": {"duration_seconds": None},
    }


def run_stage(
    client: "CogneeHttpClient",
    *,
    stage: str,
    prompt: str,
    datasets: Sequence[str],
    timeout: float,
    search_type: str = "RAG_COMPLETION",
) -> object:
    response = client.search(prompt, datasets=datasets, search_type=search_type, timeout=timeout)
    items = parse_response_items(response)
    for item in items:
        if isinstance(item, Mapping):
            return dict(item)
    raise RuntimeError(f"{stage} did not return a JSON object: {items[:1]}")


def classify_raw_intent(query: str, scope: Mapping[str, Optional[str]]) -> dict[str, object]:
    """Classify the question before retrieval so discovery can be targeted."""
    lowered = query.lower()
    families: list[str] = []
    target_evidence: list[str] = []

    family_keywords = (
        (
            "metric",
            (
                "highest",
                "lowest",
                "share",
                "volume",
                "trend",
                "average",
                "aov",
                "gross sales",
                "return rate",
                "contribution",
                "profitability",
                "calculate",
                "count",
                "sum",
            ),
        ),
        (
            "report_generation",
            (
                "report",
                "dashboard",
                "analysis",
                "summary",
                "matrix",
            ),
        ),
        (
            "business_process",
            (
                "dependency",
                "bottleneck",
                "risk",
                "manual process",
                "managed returns",
                "return handling",
                "operational",
            ),
        ),
        (
            "workflow",
            (
                "workflow",
                "flow",
                "state",
                "lifecycle",
            ),
        ),
        (
            "source_mapping",
            (
                "handled through",
                "connected marketplaces",
                "mapping",
                "which channels use",
                "which courier handles",
                "oms systems",
                "unicommerce",
            ),
        ),
        (
            "reconciliation",
            (
                "reconciliation",
                "settlement",
                "remittance",
                "cod",
                "payout",
                "receivable",
            ),
        ),
        (
            "logistics",
            (
                "courier",
                "shipment",
                "shiprocket",
                "awb",
                "logistics",
            ),
        ),
    )

    for family, keywords in family_keywords:
        if any(keyword in lowered for keyword in keywords):
            families.append(family)

    if not families:
        families.append("metric")

    if "source_mapping" in families and not ({"metric", "reconciliation", "logistics"} & set(families)):
        answer_mode_hint = "metadata_inventory"
    elif {"business_process", "workflow", "source_mapping"} & set(families):
        answer_mode_hint = "mixed"
    else:
        answer_mode_hint = "physical_sql"

    if {"metric", "report_generation", "reconciliation", "logistics"} & set(families):
        target_evidence.extend(
            [
                "physical runtime tables",
                "physical columns for requested grain, dimensions, filters, metrics, and status fields",
                "query patterns with physical SQL logic",
                "tenant/account/platform filters",
            ]
        )
    if {"business_process", "workflow", "source_mapping"} & set(families):
        target_evidence.extend(
            [
                "account_data_binding and platform_account cards for scope and source bindings",
                "business_flow_binding, business_process, workflow_step, and state_transition cards for process topology",
                "physical table cards connected to selected metadata evidence",
                "relationship cards only when they resolve physical join keys",
            ]
        )

    must_enumerate_sources = bool(
        {"source_mapping", "business_process", "workflow", "reconciliation", "logistics"} & set(families)
        or any(keyword in lowered for keyword in ("all channels", "all marketplaces", "cross-channel", "marketplace-wide"))
    )

    return {
        "query_families": families,
        "answer_mode_hint": answer_mode_hint,
        "must_enumerate_sources": must_enumerate_sources,
        "table_limit": 3 if must_enumerate_sources else 1,
        "target_evidence": list(dict.fromkeys(target_evidence)),
        "scope": {key: value for key, value in scope.items() if value},
        "reason": "Local pre-retrieval routing based only on the user question and explicit scope.",
    }


def ordered_search_types(primary: str, *, include_both: bool) -> list[str]:
    if not include_both:
        return [primary]
    return [primary] + [search_type for search_type in SEARCH_TYPES if search_type != primary]


def render_skill(name: str, **values: object) -> str:
    template = load_skill_template(name)
    rendered = template
    for key, value in values.items():
        rendered = rendered.replace("{{" + key + "}}", str(value))
    unresolved = sorted(set(re.findall(r"\{\{([a-zA-Z0-9_]+)\}\}", rendered)))
    if unresolved:
        raise RuntimeError(f"Unresolved placeholders in skill {name}: {', '.join(unresolved)}")
    return rendered


def load_skill_template(name: str) -> str:
    path = SKILLS_DIR / f"{name}.md"
    if not path.exists():
        raise RuntimeError(f"Missing SQL handoff skill: {path}")
    return path.read_text(encoding="utf-8").strip()


def validate_handoff(handoff: object) -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(handoff, Mapping):
        return {"ok": False, "errors": ["handoff is not a JSON object"], "warnings": []}

    sql = str(handoff.get("sql_skeleton") or "")
    selected_source = str(handoff.get("selected_source") or "")
    lowered_sql = sql.lower()

    if selected_source.startswith("table."):
        errors.append("selected_source is a canonical table id, not a physical SQL table name")
    for forbidden in FORBIDDEN_SQL_NAMES:
        if forbidden.lower() in lowered_sql:
            errors.append(f"sql_skeleton references canonical metadata name: {forbidden}")
    if re.search(r"\bselect\s+['\"]", lowered_sql):
        errors.append("sql_skeleton creates literal metadata rows; query physical tables instead")
    if " from " not in f" {lowered_sql} " and not lowered_sql.lstrip().startswith("--"):
        errors.append("sql_skeleton has no FROM clause and is not a commented partial template")
    if " union " in f" {lowered_sql} ":
        warnings.append("sql_skeleton uses UNION; verify deduplication keys and source precedence are grounded")

    for table in selected_physical_tables(handoff):
        if table.lower() not in lowered_sql:
            warnings.append(f"selected table is not referenced in sql_skeleton: {table}")

    return {"ok": not errors, "errors": errors, "warnings": warnings}


def selected_physical_tables(handoff: Mapping[str, object]) -> list[str]:
    tables = []
    raw_tables = handoff.get("require_tables")
    if not isinstance(raw_tables, list):
        return tables
    for item in raw_tables:
        if not isinstance(item, Mapping):
            continue
        if str(item.get("selected?") or "").strip().lower() != "yes":
            continue
        field = str(item.get("field") or "").strip()
        if field and "." in field and not is_canonical_reference(field):
            tables.append(field)
    return tables


def parse_response_items(response: object) -> list[object]:
    if isinstance(response, list):
        items: list[object] = []
        for item in response:
            items.extend(parse_response_items(item))
        return items
    if not isinstance(response, str):
        return [unwrap_content(response)]
    text = strip_json_fence(response.strip())
    if not text:
        return [response]
    decoder = json.JSONDecoder()
    parsed: list[object] = []
    offset = 0
    while offset < len(text):
        while offset < len(text) and text[offset].isspace():
            offset += 1
        if offset >= len(text):
            break
        try:
            value, end = decoder.raw_decode(text, offset)
        except json.JSONDecodeError:
            if parsed:
                return parsed
            recovered = recover_json_prefix(text[offset:])
            return [unwrap_content(recovered)] if recovered is not None else [response]
        parsed.append(unwrap_content(value))
        offset = end
    return parsed or [response]


def recover_json_prefix(text: str) -> object | None:
    """Best-effort recovery for model output that appends prose after JSON.

    Cognee stage calls occasionally return a useful JSON object followed by
    malformed text. Keep this conservative: only return a value when a balanced
    JSON object/array prefix can be parsed exactly.
    """
    text = text.lstrip()
    if not text or text[0] not in "[{":
        return None
    stack: list[str] = []
    in_string = False
    escaped = False
    for index, char in enumerate(text):
        if in_string:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            continue
        if char == '"':
            in_string = True
        elif char in "[{":
            stack.append("]" if char == "[" else "}")
        elif char in "]}":
            if not stack or stack[-1] != char:
                return None
            stack.pop()
            if not stack:
                try:
                    return json.loads(text[: index + 1])
                except json.JSONDecodeError:
                    return None
    return None


def unwrap_content(value: object) -> object:
    if not isinstance(value, Mapping) or "content" not in value:
        return value
    content = value.get("content")
    if isinstance(content, str):
        try:
            return json.loads(strip_json_fence(content.strip()))
        except json.JSONDecodeError:
            return content
    return content


def strip_json_fence(text: str) -> str:
    if not text.startswith("```"):
        return text
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def is_canonical_reference(value: str) -> bool:
    lowered = value.strip().lower()
    return lowered.startswith(CANONICAL_REFERENCE_PREFIXES)


def compact_context(discovery_items: Mapping[str, Sequence[object]], *, max_chars: int) -> str:
    blocks = []
    for search_type, items in discovery_items.items():
        blocks.append(f"## {search_type}")
        for index, item in enumerate(items, start=1):
            blocks.append(f"### Result {index}")
            blocks.append(json.dumps(item, ensure_ascii=False, sort_keys=True) if isinstance(item, Mapping) else str(item))
    text = "\n".join(blocks)
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "\n...[truncated]"


def scope_text(scope: Mapping[str, Optional[str]]) -> str:
    parts = [f"- {key}: {value}" for key, value in scope.items() if value]
    return "Scope:\n" + "\n".join(parts) if parts else "Scope: none provided"


def render_markdown(result: Mapping[str, object]) -> str:
    validation = result.get("validation") if isinstance(result.get("validation"), Mapping) else {}
    stages = result.get("stages") if isinstance(result.get("stages"), Mapping) else {}
    handoff = stages.get("sql_handoff") if isinstance(stages, Mapping) else {}
    lines = [
        "# Cognee SQL Handoff",
        "",
        f"- query: `{result.get('query')}`",
        f"- search_types: `{', '.join(result.get('search_types') or []) if isinstance(result.get('search_types'), list) else result.get('search_types')}`",
        f"- validation_ok: `{validation.get('ok')}`",
        f"- duration_seconds: `{(result.get('timing') or {}).get('duration_seconds') if isinstance(result.get('timing'), Mapping) else 'unknown'}`",
        "",
        "## Validation",
        "",
        "```json",
        json.dumps(validation, indent=2, ensure_ascii=False, sort_keys=True),
        "```",
        "",
        "## SQL Handoff",
        "",
        "```json",
        json.dumps(handoff, indent=2, ensure_ascii=False, sort_keys=True),
        "```",
    ]
    return "\n".join(lines)


class CogneeHttpClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def search(self, query: str, *, datasets: Sequence[str], search_type: str, timeout: float) -> object:
        payload = {
            "query": query,
            "search_type": search_type,
            "datasets": list(datasets),
        }
        return self.post_json("/api/v1/search", payload, timeout=timeout)

    def post_json(self, path: str, payload: Mapping[str, object], *, timeout: float) -> object:
        body = json.dumps(payload).encode("utf-8")
        request = urllib.request.Request(
            self.base_url + path,
            data=body,
            headers={"Accept": "application/json", "Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"{exc.code} {exc.reason}: {detail}") from exc
        except (urllib.error.URLError, TimeoutError, ConnectionResetError) as exc:
            raise RuntimeError(f"Cognee API unavailable: {exc}") from exc
        if not raw:
            return {}
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return raw


if __name__ == "__main__":
    raise SystemExit(main())
