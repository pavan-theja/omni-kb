from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .utils import write_json, write_jsonl


def build_readiness_pack(
    *,
    cards: list[dict[str, Any]],
    edges: list[dict[str, Any]],
    parse_errors: list[dict[str, Any]],
    validation: dict[str, Any],
    catalog_manifest: dict[str, Any],
    doc_manifest: list[dict[str, Any]],
    add_batches: list[dict[str, Any]],
    cognify_batches: list[dict[str, Any]],
    output_dir: Path,
) -> dict[str, Any]:
    readiness_dir = output_dir / "readiness"
    errors = validation.get("errors") if isinstance(validation.get("errors"), list) else []
    warnings = validation.get("warnings") if isinstance(validation.get("warnings"), list) else []
    missing_scope_columns = missing_scope_column_rows(errors)
    blocked_runtime_bindings = blocked_binding_rows(missing_scope_columns)
    scope_key_warnings = scope_key_warning_rows(warnings)

    doc_count_matches_card_count = len(doc_manifest) == len(cards)
    ingestion_batches_generated = bool(add_batches) and bool(cognify_batches)
    packaging_ready = not parse_errors and doc_count_matches_card_count and ingestion_batches_generated
    contract_validation_ready = bool(validation.get("ok"))
    runtime_search_ready = contract_validation_ready and not blocked_runtime_bindings

    error_counts = Counter(str(row.get("error") or "unknown") for row in errors)
    warning_counts = Counter(str(row.get("warning") or "unknown") for row in warnings)
    missing_scope_table_counts = Counter(
        str(row.get("table_id") or "unknown") for row in missing_scope_columns
    )
    source_layer_counts = Counter(
        str((card.get("_meta") or {}).get("pack_layer_hint") or "unknown") for card in cards
    )

    artifacts = {
        "readiness_summary": str(readiness_dir / "readiness_summary.json"),
        "readiness_report": str(readiness_dir / "readiness_report.md"),
        "blocked_runtime_bindings": str(readiness_dir / "blocked_runtime_bindings.jsonl"),
        "missing_scope_columns": str(readiness_dir / "missing_scope_columns.jsonl"),
        "scope_key_warnings": str(readiness_dir / "scope_key_warnings.jsonl"),
    }
    gates = {
        "packaging_ready_for_cognee_add": packaging_ready,
        "contract_validation_ready": contract_validation_ready,
        "runtime_search_ready": runtime_search_ready,
    }
    summary = {
        "readiness_version": "refactored_v2_build_readiness_v1",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat(),
        "readiness_dir": str(readiness_dir),
        "gates": gates,
        "counts": {
            "card_count": len(cards),
            "edge_count": len(edges),
            "doc_count": len(doc_manifest),
            "parse_error_count": len(parse_errors),
            "validation_error_count": len(errors),
            "validation_warning_count": len(warnings),
            "runtime_binding_count": catalog_manifest.get("runtime_binding_count"),
            "active_runtime_binding_count": catalog_manifest.get("active_runtime_binding_count"),
            "blocked_runtime_binding_count": len(blocked_runtime_bindings),
            "missing_scope_column_count": len(missing_scope_columns),
            "scope_key_warning_count": len(scope_key_warnings),
            "add_batch_count": len(add_batches),
            "cognify_batch_count": len(cognify_batches),
            "table_count": catalog_manifest.get("table_count"),
        },
        "validation_error_counts": dict(sorted(error_counts.items())),
        "validation_warning_counts": dict(sorted(warning_counts.items())),
        "source_layer_counts": dict(sorted(source_layer_counts.items())),
        "top_missing_scope_column_tables": [
            {"table_id": table_id, "missing_scope_column_count": count}
            for table_id, count in missing_scope_table_counts.most_common(25)
        ],
        "artifacts": artifacts,
        "recommended_next_action": readiness_next_action(gates, len(blocked_runtime_bindings), len(scope_key_warnings)),
    }

    write_json(readiness_dir / "readiness_summary.json", summary)
    write_jsonl(readiness_dir / "blocked_runtime_bindings.jsonl", blocked_runtime_bindings)
    write_jsonl(readiness_dir / "missing_scope_columns.jsonl", missing_scope_columns)
    write_jsonl(readiness_dir / "scope_key_warnings.jsonl", scope_key_warnings)
    (readiness_dir / "readiness_report.md").write_text(
        render_readiness_report(summary, blocked_runtime_bindings),
        encoding="utf-8",
    )
    return summary


