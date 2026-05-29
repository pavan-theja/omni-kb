# SQL Builder Skill

Build the final handoff JSON. Prefer executable SQL when the selected path is physical SQL. For metadata/inventory questions, produce a metadata handoff and do not fake SQL.

Question:
{{query}}

{{scope}}

Intent JSON:
{{intent_json}}

Source JSON:
{{source_json}}

Field/Join JSON:
{{field_join_json}}

Hard rules:
- `sql_skeleton` must query physical runtime tables only.
- Do not generate SQL against canonical metadata objects such as account_data_binding, query_pattern, relationship, platform_account, business_flow_binding, workflow_step, business_process, metric, state_transition, evidence, metadata.account_data_bindings, account_data_bindings, or canonical.cards.
- Do not create literal metadata SQL rows such as `SELECT 'Meesho' AS channel_name`.
- Do not UNION multiple physical sources unless deduplication keys and source precedence are grounded.
- If Source JSON has `answer_mode=metadata_inventory`, set `selected_source=null`, make `sql_skeleton` a SQL comment, and use `require_tables` to list the selected metadata/table evidence with `selected? = Yes`. Explain that these are evidence cards, not runtime SQL tables.
- If no physical table path is grounded for a SQL request, set `selected_source=null` and make `sql_skeleton` a SQL comment explaining the missing tables, columns, joins, or deduplication rules.
- In `require_tables`, mark `selected? = Yes` for physical SQL tables used in `sql_skeleton` or for canonical cards selected as metadata evidence in `metadata_inventory` mode.

Return a top-level JSON object with exactly one key named `content`.
The `content` value must be a string containing a JSON-serialized object matching this payload schema:
{
  "answer_mode": "physical_sql | metadata_inventory | partial",
  "selected_source": "string physical SQL table name, or null",
  "rejected_sources": ["array of rejected source ids or names"],
  "require_tables": [
    {
      "field": "physical SQL table name when selected for SQL; canonical metadata id when selected as evidence or rejected/supporting/risky",
      "role": "Primary Source | Selected Metadata Evidence | Supporting Metadata | Risky Candidate | Irrelevant Candidate | Filter Source | Metric Source",
      "selected?": "Yes/No",
      "reason": "candidate classification and SQL relevance"
    }
  ],
  "required_fields": [
    {
      "field": "physical column name or logical field name",
      "role": "Channel Identifier | Filter Column | Metric | Join Key | Status Field | Date Field",
      "selected?": "Yes/No",
      "reason": "why the field is needed; mark inferred reasoning when applicable"
    }
  ],
  "rejected_or_ambiguous_fields": ["array of objects or strings"],
  "metric_logic": {
    "formula": "string or null",
    "numerator": "string or null",
    "denominator": "string or null",
    "aggregation_grain": "string or null",
    "deduplication_rule": "string or null"
  },
  "filters": ["array of exact WHERE conditions or logical filters"],
  "joins": "join logic, or why no join is needed",
  "missing_or_ambiguous": "None only when complete; otherwise list blocking gaps/inferences",
  "sql_skeleton": "valid SQL template using selected fields and filters, or commented partial template"
}
