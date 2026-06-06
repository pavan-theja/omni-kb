from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable


def read_json(path: str | Path, default: Any = None) -> Any:
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    p = Path(path)
    if not p.exists():
        return []
    rows: list[dict[str, Any]] = []
    with p.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Invalid JSON on {p}:{line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"Expected object on {p}:{line_number}")
            rows.append(value)
    return rows


def write_json(path: str | Path, value: Any) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def jsonable(value: Any) -> Any:
    try:
        json.dumps(value)
        return value
    except TypeError:
        return repr(value)


def result_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if hasattr(value, "model_dump"):
        return result_text(value.model_dump(mode="json"))
    if isinstance(value, dict):
        return "\n".join(result_text(item) for item in value.values())
    if isinstance(value, list):
        return "\n".join(result_text(item) for item in value)
    return repr(value)


def unique_in_order(values: Iterable[str]) -> list[str]:
    out: list[str] = []
    for value in values:
        if value and value not in out:
            out.append(value)
    return out


def node_set_map(node_sets: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for raw in node_sets:
        text = str(raw)
        if ":" not in text:
            out.setdefault("__malformed__", []).append(text)
            continue
        key, value = text.split(":", 1)
        out.setdefault(key, []).append(value)
    return out


def first_node_set(node_sets: list[str], key: str) -> str | None:
    values = node_set_map(node_sets).get(key) or []
    return values[0] if values else None

