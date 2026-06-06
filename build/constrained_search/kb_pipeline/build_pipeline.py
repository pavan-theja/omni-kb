from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .catalog_builder import build_catalogs
from .ingestion_batches import DATASET_MODE_CHOICES, build_add_batches, build_cognify_batches
from .markdown_parser import parse_source_tree
from .normalizer import normalize_cards, normalize_edges
from .readiness import build_readiness_pack
from .render_docs import render_docs
from .slice_profiles import FULL_PROFILE, apply_slice_profile, canonical_profile
from .utils import write_json
from .validator import validate_cards


def build_refactored_v2_pack(
    *,
    source_dir: Path,
    output_dir: Path,
    dataset_prefix: str,
    max_docs_per_add_batch: int,
    max_datasets_per_cognify_batch: int,
    clean: bool,
    profile: str = FULL_PROFILE,
    dataset_mode: str = "single",
) -> dict[str, Any]:
    if dataset_mode not in DATASET_MODE_CHOICES:
        raise ValueError(f"dataset_mode must be one of {DATASET_MODE_CHOICES}")

    profile = canonical_profile(profile)
    if clean and output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_cards, raw_edges, parse_errors = parse_source_tree(source_dir)
    cards = normalize_cards(raw_cards)
    edges = normalize_edges(raw_edges)
    cards, edges, slice_manifest = apply_slice_profile(cards, edges, profile=profile)
    validation = validate_cards(cards, edges)
    doc_manifest = render_docs(cards, output_dir)
    catalog_manifest = build_catalogs(cards, edges, output_dir)
    add_batches = build_add_batches(
        doc_manifest,
        output_dir,
        dataset_prefix=dataset_prefix,
        max_docs_per_batch=max_docs_per_add_batch,
        dataset_mode=dataset_mode,
    )
    cognify_batches = build_cognify_batches(
        add_batches,
        output_dir,
        max_datasets_per_batch=max_datasets_per_cognify_batch,
    )
    readiness = build_readiness_pack(
        cards=cards,
        edges=edges,
        parse_errors=parse_errors,
        validation=validation,
        catalog_manifest=catalog_manifest,
        doc_manifest=doc_manifest,
        add_batches=add_batches,
        cognify_batches=cognify_batches,
        output_dir=output_dir,
    )

    manifest = {
        "build_mode": "refactored_v2_constrained_search_build_only",
        "profile": profile,
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "dataset_prefix": dataset_prefix,
        "dataset_mode": dataset_mode,
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "parse_error_count": len(parse_errors),
        "validation": validation,
        "catalog_manifest": catalog_manifest,
        "card_count": len(cards),
        "edge_count": len(edges),
        "doc_count": len(doc_manifest),
        "add_batch_count": len(add_batches),
        "cognify_batch_count": len(cognify_batches),
        "add_batching_rule": "dataset_plus_identical_nodeset_signature",
        "cognify_batching_rule": "dataset_batches_after_all_adds_complete",
        "slice_manifest": slice_manifest,
        "readiness": readiness,
    }
    write_json(output_dir / "parse_errors.json", parse_errors)
    write_json(output_dir / "slice_manifest.json", slice_manifest)
    write_json(output_dir / "pack_manifest.json", manifest)
    return manifest


def stdout_summary(manifest: dict[str, Any]) -> dict[str, Any]:
    validation = manifest.get("validation") if isinstance(manifest.get("validation"), dict) else {}
    catalog = manifest.get("catalog_manifest") if isinstance(manifest.get("catalog_manifest"), dict) else {}
    readiness = manifest.get("readiness") if isinstance(manifest.get("readiness"), dict) else {}
    gates = readiness.get("gates") if isinstance(readiness.get("gates"), dict) else {}
    return {
        "build_mode": manifest.get("build_mode"),
        "profile": manifest.get("profile"),
        "source_dir": manifest.get("source_dir"),
        "output_dir": manifest.get("output_dir"),
        "dataset_mode": manifest.get("dataset_mode"),
        "card_count": manifest.get("card_count"),
        "edge_count": manifest.get("edge_count"),
        "parse_error_count": manifest.get("parse_error_count"),
        "validation_ok": validation.get("ok"),
        "validation_error_count": len(validation.get("errors") or []),
        "validation_warning_count": len(validation.get("warnings") or []),
        "runtime_binding_count": catalog.get("runtime_binding_count"),
        "active_runtime_binding_count": catalog.get("active_runtime_binding_count"),
        "blocked_runtime_binding_count": catalog.get("blocked_runtime_binding_count"),
        "deferred_runtime_binding_count": catalog.get("deferred_runtime_binding_count"),
        "table_count": catalog.get("table_count"),
        "doc_count": manifest.get("doc_count"),
        "add_batch_count": manifest.get("add_batch_count"),
        "cognify_batch_count": manifest.get("cognify_batch_count"),
        "packaging_ready_for_cognee_add": gates.get("packaging_ready_for_cognee_add"),
        "contract_validation_ready": gates.get("contract_validation_ready"),
        "runtime_search_ready": gates.get("runtime_search_ready"),
        "readiness_dir": readiness.get("readiness_dir"),
    }
