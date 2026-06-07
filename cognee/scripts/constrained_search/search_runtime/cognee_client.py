from __future__ import annotations

import asyncio
import importlib
import inspect
import os
import sys
from pathlib import Path
from typing import Any, Iterable

from runtime_env import REPO_ROOT

from .catalogs import CatalogBundle
from .nodeset_contracts import SearchContract
from .utils import first_node_set, jsonable, read_jsonl, result_text, unique_in_order


class CogneeIntegrationError(RuntimeError):
    pass


class CogneeClient:
    """Cognee SDK adapter for constrained NodeSet contract search."""

    def __init__(
        self,
        *,
        pack_dir: str | Path,
        catalogs: CatalogBundle,
        datasets: list[str] | None = None,
        all_datasets: bool = False,
        prompted_recall: bool = False,
        cognee_module: Any | None = None,
    ):
        self.pack_dir = Path(pack_dir)
        self.catalogs = catalogs
        self.configured_datasets = datasets or datasets_from_pack(self.pack_dir)
        self.all_datasets = all_datasets
        self.prompted_recall = prompted_recall
        self.add_batches = read_jsonl(self.pack_dir / "cognee_ingestion" / "add_batches.jsonl")
        self._cognee = cognee_module

    @staticmethod
    def _import_cognee() -> Any:
        saved_path = list(sys.path)
        try:
            sys.path = sdk_import_path(saved_path)
            return importlib.import_module("cognee")
        except Exception as exc:  # noqa: BLE001
            raise CogneeIntegrationError("Cognee SDK is not importable in this environment.") from exc
        finally:
            sys.path = saved_path

    @property
    def cognee(self) -> Any:
        if self._cognee is None:
            self._cognee = self._import_cognee()
        return self._cognee

    async def search(self, contract: SearchContract) -> list[dict[str, Any]]:
        routed_contract = self.with_routed_datasets(contract)
        response = await self.recall_context(routed_contract)
        return normalize_cognee_recall_result(response, routed_contract, self.catalogs)

    def with_routed_datasets(self, contract: SearchContract) -> SearchContract:
        if self.all_datasets:
            return SearchContract(**{**contract.to_dict(), "datasets": contract.datasets or self.configured_datasets})
        if contract.datasets:
            return SearchContract(**{**contract.to_dict(), "datasets": self._known_datasets(contract.datasets)})

        required = set(contract.node_sets)
        routed = unique_in_order(
            str(batch.get("dataset_name") or "")
            for batch in self.add_batches
            if required.issubset(set(batch.get("node_sets") or []))
        )

        if not routed:
            routed = unique_in_order(
                dataset
                for cid in contract.candidate_seed_ids + contract.exact_dereference_ids + canonical_ids_from_node_sets(contract.node_sets)
                for dataset in self.datasets_for_card_id(cid)
            )

        return SearchContract(**{**contract.to_dict(), "datasets": self._known_datasets(routed or self.configured_datasets)})

    def datasets_for_card_id(self, canonical_id: str) -> list[str]:
        return unique_in_order(
            str(batch.get("dataset_name") or "")
            for batch in self.add_batches
            if canonical_id in set(str(cid) for cid in batch.get("canonical_ids") or [])
        )

    def _known_datasets(self, datasets: Iterable[str]) -> list[str]:
        configured = set(self.configured_datasets)
        return unique_in_order(dataset for dataset in datasets if dataset in configured)

    async def recall_context(self, contract: SearchContract) -> Any:
        recall_fn = getattr(self.cognee, "recall", None)
        search_type = getattr(self.cognee, "SearchType", None)
        if recall_fn is None:
            raise CogneeIntegrationError("Imported Cognee SDK does not expose cognee.recall.")
        if search_type is None or not hasattr(search_type, "GRAPH_COMPLETION"):
            raise CogneeIntegrationError("Imported Cognee SDK does not expose SearchType.GRAPH_COMPLETION.")

        kwargs: dict[str, Any] = {
            "query_text": prompted_recall_query_text(contract) if self.prompted_recall else contract.query_text,
            "query_type": search_type.GRAPH_COMPLETION,
            "top_k": contract.top_k,
            "scope": "graph",
            "auto_route": False,
            "node_name": contract.node_sets,
            "node_name_filter_operator": "AND",
            "only_context": not self.prompted_recall,
        }
        if contract.datasets:
            kwargs["datasets"] = contract.datasets
        return await invoke_maybe_async(recall_fn, kwargs)


