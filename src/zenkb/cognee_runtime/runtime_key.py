from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Mapping, Optional


def build_runtime_key(
    values: Mapping[str, str],
    *,
    profile: str,
    graph_model: Optional[Path] = None,
    custom_prompt: Optional[Path] = None,
) -> str:
    components = [
        profile,
        f"llm_{values.get('ZENKB_COGNEE_LLM_PROVIDER') or values.get('LLM_PROVIDER') or 'runtime'}",
        values.get("LLM_MODEL", ""),
        f"embed_{values.get('ZENKB_COGNEE_EMBEDDING_PROVIDER') or values.get('EMBEDDING_PROVIDER') or 'runtime'}",
        values.get("EMBEDDING_MODEL", ""),
        f"dim_{values.get('EMBEDDING_DIMENSIONS', '')}",
    ]
    graph_hash = file_hash(graph_model)
    prompt_hash = file_hash(custom_prompt)
    if graph_hash:
        components.append(f"graph_{graph_hash[:8]}")
    if prompt_hash:
        components.append(f"prompt_{prompt_hash[:8]}")
    return "__".join(_slug(component) for component in components if str(component).strip())


def file_hash(path: Optional[Path]) -> str:
    if not path or not path.exists() or not path.is_file():
        return ""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _slug(value: object) -> str:
    text = str(value).strip().lower()
    text = text.replace("/", "_").replace(".", "_")
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return text.strip("_") or "default"

