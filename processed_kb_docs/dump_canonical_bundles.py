#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, Optional, Sequence


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_CARDS = ROOT_DIR / "canonical" / "cards.jsonl"
DEFAULT_EDGES = ROOT_DIR / "canonical" / "edges.jsonl"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "cognee" / "bundled_export"
DEFAULT_BUNDLE_BY = "single"
DEFAULT_MAX_CARDS_PER_FILE = 0
DEFAULT_OVERLAP_CARDS = 0


SEARCH_FIELDS = (
    "canonical_id",
    "card_type",
    "name",
    "description",
    "tenant_id",
    "group_id",
    "platform_id",
    "platform_account_id",
    "platform_type",
    "table_id",
    "table_name",
    "full_reference",
    "column_name",
    "metric_id",
    "metric_name",
    "implementation_name",
    "formula_description",
    "formula_sql",
    "required_filters",
    "column_ids",
    "implementation_ids",
    "metric_implementation_ids",
    "relationship_ids",
    "business_definition",
    "business_meaning",
    "aliases",
    "status",
    "confidence",
    "review_status",
    "source_documents",
)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        description="Dump canonical cards/edges into fewer Cognee-ready bundle documents."
    )
    parser.add_argument("--cards", type=Path, default=DEFAULT_CARDS)
    parser.add_argument("--edges", type=Path, default=DEFAULT_EDGES)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--bundle-by",
        choices=("card_type", "single"),
        default=DEFAULT_BUNDLE_BY,
        help="Bundle all cards into one file, or split by card_type.",
    )
    parser.add_argument(
        "--max-cards-per-file",
        type=int,
        default=DEFAULT_MAX_CARDS_PER_FILE,
        help="Split large bundles after this many cards. Default 0 keeps bundled export to one add file.",
    )
    parser.add_argument(
        "--overlap-cards",
        type=int,
        default=DEFAULT_OVERLAP_CARDS,
        help="Repeat this many neighboring cards on each side of a split bundle.",
    )
    parser.add_argument("--no-clean", action="store_true", help="Do not clean output directory first.")
    args = parser.parse_args(argv)

    cards = _load_jsonl(args.cards)
    edges = _load_jsonl(args.edges)
    result = dump_canonical_bundles(
        cards,
        edges,
        args.output_dir,
        bundle_by=args.bundle_by,
        max_cards_per_file=args.max_cards_per_file,
        overlap_cards=args.overlap_cards,
        clean=not args.no_clean,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


def dump_canonical_bundles(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
    output_dir: Path,
    *,
    bundle_by: str = DEFAULT_BUNDLE_BY,
    max_cards_per_file: int = DEFAULT_MAX_CARDS_PER_FILE,
    overlap_cards: int = DEFAULT_OVERLAP_CARDS,
    clean: bool = True,
) -> Dict[str, object]:
    if max_cards_per_file < 0:
        raise ValueError("max_cards_per_file must be >= 0")
    if overlap_cards < 0:
        raise ValueError("overlap_cards must be >= 0")
    if max_cards_per_file == 0 and overlap_cards:
        raise ValueError("overlap_cards requires max_cards_per_file > 0")
    if clean and output_dir.exists():
        _clean_output_dir(output_dir)

    documents_dir = output_dir / "documents"
    outgoing = _edges_by(edges, "source_id")
    incoming = _edges_by(edges, "target_id")
    grouped = _group_cards(cards, bundle_by)
    metadata: List[Dict[str, object]] = []

    for group_key in sorted(grouped):
        group_cards = sorted(grouped[group_key], key=lambda card: str(card.get("canonical_id")))
        for part_index, batch in enumerate(
            _overlapping_batches(group_cards, max_cards_per_file, overlap_cards),
            start=1,
        ):
            filename = _bundle_filename(group_key, part_index, len(group_cards), max_cards_per_file)
            path = documents_dir / filename
            markdown = _render_bundle(
                group_key,
                batch["cards"],
                core_start=batch["core_start"],
                core_end=batch["core_end"],
                outgoing=outgoing,
                incoming=incoming,
                total_cards=len(group_cards),
                part_index=part_index,
                overlap_cards=overlap_cards,
            )
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(markdown, encoding="utf-8")
            metadata.append(
                {
                    "document_path": path.relative_to(output_dir).as_posix(),
                    "bundle_key": group_key,
                    "part_index": part_index,
                    "card_count": len(batch["cards"]),
                    "core_card_count": len(batch["core_cards"]),
                    "overlap_card_count": len(batch["overlap_cards"]),
                    "canonical_ids": [card.get("canonical_id") for card in batch["cards"]],
                    "core_canonical_ids": [card.get("canonical_id") for card in batch["core_cards"]],
                    "overlap_canonical_ids": [card.get("canonical_id") for card in batch["overlap_cards"]],
                }
            )

    _write_jsonl(metadata, output_dir / "metadata.jsonl")
    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source": "canonical",
        "bundle_by": bundle_by,
        "max_cards_per_file": max_cards_per_file,
        "overlap_cards": overlap_cards,
        "card_count": len(cards),
        "edge_count": len(edges),
        "document_count": len(metadata),
        "documents_dir": str(documents_dir),
    }
    _write_json(manifest, output_dir / "manifest.json")
    return manifest


