## 001. Which channel has the highest order volume share?

### Timing

- started_at: `2026-05-28T10:08:18+00:00`
- duration_seconds: `17.813`
- RAG_COMPLETION_seconds: `17.812`

### Query

```text
Which channel has the highest order volume share?

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
    "sales_channel IS NOT NULL"
  ],
  "joins": "No joins needed as sales transactions are consolidated inside the single zs_observe.increff_sales table.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "GROUP BY sales_channel",
    "denominator": "SUM(COUNT(DISTINCT channel_order_id)) OVER()",
    "formula": "COUNT(DISTINCT channel_order_id) * 100.0 / SUM(COUNT(DISTINCT channel_order_id)) OVER()",
    "numerator": "COUNT(DISTINCT channel_order_id)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.nykaa_oms",
    "zs_observe.ajio_oms",
    "zs_observe.limeroad_oms"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains multi-channel sales transaction data for Mensa operational flow.",
      "role": "WMS operations sales transactions",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Identifies the sales channel/marketplace for share aggregation.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "channel_order_id",
      "reason": "Used to count distinct order volumes per channel.",
      "role": "Order Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "WITH channel_orders AS (SELECT sales_channel, COUNT(DISTINCT channel_order_id) AS order_volume FROM zs_observe.increff_sales WHERE sales_channel IS NOT NULL GROUP BY sales_channel), ranked_channels AS (SELECT sales_channel, order_volume, order_volume * 100.0 / SUM(order_volume) OVER() AS volume_share FROM channel_orders) SELECT sales_channel, order_volume, volume_share FROM ranked_channels ORDER BY order_volume DESC;"
}
