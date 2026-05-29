#!/usr/bin/env python3
"""Simple shaped Cognee ingestion pipeline.

Function hierarchy:
- Entrypoint: CLI parsing and top-level shape/add/Cognify routing.
- Workflow/orchestration: canonical shaping, Cognee add, and plain Cognify.
- Document rendering/data structuring: canonical JSONL -> markdown packs.
- File/data helpers: JSONL, JSON, batching, counts, escaping.
- HTTP/response helpers: compact Cognee API response formatting.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import DefaultDict, Iterable, List, Mapping, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from zenkb.cognee_runtime.client import CogneeClient  # noqa: E402
from zenkb.cognee_runtime.progress import make_progress, progress_close, progress_status, progress_update  # noqa: E402


DEFAULT_BASE_URL = "http://localhost:8000"
DEFAULT_DATASET = "zenstatement_canonical"
DEFAULT_CARDS = REPO_ROOT / "canonical" / "cards.jsonl"
DEFAULT_EDGES = REPO_ROOT / "canonical" / "edges.jsonl"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "cognee" / "shaped_export"
DEFAULT_MAX_TOKENS = 6000
DEFAULT_BATCH_SIZE = 50
DEFAULT_TIMEOUT_SECONDS = 600.0
DEFAULT_COGNIFY_POLL_INTERVAL_SECONDS = 10.0
DEFAULT_COGNEE_CONTAINER = "zenstatement-cognee"

CORE_FIELD_ORDER = (
    "canonical_id",
    "card_type",
    "name",
    "description",
    "status",
    "confidence",
    "review_status",
)

TOKEN_RE = re.compile(r"\w+|[^\w\s]", re.UNICODE)


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Parse CLI arguments and run the simple shaped add/Cognify flow.

    Category: Entrypoint.
    Consumed by: the __main__ block and direct command-line execution.
    Why: turns user flags into the ordered workflow: shape or reuse packs,
    upload them, then optionally start plain Cognee Cognify.
    """

    parser = argparse.ArgumentParser(
        description=(
            "Shape canonical cards into card-boundary-safe Cognee add packs, "
            "then POST those packs to /api/v1/add and run /api/v1/cognify."
        )
    )
    parser.add_argument("--base-url", default=DEFAULT_BASE_URL)
    parser.add_argument("--dataset", default=DEFAULT_DATASET)
    parser.add_argument("--cards", type=Path, default=DEFAULT_CARDS)
    parser.add_argument("--edges", type=Path, default=DEFAULT_EDGES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help="Estimated token cap per generated markdown pack. Whole cards are never split.",
    )
    parser.add_argument(
        "--add-batch-size",
        "--batch-size",
        dest="add_batch_size",
        type=int,
        default=DEFAULT_BATCH_SIZE,
        help="Markdown files per /api/v1/add request. --batch-size is kept as an alias.",
    )
    parser.add_argument(
        "--cognify-dataset-size",
        "--cognify-batch-size",
        dest="cognify_dataset_size",
        type=int,
        default=0,
        help=(
            "When > 0, process shaped markdown packs in Cognify batches of this size."
        ),
    )
    parser.add_argument(
        "--cognify-scope",
        choices=("separate-datasets", "same-dataset"),
        default="separate-datasets",
        help=(
            "With --cognify-dataset-size, choose whether each batch gets a suffixed "
            "dataset or every batch is additively added to the same dataset."
        ),
    )
    parser.add_argument(
        "--cognify-poll-interval",
        type=float,
        default=DEFAULT_COGNIFY_POLL_INTERVAL_SECONDS,
        help="Seconds between local Docker log checks when Cognify batching is enabled.",
    )
    parser.add_argument(
        "--start-batch",
        type=int,
        default=1,
        help="First Cognify batch index to process when --cognify-dataset-size is used.",
    )
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--shape-only", action="store_true", help="Write shaped packs but do not call Cognee add.")
    parser.add_argument("--skip-shape", action="store_true", help="Add existing files from output-dir/documents.")
    parser.add_argument("--skip-cognify", action="store_true", help="Add documents but do not start Cognify.")
    parser.add_argument("--no-progress", action="store_true", help="Disable tqdm/plain progress output.")
    parser.add_argument("--no-clean", action="store_true", help="Do not clean output-dir before shaping.")
    args = parser.parse_args(argv)

    try:
        # skip-shape is the retry path: reuse already-shaped packs without
        # touching canonical/cards.jsonl or canonical/edges.jsonl again.
        if args.skip_shape:
            documents_dir = args.output_dir / "documents"
            manifest = {"documents_dir": str(documents_dir), "document_count": _count_markdown_files(documents_dir)}
        else:
            # The default path keeps complete canonical cards together before
            # upload so Cognee does not see fragmented card records.
            manifest = shape_canonical_dataset(
                cards_path=args.cards,
                edges_path=args.edges,
                output_dir=args.output_dir,
                max_tokens=args.max_tokens,
                clean=not args.no_clean,
            )
            documents_dir = Path(str(manifest["documents_dir"]))
            print(json.dumps(manifest, indent=2, sort_keys=True), flush=True)

        document_paths = sorted(documents_dir.glob("*.md"))
        if not document_paths:
            raise RuntimeError(f"No shaped markdown documents found under {documents_dir}")
        if args.shape_only:
            return 0

        # The simple flow only sends docs and triggers Cognee's default Cognify;
        # schema-aware prompt/model behavior lives in cognee_ingest_custom.py.
        client = CogneeClient(args.base_url)
        if args.cognify_dataset_size:
            add_and_cognify_dataset_batches(
                client,
                dataset=args.dataset,
                document_paths=document_paths,
                dataset_batch_size=args.cognify_dataset_size,
                add_batch_size=args.add_batch_size,
                cognify_scope=args.cognify_scope,
                timeout=args.timeout,
                poll_interval=args.cognify_poll_interval,
                start_batch=args.start_batch,
                skip_cognify=args.skip_cognify,
                no_progress=args.no_progress,
            )
        else:
            add_documents(
                client,
                dataset=args.dataset,
                document_paths=document_paths,
                batch_size=args.add_batch_size,
                timeout=args.timeout,
                no_progress=args.no_progress,
            )
            if not args.skip_cognify:
                cognify_dataset(client, dataset=args.dataset, timeout=args.timeout)
        return 0
    except RuntimeError as exc:
        print(f"cognee simple ingest failed: {exc}", file=sys.stderr)
        return 1


