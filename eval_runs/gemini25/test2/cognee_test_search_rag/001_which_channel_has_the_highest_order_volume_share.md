## 001. Which channel has the highest order volume share?

### Query

```text
Which channel has the highest order volume share?

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
  "selected_source": "platform_domain.increff.operations",
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "increff_operations_orders_data",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "Inferred as the main logical table within the 'platform_domain.increff.operations' domain that would contain both channel and order information for Mensa Brands, based on associated query patterns (e.g., `query_pattern.increff.7_1_monthly_gmv_by_channel`) and join keys (`order_id`, `channel_order_id`) mentioned in `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    }
  ],
  "required_fields": [
    {
      "field": "channel",
      "role": "Grouping Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the question ('Which channel') and its presence is strongly implied within Increff operations for Mensa Brands by `query_pattern.increff.7_1_monthly_gmv_by_channel` and join key `channel_order_id` in `execution_constraint_set.increff.operations_manifest_refactored_constraints`. Inferred as the logical column name."
    },
    {
      "field": "order_id",
      "role": "Order Identifier (for volume calculation)",
      "selected?": "Yes",
      "reason": "Needed to calculate 'order volume'. Its presence as a core identifier for orders is implied by `order_id` join keys and `order_id` coverage noted in `execution_constraint_set.increff.operations_manifest_refactored_constraints`. Inferred as the logical column name."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', where `group_level_id = 22` is the documented identifier in `execution_constraint_set.increff.operations_manifest_refactored_constraints`. Inferred as the logical column name."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`is_active = true`) in `execution_constraint_set.increff.operations_manifest_refactored_constraints` for general data validity. Inferred as the logical column name."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`order_status = COMPLETED`) in `execution_constraint_set.increff.operations_manifest_refactored_constraints` for revenue/GMV contexts, which implies relevance for counting valid orders. Inferred as the logical column name."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`transaction_type = SALES`) in `execution_constraint_set.increff.operations_manifest_refactored_constraints` for revenue/GMV contexts, which implies relevance for counting valid orders. Inferred as the logical column name."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "MAX ( (COUNT(DISTINCT order_id) per channel / Total COUNT(DISTINCT order_id) for Mensa Brands) * 100 )",
    "numerator": "COUNT(DISTINCT order_id) per channel",
    "denominator": "Total COUNT(DISTINCT order_id) for Mensa Brands",
    "aggregation_grain": "channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) to ensure each order is counted once for volume."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No specific joins can be determined from the context as the exact relationships between potential sub-tables within the inferred 'increff_operations_orders_data' are not explicitly defined, but the hard rule defaults to a single source table or single relationship path. Thus, all fields are assumed to be available directly in 'increff_operations_orders_data' for this query.",
  "missing_or_ambiguous": "The explicit physical table name for 'increff_operations_orders_data' and the precise column names for 'channel', 'order_id', 'group_level_id', 'is_active', 'order_status', and 'transaction_type' are not provided. These were logically inferred based on domain conventions and the strong implications from the Increff constraint set's related query patterns and join keys/filters.",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        increff_operations_orders_data\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        channel\n),\nTotalOrderVolume AS (\n    SELECT\n        COUNT(DISTINCT order_id) AS total_order_count\n    FROM\n        increff_operations_orders_data\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n)\nSELECT\n    cov.channel,\n    (CAST(cov.channel_order_count AS DOUBLE) / tov.total_order_count) * 100 AS order_volume_share\nFROM\n    ChannelOrderVolume cov,\n    TotalOrderVolume tov\nORDER BY\n    order_volume_share DESC\nLIMIT 1"
}
