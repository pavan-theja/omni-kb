from __future__ import annotations

import asyncio
import ast
import importlib
import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Protocol

from .nodeset_contracts import SearchContract


class LLMProvider(Protocol):
    async def complete_json(self, *, prompt_id: str, system_prompt: str, user_payload: dict[str, Any]) -> dict[str, Any]: ...


class CallableLLMProvider:
    """Adapter around a production JSON-completion callable."""

    def __init__(self, fn: Callable[..., Any]):
        self.fn = fn

    @classmethod
    def from_dotted_path(cls, dotted_path: str) -> "CallableLLMProvider":
        module_name, attr_name = dotted_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        fn = getattr(module, attr_name)
        if not callable(fn):
            raise TypeError(f"Configured LLM callable is not callable: {dotted_path}")
        return cls(fn)

    async def complete_json(self, *, prompt_id: str, system_prompt: str, user_payload: dict[str, Any]) -> dict[str, Any]:
        result = self.fn(prompt_id=prompt_id, system_prompt=system_prompt, user_payload=user_payload)
        if asyncio.iscoroutine(result):
            result = await result
        if not isinstance(result, dict):
            raise TypeError("LLM callable must return a JSON dictionary")
        return result


class LiteLLMJSONProvider:
    """JSON-completion provider backed by the configured LiteLLM model."""

    def __init__(
        self,
        *,
        model: str | None = None,
        temperature: float = 0.0,
        max_tokens: int = 4096,
        timeout: int = 120,
    ):
        self.model = (model or os.environ.get("LLM_MODEL") or "").strip()
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.timeout = timeout
        if not self.model:
            raise RuntimeError("LLM_MODEL is not set. Pass --env-file/--provider or --llm-callable.")

    async def complete_json(self, *, prompt_id: str, system_prompt: str, user_payload: dict[str, Any]) -> dict[str, Any]:
        try:
            import litellm
        except ImportError as exc:
            raise RuntimeError("Built-in JSON LLM provider requires litellm in the active .venv.") from exc

        messages = [
            {
                "role": "system",
                "content": system_prompt.strip() + "\n\nReturn one valid JSON object. Do not wrap it in markdown.",
            },
            {
                "role": "user",
                "content": json.dumps(user_payload, indent=2, ensure_ascii=False, sort_keys=True),
            },
        ]
        kwargs: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "timeout": self.timeout,
            "response_format": {"type": "json_object"},
        }
        try:
            result = await litellm.acompletion(**kwargs)
        except Exception as exc:  # noqa: BLE001
            if not supports_json_retry(exc):
                raise
            kwargs.pop("response_format", None)
            result = await litellm.acompletion(**kwargs)

        return parse_json_completion(result, prompt_id=prompt_id)


@dataclass(slots=True)
class LLMDecision:
    decision_id: str
    prompt_id: str
    input_payload: dict[str, Any]
    validated_output: dict[str, Any]

    def to_dict(self) -> dict[str, Any]:
        return {
            "decision_id": self.decision_id,
            "prompt_id": self.prompt_id,
            "input_payload": self.input_payload,
            "validated_output": self.validated_output,
        }