def shape_canonical_dataset(
    *,
    cards_path: Path,
    edges_path: Path,
    output_dir: Path,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    clean: bool = True,
) -> Mapping[str, object]:
    """Render canonical cards and explicit edges into card-safe markdown packs.

    Category: Workflow/orchestration and document structuring.
    Consumed by: main().
    Why: transforms canonical JSONL artifacts into bounded markdown documents
    that preserve whole-card boundaries before Cognee add.
    """

    if max_tokens < 500:
        raise RuntimeError("--max-tokens must be >= 500")
    if clean and output_dir.exists():
        shutil.rmtree(output_dir)

    documents_dir = output_dir / "documents"
    documents_dir.mkdir(parents=True, exist_ok=True)

    cards = _load_jsonl(cards_path)
    edges = _load_jsonl(edges_path)
    outgoing = _edges_by(edges, "source_id")
    incoming = _edges_by(edges, "target_id")
    body_limit = _body_token_limit(max_tokens)

    pack_index = 0
    current_cards: List[str] = []
    current_ids: List[str] = []
    current_body_tokens = 0
    metadata_records: List[Mapping[str, object]] = []
    oversized_card_ids: List[str] = []

    def flush_pack(*, oversized: bool = False) -> None:
        """Write the current in-memory pack and reset pack accumulators.

        Category: Local workflow helper.
        Consumed by: shape_canonical_dataset().
        Why: normal, oversized, and final flush paths should write identical
        markdown and metadata records.
        """

        nonlocal pack_index, current_cards, current_ids, current_body_tokens
        if not current_cards:
            return
        pack_index += 1
        filename = f"canonical_pack_{pack_index:04d}.md"
        path = documents_dir / filename
        markdown = _render_pack(
            pack_index=pack_index,
            canonical_ids=current_ids,
            card_markdown=current_cards,
            max_tokens=max_tokens,
        )
        estimated_tokens = estimate_tokens(markdown)
        path.write_text(markdown, encoding="utf-8")
        metadata_records.append(
            {
                "document_path": path.relative_to(output_dir).as_posix(),
                "pack_index": pack_index,
                "card_count": len(current_ids),
                "canonical_ids": list(current_ids),
                "estimated_tokens": estimated_tokens,
                "oversized": oversized,
            }
        )
        if oversized:
            # Oversized cards are still written intact; the manifest records
            # them for review instead of splitting card evidence across files.
            oversized_card_ids.extend(current_ids)
        current_cards = []
        current_ids = []
        current_body_tokens = 0

    for card in sorted(cards, key=lambda item: str(item.get("canonical_id"))):
        canonical_id = str(card.get("canonical_id") or "")
        if not canonical_id:
            continue
        card_markdown = _render_card(
            card,
            outgoing_edges=outgoing.get(canonical_id, []),
            incoming_edges=incoming.get(canonical_id, []),
        )
        card_tokens = estimate_tokens(card_markdown)

        if card_tokens > body_limit:
            # Never split a canonical card. If a single card is too large, place
            # it alone in an oversized pack.
            flush_pack()
            current_cards.append(card_markdown)
            current_ids.append(canonical_id)
            current_body_tokens = card_tokens
            flush_pack(oversized=True)
            continue

        # Count the markdown separator only when appending to a non-empty pack.
        separator_tokens = estimate_tokens("\n\n---\n\n") if current_cards else 0
        next_tokens = current_body_tokens + separator_tokens + card_tokens
        if current_cards and next_tokens > body_limit:
            # Flush before appending so the current pack stays within the
            # approximate token target while card boundaries remain intact.
            flush_pack()
            separator_tokens = 0
            next_tokens = card_tokens

        current_cards.append(card_markdown)
        current_ids.append(canonical_id)
        current_body_tokens = next_tokens

    flush_pack()
    _write_jsonl(metadata_records, output_dir / "metadata.jsonl")

    # The manifest is the shaping receipt used by humans and retry runs.
    manifest = {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "source": "canonical",
        "cards": str(cards_path),
        "edges": str(edges_path),
        "documents_dir": str(documents_dir),
        "card_count": len(cards),
        "edge_count": len(edges),
        "document_count": len(metadata_records),
        "max_tokens": max_tokens,
        "oversized_card_count": len(oversized_card_ids),
        "oversized_card_ids": oversized_card_ids,
    }
    _write_json(manifest, output_dir / "manifest.json")
    return manifest


