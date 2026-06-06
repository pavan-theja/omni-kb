## 001. Which channel has the highest order volume share?

### Timing

- started_at: `2026-05-27T04:01:27+00:00`
- duration_seconds: `31.965`
- RAG_COMPLETION_seconds: `21.91`
- GRAPH_COMPLETION_seconds: `10.054`

### Query

```text
Which channel has the highest order volume share?

Scope:
- tenant: Mensa Brands

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Do not default to a single source table. First identify all grounded candidate sources or relationship paths that could answer the request. Then mark each candidate as direct, supporting, risky, or irrelevant based on whether it contains the required grain, dimensions, measures, filters, and joins. If no candidate is fully grounded, return a partial recommended path with usable fields, risks, and blocking gaps.
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

Return up to 3 recommended SQL packages:
- include only packages grounded in the provided context
- rank packages by directness, completeness, and SQL safety
- mark each package as complete, partial, or risky
- explain what each package can answer and what it cannot answer
- do not merge packages unless the context provides grounded join keys and deduplication rules

Response Format:
Cognee validates completion answers with a wrapper schema where `content` must be a string. To avoid parser failures, the top-level response MUST be a JSON object with exactly one key named `content`, and the value of `content` MUST be a string.

The `content` string must contain one valid JSON object serialized as text. Do not put a JSON object or array directly inside `content`.

Correct top-level shape:
{
  "content": "{\"selected_source\":\"table.example\",\"rejected_sources\":[],\"require_tables\":[],\"required_fields\":[],\"rejected_or_ambiguous_fields\":[],\"metric_logic\":{\"formula\":null,\"numerator\":null,\"denominator\":null,\"aggregation_grain\":null,\"deduplication_rule\":null},\"filters\":[],\"joins\":\"No joins needed\",\"missing_or_ambiguous\":\"None\",\"sql_skeleton\":\"SELECT 1\"}"
}

Incorrect top-level shape:
{
  "content": {
    "selected_source": "table.example"
  }
}

The JSON object inside the `content` string must strictly match this structural schema:
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
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) ensures each unique order is counted only once.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) across all sales_channels",
    "formula": "COUNT(DISTINCT order_id) / (SUM(COUNT(DISTINCT order_id)) OVER ())",
    "numerator": "COUNT(DISTINCT order_id) for each sales_channel"
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped sales queries. The value `transaction_type = 'SALES'` is used for clarity, assuming `'SAL'` is an abbreviation.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is consistently inferred to contain sales order data, including channel information and order identifiers, for Mensa Brands, which is crucial for determining order volume and share per channel. The context explicitly lists `group_level_id` for this table with value `22`, corresponding to Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to group order volume by channel, as specified in the report request. This is a common field in sales data for channel differentiation and is inferred to exist in a sales table like `increff_sales`.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Required to count the number of unique orders, representing 'order volume'. This is a standard primary key for orders in a sales table and is inferred to exist in `increff_sales`.",
      "role": "Metric (Order Volume)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly mentioned in the context for `column.zs_observe.increff_sales.group_level_id` with value `22`, which is required for scoping the report to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the order volume calculation (consistent with prior interactions).",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n)\nSELECT\n    sales_channel,\n    channel_order_count,\n    (CAST(channel_order_count AS DOUBLE) / SUM(channel_order_count) OVER ()) * 100 AS order_volume_share_pct\nFROM\n    ChannelOrderVolume\nORDER BY\n    order_volume_share_pct DESC\nLIMIT 1"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) ensures each unique order is counted only once.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) across all sales_channels",
    "formula": "COUNT(DISTINCT order_id) / (SUM(COUNT(DISTINCT order_id)) OVER ())",
    "numerator": "COUNT(DISTINCT order_id) for each sales_channel"
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped sales queries. The value `transaction_type = 'SALES'` is used for clarity, assuming `'SAL'` is an abbreviation.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table has been consistently inferred to contain sales order data, including channel information and order identifiers, for Mensa Brands, which is crucial for determining order volume and share per channel. The context explicitly lists `group_level_id` for this table with value `22`, corresponding to Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to group order volume by channel, as specified in the report request. This is a common field in sales data for channel differentiation and is inferred to exist in a sales table like `increff_sales`.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Required to count the number of unique orders, representing 'order volume'. This is a standard primary key for orders in a sales table and is inferred to exist in `increff_sales`.",
      "role": "Metric (Order Volume)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly mentioned in the context for `column.zs_observe.increff_sales.group_level_id` with value `22`, which is required for scoping the report to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the order volume calculation (consistent with prior interactions).",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n)\nSELECT\n    sales_channel,\n    channel_order_count,\n    (CAST(channel_order_count AS DOUBLE) / SUM(channel_order_count) OVER ()) * 100 AS order_volume_share_pct\nFROM\n    ChannelOrderVolume\nORDER BY\n    order_volume_share_pct DESC\nLIMIT 1"
}
