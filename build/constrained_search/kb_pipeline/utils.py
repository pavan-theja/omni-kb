from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable


def layer_for_path(path: Path, source_dir: Path) -> str:
    parts = path.relative_to(source_dir).parts
    return "runtime" if parts and parts[0] == "client" else "semantic"


def domain_family_for_path(path: Path, source_dir: Path) -> str:
    folder = path.relative_to(source_dir).parts[0]
    return {
        "client": "client_runtime",
        "marketplaces": "marketplace",
        "logistics": "logistics",
        "oms": "oms",
        "wms": "wms",
        "bank": "bank_statement",
        "payment_gateway": "payment_gateway",
    }.get(folder, folder)


def scope_column_ids_for_binding(table_id: Any, scope_keys: Any) -> list[str]:
    ids: list[str] = []
    for scope in scope_keys if isinstance(scope_keys, list) else []:
        if not isinstance(scope, dict):
            continue
        col_id = scope.get("scope_column_id") or scope.get("column_id")
        if not col_id and table_id and scope.get("column"):
            col_id = f"column.{str(table_id).removeprefix('table.')}.{scope['column']}"
        if col_id:
            ids.append(str(col_id))
    return dedupe(ids)


def infer_table_id_from_column_id(column_id: str | None) -> str | None:
    if not column_id or not str(column_id).startswith("column."):
        return None
    parts = str(column_id).split(".")
    if len(parts) < 3:
        return None
    return "table." + ".".join(parts[1:-1])


def first_present(*values: Any) -> Any:
    for value in values:
        if value not in (None, "", []):
            return value
    return None


def listify(value: Any) -> list[Any]:
    if value in (None, ""):
        return []
    if isinstance(value, list):
        return value
    return [value]


def flatten_strings(value: Any) -> list[str]:
    out: list[str] = []
    if value is None:
        return out
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        for key, item in value.items():
            out.extend(flatten_strings(key))
            out.extend(flatten_strings(item))
        return out
    if isinstance(value, Iterable) and not isinstance(value, (bytes, bytearray)):
        for item in value:
            out.extend(flatten_strings(item))
        return out
    return [str(value)]


def stable_node_set_signature(node_sets: Iterable[str]) -> str:
    return "|".join(sorted(dedupe(str(item) for item in node_sets if item)))


def slugify(value: str, max_length: int = 180) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_.-]+", "_", value.strip()).strip("._-").lower()
    return (slug or "item")[:max_length]


def stable_short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]


def dedupe(values: Iterable[Any]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for value in values:
        if value in (None, "", []):
            continue
        text = str(value)
        if text not in seen:
            seen.add(text)
            out.append(text)
    return out


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")

