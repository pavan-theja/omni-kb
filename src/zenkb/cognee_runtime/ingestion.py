from __future__ import annotations

import json
import time
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable, List, Literal, Optional, Sequence

from .client import CogneeApiError, CogneeClient
from .config import CogneeRuntimeConfig, validate_runtime_providers
from .progress import make_progress, progress_close, progress_set_absolute, progress_status, progress_update
from .schema import load_optional_json, load_optional_text, validate_graph_model
from .status import compact_json, progress_snapshot_from_response, status_summary, terminal_state


@dataclass(frozen=True)
class IngestionProfile:
    name: str
    graph_model: Optional[Path] = None
    custom_prompt: Optional[Path] = None
    update_schema: bool = False
    cognify_data_per_batch: Optional[int] = None
    cognify_chunks_per_batch: Optional[int] = None
    cognify_chunk_size: Optional[int] = None
    max_status_errors: int = 0


@dataclass(frozen=True)
class IngestOptions:
    mode: Literal["full", "staged"] = "full"
    stage: Optional[Literal["build-embeddings", "edge-cognify"]] = None
    batch_size: int = 50
    skip_add: bool = False
    skip_cognify: bool = False
    skip_graph_model: bool = False
    skip_schema_update: bool = False
    foreground_cognify: bool = False
    no_progress: bool = False
    verbose: bool = False
    search: str = ""
    status_only: bool = False
    dataset_id: str = ""


def ingest_documents(
    config: CogneeRuntimeConfig,
    profile: IngestionProfile,
    options: IngestOptions,
    *,
    client: Optional[CogneeClient] = None,
) -> int:
    client = client or CogneeClient(config.base_url)
    validate_runtime_providers(config.provider_expectation, config.runtime_env)

    if options.status_only:
        response = client.dataset_status(
            dataset_name=config.dataset,
            dataset_id=options.dataset_id,
            timeout=config.status_timeout,
        )
        print(json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True))
        return 0

    if options.mode == "staged" and not options.stage:
        raise RuntimeError("--stage is required when --mode staged is used")
    if options.mode == "staged" and options.stage == "edge-cognify":
        options = replace(options, skip_add=True)

    files = sorted(config.docs_dir.rglob("*.md"))
    if not files and not options.skip_add:
        raise RuntimeError(f"No markdown documents found under {config.docs_dir}")
    if not options.skip_add:
        batches = list(_batches(files, options.batch_size))
        print(
            f"Discovered {len(files)} markdown documents under {config.docs_dir} "
            f"({len(batches)} batches, batch_size={options.batch_size})",
            flush=True,
        )
        _add_batches(client, config, files, batches, options)

    if options.mode == "staged" and options.stage == "build-embeddings":
        print(
            "Prepared dataset stage completed. This Cognee wrapper has no verified "
            "embedding-only endpoint yet; run --mode staged --stage edge-cognify "
            "to execute schema-aware Cognify.",
            flush=True,
        )
        return 0

    graph_model = None
    if not options.skip_graph_model:
        graph_model = load_optional_json(profile.graph_model)
        if graph_model is not None and profile.graph_model is not None:
            validate_graph_model(graph_model, profile.graph_model)
    custom_prompt = load_optional_text(profile.custom_prompt)

    if not options.skip_cognify:
        if profile.update_schema and not options.skip_schema_update and (graph_model or custom_prompt):
            dataset_id = options.dataset_id or client.resolve_dataset_id(
                config.dataset,
                timeout=config.request_timeout,
            )
            print(f"Updating Cognee dataset schema: {dataset_id}", flush=True)
            schema_response = update_dataset_schema(
                client,
                dataset_id=dataset_id,
                graph_schema=graph_model,
                custom_prompt=custom_prompt,
                timeout=config.request_timeout,
            )
            print(format_response(schema_response, verbose=options.verbose), flush=True)

        cognify_payload = build_cognify_payload(
            config.dataset,
            run_in_background=not options.foreground_cognify,
            graph_model=graph_model,
            custom_prompt=custom_prompt,
            data_per_batch=profile.cognify_data_per_batch,
            chunks_per_batch=profile.cognify_chunks_per_batch,
            chunk_size=profile.cognify_chunk_size,
        )
        if options.foreground_cognify:
            print(f"Cognifying dataset in foreground: {config.dataset}", flush=True)
            response = client.post_json("/api/v1/cognify", cognify_payload, timeout=config.request_timeout)
            print(format_response(response, verbose=options.verbose), flush=True)
        else:
            print(f"Starting background Cognify for dataset: {config.dataset}", flush=True)
            response = client.post_json("/api/v1/cognify", cognify_payload, timeout=config.request_timeout)
            print(format_response(response, verbose=options.verbose), flush=True)
            poll_cognify(client, config, options, max_status_errors=profile.max_status_errors)

    if options.search:
        print(f"Searching dataset: {options.search}")
        response = client.post_json(
            "/api/v1/search",
            {
                "query": options.search,
                "search_type": "GRAPH_COMPLETION",
                "datasets": [config.dataset],
            },
            timeout=config.request_timeout,
        )
        print(json.dumps(response, indent=2, ensure_ascii=False, sort_keys=True))

    return 0