def missing_scope_column_rows(errors: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for error in errors:
        if error.get("error") != "binding_scope_column_missing_despite_table_loaded":
            continue
        rows.append(
            {
                "canonical_id": error.get("canonical_id"),
                "table_id": error.get("table_id"),
                "scope_column_id": error.get("scope_column_id"),
                "status": "blocked_scope_column_missing",
                "severity": "critical",
                "readiness_gate": "runtime_contract",
            }
        )
    return sorted(rows, key=lambda row: (str(row.get("canonical_id")), str(row.get("scope_column_id"))))


def blocked_binding_rows(missing_scope_columns: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = {}
    for row in missing_scope_columns:
        binding_id = str(row.get("canonical_id") or "")
        if not binding_id:
            continue
        grouped.setdefault(
            binding_id,
            {
                "canonical_id": binding_id,
                "binding_status": "blocked_scope_column_missing",
                "severity": "critical",
                "search_runtime_policy": "must_not_emit_table_frame_contract_until_fixed",
                "table_ids": [],
                "missing_scope_columns": [],
            },
        )
        table_id = row.get("table_id")
        scope_column_id = row.get("scope_column_id")
        if table_id and table_id not in grouped[binding_id]["table_ids"]:
            grouped[binding_id]["table_ids"].append(table_id)
        if scope_column_id and scope_column_id not in grouped[binding_id]["missing_scope_columns"]:
            grouped[binding_id]["missing_scope_columns"].append(scope_column_id)

    out = list(grouped.values())
    for row in out:
        row["table_ids"] = sorted(row["table_ids"])
        row["missing_scope_columns"] = sorted(row["missing_scope_columns"])
        row["missing_scope_column_count"] = len(row["missing_scope_columns"])
    return sorted(out, key=lambda row: str(row.get("canonical_id")))


def scope_key_warning_rows(warnings: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for warning in warnings:
        if warning.get("warning") != "binding_has_no_scope_keys":
            continue
        rows.append(
            {
                "canonical_id": warning.get("canonical_id"),
                "status": "binding_has_no_scope_keys",
                "severity": "warning",
                "readiness_gate": "runtime_scope_specificity",
            }
        )
    return sorted(rows, key=lambda row: str(row.get("canonical_id")))


def readiness_next_action(gates: dict[str, bool], blocked_count: int, warning_count: int) -> str:
    if not gates["packaging_ready_for_cognee_add"]:
        return "Fix parse or packaging failures before Cognee add/cognify ingestion."
    if blocked_count:
        return "Repair missing scope-column cards or explicitly keep those runtime bindings blocked before runtime migration."
    if warning_count:
        return "Review bindings without scope keys before relying on tenant/group scoped runtime search."
    return "Build pack is ready for Cognee ingestion and runtime contract migration."


def render_readiness_report(summary: dict[str, Any], blocked_runtime_bindings: list[dict[str, Any]]) -> str:
    counts = summary.get("counts") if isinstance(summary.get("counts"), dict) else {}
    gates = summary.get("gates") if isinstance(summary.get("gates"), dict) else {}
    top_tables = summary.get("top_missing_scope_column_tables") or []
    artifacts = summary.get("artifacts") if isinstance(summary.get("artifacts"), dict) else {}

    lines = [
        "# Constrained Search Build Readiness",
        "",
        "## Gates",
        f"- Packaging ready for Cognee add: {gate_label(gates.get('packaging_ready_for_cognee_add'))}",
        f"- Contract validation ready: {gate_label(gates.get('contract_validation_ready'))}",
        f"- Runtime search ready: {gate_label(gates.get('runtime_search_ready'))}",
        "",
        "## Counts",
        f"- Cards: {counts.get('card_count')}",
        f"- Edges: {counts.get('edge_count')}",
        f"- Rendered docs: {counts.get('doc_count')}",
        f"- Parse errors: {counts.get('parse_error_count')}",
        f"- Validation errors: {counts.get('validation_error_count')}",
        f"- Validation warnings: {counts.get('validation_warning_count')}",
        f"- Runtime bindings: {counts.get('runtime_binding_count')}",
        f"- Active runtime bindings: {counts.get('active_runtime_binding_count')}",
        f"- Blocked runtime bindings: {counts.get('blocked_runtime_binding_count')}",
        f"- Missing scope columns: {counts.get('missing_scope_column_count')}",
        f"- Scope-key warnings: {counts.get('scope_key_warning_count')}",
        f"- Add batches: {counts.get('add_batch_count')}",
        f"- Cognify batches: {counts.get('cognify_batch_count')}",
        "",
        "## Top Missing Scope-Column Tables",
    ]
    if top_tables:
        for row in top_tables[:10]:
            lines.append(f"- `{row.get('table_id')}`: {row.get('missing_scope_column_count')}")
    else:
        lines.append("- None")

    lines.extend(["", "## Example Blocked Runtime Bindings"])
    if blocked_runtime_bindings:
        for row in blocked_runtime_bindings[:10]:
            missing = ", ".join(f"`{item}`" for item in row.get("missing_scope_columns", [])[:3])
            extra_count = max(0, int(row.get("missing_scope_column_count") or 0) - 3)
            suffix = f" plus {extra_count} more" if extra_count else ""
            lines.append(f"- `{row.get('canonical_id')}`: {missing}{suffix}")
    else:
        lines.append("- None")

    lines.extend(
        [
            "",
            "## Generated Artifacts",
            f"- Summary: `{artifacts.get('readiness_summary')}`",
            f"- Blocked runtime bindings: `{artifacts.get('blocked_runtime_bindings')}`",
            f"- Missing scope columns: `{artifacts.get('missing_scope_columns')}`",
            f"- Scope-key warnings: `{artifacts.get('scope_key_warnings')}`",
            "",
            "## Recommended Next Action",
            str(summary.get("recommended_next_action") or ""),
            "",
        ]
    )
    return "\n".join(lines)


def gate_label(value: Any) -> str:
    return "PASS" if value else "FAIL"

