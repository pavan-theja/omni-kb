from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from .utils import flatten_strings, infer_table_id_from_column_id, scope_column_ids_for_binding, write_json, write_jsonl


def build_catalogs(cards: list[dict[str, Any]], edges: list[dict[str, Any]], output_dir: Path) -> dict[str, Any]:
    catalog_dir = output_dir / "resolver_catalog"
    catalog_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(output_dir / "cards.jsonl", cards)
    write_jsonl(output_dir / "edges.jsonl", edges)

    card_catalog: dict[str, dict[str, Any]] = {}
    node_set_registry: list[dict[str, Any]] = []
    alias_registry: dict[str, list[str]] = defaultdict(list)
    runtime_binding_catalog: list[dict[str, Any]] = []
    source_role_registry: dict[str, list[str]] = defaultdict(list)
    table_contract_catalog: dict[str, dict[str, Any]] = {}

    for card in cards:
        cid = str(card.get("canonical_id"))
        ctype = card.get("card_type")
        fields = card.get("fields") if isinstance(card.get("fields"), dict) else {}
        traversal = card.get("traversal") if isinstance(card.get("traversal"), dict) else {}
        semantic = card.get("semantic") if isinstance(card.get("semantic"), dict) else {}
        retrieval = card.get("retrieval") if isinstance(card.get("retrieval"), dict) else {}
        node_sets = card.get("ingestion_node_sets") or []

        card_catalog[cid] = {
            "canonical_id": cid,
            "card_type": ctype,
            "canonical_name": card.get("canonical_name") or card.get("name"),
            "node_sets": node_sets,
            "source_layer": (card.get("_meta") or {}).get("pack_layer_hint"),
            "traversal": traversal,
            "fields": fields,
        }
        node_set_registry.append({"canonical_id": cid, "card_type": ctype, "node_sets": node_sets})

        for alias in flatten_strings(
            [
                semantic.get("aliases"),
                semantic.get("colloquial_phrases"),
                retrieval.get("search_keywords"),
                retrieval.get("exact_match_keys"),
                card.get("aliases"),
                card.get("name"),
                card.get("canonical_name"),
            ]
        ):
            key = alias.lower().strip()
            if key and cid not in alias_registry[key]:
                alias_registry[key].append(cid)

        role = traversal.get("source_role") or fields.get("source_role") or card.get("source_role")
        if role:
            source_role_registry[str(role)].append(cid)

        if ctype == "account_data_binding":
            runtime_binding_catalog.append(
                {
                    "canonical_id": cid,
                    "platform_account_id": traversal.get("platform_account_id") or fields.get("platform_account_id") or card.get("platform_account_id"),
                    "platform_id": traversal.get("platform_id") or fields.get("platform_id") or card.get("platform_id"),
                    "platform_context_id": traversal.get("platform_context_id") or fields.get("platform_context_id") or card.get("platform_context_id"),
                    "table_id": traversal.get("table_id") or fields.get("table_id") or card.get("table_id"),
                    "source_role": role,
                    "scope_keys": fields.get("scope_keys") or card.get("scope_keys") or [],
                    "node_sets": node_sets,
                }
            )

        if ctype == "table":
            table_contract_catalog[cid] = {
                "canonical_id": cid,
                "platform_id": traversal.get("platform_id") or fields.get("platform_id") or card.get("platform_id"),
                "platform_context_id": traversal.get("platform_context_id") or fields.get("platform_context_id") or card.get("platform_context_id"),
                "domain_id": traversal.get("domain_id") or fields.get("domain_id") or card.get("domain_id"),
                "source_role": role,
                "node_sets": node_sets,
                "amount_columns": fields.get("amount_columns") or card.get("amount_columns") or [],
                "date_columns": fields.get("date_columns") or card.get("date_columns") or [],
                "recommended_date_columns": fields.get("recommended_date_columns") or card.get("recommended_date_columns") or [],
                "mandatory_filters": fields.get("mandatory_filters") or card.get("mandatory_filters") or [],
                "business_keys": fields.get("business_keys") or card.get("business_keys") or [],
                "grain": fields.get("grain") or card.get("grain"),
            }

    runtime_binding_status = runtime_binding_status_catalog(runtime_binding_catalog, set(card_catalog), set(table_contract_catalog))

    write_json(catalog_dir / "card_catalog.json", card_catalog)
    write_jsonl(catalog_dir / "card_catalog.jsonl", list(card_catalog.values()))
    write_jsonl(catalog_dir / "node_set_registry.jsonl", node_set_registry)
    write_json(catalog_dir / "alias_registry.json", dict(alias_registry))
    write_json(catalog_dir / "source_role_registry.json", dict(source_role_registry))
    write_json(catalog_dir / "runtime_binding_catalog.json", runtime_binding_catalog)
    write_json(catalog_dir / "runtime_binding_status_catalog.json", runtime_binding_status)
    write_json(catalog_dir / "table_contract_catalog.json", table_contract_catalog)
    write_json(catalog_dir / "search_contract_templates.json", search_contract_templates())

    status_counts = Counter(row.get("binding_status") for row in runtime_binding_status.values())
    return {
        "card_count": len(cards),
        "edge_count": len(edges),
        "runtime_binding_count": len(runtime_binding_catalog),
        "active_runtime_binding_count": status_counts.get("active", 0),
        "blocked_runtime_binding_count": sum(count for key, count in status_counts.items() if str(key).startswith("blocked")),
        "deferred_runtime_binding_count": sum(count for key, count in status_counts.items() if str(key).startswith("deferred")),
        "table_count": len(table_contract_catalog),
    }


