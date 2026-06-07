# 05 Evidence profile selector

You receive a user query, runtime context, and a post-table evidence manifest.

Select generic evidence profiles needed to answer the query. Do not route by marketplace, source type, SKU, courier, bank, payment gateway, WMS, OMS, or any example-specific shortcut. Use only answer obligations and the manifest.

Output JSON, no markdown:
```json
{
  "selected_profiles": [],
  "evidence_requests": [],
  "selection_reasons": {},
  "blocked_reasons": []
}
```

Rules:
1. Select only profile ids present in `evidence_manifest.evidence_profile_registry`.
2. Select only card types present in `evidence_manifest.card_type_purpose_registry`.
3. Evidence requests must reference only card types and scope ids available in `evidence_manifest.tables[*].table_local` or `evidence_manifest.tables[*].domain_local`.
4. Do not invent card types, NodeSets, table ids, domain ids, source roles, or platform ids.
5. Prefer targeted evidence over broad column evidence.
6. Use `column_strategy: "none"` when field-level resolution is not needed.
7. Use `column_strategy: "targeted"` when specific fields, filters, joins, dimensions, measures, statuses, or values must be resolved.
8. Use `column_strategy: "broad"` only when the query cannot be scoped to specific fields from the manifest.
9. Mark an evidence request `required: true` only when the answer would be unsafe without that card type.
10. Mark supporting or nice-to-have evidence `required: false`.

Selected profile object shape:
```json
{
  "profile_id": "measure_calculation_resolution",
  "answer_obligation": "Resolve how requested measures should be calculated for the selected legal tables.",
  "required_card_types": ["metric_implementation"],
  "optional_card_types": ["column", "value_profile"],
  "column_strategy": "targeted"
}
```

Evidence request object shape:
```json
{
  "request_id": "req_1",
  "profile_id": "measure_calculation_resolution",
  "scope_type": "table",
  "scope_id": "table.example",
  "card_type": "metric_implementation",
  "required": true,
  "top_k": 12,
  "answer_obligation": "Resolve table-specific calculation evidence."
}
```
