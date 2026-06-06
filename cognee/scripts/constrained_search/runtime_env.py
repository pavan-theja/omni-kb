from __future__ import annotations

import os
from pathlib import Path
from typing import Mapping


REPO_ROOT = Path(__file__).resolve().parents[3]
PROVIDER_CHOICES = ("auto", "azure", "vertex")


def configure_cognee_environment(pack_dir: Path, *, env_file: Path | None, provider: str) -> None:
    pack_dir = resolve_optional_path(pack_dir)
    values: dict[str, str] = {}
    if env_file:
        values = load_env_file(resolve_optional_path(env_file))
        apply_llm_env(values, provider=provider)
        apply_cognee_runtime_env(values)
    apply_cognee_runtime_defaults()
    runtime_dir = pack_dir / "cognee_runtime"
    apply_pack_runtime_dirs(runtime_dir)
    register_optional_provider_adapters()


def register_optional_provider_adapters() -> None:
    vector_provider = os.environ.get("VECTOR_DB_PROVIDER", "").strip().lower()
    if vector_provider != "qdrant":
        return
    try:
        import cognee_community_vector_adapter_qdrant.register  # noqa: F401
    except ImportError as exc:
        raise RuntimeError(
            "VECTOR_DB_PROVIDER=qdrant requires cognee-community-vector-adapter-qdrant "
            "and qdrant-client in the active .venv."
        ) from exc


def apply_pack_runtime_dirs(runtime_dir: Path) -> None:
    runtime_dir = runtime_dir.resolve()
    os.environ["DATA_ROOT_DIRECTORY"] = str(runtime_dir / "data")
    os.environ["SYSTEM_ROOT_DIRECTORY"] = str(runtime_dir / "system")
    os.environ["CACHE_ROOT_DIRECTORY"] = str(runtime_dir / "cache")
    os.environ["COGNEE_LOGS_DIR"] = str(runtime_dir / "logs")


def apply_cognee_runtime_env(values: Mapping[str, str]) -> None:
    for key in (
        "COGNEE_SKIP_CONNECTION_TEST",
        "REQUIRE_AUTHENTICATION",
        "ENABLE_BACKEND_ACCESS_CONTROL",
        "ENV",
        "CORS_ALLOWED_ORIGINS",
        "TELEMETRY_DISABLED",
        "LOG_LEVEL",
        "COGNEE_RUNTIME_KEY",
        "DB_PROVIDER",
        "DB_NAME",
        "DB_HOST",
        "DB_PORT",
        "DB_USERNAME",
        "DB_PASSWORD",
        "DATABASE_CONNECT_ARGS",
        "POOL_ARGS",
        "GRAPH_DATABASE_PROVIDER",
        "GRAPH_DATABASE_URL",
        "GRAPH_DATABASE_NAME",
        "GRAPH_DATABASE_USERNAME",
        "GRAPH_DATABASE_PASSWORD",
        "GRAPH_DATABASE_PORT",
        "VECTOR_DB_PROVIDER",
        "VECTOR_DB_URL",
        "VECTOR_DB_KEY",
        "VECTOR_DB_PORT",
        "VECTOR_DB_NAME",
        "VECTOR_DB_USERNAME",
        "VECTOR_DB_PASSWORD",
        "VECTOR_DB_HOST",
        "VECTOR_DATASET_DATABASE_HANDLER",
        "VECTOR_DB_SUBPROCESS_ENABLED",
        "CACHING",
    ):
        value = values.get(key)
        if value is None:
            continue
        os.environ[key] = host_safe_runtime_value(value)


def apply_cognee_runtime_defaults() -> None:
    os.environ.setdefault("REQUIRE_AUTHENTICATION", "false")
    os.environ.setdefault("ENABLE_BACKEND_ACCESS_CONTROL", "false")
    os.environ.setdefault("ENV", "local")
    os.environ.setdefault("CORS_ALLOWED_ORIGINS", "*")
    os.environ.setdefault("TELEMETRY_DISABLED", "true")
    os.environ.setdefault("COGNEE_SKIP_CONNECTION_TEST", "true")
    os.environ.setdefault("LOG_LEVEL", "INFO")


