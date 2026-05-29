## 014. Compare return handling models between own website and marketplace channels.

### Query

```text
Compare return handling models between own website and marketplace channels.

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

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_returns",
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is described as a 'Cross-channel returns log (ops view)' and explicitly includes 'returns fulfilment evidence' for Increff operations, which processes both marketplace and own website orders for Mensa."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension for comparison",
      "selected?": "Yes",
      "reason": "Required to distinguish between 'own website' and 'marketplace' channels to compare their return handling models. This column is logically present in a cross-channel returns log."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier in Mensa's operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`is_active = true`) for data validity in `table.zs_observe.increff_returns`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Categorize sales_channel into 'Marketplace Returns' or 'Own Website Returns' to compare their handling models.",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(sales_channel, return_handling_model)",
    "deduplication_rule": "DISTINCT on (sales_channel) to identify unique channels and their inferred return handling model."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins are required as all necessary information (sales channel, tenant ID, and activity status) is inferred to exist within the single selected table `zs_observe.increff_returns`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` within `table.zs_observe.increff_returns` is inferred based on domain knowledge of cross-channel return logs. The categorization into 'Marketplace Returns' and 'Own Website Returns' based on the `sales_channel` value is an inference using common channel types and Mensa's known platforms (Shopify for D2C/own website; Amazon, Flipkart, etc. for marketplaces).",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel,\n    CASE\n        WHEN sales_channel IN ('Shopify', 'Website') THEN 'Own Website Returns'\n        WHEN sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace Returns'\n        ELSE 'Other/Unspecified Returns'\n    END AS return_handling_model\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    return_handling_model, sales_channel"
}
