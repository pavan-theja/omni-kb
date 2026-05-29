from __future__ import annotations

import json
from dataclasses import dataclass
from typing import List, Optional, Sequence, Tuple


@dataclass(frozen=True)
class ProgressSnapshot:
    current: int
    total: int
    unit: str
    status: str = ""

    def summary(self) -> str:
        percent = (self.current / self.total * 100) if self.total else 0.0
        status_suffix = f", status={self.status}" if self.status else ""
        return f"{self.current}/{self.total} {self.unit} ({percent:.1f}%){status_suffix}"


def compact_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def status_summary(value: object, verbose: bool) -> str:
    if verbose:
        return compact_json(value)
    pipeline_statuses = pipeline_statuses_from_response(value)
    progress = progress_snapshot_from_response(value)
    if progress:
        parts = [progress.summary()]
        if pipeline_statuses:
            parts.append(", ".join(f"{name}={status}" for name, status in pipeline_statuses))
        return ", ".join(parts)
    if pipeline_statuses:
        return ", ".join(f"{name}={status}" for name, status in pipeline_statuses)
    return compact_json(value)[:500]


def progress_snapshot_from_response(value: object, *, pipeline_hint: str = "cognify") -> Optional[ProgressSnapshot]:
    candidates: list[tuple[int, ProgressSnapshot]] = []

    def visit(item: object, path: Sequence[str], inherited_name: str, inherited_status: str) -> None:
        if isinstance(item, dict):
            name = _first_string(
                item,
                (
                    "pipeline",
                    "pipeline_name",
                    "pipelineName",
                    "name",
                    "task_name",
                    "taskName",
                    "run_name",
                ),
            ) or inherited_name
            status = _first_string(
                item,
                (
                    "status",
                    "state",
                    "pipeline_status",
                    "pipelineStatus",
                    "run_status",
                    "runStatus",
                    "result",
                ),
            ) or inherited_status
            numeric = {
                str(key): number
                for key, raw_value in item.items()
                for number in [_int_value(raw_value)]
                if number is not None
            }
            current_items = [
                (key, number)
                for key, number in numeric.items()
                if _is_current_key(key)
            ]
            total_items = [
                (key, number)
                for key, number in numeric.items()
                if _is_total_key(key)
            ]
            for current_key, current in current_items:
                for total_key, total in total_items:
                    if total <= 0:
                        continue
                    unit = _unit_for_progress(current_key, total_key, name, path)
                    score = _progress_score(
                        name=name,
                        path=path,
                        current=current,
                        total=total,
                        unit=unit,
                        pipeline_hint=pipeline_hint,
                    )
                    candidates.append(
                        (
                            score,
                            ProgressSnapshot(
                                current=current,
                                total=total,
                                unit=unit,
                                status=status,
                            ),
                        )
                    )
            for key, nested in item.items():
                visit(nested, [*path, str(key)], name, status)
        elif isinstance(item, list):
            for index, nested in enumerate(item):
                visit(nested, [*path, str(index)], inherited_name, inherited_status)

    visit(value, [], "", "")
    if not candidates:
        return None
    candidates.sort(key=lambda item: (item[0], item[1].total, item[1].current), reverse=True)
    return candidates[0][1]


def pipeline_statuses_from_response(value: object) -> List[Tuple[str, str]]:
    records: List[Tuple[str, str]] = []

    def visit(item: object) -> None:
        if isinstance(item, dict):
            name = _first_string(
                item,
                (
                    "pipeline",
                    "pipeline_name",
                    "pipelineName",
                    "name",
                    "task_name",
                    "taskName",
                    "run_name",
                ),
            )
            status = _first_string(
                item,
                (
                    "status",
                    "state",
                    "pipeline_status",
                    "pipelineStatus",
                    "run_status",
                    "runStatus",
                    "result",
                ),
            )
            if name or status:
                records.append((name or "pipeline", status or "unknown"))
            for nested in item.values():
                visit(nested)
        elif isinstance(item, list):
            for nested in item:
                visit(nested)

    visit(value)
    deduped: List[Tuple[str, str]] = []
    seen = set()
    for record in records:
        key = (record[0].lower(), record[1].lower())
        if key not in seen:
            deduped.append(record)
            seen.add(key)
    return deduped[:8]


def terminal_state(value: object) -> str:
    statuses = " ".join(status.lower() for _, status in pipeline_statuses_from_response(value))
    raw = compact_json(value).lower()
    text = f"{statuses} {raw}"
    if any(marker in text for marker in ("failed", "failure", "error", "cancelled")):
        return "failed"
    active_markers = ("running", "processing", "pending", "queued", "started", "in_progress")
    completed_markers = ("completed", "complete", "finished", "success", "successful")
    if any(marker in text for marker in active_markers):
        return "running"
    if "cognify" in text and any(marker in text for marker in completed_markers):
        return "completed"
    if any(marker in statuses for marker in completed_markers):
        return "completed"
    return "running"


def _first_string(record: dict, keys: Sequence[str]) -> str:
    for key in keys:
        value = record.get(key)
        if isinstance(value, str) and value:
            return value
    return ""


def _int_value(value: object) -> Optional[int]:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str) and value.strip().isdigit():
        return int(value.strip())
    return None


def _normalized_key(key: str) -> str:
    return "".join(char for char in key.lower() if char.isalnum())


def _is_current_key(key: str) -> bool:
    normalized = _normalized_key(key)
    return normalized in {
        "completed",
        "completedcount",
        "completeditems",
        "completedtasks",
        "completedchunks",
        "completeddocuments",
        "processed",
        "processedcount",
        "processeditems",
        "processedtasks",
        "processedchunks",
        "processeddocuments",
        "finished",
        "finishedcount",
        "done",
        "donecount",
        "current",
        "currentcount",
        "successful",
        "successfulcount",
        "success",
        "successcount",
    }


def _is_total_key(key: str) -> bool:
    normalized = _normalized_key(key)
    return normalized in {
        "total",
        "totalcount",
        "totalitems",
        "totaltasks",
        "totalchunks",
        "totaldocuments",
        "totaldocs",
        "totalfiles",
        "totaldata",
        "totaldataitems",
    }


def _unit_for_progress(current_key: str, total_key: str, name: str, path: Sequence[str]) -> str:
    text = " ".join([current_key, total_key, name, *path]).lower()
    if "chunk" in text:
        return "chunks"
    if "document" in text or "doc" in text or "file" in text or "textdocument" in text:
        return "documents"
    if "task" in text:
        return "tasks"
    if "data" in text:
        return "data items"
    return "items"


def _progress_score(
    *,
    name: str,
    path: Sequence[str],
    current: int,
    total: int,
    unit: str,
    pipeline_hint: str,
) -> int:
    text = " ".join([name, *path]).lower()
    score = 0
    if pipeline_hint and pipeline_hint.lower() in text:
        score += 20
    if unit in {"chunks", "documents", "data items"}:
        score += 5
    if 0 <= current <= total:
        score += 3
    return score