def host_safe_runtime_value(value: str) -> str:
    if running_in_container() or preserve_docker_host_internal():
        return value
    return value.replace("host.docker.internal", "localhost")


def running_in_container() -> bool:
    return Path("/.dockerenv").exists()


def preserve_docker_host_internal() -> bool:
    return os.environ.get("COGNEE_PRESERVE_DOCKER_HOST_INTERNAL", "").strip().lower() in {
        "1",
        "true",
        "yes",
    }


def resolve_optional_path(path: Path) -> Path:
    path = path.expanduser()
    if path.is_absolute():
        return path
    return (REPO_ROOT / path).resolve()


def load_env_file(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    values: dict[str, str] = {}
    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def apply_llm_env(values: Mapping[str, str], *, provider: str) -> None:
    selected_provider = select_provider(values, provider)
    if selected_provider == "azure":
        apply_runtime_values(azure_runtime(values))
    elif selected_provider == "vertex":
        apply_runtime_values(vertex_runtime(values))

    for key in (
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
        "EMBEDDING_BATCH_SIZE",
        "EMBEDDING_MAX_COMPLETION_TOKENS",
        "HUGGINGFACE_TOKENIZER",
        "VERTEXAI_PROJECT",
        "VERTEXAI_LOCATION",
        "GOOGLE_CLOUD_PROJECT",
        "GOOGLE_APPLICATION_CREDENTIALS",
    ):
        value = values.get(key)
        if not value:
            continue
        if key == "GOOGLE_APPLICATION_CREDENTIALS":
            value = resolve_google_credentials_path(value)
            current = os.environ.get(key)
            if current and Path(current).expanduser().exists():
                continue
            os.environ[key] = value
        else:
            os.environ[key] = value


def select_provider(values: Mapping[str, str], provider: str) -> str:
    selected = normalize_provider(provider)
    if selected:
        return selected
    for key in ("COGNEE_LLM_PROVIDER", "COGNEE_EMBEDDING_PROVIDER", "LLM_PROVIDER", "EMBEDDING_PROVIDER"):
        selected = normalize_provider(values.get(key, ""))
        if selected:
            return selected
    if values.get("AZURE_API_KEY"):
        return "azure"
    if first_value(values, "VERTEXAI_PROJECT", "VERTEX_AI_PROJECT_ID", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT"):
        return "vertex"
    return ""


def normalize_provider(value: str) -> str:
    normalized = (value or "").strip().lower().replace("-", "_")
    aliases = {
        "azure_openai": "azure",
        "vertex_ai": "vertex",
        "google_vertex": "vertex",
        "google_vertex_ai": "vertex",
    }
    provider = aliases.get(normalized, normalized)
    return provider if provider in {"azure", "vertex"} else ""


def azure_runtime(values: Mapping[str, str]) -> dict[str, str]:
    azure_base = values.get("AZURE_API_BASE", "").rstrip("/")
    azure_key = values.get("AZURE_API_KEY", "")
    azure_version = values.get("AZURE_API_VERSION", "")
    llm_deployment = values.get("AZURE_OPENAI_DEPLOYMENT", "gpt-4o-mini")
    embedding_deployment = values.get("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-3-small")
    return {
        "LLM_PROVIDER": "openai",
        "LLM_MODEL": f"azure/{llm_deployment}",
        "LLM_ENDPOINT": f"{azure_base}/openai/deployments/{llm_deployment}" if azure_base else "",
        "LLM_API_KEY": azure_key,
        "LLM_API_VERSION": azure_version,
        "EMBEDDING_PROVIDER": "openai",
        "EMBEDDING_MODEL": f"azure/{embedding_deployment}",
        "EMBEDDING_ENDPOINT": (
            f"{azure_base}/openai/deployments/{embedding_deployment}" if azure_base else ""
        ),
        "EMBEDDING_API_KEY": azure_key,
        "EMBEDDING_API_VERSION": azure_version,
        "EMBEDDING_DIMENSIONS": first_value(values, "EMBEDDING_DIMENSIONS", default="1536"),
    }


def vertex_runtime(values: Mapping[str, str]) -> dict[str, str]:
    project = first_value(values, "VERTEXAI_PROJECT", "VERTEX_AI_PROJECT_ID", "GOOGLE_CLOUD_PROJECT", "GCLOUD_PROJECT")
    location = first_value(values, "VERTEXAI_LOCATION", "VERTEX_AI_LOCATION", default="us-central1")
    credentials_file = resolve_google_credentials_path(
        first_value(values, "GOOGLE_APPLICATION_CREDENTIALS", "VERTEX_AI_SERVICE_ACCOUNT_FILE")
    )
    llm_model = first_value(values, "VERTEX_AI_LLM_MODEL", "VERTEX_LLM_MODEL", "GEMINI_LLM_MODEL", default="gemini-2.0-flash")
    embedding_model = values.get("VERTEX_AI_EMBEDDING_MODEL", "gemini-embedding-001")

    runtime = {
        "LLM_PROVIDER": "custom",
        "LLM_MODEL": with_prefix(llm_model, "vertex_ai"),
        "LLM_ENDPOINT": values.get("VERTEX_AI_LLM_ENDPOINT", ""),
        "LLM_API_KEY": first_value(values, "LLM_API_KEY", default="vertex-adc"),
        "LLM_API_VERSION": "",
        "EMBEDDING_PROVIDER": "custom",
        "EMBEDDING_MODEL": with_prefix(embedding_model, "vertex_ai"),
        "EMBEDDING_ENDPOINT": values.get("VERTEX_AI_EMBEDDING_ENDPOINT", ""),
        "EMBEDDING_API_KEY": first_value(values, "EMBEDDING_API_KEY", default="vertex-adc"),
        "EMBEDDING_API_VERSION": "",
        "EMBEDDING_DIMENSIONS": first_value(
            values,
            "VERTEX_AI_EMBEDDING_DIMENSIONALITY",
            "EMBEDDING_DIMENSIONS",
            default="1536",
        ),
        "VERTEXAI_PROJECT": project,
        "VERTEXAI_LOCATION": location,
        "GOOGLE_CLOUD_PROJECT": project,
    }
    if credentials_file:
        runtime["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file
    return runtime


def apply_runtime_values(values: Mapping[str, str]) -> None:
    for key, value in values.items():
        if not value:
            continue
        if key == "GOOGLE_APPLICATION_CREDENTIALS":
            current = os.environ.get(key)
            if current and Path(current).expanduser().exists():
                continue
            os.environ[key] = resolve_google_credentials_path(value)
        else:
            os.environ[key] = value


def first_value(values: Mapping[str, str], *keys: str, default: str = "") -> str:
    for key in keys:
        value = values.get(key, "")
        if value:
            return value
    return default


def with_prefix(model: str, prefix: str) -> str:
    if "/" in model:
        return model
    return f"{prefix}/{model}"


def resolve_google_credentials_path(value: str) -> str:
    raw = (value or "").strip()
    if not raw:
        return ""

    path = Path(raw).expanduser()
    if path.exists():
        return str(path.resolve())

    candidates: list[Path] = []
    if not path.is_absolute():
        candidates.append((REPO_ROOT / path).resolve())

    filename = path.name
    if filename:
        candidates.extend(
            [
                REPO_ROOT / "cognee" / "runtime" / "google-credentials" / filename,
                REPO_ROOT / ".google-credentials" / filename,
                REPO_ROOT / "cognee" / ".google-credentials" / filename,
            ]
        )

    for candidate in candidates:
        if candidate.exists():
            return str(candidate.resolve())
    return raw
