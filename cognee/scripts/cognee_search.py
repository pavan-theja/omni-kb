#!/usr/bin/env python3
"""Small Cognee search helper for scoped RAG and graph-completion queries."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from zenkb.cognee_runtime.client import CogneeClient  # noqa: E402


DEFAULT_BASE_URL = "http://localhost:8000"
DEFAULT_DATASET = "zenstatement_canonical"
DEFAULT_TIMEOUT_SECONDS = 300.0
SQL_CONTEXT_PROMPT_PATH = Path(__file__).with_name("sql_query_resolution_prompt.md")
SEARCH_TYPES = ("RAG_COMPLETION", "GRAPH_COMPLETION","GRAPH_COMPLETION_COT", "GRAPH_COMPLETION_CONTEXT_EXTENSION", "GRAPH_SUMMARY_COMPLETION")

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Query Cognee with optional business scope context.")
    parser.add_argument("query", nargs="?", help="Question or search text.")
    parser.add_argument("--query", dest="query_flag", help="Question or search text.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--dataset", action="append", help="Dataset name. Repeat for multiple datasets.")
    parser.add_argument("--search-type", choices=SEARCH_TYPES, default="RAG_COMPLETION")
    parser.add_argument("--both", action="store_true", help="Run both RAG_COMPLETION and GRAPH_COMPLETION.")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--tenant")
    parser.add_argument("--group")
    parser.add_argument("--platform")
    parser.add_argument("--account")
    parser.add_argument("--business-domain")
    parser.add_argument("--workflow")
    parser.add_argument("--table")
    parser.add_argument("--metric")
    parser.add_argument(
        "--no-sql-context",
        action="store_true",
        help="Do not add the default SQL-planning answer instructions.",
    )
    parser.add_argument("--json", action="store_true", help="Print raw JSON response only.")
    args = parser.parse_args(argv)

    query = args.query_flag or args.query
    if not query:
        parser.error("provide a query as positional text or --query")

    datasets = args.dataset or [DEFAULT_DATASET]
    scoped_query = build_scoped_query(
        query,
        {
            "tenant": args.tenant,
            "group": args.group,
            "platform": args.platform,
            "account": args.account,
            "business_domain": args.business_domain,
            "workflow": args.workflow,
            "table": args.table,
            "metric": args.metric,
        },
        include_sql_context=not args.no_sql_context,
    )

    client = CogneeClient(args.base_url)
    search_types = list(SEARCH_TYPES) if args.both else [args.search_type]
    for index, search_type in enumerate(search_types):
        response = search_cognee(
            client,
            query=scoped_query,
            datasets=datasets,
            search_type=search_type,
            timeout=args.timeout,
        )
        if args.json:
            print(json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True))
            continue
        if len(search_types) > 1:
            if index:
                print()
            print(f"=== {search_type} ===")
        print(format_response(response))
    return 0


def build_scoped_query(
    query: str,
    scope: Mapping[str, Optional[str]],
    *,
    include_sql_context: bool = True,
) -> str:
    parts = []
    labels = {
        "tenant": "tenant",
        "group": "group",
        "platform": "platform",
        "account": "platform account",
        "business_domain": "business domain",
        "workflow": "workflow",
        "table": "table",
        "metric": "metric",
    }
    for key, label in labels.items():
        value = scope.get(key)
        if value:
            parts.append(f"{label}: {value}")
    sections = [query]
    if parts:
        sections.append("Scope:\n" + "\n".join(f"- {part}" for part in parts))
    if include_sql_context:
        sections.append(sql_context_instruction())
    return "\n\n".join(sections)


def sql_context_instruction() -> str:
    return SQL_CONTEXT_PROMPT_PATH.read_text(encoding="utf-8").strip()


def search_cognee(
    client: CogneeClient,
    *,
    query: str,
    datasets: Sequence[str],
    search_type: str,
    timeout: float,
) -> object:
    return client.post_json(
        "/api/v1/search",
        {
            "query": query,
            "search_type": search_type,
            "datasets": list(datasets),
        },
        timeout=timeout,
    )


def parse_response_items(response: object) -> list[object]:
    """Return every parseable Cognee completion item.

    Cognee completion searches usually return a list of strings. When more
    than one completion comes back, each string needs to become its own parsed
    object instead of being flattened into one display blob.
    """
    if isinstance(response, list):
        items: list[object] = []
        for item in response:
            items.extend(_parse_single_response_item(item))
        return items
    return _parse_single_response_item(response)


def format_response(response: object) -> str:
    parsed_items = parse_response_items(response)
    if not parsed_items:
        return "(no response)"
    if len(parsed_items) == 1:
        return _format_response_item(parsed_items[0])
    sections = []
    for index, item in enumerate(parsed_items, start=1):
        sections.extend(
            [
                f"#### Response {index}",
                "",
                _format_response_item(item),
            ]
        )
    return "\n\n".join(sections)


def _parse_single_response_item(item: object) -> list[object]:
    if not isinstance(item, str):
        return [item]
    text = _strip_json_fence(item.strip())
    if not text:
        return [item]

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
            return [item]
        parsed.append(_unwrap_content_value(value))
        offset = end

    return parsed or [item]


def _strip_json_fence(text: str) -> str:
    if not text.startswith("```"):
        return text
    lines = text.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].startswith("```"):
        lines = lines[:-1]
    return "\n".join(lines).strip()


def _format_response_item(response: object) -> str:
    if isinstance(response, Mapping):
        return json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True)
    if isinstance(response, list):
        return json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True)
    return str(response)


def _unwrap_content_value(value: object) -> object:
    if not isinstance(value, Mapping) or "content" not in value:
        return value
    content = value.get("content")
    if isinstance(content, str):
        text = _strip_json_fence(content.strip())
        try:
            parsed = json.loads(text)
        except json.JSONDecodeError:
            return content
        return parsed
    if isinstance(content, (Mapping, list)):
        return content
    return value


if __name__ == "__main__":
    raise SystemExit(main())
