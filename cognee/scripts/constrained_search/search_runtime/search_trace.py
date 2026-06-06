from __future__ import annotations

import argparse
import asyncio
import os
import sys
from pathlib import Path
from typing import Any, Optional, Sequence

from runtime_env import PROVIDER_CHOICES, REPO_ROOT, configure_cognee_environment

from .catalogs import CatalogBundle
from .cognee_client import CogneeClient, CogneeIntegrationError, datasets_from_pack
from .contract_validator import validate_contract
from .llm_plane import CallableLLMProvider, LLMPlane, LiteLLMJSONProvider
from .search_state_machine import CogneeSearchStateMachine
from .utils import write_json


CONSTRAINED_SEARCH_DIR = Path(__file__).resolve().parents[1]
DEFAULT_PACK_DIR = REPO_ROOT / "build" / "constrained_search" / "build"
DEFAULT_ENV_FILE = REPO_ROOT / "cognee" / ".env"
DEFAULT_TENANT_ID = "tenant.mensa_brand_technologies_private_limited"
DEFAULT_GROUP_ID = "group.mensa_brand_technologies_private_limited.g8.gl22"


class NoProvider:
    async def complete_json(self, *, prompt_id: str, system_prompt: str, user_payload: dict[str, Any]) -> dict[str, Any]:
        raise RuntimeError(
            "No LLM provider configured. Use --provider vertex with a Vertex env file or pass --llm-callable dotted.path."
        )


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Run live Cognee constrained-search trace from NodeSet contracts.")
    parser.add_argument("--pack-dir", type=Path, default=DEFAULT_PACK_DIR)
    parser.add_argument("--env-file", type=Path, default=DEFAULT_ENV_FILE)
    parser.add_argument("--provider", choices=PROVIDER_CHOICES, default="auto")
    parser.add_argument("--query", required=True)
    parser.add_argument("--tenant-id", default=DEFAULT_TENANT_ID)
    parser.add_argument("--group-id", default=DEFAULT_GROUP_ID)
    parser.add_argument("--dataset", action="append", help="Dataset to search. Defaults to datasets from the pack.")
    parser.add_argument("--all-datasets", action="store_true", help="Disable add-batch dataset routing.")
    parser.add_argument("--llm-callable", help="Dotted path for a JSON LLM callable.")
    parser.add_argument("--max-steps", type=int, default=30)
    parser.add_argument("--dry-run", action="store_true", help="Validate pack, prompts, and runtime wiring without calling Cognee or an LLM.")
    parser.add_argument(
        "--llm-dry-run",
        "--plan-only",
        action="store_true",
        help="Call the LLM anchor extractor, validate/route emitted contracts, and stop before Cognee recall.",
    )
    args = parser.parse_args(argv)

    try:
        result = asyncio.run(run(args))
    except (CogneeIntegrationError, RuntimeError, ValueError) as exc:
        print(f"constrained search trace failed: {exc}", file=sys.stderr)
        return 1

    print(result["status"])
    print(result["trace_path"])
    return 0 if result["status"] in {"complete", "blocked", "dry_run", "llm_dry_run"} else 1


async def run(args: argparse.Namespace) -> dict[str, Any]:
    if args.max_steps < 1:
        raise ValueError("--max-steps must be >= 1")
    if args.dry_run and args.llm_dry_run:
        raise ValueError("Use only one of --dry-run or --llm-dry-run")
    validate_runtime_scope_args(args)

    pack_dir = resolve_pack_dir(args.pack_dir)
    configure_cognee_environment(pack_dir, env_file=args.env_file, provider=args.provider)
    catalogs = CatalogBundle.load(pack_dir)
    datasets = args.dataset or datasets_from_pack(pack_dir)
    if not datasets:
        raise RuntimeError("No datasets configured. Pass --dataset or build cognify_batches.jsonl first.")

    trace_dir = pack_dir / "traces"
    if args.dry_run:
        result = dry_run_result(pack_dir, datasets)
        write_json(result["trace_path"], result)
        return result
    if args.llm_dry_run:
        result = await llm_dry_run_result(args, pack_dir, catalogs, datasets)
        write_json(result["trace_path"], result)
        return result

    provider = provider_from_args(args)
    llm = LLMPlane(provider=provider, prompt_dir=CONSTRAINED_SEARCH_DIR / "prompts")
    client = CogneeClient(
        pack_dir=pack_dir,
        catalogs=catalogs,
        datasets=datasets,
        all_datasets=args.all_datasets,
    )
    machine = CogneeSearchStateMachine(
        client,
        llm,
        trace_dir,
        catalogs=catalogs,
        max_steps=args.max_steps,
    )
    return await machine.run_query(
        args.query,
        runtime_context=runtime_context_from_args(args, datasets),
    )


