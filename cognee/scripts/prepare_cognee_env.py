#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "src"))

from zenkb.cognee_runtime.runtime_key import build_runtime_key  # noqa: E402

COGNEE_DIR = REPO_ROOT / "cognee"
SOURCE_ENV = COGNEE_DIR / ".env"
RUNTIME_ENV = COGNEE_DIR / "runtime" / "cognee.env"
CURRENT_RUNTIME_ENV = COGNEE_DIR / "runtime" / "current_runtime.env"
RUNTIME_INSTANCES_DIR = COGNEE_DIR / "runtime" / "instances"
DEFAULT_GRAPH_MODEL = COGNEE_DIR / "canonical_graph_model.json"
DEFAULT_CUSTOM_PROMPT = COGNEE_DIR / "canonical_cognify_prompt.md"
PROVIDER_CHOICES = ("azure", "gemini", "vertex")
PROFILE_CHOICES = ("plain", "canonical", "custom")


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Prepare Cognee runtime environment from cognee/.env")
    parser.add_argument(
        "--env-file",
        type=Path,
        default=SOURCE_ENV,
        help="Source env file. Defaults to cognee/.env.",
    )
    parser.add_argument(
        "--profile",
        choices=PROFILE_CHOICES,
        help="Runtime profile used in provider-keyed local DB paths. Defaults to COGNEE_RUNTIME_PROFILE or canonical.",
    )
    parser.add_argument(
        "--runtime-key",
        help="Explicit runtime key. Defaults to a provider/model/schema/prompt-derived key.",
    )
    parser.add_argument(
        "--graph-model",
        type=Path,
        default=DEFAULT_GRAPH_MODEL,
        help="Graph model path included in the default runtime-key hash.",
    )
    parser.add_argument(
        "--custom-prompt",
        type=Path,
        default=DEFAULT_CUSTOM_PROMPT,
        help="Custom prompt path included in the default runtime-key hash.",
    )
    parser.add_argument(
        "--llm-provider",
        choices=PROVIDER_CHOICES,
        help="Provider for Cognee Cognify LLM calls. Defaults to COGNEE_LLM_PROVIDER or azure.",
    )
    parser.add_argument(
        "--embedding-provider",
        choices=PROVIDER_CHOICES,
        help="Provider for Cognee embedding calls. Defaults to COGNEE_EMBEDDING_PROVIDER or azure.",
    )
    args = parser.parse_args(argv)

    values = _read_env(args.env_file)
    profile = args.profile or values.get("COGNEE_RUNTIME_PROFILE") or "canonical"
    if profile not in PROFILE_CHOICES:
        raise SystemExit(f"Unsupported profile {profile!r}; expected one of: {', '.join(PROFILE_CHOICES)}")
    llm_provider = _provider_choice(args.llm_provider or values.get("COGNEE_LLM_PROVIDER"), default="azure")
    embedding_provider = _provider_choice(
        args.embedding_provider or values.get("COGNEE_EMBEDDING_PROVIDER"),
        default="azure",
    )

    runtime = dict(values)
    runtime.setdefault("REQUIRE_AUTHENTICATION", "false")
    runtime.setdefault("ENABLE_BACKEND_ACCESS_CONTROL", "false")
    runtime.setdefault("ENV", "local")
    runtime.setdefault("CORS_ALLOWED_ORIGINS", "*")
    runtime.setdefault("TELEMETRY_DISABLED", "true")
    runtime.setdefault("COGNEE_SKIP_CONNECTION_TEST", "false")
    runtime.setdefault("LOG_LEVEL", "INFO")
    runtime.setdefault("DB_PROVIDER", "sqlite")
    runtime.setdefault("GRAPH_DATABASE_PROVIDER", "kuzu")
    runtime.setdefault("VECTOR_DB_PROVIDER", "lancedb")
    runtime.setdefault("SYSTEM_ROOT_DIRECTORY", "/app/.cognee_system")
    runtime.setdefault("DATA_ROOT_DIRECTORY", "/app/.data_storage")
    runtime.update(_llm_runtime(values, llm_provider))
    runtime.update(_embedding_runtime(values, embedding_provider))
    runtime["COGNEE_RUNTIME_PROFILE"] = profile
    runtime["ZENKB_COGNEE_LLM_PROVIDER"] = llm_provider
    runtime["ZENKB_COGNEE_EMBEDDING_PROVIDER"] = embedding_provider
    if llm_provider == "vertex" or embedding_provider == "vertex":
        runtime.update(_vertex_runtime(values))
    runtime_graph_model = args.graph_model if profile != "plain" else None
    runtime_custom_prompt = args.custom_prompt if profile != "plain" else None
    runtime_key = args.runtime_key or build_runtime_key(
        runtime,
        profile=profile,
        graph_model=runtime_graph_model,
        custom_prompt=runtime_custom_prompt,
    )
    runtime["COGNEE_RUNTIME_KEY"] = runtime_key

    for warning in _configuration_warnings(values, llm_provider, embedding_provider, source_env=args.env_file):
        print(f"Warning: {warning}")

    instance_dir = RUNTIME_INSTANCES_DIR / runtime_key
    instance_env = instance_dir / "cognee.env"
    system_dir = instance_dir / "system"
    data_storage_dir = instance_dir / "data_storage"
    system_dir.mkdir(parents=True, exist_ok=True)
    (system_dir / "databases").mkdir(parents=True, exist_ok=True)
    data_storage_dir.mkdir(parents=True, exist_ok=True)
    instance_env.parent.mkdir(parents=True, exist_ok=True)
    RUNTIME_ENV.parent.mkdir(parents=True, exist_ok=True)

    _write_env(runtime, instance_env)
    # Keep a compatibility copy for existing ingestion commands and direct
    # `docker compose -f cognee/compose.yaml` usage.
    _write_env(runtime, RUNTIME_ENV)
    _write_current_runtime_env(
        CURRENT_RUNTIME_ENV,
        runtime_key=runtime_key,
        runtime_env=instance_env,
        system_dir=system_dir,
        data_storage_dir=data_storage_dir,
    )
    print(f"Runtime key: {runtime_key}")
    print(f"Wrote {instance_env}")
    print(f"Wrote {RUNTIME_ENV}")
    print(f"Wrote {CURRENT_RUNTIME_ENV}")
    return 0


