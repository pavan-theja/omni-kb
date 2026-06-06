#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import importlib
import inspect
import json
import os
import sys
from dataclasses import asdict, dataclass, field, replace
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence


CONSTRAINED_SEARCH_DIR = Path(__file__).resolve().parents[1]
if str(CONSTRAINED_SEARCH_DIR) not in sys.path:
    sys.path.insert(0, str(CONSTRAINED_SEARCH_DIR))

from runtime_env import PROVIDER_CHOICES, REPO_ROOT, configure_cognee_environment  # noqa: E402


DEFAULT_PACK_DIR = REPO_ROOT / "build" / "constrained_search" / "build_marketplace_runtime"
DEFAULT_ENV_FILE = REPO_ROOT / "cognee" / ".env"
DEFAULT_TENANT_ID = "tenant.mensa_brand_technologies_private_limited"
DEFAULT_GROUP_ID = "group.mensa_brand_technologies_private_limited.g8.gl22"


class CogneeIntegrationError(RuntimeError):
    pass


@dataclass
class CatalogBundle:
    card_catalog: dict[str, dict[str, Any]]
    runtime_binding_status: dict[str, dict[str, Any]]
    search_contract_templates: dict[str, dict[str, Any]]

    @classmethod
    def load(cls, pack_dir: Path) -> "CatalogBundle":
        catalog_dir = pack_dir / "resolver_catalog"
        return cls(
            card_catalog=read_json(catalog_dir / "card_catalog.json"),
            runtime_binding_status=read_json(catalog_dir / "runtime_binding_status_catalog.json"),
            search_contract_templates=read_json(catalog_dir / "search_contract_templates.json"),
        )

    def known_card_id(self, canonical_id: str) -> bool:
        return canonical_id in self.card_catalog

    def known_table_id(self, table_id: str) -> bool:
        card = self.card_catalog.get(table_id)
        return bool(card and card.get("card_type") == "table")

    def template_for_stage(self, stage: str) -> dict[str, Any]:
        return self.search_contract_templates.get(stage) or {}

    def authored_node_sets_for_card(self, canonical_id: str) -> set[str]:
        card = self.card_catalog.get(canonical_id) or {}
        return set(card.get("node_sets") or [])


