## 020. Build an Average order value report per channel.

### Query

```text
Build an Average order value report per channel.

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
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "This chunk is about an account data...",
    "primary` - scope_keys: ```json [ { \"business_key\":...",
    "This chunk describes nine active \"account_data_binding\" cards...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0024\" pack_index: 24...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0048\" pack_index: 48...",
    "bind platform_account.tanvi_fitness_private_limited.amazon_in.primary to table.zs_observe.amazon_settlement using client-level group_id and group_level_id scope filters.",
    "canonical_pack_0024",
    "canonical_pack_0061",
    "canonical_pack_0048",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0061\" pack_index: 61...",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "effective_cost_per_delivered_order",
    "metricimplementation",
    "metric implementation"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is consistently used for Mensa's sales and operational data, containing information about sales channels and orders, which are necessary for calculating Average Order Value per channel."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to group the Average Order Value by each sales channel, as specified in the report request. This column is logically present in a sales table."
    },
    {
      "field": "order_total_amount",
      "role": "Metric (Numerator)",
      "selected?": "Yes",
      "reason": "Required to sum the total monetary value of orders for the AOV calculation. This is inferred as a standard column for the total amount of a sales order in a sales table."
    },
    {
      "field": "order_id",
      "role": "Metric (Denominator)",
      "selected?": "Yes",
      "reason": "Required to count the number of distinct orders for the AOV calculation (total sales amount / number of orders). This is a common identifier in sales tables."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "order_status",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the AOV calculation (inferred from prior interactions)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SUM(order_total_amount) / COUNT(DISTINCT order_id)",
    "numerator": "SUM(order_total_amount)",
    "denominator": "COUNT(DISTINCT order_id)",
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) to ensure each unique order contributes once to the order count, and SUM(order_total_amount) aggregates the value for each distinct order."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order value, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `order_total_amount` column within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables for calculating Average Order Value. The `sales_channel` and `order_id` columns are inferred from consistent usage in previous Mensa-scoped sales queries. Standard mandatory filters for Mensa's Increff operations (`is_active`, `order_status`, `transaction_type`) are also inferred from domain knowledge and prior interactions.",
  "sql_skeleton": "SELECT sales_channel, SUM(order_total_amount) / COUNT(DISTINCT order_id) AS average_order_value FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES' GROUP BY sales_channel ORDER BY average_order_value DESC"
}