def _provider_choice(value: str | None, *, default: str) -> str:
    normalized = (value or default).strip().lower().replace("-", "_")
    aliases = {
        "azure_openai": "azure",
        "google": "gemini",
        "google_ai": "gemini",
        "google_gemini": "gemini",
        "vertex_ai": "vertex",
        "google_vertex": "vertex",
    }
    provider = aliases.get(normalized, normalized)
    if provider not in PROVIDER_CHOICES:
        raise SystemExit(f"Unsupported provider {value!r}; expected one of: {', '.join(PROVIDER_CHOICES)}")
    return provider


def _llm_runtime(values: Mapping[str, str], provider: str) -> dict[str, str]:
    if provider == "azure":
        azure_base = values.get("AZURE_API_BASE", "").rstrip("/")
        azure_key = values.get("AZURE_API_KEY", "")
        azure_version = values.get("AZURE_API_VERSION", "")
        llm_deployment = values.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
        return {
            "LLM_PROVIDER": "openai",
            "LLM_MODEL": f"azure/{llm_deployment}",
            "LLM_ENDPOINT": f"{azure_base}/openai/deployments/{llm_deployment}" if azure_base else "",
            "LLM_API_KEY": azure_key,
            "LLM_API_VERSION": azure_version,
        }
    if provider == "gemini":
        api_key = _first_value(values, "GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_AI_API_KEY", "AI_STUDIO_API_KEY")
        model = values.get("GEMINI_LLM_MODEL", "gemini-2.0-flash")
        return {
            "LLM_PROVIDER": "gemini",
            "LLM_MODEL": _with_prefix(model, "gemini"),
            "LLM_ENDPOINT": values.get("GEMINI_LLM_ENDPOINT", ""),
            "LLM_API_KEY": api_key,
            "LLM_API_VERSION": values.get("GEMINI_API_VERSION", ""),
        }
    model = _first_value(values, "VERTEX_AI_LLM_MODEL", "VERTEX_LLM_MODEL", "GEMINI_LLM_MODEL", default="gemini-2.0-flash")
    return {
        "LLM_PROVIDER": "custom",
        "LLM_MODEL": _with_prefix(model, "vertex_ai"),
        "LLM_ENDPOINT": values.get("VERTEX_AI_LLM_ENDPOINT", ""),
        # Cognee validates custom LLM providers before LiteLLM reaches the Vertex
        # service-account auth path, so Vertex needs a non-empty placeholder here.
        "LLM_API_KEY": _first_value(values, "LLM_API_KEY", default="vertex-adc"),
        "LLM_API_VERSION": "",
    }


