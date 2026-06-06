#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from kb_pipeline.build_pipeline import build_refactored_v2_pack, stdout_summary
from kb_pipeline.ingestion_batches import DATASET_MODE_CHOICES
from kb_pipeline.slice_profiles import FULL_PROFILE, MARKETPLACE_RUNTIME_PROFILE, PROFILE_CHOICES, canonical_profile


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE_DIR = REPO_ROOT / "raw" / "Source" / "refactored_v2"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "build" / "constrained_search" / "build"
DEFAULT_MARKETPLACE_RUNTIME_OUTPUT_DIR = REPO_ROOT / "build" / "constrained_search" / "build_marketplace_runtime"
DEFAULT_DATASET_PREFIX = "zen_csearch_refactored_v2"
DEFAULT_MARKETPLACE_RUNTIME_DATASET_PREFIX = "zen_csearch_refactored_v2_marketplace_runtime"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build constrained-search artifacts from raw/Source/refactored_v2.")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path)
    parser.add_argument("--dataset-prefix")
    parser.add_argument("--profile", choices=PROFILE_CHOICES, default=FULL_PROFILE)
    parser.add_argument("--dataset-mode", choices=DATASET_MODE_CHOICES, default="single")
    parser.add_argument("--max-docs-per-add-batch", type=int, default=50)
    parser.add_argument("--max-datasets-per-cognify-batch", type=int, default=1)
    parser.add_argument("--clean", action="store_true")
    args = parser.parse_args()
    profile = canonical_profile(args.profile)
    output_dir = args.output_dir or default_output_dir(profile)
    dataset_prefix = args.dataset_prefix or default_dataset_prefix(profile)

    manifest = build_refactored_v2_pack(
        source_dir=args.source_dir,
        output_dir=output_dir,
        dataset_prefix=dataset_prefix,
        max_docs_per_add_batch=args.max_docs_per_add_batch,
        max_datasets_per_cognify_batch=args.max_datasets_per_cognify_batch,
        clean=args.clean,
        profile=profile,
        dataset_mode=args.dataset_mode,
    )
    print(json.dumps(stdout_summary(manifest), indent=2, ensure_ascii=False, sort_keys=True))
    return 0


def default_output_dir(profile: str) -> Path:
    if profile == MARKETPLACE_RUNTIME_PROFILE:
        return DEFAULT_MARKETPLACE_RUNTIME_OUTPUT_DIR
    return DEFAULT_OUTPUT_DIR


def default_dataset_prefix(profile: str) -> str:
    if profile == MARKETPLACE_RUNTIME_PROFILE:
        return DEFAULT_MARKETPLACE_RUNTIME_DATASET_PREFIX
    return DEFAULT_DATASET_PREFIX


if __name__ == "__main__":
    raise SystemExit(main())
