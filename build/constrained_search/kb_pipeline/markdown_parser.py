from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from .utils import domain_family_for_path, layer_for_path


YAML_FENCE_RE = re.compile(r"```yaml\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def parse_source_tree(source_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    cards: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    for path in sorted(source_dir.rglob("*.md")):
        file_cards, file_edges, file_errors = parse_markdown_file(path, source_dir)
        cards.extend(file_cards)
        edges.extend(file_edges)
        errors.extend(file_errors)
    return cards, edges, errors


def parse_markdown_file(path: Path, source_dir: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8")
    cards: list[dict[str, Any]] = []
    edges: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    layer = layer_for_path(path, source_dir)
    domain_family = domain_family_for_path(path, source_dir)
    for block_index, match in enumerate(YAML_FENCE_RE.finditer(text)):
        raw = match.group(1)
        try:
            data = yaml.safe_load(raw)
        except Exception as exc:  # noqa: BLE001
            errors.append({"source_path": str(path), "block_index": block_index, "error": f"yaml_parse_error: {exc}"})
            continue
        if not isinstance(data, dict):
            continue
        if isinstance(data.get("canonical_card"), dict):
            card = dict(data["canonical_card"])
            card["_meta"] = {
                "source_path": str(path),
                "source_filename": path.name,
                "source_family": domain_family,
                "block_index": block_index,
                "pack_layer_hint": layer,
            }
            cards.append(card)
        elif isinstance(data.get("canonical_edge"), dict):
            edge = dict(data["canonical_edge"])
            edge["_meta"] = {
                "source_path": str(path),
                "source_filename": path.name,
                "source_family": domain_family,
                "block_index": block_index,
                "pack_layer_hint": layer,
            }
            edges.append(edge)
    return cards, edges, errors

