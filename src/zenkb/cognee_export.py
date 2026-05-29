from __future__ import annotations

import shutil
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import DefaultDict, Dict, Iterable, List, Mapping, Sequence

from .io_utils import write_json, write_jsonl


FRONTMATTER_FIELDS = (
    "canonical_id",
    "card_type",
    "status",
    "confidence",
    "review_status",
    "version",
)

SEARCH_FIELD_CANDIDATES = (
    "tenant_name",
    "tenant_code",
    "group_name",
    "platform_name",
    "platform_type",
    "context_name",
    "source_context_code",
    "account_name",
    "account_type",
    "source_account_identifier",
    "scope_name",
    "binding_name",
    "binding_type",
    "table_name",
    "full_reference",
    "schema",
    "business_purpose",
    "grain",
    "column_name",
    "business_meaning",
    "semantic_roles",
    "domain_name",
    "metric_name",
    "business_definition",
    "business_concepts",
    "implementation_name",
    "metric_id",
    "base_tables",
    "formula_description",
    "formula_sql",
    "template_name",
    "process_name",
    "profile_name",
    "side_name",
    "unit_name",
    "logic_name",
    "category_name",
    "variant_name",
    "pattern_name",
    "rule_name",
    "rule_type",
    "rule_statement",
    "test_name",
    "test_type",
    "aliases",
    "column_ids",
    "implementation_ids",
    "metric_implementation_ids",
    "relationship_ids",
    "business_flow_binding_ids",
    "tags",
)


@dataclass(frozen=True)
class CogneeExportResult:
    document_count: int
    metadata_count: int
    output_dir: str
    manifest_path: str


def export_cognee(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
    output_dir: Path,
    clean: bool = True,
) -> CogneeExportResult:
    if clean and output_dir.exists():
        _clean_output_dir(output_dir)

    outgoing = _edges_by(edges, "source_id")
    incoming = _edges_by(edges, "target_id")
    metadata_records: List[Dict[str, object]] = []

    documents_dir = output_dir / "documents"
    for card in sorted(cards, key=lambda item: str(item.get("canonical_id"))):
        card_type = str(card.get("card_type"))
        canonical_id = str(card.get("canonical_id"))
        doc_path = documents_dir / card_type / f"{_file_slug(canonical_id)}.md"
        markdown = render_cognee_document(
            card,
            outgoing.get(canonical_id, []),
            incoming.get(canonical_id, []),
        )
        doc_path.parent.mkdir(parents=True, exist_ok=True)
        doc_path.write_text(markdown, encoding="utf-8")
        metadata_records.append(_metadata_record(card, doc_path, output_dir))

    write_jsonl(metadata_records, output_dir / "metadata.jsonl")
    manifest = _manifest(cards, edges, metadata_records)
    manifest_path = output_dir / "manifest.json"
    write_json(manifest, manifest_path)

    return CogneeExportResult(
        document_count=len(cards),
        metadata_count=len(metadata_records),
        output_dir=str(output_dir),
        manifest_path=str(manifest_path),
    )


def render_cognee_document(
    card: Mapping[str, object],
    outgoing_edges: Sequence[Mapping[str, object]],
    incoming_edges: Sequence[Mapping[str, object]],
) -> str:
    lines: List[str] = []
    lines.extend(_frontmatter(card))
    lines.append("")
    lines.append(f"# {card.get('name') or card.get('canonical_id')}")
    lines.append("")
    lines.append(str(card.get("description") or ""))
    lines.append("")
    lines.append("## Card")
    lines.append("")
    lines.append(f"- canonical_id: `{card.get('canonical_id')}`")
    lines.append(f"- card_type: `{card.get('card_type')}`")
    lines.append(f"- status: `{card.get('status')}`")
    lines.append(f"- confidence: `{card.get('confidence')}`")

    key_fields = _key_fields(card)
    if key_fields:
        lines.append("")
        lines.append("## Retrieval Fields")
        lines.append("")
        for key, value in key_fields.items():
            lines.append(f"- {key}: {_format_inline(value)}")

    if outgoing_edges or incoming_edges:
        lines.append("")
        lines.append("## Relationships")
        lines.append("")
        for edge in outgoing_edges:
            lines.append(
                f"- outgoing `{edge.get('edge_type')}` -> `{edge.get('target_id')}`"
            )
        for edge in incoming_edges:
            lines.append(
                f"- incoming `{edge.get('edge_type')}` <- `{edge.get('source_id')}`"
            )

    evidence_refs = card.get("evidence_refs") or []
    if isinstance(evidence_refs, list) and evidence_refs:
        lines.append("")
        lines.append("## Evidence")
        lines.append("")
        for ref in evidence_refs[:10]:
            if not isinstance(ref, Mapping):
                continue
            source_doc = ref.get("source_doc")
            chunk_id = ref.get("chunk_id")
            source_span = ref.get("source_span")
            lines.append(f"- `{source_doc}` `{source_span}` chunk `{chunk_id}`")
        if len(evidence_refs) > 10:
            lines.append(f"- plus {len(evidence_refs) - 10} additional evidence refs")

    lines.append("")
    return "\n".join(lines)


