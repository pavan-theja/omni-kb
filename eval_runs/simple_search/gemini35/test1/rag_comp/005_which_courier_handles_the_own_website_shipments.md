## 005. Which courier handles the own website shipments?

### Timing

- started_at: `2026-05-28T10:09:44+00:00`
- duration_seconds: `27.136`
- RAG_COMPLETION_seconds: `27.136`

### Query

```text
Which courier handles the own website shipments?

Scope:
- platform account: Mensa

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
  "required_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ],
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
  "filters": [
    "o.group_level_id = 22",
    "s.group_level_id = 22"
  ],
  "joins": "INNER JOIN zs_observe.shopify_oms o ON o.order_id = s.order_id",
  "metric_logic": {
    "aggregation_grain": "courier_name",
    "deduplication_rule": "GROUP BY",
    "denominator": null,
    "formula": "COUNT(DISTINCT o.order_id) aggregated by courier_name",
    "numerator": "COUNT(DISTINCT o.order_id)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.increff_sales",
    "zs_observe.meesho_returns"
  ],
  "required_fields": [
    {
      "field": "order_id",
      "reason": "Identifies own website (Shopify D2C) orders.",
      "role": "Order Identifier",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Filters own website orders to Mensa Brands (group_level_id = 22).",
      "role": "Filter Column",
      "selected?": "Yes"
    },
    {
      "field": "courier_name",
      "reason": "Inferred column representing the assigned courier partner handling the shipment.",
      "role": "Courier Identifier",
      "selected?": "Selected"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.shopify_oms",
      "reason": "Provides the order transactions from the own D2C website.",
      "role": "Shopify D2C order capturing source representing own website",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "reason": "Provides details on courier partner allocation for each order.",
      "role": "Logistics operations and courier allocation source",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.shiprocket_oms",
  "sql_skeleton": "SELECT s.courier_name, COUNT(DISTINCT o.order_id) AS shipment_count FROM zs_observe.shopify_oms o INNER JOIN zs_observe.shiprocket_oms s ON o.order_id = s.order_id WHERE o.group_level_id = 22 AND s.group_level_id = 22 GROUP BY 1 ORDER BY shipment_count DESC;"
}
