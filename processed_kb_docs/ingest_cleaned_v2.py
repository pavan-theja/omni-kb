#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import logging
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, Iterable, Iterator, List, Mapping, MutableMapping, Optional, Sequence, Tuple

try:
    from tqdm.auto import tqdm as _tqdm
except ModuleNotFoundError:
    _tqdm = None


ROOT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE_DIR = ROOT_DIR / "raw" / "Source" / "cleaned"
DEFAULT_OUTPUT_DIR = ROOT_DIR / "processed_kb_docs" / "cleaned"

YAML_BLOCK_RE = re.compile(r"```yaml\s*\n(.*?)```", re.S)
FIRST_KEY_RE = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:", re.M)

CARD_TYPE_BY_PREFIX = {
    "account_data_binding": "account_data_binding",
    "business_flow_binding": "business_flow_binding",
    "business_process": "business_process",
    "business_scope_set": "business_scope_set",
    "column": "column",
    "domain": "domain",
    "execution_constraint_set": "execution_constraint_set",
    "formula_template": "formula_template",
    "group": "group",
    "matching_logic": "matching_logic",
    "metric": "metric",
    "metric_dependency": "metric_dependency",
    "metric_impl": "metric_implementation",
    "metric_implementation": "metric_implementation",
    "mismatch_category": "mismatch_category",
    "output_contract": "output_contract",
    "platform": "platform",
    "platform_account": "platform_account",
    "platform_context": "platform_context",
    "process_variant": "process_variant",
    "query_pattern": "query_pattern",
    "reconciliation_profile": "reconciliation_profile",
    "reconciliation_side": "reconciliation_side",
    "reconciliation_unit": "reconciliation_unit",
    "reconciliation_variant": "reconciliation_variant",
    "relationship": "relationship",
    "review_item": "review_item",
    "rule": "rule",
    "state_transition": "state_transition",
    "table": "table",
    "tenant": "tenant",
    "validation": "validation_test",
    "validation_test": "validation_test",
    "value_profile": "value_profile",
    "workflow_step": "workflow_step",
}

STATUS_MAP = {
    "accepted": "active",
    "active": "active",
    "candidate": "draft",
    "draft": "draft",
    "failed_or_partial": "draft",
    "open": "draft",
    "ready": "draft",
    "ready_for_review": "draft",
    "review_required": "draft",
    "blocked_or_review_required": "draft",
    "deprecated": "deprecated",
    "archived": "archived",
}

CONFIDENCE_MAP = {
    "curated": "curated",
    "high": "curated",
    "source_confirmed": "curated",
    "source_configured": "curated",
    "source_confirmed_context_missing": "inferred",
    "medium": "inferred",
    "inferred": "inferred",
    "low": "low_confidence",
    "low_confidence": "low_confidence",
    "experimental": "experimental",
    "unknown": "unknown",
}


@dataclass(frozen=True)
class ParsedYamlBlock:
    source_path: str
    line_number: int
    block_key: str
    data: Mapping[str, object]


def _progress(
    iterable: Iterable[object],
    *,
    desc: str,
    unit: str,
    disable: bool = False,
    leave: bool = True,
) -> Iterable[object]:
    if disable:
        return iterable
    if _tqdm is not None:
        return _tqdm(iterable, desc=desc, unit=unit, leave=leave)
    return _FallbackProgress(iterable, desc=desc, unit=unit)


class _FallbackProgress:
    def __init__(self, iterable: Iterable[object], *, desc: str, unit: str) -> None:
        self._items = list(iterable)
        self._desc = desc
        self._unit = unit
        self._total = len(self._items)

    def __iter__(self) -> Iterator[object]:
        if self._total:
            print(f"{self._desc}: 0/{self._total} {self._unit}", file=sys.stderr)
        for index, item in enumerate(self._items, start=1):
            if self._total and (index == 1 or index == self._total or index % 5 == 0):
                print(f"{self._desc}: {index}/{self._total} {self._unit}", file=sys.stderr)
            yield item


