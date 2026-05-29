## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is an evidence table for marketplace operations and sales data for Mensa (group_level_id=22), containing both sales channel information and order details necessary for a sales concentration analysis. Its use is validated by the `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Required to group sales by marketplace and identify the top performers, directly addressing 'top 2 marketplaces'. Logically available in a sales operations table."
    },
    {
      "field": "order_id",
      "role": "Metric (Sales Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used to calculate the sales concentration by counting unique orders, serving as a proxy for sales volume per channel, as an explicit sales amount column is not detailed in the context for this specific report type but was inferred in previous similar queries."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`is_active = true`) for data validity in Increff operations within `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`order_status = COMPLETED`) in `execution_constraint_set.increff.operations_manifest_refactored_constraints` for analyzing valid sales transactions."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`transaction_type = SALES`) in `execution_constraint_set.increff.operations_manifest_refactored_constraints` to ensure only sales transactions contribute to the analysis."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Calculate the total count of distinct orders per marketplace and then determine the percentage contribution of the top 2 marketplaces to the total marketplace orders.",
    "numerator": "COUNT(DISTINCT order_id) for a specific marketplace",
    "denominator": "SUM(COUNT(DISTINCT order_id)) for all marketplaces",
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) to ensure each unique order is counted once for volume calculation."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (marketplace, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `order_id` columns within `table.zs_observe.increff_sales` is inferred from domain knowledge of sales/operations tables and previous Mensa queries. The list of marketplace channels used in the filter is consistently inferred from previous Mensa-specific queries. Filters are inferred from `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
  "sql_skeleton": "WITH MarketplaceOrders AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n        AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')\n    GROUP BY\n        sales_channel\n),\nRankedMarketplaces AS (\n    SELECT\n        sales_channel,\n        channel_order_count,\n        RANK() OVER (ORDER BY channel_order_count DESC) as rnk\n    FROM\n        MarketplaceOrders\n),\nTotalMarketplaceOrders AS (\n    SELECT\n        SUM(channel_order_count) AS total_orders\n    FROM\n        MarketplaceOrders\n)\nSELECT\n    rm.sales_channel,\n    rm.channel_order_count,\n    (CAST(rm.channel_order_count AS DOUBLE) / tmo.total_orders) * 100 AS percentage_of_total_marketplace_orders\nFROM\n    RankedMarketplaces rm, TotalMarketplaceOrders tmo\nWHERE\n    rm.rnk <= 2\nORDER BY\n    rm.rnk"
}
