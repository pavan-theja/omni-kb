## 020. Build an Average order value report per channel.

### Timing

- started_at: `2026-05-28T10:16:46+00:00`
- duration_seconds: `16.187`
- RAG_COMPLETION_seconds: `16.187`

### Query

```text
Build an Average order value report per channel.

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
    "group_level_id = 22",
    "sales_channel IS NOT NULL"
  ],
  "joins": "No joins are needed as all channel order, revenue, and identifier columns are stored within the single consolidated table zs_observe.increff_sales.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "GROUP BY sales_channel",
    "denominator": "COUNT(DISTINCT channel_order_id)",
    "formula": "SUM(TRY_CAST(selling_price AS DOUBLE)) / COUNT(DISTINCT channel_order_id)",
    "numerator": "SUM(TRY_CAST(selling_price AS DOUBLE))"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.ajio_oms",
    "zs_observe.myntra_oms",
    "zs_observe.nykaa_oms",
    "zs_observe.limeroad_oms",
    "table.flipkart.oms"
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Used to group sales and order counts to compute per-channel metrics.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "selling_price",
      "reason": "Represents the selling price of items, used to calculate total revenue.",
      "role": "Revenue Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "channel_order_id",
      "reason": "Represents the distinct order identifier to determine the denominator for AOV.",
      "role": "Order Identifier Key",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "group_level_id",
      "reason": "Filters records to Mensa Brands (group_level_id = 22).",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains operational sales records across all connected channels (Amazon, Myntra, Flipkart, etc.) with selling price and order keys under WMS operations.",
      "role": "Consolidated multi-channel sales transactions table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "SELECT sales_channel, SUM(TRY_CAST(selling_price AS DOUBLE)) AS total_sales, COUNT(DISTINCT channel_order_id) AS total_orders, SUM(TRY_CAST(selling_price AS DOUBLE)) / NULLIF(COUNT(DISTINCT channel_order_id), 0) AS average_order_value FROM zs_observe.increff_sales WHERE group_level_id = 22 AND sales_channel IS NOT NULL GROUP BY 1 ORDER BY average_order_value DESC;"
}
