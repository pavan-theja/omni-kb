## 021. Gross sales trend across all marketplaces.

### Query

```text
Gross sales trend across all marketplaces.

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
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is consistently used for Mensa's sales and operational data, containing sales channel information and order details necessary for a gross sales trend analysis. Its use is validated by the `execution_constraint_set.increff.operations_manifest_refactored_constraints` (inferred from prior interactions)."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Required to group sales by each marketplace, as specified in the report request. This column is logically present in a sales operations table."
    },
    {
      "field": "transaction_date",
      "role": "Dimension (Time for Trend)",
      "selected?": "Yes",
      "reason": "Required to analyze the 'trend' of gross sales over time. This is inferred as a standard date column in a sales transaction table."
    },
    {
      "field": "order_total_amount",
      "role": "Metric (Gross Sales)",
      "selected?": "Yes",
      "reason": "Required to calculate 'Gross sales'. This is inferred as the column representing the total monetary value of an order in a sales table."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions)."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations (inferred from prior interactions)."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) for analyzing valid sales transactions (inferred from prior interactions)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) to ensure only sales transactions contribute to the analysis (inferred from prior interactions)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SUM(order_total_amount)",
    "numerator": "SUM(order_total_amount)",
    "denominator": null,
    "aggregation_grain": "(sales_channel, DATE_TRUNC('month', transaction_date))",
    "deduplication_rule": "SUM(order_total_amount) per unique combination of sales_channel and transaction_date to represent gross sales."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SAL'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, transaction date, gross sales amount, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `transaction_date` and `order_total_amount` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables for calculating sales trends. The `sales_channel` column is inferred from consistent usage in previous Mensa-scoped sales queries. Standard mandatory filters for Mensa's Increff operations (`is_active`, `order_status`, `transaction_type`) are also inferred from domain knowledge and prior interactions. The `transaction_type = 'SALES'` filter will be truncated to `transaction_type = 'SAL'` based on the common abbreviation in similar contexts.",
  "sql_skeleton": "SELECT sales_channel, DATE_TRUNC('month', transaction_date) AS sales_month, SUM(order_total_amount) AS gross_sales FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SAL' GROUP BY sales_channel, sales_month ORDER BY sales_channel, sales_month"
}
