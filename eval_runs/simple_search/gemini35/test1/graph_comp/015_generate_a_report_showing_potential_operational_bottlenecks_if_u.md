## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Timing

- started_at: `2026-05-28T11:17:08+00:00`
- duration_seconds: `70.006`
- GRAPH_COMPLETION_seconds: `70.005`

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

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
    "group_level_id = 22",
    "channel_name IS NOT NULL",
    "order_status NOT IN ('CANCELLED', 'DISPATCHED', 'DELIVERED', 'COMPLETE')"
  ],
  "joins": "No joins are needed as all marketplace order details, statuses, and tenant identifiers reside in the consolidated zs_observe.unicommerce_order_sales_report table.",
  "metric_logic": {
    "aggregation_grain": "channel_name, order_status",
    "deduplication_rule": "GROUP BY channel_name, order_status",
    "denominator": null,
    "formula": "Count of active/pending orders grouped by marketplace channel and order status to show bottleneck concentration.",
    "numerator": "COUNT(DISTINCT channel_order_id)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.increff_sales",
    "zs_observe.shopify_oms",
    "zs_observe.amazon_oms"
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "reason": "Identifies which marketplaces are integrated with Unicommerce and would be impacted by an outage.",
      "role": "Marketplace Channel",
      "selected?": "Yes",
      "table": "zs_observe.unicommerce_order_sales_report"
    },
    {
      "field": "channel_order_id",
      "reason": "Used to count the number of orders exposed to bottleneck risks.",
      "role": "Order Identifier",
      "selected?": "Yes",
      "table": "zs_observe.unicommerce_order_sales_report"
    },
    {
      "field": "order_status",
      "reason": "Helps categorize orders into pending/unfulfilled states to pinpoint exactly where bottlenecks would occur.",
      "role": "Fulfillment Status",
      "selected?": "Yes",
      "table": "zs_observe.unicommerce_order_sales_report"
    },
    {
      "field": "group_level_id",
      "reason": "Filters the dataset to the Mensa tenant (group_level_id = 22).",
      "role": "Tenant Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.unicommerce_order_sales_report"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.unicommerce_order_sales_report",
      "reason": "Contains transactional logs of all marketplace orders processed through Unicommerce OMS, which is essential to measure the operational reliance and risk exposure of each channel.",
      "role": "Primary OMS Sales Report Table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.unicommerce_order_sales_report",
  "sql_skeleton": "SELECT channel_name AS marketplace, order_status, COUNT(DISTINCT channel_order_id) AS pending_orders_at_risk, COUNT(DISTINCT channel_order_id) * 100.0 / SUM(COUNT(DISTINCT channel_order_id)) OVER() AS risk_contribution_pct FROM zs_observe.unicommerce_order_sales_report WHERE group_level_id = 22 AND channel_name IS NOT NULL AND order_status NOT IN ('CANCELLED', 'DISPATCHED', 'DELIVERED', 'COMPLETE') GROUP BY 1, 2 ORDER BY pending_orders_at_risk DESC;"
}