@dataclass
class SearchContract:
    contract_id: str
    stage: str
    query_text: str
    node_sets: list[str]
    allowed_card_types: list[str]
    expected_card_ids: list[str]
    datasets: list[str] = field(default_factory=list)
    top_k: int = 3

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Probe post-cognify constrained-search NodeSets through the Cognee SDK.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--tenant-id", default=DEFAULT_TENANT_ID)
    parser.add_argument("--group-id", default=DEFAULT_GROUP_ID)
    parser.add_argument("--dataset", action="append", help="Dataset to search. Defaults to datasets from the pack.")
    parser.add_argument(
        "--mode",
        choices=("recall-context", "search-completion"),
        default="recall-context",
        help="Use targeted recall context by default; search-completion keeps the legacy completion probe.",
    )
    parser.add_argument(
        "--all-datasets",
        action="store_true",
        help="Disable add-batch shard routing and search every configured dataset for every contract.",
    )
    parser.add_argument("--search-callable", help="Optional dotted path for a Cognee search wrapper.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args(argv)

    try:
        result = asyncio.run(run(args))
    except (CogneeIntegrationError, RuntimeError, ValueError) as exc:
        print(f"constrained ingestion probe failed: {exc}", file=sys.stderr)
        return 1

    print(result["status"])
    print(result["output_path"])
    return 0 if result["status"] in {"passed", "dry_run"} else 1


async def run(args: argparse.Namespace) -> dict[str, Any]:
    pack_dir = resolve_pack_dir(args.pack_dir)
    configure_cognee_environment(pack_dir, env_file=args.env_file, provider=args.provider)
    catalogs = CatalogBundle.load(pack_dir)
    configured_datasets = args.dataset or datasets_from_pack(pack_dir)
    explicit_datasets = bool(args.dataset)
    datasets = configured_datasets
    if not datasets:
        raise RuntimeError("No datasets configured. Pass --dataset or build cognify_batches.jsonl first.")

    probes = build_probes(catalogs, tenant_id=args.tenant_id, group_id=args.group_id, datasets=datasets)
    if not explicit_datasets and not args.all_datasets:
        probes = route_probe_datasets(probes, add_batch_dataset_index(pack_dir), datasets)
    active_datasets = unique_in_order(dataset for probe in probes for dataset in probe.datasets)
    trace: list[dict[str, Any]] = []
    failed = False

    if args.dry_run:
        for contract in probes:
            contract_validation = validate_contract(contract, catalogs)
            if not contract_validation["ok"]:
                failed = True
            trace.append(
                {
                    "contract": contract.to_dict(),
                    "contract_validation": contract_validation,
                    "probe_mode": args.mode,
                    "dataset_routing": dataset_routing_summary(
                        contract,
                        configured_datasets=configured_datasets,
                        explicit_datasets=explicit_datasets,
                        all_datasets=args.all_datasets,
                    ),
                    "status": "contract_valid" if contract_validation["ok"] else "contract_invalid",
                }
            )
        status = "failed" if failed else "dry_run"
        return write_probe_result(
            pack_dir,
            status=status,
            mode=args.mode,
            datasets=active_datasets,
            configured_datasets=configured_datasets,
            trace=trace,
        )

    if args.mode == "recall-context" and args.search_callable:
        raise ValueError("--search-callable is only used with --mode search-completion")
    search_fn = load_search_callable(args.search_callable) if args.mode == "search-completion" else None
    cognee_sdk = load_cognee_sdk() if args.mode == "recall-context" else None
    for contract in probes:
        contract_validation = validate_contract(contract, catalogs)
        if not contract_validation["ok"]:
            failed = True
            trace.append(
                {
                    "contract": contract.to_dict(),
                    "contract_validation": contract_validation,
                    "probe_mode": args.mode,
                    "dataset_routing": dataset_routing_summary(
                        contract,
                        configured_datasets=configured_datasets,
                        explicit_datasets=explicit_datasets,
                        all_datasets=args.all_datasets,
                    ),
                    "status": "contract_invalid",
                }
            )
            continue

        try:
            if args.mode == "recall-context":
                response = await recall_context_cognee(cognee_sdk, contract)
            else:
                response = await search_cognee(search_fn, contract)
            returned_items = normalize_search_result(response)
            result_validation = validate_returned_items(contract, returned_items, catalogs)
        except Exception as exc:  # noqa: BLE001
            failed = True
            trace.append(
                {
                    "contract": contract.to_dict(),
                    "contract_validation": contract_validation,
                    "probe_mode": args.mode,
                    "dataset_routing": dataset_routing_summary(
                        contract,
                        configured_datasets=configured_datasets,
                        explicit_datasets=explicit_datasets,
                        all_datasets=args.all_datasets,
                    ),
                    "status": "search_failed",
                    "error": repr(exc),
                }
            )
            continue

        if not result_validation["ok"]:
            failed = True
        trace.append(
            {
                "contract": contract.to_dict(),
                "contract_validation": contract_validation,
                "probe_mode": args.mode,
                "dataset_routing": dataset_routing_summary(
                    contract,
                    configured_datasets=configured_datasets,
                    explicit_datasets=explicit_datasets,
                    all_datasets=args.all_datasets,
                ),
                "returned_count": len(returned_items),
                "result_validation": result_validation,
                "returned_card_ids": returned_card_ids(returned_items, contract.expected_card_ids),
            }
        )

    return write_probe_result(
        pack_dir,
        status="failed" if failed else "passed",
        mode=args.mode,
        datasets=active_datasets,
        configured_datasets=configured_datasets,
        trace=trace,
    )


def build_probes(
    catalogs: CatalogBundle,
    *,
    tenant_id: str,
    group_id: str,
    datasets: list[str],
) -> list[SearchContract]:
    probes = [
        SearchContract(
            contract_id="probe.runtime_group",
            stage="runtime_group_search",
            query_text="Mensa runtime group scope",
            node_sets=[
                "domain_family:client_runtime",
                "card_type:group",
                f"tenant_id:{tenant_id}",
                f"group_id:{group_id}",
            ],
            allowed_card_types=["group"],
            expected_card_ids=[group_id],
            datasets=datasets,
            top_k=3,
        ),
        SearchContract(
            contract_id="probe.amazon_platform",
            stage="semantic_platform_search",
            query_text="Amazon platform canonical card",
            node_sets=["card_type:platform", "platform_id:platform.amazon"],
            allowed_card_types=["platform"],
            expected_card_ids=["platform.amazon"],
            datasets=datasets,
            top_k=3,
        ),
        SearchContract(
            contract_id="probe.amazon_oms_table",
            stage="semantic_table_frame_search",
            query_text="Amazon OMS table frame",
            node_sets=["card_type:table", "table_id:table.zs_observe.amazon_oms"],
            allowed_card_types=["table"],
            expected_card_ids=["table.zs_observe.amazon_oms"],
            datasets=datasets,
            top_k=3,
        ),
        SearchContract(
            contract_id="probe.amazon_settlement_table",
            stage="semantic_table_frame_search",
            query_text="Amazon settlement table frame",
            node_sets=["card_type:table", "table_id:table.zs_observe.amazon_settlement"],
            allowed_card_types=["table"],
            expected_card_ids=["table.zs_observe.amazon_settlement"],
            datasets=datasets,
            top_k=3,
        ),
    ]
    binding = choose_runtime_binding(catalogs, tenant_id=tenant_id, group_id=group_id)
    if binding:
        probes.append(
            SearchContract(
                contract_id="probe.amazon_settlement_runtime_binding",
                stage="runtime_account_binding_search",
                query_text="Mensa Amazon settlement runtime account binding",
                node_sets=list(binding.get("node_sets") or []),
                allowed_card_types=["account_data_binding"],
                expected_card_ids=[str(binding["canonical_id"])],
                datasets=datasets,
                top_k=3,
            )
        )
    return probes


def choose_runtime_binding(catalogs: CatalogBundle, *, tenant_id: str, group_id: str) -> Optional[dict[str, Any]]:
    preferred_id = (
        "account_data_binding.mensa_brand_technologies_private_limited."
        "amazon_india.settlement.zs_observe_amazon_settlement"
    )
    preferred = catalogs.runtime_binding_status.get(preferred_id)
    if preferred and preferred.get("binding_status") == "active":
        return preferred

    for binding in catalogs.runtime_binding_status.values():
        node_sets = set(binding.get("node_sets") or [])
        if (
            binding.get("binding_status") == "active"
            and f"tenant_id:{tenant_id}" in node_sets
            and f"group_id:{group_id}" in node_sets
            and "platform_id:platform.amazon" in node_sets
            and "table_id:table.zs_observe.amazon_settlement" in node_sets
        ):
            return binding
    return None


async def search_cognee(search_fn: Any, contract: SearchContract) -> Any:
    kwargs: dict[str, Any] = {
        "query_text": contract.query_text,
        "top_k": contract.top_k,
    }
    kwargs.update(nodeset_search_kwargs(search_fn, contract))
    if contract.datasets:
        kwargs["datasets"] = contract.datasets
    try:
        return await invoke_maybe_async(search_fn, kwargs)
    except TypeError:
        if "datasets" not in kwargs:
            raise
        kwargs.pop("datasets")
        return await invoke_maybe_async(search_fn, kwargs)


async def recall_context_cognee(cognee_sdk: Any, contract: SearchContract) -> Any:
    recall_fn = getattr(cognee_sdk, "recall", None)
    search_type = getattr(cognee_sdk, "SearchType", None)
    if recall_fn is None:
        raise CogneeIntegrationError("Imported Cognee SDK does not expose cognee.recall.")
    if search_type is None or not hasattr(search_type, "GRAPH_COMPLETION"):
        raise CogneeIntegrationError("Imported Cognee SDK does not expose SearchType.GRAPH_COMPLETION.")

    kwargs: dict[str, Any] = {
        "query_text": contract.query_text,
        "query_type": search_type.GRAPH_COMPLETION,
        "top_k": contract.top_k,
        "scope": "graph",
        "auto_route": False,
        "node_name": contract.node_sets,
        "node_name_filter_operator": "AND",
        "only_context": True,
    }
    if contract.datasets:
        kwargs["datasets"] = contract.datasets
    return await invoke_maybe_async(recall_fn, kwargs)


def validate_contract(contract: SearchContract, catalogs: CatalogBundle) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    ns_map = node_set_map(contract.node_sets)
    keys = set(ns_map)

    if not contract.node_sets:
        errors.append("contract_has_no_node_sets")
    if "__malformed__" in keys:
        errors.append(f"contract_has_malformed_nodesets:{ns_map['__malformed__']}")
    if not contract.query_text.strip():
        errors.append("contract_has_empty_query_text")
    if contract.top_k <= 0:
        errors.append("contract_top_k_must_be_positive")
    if contract.allowed_card_types and "card_type" not in keys:
        errors.append("allowed_card_types_present_but_no_card_type_nodeset")
    if contract.allowed_card_types and first_node_set(ns_map, "card_type") not in contract.allowed_card_types:
        errors.append("card_type_nodeset_not_in_allowed_card_types")

    if contract.stage.startswith("runtime_"):
        for key in ["domain_family", "card_type", "tenant_id", "group_id"]:
            if key not in keys:
                errors.append(f"runtime_contract_missing_{key}")
    if contract.stage.startswith("table_local_") or contract.stage.startswith("semantic_table_"):
        for key in ["card_type", "table_id"]:
            if key not in keys:
                errors.append(f"table_contract_missing_{key}")

    template = catalogs.template_for_stage(contract.stage)
    if template:
        for key in template.get("required_node_set_keys") or []:
            if key not in keys:
                errors.append(f"contract_missing_template_required_nodeset_key:{key}")
        template_card_type = template.get("card_type")
        if template_card_type and first_node_set(ns_map, "card_type") != template_card_type:
            errors.append(f"contract_card_type_does_not_match_template:{template_card_type}")
    else:
        warnings.append("stage_has_no_catalog_template")

    table_id = first_node_set(ns_map, "table_id")
    if table_id and not catalogs.known_table_id(table_id):
        errors.append(f"unknown_table_id_in_contract:{table_id}")
    for canonical_id in contract.expected_card_ids:
        if canonical_id and not catalogs.known_card_id(canonical_id):
            errors.append(f"unknown_expected_card_id:{canonical_id}")

    return {"ok": not errors, "errors": errors, "warnings": warnings, "node_set_keys": sorted(k for k in keys if k != "__malformed__")}


def validate_returned_items(
    contract: SearchContract,
    items: list[Any],
    catalogs: CatalogBundle,
) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    warnings: list[dict[str, Any]] = []
    if not items:
        errors.append({"error": "no_results_returned"})
        return {"ok": False, "errors": errors, "warnings": warnings, "returned_count": 0}

    matched = [item for item in items if item_matches_expected_id(item, contract.expected_card_ids)]
    if contract.expected_card_ids and not matched:
        errors.append({"error": "expected_card_not_returned", "expected_card_ids": contract.expected_card_ids})
        matched = items

    for item in matched:
        text = result_text(item)
        structured_node_sets = set(find_first_key(item, "node_sets") or find_first_key(item, "ingestion_node_sets") or [])
        if structured_node_sets:
            missing = sorted(set(contract.node_sets) - structured_node_sets)
            if missing:
                errors.append({"error": "returned_card_missing_required_nodesets", "missing": missing})
        elif not all(node_set in text for node_set in contract.node_sets):
            errors.append({"error": "returned_text_missing_required_nodesets", "missing": [ns for ns in contract.node_sets if ns not in text]})

        card_type = find_first_key(item, "card_type")
        if card_type and contract.allowed_card_types and card_type not in contract.allowed_card_types:
            errors.append({"error": "returned_card_type_not_allowed", "card_type": card_type})
        elif contract.allowed_card_types and not card_type:
            if not any(f"card_type:{ctype}" in text or f"card_type: `{ctype}`" in text for ctype in contract.allowed_card_types):
                errors.append({"error": "returned_text_missing_allowed_card_type", "allowed_card_types": contract.allowed_card_types})

        canonical_id = find_first_key(item, "canonical_id") or find_first_key(item, "id")
        if canonical_id and not catalogs.known_card_id(str(canonical_id)):
            warnings.append({"canonical_id": canonical_id, "warning": "returned_card_not_in_generated_catalog"})

    return {"ok": not errors, "errors": errors, "warnings": warnings, "returned_count": len(items)}


def normalize_search_result(result: Any) -> list[Any]:
    if result is None:
        return []
    if isinstance(result, list):
        out: list[Any] = []
        for item in result:
            out.extend(normalize_search_result(item))
        return out
    if hasattr(result, "model_dump"):
        return [result.model_dump(mode="json")]
    if isinstance(result, dict):
        for key in ("results", "items", "documents", "cards", "chunks"):
            value = result.get(key)
            if isinstance(value, list):
                return normalize_search_result(value)
        return [result]
    return [result]


def returned_card_ids(items: list[Any], expected_ids: list[str]) -> list[str]:
    out: list[str] = []
    for item in items:
        direct = find_first_key(item, "canonical_id") or find_first_key(item, "id")
        if direct:
            out.append(str(direct))
            continue
        text = result_text(item)
        for expected in expected_ids:
            if expected in text and expected not in out:
                out.append(expected)
    return out


def item_matches_expected_id(item: Any, expected_ids: list[str]) -> bool:
    if not expected_ids:
        return True
    direct = find_first_key(item, "canonical_id") or find_first_key(item, "id")
    if direct and str(direct) in expected_ids:
        return True
    text = result_text(item)
    return any(expected in text for expected in expected_ids)


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


def result_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return "\n".join(result_text(item) for item in value.values())
    if isinstance(value, list):
        return "\n".join(result_text(item) for item in value)
    return repr(value)


def node_set_map(node_sets: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for raw in node_sets:
        text = str(raw)
        if ":" not in text:
            out.setdefault("__malformed__", []).append(text)
            continue
        key, value = text.split(":", 1)
        out.setdefault(key, []).append(value)
    return out


def first_node_set(ns_map: dict[str, list[str]], key: str) -> Optional[str]:
    values = ns_map.get(key) or []
    return values[0] if values else None


def load_search_callable(dotted_path: Optional[str]) -> Any:
    if dotted_path:
        module_name, attr_name = dotted_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        fn = getattr(module, attr_name)
        if not callable(fn):
            raise CogneeIntegrationError(f"Configured search callable is not callable: {dotted_path}")
        if not callable_accepts_kwarg(fn, "node_set") and not callable_accepts_kwarg(fn, "node_name"):
            raise CogneeIntegrationError(f"Configured search callable does not accept node_set or node_name: {dotted_path}")
        return fn
    search_fn = getattr(load_cognee_sdk(), "search", None)
    if search_fn is None:
        raise CogneeIntegrationError("Imported Cognee SDK does not expose cognee.search.")
    if not callable_accepts_kwarg(search_fn, "node_set") and not callable_accepts_kwarg(search_fn, "node_name"):
        raise CogneeIntegrationError(
            "Imported cognee.search does not accept node_set or node_name. "
            "Pass --search-callable for a NodeSet-capable search wrapper or use a compatible Cognee SDK/runtime."
        )
    return search_fn


def nodeset_search_kwargs(search_fn: Any, contract: SearchContract) -> dict[str, Any]:
    if callable_accepts_kwarg(search_fn, "node_set"):
        return {"node_set": contract.node_sets}
    if callable_accepts_kwarg(search_fn, "node_name"):
        return {
            "node_name": contract.node_sets,
            "node_name_filter_operator": "AND",
        }
    raise CogneeIntegrationError("Search callable does not accept NodeSet filtering kwargs.")


async def invoke_maybe_async(fn: Any, kwargs: dict[str, Any]) -> Any:
    if inspect.iscoroutinefunction(fn):
        result = fn(**kwargs)
    else:
        result = await asyncio.to_thread(fn, **kwargs)
    if inspect.isawaitable(result):
        return await result
    return result


def callable_accepts_kwarg(fn: Any, key: str) -> bool:
    try:
        signature = inspect.signature(fn)
    except (TypeError, ValueError):
        return True
    for parameter in signature.parameters.values():
        if parameter.kind == inspect.Parameter.VAR_KEYWORD:
            return True
        if parameter.name == key:
            return True
    return False


def load_cognee_sdk() -> Any:
    saved_path = list(sys.path)
    try:
        sys.path = sdk_import_path(saved_path)
        module = importlib.import_module("cognee")
    except Exception as exc:  # noqa: BLE001
        raise CogneeIntegrationError("Cognee SDK is not importable in this environment.") from exc
    finally:
        sys.path = saved_path
    return module


def sdk_import_path(paths: Iterable[str]) -> list[str]:
    filtered: list[str] = []
    for entry in paths:
        resolved = Path(entry or os.getcwd()).resolve()
        if resolved == REPO_ROOT:
            continue
        filtered.append(entry)
    return filtered


def datasets_from_pack(pack_dir: Path) -> list[str]:
    batches = read_jsonl(pack_dir / "cognee_ingestion" / "cognify_batches.jsonl")
    datasets: list[str] = []
    for batch in batches:
        for dataset in batch.get("datasets") or []:
            if dataset not in datasets:
                datasets.append(str(dataset))
    return datasets


def add_batch_dataset_index(pack_dir: Path) -> dict[str, list[str]]:
    rows = read_jsonl(pack_dir / "cognee_ingestion" / "add_batches.jsonl")
    index: dict[str, list[str]] = {}
    for row in rows:
        dataset = str(row.get("dataset_name") or "")
        if not dataset:
            continue
        for canonical_id in row.get("canonical_ids") or []:
            index.setdefault(str(canonical_id), [])
            if dataset not in index[str(canonical_id)]:
                index[str(canonical_id)].append(dataset)
    return index


def route_probe_datasets(
    probes: list[SearchContract],
    dataset_index: dict[str, list[str]],
    configured_datasets: list[str],
) -> list[SearchContract]:
    configured = set(configured_datasets)
    routed: list[SearchContract] = []
    for probe in probes:
        target_datasets = unique_in_order(
            dataset
            for expected_id in probe.expected_card_ids
            for dataset in dataset_index.get(expected_id, [])
            if dataset in configured
        )
        routed.append(replace(probe, datasets=target_datasets or probe.datasets))
    return routed


def dataset_routing_summary(
    contract: SearchContract,
    *,
    configured_datasets: list[str],
    explicit_datasets: bool,
    all_datasets: bool,
) -> dict[str, Any]:
    return {
        "configured_dataset_count": len(configured_datasets),
        "effective_dataset_count": len(contract.datasets),
        "explicit_datasets": explicit_datasets,
        "all_datasets": all_datasets,
        "routed": not explicit_datasets and not all_datasets and len(contract.datasets) < len(configured_datasets),
    }


def unique_in_order(values: Iterable[str]) -> list[str]:
    out: list[str] = []
    for value in values:
        if value and value not in out:
            out.append(value)
    return out


def write_probe_result(
    pack_dir: Path,
    *,
    status: str,
    mode: str,
    datasets: list[str],
    configured_datasets: list[str],
    trace: list[dict[str, Any]],
) -> dict[str, Any]:
    out_path = pack_dir / "traces" / "cognee_ingestion_probe_result.json"
    payload = {
        "status": status,
        "mode": mode,
        "datasets": datasets,
        "configured_datasets": configured_datasets,
        "probe_count": len(trace),
        "trace": trace,
        "output_path": str(out_path),
    }
    write_json(out_path, payload)
    return payload


def resolve_pack_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


def read_json(path: Path) -> Any:
    if not path.exists():
        raise RuntimeError(f"Missing JSON file: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise RuntimeError(f"Missing JSONL file: {path}")
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                value = json.loads(line)
            except json.JSONDecodeError as exc:
                raise RuntimeError(f"Invalid JSON on {path}:{line_number}: {exc}") from exc
            if not isinstance(value, dict):
                raise RuntimeError(f"Expected object on {path}:{line_number}")
            rows.append(value)
    return rows


if __name__ == "__main__":
    raise SystemExit(main())