def prompted_recall_query_text(contract: SearchContract) -> str:
    return (
        "Use only the cards that match the supplied NodeSet filters. "
        "Return one compact JSON object with selected_card_ids, rejected_card_ids, "
        "selection_reasons, missing_evidence, readiness, and a concise evidence_summary. "
        "Every selected_card_id must be an exact canonical_id from the retrieved cards.\n\n"
        f"Task: {contract.query_text}"
    )


def normalize_cognee_recall_result(result: Any, contract: SearchContract, catalogs: CatalogBundle) -> list[dict[str, Any]]:
    items = normalize_result_items(result)
    cards: list[dict[str, Any]] = []
    seen: set[str] = set()
    required = set(contract.node_sets)

    for item in items:
        for canonical_id in canonical_ids_from_result(item, catalogs):
            if canonical_id in seen:
                continue
            card = catalogs.card_for_id(canonical_id)
            if not card:
                continue
            if not required.issubset(set(card.get("node_sets") or [])):
                continue
            card["retrieval"] = {
                "contract_id": contract.contract_id,
                "datasets": contract.datasets,
                "raw_result": jsonable(item),
            }
            cards.append(card)
            seen.add(canonical_id)
    return cards


def normalize_result_items(result: Any) -> list[Any]:
    if result is None:
        return []
    if isinstance(result, list):
        out: list[Any] = []
        for item in result:
            out.extend(normalize_result_items(item))
        return out
    if hasattr(result, "model_dump"):
        return [result.model_dump(mode="json")]
    if isinstance(result, dict):
        for key in ("results", "items", "documents", "cards", "chunks", "context"):
            value = result.get(key)
            if isinstance(value, list):
                return normalize_result_items(value)
        return [result]
    return [result]


def canonical_ids_from_result(item: Any, catalogs: CatalogBundle) -> list[str]:
    direct = find_first_key(item, "canonical_id") or find_first_key(item, "id")
    ids: list[str] = []
    if direct and catalogs.known_card_id(str(direct)):
        ids.append(str(direct))

    text = result_text(item)
    if text:
        ids.extend(cid for cid in catalogs.card_catalog if cid in text)
    return unique_in_order(ids)


def canonical_ids_from_node_sets(node_sets: list[str]) -> list[str]:
    value = first_node_set(node_sets, "canonical_id")
    return [value] if value else []


def find_first_key(value: Any, key: str) -> Any:
    if isinstance(value, dict):
        if key in value:
            return value[key]
        for item in value.values():
            found = find_first_key(item, key)
            if found not in (None, "", []):
                return found
    elif isinstance(value, list):
        for item in value:
            found = find_first_key(item, key)
            if found not in (None, "", []):
                return found
    return None


async def invoke_maybe_async(fn: Any, kwargs: dict[str, Any]) -> Any:
    if inspect.iscoroutinefunction(fn):
        result = fn(**kwargs)
    else:
        result = await asyncio.to_thread(fn, **kwargs)
    if inspect.isawaitable(result):
        return await result
    return result


def datasets_from_pack(pack_dir: str | Path) -> list[str]:
    batches = read_jsonl(Path(pack_dir) / "cognee_ingestion" / "cognify_batches.jsonl")
    datasets: list[str] = []
    for batch in batches:
        for dataset in batch.get("datasets") or []:
            if dataset not in datasets:
                datasets.append(str(dataset))
    return datasets


def sdk_import_path(paths: Iterable[str]) -> list[str]:
    filtered: list[str] = []
    for entry in paths:
        resolved = Path(entry or os.getcwd()).resolve()
        if resolved == REPO_ROOT:
            continue
        filtered.append(entry)
    return filtered