def runtime_binding_status_catalog(
    runtime_bindings: list[dict[str, Any]],
    card_ids: set[str],
    table_ids: set[str],
) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for binding in runtime_bindings:
        binding_id = str(binding["canonical_id"])
        table_id = binding.get("table_id")
        scope_keys = binding.get("scope_keys") or []
        scope_column_ids = scope_column_ids_for_binding(table_id, scope_keys)
        missing_scope_columns = [cid for cid in scope_column_ids if cid not in card_ids]
        semantic_table_loaded = bool(table_id and table_id in table_ids)
        table_present_column_missing: list[str] = []
        missing_due_to_unloaded_table: list[str] = []
        for col_id in missing_scope_columns:
            col_table_id = infer_table_id_from_column_id(col_id)
            if col_table_id in table_ids:
                table_present_column_missing.append(col_id)
            else:
                missing_due_to_unloaded_table.append(col_id)

        if not semantic_table_loaded:
            status = "deferred_missing_reusable_table"
            severity = "medium"
        elif table_present_column_missing:
            status = "blocked_scope_column_missing"
            severity = "critical"
        else:
            status = "active"
            severity = "none"

        out[binding_id] = {
            **binding,
            "semantic_table_loaded": semantic_table_loaded,
            "scope_column_ids": scope_column_ids,
            "missing_reusable_table_ids": [] if semantic_table_loaded else ([table_id] if table_id else []),
            "missing_scope_columns": missing_scope_columns,
            "missing_scope_columns_because_table_unloaded": missing_due_to_unloaded_table,
            "missing_scope_columns_despite_table_loaded": table_present_column_missing,
            "binding_status": status,
            "severity": severity,
            "search_runtime_policy": (
                "may_emit_table_frame_contract" if status == "active" else "must_not_emit_table_frame_contract_until_fixed"
            ),
        }
    return out


def search_contract_templates() -> dict[str, dict[str, Any]]:
    return {
        "runtime_group_search": {
            "required_node_set_keys": ["domain_family", "card_type", "tenant_id", "group_id"],
            "card_type": "group",
        },
        "runtime_platform_account_search": {
            "required_node_set_keys": ["domain_family", "card_type", "tenant_id", "group_id", "platform_id"],
            "card_type": "platform_account",
        },
        "runtime_account_binding_search": {
            "required_node_set_keys": ["domain_family", "card_type", "tenant_id", "group_id", "platform_account_id"],
            "card_type": "account_data_binding",
        },
        "semantic_platform_search": {
            "required_node_set_keys": ["card_type", "platform_id"],
            "card_type": "platform",
        },
        "semantic_table_frame_search": {
            "required_node_set_keys": ["card_type", "table_id"],
            "card_type": "table",
        },
        "exact_card_dereference_search": {
            "required_node_set_keys": ["canonical_id"],
            "card_type": None,
        },
        "table_local_column_search": {
            "required_node_set_keys": ["card_type", "table_id"],
            "card_type": "column",
        },
        "table_local_metric_implementation_search": {
            "required_node_set_keys": ["card_type", "table_id"],
            "card_type": "metric_implementation",
        },
        "table_local_query_pattern_search": {
            "required_node_set_keys": ["card_type", "table_id"],
            "card_type": "query_pattern",
        },
    }

