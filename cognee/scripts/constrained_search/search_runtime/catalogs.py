from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .utils import read_json, read_jsonl


@dataclass(slots=True)
class CatalogBundle:
    """Read-only resolver catalogs generated during constrained-search packaging."""

    pack_dir: Path
    card_catalog: dict[str, dict[str, Any]] = field(default_factory=dict)
    search_contract_templates: dict[str, dict[str, Any]] = field(default_factory=dict)
    runtime_binding_catalog: list[dict[str, Any]] = field(default_factory=list)
    runtime_binding_status_catalog: dict[str, dict[str, Any]] = field(default_factory=dict)
    table_contract_catalog: dict[str, dict[str, Any]] = field(default_factory=dict)
    node_set_registry: list[dict[str, Any]] = field(default_factory=list)
    source_role_registry: dict[str, list[str]] = field(default_factory=dict)
    alias_registry: dict[str, list[str]] = field(default_factory=dict)
    node_set_values: set[str] = field(default_factory=set)
    platform_alias_map: dict[str, str] = field(default_factory=dict)

    @classmethod
    def load(cls, pack_dir: str | Path) -> "CatalogBundle":
        pack_dir = Path(pack_dir)
        catalog_dir = pack_dir / "resolver_catalog"
        card_catalog = read_json(catalog_dir / "card_catalog.json", default={})
        node_set_registry = read_jsonl(catalog_dir / "node_set_registry.jsonl")
        return cls(
            pack_dir=pack_dir,
            card_catalog=card_catalog,
            search_contract_templates=read_json(catalog_dir / "search_contract_templates.json", default={}),
            runtime_binding_catalog=read_json(catalog_dir / "runtime_binding_catalog.json", default=[]),
            runtime_binding_status_catalog=read_json(catalog_dir / "runtime_binding_status_catalog.json", default={}),
            table_contract_catalog=read_json(catalog_dir / "table_contract_catalog.json", default={}),
            node_set_registry=node_set_registry,
            source_role_registry=read_json(catalog_dir / "source_role_registry.json", default={}),
            alias_registry=read_json(catalog_dir / "alias_registry.json", default={}),
            node_set_values=collect_node_set_values(card_catalog, node_set_registry),
            platform_alias_map=collect_platform_alias_map(card_catalog),
        )

    def template_for_stage(self, stage: str) -> dict[str, Any] | None:
        if stage in self.search_contract_templates:
            return self.search_contract_templates[stage]
        for key, template in self.search_contract_templates.items():
            if stage.startswith(key):
                return template
        return None

    def card_type_for_contract_stage(self, stage: str) -> str | None:
        template = self.template_for_stage(stage) or {}
        value = template.get("card_type")
        return str(value) if value else None

    def known_card_id(self, canonical_id: str) -> bool:
        return canonical_id in self.card_catalog

    def card_for_id(self, canonical_id: str) -> dict[str, Any] | None:
        card = self.card_catalog.get(canonical_id)
        return dict(card) if isinstance(card, dict) else None

    def known_table_id(self, table_id: str) -> bool:
        if table_id in self.table_contract_catalog:
            return True
        card = self.card_catalog.get(table_id) or {}
        return card.get("card_type") == "table"

    def authored_node_sets_for_card(self, canonical_id: str) -> set[str]:
        card = self.card_catalog.get(canonical_id) or {}
        return set(card.get("node_sets") or [])

    def binding_status(self, account_data_binding_id: str) -> dict[str, Any] | None:
        return self.runtime_binding_status_catalog.get(account_data_binding_id)

    def known_node_set(self, node_set: str) -> bool:
        return node_set in self.node_set_values

    def canonicalize_node_set(self, node_set: str) -> str:
        if node_set in self.node_set_values or ":" not in node_set:
            return node_set
        key, value = node_set.split(":", 1)
        if key == "platform_id":
            canonical = self.platform_alias_map.get(value) or self.platform_alias_map.get(value.lower())
            if canonical:
                return f"platform_id:{canonical}"
        return node_set


def collect_node_set_values(card_catalog: dict[str, dict[str, Any]], node_set_registry: list[dict[str, Any]]) -> set[str]:
    values: set[str] = set()
    for row in node_set_registry:
        values.update(str(node_set) for node_set in row.get("node_sets") or [])
    for card in card_catalog.values():
        if isinstance(card, dict):
            values.update(str(node_set) for node_set in card.get("node_sets") or [])
    return values


def collect_platform_alias_map(card_catalog: dict[str, dict[str, Any]]) -> dict[str, str]:
    aliases: dict[str, str] = {}
    for canonical_id, card in card_catalog.items():
        if not isinstance(card, dict) or card.get("card_type") != "platform":
            continue
        platform_id = str((card.get("traversal") or {}).get("platform_id") or canonical_id)
        add_platform_alias(aliases, platform_id, platform_id)
        if platform_id.startswith("platform."):
            add_platform_alias(aliases, platform_id.removeprefix("platform."), platform_id)
        for node_set in card.get("node_sets") or []:
            text = str(node_set)
            if text.startswith("platform_alias:"):
                add_platform_alias(aliases, text.split(":", 1)[1], platform_id)
        fields = card.get("fields") or {}
        for value in fields.get("aliases") or []:
            add_platform_alias(aliases, str(value), platform_id)
        for value in fields.get("source_platform_codes") or []:
            add_platform_alias(aliases, str(value), platform_id)
    return aliases


def add_platform_alias(aliases: dict[str, str], alias: str, platform_id: str) -> None:
    normalized = alias.strip()
    if not normalized:
        return
    aliases.setdefault(normalized, platform_id)
    aliases.setdefault(normalized.lower(), platform_id)