class LLMPlane:
    """Narrow LLM plane for contract generation and bounded ranking."""

    def __init__(self, provider: LLMProvider, prompt_dir: str | Path):
        self.provider = provider
        self.prompt_dir = Path(prompt_dir)

    def _prompt(self, prompt_id: str) -> str:
        matches = list(self.prompt_dir.glob(f"{prompt_id}*.md"))
        if not matches:
            raise FileNotFoundError(f"Prompt not found for id {prompt_id}")
        return matches[0].read_text(encoding="utf-8")

    async def extract_anchors(self, query_text: str, runtime_context: dict[str, Any]) -> LLMDecision:
        prompt_id = "00_anchor_extractor"
        payload = {"query_text": query_text, "runtime_context": runtime_context}
        raw = await self.provider.complete_json(prompt_id=prompt_id, system_prompt=self._prompt(prompt_id), user_payload=payload)
        _require_keys(raw, ["platform_mentions", "source_role_mentions", "operation_shape", "requires_relationship_search"], prompt_id)
        return LLMDecision("llm_anchor_001", prompt_id, payload, raw)

    async def select_runtime_bindings(self, query_text: str, anchor_decision: dict[str, Any], runtime_candidates: list[dict[str, Any]]) -> LLMDecision:
        prompt_id = "01_runtime_binding_selector"
        payload = {"query_text": query_text, "anchors": anchor_decision, "runtime_candidates": runtime_candidates}
        raw = await self.provider.complete_json(prompt_id=prompt_id, system_prompt=self._prompt(prompt_id), user_payload=payload)
        raw = normalize_runtime_binding_selector_output(raw, runtime_candidates)
        _require_keys(raw, ["selected_platform_account_ids", "selected_binding_ids", "rejected_candidate_ids", "next_search_contracts"], prompt_id)
        return LLMDecision("llm_runtime_binding_001", prompt_id, payload, raw)

    async def plan_next_nodesets(self, query_text: str, predecessor_result: dict[str, Any]) -> LLMDecision:
        prompt_id = "02_next_nodeset_planner"
        payload = {"query_text": query_text, "predecessor_result": predecessor_result}
        raw = await self.provider.complete_json(prompt_id=prompt_id, system_prompt=self._prompt(prompt_id), user_payload=payload)
        _require_keys(raw, ["next_search_contracts", "closed_gates", "blocked_reasons"], prompt_id)
        return LLMDecision("llm_next_nodeset_001", prompt_id, payload, raw)

    async def rank_bounded_candidates(self, query_text: str, contract: SearchContract, returned_cards: list[dict[str, Any]]) -> LLMDecision:
        prompt_id = "03_bounded_candidate_ranker"
        payload = {"query_text": query_text, "contract": contract.to_dict(), "returned_cards": returned_cards}
        raw = await self.provider.complete_json(prompt_id=prompt_id, system_prompt=self._prompt(prompt_id), user_payload=payload)
        raw = normalize_bounded_ranker_output(raw)
        _require_keys(raw, ["selected_card_ids", "rejected_card_ids", "next_search_contracts", "exact_dereference_requests"], prompt_id)
        return LLMDecision("llm_rank_001", prompt_id, payload, raw)

    async def write_sql_handoff(self, query_text: str, evidence_pack: dict[str, Any]) -> LLMDecision:
        prompt_id = "04_sql_handoff_writer"
        payload = {"query_text": query_text, "evidence_pack": evidence_pack}
        raw = await self.provider.complete_json(prompt_id=prompt_id, system_prompt=self._prompt(prompt_id), user_payload=payload)
        _require_keys(raw, ["handoff_status", "source_blocks", "blocked_reasons"], prompt_id)
        return LLMDecision("llm_sql_handoff_001", prompt_id, payload, raw)


def _require_keys(raw: dict[str, Any], keys: list[str], prompt_id: str) -> None:
    missing = [key for key in keys if key not in raw]
    if missing:
        raise ValueError(f"LLM output for {prompt_id} missing keys: {missing}")


def normalize_runtime_binding_selector_output(raw: dict[str, Any], runtime_candidates: list[dict[str, Any]]) -> dict[str, Any]:
    normalized = dict(raw)
    selected_alias_ids = first_list(
        normalized.get("selected_card_ids"),
        normalized.get("selected_candidate_ids"),
        normalized.get("selected_ids"),
    )
    platform_ids, binding_ids = runtime_selector_candidate_ids(runtime_candidates)

    if "selected_platform_account_ids" not in normalized:
        normalized["selected_platform_account_ids"] = [item for item in selected_alias_ids if item in platform_ids]
    if "selected_binding_ids" not in normalized:
        normalized["selected_binding_ids"] = [item for item in selected_alias_ids if item in binding_ids]
    normalized.setdefault("selected_table_ids", [])
    if "rejected_candidate_ids" not in normalized:
        normalized["rejected_candidate_ids"] = first_list(
            normalized.get("rejected_card_ids"),
            normalized.get("rejected_ids"),
        )
    normalized.setdefault("selection_reasons", {})
    normalized.setdefault("next_search_contracts", [])
    normalized.setdefault("blocked_reasons", [])
    return normalized


