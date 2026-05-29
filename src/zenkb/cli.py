from __future__ import annotations

import argparse
import importlib.util
import json
import sys
from dataclasses import asdict
from pathlib import Path
from typing import Optional, Sequence

from .canonical import load_jsonl, validate_canonical
from .chunker import (
    chunk_markdown_files,
    validate_chunks,
    write_chunks,
)
from .cognee_export import export_cognee
from .io_utils import write_json, write_jsonl, write_yaml_documents
from .paths import (
    CANONICAL_DIR,
    CHUNKS_DIR,
    CLEANED_V2_SOURCE_DIR,
    COGNEE_EXPORT_DIR,
    INTERMEDIATE_DIR,
    PROCESSED_KB_DIR,
    RAW_SOURCE_DIR,
    REPO_ROOT,
)
from .promoter import promote_intermediate
from .retrieval import build_cognee_candidate_handoff, build_sql_context_bundle, build_sql_handoff_brief


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(prog="zenkb")
    subparsers = parser.add_subparsers(dest="command", required=True)

    chunk_parser = subparsers.add_parser("chunk", help="Generate semantic chunks")
    chunk_parser.add_argument(
        "--source-dir",
        type=Path,
        default=RAW_SOURCE_DIR,
        help="Directory containing raw markdown source files",
    )
    chunk_parser.add_argument(
        "--output",
        type=Path,
        default=CHUNKS_DIR / "semantic_chunks.jsonl",
        help="Output JSONL path for semantic chunks",
    )

    validate_parser = subparsers.add_parser("validate", help="Validate canonical artifacts")
    validate_parser.add_argument(
        "--cards",
        type=Path,
        default=CANONICAL_DIR / "cards.jsonl",
        help="Canonical cards JSONL path",
    )
    validate_parser.add_argument(
        "--edges",
        type=Path,
        default=CANONICAL_DIR / "edges.jsonl",
        help="Canonical edges JSONL path",
    )
    validate_parser.add_argument(
        "--chunks",
        type=Path,
        help="Optional semantic chunks JSONL path for legacy evidence ref checks",
    )

    extract_parser = subparsers.add_parser("extract", help="Extract cleaned_v2 structured KB candidates")
    extract_parser.add_argument(
        "--source-dir",
        type=Path,
        default=CLEANED_V2_SOURCE_DIR,
        help="Directory containing structured cleaned KB files",
    )
    extract_parser.add_argument(
        "--processed-output-dir",
        type=Path,
        default=PROCESSED_KB_DIR,
        help="Output directory for processed cleaned_v2 artifacts",
    )
    extract_parser.add_argument(
        "--output-dir",
        type=Path,
        default=INTERMEDIATE_DIR,
        help="Output directory for candidate cards, edges, and review items",
    )
    extract_parser.add_argument(
        "--include-validation-reports",
        action="store_true",
        help="Include cleaned_v2 validation_report.md files. They are skipped by default.",
    )
    extract_parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable ingestion progress output. File-level logs are still written.",
    )

    promote_parser = subparsers.add_parser("promote", help="Promote intermediate candidates to canonical artifacts")
    promote_parser.add_argument(
        "--candidate-cards",
        type=Path,
        default=INTERMEDIATE_DIR / "candidate_cards.jsonl",
        help="Intermediate candidate cards JSONL path",
    )
    promote_parser.add_argument(
        "--candidate-edges",
        type=Path,
        default=INTERMEDIATE_DIR / "candidate_edges.jsonl",
        help="Intermediate candidate edges JSONL path",
    )
    promote_parser.add_argument(
        "--review-items",
        type=Path,
        default=INTERMEDIATE_DIR / "review_items.jsonl",
        help="Intermediate review items JSONL path",
    )
    promote_parser.add_argument(
        "--chunks",
        type=Path,
        help="Optional semantic chunks JSONL path for legacy evidence ref checks",
    )
    promote_parser.add_argument(
        "--output-dir",
        type=Path,
        default=CANONICAL_DIR,
        help="Canonical output directory",
    )
    promote_parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not clean existing canonical card/edge/manifest outputs before writing",
    )

    export_parser = subparsers.add_parser("export-cognee", help="Export canonical cards as Cognee-friendly documents")
    export_parser.add_argument(
        "--cards",
        type=Path,
        default=CANONICAL_DIR / "cards.jsonl",
        help="Canonical cards JSONL path",
    )
    export_parser.add_argument(
        "--edges",
        type=Path,
        default=CANONICAL_DIR / "edges.jsonl",
        help="Canonical edges JSONL path",
    )
    export_parser.add_argument(
        "--output-dir",
        type=Path,
        default=COGNEE_EXPORT_DIR,
        help="Cognee export output directory",
    )
    export_parser.add_argument(
        "--no-clean",
        action="store_true",
        help="Do not clean existing Cognee export outputs before writing",
    )

    retrieve_parser = subparsers.add_parser("retrieve", help="Build a SQL-generation context bundle")
    retrieve_parser.add_argument("query", help="Business/SQL intent query to retrieve context for")
    retrieve_parser.add_argument(
        "--cards",
        type=Path,
        default=CANONICAL_DIR / "cards.jsonl",
        help="Canonical cards JSONL path",
    )
    retrieve_parser.add_argument(
        "--edges",
        type=Path,
        default=CANONICAL_DIR / "edges.jsonl",
        help="Canonical edges JSONL path",
    )
    retrieve_parser.add_argument(
        "--max-seed-cards",
        type=int,
        default=12,
        help="Maximum canonical candidate IDs accepted from Cognee discovery",
    )
    retrieve_parser.add_argument("--graph-depth", type=int, default=2)
    retrieve_parser.add_argument("--max-cards", type=int, default=80)
    retrieve_parser.add_argument(
        "--format",
        choices=("candidates", "full", "handoff"),
        default="full",
        help="Output Cognee candidates, the full context bundle, or a compact SQL handoff brief",
    )
    retrieve_parser.add_argument("--cognee-base-url", default="http://localhost:8000")
    retrieve_parser.add_argument("--cognee-dataset", default="zenstatement_canonical")
    retrieve_parser.add_argument("--timeout", type=float, default=30.0)
    retrieve_parser.add_argument("--tenant", help="Optional tenant canonical ID or code, such as tenant.nimbus_retail")
    retrieve_parser.add_argument("--group", help="Optional group canonical ID or code, such as group.nimbus_india_d2c")
    retrieve_parser.add_argument("--platform", help="Optional platform canonical ID or code, such as platform.amazon")
    retrieve_parser.add_argument(
        "--account",
        help="Optional platform account canonical ID or code, such as platform_account.nimbus.amazon_in.primary",
    )
    retrieve_parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to also write the context bundle JSON",
    )

    args = parser.parse_args(argv)

    if args.command == "chunk":
        return _run_chunk(args.source_dir, args.output)
    if args.command == "extract":
        return _run_extract(
            args.source_dir,
            args.processed_output_dir,
            args.output_dir,
            include_validation_reports=args.include_validation_reports,
            show_progress=not args.no_progress,
        )
    if args.command == "promote":
        return _run_promote(
            args.candidate_cards,
            args.candidate_edges,
            args.review_items,
            args.chunks,
            args.output_dir,
            clean=not args.no_clean,
        )
    if args.command == "export-cognee":
        return _run_export_cognee(
            args.cards,
            args.edges,
            args.output_dir,
            clean=not args.no_clean,
        )
    if args.command == "validate":
        return _run_validate(args.cards, args.edges, args.chunks)
    if args.command == "retrieve":
        return _run_retrieve(
            args.query,
            args.cards,
            args.edges,
            args.max_seed_cards,
            args.graph_depth,
            args.max_cards,
            args.format,
            args.cognee_base_url,
            args.cognee_dataset,
            args.timeout,
            args.tenant,
            args.group,
            args.platform,
            args.account,
            args.output,
        )
    parser.error(f"unknown command: {args.command}")
    return 2