def add_documents(
    client: CogneeClient,
    *,
    dataset: str,
    document_paths: Sequence[Path],
    batch_size: int,
    timeout: float,
    no_progress: bool = False,
) -> None:
    """Upload shaped markdown packs to Cognee in deterministic batches.

    Category: Workflow/orchestration.
    Consumed by: main().
    Why: isolates the add phase, including batch sizing, multipart upload, and
    progress output for the shaped markdown documents.
    """

    if batch_size < 1:
        raise RuntimeError("--add-batch-size must be >= 1")

    batches = list(_batches(document_paths, batch_size))
    progress = make_progress(len(document_paths), "Add shaped packs", "file", disabled=no_progress)
    added = 0
    try:
        for batch_index, batch in enumerate(batches, start=1):
            # Cognee's add endpoint accepts multiple multipart `data` files, so
            # each batch becomes one API call.
            progress_status(progress, f"batch {batch_index}/{len(batches)}")
            response = client.post_multipart(
                "/api/v1/add",
                fields={
                    "datasetName": dataset,
                    "run_in_background": "false",
                },
                files=[("data", path) for path in batch],
                timeout=timeout,
            )
            added += len(batch)
            progress_update(progress, len(batch))
            progress_status(progress, _format_response(response)[:120])
    finally:
        progress_close(progress)
    print(f"Added {added}/{len(document_paths)} shaped markdown packs to dataset {dataset}.", flush=True)