def _embedding_runtime(values: Mapping[str, str], provider: str) -> dict[str, str]:
    if provider == "azure":
        azure_base = values.get("AZURE_API_BASE", "").rstrip("/")
        azure_key = values.get("AZURE_API_KEY", "")
        azure_version = values.get("AZURE_API_VERSION", "")
        embedding_deployment = values.get(
            "AZURE_OPENAI_EMBEDDING_DEPLOYMENT",
            "text-embedding-3-small",
        )
        return {
            "EMBEDDING_PROVIDER": "openai",
            "EMBEDDING_MODEL": f"azure/{embedding_deployment}",
            "EMBEDDING_ENDPOINT": (
                f"{azure_base}/openai/deployments/{embedding_deployment}"
                if azure_base
                else ""
            ),
            "EMBEDDING_API_KEY": azure_key,
            "EMBEDDING_API_VERSION": azure_version,
            "EMBEDDING_DIMENSIONS": _first_value(values, "EMBEDDING_DIMENSIONS", default="1536"),
        }
    if provider == "gemini":
        api_key = _first_value(values, "GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_AI_API_KEY", "AI_STUDIO_API_KEY")
        model = values.get("GEMINI_EMBEDDING_MODEL", "gemini-embedding-001")
        return {
            "EMBEDDING_PROVIDER": "gemini",
            "EMBEDDING_MODEL": _with_prefix(model, "gemini"),
            "EMBEDDING_ENDPOINT": values.get("GEMINI_EMBEDDING_ENDPOINT", ""),
            "EMBEDDING_API_KEY": api_key,
            "EMBEDDING_API_VERSION": values.get("GEMINI_API_VERSION", ""),
            "EMBEDDING_DIMENSIONS": _first_value(
                values,
                "GEMINI_EMBEDDING_DIMENSIONS",
                "VERTEX_AI_EMBEDDING_DIMENSIONALITY",
                "EMBEDDING_DIMENSIONS",
                default="1536",
            ),
        }
    model = values.get("VERTEX_AI_EMBEDDING_MODEL", "gemini-embedding-001")
    return {
        "EMBEDDING_PROVIDER": "custom",
        "EMBEDDING_MODEL": _with_prefix(model, "vertex_ai"),
        "EMBEDDING_ENDPOINT": values.get("VERTEX_AI_EMBEDDING_ENDPOINT", ""),
        "EMBEDDING_API_KEY": _first_value(values, "EMBEDDING_API_KEY", default="vertex-adc"),
        "EMBEDDING_API_VERSION": "",
        "EMBEDDING_DIMENSIONS": _first_value(
            values,
            "VERTEX_AI_EMBEDDING_DIMENSIONALITY",
            "EMBEDDING_DIMENSIONS",
            default="1536",
        ),
    }