def _build_logger(log_file: Path) -> logging.Logger:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("cleaned_v2_ingest")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.propagate = False

    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Normalize structured cleaned KB documents.")
    parser.add_argument("--source-dir", type=Path, default=DEFAULT_SOURCE_DIR)
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument(
        "--no-progress",
        action="store_true",
        help="Disable tqdm/progress output. The log file is still written.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        help="Optional log file path. Defaults to <output-dir>/ingest.log.",
    )
    parser.add_argument(
        "--include-validation-reports",
        action="store_true",
        help="Include validation_report.md files as parsed documents. They are skipped by default.",
    )
    args = parser.parse_args(argv)

    result = ingest_cleaned_v2(
        args.source_dir,
        args.output_dir,
        include_validation_reports=args.include_validation_reports,
        show_progress=not args.no_progress,
        log_file=args.log_file,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if not result["parse_errors"] else 1


def ingest_cleaned_v2(
    source_dir: Path,
    output_dir: Path,
    *,
    include_validation_reports: bool = False,
    show_progress: bool = True,
    log_file: Optional[Path] = None,
) -> Dict[str, object]:
    source_dir = source_dir.resolve()
    output_dir = output_dir.resolve()
    if not source_dir.exists():
        raise FileNotFoundError(f"source directory does not exist: {source_dir}")
    if not source_dir.is_dir():
        raise NotADirectoryError(f"source path is not a directory: {source_dir}")
    output_dir.mkdir(parents=True, exist_ok=True)
    log_file = (log_file or output_dir / "ingest.log").resolve()
    logger = _build_logger(log_file)
    logger.info("starting cleaned_v2 ingestion source_dir=%s output_dir=%s", source_dir, output_dir)
    logger.info("progress_backend=%s", "tqdm" if _tqdm is not None and show_progress else "fallback/no-progress")

    cards: List[Dict[str, object]] = []
    edges: List[Dict[str, object]] = []
    evidence: List[Dict[str, object]] = []
    sql_patterns: List[Dict[str, object]] = []
    review_items: List[Dict[str, object]] = []
    documents: List[Dict[str, object]] = []
    semantic_mappings: List[Dict[str, object]] = []
    future_context_gaps: List[Dict[str, object]] = []
    parse_errors: List[Dict[str, object]] = []

    yaml_sources: List[Tuple[Path, str]] = []
    json_sources: List[Path] = []
    skipped_files: List[str] = []

    all_paths = sorted(source_dir.rglob("*"))
    logger.info("discovered %s filesystem paths under source dir", len(all_paths))
    for path in _progress(all_paths, desc="Discover sources", unit="path", disable=not show_progress):
        if not path.is_file():
            continue
        rel = _relative_path(path)
        if "reference docs" in path.parts:
            skipped_files.append(rel)
            continue
        if path.name == ".DS_Store":
            skipped_files.append(rel)
            continue
        if path.name == "validation_report.md" and not include_validation_reports:
            skipped_files.append(rel)
            continue
        if path.suffix.lower() == ".md":
            logger.info("queue markdown source path=%s", rel)
            yaml_sources.append((path, path.read_text(encoding="utf-8", errors="replace")))
        elif path.suffix.lower() == ".json":
            logger.info("queue json source path=%s", rel)
            json_sources.append(path)
        else:
            skipped_files.append(rel)

    logger.info(
        "source queue ready markdown=%s json=%s skipped=%s",
        len(yaml_sources),
        len(json_sources),
        len(skipped_files),
    )

    for path, content in _progress(yaml_sources, desc="Parse markdown files", unit="file", disable=not show_progress):
        logger.info("parse markdown start path=%s bytes=%s", _relative_path(path), len(content.encode("utf-8")))
        doc_context = {
            "source_path": _relative_path(path),
            "source_format": "markdown_yaml_blocks",
        }
        blocks, block_errors = _parse_markdown_yaml_blocks(path, content, logger=logger)
        logger.info(
            "parse markdown done path=%s blocks=%s errors=%s",
            _relative_path(path),
            len(blocks),
            len(block_errors),
        )
        parse_errors.extend(block_errors)
        document_metadata = [block.data.get("document_metadata") for block in blocks if block.block_key == "document_metadata"]
        if document_metadata and isinstance(document_metadata[0], Mapping):
            doc_context.update(_document_context(document_metadata[0]))
            documents.append(_normalize_document_metadata(document_metadata[0], doc_context, blocks[0].line_number))

        for block in blocks:
            if block.block_key == "source_evidence":
                payload = block.data.get("source_evidence")
                if isinstance(payload, Mapping):
                    evidence.append(_normalize_evidence(payload, doc_context, block.line_number))
            elif block.block_key == "candidate_card":
                payload = block.data.get("candidate_card")
                if isinstance(payload, Mapping):
                    cards.append(_normalize_card(payload, doc_context, block.line_number))
            elif block.block_key == "candidate_cards":
                payload = block.data.get("candidate_cards")
                if isinstance(payload, list):
                    for item in payload:
                        if isinstance(item, Mapping):
                            cards.append(_normalize_card(item, doc_context, block.line_number))
            elif block.block_key == "candidate_edge":
                payload = block.data.get("candidate_edge")
                if isinstance(payload, Mapping):
                    edges.append(_normalize_edge(payload, doc_context, block.line_number))
            elif block.block_key == "candidate_edges":
                payload = block.data.get("candidate_edges")
                if isinstance(payload, list):
                    for item in payload:
                        if isinstance(item, Mapping):
                            edges.append(_normalize_edge(item, doc_context, block.line_number))
            elif block.block_key == "sql_pattern":
                payload = block.data.get("sql_pattern")
                if isinstance(payload, Mapping):
                    sql_patterns.append(_normalize_sql_pattern(payload, doc_context, block.line_number))
            elif block.block_key == "review_item":
                payload = block.data.get("review_item")
                if isinstance(payload, Mapping):
                    review_items.append(_normalize_review_item(payload, doc_context, block.line_number))
        logger.info("normalize markdown done path=%s", _relative_path(path))

    for path in _progress(json_sources, desc="Parse client JSON files", unit="file", disable=not show_progress):
        logger.info("parse json start path=%s", _relative_path(path))
        data = json.loads(path.read_text(encoding="utf-8"))
        metadata = data.get("package_metadata")
        doc_context = {
            "source_path": _relative_path(path),
            "source_format": "client_runtime_json",
        }
        if isinstance(metadata, Mapping):
            doc_context.update(_document_context(metadata))
            documents.append(_normalize_document_metadata(metadata, doc_context, 1))

        for item in _list(data.get("cards")):
            if isinstance(item, Mapping):
                cards.append(_normalize_card(item, doc_context, 1))
        for item in _list(data.get("edges")):
            if isinstance(item, Mapping):
                edges.append(_normalize_edge(item, doc_context, 1))
        for item in _list(data.get("review_items")):
            if isinstance(item, Mapping):
                review_items.append(_normalize_review_item(item, doc_context, 1))
        for item in _list(data.get("semantic_mappings")):
            if isinstance(item, Mapping):
                semantic_mappings.append(_with_source(dict(item), doc_context, 1))
        for item in _list(data.get("future_context_gaps")):
            if isinstance(item, Mapping):
                future_context_gaps.append(_with_source(dict(item), doc_context, 1))
        logger.info(
            "parse json done path=%s cards=%s edges=%s",
            _relative_path(path),
            len(_list(data.get("cards"))),
            len(_list(data.get("edges"))),
        )

    logger.info("dedupe start")
    cards, duplicate_card_ids = _dedupe_records(cards, "canonical_id")
    edges, duplicate_edges = _dedupe_edges(edges)
    evidence, duplicate_evidence_ids = _dedupe_records(evidence, "evidence_id")
    sql_patterns, duplicate_sql_ids = _dedupe_records(sql_patterns, "sql_id")
    review_items, duplicate_review_ids = _dedupe_records(review_items, "review_id")
    documents, duplicate_document_ids = _dedupe_records(documents, "document_id")
    logger.info(
        "dedupe done cards=%s edges=%s evidence=%s sql_patterns=%s review_items=%s documents=%s",
        len(cards),
        len(edges),
        len(evidence),
        len(sql_patterns),
        len(review_items),
        len(documents),
    )

    dangling_edges = [
        {
            "source_id": edge.get("source_id"),
            "edge_type": edge.get("edge_type"),
            "target_id": edge.get("target_id"),
            "source_path": edge.get("source_path"),
        }
        for edge in edges
        if edge.get("source_id") not in {card.get("canonical_id") for card in cards}
        or edge.get("target_id") not in {card.get("canonical_id") for card in cards}
    ]

    output_sets = [
        ("cards", cards, output_dir / "cards.jsonl"),
        ("edges", edges, output_dir / "edges.jsonl"),
        ("evidence", evidence, output_dir / "evidence.jsonl"),
        ("sql_patterns", sql_patterns, output_dir / "sql_patterns.jsonl"),
        ("review_items", review_items, output_dir / "review_items.jsonl"),
        ("documents", documents, output_dir / "documents.jsonl"),
        ("semantic_mappings", semantic_mappings, output_dir / "semantic_mappings.jsonl"),
        ("future_context_gaps", future_context_gaps, output_dir / "future_context_gaps.jsonl"),
    ]
    for name, records, path in _progress(output_sets, desc="Write outputs", unit="file", disable=not show_progress):
        logger.info("write output start name=%s path=%s records=%s", name, path, len(records))
        _write_jsonl(records, path)
        logger.info("write output done name=%s path=%s", name, path)
    scoped_summary = _write_scoped_outputs(
        output_dir,
        output_sets,
        logger=logger,
        show_progress=show_progress,
    )

    manifest: Dict[str, object] = {
        "generated_on": date.today().isoformat(),
        "source_dir": str(source_dir),
        "output_dir": str(output_dir),
        "source_files": {
            "markdown": len(yaml_sources),
            "json": len(json_sources),
            "skipped": len(skipped_files),
        },
        "counts": {
            "cards": len(cards),
            "edges": len(edges),
            "evidence": len(evidence),
            "sql_patterns": len(sql_patterns),
            "review_items": len(review_items),
            "documents": len(documents),
            "semantic_mappings": len(semantic_mappings),
            "future_context_gaps": len(future_context_gaps),
        },
        "card_types": dict(sorted(Counter(str(card.get("card_type")) for card in cards).items())),
        "edge_types": dict(sorted(Counter(str(edge.get("edge_type")) for edge in edges).items())),
        "confidence": dict(sorted(Counter(str(card.get("confidence")) for card in cards).items())),
        "status": dict(sorted(Counter(str(card.get("status")) for card in cards).items())),
        "duplicates": {
            "cards": duplicate_card_ids,
            "edges": duplicate_edges,
            "evidence": duplicate_evidence_ids,
            "sql_patterns": duplicate_sql_ids,
            "review_items": duplicate_review_ids,
            "documents": duplicate_document_ids,
        },
        "dangling_edges": {
            "count": len(dangling_edges),
            "sample": dangling_edges[:50],
        },
        "parse_errors": parse_errors,
        "skipped_files": skipped_files,
        "outputs": {
            "cards": str(output_dir / "cards.jsonl"),
            "edges": str(output_dir / "edges.jsonl"),
            "evidence": str(output_dir / "evidence.jsonl"),
            "sql_patterns": str(output_dir / "sql_patterns.jsonl"),
            "review_items": str(output_dir / "review_items.jsonl"),
            "documents": str(output_dir / "documents.jsonl"),
            "semantic_mappings": str(output_dir / "semantic_mappings.jsonl"),
            "future_context_gaps": str(output_dir / "future_context_gaps.jsonl"),
            "manifest": str(output_dir / "manifest.json"),
            "log": str(log_file),
            "scoped": str(output_dir / "scoped"),
        },
        "scoped_outputs": scoped_summary,
    }
    _write_json(manifest, output_dir / "manifest.json")
    logger.info("wrote manifest path=%s", output_dir / "manifest.json")
    logger.info("finished cleaned_v2 ingestion parse_errors=%s dangling_edges=%s", len(parse_errors), len(dangling_edges))
    return manifest


def _parse_markdown_yaml_blocks(
    path: Path,
    content: str,
    *,
    logger: logging.Logger,
) -> Tuple[List[ParsedYamlBlock], List[Dict[str, object]]]:
    raw_blocks: List[Dict[str, object]] = []
    errors: List[Dict[str, object]] = []
    for match in YAML_BLOCK_RE.finditer(content):
        yaml_text = match.group(1)
        first_key = FIRST_KEY_RE.search(yaml_text)
        if not first_key:
            continue
        block_key = first_key.group(1)
        if block_key not in {
            "document_metadata",
            "source_evidence",
            "candidate_card",
            "candidate_cards",
            "candidate_edge",
            "candidate_edges",
            "sql_pattern",
            "review_item",
        }:
            continue
        raw_blocks.append(
            {
                "source_path": _relative_path(path),
                "line_number": content.count("\n", 0, match.start()) + 1,
                "block_key": block_key,
                "yaml": yaml_text,
            }
        )

    logger.info("yaml block scan path=%s raw_blocks=%s", _relative_path(path), len(raw_blocks))
    parsed: List[ParsedYamlBlock] = []
    for item in _parse_yaml_with_ruby(raw_blocks):
        if item.get("ok"):
            data = item.get("data")
            if isinstance(data, Mapping):
                parsed.append(
                    ParsedYamlBlock(
                        source_path=str(item["source_path"]),
                        line_number=int(item["line_number"]),
                        block_key=str(item["block_key"]),
                        data=data,
                    )
                )
        else:
            errors.append(
                {
                    "source_path": item.get("source_path"),
                    "line_number": item.get("line_number"),
                    "block_key": item.get("block_key"),
                    "error": item.get("error"),
                }
            )
    return parsed, errors


def _parse_yaml_with_ruby(blocks: Sequence[Mapping[str, object]]) -> Iterator[Mapping[str, object]]:
    if not blocks:
        return iter(())

    ruby = r'''
require "json"
require "yaml"
require "date"

STDIN.each_line do |line|
  item = JSON.parse(line)
  begin
    data = YAML.safe_load(
      item["yaml"],
      permitted_classes: [Date, Time, Symbol],
      permitted_symbols: [],
      aliases: true
    )
    puts JSON.generate({
      ok: true,
      source_path: item["source_path"],
      line_number: item["line_number"],
      block_key: item["block_key"],
      data: data
    })
  rescue => e
    puts JSON.generate({
      ok: false,
      source_path: item["source_path"],
      line_number: item["line_number"],
      block_key: item["block_key"],
      error: "#{e.class}: #{e.message}"
    })
  end
end
'''
    payload = "".join(json.dumps(block, ensure_ascii=False) + "\n" for block in blocks)
    process = subprocess.Popen(
        ["ruby", "-e", ruby],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    stdout, stderr = process.communicate(payload)
    return_code = process.returncode
    if return_code:
        raise RuntimeError(f"ruby YAML parser failed with exit {return_code}: {stderr}")
    return (json.loads(line) for line in stdout.splitlines() if line.strip())


def _normalize_card(raw: Mapping[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    fields = _dict(raw.get("fields"))
    optional_fields = _dict(raw.get("optional_semantic_fields"))
    merged: Dict[str, object] = {}
    merged.update(fields)
    merged.update(optional_fields)
    for key, value in raw.items():
        if key not in {"fields", "optional_semantic_fields"}:
            merged[key] = value

    canonical_id = _first_string(merged, "canonical_id", "card_id", "id")
    if not canonical_id:
        canonical_id = _synthetic_id("unknown_card", doc_context, line_number)
    card_type = _first_string(merged, "card_type") or _card_type_from_id(canonical_id) or "unknown"
    card_type = "metric_implementation" if card_type == "metric_impl" else card_type

    status_source = _first_string(merged, "status", "review_status", "create_action")
    confidence_source = _first_string(merged, "confidence")
    name = _first_string(
        merged,
        "name",
        "display_name",
        "canonical_name",
        "metric_key",
        "platform_specific_name",
        "title",
        "group_name",
        "tenant_name",
        "account_name",
        "table_name",
        "column_name",
    ) or _name_from_id(canonical_id)
    description = _first_string(
        merged,
        "description",
        "business_definition",
        "business_meaning",
        "business_interpretation",
        "process_summary",
        "rule_statement",
        "assertion",
        "purpose",
    ) or f"{card_type} card from {_relative_source(doc_context)}."

    card = dict(merged)
    card.update(
        {
            "card_type": card_type,
            "canonical_id": canonical_id,
            "name": name,
            "description": description,
            "status": _normalize_status(status_source),
            "confidence": _normalize_confidence(confidence_source),
            "source_status": status_source,
            "source_confidence": confidence_source,
            "source_documents": _source_documents(card, doc_context),
            "evidence_ids": _evidence_ids(card),
        }
    )
    _strip_source_id_aliases(card)
    return _with_source(card, doc_context, line_number)


def _normalize_edge(raw: Mapping[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    fields = _dict(raw.get("fields"))
    edge = {}
    edge.update(fields)
    for key, value in raw.items():
        if key != "fields":
            edge[key] = value

    source_id = _first_string(edge, "source_id", "source_card_id", "source")
    target_id = _first_string(edge, "target_id", "target_card_id", "target")
    edge_type = _first_string(edge, "edge_type", "canonical_edge_type", "edge")
    confidence_source = _first_string(edge, "confidence")

    normalized = dict(edge)
    normalized.update(
        {
            "edge_id": _first_string(edge, "edge_id", "id") or _synthetic_edge_id(source_id, edge_type, target_id),
            "source_id": source_id,
            "edge_type": edge_type,
            "target_id": target_id,
            "confidence": _normalize_confidence(confidence_source),
            "source_confidence": confidence_source,
            "evidence_ids": _evidence_ids(edge),
        }
    )
    for key in ("source_card_id", "target_card_id", "source", "target", "edge", "canonical_edge_type"):
        if key in normalized and key not in {"canonical_edge_type"}:
            normalized[f"source_{key}"] = normalized.pop(key)
    return _with_source(normalized, doc_context, line_number)


def _normalize_evidence(raw: Mapping[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    evidence_id = _first_string(raw, "id", "evidence_id") or _synthetic_id("evidence", doc_context, line_number)
    record = dict(raw)
    record["evidence_id"] = evidence_id
    return _with_source(record, doc_context, line_number)


def _normalize_sql_pattern(raw: Mapping[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    sql_id = _first_string(raw, "sql_id", "id") or _synthetic_id("sql", doc_context, line_number)
    record = dict(raw)
    record["sql_id"] = sql_id
    record["evidence_ids"] = _evidence_ids(raw)
    return _with_source(record, doc_context, line_number)


def _normalize_review_item(raw: Mapping[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    review_id = _first_string(raw, "review_id", "id") or _synthetic_id("review", doc_context, line_number)
    record = dict(raw)
    record["review_id"] = review_id
    record["evidence_ids"] = _evidence_ids(raw)
    return _with_source(record, doc_context, line_number)


def _normalize_document_metadata(
    raw: Mapping[str, object],
    doc_context: Mapping[str, object],
    line_number: int,
) -> Dict[str, object]:
    document_id = _first_string(raw, "document_id", "package_id") or _synthetic_id("document", doc_context, line_number)
    record = dict(raw)
    record["document_id"] = document_id
    return _with_source(record, doc_context, line_number)


def _document_context(metadata: Mapping[str, object]) -> Dict[str, object]:
    context: Dict[str, object] = {}
    for key in (
        "document_id",
        "package_id",
        "system",
        "vendor",
        "client_slug",
        "created_for",
        "source_documents",
        "source_docx",
        "source_markdown",
        "allowed_card_types",
        "forbidden_card_types",
    ):
        if key in metadata:
            context[key] = metadata[key]
    return context


def _source_documents(record: Mapping[str, object], doc_context: Mapping[str, object]) -> List[str]:
    values: List[str] = []
    for key in ("source_documents", "source_document", "source_docx", "source_markdown"):
        values.extend(_strings(record.get(key)))
        values.extend(_strings(doc_context.get(key)))
    if not values:
        values.append(str(doc_context.get("source_path") or "unknown"))
    return _dedupe_strings(values)


def _evidence_ids(record: Mapping[str, object]) -> List[str]:
    values: List[str] = []
    for key in ("evidence_ids", "evidence_refs", "source_evidence", "source_evidence_refs"):
        values.extend(_strings(record.get(key)))
    return _dedupe_strings(values)


def _with_source(record: Dict[str, object], doc_context: Mapping[str, object], line_number: int) -> Dict[str, object]:
    record["source_path"] = doc_context.get("source_path")
    record["source_format"] = doc_context.get("source_format")
    record["source_line"] = line_number
    if doc_context.get("document_id") and "document_id" not in record:
        record["document_id"] = doc_context.get("document_id")
    if doc_context.get("package_id") and "package_id" not in record:
        record["package_id"] = doc_context.get("package_id")
    return record


def _normalize_status(value: Optional[str]) -> str:
    if not value:
        return "draft"
    return STATUS_MAP.get(value.strip().lower(), "draft")


def _normalize_confidence(value: Optional[str]) -> str:
    if not value:
        return "unknown"
    return CONFIDENCE_MAP.get(value.strip().lower(), "unknown")


def _strip_source_id_aliases(record: MutableMapping[str, object]) -> None:
    if "card_id" in record:
        record["source_card_id"] = record.pop("card_id")
    if "id" in record and record["id"] == record.get("canonical_id"):
        record.pop("id")


def _dedupe_records(records: Sequence[Dict[str, object]], key: str) -> Tuple[List[Dict[str, object]], Dict[str, int]]:
    by_key: Dict[str, Dict[str, object]] = {}
    counts: Counter[str] = Counter()
    missing_index = 0
    for record in records:
        record_key = str(record.get(key) or "")
        if not record_key:
            missing_index += 1
            record_key = f"missing.{key}.{missing_index}"
            record[key] = record_key
        counts[record_key] += 1
        if record_key not in by_key:
            by_key[record_key] = record
        else:
            by_key[record_key] = _merge_record(by_key[record_key], record)
    duplicates = {item_key: count for item_key, count in sorted(counts.items()) if count > 1}
    return sorted(by_key.values(), key=lambda item: str(item.get(key))), duplicates


def _dedupe_edges(records: Sequence[Dict[str, object]]) -> Tuple[List[Dict[str, object]], Dict[str, int]]:
    by_key: Dict[Tuple[str, str, str], Dict[str, object]] = {}
    counts: Counter[str] = Counter()
    for record in records:
        edge_key = (
            str(record.get("source_id") or ""),
            str(record.get("edge_type") or ""),
            str(record.get("target_id") or ""),
        )
        counts["|".join(edge_key)] += 1
        if edge_key not in by_key:
            by_key[edge_key] = record
        else:
            by_key[edge_key] = _merge_record(by_key[edge_key], record)
    duplicates = {item_key: count for item_key, count in sorted(counts.items()) if count > 1}
    return sorted(
        by_key.values(),
        key=lambda item: (str(item.get("source_id")), str(item.get("edge_type")), str(item.get("target_id"))),
    ), duplicates


def _merge_record(left: Dict[str, object], right: Mapping[str, object]) -> Dict[str, object]:
    merged = dict(left)
    source_paths = _dedupe_strings(_strings(left.get("source_path")) + _strings(right.get("source_path")))
    if source_paths:
        merged["source_paths"] = source_paths
    for key, value in right.items():
        if key not in merged or merged[key] in (None, "", []):
            merged[key] = value
        elif key in {"evidence_ids", "source_documents"}:
            merged[key] = _dedupe_strings(_strings(merged.get(key)) + _strings(value))
    return merged


def _write_jsonl(records: Iterable[Mapping[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def _write_json(record: Mapping[str, object], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(record, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")


def _write_scoped_outputs(
    output_dir: Path,
    output_sets: Sequence[Tuple[str, Sequence[Mapping[str, object]], Path]],
    *,
    logger: logging.Logger,
    show_progress: bool,
) -> Dict[str, object]:
    scoped_root = output_dir / "scoped"
    if scoped_root.exists():
        logger.info("remove existing scoped output dir path=%s", scoped_root)
        shutil.rmtree(scoped_root)

    platform_type_registry = _build_platform_type_registry(output_sets)
    views = {
        "source_type": _source_scopes,
        "platform_type": lambda record: _platform_type_scopes(record, platform_type_registry),
    }
    summary: Dict[str, object] = {}
    for view_name, scope_fn in views.items():
        groups: Dict[Tuple[str, ...], Dict[str, List[Mapping[str, object]]]] = defaultdict(lambda: defaultdict(list))
        seen_keys = set()
        for dataset_name, records, _path in output_sets:
            for record in records:
                for scope in scope_fn(record):
                    record_key = (
                        view_name,
                        scope,
                        dataset_name,
                        str(record.get("canonical_id") or record.get("edge_id") or record.get("evidence_id") or record.get("sql_id") or record.get("review_id") or id(record)),
                    )
                    if record_key in seen_keys:
                        continue
                    seen_keys.add(record_key)
                    groups[scope][dataset_name].append(record)

        view_root = scoped_root / view_name
        view_summary = {
            "scope_count": len(groups),
            "record_count": sum(len(records) for by_dataset in groups.values() for records in by_dataset.values()),
            "root": str(view_root),
        }
        logger.info(
            "write scoped view start view=%s scopes=%s records=%s",
            view_name,
            view_summary["scope_count"],
            view_summary["record_count"],
        )
        for scope, by_dataset in _progress(
            sorted(groups.items(), key=lambda item: item[0]),
            desc=f"Write scoped {view_name}",
            unit="scope",
            disable=not show_progress,
        ):
            scope_dir = view_root.joinpath(*scope)
            _write_scope_dir(scope_dir, scope, by_dataset, logger)
        logger.info("write scoped view done view=%s", view_name)
        summary[view_name] = view_summary
    return summary


def _write_scope_dir(
    scope_dir: Path,
    scope: Tuple[str, ...],
    by_dataset: Mapping[str, Sequence[Mapping[str, object]]],
    logger: logging.Logger,
) -> None:
    scope_dir.mkdir(parents=True, exist_ok=True)
    cards = list(by_dataset.get("cards", []))
    cards_by_type: Dict[str, List[Mapping[str, object]]] = defaultdict(list)
    for card in cards:
        cards_by_type[str(card.get("card_type") or "unknown")].append(card)

    for card_type, records in sorted(cards_by_type.items()):
        _write_jsonl(records, scope_dir / "cards" / f"{_safe_path_part(card_type)}.jsonl")

    for dataset_name, records in sorted(by_dataset.items()):
        if dataset_name == "cards" or not records:
            continue
        _write_jsonl(records, scope_dir / f"{dataset_name}.jsonl")

    manifest = {
        "scope": list(scope),
        "counts": {name: len(records) for name, records in sorted(by_dataset.items())},
        "card_types": dict(sorted(Counter(str(card.get("card_type") or "unknown") for card in cards).items())),
        "edge_types": dict(sorted(Counter(str(edge.get("edge_type") or "unknown") for edge in by_dataset.get("edges", [])).items())),
    }
    _write_json(manifest, scope_dir / "manifest.json")
    logger.info("write scoped scope=%s dir=%s counts=%s", "/".join(scope), scope_dir, manifest["counts"])


def _source_scopes(record: Mapping[str, object]) -> List[Tuple[str, str]]:
    scopes = []
    for source_path in _record_source_paths(record):
        parsed = _parse_cleaned_v2_source_path(source_path)
        if parsed:
            scopes.append(parsed)
    return sorted(set(scopes))


def _build_platform_type_registry(
    output_sets: Sequence[Tuple[str, Sequence[Mapping[str, object]], Path]]
) -> Dict[str, str]:
    candidates: Dict[str, Counter[str]] = defaultdict(Counter)
    for _dataset_name, records, _path in output_sets:
        for record in records:
            for source_path in _record_source_paths(record):
                parsed = _parse_cleaned_v2_source_path(source_path)
                if parsed and parsed[0] != "clients":
                    source_type, source_name = parsed
                    platform = _platform_from_source_name(source_name)
                    candidates[platform][_platform_type_from_source_type(source_type)] += 1

            for key in ("platform_id", "platform_context_id", "platform_account_id", "source_id", "target_id", "canonical_id"):
                value = record.get(key)
                if isinstance(value, str):
                    platform = _platform_from_id(value)
                    if platform:
                        inferred_type = _platform_type_from_record(record)
                        if inferred_type != "unknown":
                            candidates[platform][inferred_type] += 1

    registry: Dict[str, str] = {}
    priority = {
        "marketplace": 0,
        "logistics": 1,
        "bank": 2,
        "payments": 3,
        "oms": 4,
        "wms": 5,
        "clients": 6,
        "other": 7,
        "unknown": 8,
    }
    for platform, type_counts in candidates.items():
        best_type = sorted(type_counts.items(), key=lambda item: (-item[1], priority.get(item[0], 99), item[0]))[0][0]
        registry[platform] = best_type
    return registry


def _platform_type_scopes(
    record: Mapping[str, object],
    platform_type_registry: Mapping[str, str],
) -> List[Tuple[str, str]]:
    platform_names = set()
    for key in ("platform_id", "platform_context_id"):
        value = record.get(key)
        if isinstance(value, str):
            platform = _platform_from_id(value)
            if platform:
                platform_names.add(platform)

    for key in ("platform_account_id", "source_id", "target_id", "canonical_id"):
        value = record.get(key)
        if isinstance(value, str):
            platform = _platform_from_id(value)
            if platform:
                platform_names.add(platform)

    source_types = set()
    for source_path in _record_source_paths(record):
        parsed = _parse_cleaned_v2_source_path(source_path)
        if parsed:
            source_type, source_name = parsed
            source_types.add(_platform_type_from_source_type(source_type))
            if source_type != "clients":
                platform_names.add(_platform_from_source_name(source_name))

    if not platform_names:
        fallback_type = sorted(source_types)[0] if source_types else "unknown"
        return [(fallback_type, "unknown")]

    scopes = []
    for platform in sorted(platform_names):
        platform_type = platform_type_registry.get(platform) or _platform_type_from_record(record)
        if platform_type == "unknown" and source_types:
            platform_type = sorted(source_types)[0]
        scopes.append((_safe_path_part(platform_type), platform))
    return sorted(set(scopes))


def _platform_type_from_source_type(source_type: str) -> str:
    mapping = {
        "bank": "bank",
        "clients": "clients",
        "logistics": "logistics",
        "marketplace": "marketplace",
        "oms": "oms",
        "payments": "payments",
        "wms": "wms",
    }
    return mapping.get(source_type, "other")


def _platform_type_from_record(record: Mapping[str, object]) -> str:
    values: List[str] = []
    for key in (
        "platform_category",
        "platform_type",
        "account_type",
        "account_role",
        "business_role",
        "domain_family",
        "source_config_text",
        "description",
        "name",
    ):
        values.extend(_strings(record.get(key)))
    text = " ".join(values).lower()
    if any(marker in text for marker in ("marketplace", "seller", "amazon", "flipkart", "myntra", "ajio")):
        return "marketplace"
    if any(marker in text for marker in ("logistics", "courier", "awb", "shipment", "freight", "shiprocket", "delhivery")):
        return "logistics"
    if any(marker in text for marker in ("bank", "banking", "statement", "payout banking")):
        return "bank"
    if any(marker in text for marker in ("payment", "gateway", "payin", "payout", "settlement gateway")):
        return "payments"
    if any(marker in text for marker in ("oms", "order management", "d2c channel")):
        return "oms"
    if any(marker in text for marker in ("wms", "warehouse", "inventory")):
        return "wms"
    return "unknown"


def _record_source_paths(record: Mapping[str, object]) -> List[str]:
    values = _strings(record.get("source_path")) + _strings(record.get("source_paths"))
    return _dedupe_strings(values)


def _parse_cleaned_v2_source_path(source_path: str) -> Optional[Tuple[str, str]]:
    parts = Path(source_path).parts
    index = -1
    for marker in ("cleaned_v2", "cleaned"):
        try:
            index = parts.index(marker)
            break
        except ValueError:
            continue
    if index < 0:
        return None
    remaining = parts[index + 1 :]
    if len(remaining) < 2:
        return None
    source_type = _safe_path_part(remaining[0])
    source_name = _safe_path_part(Path(remaining[-1]).stem)
    return source_type, source_name


def _platform_from_id(value: str) -> Optional[str]:
    parts = value.split(".")
    if value.startswith("platform."):
        return _safe_path_part(parts[1]) if len(parts) > 1 else None
    if value.startswith("platform_context."):
        return _safe_path_part(parts[1]) if len(parts) > 1 else None
    if value.startswith("platform_account.") and len(parts) > 2:
        return _safe_path_part(_strip_country_suffix(parts[2]))
    if value.startswith("account_data_binding.") and len(parts) > 2:
        return _safe_path_part(_strip_country_suffix(parts[2]))
    return None


def _platform_from_source_name(source_name: str) -> str:
    cleaned = source_name
    suffixes = (
        "_marketplace",
        "_logistics_aggregator",
        "_logistics",
        "_d2c_oms",
        "_operations",
        "_payment_gateway",
        "_bank_statement",
    )
    for suffix in suffixes:
        if cleaned.endswith(suffix):
            cleaned = cleaned[: -len(suffix)]
            break
    return _safe_path_part(cleaned or source_name)


def _strip_country_suffix(value: str) -> str:
    for suffix in ("_in", "_us", "_usa", "_uk", "_ae"):
        if value.endswith(suffix):
            return value[: -len(suffix)]
    return value


def _safe_path_part(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_.-]+", "_", str(value).strip()).strip("._-")
    return slug.lower() or "unknown"


def _first_string(record: Mapping[str, object], *keys: str) -> Optional[str]:
    for key in keys:
        value = record.get(key)
        if isinstance(value, str) and value.strip():
            return value.strip()
        if isinstance(value, (int, float)):
            return str(value)
    return None


def _dict(value: object) -> Dict[str, object]:
    return dict(value) if isinstance(value, Mapping) else {}


def _list(value: object) -> List[object]:
    return list(value) if isinstance(value, list) else []


def _strings(value: object) -> List[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, (int, float)):
        return [str(value)]
    if isinstance(value, Mapping):
        for key in ("id", "evidence_id", "chunk_id", "source_document", "source_doc"):
            if isinstance(value.get(key), str):
                return [str(value[key])]
        return []
    if isinstance(value, list):
        output: List[str] = []
        for item in value:
            output.extend(_strings(item))
        return output
    return []


def _dedupe_strings(values: Iterable[str]) -> List[str]:
    seen = set()
    output = []
    for value in values:
        text = str(value).strip()
        if not text or text in seen:
            continue
        seen.add(text)
        output.append(text)
    return output


def _card_type_from_id(canonical_id: str) -> Optional[str]:
    prefix = canonical_id.split(".", 1)[0]
    return CARD_TYPE_BY_PREFIX.get(prefix)


def _name_from_id(canonical_id: str) -> str:
    stem = canonical_id.rsplit(".", 1)[-1]
    return stem.replace("_", " ").replace("-", " ").title()


def _synthetic_id(prefix: str, doc_context: Mapping[str, object], line_number: int) -> str:
    source = str(doc_context.get("source_path") or "unknown")
    slug = re.sub(r"[^a-z0-9]+", "_", source.lower()).strip("_")
    return f"{prefix}.{slug}.{line_number}"


def _synthetic_edge_id(source_id: Optional[str], edge_type: Optional[str], target_id: Optional[str]) -> str:
    raw = ".".join(part for part in (source_id, edge_type, target_id) if part)
    slug = re.sub(r"[^a-z0-9]+", "_", raw.lower()).strip("_")
    return f"edge.{slug or 'unknown'}"


def _relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT_DIR))
    except ValueError:
        return str(path)


def _relative_source(doc_context: Mapping[str, object]) -> str:
    return str(doc_context.get("source_path") or "unknown source")


if __name__ == "__main__":
    sys.exit(main())
