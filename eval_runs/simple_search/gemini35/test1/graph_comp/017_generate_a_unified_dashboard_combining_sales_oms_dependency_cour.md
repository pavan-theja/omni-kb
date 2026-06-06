## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-28T11:18:50+00:00`
- duration_seconds: `38.449`
- GRAPH_COMPLETION_seconds: `38.449`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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

### GRAPH_COMPLETION

{
  "filters": [
    "s.group_level_id = 22"
  ],
  "joins": "LEFT JOIN zs_observe.increff_returns r ON s.order_id = r.order_id AND s.group_level_id = r.group_level_id",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "GROUP BY sales_channel",
    "denominator": null,
    "formula": "COALESCE(SUM(charged_amount), 0) for GMV, concentration of fulfilment_channel for courier dependency, and ratio of non-null channel_return_id for return ownership.",
    "numerator": null
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.unicommerce_order_sales_report",
    "zs_observe.nykaa_oms",
    "zs_observe.myntra_oms"
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Aggregates metrics at the marketplace/own website level.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "charged_amount",
      "reason": "Sums total sales value per channel.",
      "role": "Sales GMV Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "fulfilment_channel",
      "reason": "Determines logistics dependency and courier concentration.",
      "role": "Courier/Logistics Partner",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "channel_return_id",
      "reason": "Differentiates marketplace-managed returns from seller-managed returns.",
      "role": "Return Ownership Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "group_level_id",
      "reason": "Filters data for Mensa Brand (group_level_id = 22).",
      "role": "Tenant Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Provides the multi-channel sales transactions, GMV (charged_amount), couriers (fulfilment_channel), and channels.",
      "role": "Primary Sales and Courier Source Table",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides returns data and marketplace return identifiers (channel_return_id) to classify return ownership.",
      "role": "Return Ownership Source Table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "SELECT s.sales_channel, 'Increff' AS oms_system, SUM(s.charged_amount) AS total_sales_gmv, COUNT(DISTINCT s.channel_order_id) AS total_orders, COUNT(DISTINCT s.fulfilment_channel) AS unique_couriers_used, COUNT(DISTINCT r.channel_return_id) AS marketplace_managed_returns, COUNT(DISTINCT CASE WHEN r.order_id IS NOT NULL AND r.channel_return_id IS NULL THEN r.order_id END) AS warehouse_managed_returns FROM zs_observe.increff_sales s LEFT JOIN zs_observe.increff_returns r ON s.order_id = r.order_id AND s.group_level_id = r.group_level_id WHERE s.group_level_id = 22 GROUP BY 1, 2 ORDER BY total_sales_gmv DESC;"
}