def normalize_bounded_ranker_output(raw: dict[str, Any]) -> dict[str, Any]:
    normalized = dict(raw)
    if "selected_card_ids" not in normalized:
        normalized["selected_card_ids"] = first_list(
            normalized.get("selected_binding_ids"),
            normalized.get("selected_domain_ids"),
            normalized.get("selected_table_ids"),
            normalized.get("selected_candidate_ids"),
            normalized.get("selected_ids"),
        )
    if "rejected_card_ids" not in normalized:
        normalized["rejected_card_ids"] = first_list(
            normalized.get("rejected_candidate_ids"),
            normalized.get("rejected_ids"),
        )
    normalized.setdefault("selection_reasons", {})
    normalized.setdefault("next_search_contracts", [])
    normalized.setdefault("exact_dereference_requests", [])
    normalized.setdefault("blocked_reasons", [])
    return normalized


def runtime_selector_candidate_ids(runtime_candidates: list[dict[str, Any]]) -> tuple[set[str], set[str]]:
    platform_ids: set[str] = set()
    binding_ids: set[str] = set()
    for candidate in runtime_candidates:
        canonical_id = str(candidate.get("canonical_id") or candidate.get("candidate_id") or "")
        card_type = str(candidate.get("card_type") or "")
        candidate_type = str(candidate.get("candidate_type") or "")
        if card_type == "platform_account" and canonical_id:
            platform_ids.add(canonical_id)
        if card_type == "account_data_binding" or candidate_type == "runtime_binding_table_candidate":
            binding_id = str(candidate.get("account_data_binding_id") or canonical_id)
            if binding_id:
                binding_ids.add(binding_id)
    return platform_ids, binding_ids


def first_list(*values: Any) -> list[str]:
    for value in values:
        if isinstance(value, list):
            return [str(item) for item in value]
    return []


def supports_json_retry(exc: Exception) -> bool:
    text = repr(exc).lower()
    return "response_format" in text or "json_object" in text or "json mode" in text


def parse_json_completion(result: Any, *, prompt_id: str) -> dict[str, Any]:
    if isinstance(result, dict):
        direct = result.get("validated_output")
        if isinstance(direct, dict):
            return direct

    content = completion_text(result)
    json_text = extract_json_object(content)
    try:
        value = json.loads(content)
    except json.JSONDecodeError:
        try:
            value = json.loads(json_text)
        except json.JSONDecodeError:
            try:
                value = ast.literal_eval(json_text)
            except (SyntaxError, ValueError) as exc:
                raise ValueError(f"LLM output for {prompt_id} is not parseable JSON: {content[:500]}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"LLM output for {prompt_id} must be a JSON object")
    return value


def completion_text(result: Any) -> str:
    if hasattr(result, "model_dump"):
        return completion_text(result.model_dump(mode="json"))
    if isinstance(result, dict):
        choices = result.get("choices") or []
        if choices:
            return completion_text(choices[0])
        message = result.get("message")
        if message is not None:
            return completion_text(message)
        content = result.get("content")
        if content is not None:
            return completion_text(content)
        text = result.get("text")
        if text is not None:
            return str(text)
    if isinstance(result, list):
        parts: list[str] = []
        for item in result:
            if isinstance(item, dict) and item.get("type") == "text":
                parts.append(str(item.get("text") or ""))
            else:
                parts.append(completion_text(item))
        return "\n".join(part for part in parts if part)
    return str(result)


def extract_json_object(text: str) -> str:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = stripped.removeprefix("```json").removeprefix("```").strip()
        if stripped.endswith("```"):
            stripped = stripped[:-3].strip()
    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError(f"LLM output is not valid JSON: {stripped[:500]}")
    return stripped[start : end + 1]
