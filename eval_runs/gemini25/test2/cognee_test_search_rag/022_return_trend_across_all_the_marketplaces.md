## 022. Return trend across all the marketplaces.

### Query

```text
Return trend across all the marketplaces.

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
  "rejected_sources": [
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is explicitly described as a 'Cross-channel returns log (ops view)' and contains `sales_channel` and `group_level_id`, making it the most direct source for analyzing return trends across channels for Mensa."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Required to group return data by each marketplace, as specified in the report request. This column is logically present in a cross-channel returns log."
    },
    {
      "field": "return_date",
      "role": "Dimension (Time for Trend)",
      "selected?": "Yes",
      "reason": "Required to analyze the 'trend' of returns over time. This is inferred as a standard date column in a returns table."
    },
    {
      "field": "return_id",
      "role": "Metric (Return Count)",
      "selected?": "Yes",
      "reason": "Required to quantify the number of returns per marketplace per period. This is inferred as a primary identifier for a return transaction."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in `table.zs_observe.increff_returns`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "COUNT(DISTINCT return_id)",
    "numerator": "COUNT(DISTINCT return_id)",
    "denominator": null,
    "aggregation_grain": "(sales_channel, DATE_TRUNC('month', return_date))",
    "deduplication_rule": "COUNT(DISTINCT return_id) to ensure each unique return is counted once for the trend analysis."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (sales channel, return date, return ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_returns`.",
  "missing_or_ambiguous": "The explicit presence of `return_date` and `return_id` columns within `table.zs_observe.increff_returns` is inferred based on domain knowledge of returns tables. The list of marketplace channels used in the filter is consistently inferred from previous Mensa-specific queries.",
  "sql_skeleton": "SELECT sales_channel, DATE_TRUNC('month', return_date) AS return_month, COUNT(DISTINCT return_id) AS total_returns FROM zs_observe.increff_returns WHERE group_level_id = '22' AND is_active = true AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') GROUP BY sales_channel, return_month ORDER BY sales_channel, return_month"
}
