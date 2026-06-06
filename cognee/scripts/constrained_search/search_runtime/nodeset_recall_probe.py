from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional, Sequence

from runtime_env import PROVIDER_CHOICES, REPO_ROOT, configure_cognee_environment

from .catalogs import CatalogBundle
from .cognee_client import CogneeClient, CogneeIntegrationError, datasets_from_pack
from .contract_validator import validate_contract, validate_returned_cards
from .nodeset_contracts import SearchContract
from .utils import write_json


DEFAULT_PACK_DIR = REPO_ROOT / "build" / "constrained_search" / "build"
DEFAULT_ENV_FILE = REPO_ROOT / "cognee" / ".env"
OUTPUT_FILENAME = "manual_nodeset_recall_probe_result.json"


@dataclass(frozen=True, slots=True)
class ManualProbeSpec:
    contract_id: str
    expected_card_id: str
    stage: str
    query_text: str
    allowed_card_type: str
    node_set_keys: tuple[str, ...]
    top_k: int = 5


DEFAULT_PROBE_SPECS = [
    ManualProbeSpec(
        contract_id="manual.platform.amazon",
        expected_card_id="platform.amazon",
        stage="semantic_platform_search",
        query_text="Amazon platform canonical card",
        allowed_card_type="platform",
        node_set_keys=("card_type", "platform_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.platform.shopify",
        expected_card_id="platform.shopify",
        stage="semantic_platform_search",
        query_text="Shopify platform canonical card",
        allowed_card_type="platform",
        node_set_keys=("card_type", "platform_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.table.amazon_settlement",
        expected_card_id="table.zs_observe.amazon_settlement",
        stage="semantic_table_frame_search",
        query_text="Amazon settlement table frame",
        allowed_card_type="table",
        node_set_keys=("card_type", "table_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.table.flipkart_oms",
        expected_card_id="table.zs_recon_processor.flipkart_oms",
        stage="semantic_table_frame_search",
        query_text="Flipkart OMS table frame",
        allowed_card_type="table",
        node_set_keys=("card_type", "table_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.table.shopify_returns",
        expected_card_id="table.zs_observe.shopify_returns",
        stage="semantic_table_frame_search",
        query_text="Shopify returns table frame",
        allowed_card_type="table",
        node_set_keys=("card_type", "table_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.binding.mensa_amazon_settlement",
        expected_card_id=(
            "account_data_binding.mensa_brand_technologies_private_limited."
            "amazon_india.settlement.zs_observe_amazon_settlement"
        ),
        stage="runtime_account_binding_search",
        query_text="Mensa Amazon settlement runtime binding",
        allowed_card_type="account_data_binding",
        node_set_keys=(
            "card_type",
            "domain_family",
            "tenant_id",
            "group_id",
            "platform_account_id",
            "platform_id",
            "table_id",
            "source_role",
            "canonical_id",
        ),
    ),
    ManualProbeSpec(
        contract_id="manual.binding.tanvi_flipkart_settlement",
        expected_card_id=(
            "account_data_binding.tanvi_fitness_private_limited."
            "flipkart.settlement.zs_observe_flipkart_settlement"
        ),
        stage="runtime_account_binding_search",
        query_text="Tanvi Fitness Flipkart settlement runtime binding",
        allowed_card_type="account_data_binding",
        node_set_keys=(
            "card_type",
            "domain_family",
            "tenant_id",
            "group_id",
            "platform_account_id",
            "platform_id",
            "table_id",
            "source_role",
            "canonical_id",
        ),
    ),
    ManualProbeSpec(
        contract_id="manual.binding.rosenza_shopify_returns",
        expected_card_id=(
            "account_data_binding.rosenza_international_trading_l_l_c."
            "shopify_d2c.returns.zs_observe_shopify_returns"
        ),
        stage="runtime_account_binding_search",
        query_text="Rosenza Shopify returns runtime binding",
        allowed_card_type="account_data_binding",
        node_set_keys=(
            "card_type",
            "domain_family",
            "tenant_id",
            "group_id",
            "platform_account_id",
            "platform_id",
            "table_id",
            "source_role",
            "canonical_id",
        ),
    ),
    ManualProbeSpec(
        contract_id="manual.column.amazon_settlement_group_level",
        expected_card_id="column.zs_observe.amazon_settlement.group_level_id",
        stage="table_local_column_search",
        query_text="Amazon settlement group level scope column",
        allowed_card_type="column",
        node_set_keys=("card_type", "table_id", "column_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.column.flipkart_oms_order_id",
        expected_card_id="column.zs_recon_processor.flipkart_oms.order_id",
        stage="table_local_column_search",
        query_text="Flipkart OMS order id column",
        allowed_card_type="column",
        node_set_keys=("card_type", "table_id", "column_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.column.shopify_returns_refunded_payments",
        expected_card_id="column.zs_observe.shopify_returns.refunded_payments",
        stage="table_local_column_search",
        query_text="Shopify returns refunded payments column",
        allowed_card_type="column",
        node_set_keys=("card_type", "table_id", "column_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.metric.flipkart_order_count",
        expected_card_id="metric.flipkart.order_count",
        stage="exact_card_dereference_search",
        query_text="Flipkart order count metric",
        allowed_card_type="metric",
        node_set_keys=("card_type", "metric_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.reconciliation_profile.meesho_sales_settlement",
        expected_card_id="reconciliation_profile.meesho.sales_settlement",
        stage="exact_card_dereference_search",
        query_text="Meesho sales settlement reconciliation profile",
        allowed_card_type="reconciliation_profile",
        node_set_keys=("card_type", "reconciliation_profile_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.tenant.mensa",
        expected_card_id="tenant.mensa_brand_technologies_private_limited",
        stage="exact_card_dereference_search",
        query_text="Mensa tenant runtime card",
        allowed_card_type="tenant",
        node_set_keys=("card_type", "domain_family", "tenant_id", "canonical_id"),
    ),
    ManualProbeSpec(
        contract_id="manual.group.mensa_g8_gl22",
        expected_card_id="group.mensa_brand_technologies_private_limited.g8.gl22",
        stage="runtime_group_search",
        query_text="Mensa group runtime card",
        allowed_card_type="group",
        node_set_keys=("card_type", "domain_family", "tenant_id", "group_id", "canonical_id"),
    ),
]


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run manual NodeSet recall probes against a constrained-search pack.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--dataset", action="append", help="Dataset to search. Defaults to datasets from the pack.")
    parser.add_argument("--contract-id", action="append", help="Run only selected manual contract id(s).")
    parser.add_argument("--all-datasets", action="store_true", help="Disable add-batch dataset routing.")
    parser.add_argument("--dry-run", action="store_true", help="Validate contracts without calling Cognee recall.")
    parser.add_argument("--list-contracts", action="store_true", help="Print default contract ids and exit.")
    args = parser.parse_args(argv)

    if args.list_contracts:
        for spec in DEFAULT_PROBE_SPECS:
            print(spec.contract_id)
        return 0

    try:
        result = asyncio.run(run(args))
    except (CogneeIntegrationError, RuntimeError, ValueError) as exc:
        print(f"manual nodeset recall probe failed: {exc}", file=sys.stderr)
        return 1

    print(result["status"])
    print(result["output_path"])
    return 0 if result["status"] in {"passed", "dry_run"} else 1


async def run(args: argparse.Namespace) -> dict[str, Any]:
    pack_dir = resolve_pack_dir(args.pack_dir)
    configure_cognee_environment(pack_dir, env_file=args.env_file, provider=args.provider)
    catalogs = CatalogBundle.load(pack_dir)
    configured_datasets = args.dataset or datasets_from_pack(pack_dir)
    if not configured_datasets:
        raise RuntimeError("No datasets configured. Pass --dataset or build cognify_batches.jsonl first.")

    materialized_ids = materialized_card_ids(pack_dir)
    specs = selected_specs(args.contract_id)
    contracts = [
        build_contract(spec, catalogs, configured_datasets=configured_datasets)
        for spec in specs
    ]
    client = CogneeClient(
        pack_dir=pack_dir,
        catalogs=catalogs,
        datasets=configured_datasets,
        all_datasets=args.all_datasets,
    )

    trace: list[dict[str, Any]] = []
    failed = False
    started = time.perf_counter()

    for spec, contract in zip(specs, contracts):
        routed_contract = client.with_routed_datasets(contract)
        contract_validation = validate_contract(routed_contract, catalogs)
        materialized = spec.expected_card_id in materialized_ids
        if not materialized:
            failed = True
            contract_validation["ok"] = False
            contract_validation["errors"].append(f"expected_card_not_materialized:{spec.expected_card_id}")

        event: dict[str, Any] = {
            "contract": routed_contract.to_dict(),
            "expected_card_ids": [spec.expected_card_id],
            "contract_validation": contract_validation,
            "dataset_routing": {
                "configured_dataset_count": len(configured_datasets),
                "effective_dataset_count": len(routed_contract.datasets),
                "datasets": routed_contract.datasets,
                "all_datasets": args.all_datasets,
            },
            "materialized": materialized,
        }

        if args.dry_run or not contract_validation["ok"]:
            event["status"] = "contract_valid" if contract_validation["ok"] else "contract_invalid"
            trace.append(event)
            failed = failed or not contract_validation["ok"]
            continue

        search_started = time.perf_counter()
        try:
            cards = await client.search(routed_contract)
        except Exception as exc:  # noqa: BLE001
            failed = True
            event.update(
                {
                    "status": "search_failed",
                    "error": repr(exc),
                    "duration_seconds": round(time.perf_counter() - search_started, 3),
                }
            )
            trace.append(event)
            continue

        result_validation = validate_returned_cards(routed_contract, cards, catalogs)
        expected_validation = validate_expected_card(spec.expected_card_id, cards)
        if not expected_validation["ok"]:
            failed = True
        if not result_validation["ok"]:
            failed = True
        event.update(
            {
                "status": "passed" if result_validation["ok"] and expected_validation["ok"] else "failed",
                "duration_seconds": round(time.perf_counter() - search_started, 3),
                "returned_count": len(cards),
                "returned_card_ids": returned_card_ids(cards),
                "result_validation": result_validation,
                "expected_validation": expected_validation,
            }
        )
        trace.append(event)

    status = "dry_run" if args.dry_run and not failed else "failed" if failed else "passed"
    payload = {
        "status": status,
        "mode": "manual_nodeset_recall",
        "dry_run": args.dry_run,
        "configured_datasets": configured_datasets,
        "probe_count": len(trace),
        "passed_count": sum(1 for event in trace if event.get("status") in {"passed", "contract_valid"}),
        "failed_count": sum(1 for event in trace if event.get("status") in {"failed", "search_failed", "contract_invalid"}),
        "duration_seconds": round(time.perf_counter() - started, 3),
        "trace": trace,
        "output_path": str(pack_dir / "traces" / OUTPUT_FILENAME),
    }
    write_json(payload["output_path"], payload)
    return payload


def selected_specs(contract_ids: list[str] | None) -> list[ManualProbeSpec]:
    if not contract_ids:
        return list(DEFAULT_PROBE_SPECS)
    selected = set(contract_ids)
    known = {spec.contract_id for spec in DEFAULT_PROBE_SPECS}
    unknown = sorted(selected - known)
    if unknown:
        raise ValueError(f"Unknown manual contract id(s): {unknown}")
    return [spec for spec in DEFAULT_PROBE_SPECS if spec.contract_id in selected]


def build_contract(
    spec: ManualProbeSpec,
    catalogs: CatalogBundle,
    *,
    configured_datasets: list[str],
) -> SearchContract:
    card = catalogs.card_for_id(spec.expected_card_id)
    if not card:
        raise ValueError(f"Expected card is missing from catalog: {spec.expected_card_id}")
    node_sets = filter_node_sets(card.get("node_sets") or [], spec.node_set_keys)
    missing_keys = [key for key in spec.node_set_keys if not has_node_set_key(node_sets, key)]
    if missing_keys:
        raise ValueError(f"{spec.expected_card_id} missing NodeSet keys for probe: {missing_keys}")
    return SearchContract(
        contract_id=spec.contract_id,
        stage=spec.stage,
        query_text=spec.query_text,
        node_sets=node_sets,
        top_k=spec.top_k,
        datasets=configured_datasets,
        allowed_card_types=[spec.allowed_card_type],
        exact_dereference_ids=[spec.expected_card_id],
        reason="manual_nodeset_recall_probe",
    )


def filter_node_sets(node_sets: list[str], allowed_keys: tuple[str, ...]) -> list[str]:
    allowed = set(allowed_keys)
    return [node_set for node_set in node_sets if node_set_key(node_set) in allowed]


def has_node_set_key(node_sets: list[str], key: str) -> bool:
    return any(node_set_key(node_set) == key for node_set in node_sets)


def node_set_key(node_set: str) -> str:
    return str(node_set).split(":", 1)[0]


def validate_expected_card(expected_card_id: str, cards: list[dict[str, Any]]) -> dict[str, Any]:
    ids = returned_card_ids(cards)
    errors: list[dict[str, Any]] = []
    if not cards:
        errors.append({"error": "no_cards_returned"})
    if expected_card_id not in ids:
        errors.append({"error": "expected_card_not_returned", "expected_card_id": expected_card_id})
    return {"ok": not errors, "errors": errors, "returned_card_ids": ids}


def returned_card_ids(cards: list[dict[str, Any]]) -> list[str]:
    ids: list[str] = []
    for card in cards:
        canonical_id = str(card.get("canonical_id") or card.get("id") or "")
        if canonical_id and canonical_id not in ids:
            ids.append(canonical_id)
    return ids


def materialized_card_ids(pack_dir: Path) -> set[str]:
    path = pack_dir / "cognee_ingestion" / "add_manifest.jsonl"
    if not path.exists():
        return set()
    materialized: set[str] = set()
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            if "data_id': UUID" not in line:
                continue
            row = read_manifest_line(line)
            materialized.update(str(canonical_id) for canonical_id in row.get("canonical_ids") or [])
    return materialized


def read_manifest_line(line: str) -> dict[str, Any]:
    value = json.loads(line)
    if not isinstance(value, dict):
        raise RuntimeError("Expected object in add_manifest.jsonl")
    return value


def resolve_pack_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()