async def llm_dry_run_result(
    args: argparse.Namespace,
    pack_dir: Path,
    catalogs: CatalogBundle,
    datasets: list[str],
) -> dict[str, Any]:
    llm = LLMPlane(provider=provider_from_args(args), prompt_dir=CONSTRAINED_SEARCH_DIR / "prompts")
    client = CogneeClient(
        pack_dir=pack_dir,
        catalogs=catalogs,
        datasets=datasets,
        all_datasets=args.all_datasets,
    )
    trace_path = str(pack_dir / "traces" / "last_search_trace.json")
    runtime_context = runtime_context_from_args(args, datasets)
    trace: list[dict[str, Any]] = []

    try:
        anchor = await llm.extract_anchors(args.query, runtime_context)
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "blocked",
            "mode": "llm_dry_run",
            "blocked_reason": "anchor_extractor_failed",
            "error": repr(exc),
            "trace_path": trace_path,
            "trace": trace,
        }

    anchor_decision = anchor.to_dict()
    trace.append({"event": "llm_anchor_decision", "decision": anchor_decision})
    raw_contracts = anchor.validated_output.get("next_search_contracts", [])
    if not raw_contracts:
        return {
            "status": "blocked",
            "mode": "llm_dry_run",
            "blocked_reason": "anchor_extractor_did_not_emit_contracts",
            "trace_path": trace_path,
            "trace": trace,
        }

    machine = CogneeSearchStateMachine(
        client,
        llm,
        pack_dir / "traces",
        catalogs=catalogs,
        max_steps=args.max_steps,
    )
    contracts = machine._coerce_contracts(raw_contracts, "anchor_extractor", args.query)
    trace.extend(machine.trace)

    failed = not contracts
    valid_contract_count = 0
    for idx, contract in enumerate(contracts):
        routed_contract = client.with_routed_datasets(contract)
        validation = validate_contract(routed_contract, catalogs)
        if validation["ok"]:
            valid_contract_count += 1
        else:
            failed = True
        trace.append(
            {
                "event": "llm_contract_candidate_validated",
                "index": idx,
                "contract": routed_contract.to_dict(),
                "dataset_routing": {
                    "requested_dataset_count": len(contract.datasets),
                    "effective_dataset_count": len(routed_contract.datasets),
                    "datasets": routed_contract.datasets,
                },
                "validation": validation,
            }
        )

    return {
        "status": "blocked" if failed or valid_contract_count == 0 else "llm_dry_run",
        "mode": "llm_dry_run",
        "blocked_reason": "llm_emitted_invalid_contracts" if failed else None,
        "contract_count": len(raw_contracts),
        "expanded_contract_count": len(contracts),
        "valid_contract_count": valid_contract_count,
        "trace_path": trace_path,
        "trace": trace,
    }


def dry_run_result(pack_dir: Path, datasets: list[str]) -> dict[str, Any]:
    prompt_dir = CONSTRAINED_SEARCH_DIR / "prompts"
    prompt_files = sorted(path.name for path in prompt_dir.glob("*.md"))
    required_prompts = {
        "00_anchor_extractor.md",
        "01_runtime_binding_selector.md",
        "02_next_nodeset_planner.md",
        "03_bounded_candidate_ranker.md",
        "04_sql_handoff_writer.md",
    }
    missing = sorted(required_prompts - set(prompt_files))
    status = "failed" if missing else "dry_run"
    return {
        "status": status,
        "mode": "dry_run",
        "trace_path": str(pack_dir / "traces" / "last_search_trace.json"),
        "dataset_count": len(datasets),
        "datasets": datasets,
        "prompt_files": prompt_files,
        "missing_prompts": missing,
    }


def provider_from_args(args: argparse.Namespace) -> CallableLLMProvider | LiteLLMJSONProvider | NoProvider:
    if args.llm_callable:
        return CallableLLMProvider.from_dotted_path(args.llm_callable)
    if should_use_builtin_litellm_provider(args):
        return LiteLLMJSONProvider()
    return NoProvider()


def should_use_builtin_litellm_provider(args: argparse.Namespace) -> bool:
    model = os.environ.get("LLM_MODEL", "").strip().lower()
    if args.provider == "vertex":
        return True
    return model.startswith("vertex_ai/")


def runtime_context_from_args(args: argparse.Namespace, datasets: list[str]) -> dict[str, Any]:
    return {
        "tenant_id": args.tenant_id,
        "group_id": args.group_id,
        "datasets": datasets,
    }


def validate_runtime_scope_args(args: argparse.Namespace) -> None:
    if args.dry_run:
        return
    missing: list[str] = []
    if not str(args.tenant_id or "").strip():
        missing.append("--tenant-id")
    if not str(args.group_id or "").strip():
        missing.append("--group-id")
    if missing:
        raise ValueError(
            f"{' and '.join(missing)} cannot be empty. "
            "Set TENANT_ID/GROUP_ID in this shell or pass the literal canonical IDs."
        )


def resolve_pack_dir(path: Path) -> Path:
    path = path.expanduser()
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path.resolve()


if __name__ == "__main__":
    raise SystemExit(main())
