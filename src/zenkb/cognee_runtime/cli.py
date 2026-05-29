from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional, Sequence

from .config import CogneeRuntimeConfig, ProviderExpectation, PROVIDER_CHOICES
from .ingestion import IngestOptions, IngestionProfile, ingest_documents


REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_BASE_URL = "http://localhost:8000"
DEFAULT_DATASET = "zenstatement_canonical"
DEFAULT_DOCS_DIR = REPO_ROOT / "cognee" / "export" / "documents"
DEFAULT_GRAPH_MODEL = REPO_ROOT / "cognee" / "canonical_graph_model.json"
DEFAULT_CUSTOM_PROMPT = REPO_ROOT / "cognee" / "canonical_cognify_prompt.md"
DEFAULT_RUNTIME_ENV = REPO_ROOT / "cognee" / "runtime" / "cognee.env"
DEFAULT_REQUEST_TIMEOUT_SECONDS = 600.0
DEFAULT_STATUS_TIMEOUT_SECONDS = 30.0
DEFAULT_COGNIFY_TIMEOUT_SECONDS = 21600.0
DEFAULT_POLL_INTERVAL_SECONDS = 15.0
DEFAULT_COGNIFY_DATA_PER_BATCH = 1
DEFAULT_COGNIFY_CHUNKS_PER_BATCH = 5
DEFAULT_COGNIFY_CHUNK_SIZE = 2048
DEFAULT_MAX_STATUS_ERRORS = 40


def main(argv: Optional[Sequence[str]] = None, *, default_profile: str = "plain") -> int:
    parser = argparse.ArgumentParser(description="Ingest generated Cognee docs into a local Cognee API")
    parser.add_argument("--profile", choices=("plain", "canonical", "custom"), default=default_profile)
    parser.add_argument("--mode", choices=("full", "staged"), default="full")
    parser.add_argument("--stage", choices=("build-embeddings", "edge-cognify"))
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--dataset", default=DEFAULT_DATASET)
    parser.add_argument("--docs-dir", type=Path, default=DEFAULT_DOCS_DIR)
    parser.add_argument("--runtime-env", type=Path, default=_default_runtime_env())
    parser.add_argument("--runtime-key", default=os.environ.get("COGNEE_RUNTIME_KEY", ""))
    parser.add_argument("--graph-model", type=Path)
    parser.add_argument(
        "--skip-graph-model",
        action="store_true",
        help="Do not send graphSchema/graphModel to Cognee; useful if this Cognee build rejects custom schemas.",
    )
    parser.add_argument("--custom-prompt", type=Path)
    parser.add_argument("--batch-size", type=int, default=50)
    parser.add_argument("--timeout", type=float, default=DEFAULT_REQUEST_TIMEOUT_SECONDS)
    parser.add_argument("--status-timeout", type=float)
    parser.add_argument("--poll-interval", type=float, default=DEFAULT_POLL_INTERVAL_SECONDS)
    parser.add_argument("--cognify-timeout", type=float, default=DEFAULT_COGNIFY_TIMEOUT_SECONDS)
    parser.add_argument("--cognify-data-per-batch", type=int)
    parser.add_argument("--cognify-chunks-per-batch", type=int)
    parser.add_argument("--cognify-chunk-size", type=int)
    parser.add_argument("--max-status-errors", type=int)
    parser.add_argument("--skip-add", action="store_true")
    parser.add_argument("--skip-cognify", action="store_true")
    parser.add_argument("--skip-schema-update", action="store_true")
    parser.add_argument("--foreground-cognify", action="store_true")
    parser.add_argument("--no-progress", action="store_true")
    parser.add_argument("--search", default="")
    parser.add_argument("--status", action="store_true", help="Print Cognee dataset processing status")
    parser.add_argument("--dataset-id", default="", help="Cognee dataset UUID for status polling")
    parser.add_argument("--llm-provider", choices=PROVIDER_CHOICES, default="runtime")
    parser.add_argument("--embedding-provider", choices=PROVIDER_CHOICES, default="runtime")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    try:
        profile = _profile_from_args(args)
        status_timeout = args.status_timeout
        if status_timeout is None:
            status_timeout = DEFAULT_STATUS_TIMEOUT_SECONDS if args.profile == "canonical" else args.timeout
        config = CogneeRuntimeConfig(
            base_url=args.base_url,
            dataset=args.dataset,
            docs_dir=args.docs_dir,
            runtime_env=args.runtime_env,
            runtime_key=args.runtime_key,
            request_timeout=args.timeout,
            status_timeout=status_timeout,
            poll_interval=args.poll_interval,
            cognify_timeout=args.cognify_timeout,
            provider_expectation=ProviderExpectation(args.llm_provider, args.embedding_provider),
        )
        options = IngestOptions(
            mode=args.mode,
            stage=args.stage,
            batch_size=args.batch_size,
            skip_add=args.skip_add,
            skip_cognify=args.skip_cognify,
            skip_graph_model=args.skip_graph_model,
            skip_schema_update=args.skip_schema_update,
            foreground_cognify=args.foreground_cognify,
            no_progress=args.no_progress,
            verbose=args.verbose,
            search=args.search,
            status_only=args.status,
            dataset_id=args.dataset_id,
        )
        return ingest_documents(config, profile, options)
    except RuntimeError as exc:
        print(f"cognee ingest failed: {exc}", file=sys.stderr)
        return 1


def _profile_from_args(args: argparse.Namespace) -> IngestionProfile:
    graph_model = args.graph_model
    custom_prompt = args.custom_prompt
    update_schema = False
    data_per_batch = args.cognify_data_per_batch
    chunks_per_batch = args.cognify_chunks_per_batch
    chunk_size = args.cognify_chunk_size
    max_status_errors = args.max_status_errors

    if args.profile == "canonical":
        graph_model = graph_model or DEFAULT_GRAPH_MODEL
        custom_prompt = custom_prompt or DEFAULT_CUSTOM_PROMPT
        update_schema = True
        data_per_batch = DEFAULT_COGNIFY_DATA_PER_BATCH if data_per_batch is None else data_per_batch
        chunks_per_batch = DEFAULT_COGNIFY_CHUNKS_PER_BATCH if chunks_per_batch is None else chunks_per_batch
        chunk_size = DEFAULT_COGNIFY_CHUNK_SIZE if chunk_size is None else chunk_size
        max_status_errors = DEFAULT_MAX_STATUS_ERRORS if max_status_errors is None else max_status_errors
    elif args.profile == "custom":
        update_schema = not args.skip_schema_update and bool(graph_model or custom_prompt)
        max_status_errors = 0 if max_status_errors is None else max_status_errors
    else:
        max_status_errors = 0 if max_status_errors is None else max_status_errors

    return IngestionProfile(
        name=args.profile,
        graph_model=graph_model,
        custom_prompt=custom_prompt,
        update_schema=update_schema,
        cognify_data_per_batch=data_per_batch,
        cognify_chunks_per_batch=chunks_per_batch,
        cognify_chunk_size=chunk_size,
        max_status_errors=max_status_errors,
    )


def _default_runtime_env() -> Path:
    value = os.environ.get("COGNEE_RUNTIME_ENV_FILE") or os.environ.get("COGNEE_RUNTIME_ENV")
    return Path(value) if value else DEFAULT_RUNTIME_ENV


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