def build_cognify_payload(
    dataset: str,
    *,
    run_in_background: bool,
    graph_model: Optional[dict],
    custom_prompt: str,
    data_per_batch: Optional[int],
    chunks_per_batch: Optional[int],
    chunk_size: Optional[int],
) -> dict:
    payload: dict[str, object] = {
        "datasets": [dataset],
        "runInBackground": run_in_background,
    }
    if data_per_batch is not None:
        if data_per_batch < 1:
            raise RuntimeError("--cognify-data-per-batch must be >= 1")
        payload["dataPerBatch"] = data_per_batch
    if chunks_per_batch is not None:
        if chunks_per_batch < 1:
            raise RuntimeError("--cognify-chunks-per-batch must be >= 1")
        payload["chunksPerBatch"] = chunks_per_batch
    if chunk_size is not None:
        if chunk_size < 256:
            raise RuntimeError("--cognify-chunk-size must be >= 256")
        payload["chunkSize"] = chunk_size
    if graph_model:
        payload["graphModel"] = graph_model
    if custom_prompt:
        payload["customPrompt"] = custom_prompt
    return payload


def update_dataset_schema(
    client: CogneeClient,
    *,
    dataset_id: str,
    graph_schema: Optional[dict],
    custom_prompt: str,
    timeout: float,
) -> object:
    payload: dict[str, object] = {}
    if graph_schema:
        payload["graphSchema"] = graph_schema
    if custom_prompt:
        payload["customPrompt"] = custom_prompt
    if not payload:
        return {"status": "skipped", "reason": "no graph schema or custom prompt configured"}
    return client.put_json(f"/api/v1/datasets/{dataset_id}/schema", payload, timeout=timeout)


def poll_cognify(
    client: CogneeClient,
    config: CogneeRuntimeConfig,
    options: IngestOptions,
    *,
    max_status_errors: int,
) -> None:
    if config.poll_interval <= 0:
        raise RuntimeError("--poll-interval must be > 0")
    if max_status_errors < 0:
        raise RuntimeError("--max-status-errors must be >= 0")
    started = time.monotonic()
    progress = make_progress(None, "Cognify", "poll", disabled=options.no_progress)
    last_summary = ""
    transient_status_errors = 0
    try:
        while True:
            if config.cognify_timeout and time.monotonic() - started > config.cognify_timeout:
                raise RuntimeError(f"Cognify polling timed out after {config.cognify_timeout:g}s")
            try:
                response = client.dataset_status(
                    dataset_name=config.dataset,
                    dataset_id=options.dataset_id,
                    timeout=config.status_timeout,
                )
                transient_status_errors = 0
            except CogneeApiError as exc:
                if not exc.transient:
                    raise
                transient_status_errors += 1
                summary = f"Cognee API unavailable while polling ({transient_status_errors}): {exc}"
                if summary != last_summary:
                    print(f"Cognify status: {summary}", flush=True)
                    last_summary = summary
                progress_status(progress, summary[:120])
                progress_update(progress, 1)
                if max_status_errors and transient_status_errors >= max_status_errors:
                    raise RuntimeError(
                        "Cognee API stayed unavailable for "
                        f"{transient_status_errors} consecutive status polls; "
                        "restart Cognee and rerun with --skip-add if the dataset add phase completed."
                    ) from exc
                time.sleep(config.poll_interval)
                continue
            summary = status_summary(response, verbose=options.verbose)
            if summary != last_summary:
                print(f"Cognify status: {summary}", flush=True)
                last_summary = summary
            progress_status(progress, summary[:120])
            snapshot = progress_snapshot_from_response(response)
            if snapshot:
                progress_set_absolute(progress, snapshot.current, snapshot.total)
            else:
                progress_update(progress, 1)
            state = terminal_state(response)
            if state == "failed":
                raise RuntimeError(f"Cognify failed: {compact_json(response)}")
            if state == "completed":
                print("Cognify completed.", flush=True)
                return
            time.sleep(config.poll_interval)
    finally:
        progress_close(progress)


def format_response(value: object, verbose: bool) -> str:
    if verbose or not isinstance(value, dict):
        return compact_json(value)
    parts: List[str] = []
    status = value.get("status")
    if status:
        parts.append(f"status={status}")
    dataset_name = value.get("dataset_name")
    if dataset_name:
        parts.append(f"dataset={dataset_name}")
    pipeline_run_id = value.get("pipeline_run_id")
    if pipeline_run_id:
        parts.append(f"pipeline_run_id={pipeline_run_id}")
    ingestion_info = value.get("data_ingestion_info")
    if isinstance(ingestion_info, list):
        parts.append(f"items={len(ingestion_info)}")
    if parts:
        return ", ".join(parts)
    return compact_json(value)


def _add_batches(
    client: CogneeClient,
    config: CogneeRuntimeConfig,
    files: Sequence[Path],
    batches: Sequence[Sequence[Path]],
    options: IngestOptions,
) -> None:
    progress = make_progress(len(files), "Add documents", "file", disabled=options.no_progress)
    uploaded = 0
    try:
        for batch_index, batch in enumerate(batches, start=1):
            progress_status(progress, f"batch {batch_index}/{len(batches)}")
            print(f"Adding batch {batch_index}/{len(batches)}: {len(batch)} files", flush=True)
            response = client.post_multipart(
                "/api/v1/add",
                fields={
                    "datasetName": config.dataset,
                    "run_in_background": "false",
                },
                files=[("data", path) for path in batch],
                timeout=config.request_timeout,
            )
            uploaded += len(batch)
            progress_update(progress, len(batch))
            print(
                f"Added batch {batch_index}/{len(batches)} "
                f"({uploaded}/{len(files)} files): {format_response(response, verbose=options.verbose)}",
                flush=True,
            )
    finally:
        progress_close(progress)


def _batches(items: Sequence[Path], size: int) -> Iterable[Sequence[Path]]:
    if size < 1:
        raise RuntimeError("--batch-size must be >= 1")
    for index in range(0, len(items), size):
        yield items[index:index + size]
