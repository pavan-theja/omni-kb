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

from zenkb.cognee_runtime.client import CogneeApiError, CogneeClient  # noqa: E402


DEFAULT_BASE_URL = "http://localhost:8000"
DEFAULT_DATASET = "zenstatement_canonical"
DEFAULT_TIMEOUT_SECONDS = 300.0
SQL_CONTEXT_PROMPT_PATH = Path(__file__).with_name("sql_query_resolution_prompt.md")
SEARCH_TYPES = (
    "SUMMARIES",
    "CHUNKS",
    "RAG_COMPLETION",
    "TRIPLET_COMPLETION",
    "GRAPH_COMPLETION",
    "GRAPH_COMPLETION_DECOMPOSITION",
    "GRAPH_SUMMARY_COMPLETION",
    "CYPHER",
    "NATURAL_LANGUAGE",
    "GRAPH_COMPLETION_COT",
    "GRAPH_COMPLETION_CONTEXT_EXTENSION",
    "FEELING_LUCKY",
    "TEMPORAL",
    "CODING_RULES",
    "CHUNKS_LEXICAL",
    "AGENTIC_COMPLETION",
)
COMPARISON_SEARCH_TYPES = ("RAG_COMPLETION", "GRAPH_COMPLETION")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Query Cognee with optional business scope context.")
    parser.add_argument("query", nargs="?", help="Question or search text.")
    parser.add_argument("--query", dest="query_flag", help="Question or search text.")
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--dataset", action="append", help="Dataset name. Repeat for multiple datasets.")
    parser.add_argument("--search-type", choices=SEARCH_TYPES, default="RAG_COMPLETION")
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
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write a JSON result record. Relative paths are resolved from the repo root.",
    )
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
    scoped_query = build_scoped_query(
        query,
        scope,
        include_sql_context=not args.no_sql_context,
    )

    client = CogneeClient(args.base_url)
    search_types = selected_search_types(args.search_type, include_both=args.both)
    search_options = {
        "top_k": args.top_k,
        "only_context": args.only_context,
        "verbose": args.verbose,
        "system_prompt": args.system_prompt,
        "node_names": args.node_name or [],
        "include_sql_context": not args.no_sql_context,
    }
    results: dict[str, object] = {}
    parsed_results: dict[str, list[object]] = {}
    for index, search_type in enumerate(search_types):
        try:
            response = search_cognee(
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
        except CogneeApiError as exc:
            print(format_search_error(exc, client=client, timeout=args.timeout), file=sys.stderr)
            return 1
        results[search_type] = response
        parsed_results[search_type] = parse_response_items(response)
        if args.json:
            print(json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True))
            continue
        if len(search_types) > 1:
            if index:
                print()
            print(f"=== {search_type} ===")
        print(format_response(response))
    if args.output:
        write_json(
            build_result_record(
                query=query,
                scoped_query=scoped_query,
                scope=scope,
                datasets=datasets,
                search_types=search_types,
                search_options=search_options,
                results=results,
                parsed_results=parsed_results,
            ),
            resolve_output_path(args.output),
        )
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


def build_result_record(
    *,
    query: str,
    scoped_query: str,
    scope: Mapping[str, Optional[str]],
    datasets: Sequence[str],
    search_types: Sequence[str],
    search_options: Mapping[str, object],
    results: Mapping[str, object],
    parsed_results: Mapping[str, Sequence[object]],
) -> dict[str, object]:
    return {
        "query": query,
        "scoped_query": scoped_query,
        "scope": {key: value for key, value in scope.items() if value},
        "datasets": list(datasets),
        "search_types": list(search_types),
        "search_options": dict(search_options),
        "results": dict(results),
        "parsed_results": {key: list(value) for key, value in parsed_results.items()},
    }


def write_json(value: object, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def resolve_output_path(path: Path) -> Path:
    path = path.expanduser()
    if path.is_absolute():
        return path
    return REPO_ROOT / path


def sql_context_instruction() -> str:
    return SQL_CONTEXT_PROMPT_PATH.read_text(encoding="utf-8").strip()


def selected_search_types(primary: str, *, include_both: bool) -> list[str]:
    if not include_both:
        return [primary]
    ordered = [primary]
    for search_type in COMPARISON_SEARCH_TYPES:
        if search_type not in ordered:
            ordered.append(search_type)
    return ordered


def search_cognee(
    client: CogneeClient,
    *,
    query: str,
    datasets: Sequence[str],
    search_type: str,
    timeout: float,
    top_k: Optional[int] = None,
    only_context: bool = False,
    verbose: bool = False,
    system_prompt: Optional[str] = None,
    node_names: Optional[Sequence[str]] = None,
) -> object:
    return client.post_json(
        "/api/v1/search",
        build_search_payload(
            query=query,
            datasets=datasets,
            search_type=search_type,
            top_k=top_k,
            only_context=only_context,
            verbose=verbose,
            system_prompt=system_prompt,
            node_names=node_names,
        ),
        timeout=timeout,
    )


def format_search_error(exc: CogneeApiError, *, client: CogneeClient, timeout: float) -> str:
    lines = [f"cognee search failed: {exc}"]
    if "DatasetNotFoundError" in str(exc) or "No datasets found" in str(exc):
        datasets = available_dataset_names(client, timeout=min(timeout, 10.0))
        if datasets:
            lines.append("Available datasets:")
            lines.extend(f"- {name}" for name in datasets)
        else:
            lines.append("No datasets were returned by /api/v1/datasets.")
    return "\n".join(lines)


def available_dataset_names(client: CogneeClient, *, timeout: float) -> list[str]:
    try:
        response = client.datasets(timeout=timeout)
    except CogneeApiError:
        return []
    if not isinstance(response, list):
        return []
    names = []
    for dataset in response:
        if not isinstance(dataset, Mapping):
            continue
        name = dataset.get("name")
        if name:
            names.append(str(name))
    return sorted(names)


def build_search_payload(
    *,
    query: str,
    datasets: Sequence[str],
    search_type: str,
    top_k: Optional[int] = None,
    only_context: bool = False,
    verbose: bool = False,
    system_prompt: Optional[str] = None,
    node_names: Optional[Sequence[str]] = None,
) -> dict[str, object]:
    if top_k is not None and top_k < 1:
        raise ValueError("top_k must be >= 1")
    payload: dict[str, object] = {
        "query": query,
        "search_type": search_type,
        "datasets": list(datasets),
    }
    if top_k is not None:
        payload["top_k"] = top_k
    if only_context:
        payload["only_context"] = True
    if verbose:
        payload["verbose"] = True
    if system_prompt:
        payload["system_prompt"] = system_prompt
    if node_names:
        payload["node_name"] = list(node_names)
    return payload


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
