## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-27T04:16:50+00:00`
- duration_seconds: `254.363`
- RAG_COMPLETION_seconds: `155.369`
- GRAPH_COMPLETION_seconds: `98.993`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for each data aspect (Sales, OMS, Courier, Returns) from different source tables. These CTEs are then combined using FULL OUTER JOINs on a normalized sales_channel to create a unified view. The common sales_channel dimension is derived by uniting all distinct channel identifiers found across the various data sources.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Aggregates sales, OMS, courier, and return data to the sales_channel level. Sales are summed, OMS systems are collected as an array, top courier is selected by volume, and return metrics are counted per sales channel.",
    "denominator": null,
    "formula": "Combines total sales, associated OMS systems, primary courier partner, and return ownership metrics (total returns, QC data presence, distinct return reasons) aggregated by sales channel. The channel type (Own Website/Marketplace) is derived for each sales channel.",
    "numerator": "SUM(sales_value) for total_sales; COUNT(order_id) for primary_courier_partner; COUNT(return_id) for returns metrics."
  },
  "missing_or_ambiguous": "The primary challenge is the lack of explicit, standardized sales_channel identifiers or mapping tables that universally link all disparate data sources (Myntra OMS, LimeRoad Settlement, Increff Sales/Returns, Amazon OMS, Unicommerce) under a single 'Mensa Brands' umbrella. The channel names like 'Myntra', 'Amazon', 'LimeRoad' are inferred literals, while Increff and Unicommerce might have their own naming conventions for sales_channel. The oms_system values (e.g., 'Unicommerce_Managed', 'Myntra_Marketplace_OMS') are derived from source systems/table roles, which technically uses system context as a dimension value. The assumption of 'Shopify D2C' being 'Own Website' and others 'Marketplace' for return ownership is also an inference. The combined SQL is comprehensive but relies on these inferences for cross-system channel mapping and explicit system identification.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
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
      "reason": "Used for sales data (total_amount) for Myntra marketplace and to identify Myntra as an OMS for its channel. Confirmed by query_pattern.myntra.gross_sales_oms and account data binding.",
      "role": "Source for Myntra sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Used for sales data (gmv_amount) for LimeRoad marketplace. Confirmed by query_pattern.limeroad.total_forward_gmv.",
      "role": "Source for LimeRoad sales",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table provides sales data for various channels, courier partner information (fulfilment_channel), and indicates channels managed by Increff. Mentioned in execution_constraint_set.increff.operations_manifest_refactored_constraints and various Increff sales/courier query patterns.",
      "role": "Source for general sales, courier dependency, and Increff OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (total_amount) for Amazon marketplace and indicates Amazon as an OMS for its channel. Confirmed by account_data_binding.mensa.amazon_in.primary.amazon_oms.",
      "role": "Source for Amazon sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Used to identify channels managed by Unicommerce, serving as an OMS dependency indicator. Confirmed by business_scope_set.mensa_brands.operations_wms mentioning 'Unicommerce'.",
      "role": "Source for Unicommerce OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return metrics like return_id, qc_status, return_reason, crucial for analyzing return handling models by channel type. Referenced in various Increff return query patterns.",
      "role": "Source for return ownership details",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The central dimension for combining all aspects of the dashboard. Derived or explicitly available in all relevant tables.",
      "role": "Primary Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "channel_type",
      "reason": "Derived from sales_channel to categorize into 'Own Website' or 'Marketplace' for return ownership analysis.",
      "role": "Derived Dimension (Channel Type)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales",
      "reason": "Represents the sales volume for each channel, aggregated from multiple sources.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "oms_systems_used",
      "reason": "Indicates which OMS/WMS systems are associated with a given sales channel, derived from the various OMS tables.",
      "role": "Metric (OMS Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "primary_courier_partner",
      "reason": "Identifies the top courier used for each channel, primarily from Increff sales data.",
      "role": "Metric (Courier Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Count of returns, providing insight into return volume per channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc_data",
      "reason": "Count of returns with quality check data, indicating the level of return handling detail available for a channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Number of unique return reasons, indicating granularity of return feedback by channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (group_level_id = '22') to scope all data to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (is_active = true) for data validity across all operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (order_status = 'COMPLETED') for accurate sales and courier dependency metrics from sales tables.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (transaction_type = 'SALES') for accurate sales and courier dependency metrics from sales tables.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (return_status = 'COMPLETED') to ensure only relevant, processed return transactions are included.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_CTE AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        SUM(TRY_CAST(oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n    GROUP BY\n        'Myntra'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        SUM(settlement.gmv_amount) AS total_sales\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n    GROUP BY\n        'LimeRoad'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS sales_channel,\n        SUM(sales.total_amount) AS total_sales\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n    GROUP BY\n        sales.sales_channel\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        SUM(TRY_CAST(amazon_oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n    GROUP BY\n        'Amazon'\n),\nOMS_Dependency_Raw_CTE AS (\n    SELECT DISTINCT\n        unicommerce.sales_channel AS sales_channel,\n        'Unicommerce_Managed' AS oms_system\n    FROM\n        zs_observe.unicommerce unicommerce\n    WHERE\n        unicommerce.group_level_id = '22'\n        AND unicommerce.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Myntra' AS sales_channel,\n        'Myntra_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Amazon' AS sales_channel,\n        'Amazon_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        increff_sales.sales_channel AS sales_channel,\n        'Increff_Managed_OMS/WMS' AS oms_system\n    FROM\n        zs_observe.increff_sales increff_sales\n    WHERE\n        increff_sales.group_level_id = '22'\n        AND increff_sales.is_active = true\n),\nOMS_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        ARRAY_AGG(DISTINCT oms_system) AS oms_systems_used\n    FROM\n        OMS_Dependency_Raw_CTE\n    GROUP BY\n        sales_channel\n),\nCourier_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        fulfilment_channel AS primary_courier_partner,\n        order_count\n    FROM (\n        SELECT\n            sales.sales_channel,\n            sales.fulfilment_channel,\n            COUNT(sales.order_id) AS order_count,\n            ROW_NUMBER() OVER(PARTITION BY sales.sales_channel ORDER BY COUNT(sales.order_id) DESC) as rn\n        FROM\n            zs_observe.increff_sales sales\n        WHERE\n            sales.group_level_id = '22'\n            AND sales.is_active = true\n            AND sales.order_status = 'COMPLETED'\n            AND sales.transaction_type = 'SALES'\n            AND sales.fulfilment_channel IS NOT NULL\n        GROUP BY\n            sales.sales_channel,\n            sales.fulfilment_channel\n    ) AS ranked_couriers\n    WHERE rn = 1\n),\nReturn_Ownership_CTE AS (\n    SELECT\n        returns.sales_channel,\n        COUNT(DISTINCT returns.return_id) AS total_returns,\n        COUNT(CASE WHEN returns.qc_status IS NOT NULL THEN returns.return_id END) AS returns_with_qc_data,\n        COUNT(DISTINCT returns.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns returns\n    WHERE\n        returns.group_level_id = '22'\n        AND returns.is_active = true\n        AND returns.return_status = 'COMPLETED'\n    GROUP BY\n        returns.sales_channel\n),\nAll_Channels AS (\n    SELECT sales_channel FROM Sales_CTE\n    UNION\n    SELECT sales_channel FROM OMS_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Courier_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Return_Ownership_CTE\n)\nSELECT\n    ac.sales_channel,\n    CASE WHEN ac.sales_channel = 'Shopify D2C' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type,\n    COALESCE(s.total_sales, 0) AS total_sales,\n    COALESCE(o.oms_systems_used, ARRAY<STRING>[]) AS oms_systems_used,\n    c.primary_courier_partner,\n    COALESCE(ro.total_returns, 0) AS total_returns,\n    COALESCE(ro.returns_with_qc_data, 0) AS returns_with_qc_data,\n    COALESCE(ro.distinct_return_reasons, 0) AS distinct_return_reasons\nFROM\n    (SELECT DISTINCT sales_channel FROM All_Channels) ac\nLEFT JOIN\n    Sales_CTE s ON ac.sales_channel = s.sales_channel\nLEFT JOIN\n    OMS_Dependency_CTE o ON ac.sales_channel = o.sales_channel\nLEFT JOIN\n    Courier_Dependency_CTE c ON ac.sales_channel = c.sales_channel\nLEFT JOIN\n    Return_Ownership_CTE ro ON ac.sales_channel = ro.sales_channel\nORDER BY\n    ac.sales_channel;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for each data aspect (Sales, OMS, Courier, Returns) from different source tables. These CTEs are then combined using FULL OUTER JOINs on a normalized `sales_channel` to create a unified view. The common `sales_channel` dimension is derived by uniting all distinct channel identifiers found across the various data sources. For courier dependency, an inner query ranks couriers per channel to identify the primary one.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Aggregates sales, OMS, courier, and return data to the sales_channel level. Sales are summed. OMS systems are collected as an array of distinct systems. The top courier is selected by volume. Return metrics are counted per sales channel, with `return_id` used for total/QC counts and `return_reason` for distinct counts.",
    "denominator": null,
    "formula": "Combines total sales, associated OMS systems, primary courier partner, and return ownership metrics (total returns, QC data presence, distinct return reasons) aggregated by sales channel. The channel type (Own Website/Marketplace) is derived for each sales channel.",
    "numerator": "SUM(sales_value) for total_sales; COUNT(order_id) for primary_courier_partner (after ranking); COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason) for returns metrics."
  },
  "missing_or_ambiguous": "The primary challenge is the lack of explicit, standardized `sales_channel` identifiers or mapping tables that universally link all disparate data sources (Myntra OMS, LimeRoad Settlement, Increff Sales/Returns, Amazon OMS, Unicommerce) under a single 'Mensa Brands' umbrella. The channel names like 'Myntra', 'Amazon', 'LimeRoad' are inferred as literal strings for their respective dedicated tables, while Increff and Unicommerce might use varied `sales_channel` column values. The `oms_system` values (e.g., 'Unicommerce_Managed', 'Myntra_Marketplace_OMS') are derived from source systems/table roles, which technically uses system context as a dimension value rather than an explicit column. The assumption of 'Shopify D2C' being 'Own Website' and other `sales_channel` values being 'Marketplace' for return ownership is also an inference based on common e-commerce distinctions and specific query patterns mentioning 'Shopify D2C'. The specific column names for sales values (`total_amount`, `gmv_amount`) are inferred from common marketplace data schemas and related query patterns. The `is_active` filter is inferred as a best practice for operational data validity across all relevant tables.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
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
      "reason": "Used for sales data (total_amount) for Myntra marketplace and to identify Myntra as an OMS for its channel. Confirmed by `query_pattern.myntra.gross_sales_oms` and `account_data_binding.mensa.amazon_in.primary.amazon_oms` (which establishes pattern for Mensa's marketplace OMS tables).",
      "role": "Source for Myntra sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Used for sales data (gmv_amount) for LimeRoad marketplace. Confirmed by `query_pattern.limeroad.total_forward_gmv`.",
      "role": "Source for LimeRoad sales",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table provides sales data for various channels, courier partner information (fulfilment_channel), and indicates channels managed by Increff. Mentioned in `execution_constraint_set.increff.operations_manifest_refactored_constraints` and various Increff sales/courier query patterns (e.g., `query_pattern.increff.7_1_monthly_gmv_by_channel`, `query_pattern.increff.7_6_courier_partner_distribution_normalized`).",
      "role": "Source for general sales, courier dependency, and Increff OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (total_amount) for Amazon marketplace and indicates Amazon as an OMS for its channel. Confirmed by `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Source for Amazon sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Used to identify channels managed by Unicommerce, serving as an OMS dependency indicator. Confirmed by `business_scope_set.mensa_brands.operations_wms` mentioning 'Unicommerce'.",
      "role": "Source for Unicommerce OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return metrics like `return_id`, `qc_status`, `return_reason`, crucial for analyzing return handling models by channel type. Referenced in various Increff return query patterns (e.g., `query_pattern.increff.8_1_return_volume_by_channel_and_type`).",
      "role": "Source for return ownership details",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The central dimension for combining all aspects of the dashboard. Derived or explicitly available in all relevant tables. Normalization is required across different sources.",
      "role": "Primary Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "channel_type",
      "reason": "Derived from `sales_channel` to categorize into 'Own Website' or 'Marketplace' for return ownership analysis, as suggested by `query_pattern.increff.8_3_qc_pass_fail_analysis_shopify_d2c` for 'Shopify D2C'.",
      "role": "Derived Dimension (Channel Type)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales",
      "reason": "Represents the sales volume for each channel, aggregated from multiple sources (`myntra_oms.total_amount`, `limeroad_settlement.gmv_amount`, `increff_sales.total_amount`, `amazon_oms.total_amount`).",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "oms_systems_used",
      "reason": "Indicates which OMS/WMS systems are associated with a given sales channel, derived from the various OMS tables (`unicommerce`, `myntra_oms`, `amazon_oms`, `increff_sales`).",
      "role": "Metric (OMS Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "primary_courier_partner",
      "reason": "Identifies the top courier used for each channel, primarily from `increff_sales.fulfilment_channel` based on shipment count.",
      "role": "Metric (Courier Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Count of returns, providing insight into return volume per channel, derived from `increff_returns.return_id`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc_data",
      "reason": "Count of returns with quality check data, indicating the level of return handling detail available for a channel, derived from `increff_returns.qc_status`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Number of unique return reasons, indicating granularity of return feedback by channel, derived from `increff_returns.return_reason`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as per `account_data_binding` entries and scope policies.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, consistent with `execution_constraint_set.increff.operations_manifest_refactored_constraints` and common data practices.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales and courier dependency metrics from sales tables (`increff_sales`), as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales and courier dependency metrics from sales tables (`increff_sales`), as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`).",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_CTE AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        SUM(TRY_CAST(oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n    GROUP BY\n        'Myntra'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        SUM(settlement.gmv_amount) AS total_sales\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n    GROUP BY\n        'LimeRoad'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS sales_channel,\n        SUM(sales.total_amount) AS total_sales\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n    GROUP BY\n        sales.sales_channel\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        SUM(TRY_CAST(amazon_oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n    GROUP BY\n        'Amazon'\n),\nOMS_Dependency_Raw_CTE AS (\n    SELECT DISTINCT\n        unicommerce.sales_channel AS sales_channel,\n        'Unicommerce_Managed' AS oms_system\n    FROM\n        zs_observe.unicommerce unicommerce\n    WHERE\n        unicommerce.group_level_id = '22'\n        AND unicommerce.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Myntra' AS sales_channel,\n        'Myntra_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Amazon' AS sales_channel,\n        'Amazon_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        increff_sales.sales_channel AS sales_channel,\n        'Increff_Managed_OMS/WMS' AS oms_system\n    FROM\n        zs_observe.increff_sales increff_sales\n    WHERE\n        increff_sales.group_level_id = '22'\n        AND increff_sales.is_active = true\n),\nOMS_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        ARRAY_AGG(DISTINCT oms_system) AS oms_systems_used\n    FROM\n        OMS_Dependency_Raw_CTE\n    GROUP BY\n        sales_channel\n),\nCourier_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        fulfilment_channel AS primary_courier_partner,\n        order_count\n    FROM (\n        SELECT\n            sales.sales_channel,\n            sales.fulfilment_channel,\n            COUNT(sales.order_id) AS order_count,\n            ROW_NUMBER() OVER(PARTITION BY sales.sales_channel ORDER BY COUNT(sales.order_id) DESC) as rn\n        FROM\n            zs_observe.increff_sales sales\n        WHERE\n            sales.group_level_id = '22'\n            AND sales.is_active = true\n            AND sales.order_status = 'COMPLETED'\n            AND sales.transaction_type = 'SALES'\n            AND sales.fulfilment_channel IS NOT NULL\n        GROUP BY\n            sales.sales_channel,\n            sales.fulfilment_channel\n    ) AS ranked_couriers\n    WHERE rn = 1\n),\nReturn_Ownership_CTE AS (\n    SELECT\n        returns.sales_channel,\n        COUNT(DISTINCT returns.return_id) AS total_returns,\n        COUNT(CASE WHEN returns.qc_status IS NOT NULL THEN returns.return_id END) AS returns_with_qc_data,\n        COUNT(DISTINCT returns.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns returns\n    WHERE\n        returns.group_level_id = '22'\n        AND returns.is_active = true\n        AND returns.return_status = 'COMPLETED'\n    GROUP BY\n        returns.sales_channel\n),\nAll_Channels AS (\n    SELECT sales_channel FROM Sales_CTE\n    UNION\n    SELECT sales_channel FROM OMS_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Courier_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Return_Ownership_CTE\n)\nSELECT\n    ac.sales_channel,\n    CASE WHEN ac.sales_channel = 'Shopify D2C' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type,\n    COALESCE(s.total_sales, 0) AS total_sales,\n    COALESCE(o.oms_systems_used, ARRAY<STRING>[]) AS oms_systems_used,\n    c.primary_courier_partner,\n    COALESCE(ro.total_returns, 0) AS total_returns,\n    COALESCE(ro.returns_with_qc_data, 0) AS returns_with_qc_data,\n    COALESCE(ro.distinct_return_reasons, 0) AS distinct_return_reasons\nFROM\n    (SELECT DISTINCT sales_channel FROM All_Channels) ac\nLEFT JOIN\n    Sales_CTE s ON ac.sales_channel = s.sales_channel\nLEFT JOIN\n    OMS_Dependency_CTE o ON ac.sales_channel = o.sales_channel\nLEFT JOIN\n    Courier_Dependency_CTE c ON ac.sales_channel = c.sales_channel\nLEFT JOIN\n    Return_Ownership_CTE ro ON ac.sales_channel = ro.sales_channel\nORDER BY\n    ac.sales_channel;"
}