def _render_bundle(
    group_key: str,
    cards: Sequence[Mapping[str, object]],
    *,
    core_start: int,
    core_end: int,
    outgoing: Mapping[str, Sequence[Mapping[str, object]]],
    incoming: Mapping[str, Sequence[Mapping[str, object]]],
    total_cards: int,
    part_index: int,
    overlap_cards: int,
) -> str:
    lines: List[str] = [
        "---",
        'source: "canonical"',
        f'bundle_key: "{_escape_frontmatter(group_key)}"',
        f"part_index: {part_index}",
        f"bundle_card_count: {len(cards)}",
        f"core_card_start_index: {core_start}",
        f"core_card_end_index: {core_end}",
        f"overlap_cards: {overlap_cards}",
        f"total_group_card_count: {total_cards}",
        "---",
        "",
        f"# Canonical Bundle: {group_key} part {part_index}",
        "",
        "This file is generated from canonical/cards.jsonl and canonical/edges.jsonl.",
        "Use canonical_id as the stable identity. Relationships listed here are explicit canonical edges.",
        "",
    ]
    for local_index, card in enumerate(cards):
        canonical_id = str(card.get("canonical_id") or "")
        card_position = "core" if core_start <= local_index < core_end else "overlap_context"
        lines.extend(
            [
                "---",
                "",
                f"## {canonical_id}",
                "",
                "### Card",
                "",
                f"- bundle_position: `{card_position}`",
            ]
        )
        for key in SEARCH_FIELDS:
            value = card.get(key)
            if value not in (None, "", []):
                lines.append(f"- {key}: {_format_inline(value)}")
        lines.append("")
        card_outgoing = outgoing.get(canonical_id, [])
        card_incoming = incoming.get(canonical_id, [])
        if card_outgoing or card_incoming:
            lines.extend(["### Relationships", ""])
            for edge in card_outgoing:
                lines.append(f"- outgoing `{edge.get('edge_type')}` -> `{edge.get('target_id')}`")
            for edge in card_incoming:
                lines.append(f"- incoming `{edge.get('edge_type')}` <- `{edge.get('source_id')}`")
            lines.append("")
    return "\n".join(lines)


def _group_cards(
    cards: Sequence[Mapping[str, object]],
    bundle_by: str,
) -> Dict[str, List[Mapping[str, object]]]:
    groups: Dict[str, List[Mapping[str, object]]] = defaultdict(list)
    if bundle_by == "single":
        for card in cards:
            groups["canonical_all"].append(card)
        return groups
    if bundle_by == "card_type":
        for card in cards:
            groups[_safe_part(str(card.get("card_type") or "unknown"))].append(card)
        return groups
    raise ValueError(f"unsupported bundle_by: {bundle_by}")


def _bundle_filename(group_key: str, part_index: int, group_size: int, max_cards_per_file: int) -> str:
    if max_cards_per_file == 0 or group_size <= max_cards_per_file:
        return f"{_safe_part(group_key)}.md"
    return f"{_safe_part(group_key)}__part_{part_index:03d}.md"


def _edges_by(edges: Sequence[Mapping[str, object]], key: str) -> Dict[str, List[Mapping[str, object]]]:
    grouped: Dict[str, List[Mapping[str, object]]] = defaultdict(list)
    for edge in edges:
        value = edge.get(key)
        if value:
            grouped[str(value)].append(edge)
    return grouped


def _overlapping_batches(
    items: Sequence[Mapping[str, object]],
    size: int,
    overlap: int,
) -> Iterator[Dict[str, object]]:
    if size == 0:
        yield {
            "cards": list(items),
            "core_cards": list(items),
            "overlap_cards": [],
            "core_start": 0,
            "core_end": len(items),
        }
        return
    for index in range(0, len(items), size):
        core_start = index
        core_end = min(index + size, len(items))
        window_start = max(0, core_start - overlap)
        window_end = min(len(items), core_end + overlap)
        cards = list(items[window_start:window_end])
        core_cards = list(items[core_start:core_end])
        overlap_set = {id(card) for card in core_cards}
        yield {
            "cards": cards,
            "core_cards": core_cards,
            "overlap_cards": [card for card in cards if id(card) not in overlap_set],
            "core_start": core_start - window_start,
            "core_end": core_end - window_start,
        }


def _format_inline(value: object) -> str:
    if isinstance(value, (dict, list)):
        return "`" + json.dumps(value, ensure_ascii=False, sort_keys=True) + "`"
    return "`" + str(value).replace("`", "'") + "`"


def _safe_part(value: str) -> str:
    safe = []
    for char in value.lower():
        if char.isalnum() or char in {"_", "-"}:
            safe.append(char)
        else:
            safe.append("_")
    return "".join(safe).strip("_") or "unknown"


def _escape_frontmatter(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _load_jsonl(path: Path) -> List[Dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def _write_json(record: Mapping[str, object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _write_jsonl(records: Iterable[Mapping[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def _clean_output_dir(output_dir: Path) -> None:
    if output_dir.exists():
        shutil.rmtree(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    raise SystemExit(main())
