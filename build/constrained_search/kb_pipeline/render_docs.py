from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .utils import slugify, stable_short_hash


def render_docs(cards: list[dict[str, Any]], output_dir: Path) -> list[dict[str, Any]]:
    out_dir = output_dir / "cognee_docs" / "cards"
    out_dir.mkdir(parents=True, exist_ok=True)
    manifest: list[dict[str, Any]] = []
    for card in cards:
        cid = str(card.get("canonical_id"))
        path = out_dir / f"{slugify(cid)}__{stable_short_hash(cid)}.md"
        path.write_text(render_card_doc(card), encoding="utf-8")
        manifest.append(
            {
                "canonical_id": cid,
                "card_type": card.get("card_type"),
                "doc_path": str(path),
                "node_sets": card.get("ingestion_node_sets") or [],
                "source_layer": (card.get("_meta") or {}).get("pack_layer_hint"),
            }
        )
    return manifest


def render_card_doc(card: dict[str, Any]) -> str:
    safe = {key: value for key, value in card.items() if key != "_meta"}
    cid = card.get("canonical_id", "unknown")
    ctype = card.get("card_type", "unknown")
    title = card.get("canonical_name") or card.get("name") or cid
    lines = [
        f"# {title}",
        "",
        "## Canonical identity",
        f"- canonical_id: `{cid}`",
        f"- card_type: `{ctype}`",
        "",
        "## Cognee NodeSets",
    ]
    for node_set in card.get("ingestion_node_sets") or []:
        lines.append(f"- `{node_set}`")
    lines.extend(["", "## Canonical card YAML", "```yaml"])
    lines.append(yaml.safe_dump({"canonical_card": safe}, sort_keys=False, allow_unicode=True))
    lines.extend(["```", ""])
    return "\n".join(lines)

