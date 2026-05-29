from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Mapping


PROVIDER_CHOICES = ("runtime", "azure", "gemini", "vertex")


@dataclass(frozen=True)
class ProviderExpectation:
    llm_provider: str = "runtime"
    embedding_provider: str = "runtime"


@dataclass(frozen=True)
class CogneeRuntimeConfig:
    base_url: str
    dataset: str
    docs_dir: Path
    runtime_env: Path
    runtime_key: str = ""
    request_timeout: float = 600.0
    status_timeout: float = 30.0
    poll_interval: float = 15.0
    cognify_timeout: float = 21600.0
    provider_expectation: ProviderExpectation = ProviderExpectation()


def validate_runtime_providers(expectation: ProviderExpectation, runtime_env: Path) -> None:
    if expectation.llm_provider == "runtime" and expectation.embedding_provider == "runtime":
        return
    values = read_env_values(runtime_env)
    expected = {
        "llm": expectation.llm_provider,
        "embedding": expectation.embedding_provider,
    }
    for kind, provider in expected.items():
        if provider == "runtime":
            continue
        actual = values.get(f"ZENKB_COGNEE_{kind.upper()}_PROVIDER") or infer_runtime_provider(values, kind)
        if actual != provider:
            raise RuntimeError(
                f"Cognee runtime {kind} provider is {actual or 'unknown'} but "
                f"--{kind}-provider={provider} was requested. Restart with: "
                f"cognee/scripts/cognee_up.sh --{kind}-provider {provider}"
            )


def infer_runtime_provider(values: Mapping[str, str], kind: str) -> str:
    provider = values.get("LLM_PROVIDER" if kind == "llm" else "EMBEDDING_PROVIDER", "")
    model = values.get("LLM_MODEL" if kind == "llm" else "EMBEDDING_MODEL", "")
    if provider == "openai" and model.startswith("azure/"):
        return "azure"
    if provider == "gemini" or model.startswith("gemini/"):
        return "gemini"
    if model.startswith("vertex_ai/"):
        return "vertex"
    return provider


def read_env_values(path: Path) -> dict[str, str]:
    if not path.exists():
        raise RuntimeError(f"Missing {path}; start Cognee with cognee/scripts/cognee_up.sh first.")
    values: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values

