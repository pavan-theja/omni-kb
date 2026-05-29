from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, Sequence


REQUIRED_CARD_FIELDS = (
    "card_type",
    "canonical_id",
    "name",
    "description",
    "status",
    "confidence",
    "source_documents",
    "created_by",
    "updated_by",
    "created_at",
    "updated_at",
)

VALID_STATUSES = {"draft", "active", "deprecated", "archived"}
VALID_CONFIDENCE = {
    "curated",
    "inferred",
    "experimental",
    "low_confidence",
    "unknown",
}

CARD_ID_RE = re.compile(r"^[a-z][a-z0-9_]*\.[a-z0-9][a-z0-9_.-]*$")
EDGE_TYPE_RE = re.compile(r"^[A-Z][A-Z0-9_]*$")

CARD_TYPE_ID_PREFIXES = {
    "formula_template": ("formula",),
    "metric_implementation": ("metric_impl",),
    "review_item": ("review",),
    "validation_test": ("validation",),
}

EDGE_TYPES = {
    "HAS_GROUP",
    "BELONGS_TO_TENANT",
    "HAS_PLATFORM_ACCOUNT",
    "BELONGS_TO_GROUP",
    "USES_PLATFORM",
    "HAS_PLATFORM_CONTEXT",
    "BELONGS_TO_PLATFORM",
    "HAS_DATA_BINDING",
    "BINDS_PLATFORM_ACCOUNT",
    "APPLIES_TO_TABLE",
    "INCLUDES_PLATFORM_ACCOUNT",
    "INCLUDED_IN_BUSINESS_SCOPE_SET",
    "HAS_BUSINESS_FLOW_BINDING",
    "USES_PLATFORM_ACCOUNT",
    "USES_SOURCE_ACCOUNT",
    "USES_TARGET_ACCOUNT",
    "USES_OPERATIONAL_EVIDENCE_ACCOUNT",
    "USES_SETTLEMENT_SOURCE_ACCOUNT",
    "USES_BANK_DESTINATION_ACCOUNT",
    "USES_ACCOUNT_DATA_BINDING",
    "USES_TABLE",
    "USES_RELATIONSHIP",
    "SUPPORTS_PROCESS",
    "SUPPORTS_RECONCILIATION_PROFILE",
    "USES_QUERY_PATTERN",
    "USES_EXECUTION_CONSTRAINT_SET",
    "HAS_COLUMN",
    "HAS_VALUE_PROFILE",
    "RELATED_TO",
    "HAS_IMPLEMENTATION",
    "USES_COLUMN",
    "HAS_WORKFLOW_STEP",
    "HAS_STATE_TRANSITION",
    "HAS_SIDE",
    "HAS_UNIT",
    "HAS_MATCHING_LOGIC",
    "HAS_MISMATCH_CATEGORY",
    "REQUIRES_RULE",
    "HAS_VALIDATION_TEST",
    "HAS_OUTPUT_CONTRACT",
    "BELONGS_TO_DOMAIN",
    "SUPPORTS_DOMAIN",
    "USES_METRIC",
    "HAS_RECONCILIATION_VARIANT",
}


@dataclass(frozen=True)
class ValidationIssue:
    severity: str
    artifact_id: str
    message: str


@dataclass(frozen=True)
class CanonicalValidationResult:
    card_count: int
    edge_count: int
    issues: List[ValidationIssue]

    @property
    def ok(self) -> bool:
        return not any(issue.severity == "error" for issue in self.issues)


def load_jsonl(path: Path) -> List[Dict[str, object]]:
    if not path.exists():
        return []
    records: List[Dict[str, object]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            try:
                record = json.loads(stripped)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number}: invalid JSONL: {exc}") from exc
            if not isinstance(record, dict):
                raise ValueError(f"{path}:{line_number}: expected object record")
            records.append(record)
    return records