def add_and_cognify_dataset_batches(
    client: CogneeClient,
    *,
    dataset: str,
    document_paths: Sequence[Path],
    dataset_batch_size: int,
    add_batch_size: int,
    timeout: float,
    cognify_scope: str = "separate-datasets",
    poll_interval: float = DEFAULT_COGNIFY_POLL_INTERVAL_SECONDS,
    start_batch: int = 1,
    skip_cognify: bool = False,
    no_progress: bool = False,
    wait_for_completion: bool = True,
) -> List[str]:
    """Add bounded document groups to separate datasets and Cognify each group.

    Category: Workflow/orchestration.
    Consumed by: main().
    Why: Cognee Cognify runs at dataset level, so smaller independent datasets
    are the simplest way to avoid one giant Cognify job.
    """

    if dataset_batch_size < 1:
        raise RuntimeError("--cognify-dataset-size must be >= 1")
    if cognify_scope not in ("separate-datasets", "same-dataset"):
        raise RuntimeError("--cognify-scope must be separate-datasets or same-dataset")
    if poll_interval <= 0:
        raise RuntimeError("--cognify-poll-interval must be > 0")
    if start_batch < 1:
        raise RuntimeError("--start-batch must be >= 1")

    document_batches = list(_batches(document_paths, dataset_batch_size))
    dataset_names: List[str] = []
    print(
        f"Processing {len(document_paths)} shaped markdown packs as "
        f"{len(document_batches)} Cognify batches "
        f"(cognify_dataset_size={dataset_batch_size}, cognify_scope={cognify_scope}).",
        flush=True,
    )
    for batch_index, batch in enumerate(document_batches, start=1):
        if batch_index < start_batch:
            continue
        batch_dataset = dataset if cognify_scope == "same-dataset" else f"{dataset}_batch_{batch_index:04d}"
        if batch_dataset not in dataset_names:
            dataset_names.append(batch_dataset)
        print(
            f"Cognify batch {batch_index}/{len(document_batches)}: "
            f"{len(batch)} markdown packs -> dataset {batch_dataset}",
            flush=True,
        )
        add_documents(
            client,
            dataset=batch_dataset,
            document_paths=batch,
            batch_size=add_batch_size,
            timeout=timeout,
            no_progress=no_progress,
        )
        if skip_cognify:
            continue
        started_at = datetime.now(timezone.utc)
        response = cognify_dataset(client, dataset=batch_dataset, timeout=timeout, run_in_background=True)
        if wait_for_completion:
            wait_for_cognify_log_completion(
                response,
                started_at=started_at,
                timeout=timeout,
                poll_interval=poll_interval,
            )
    print("Batch datasets:", ", ".join(dataset_names), flush=True)
    return dataset_names


def cognify_dataset(
    client: CogneeClient,
    *,
    dataset: str,
    timeout: float,
    run_in_background: bool = True,
) -> object:
    """Start Cognee's default background Cognify pipeline for one dataset.

    Category: Workflow/orchestration.
    Consumed by: main().
    Why: the simple ingest path intentionally uses Cognee defaults after add,
    without custom graph schema or custom prompt fields.
    """

    mode = "background" if run_in_background else "foreground"
    print(f"Starting {mode} Cognify for dataset {dataset}", flush=True)
    response = client.post_json(
        "/api/v1/cognify",
        {
            "datasets": [dataset],
            "runInBackground": run_in_background,
        },
        timeout=timeout,
    )
    print(f"Cognify response: {_format_response(response)}", flush=True)
    return response