def _frontmatter(card: Mapping[str, object]) -> List[str]:
    lines = ["---"]
    for field in FRONTMATTER_FIELDS:
        lines.append(f"{field}: {_yaml_scalar(card.get(field))}")
    source_documents = card.get("source_documents") or []
    tags = card.get("tags") or []
    lines.append("source_documents:")
    for item in source_documents if isinstance(source_documents, list) else [source_documents]:
        lines.append(f"  - {_yaml_scalar(item)}")
    lines.append("tags:")
    for item in tags if isinstance(tags, list) else [tags]:
        lines.append(f"  - {_yaml_scalar(item)}")
    lines.append("---")
    return lines


def _key_fields(card: Mapping[str, object]) -> Dict[str, object]:
    fields: Dict[str, object] = {}
    for key in SEARCH_FIELD_CANDIDATES:
        value = card.get(key)
        if value not in (None, "", []):
            fields[key] = value
    return fields


def _metadata_record(
    card: Mapping[str, object],
    doc_path: Path,
    output_dir: Path,
) -> Dict[str, object]:
    return {
        "canonical_id": card.get("canonical_id"),
        "card_type": card.get("card_type"),
        "status": card.get("status"),
        "confidence": card.get("confidence"),
        "document_path": doc_path.relative_to(output_dir).as_posix(),
        "source_documents": card.get("source_documents") or [],
        "tags": card.get("tags") or [],
    }


def _manifest(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
    metadata_records: Sequence[Mapping[str, object]],
) -> Dict[str, object]:
    card_types = Counter(str(card.get("card_type")) for card in cards)
    return {
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "generator": "zenkb.cognee_export",
        "source_artifacts": {
            "cards": "canonical/cards.jsonl",
            "edges": "canonical/edges.jsonl",
        },
        "counts": {
            "cards": len(cards),
            "edges": len(edges),
            "documents": len(metadata_records),
            "metadata_records": len(metadata_records),
        },
        "card_types": dict(sorted(card_types.items())),
        "policy": {
            "one_document_per_card": True,
            "raw_chunks_embedded": False,
            "evidence_refs_included": True,
            "edge_summaries_included": True,
        },
    }


def _edges_by(
    edges: Iterable[Mapping[str, object]],
    key: str,
) -> DefaultDict[str, List[Mapping[str, object]]]:
    grouped: DefaultDict[str, List[Mapping[str, object]]] = defaultdict(list)
    for edge in edges:
        grouped[str(edge.get(key))].append(edge)
    for edge_list in grouped.values():
        edge_list.sort(
            key=lambda item: (
                str(item.get("edge_type")),
                str(item.get("source_id")),
                str(item.get("target_id")),
            )
        )
    return grouped


def _clean_output_dir(output_dir: Path) -> None:
    for path in (output_dir / "documents", output_dir / "metadata.jsonl", output_dir / "manifest.json"):
        if path.is_dir():
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()


def _format_inline(value: object) -> str:
    if isinstance(value, list):
        return ", ".join(f"`{item}`" for item in value)
    if isinstance(value, Mapping):
        return "`" + ", ".join(f"{key}={val}" for key, val in value.items()) + "`"
    return f"`{value}`"


def _yaml_scalar(value: object) -> str:
    if value is None:
        return '""'
    text = str(value).replace('"', '\\"')
    return f'"{text}"'


def _file_slug(canonical_id: str) -> str:
    return canonical_id.replace(".", "__").replace("/", "_")
