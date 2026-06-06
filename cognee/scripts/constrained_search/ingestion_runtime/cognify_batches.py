#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import importlib
import inspect
import json
import os
import sys
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence


CONSTRAINED_SEARCH_DIR = Path(__file__).resolve().parents[1]
if str(CONSTRAINED_SEARCH_DIR) not in sys.path:
    sys.path.insert(0, str(CONSTRAINED_SEARCH_DIR))

from runtime_env import PROVIDER_CHOICES, REPO_ROOT, configure_cognee_environment  # noqa: E402


DEFAULT_PACK_DIR = REPO_ROOT / "build" / "constrained_search" / "build_marketplace_runtime"
DEFAULT_ENV_FILE = REPO_ROOT / "cognee" / ".env"


class CogneeIntegrationError(RuntimeError):
    pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run SDK cognee.cognify for constrained-search dataset batches.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        results = asyncio.run(run(args))
    except (CogneeIntegrationError, RuntimeError, ValueError) as exc:
        print(f"constrained cognify failed: {exc}", file=sys.stderr)
        return 1

    failed = [row for row in results if row.get("status") == "failed"]
    if args.dry_run:
        print(f"cognify_batches_dry_run={len(results)} failed={len(failed)}")
        return 1 if failed else 0
    print(f"cognify_batches_run={len(results)} failed={len(failed)}")
    return 1 if failed else 0


async def run(args: argparse.Namespace) -> list[dict[str, Any]]:
    pack_dir = resolve_pack_dir(args.pack_dir)
    batches = read_jsonl(pack_dir / "cognee_ingestion" / "cognify_batches.jsonl")
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("--limit must be >= 1")
        batches = batches[: args.limit]
    if not batches:
        raise RuntimeError(f"No cognify batches found under {pack_dir}")

    prepared = [prepare_cognify_batch(batch) for batch in batches]
    validation_failures = [row for row in prepared if row.get("status") == "failed"]
    if args.dry_run:
        return prepared
    if validation_failures:
        write_jsonl(pack_dir / "cognee_ingestion" / "cognify_manifest.jsonl", prepared)
        return prepared

    configure_cognee_environment(pack_dir, env_file=args.env_file, provider=args.provider)
    cognify_fn = getattr(load_cognee_sdk(), "cognify", None)
    if cognify_fn is None:
        raise CogneeIntegrationError("Imported Cognee SDK does not expose cognee.cognify.")

    results: list[dict[str, Any]] = []
    for row in prepared:
        results.append(await cognify_one_batch(cognify_fn, row))
    write_jsonl(pack_dir / "cognee_ingestion" / "cognify_manifest.jsonl", results)
    return results


async def cognify_one_batch(cognify_fn: Any, row: dict[str, Any]) -> dict[str, Any]:
    try:
        result = await invoke_maybe_async(cognify_fn, {"datasets": row["datasets"]})
        return {**row, "status": "cognified", "result": jsonable(result)}
    except Exception as exc:  # noqa: BLE001
        return {**row, "status": "failed", "error": repr(exc)}


def prepare_cognify_batch(batch: dict[str, Any]) -> dict[str, Any]:
    datasets = batch.get("datasets") or []
    row = {
        "batch_id": batch.get("batch_id"),
        "dataset_count": batch.get("dataset_count") or len(datasets),
        "datasets": list(datasets) if isinstance(datasets, list) else [],
        "status": "validated",
    }
    errors: list[str] = []
    if not row["batch_id"]:
        errors.append("missing_batch_id")
    if not row["datasets"]:
        errors.append("missing_datasets")
    if int(row["dataset_count"] or 0) != len(row["datasets"]):
        errors.append(f"dataset_count_mismatch:{row['dataset_count']}!={len(row['datasets'])}")
    if errors:
        row["status"] = "failed"
        row["errors"] = errors
    return row


async def invoke_maybe_async(fn: Any, kwargs: dict[str, Any]) -> Any:
    if inspect.iscoroutinefunction(fn):
        result = fn(**kwargs)
    else:
        result = await asyncio.to_thread(fn, **kwargs)
    if inspect.isawaitable(result):
        return await result
    return result


def load_cognee_sdk() -> Any:
    saved_path = list(sys.path)
    try:
        sys.path = sdk_import_path(saved_path)
        module = importlib.import_module("cognee")
    except Exception as exc:  # noqa: BLE001
        raise CogneeIntegrationError("Cognee SDK is not importable in this environment.") from exc
    finally:
        sys.path = saved_path
    return module


def sdk_import_path(paths: Iterable[str]) -> list[str]:
    filtered: list[str] = []
    for entry in paths:
        resolved = Path(entry or os.getcwd()).resolve()
        if resolved == REPO_ROOT:
            continue
        filtered.append(entry)
    return filtered


def resolve_pack_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise RuntimeError(f"Missing JSONL file: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Invalid JSON on {path}:{line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"Expected object on {path}:{line_number}")
            rows.append(value)
    return rows


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def jsonable(value: Any) -> Any:
    try:
        json.dumps(value)
        return value
    except TypeError:
        return repr(value)


if __name__ == "__main__":
    raise SystemExit(main())