def _vertex_runtime(values: Mapping[str, str]) -> dict[str, str]:
    project = _first_value(values, "VERTEXAI_PROJECT", "VERTEX_AI_PROJECT_ID", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT")
    location = _first_value(values, "VERTEXAI_LOCATION", "VERTEX_AI_LOCATION", default="us-central1")
    credentials_file = _first_value(values, "GOOGLE_APPLICATION_CREDENTIALS", "VERTEX_AI_SERVICE_ACCOUNT_FILE")
    runtime = {
        "VERTEXAI_PROJECT": project,
        "VERTEXAI_LOCATION": location,
        "GOOGLE_CLOUD_PROJECT": project,
    }
    if credentials_file:
        runtime["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file
    return runtime


def _configuration_warnings(
    values: Mapping[str, str],
    llm_provider: str,
    embedding_provider: str,
    *,
    source_env: Path,
) -> list[str]:
    warnings = []
    if "azure" in {llm_provider, embedding_provider}:
        missing = [
            key
            for key in ("AZURE_API_BASE", "AZURE_API_KEY", "AZURE_API_VERSION")
            if not values.get(key)
        ]
        if missing:
            warnings.append(
                f"missing Azure settings in {source_env}: {', '.join(missing)}. "
                "Cognee may fail provider checks until these are set."
            )
    if "gemini" in {llm_provider, embedding_provider} and not _first_value(
        values,
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "GOOGLE_AI_API_KEY",
        "AI_STUDIO_API_KEY",
    ):
        warnings.append("Gemini provider selected but GEMINI_API_KEY/GOOGLE_API_KEY is not set.")
    if "vertex" in {llm_provider, embedding_provider}:
        if not _first_value(values, "VERTEX_AI_PROJECT_ID", "VERTEXAI_PROJECT", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT"):
            warnings.append("Vertex provider selected but VERTEX_AI_PROJECT_ID/GOOGLE_CLOUD_PROJECT is not set.")
        if not _first_value(values, "GOOGLE_APPLICATION_CREDENTIALS", "VERTEX_AI_SERVICE_ACCOUNT_FILE"):
            warnings.append(
                "Vertex provider selected but no container-visible GOOGLE_APPLICATION_CREDENTIALS, "
                "or VERTEX_AI_SERVICE_ACCOUNT_FILE is set."
            )
        access_token = values.get("VERTEX_AI_ACCESS_TOKEN", "")
        if access_token.startswith("AIza"):
            warnings.append(
                "VERTEX_AI_ACCESS_TOKEN looks like a Google API key. Cognee Vertex runtime should use "
                "a service-account JSON file mounted into the container."
            )
    return warnings


def _first_value(values: Mapping[str, str], *keys: str, default: str = "") -> str:
    for key in keys:
        value = values.get(key, "")
        if value:
            return value
    return default


def _with_prefix(model: str, prefix: str) -> str:
    return model if "/" in model else f"{prefix}/{model}"


def _read_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        raise SystemExit(f"Missing {path}")
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def _write_env(values: dict[str, str], path: Path) -> None:
    ordered_keys = [
        "COGNEE_RUNTIME_PROFILE",
        "COGNEE_RUNTIME_KEY",
        "COGNEE_LLM_PROVIDER",
        "COGNEE_EMBEDDING_PROVIDER",
        "ZENKB_COGNEE_LLM_PROVIDER",
        "ZENKB_COGNEE_EMBEDDING_PROVIDER",
        "AZURE_API_BASE",
        "AZURE_API_KEY",
        "AZURE_API_VERSION",
        "AZURE_OPENAI_DEPLOYMENT",
        "AZURE_OPENAI_EMBEDDING_DEPLOYMENT",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "GEMINI_LLM_MODEL",
        "GEMINI_EMBEDDING_MODEL",
        "GEMINI_EMBEDDING_DIMENSIONS",
        "VERTEX_AI_PROJECT_ID",
        "VERTEX_AI_QUOTA_PROJECT",
        "VERTEX_AI_LOCATION",
        "VERTEX_AI_LLM_MODEL",
        "VERTEX_AI_EMBEDDING_MODEL",
        "VERTEX_AI_EMBEDDING_DIMENSIONALITY",
        "VERTEXAI_PROJECT",
        "VERTEXAI_LOCATION",
        "GOOGLE_CLOUD_PROJECT",
        "GOOGLE_APPLICATION_CREDENTIALS",
        "VERTEX_AI_SERVICE_ACCOUNT_FILE",
        "VERTEX_AI_ACCESS_TOKEN",
        "LLM_PROVIDER",
        "LLM_MODEL",
        "LLM_ENDPOINT",
        "LLM_API_KEY",
        "LLM_API_VERSION",
        "EMBEDDING_PROVIDER",
        "EMBEDDING_MODEL",
        "EMBEDDING_ENDPOINT",
        "EMBEDDING_API_KEY",
        "EMBEDDING_API_VERSION",
        "EMBEDDING_DIMENSIONS",
        "DB_PROVIDER",
        "GRAPH_DATABASE_PROVIDER",
        "VECTOR_DB_PROVIDER",
        "SYSTEM_ROOT_DIRECTORY",
        "DATA_ROOT_DIRECTORY",
        "REQUIRE_AUTHENTICATION",
        "ENABLE_BACKEND_ACCESS_CONTROL",
        "CORS_ALLOWED_ORIGINS",
        "TELEMETRY_DISABLED",
        "COGNEE_SKIP_CONNECTION_TEST",
        "LOG_LEVEL",
        "ENV",
    ]
    seen = set()
    lines = []
    for key in ordered_keys:
        if key in values:
            lines.append(f"{key}={_quote(values[key])}")
            seen.add(key)
    for key in sorted(set(values) - seen):
        lines.append(f"{key}={_quote(values[key])}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_current_runtime_env(
    path: Path,
    *,
    runtime_key: str,
    runtime_env: Path,
    system_dir: Path,
    data_storage_dir: Path,
) -> None:
    values = {
        "COGNEE_RUNTIME_KEY": runtime_key,
        "COGNEE_RUNTIME_ENV": str(runtime_env.resolve()),
        "COGNEE_RUNTIME_ENV_FILE": str(runtime_env.resolve()),
        "COGNEE_RUNTIME_SYSTEM_DIR": str(system_dir.resolve()),
        "COGNEE_RUNTIME_DATA_DIR": str(data_storage_dir.resolve()),
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    _write_env(values, path)


def _quote(value: str) -> str:
    if value == "":
        return ""
    if any(char.isspace() for char in value):
        return '"' + value.replace('"', '\\"') + '"'
    return value


if __name__ == "__main__":
    raise SystemExit(main())
