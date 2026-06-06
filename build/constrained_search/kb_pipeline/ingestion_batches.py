from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any

from .utils import dedupe, stable_node_set_signature, write_jsonl


DATASET_MODE_CHOICES = ("single", "layered")


def build_add_batches(
    doc_manifest: list[dict[str, Any]],
    output_dir: Path,
    *,
    dataset_prefix: str,
    max_docs_per_batch: int,
    dataset_mode: str = "single",
) -> list[dict[str, Any]]:
    if dataset_mode not in DATASET_MODE_CHOICES:
        raise ValueError(f"dataset_mode must be one of {DATASET_MODE_CHOICES}")

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in doc_manifest:
        dataset = dataset_name_for_manifest_row(row, dataset_prefix, dataset_mode=dataset_mode)
        signature = stable_node_set_signature(row.get("node_sets") or [])
        grouped[(dataset, signature)].append(row)

    batches: list[dict[str, Any]] = []
    batch_id = 0
    for (dataset, signature), rows in sorted(grouped.items()):
        for index in range(0, len(rows), max_docs_per_batch):
            chunk = rows[index : index + max_docs_per_batch]
            batch_id += 1
            batches.append(
                {
                    "batch_id": f"add_batch_{batch_id:05d}",
                    "dataset_name": dataset,
                    "node_set_signature": signature,
                    "node_sets": chunk[0].get("node_sets") or [],
                    "doc_paths": [row["doc_path"] for row in chunk],
                    "canonical_ids": [row["canonical_id"] for row in chunk],
                    "doc_count": len(chunk),
                    "batching_rule": "dataset_plus_identical_nodeset_signature",
                }
            )
    write_jsonl(output_dir / "cognee_ingestion" / "add_batches.jsonl", batches)
    return batches


def build_cognify_batches(
    add_batches: list[dict[str, Any]],
    output_dir: Path,
    *,
    max_datasets_per_batch: int,
) -> list[dict[str, Any]]:
    datasets = sorted({batch["dataset_name"] for batch in add_batches})
    batches: list[dict[str, Any]] = []
    batch_id = 0
    for index in range(0, len(datasets), max_datasets_per_batch):
        batch_id += 1
        chunk = datasets[index : index + max_datasets_per_batch]
        batches.append(
            {
                "batch_id": f"cognify_batch_{batch_id:05d}",
                "datasets": chunk,
                "dataset_count": len(chunk),
                "batching_rule": "dataset_batches_after_all_adds_complete",
            }
        )
    write_jsonl(output_dir / "cognee_ingestion" / "cognify_batches.jsonl", batches)
    return batches


def dataset_name_for_manifest_row(row: dict[str, Any], prefix: str, *, dataset_mode: str = "single") -> str:
    if dataset_mode == "single":
        return prefix

    layer = row.get("source_layer") or "semantic"
    if layer == "runtime":
        return f"{prefix}_runtime"
    return f"{prefix}_semantic"
