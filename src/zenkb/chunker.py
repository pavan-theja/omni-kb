from __future__ import annotations

import hashlib
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
MAX_CHUNK_CHARS = 6000


@dataclass(frozen=True)
class SemanticChunk:
    chunk_id: str
    source_doc: str
    source_path: str
    source_span: str
    start_line: int
    end_line: int
    heading_path: List[str]
    heading_level: Optional[int]
    title: Optional[str]
    frontmatter: Dict[str, object]
    content_hash: str
    content: str


@dataclass(frozen=True)
class ChunkValidationResult:
    chunk_count: int
    source_doc_count: int
    duplicate_chunk_ids: List[str]
    empty_chunk_ids: List[str]
    missing_span_chunk_ids: List[str]

    @property
    def ok(self) -> bool:
        return not (
            self.duplicate_chunk_ids
            or self.empty_chunk_ids
            or self.missing_span_chunk_ids
        )


def discover_markdown_files(source_dir: Path) -> List[Path]:
    return sorted(path for path in source_dir.rglob("*.md") if path.is_file())


def chunk_markdown_files(source_dir: Path) -> List[SemanticChunk]:
    chunks: List[SemanticChunk] = []
    for path in discover_markdown_files(source_dir):
        chunks.extend(chunk_markdown_file(path, source_dir))
    return chunks


def chunk_markdown_file(path: Path, source_dir: Path) -> List[SemanticChunk]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    frontmatter, body_start_index = _parse_frontmatter(lines)
    sections = _split_sections(lines, body_start_index)
    rel_path = path.relative_to(source_dir.parent).as_posix()

    chunks: List[SemanticChunk] = []
    for section in sections:
        chunks.extend(_section_to_chunks(section, rel_path, frontmatter))
    return chunks


def validate_chunks(chunks: Iterable[SemanticChunk]) -> ChunkValidationResult:
    seen: Dict[str, int] = {}
    duplicates: List[str] = []
    empty: List[str] = []
    missing_span: List[str] = []
    source_docs = set()

    for chunk in chunks:
        source_docs.add(chunk.source_doc)
        seen[chunk.chunk_id] = seen.get(chunk.chunk_id, 0) + 1
        if not chunk.content.strip():
            empty.append(chunk.chunk_id)
        if chunk.start_line < 1 or chunk.end_line < chunk.start_line:
            missing_span.append(chunk.chunk_id)

    for chunk_id, count in seen.items():
        if count > 1:
            duplicates.append(chunk_id)

    return ChunkValidationResult(
        chunk_count=sum(seen.values()),
        source_doc_count=len(source_docs),
        duplicate_chunk_ids=sorted(duplicates),
        empty_chunk_ids=sorted(empty),
        missing_span_chunk_ids=sorted(missing_span),
    )


def write_chunks(chunks: List[SemanticChunk], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(json.dumps(asdict(chunk), ensure_ascii=False, sort_keys=True))
            handle.write("\n")


def _parse_frontmatter(lines: List[str]) -> Tuple[Dict[str, object], int]:
    if not lines or lines[0].strip() != "---":
        return {}, 0

    end_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break

    if end_index is None:
        return {}, 0

    return _parse_simple_yaml(lines[1:end_index]), end_index + 1


def _parse_simple_yaml(lines: List[str]) -> Dict[str, object]:
    data: Dict[str, object] = {}
    current_key: Optional[str] = None

    for raw_line in lines:
        line = raw_line.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue

        stripped = line.strip()
        if stripped.startswith("- ") and current_key:
            existing = data.setdefault(current_key, [])
            if isinstance(existing, list):
                existing.append(_coerce_scalar(stripped[2:].strip()))
            continue

        if ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        current_key = key
        if not value:
            data[key] = []
        else:
            data[key] = _coerce_scalar(value)

    return data


def _coerce_scalar(value: str) -> object:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_coerce_scalar(item.strip()) for item in inner.split(",")]
    if (
        (value.startswith('"') and value.endswith('"'))
        or (value.startswith("'") and value.endswith("'"))
    ):
        return value[1:-1]
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return value