def wait_for_cognify_log_completion(
    response: object,
    *,
    started_at: datetime,
    timeout: float,
    poll_interval: float,
    container: str = DEFAULT_COGNEE_CONTAINER,
) -> None:
    """Wait for Cognee's Docker log completion line for the current Cognify run.

    Category: Workflow/orchestration.
    Consumed by: add_and_cognify_dataset_batches().
    Why: this local Docker runtime currently reports stale dataset status and
    foreground Cognify calls can stay open after the server logs completion.
    """

    pipeline_ids = _pipeline_run_ids(response)
    if pipeline_ids:
        print(f"Waiting for Cognify completion in Docker logs: {', '.join(pipeline_ids)}", flush=True)
    else:
        print("Waiting for Cognify completion in Docker logs", flush=True)

    since = started_at.replace(microsecond=0).isoformat().replace("+00:00", "Z")
    deadline = time.monotonic() + timeout if timeout > 0 else None
    last_report = 0.0
    while True:
        output = _docker_logs_since(container, since)
        completed = [
            line
            for line in output.splitlines()
            if "Pipeline run completed" in line
        ]
        if completed:
            if pipeline_ids and not any(pipeline_id in completed[-1] for pipeline_id in pipeline_ids):
                print(
                    "Cognify completed with a pipeline id that differed from the API response; "
                    "continuing because the completion line appeared after this batch started.",
                    flush=True,
                )
            print(f"Cognify completed: {completed[-1].strip()}", flush=True)
            return

        lowered = output.lower()
        if "pipeline run errored" in lowered or "cognify failed" in lowered:
            raise RuntimeError(f"Cognify failed according to Docker logs since {since}")
        if deadline and time.monotonic() > deadline:
            raise RuntimeError(f"Timed out waiting for Cognify completion in Docker logs after {timeout:g}s")

        now = time.monotonic()
        if now - last_report >= max(30.0, poll_interval):
            if pipeline_ids:
                print(f"Still waiting for Cognify completion: {', '.join(pipeline_ids)}", flush=True)
            else:
                print("Still waiting for Cognify completion", flush=True)
            last_report = now
        time.sleep(poll_interval)


def _render_pack(
    *,
    pack_index: int,
    canonical_ids: Sequence[str],
    card_markdown: Sequence[str],
    max_tokens: int,
) -> str:
    """Render one generated markdown file containing complete canonical cards.

    Category: Document rendering/data structuring.
    Consumed by: shape_canonical_dataset().
    Why: gives every pack stable frontmatter and a clear BEGIN/END-card body for
    Cognee add/Cognify.
    """

    lines = [
        "---",
        'source: "canonical"',
        f'pack_id: "canonical_pack_{pack_index:04d}"',
        f"pack_index: {pack_index}",
        f"card_count: {len(canonical_ids)}",
        f"max_estimated_tokens: {max_tokens}",
        f'first_canonical_id: "{_escape_frontmatter(canonical_ids[0])}"',
        f'last_canonical_id: "{_escape_frontmatter(canonical_ids[-1])}"',
        "---",
        "",
        f"# Canonical Pack {pack_index:04d}",
        "",
        "Each BEGIN/END block is one complete canonical card. Generated packs keep card boundaries intact before Cognee add.",
        "",
    ]
    return "\n".join(lines + list(card_markdown)) + "\n"


def _render_card(
    card: Mapping[str, object],
    *,
    outgoing_edges: Sequence[Mapping[str, object]],
    incoming_edges: Sequence[Mapping[str, object]],
) -> str:
    """Render one canonical card with fields and explicit relationship lines.

    Category: Document rendering/data structuring.
    Consumed by: shape_canonical_dataset().
    Why: converts canonical card JSON plus incoming/outgoing edges into markdown
    evidence while preserving exact canonical ids.
    """

    canonical_id = str(card.get("canonical_id") or "")
    lines = [
        f"<!-- BEGIN_CANONICAL_CARD {canonical_id} -->",
        "",
        f"## {canonical_id}",
        "",
        "### Fields",
        "",
    ]
    for key in _ordered_card_keys(card):
        value = card.get(key)
        if value in (None, "", []):
            continue
        lines.extend(_format_field(key, value))

    if outgoing_edges or incoming_edges:
        # Include both directions so each card carries enough relationship
        # context even when Cognee processes packs independently.
        lines.extend(["", "### Relationships", ""])
        for edge in outgoing_edges:
            lines.append(_format_edge("outgoing", edge))
        for edge in incoming_edges:
            lines.append(_format_edge("incoming", edge))

    lines.extend(["", f"<!-- END_CANONICAL_CARD {canonical_id} -->"])
    return "\n".join(lines)


