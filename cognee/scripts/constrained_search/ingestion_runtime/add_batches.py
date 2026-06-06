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
    parser = argparse.ArgumentParser(description="Run SDK cognee.add for NodeSet-homogeneous constrained-search batches.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        results = asyncio.run(run(args))
    except (CogneeIntegrationError, RuntimeError, ValueError) as exc:
        print(f"constrained add failed: {exc}", file=sys.stderr)
        return 1

    failed = [row for row in results if row.get("status") == "failed"]
    if args.dry_run:
        print(f"add_batches_dry_run={len(results)} failed={len(failed)}")
        return 1 if failed else 0
    print(f"add_batches_run={len(results)} failed={len(failed)}")
    return 1 if failed else 0


async def run(args: argparse.Namespace) -> list[dict[str, Any]]:
    if args.concurrency < 1:
        raise ValueError("--concurrency must be >= 1")
    pack_dir = resolve_pack_dir(args.pack_dir)
    batches = read_jsonl(pack_dir / "cognee_ingestion" / "add_batches.jsonl")
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("--limit must be >= 1")
        batches = batches[: args.limit]
    if not batches:
        raise RuntimeError(f"No add batches found under {pack_dir}")

    prepared = [prepare_add_batch(batch, pack_dir=pack_dir) for batch in batches]
    validation_failures = [row for row in prepared if row.get("status") == "failed"]
    if args.dry_run:
        return prepared
    if validation_failures:
        write_jsonl(pack_dir / "cognee_ingestion" / "add_manifest.jsonl", prepared)
        return prepared

    configure_cognee_environment(pack_dir, env_file=args.env_file, provider=args.provider)
    add_fn = getattr(load_cognee_sdk(), "add", None)
    if add_fn is None:
        raise CogneeIntegrationError("Imported Cognee SDK does not expose cognee.add.")
    if not callable_accepts_kwarg(add_fn, "node_set"):
        raise CogneeIntegrationError(
            "Imported cognee.add does not accept node_set. "
            "Use a Cognee SDK/runtime version with NodeSet add support before live constrained ingestion."
        )

    sem = asyncio.Semaphore(args.concurrency)

    async def _one(row: dict[str, Any]) -> dict[str, Any]:
        async with sem:
            return await add_one_batch(add_fn, row)

    results = list(await asyncio.gather(*[_one(row) for row in prepared]))
    write_jsonl(pack_dir / "cognee_ingestion" / "add_manifest.jsonl", results)
    return results


async def add_one_batch(add_fn: Any, row: dict[str, Any]) -> dict[str, Any]:
    kwargs = {
        "data": row["doc_paths"],
        "dataset_name": row["dataset_name"],
        "node_set": row["node_sets"],
    }
    try:
        result = await invoke_maybe_async(add_fn, kwargs)
        return {**row, "status": "added", "result": jsonable(result)}
    except Exception as exc:  # noqa: BLE001
        return {**row, "status": "failed", "error": repr(exc)}


def prepare_add_batch(batch: dict[str, Any], *, pack_dir: Path) -> dict[str, Any]:
    row = {
        "batch_id": batch.get("batch_id"),
        "dataset_name": batch.get("dataset_name"),
        "doc_count": batch.get("doc_count"),
        "canonical_ids": list(batch.get("canonical_ids") or []),
        "node_sets": list(batch.get("node_sets") or []),
        "doc_paths": [],
        "status": "validated",
    }
    errors: list[str] = []
    if not row["batch_id"]:
        errors.append("missing_batch_id")
    if not row["dataset_name"]:
        errors.append("missing_dataset_name")
    if not row["node_sets"]:
        errors.append("missing_node_sets")

    doc_paths = batch.get("doc_paths") or []
    if not isinstance(doc_paths, list) or not doc_paths:
        errors.append("missing_doc_paths")
    else:
        for raw_path in doc_paths:
            path = resolve_doc_path(raw_path, pack_dir=pack_dir)
            if not path.exists():
                errors.append(f"doc_path_missing:{path}")
            row["doc_paths"].append(str(path))

    expected_doc_count = int(row["doc_count"] or len(row["doc_paths"]))
    if expected_doc_count != len(row["doc_paths"]):
        errors.append(f"doc_count_mismatch:{expected_doc_count}!={len(row['doc_paths'])}")

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


def callable_accepts_kwarg(fn: Any, key: str) -> bool:
    try:
        signature = inspect.signature(fn)
    except (TypeError, ValueError):
        return True
    for parameter in signature.parameters.values():
        if parameter.kind == inspect.Parameter.VAR_KEYWORD:
            return True
        if parameter.name == key:
            return True
    return False


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


def resolve_doc_path(value: Any, *, pack_dir: Path) -> Path:
    path = Path(str(value)).expanduser()
    if path.is_absolute():
        return path
    return (pack_dir / path).resolve()


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
