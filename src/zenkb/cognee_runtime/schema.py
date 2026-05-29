from __future__ import annotations

import json
from pathlib import Path
from typing import Optional


def load_optional_json(path: Optional[Path]) -> Optional[dict]:
    if not path:
        return None
    if not path.exists():
        print(f"Warning: graph model file not found, skipping: {path}", flush=True)
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid graph model JSON {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise RuntimeError(f"Graph model must be a JSON object: {path}")
    return value


def validate_graph_model(value: dict, path: Path) -> None:
    title = value.get("title")
    if not isinstance(title, str) or not title.strip():
        raise RuntimeError(
            f"Graph model must be a JSON Schema-like object with a non-empty top-level title: {path}"
        )
    model_type = value.get("type")
    if model_type != "object":
        raise RuntimeError(f"Graph model top-level type must be object: {path}")


def load_optional_text(path: Optional[Path]) -> str:
    if not path:
        return ""
    if not path.exists():
        print(f"Warning: custom prompt file not found, skipping: {path}", flush=True)
        return ""
    return path.read_text(encoding="utf-8").strip()

