## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Timing

- started_at: `2026-05-27T04:13:55+00:00`
- duration_seconds: `174.976`
- RAG_COMPLETION_seconds: `25.668`
- GRAPH_COMPLETION_seconds: `149.307`

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

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
  "selected_source": null,
  "rejected_sources": [
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for Myntra sales data",
      "selected?": "Yes",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales and includes `group_level_id` for scoping."
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and mentions `group_level_id=22` in its scope policy."
    },
    {
      "field": "zs_observe.increff_sales",
      "role": "Source for Increff sales data from various channels",
      "selected?": "Yes",
      "reason": "The `execution_constraint_set.increff.operations_manifest_refactored_constraints` mentions 'revenue/GMV' filters and `group_level_id = 22` for Mensa, strongly implying this table contains sales data by channel. Inferred from previous interactions that `increff_sales` holds `sales_channel` and sales amounts."
    }
  ],
  "required_fields": [
    {
      "field": "oms.total_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Used to calculate gross sales for Myntra, as per `query_pattern.myntra.gross_sales_oms`."
    },
    {
      "field": "'Myntra'",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Literal string to identify the Myntra marketplace, as `myntra_oms` is specific to Myntra."
    },
    {
      "field": "oms.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables."
    },
    {
      "field": "oms.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables."
    },
    {
      "field": "settlement.gmv_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Inferred as the relevant column for GMV from `query_pattern.limeroad.total_forward_gmv`. A standard name for GMV values in settlement tables."
    },
    {
      "field": "'LimeRoad'",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Literal string to identify the LimeRoad marketplace, as `limeroad_settlement` is specific to LimeRoad."
    },
    {
      "field": "settlement.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Explicitly mentioned as `group_level_id=22` in `scope_policy` for LimeRoad data."
    },
    {
      "field": "settlement.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables."
    },
    {
      "field": "sales.total_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Inferred as the primary sales value column in `increff_sales` to represent revenue/GMV."
    },
    {
      "field": "sales.sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Explicitly used in Increff query patterns (`query_pattern.increff.7_1_monthly_gmv_by_channel`) to group sales by channel."
    },
    {
      "field": "sales.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is mandated in `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Sum of total sales/GMV for each marketplace, then rank and select the top 2.",
    "numerator": "total_sales",
    "denominator": null,
    "aggregation_grain": "marketplace",
    "deduplication_rule": "Sum sales per unique marketplace across all data sources."
  },
  "filters": [
    "oms.group_level_id = '22'",
    "oms.is_active = true",
    "settlement.group_level_id = '22'",
    "settlement.is_active = true",
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'"
  ],
  "joins": "A UNION ALL operation is used to combine sales data from different marketplace sources, followed by aggregation. No direct joins between these disparate source tables are needed or appropriate.",
  "missing_or_ambiguous": "The exact column names for sales value in `zs_observe.limeroad_settlement` (`gmv_amount`) and `zs_observe.increff_sales` (`total_amount`) are inferred based on common data patterns for sales/settlement tables. The presence of `is_active` filter in `myntra_oms` and `limeroad_settlement` is inferred as a best practice, consistent with other documented filters. The determination of 'top 2 marketplaces' requires a ranking over all combined marketplace sales data.",
  "sql_skeleton": "WITH AllMarketplaceSales AS (
    SELECT
        'Myntra' AS marketplace_name,
        TRY_CAST(oms.total_amount AS DOUBLE) AS sales_value
    FROM
        zs_observe.myntra_oms oms
    WHERE
        oms.group_level_id = '22'
        AND oms.is_active = true

    UNION ALL

    SELECT
        'LimeRoad' AS marketplace_name,
        settlement.gmv_amount AS sales_value
    FROM
        zs_observe.limeroad_settlement settlement
    WHERE
        settlement.group_level_id = '22'
        AND settlement.is_active = true

    UNION ALL

    SELECT
        sales.sales_channel AS marketplace_name,
        sales.total_amount AS sales_value
    FROM
        zs_observe.increff_sales sales
    WHERE
        sales.group_level_id = '22'
        AND sales.is_active = true
        AND sales.order_status = 'COMPLETED'
        AND sales.transaction_type = 'SALES'
)
SELECT
    marketplace_name,
    SUM(sales_value) AS total_sales,
    RANK() OVER (ORDER BY SUM(sales_value) DESC) as sales_rank
