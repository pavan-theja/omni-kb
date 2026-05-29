## 007. Which channels use marketplace-managed returns?

### Query

```text
Which channels use marketplace-managed returns?

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### RAG_COMPLETION

{
  "selected_source": "table.zs_observe.increff_returns",
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is explicitly described as a 'Cross-channel returns log (ops view)' and contains `sales_channel` and `group_level_id`. This makes it the most direct source for identifying channels associated with returns for Mensa Brands."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the question ('Which channels'). This column directly identifies the sales channel for each return record."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier in this table's `documented_scope_values`."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`is_active = true`) for data validity in `table.zs_observe.increff_returns`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT on (sales_channel) to list unique channels."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (sales channel, tenant ID, and activity status) is present within the single selected table `zs_observe.increff_returns`.",
  "missing_or_ambiguous": "The specific list of marketplace channels (`'Amazon'`, `'Flipkart'`, etc.) for the filter on `sales_channel` is inferred from previous turns where these were explicitly categorized as 'Marketplace' for Mensa. This inference assumes that if a channel is a marketplace, its returns are marketplace-managed.",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.increff_returns WHERE group_level_id = '22' AND is_active = true AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
}