def _ordered_card_keys(card: Mapping[str, object]) -> List[str]:
    """Put identity/review fields first, then keep all remaining fields sorted.

    Category: Document rendering/data structuring.
    Consumed by: _render_card().
    Why: generated cards stay readable for humans and deterministic for diffs.
    """

    keys = [key for key in CORE_FIELD_ORDER if key in card]
    keys.extend(sorted(key for key in card if key not in CORE_FIELD_ORDER))
    return keys


def _format_field(key: str, value: object) -> List[str]:
    """Format scalar fields inline and structured fields as fenced JSON.

    Category: Document rendering/data structuring.
    Consumed by: _render_card().
    Why: preserves lists/dicts without lossy stringification while keeping
    simple values compact.
    """

    if isinstance(value, (Mapping, list)):
        return [
            f"- {key}:",
            "```json",
            json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True),
            "```",
        ]
    return [f"- {key}: `{_escape_inline(value)}`"]


def _format_edge(direction: str, edge: Mapping[str, object]) -> str:
    """Format one canonical edge as an explicit relationship line.

    Category: Document rendering/data structuring.
    Consumed by: _render_card().
    Why: makes source/target direction, edge type, and confidence visible in a
    predictable markdown shape.
    """

    edge_type = edge.get("edge_type") or "RELATED_TO"
    if direction == "outgoing":
        other = edge.get("target_id")
        arrow = "->"
    else:
        other = edge.get("source_id")
        arrow = "<-"
    confidence = edge.get("confidence")
    suffix = f" confidence=`{_escape_inline(confidence)}`" if confidence not in (None, "") else ""
    return f"- {direction} `{_escape_inline(edge_type)}` {arrow} `{_escape_inline(other)}`{suffix}"


def estimate_tokens(text: str) -> int:
    """Return a conservative token estimate without depending on a tokenizer.

    Category: Document rendering/data structuring.
    Consumed by: shape_canonical_dataset().
    Why: shaping needs a cheap local approximation to keep packs near the target
    size without adding tokenizer dependencies.
    """

    if not text:
        return 0
    by_chars = (len(text) + 3) // 4
    by_pieces = len(TOKEN_RE.findall(text))
    return max(by_chars, by_pieces)


