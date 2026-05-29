from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, Mapping, Sequence


def write_json(record: Mapping[str, object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(record, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def write_jsonl(records: Iterable[Mapping[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def write_yaml_documents(records: Sequence[Mapping[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for index, record in enumerate(records):
            if index:
                handle.write("---\n")
            _write_yaml_value(record, handle, 0)


def _write_yaml_value(value: object, handle, indent: int) -> None:
    prefix = " " * indent
    if isinstance(value, Mapping):
        for key, child in value.items():
            if isinstance(child, (Mapping, list)):
                handle.write(f"{prefix}{key}:\n")
                _write_yaml_value(child, handle, indent + 2)
            else:
                handle.write(f"{prefix}{key}: {_format_scalar(child)}\n")
    elif isinstance(value, list):
        for item in value:
            if isinstance(item, (Mapping, list)):
                handle.write(f"{prefix}-\n")
                _write_yaml_value(item, handle, indent + 2)
            else:
                handle.write(f"{prefix}- {_format_scalar(item)}\n")
    else:
        handle.write(f"{prefix}{_format_scalar(value)}\n")


def _format_scalar(value: object) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    text = str(value)
    if not text:
        return '""'
    if "\n" in text:
        escaped = text.replace("\n", "\\n")
        return json.dumps(escaped, ensure_ascii=False)
    return json.dumps(text, ensure_ascii=False)