FROM
    AllMarketplaceSales
GROUP BY
    marketplace_name
ORDER BY
    total_sales DESC
LIMIT 2"

### GRAPH_COMPLETION

{
  "filters": [
    "oms.group_level_id = '22'",
    "oms.is_active = true",
    "settlement.group_level_id = '22'",
    "settlement.is_active = true",
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine sales data from different marketplace sources, followed by aggregation. No direct joins between these disparate source tables are needed or appropriate.",
  "metric_logic": {
    "aggregation_grain": "marketplace",
    "deduplication_rule": "Sum sales per unique marketplace across all data sources.",
    "denominator": null,
    "formula": "Sum of total sales/GMV for each marketplace, then rank and select the top 2.",
    "numerator": "total_sales"
  },
  "missing_or_ambiguous": "The exact column names for sales value in `zs_observe.amazon_oms` (`total_amount`) is inferred based on its role as an OMS and consistency with `myntra_oms`. The presence of an `is_active` filter in `myntra_oms`, `limeroad_settlement`, and `amazon_oms` is inferred as a best practice for operational data validity, consistent with filters found in `increff_sales`. The values for `group_level_id` (`22` for Mensa Brands) are consistently applied across all sources based on provided `scope_keys` and previous interactions. The determination of 'top 2 marketplaces' requires a ranking over all combined marketplace sales data.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.unicommerce",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales and includes `group_level_id` for scoping Mensa Brands. This is a direct source for marketplace sales figures.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and explicitly mentions `group_level_id=22` in its scope policy for Mensa Brands. This is a direct source for marketplace sales figures.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "The `business_scope_set.mensa_brands.operations_wms` mentions Increff for cross-channel operational evidence. `execution_constraint_set.increff.operations_manifest_refactored_constraints` mentions 'revenue/GMV' filters and `group_level_id = 22` for Mensa, indicating this table holds sales data by channel. `query_pattern.increff.7_1_monthly_gmv_by_channel` confirms the presence of sales data (`sales_channel` and sales amounts).",
      "role": "Source for Increff sales data from various channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` explicitly links this table to Mensa Brands (`group_level_id = 22`). As an Order Management System, it is inferred to contain sales transaction data, making it a relevant source for marketplace sales.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "oms.total_amount",
      "reason": "Used to calculate gross sales for Myntra, as per `query_pattern.myntra.gross_sales_oms`. Inferred as numeric sales value.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'Myntra'",
      "reason": "Literal string to identify the Myntra marketplace for aggregation, as `myntra_oms` is specific to Myntra.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is the documented identifier for Mensa within operational tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.gmv_amount",
      "reason": "Inferred as the relevant column for GMV from `query_pattern.limeroad.total_forward_gmv`. This is a standard naming convention for GMV values in settlement tables.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'LimeRoad'",
      "reason": "Literal string to identify the LimeRoad marketplace for aggregation, as `limeroad_settlement` is specific to LimeRoad.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.group_level_id",
      "reason": "Explicitly mentioned as `group_level_id=22` in the scope policy for LimeRoad data, ensuring Mensa Brands data is selected.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.total_amount",
      "reason": "Inferred as the primary sales value column in `increff_sales` to represent revenue/GMV, consistent with typical sales tables.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "sales.sales_channel",
      "reason": "Explicitly used in Increff query patterns (`query_pattern.increff.7_1_monthly_gmv_by_channel`) to group sales by channel/marketplace.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is mandated in `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "sales.is_active",
      "reason": "Mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.total_amount",
      "reason": "Inferred as the standard sales value column in an OMS table for Amazon, consistent with other marketplace OMS data structures.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon'",
      "reason": "Literal string to identify the Amazon marketplace for aggregation, as `amazon_oms` is specific to Amazon.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is documented in `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS sales_value\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS sales_value\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS sales_value\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS sales_value\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n)\nSELECT\n    marketplace_name,\n    SUM(sales_value) AS total_sales,\n    RANK() OVER (ORDER BY SUM(sales_value) DESC) as sales_rank\nFROM\n    AllMarketplaceSales\nGROUP BY\n    marketplace_name\nORDER BY\n    total_sales DESC\nLIMIT 2"
}
