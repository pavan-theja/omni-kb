# Raw Intent Contract

Raw intent is the pre-retrieval router for SQL handoff.

Input:
- user question
- explicit scope only, such as tenant, group, platform, or account

It must not use:
- Cognee retrieved context
- canonical cards
- physical table cards
- query patterns
- previous discovery output

Purpose:
- classify the question family before retrieval
- decide what discovery should look for
- keep retrieval targeted without letting retrieval rewrite the question

Output shape:
```json
{
  "query_families": [
    "metric | report_generation | business_process | workflow | source_mapping | reconciliation | logistics"
  ],
  "answer_mode_hint": "physical_sql | metadata_inventory | mixed",
  "must_enumerate_sources": true,
  "table_limit": 10,
  "target_evidence": [
    "physical runtime tables",
    "physical columns",
    "account/platform bindings",
    "business flow bindings"
  ],
  "scope": {},
  "reason": "Local pre-retrieval routing based only on the user question and explicit scope."
}
```

The current implementation computes this locally in `classify_raw_intent()` so this stage remains separate from Cognee discovery.