def _run_chunk(source_dir: Path, output: Path) -> int:
    chunks = chunk_markdown_files(source_dir)
    validation = validate_chunks(chunks)
    write_chunks(chunks, output)

    print(json.dumps(asdict(validation), indent=2, sort_keys=True))
    if not validation.ok:
        return 1
    return 0


def _run_extract(
    source_dir: Path,
    processed_output_dir: Path,
    output_dir: Path,
    *,
    include_validation_reports: bool,
    show_progress: bool,
) -> int:
    ingest_cleaned_v2 = _load_cleaned_v2_ingester()
    result = ingest_cleaned_v2(
        source_dir,
        processed_output_dir,
        include_validation_reports=include_validation_reports,
        show_progress=show_progress,
    )
    candidate_cards = load_jsonl(processed_output_dir / "cards.jsonl")
    candidate_edges = load_jsonl(processed_output_dir / "edges.jsonl")
    review_items = load_jsonl(processed_output_dir / "review_items.jsonl")

    cards_jsonl = output_dir / "candidate_cards.jsonl"
    edges_jsonl = output_dir / "candidate_edges.jsonl"
    review_jsonl = output_dir / "review_items.jsonl"
    write_jsonl(candidate_cards, cards_jsonl)
    write_jsonl(candidate_edges, edges_jsonl)
    write_jsonl(review_items, review_jsonl)

    write_yaml_documents(candidate_cards, output_dir / "candidate_cards.yaml")
    write_yaml_documents(candidate_edges, output_dir / "candidate_edges.yaml")
    write_yaml_documents(review_items, output_dir / "review_items.yaml")

    output = {
        "extractor": "cleaned_v2_structured_adapter",
        "candidate_card_count": len(candidate_cards),
        "candidate_edge_count": len(candidate_edges),
        "review_item_count": len(review_items),
        "processed_counts": result.get("counts", {}),
        "processed_manifest": str(processed_output_dir / "manifest.json"),
        "outputs": {
            "candidate_cards_jsonl": str(cards_jsonl),
            "candidate_edges_jsonl": str(edges_jsonl),
            "review_items_jsonl": str(review_jsonl),
            "processed_dir": str(processed_output_dir),
            "scoped_dir": str(processed_output_dir / "scoped"),
        },
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0


def _load_cleaned_v2_ingester():
    adapter_path = REPO_ROOT / "processed_kb_docs" / "ingest_cleaned_v2.py"
    spec = importlib.util.spec_from_file_location("processed_kb_docs.ingest_cleaned_v2", adapter_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load cleaned_v2 adapter: {adapter_path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module.ingest_cleaned_v2


def _run_promote(
    candidate_cards_path: Path,
    candidate_edges_path: Path,
    review_items_path: Path,
    chunks_path: Optional[Path],
    output_dir: Path,
    clean: bool,
) -> int:
    candidate_cards = load_jsonl(candidate_cards_path)
    candidate_edges = load_jsonl(candidate_edges_path)
    review_items = load_jsonl(review_items_path)
    chunks = load_jsonl(chunks_path) if chunks_path else []
    chunk_ids = [str(chunk.get("chunk_id")) for chunk in chunks if chunk.get("chunk_id")]
    result = promote_intermediate(
        candidate_cards,
        candidate_edges,
        review_items,
        chunk_ids,
        output_dir,
        clean=clean,
    )
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    return 0


def _run_export_cognee(
    cards_path: Path,
    edges_path: Path,
    output_dir: Path,
    clean: bool,
) -> int:
    cards = load_jsonl(cards_path)
    edges = load_jsonl(edges_path)
    result = export_cognee(cards, edges, output_dir, clean=clean)
    print(json.dumps(asdict(result), indent=2, sort_keys=True))
    return 0


def _run_validate(cards_path: Path, edges_path: Path, chunks_path: Optional[Path]) -> int:
    cards = load_jsonl(cards_path)
    edges = load_jsonl(edges_path)
    chunks = load_jsonl(chunks_path) if chunks_path else []
    chunk_ids = [str(chunk.get("chunk_id")) for chunk in chunks if chunk.get("chunk_id")]
    validation = validate_canonical(cards, edges, chunk_ids)
    output = {
        "card_count": validation.card_count,
        "edge_count": validation.edge_count,
        "issues": [asdict(issue) for issue in validation.issues],
    }
    print(json.dumps(output, indent=2, sort_keys=True))
    if not validation.ok:
        return 1
    return 0


def _run_retrieve(
    query: str,
    cards_path: Path,
    edges_path: Path,
    max_seed_cards: int,
    graph_depth: int,
    max_cards: int,
    output_format: str,
    cognee_base_url: str,
    cognee_dataset: str,
    timeout: float,
    tenant: Optional[str],
    group: Optional[str],
    platform: Optional[str],
    account: Optional[str],
    output: Optional[Path],
) -> int:
    cards = load_jsonl(cards_path)
    edges = load_jsonl(edges_path)
    try:
        bundle = build_sql_context_bundle(
            query,
            cards,
            edges,
            max_seed_cards=max_seed_cards,
            graph_depth=graph_depth,
            max_cards=max_cards,
            cognee_base_url=cognee_base_url,
            cognee_dataset=cognee_dataset,
            timeout=timeout,
            scope_overrides={
                "tenant": tenant or "",
                "group": group or "",
                "platform": platform or "",
                "account": account or "",
            },
        )
    except RuntimeError as exc:
        print(f"zenkb retrieve failed: {exc}", file=sys.stderr)
        return 1
    if output_format == "handoff":
        payload = build_sql_handoff_brief(bundle)
    elif output_format == "candidates":
        payload = build_cognee_candidate_handoff(bundle)
    else:
        payload = bundle
    if output:
        write_json(payload, output)
    print(json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True))
    return 0
