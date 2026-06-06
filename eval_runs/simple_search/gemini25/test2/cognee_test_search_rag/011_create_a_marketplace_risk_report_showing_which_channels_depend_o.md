## 011. Create a marketplace risk report showing which channels depend on the same OMS.

### Query

```text
Create a marketplace risk report showing which channels depend on the same OMS.

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
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is indicated as a key operational data source for Mensa, containing sales and channel information managed by Increff, which is inferred to be the OMS in question based on the question context and Mensa's typical operational setup."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested for the report ('which channels'). This column is logically inferred to exist within an OMS sales table like `increff_sales` to identify the sales channel for each order."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier in Increff operational constraints and is a standard filter for operational tables."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT 'Increff Operations' AS oms_system, sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(oms_system, sales_channel)",
    "deduplication_rule": "DISTINCT on (oms_system, sales_channel) to list unique marketplace channels processed by the Increff OMS."
  },
  "filters": [
    "group_level_id = '22'",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (sales channel and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of a `sales_channel` column within `table.zs_observe.increff_sales` is inferred from domain knowledge and previous query patterns for channels. The specific list of marketplace channels for the filter is inferred based on common marketplaces handled by Mensa, as hinted in other contextual data and previous queries. The identification of 'Increff Operations' as the common OMS system is inferred from Mensa's consistent use of Increff for its operations, as indicated by `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
  "sql_skeleton": "SELECT DISTINCT 'Increff Operations' AS oms_system, sales_channel FROM zs_observe.increff_sales WHERE group_level_id = '22' AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
}