def validate_canonical(
    cards: Sequence[Mapping[str, object]],
    edges: Sequence[Mapping[str, object]],
    known_chunk_ids: Iterable[str] = (),
) -> CanonicalValidationResult:
    issues: List[ValidationIssue] = []
    card_ids: Dict[str, int] = {}
    chunk_id_set = set(known_chunk_ids)

    for card in cards:
        artifact_id = str(card.get("canonical_id") or "<missing>")
        for field in REQUIRED_CARD_FIELDS:
            if field not in card or card[field] in (None, "", []):
                issues.append(ValidationIssue("error", artifact_id, f"missing required field: {field}"))

        canonical_id = card.get("canonical_id")
        if isinstance(canonical_id, str):
            card_ids[canonical_id] = card_ids.get(canonical_id, 0) + 1
            if not CARD_ID_RE.match(canonical_id):
                issues.append(ValidationIssue("error", artifact_id, "invalid canonical_id format"))

            card_type = card.get("card_type")
            allowed_prefixes = (card_type,)
            if isinstance(card_type, str):
                allowed_prefixes = allowed_prefixes + CARD_TYPE_ID_PREFIXES.get(card_type, ())
            if isinstance(card_type, str) and not any(
                canonical_id.startswith(f"{prefix}.") for prefix in allowed_prefixes
            ):
                issues.append(
                    ValidationIssue(
                        "error",
                        artifact_id,
                        "canonical_id must be prefixed by card_type",
                    )
                )

        if card.get("status") not in VALID_STATUSES:
            issues.append(ValidationIssue("error", artifact_id, "invalid status"))
        if card.get("confidence") not in VALID_CONFIDENCE:
            issues.append(ValidationIssue("error", artifact_id, "invalid confidence"))

        issues.extend(_validate_evidence_refs(artifact_id, card, chunk_id_set))

    for canonical_id, count in card_ids.items():
        if count > 1:
            issues.append(ValidationIssue("error", canonical_id, "duplicate canonical_id"))

    for edge in edges:
        source_id = str(edge.get("source_id") or "<missing-source>")
        target_id = str(edge.get("target_id") or "<missing-target>")
        artifact_id = f"{source_id}->{target_id}"

        if source_id not in card_ids:
            issues.append(ValidationIssue("error", artifact_id, "edge source_id does not exist"))
        if target_id not in card_ids:
            issues.append(ValidationIssue("error", artifact_id, "edge target_id does not exist"))
        edge_type = edge.get("edge_type")
        if edge_type not in EDGE_TYPES and not (isinstance(edge_type, str) and EDGE_TYPE_RE.match(edge_type)):
            issues.append(ValidationIssue("error", artifact_id, "invalid edge_type"))
        if edge.get("confidence") not in VALID_CONFIDENCE:
            issues.append(ValidationIssue("error", artifact_id, "invalid edge confidence"))
        issues.extend(_validate_evidence_refs(artifact_id, edge, chunk_id_set))

    return CanonicalValidationResult(
        card_count=len(cards),
        edge_count=len(edges),
        issues=issues,
    )


def _validate_evidence_refs(
    artifact_id: str,
    artifact: Mapping[str, object],
    known_chunk_ids: set,
) -> List[ValidationIssue]:
    issues: List[ValidationIssue] = []
    evidence_refs = artifact.get("evidence_refs", [])
    if evidence_refs in (None, []):
        issues.append(ValidationIssue("warning", artifact_id, "missing evidence_refs"))
        return issues

    if not isinstance(evidence_refs, list):
        return [ValidationIssue("error", artifact_id, "evidence_refs must be a list")]

    for ref in evidence_refs:
        if not isinstance(ref, Mapping):
            issues.append(ValidationIssue("error", artifact_id, "evidence ref must be an object"))
            continue
        chunk_id = ref.get("chunk_id")
        if known_chunk_ids and chunk_id is not None and chunk_id not in known_chunk_ids:
            issues.append(
                ValidationIssue(
                    "error",
                    artifact_id,
                    f"evidence ref chunk_id does not exist: {chunk_id}",
                )
            )
    return issues
