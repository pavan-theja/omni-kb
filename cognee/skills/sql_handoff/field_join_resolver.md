# Field And Join Resolver Skill

Resolve fields, filters, join keys, grain, and deduplication rules for the selected physical tables. Do not produce SQL yet.

Question:
{{query}}

{{scope}}

Intent JSON:
{{intent_json}}

Source JSON:
{{source_json}}

Retrieved context:
{{context}}

Rules:
- If Source JSON has `answer_mode=metadata_inventory`, resolve evidence fields instead of SQL fields:
  - identify the metadata cards, physical table cards, source bindings, platform/account identifiers, tenant filters, and named mappings that prove the inventory.
  - do not invent runtime SQL columns just to force a query.
  - set `joins` to explain metadata relationship paths, not SQL joins.
- Use physical columns only when grounded by column cards, query patterns, or stable table-column context.
- Use relationship cards only to justify joins between physical tables/columns.
- Infer tenant/account filters only from grounded scope evidence and mark them as inferred.
- Do not invent join keys, source precedence, or deduplication rules.
- If a required field is missing, keep the package partial/risky and explain the gap.
- Do not use canonical metadata objects as runtime SQL tables.

Return a top-level JSON object with exactly one key named `content`.
The `content` value must be a string containing a JSON-serialized object with keys:
`tables`, `fields`, `filters`, `joins`, `metric_logic`, `deduplication`, `missing_or_ambiguous`, `reason`.
