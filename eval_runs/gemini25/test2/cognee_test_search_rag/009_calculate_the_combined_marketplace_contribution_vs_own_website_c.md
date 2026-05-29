## 009. Calculate the combined marketplace contribution vs own website contribution.

### Query

```text
Calculate the combined marketplace contribution vs own website contribution.

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
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_settlement",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_disbursment",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.oms",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.cashback",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.settlement",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.commission",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_oms",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_settlement",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_reverse",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_non_order_settlement",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_oms_settlement",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_sales",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_settlement",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_reverse",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_reverse_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_oms",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_settlement",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_addition_charge",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_mapper_gst",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_mapping",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_oms",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_settlement",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_returns",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.tanvi_fitness_private_limited.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.tanvi_fitness_private_limited.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_oms",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_settlement",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_return",
    "account_data_binding.tanvi_fitness_private_limited.increff_wms.primary.increff_sales",
    "account_data_binding.tanvi_fitness_private_limited.increff_wms.primary.increff_returns",
    "account_data_binding.tanvi_fitness_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review",
    "table.zs_observe.marketplace_transactions",
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "2026-05-24",
    "snapdeal commission account data binding",
    "tanvi fitness private limited primary snapdeal account",
    "snapdeal non order account data binding",
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
      "field": "increff_operations_orders_data",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "Inferred as the main logical table within the 'platform_domain.increff.operations' that contains order-level details including channel information and is scoped for Mensa. Previous queries also utilized this domain for order volume and channel-related metrics, further reinforced by its associated filters (is_active, order_status, transaction_type)."
    }
  ],
  "required_fields": [
    {
      "field": "channel",
      "role": "Dimension for categorization",
      "selected?": "Yes",
      "reason": "Required to categorize orders into 'marketplace' or 'own website' contribution. Inferred as the logical column name for channel within order data for Increff operations."
    },
    {
      "field": "order_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Needed to calculate 'order volume' as a proxy for contribution. Inferred as the logical column name for a unique order identifier within Increff operations order data."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier. This is a standard filter for Mensa's operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`is_active = true`) for general data validity in Increff operations. This ensures only active records are considered for contribution calculation."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order contribution calculation."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`transaction_type = SALES`) in Increff operations, implying relevance for valid order contribution calculation."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Calculate the percentage of total distinct orders attributed to 'Marketplace' channels and 'Own Website' channels.",
    "numerator": "COUNT(DISTINCT order_id) for 'Marketplace' or 'Own Website' channels",
    "denominator": "Total COUNT(DISTINCT order_id) for Mensa across all channels",
    "aggregation_grain": "channel_category (Marketplace, Own Website)",
    "deduplication_rule": "COUNT(DISTINCT order_id) to count unique orders for volume-based contribution."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No specific joins can be determined from the context as all necessary fields are inferred to exist within the single selected table `increff_operations_orders_data`, adhering to the hard rule for single source tables.",
  "missing_or_ambiguous": "The explicit physical table name for 'increff_operations_orders_data' and precise column names for 'channel', 'order_id', 'group_level_id', 'is_active', 'order_status', and 'transaction_type' are not explicitly stated in the context. These were logically inferred based on domain knowledge, previous query patterns, and the `execution_constraint_set.increff.operations_manifest_refactored_constraints` for Mensa's Increff operations. The specific mapping of channel names to 'Marketplace' or 'Own Website' categories is also an inference based on common channel types.",
  "sql_skeleton": "WITH MensaOrders AS (\n    SELECT\n        CASE\n            WHEN channel = 'Website' THEN 'Own Website'\n            WHEN channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace'\n            ELSE 'Other'\n        END AS channel_category,\n        order_id\n    FROM\n        increff_operations_orders_data\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n),\nCategorizedOrderCounts AS (\n    SELECT\n        channel_category,\n        COUNT(DISTINCT order_id) AS orders_count\n    FROM\n        MensaOrders\n    GROUP BY\n        channel_category\n),\nTotalOrderCount AS (\n    SELECT\n        COUNT(DISTINCT order_id) AS total_orders\n    FROM\n        MensaOrders\n)\nSELECT\n    coc.channel_category,\n    (CAST(coc.orders_count AS DOUBLE) / tot.total_orders) * 100 AS contribution_percentage\nFROM\n    CategorizedOrderCounts coc,\n    TotalOrderCount tot\nWHERE\n    coc.channel_category IN ('Marketplace', 'Own Website')"
}