@dataclass(frozen=True)
class _Section:
    start_line: int
    end_line: int
    heading_path: List[str]
    heading_level: Optional[int]
    title: Optional[str]
    lines: List[str]


def _split_sections(lines: List[str], body_start_index: int) -> List[_Section]:
    sections: List[_Section] = []
    heading_stack: List[Tuple[int, str]] = []
    current_start = body_start_index + 1
    current_heading_path: List[str] = []
    current_heading_level: Optional[int] = None
    current_title: Optional[str] = None
    current_lines: List[str] = []

    for index in range(body_start_index, len(lines)):
        line = lines[index]
        match = HEADING_RE.match(line)
        if match and current_lines:
            sections.append(
                _Section(
                    start_line=current_start,
                    end_line=index,
                    heading_path=current_heading_path,
                    heading_level=current_heading_level,
                    title=current_title,
                    lines=current_lines,
                )
            )
            current_lines = []

        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            heading_stack = [(h_level, h_title) for h_level, h_title in heading_stack if h_level < level]
            heading_stack.append((level, title))
            current_start = index + 1
            current_heading_path = [h_title for _, h_title in heading_stack]
            current_heading_level = level
            current_title = title

        current_lines.append(line)

    if current_lines:
        sections.append(
            _Section(
                start_line=current_start,
                end_line=len(lines),
                heading_path=current_heading_path,
                heading_level=current_heading_level,
                title=current_title,
                lines=current_lines,
            )
        )

    return sections


def _section_to_chunks(
    section: _Section, source_doc: str, frontmatter: Dict[str, object]
) -> List[SemanticChunk]:
    content = "\n".join(section.lines).strip()
    if not content:
        return []
    if len(content) <= MAX_CHUNK_CHARS:
        return [_make_chunk(section, source_doc, frontmatter, content, section.start_line, section.end_line, 0)]

    chunks: List[SemanticChunk] = []
    part_start_line = section.start_line
    part_lines: List[str] = []
    part_index = 0

    for offset, line in enumerate(section.lines):
        candidate = "\n".join(part_lines + [line]).strip()
        if part_lines and len(candidate) > MAX_CHUNK_CHARS and not line.startswith("|"):
            part_end_line = section.start_line + offset - 1
            chunks.append(
                _make_chunk(
                    section,
                    source_doc,
                    frontmatter,
                    "\n".join(part_lines).strip(),
                    part_start_line,
                    part_end_line,
                    part_index,
                )
            )
            part_index += 1
            part_start_line = section.start_line + offset
            part_lines = [line]
        else:
            part_lines.append(line)

    if part_lines:
        chunks.append(
            _make_chunk(
                section,
                source_doc,
                frontmatter,
                "\n".join(part_lines).strip(),
                part_start_line,
                section.end_line,
                part_index,
            )
        )

    return chunks


def _make_chunk(
    section: _Section,
    source_doc: str,
    frontmatter: Dict[str, object],
    content: str,
    start_line: int,
    end_line: int,
    part_index: int,
) -> SemanticChunk:
    content_hash = hashlib.sha1(content.encode("utf-8")).hexdigest()
    heading_slug = _slugify("__".join(section.heading_path) or "document")
    source_slug = _slugify(source_doc)
    chunk_id = f"{source_slug}::{heading_slug}::{part_index:03d}::{content_hash[:12]}"

    return SemanticChunk(
        chunk_id=chunk_id,
        source_doc=source_doc,
        source_path=source_doc,
        source_span=f"lines {start_line}-{end_line}",
        start_line=start_line,
        end_line=end_line,
        heading_path=section.heading_path,
        heading_level=section.heading_level,
        title=section.title,
        frontmatter=frontmatter,
        content_hash=content_hash,
        content=content,
    )


def _slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value).strip("_")
    return value or "unknown"
