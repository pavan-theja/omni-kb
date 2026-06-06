from __future__ import annotations

from collections import Counter
from typing import Any

from .utils import infer_table_id_from_column_id


def validate_cards(cards: list[dict[str, Any]], edges: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    card_ids = {str(card.get("canonical_id")) for card in cards if card.get("canonical_id")}
    table_ids = {str(card.get("canonical_id")) for card in cards if card.get("card_type") == "table" and card.get("canonical_id")}
    by_type = Counter(str(card.get("card_type") or "unknown") for card in cards)

    for card in cards:
        cid = str(card.get("canonical_id") or "")
        ctype = str(card.get("card_type") or "")
        if not cid:
            errors.append({"error": "missing_canonical_id", "card": card.get("canonical_name") or card.get("name")})
        if not ctype:
            errors.append({"canonical_id": cid, "error": "missing_card_type"})
        if not card.get("ingestion_node_sets"):
            errors.append({"canonical_id": cid, "error": "missing_ingestion_node_sets"})
        if ctype == "account_data_binding":
            validate_account_data_binding(card, card_ids, table_ids, errors, warnings)

    for edge in edges:
        source_id = str(edge.get("source_id") or "")
        target_id = str(edge.get("target_id") or "")
        if source_id and source_id not in card_ids:
            warnings.append({"source_id": source_id, "target_id": target_id, "warning": "edge_source_id_missing_from_cards"})
        if target_id and target_id not in card_ids:
            warnings.append({"source_id": source_id, "target_id": target_id, "warning": "edge_target_id_missing_from_cards"})

    return {
        "ok": not errors,
        "errors": errors,
        "warnings": warnings,
        "card_count": len(cards),
        "edge_count": len(edges),
        "card_type_counts": dict(sorted(by_type.items())),
    }


def validate_account_data_binding(
    card: dict[str, Any],
    card_ids: set[str],
    table_ids: set[str],
    errors: list[dict[str, Any]],
    warnings: list[dict[str, Any]],
) -> None:
    cid = str(card.get("canonical_id") or "")
    fields = card.get("fields") if isinstance(card.get("fields"), dict) else {}
    traversal = card.get("traversal") if isinstance(card.get("traversal"), dict) else {}
    table_id = fields.get("table_id") or traversal.get("table_id") or card.get("table_id")
    if not table_id:
        errors.append({"canonical_id": cid, "error": "binding_missing_table_id"})
    scope_keys = fields.get("scope_keys") or card.get("scope_keys") or []
    if not scope_keys:
        warnings.append({"canonical_id": cid, "warning": "binding_has_no_scope_keys"})
    for scope in scope_keys if isinstance(scope_keys, list) else []:
        if not isinstance(scope, dict):
            continue
        col_id = scope.get("scope_column_id") or scope.get("column_id")
        if not col_id and table_id and scope.get("column"):
            col_id = f"column.{str(table_id).removeprefix('table.')}.{scope['column']}"
        if col_id and col_id not in card_ids:
            col_table_id = infer_table_id_from_column_id(str(col_id))
            if col_table_id in table_ids:
                errors.append(
                    {
                        "canonical_id": cid,
                        "error": "binding_scope_column_missing_despite_table_loaded",
                        "scope_column_id": col_id,
                        "table_id": col_table_id,
                    }
                )
            else:
                warnings.append(
                    {
                        "canonical_id": cid,
                        "warning": "binding_scope_column_deferred_because_reusable_table_pack_not_loaded",
                        "scope_column_id": col_id,
                        "table_id": col_table_id,
                    }
                )