def _body_token_limit(max_tokens: int) -> int:
    """Reserve a small budget for pack frontmatter/header text.

    Category: Document rendering/data structuring.
    Consumed by: shape_canonical_dataset().
    Why: the token target applies to the full markdown file, not just card body
    text.
    """

    header_budget = min(200, max_tokens // 5)
    return max_tokens - header_budget


def _edges_by(
    edges: Iterable[Mapping[str, object]],
    key: str,
) -> DefaultDict[str, List[Mapping[str, object]]]:
    """Group edges by source or target id and sort for stable markdown output.

    Category: Document rendering/data structuring.
    Consumed by: shape_canonical_dataset().
    Why: each rendered card needs quick access to its incoming and outgoing
    canonical relationships.
    """

    grouped: DefaultDict[str, List[Mapping[str, object]]] = defaultdict(list)
    for edge in edges:
        value = edge.get(key)
        if value:
            grouped[str(value)].append(edge)
    for edge_list in grouped.values():
        edge_list.sort(
            key=lambda item: (
                str(item.get("edge_type")),
                str(item.get("source_id")),
                str(item.get("target_id")),
            )
        )
    return grouped


def _batches(items: Sequence[Path], size: int) -> Iterable[Sequence[Path]]:
    """Yield fixed-size slices for upload batching.

    Category: File/data helper.
    Consumed by: add_documents().
    Why: Cognee add uploads are easier to observe and retry in bounded batches.
    """

    for index in range(0, len(items), size):
        yield items[index:index + size]


def _load_jsonl(path: Path) -> List[Mapping[str, object]]:
    """Load non-empty JSONL records from a canonical artifact file.

    Category: File/data helper.
    Consumed by: shape_canonical_dataset().
    Why: canonical cards and edges are stored as JSONL source artifacts.
    """

    if not path.exists():
        raise RuntimeError(f"Missing {path}")
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_json(record: Mapping[str, object], path: Path) -> None:
    """Write one deterministic JSON object for manifests.

    Category: File/data helper.
    Consumed by: shape_canonical_dataset().
    Why: the shaping manifest should be stable, readable, and reproducible.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(records: Iterable[Mapping[str, object]], path: Path) -> None:
    """Write deterministic JSONL metadata records.

    Category: File/data helper.
    Consumed by: shape_canonical_dataset().
    Why: per-pack metadata can be inspected or streamed line by line.
    """

    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def _format_response(value: object) -> str:
    """Return compact Cognee API output for progress/status messages.

    Category: HTTP/response helper.
    Consumed by: add_documents(), cognify_dataset().
    Why: normal runs need concise API feedback without dumping full nested JSON
    for every add or Cognify response.
    """

    if not isinstance(value, Mapping):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    parts = []
    for key in ("status", "dataset_name", "pipeline_run_id"):
        item = value.get(key)
        if item:
            parts.append(f"{key}={item}")
    ingestion_info = value.get("data_ingestion_info")
    if isinstance(ingestion_info, list):
        parts.append(f"items={len(ingestion_info)}")
    return ", ".join(parts) if parts else json.dumps(value, ensure_ascii=False, sort_keys=True)


def _pipeline_run_ids(value: object) -> List[str]:
    """Collect pipeline run ids from nested Cognee API responses.

    Category: HTTP/response helper.
    Consumed by: wait_for_cognify_log_completion().
    Why: Cognify responses can be keyed by dataset id, so the id may appear
    one or more levels down.
    """

    ids: List[str] = []

    def visit(item: object) -> None:
        if isinstance(item, Mapping):
            raw = item.get("pipeline_run_id")
            if raw:
                ids.append(str(raw))
            for nested in item.values():
                visit(nested)
        elif isinstance(item, list):
            for nested in item:
                visit(nested)

    visit(value)
    return sorted(set(ids))


def _docker_logs_since(container: str, since: str) -> str:
    """Return Docker logs for a container since an RFC3339 timestamp.

    Category: External boundary helper.
    Consumed by: wait_for_cognify_log_completion().
    Why: the local Cognee status endpoint can stay stale after completion, but
    the Docker logs reliably emit the pipeline completion line.
    """

    try:
        result = subprocess.run(
            ["docker", "logs", "--since", since, "--tail", "500", container],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise RuntimeError(f"Unable to run docker logs for Cognify completion: {exc}") from exc
    output = (result.stdout or "") + (result.stderr or "")
    if result.returncode != 0:
        raise RuntimeError(f"Unable to read Docker logs for {container}: {output.strip()}")
    return output


def _count_markdown_files(documents_dir: Path) -> int:
    """Count markdown documents in an existing shaped export directory.

    Category: File/data helper.
    Consumed by: main().
    Why: skip-shape mode reports the upload surface before add starts.
    """

    return len(list(documents_dir.glob("*.md"))) if documents_dir.exists() else 0


def _escape_inline(value: object) -> str:
    """Avoid breaking markdown backtick spans in generated scalar fields.

    Category: File/data helper.
    Consumed by: _format_field(), _format_edge().
    Why: canonical values should remain readable without corrupting inline-code
    formatting.
    """

    return str(value).replace("`", "'")


def _escape_frontmatter(value: str) -> str:
    """Escape values embedded in quoted YAML frontmatter strings.

    Category: File/data helper.
    Consumed by: _render_pack().
    Why: pack-level canonical ids are written inside quoted frontmatter values.
    """

    return value.replace("\\", "\\\\").replace('"', '\\"')


if __name__ == "__main__":
    raise SystemExit(main())
