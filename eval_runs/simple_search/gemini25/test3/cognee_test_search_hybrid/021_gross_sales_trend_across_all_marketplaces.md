## 021. Gross sales trend across all marketplaces.

### Timing

- started_at: `2026-05-27T04:30:01+00:00`
- duration_seconds: `90.418`
- RAG_COMPLETION_seconds: `68.809`
- GRAPH_COMPLETION_seconds: `21.608`

### Query

```text
Gross sales trend across all marketplaces.

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
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract gross sales data, marketplace identifiers, and order dates from disparate source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Sales amounts are summed per marketplace per month. Duplicate orders within a source are handled by the source table's primary key if applicable, otherwise, standard aggregation sums all relevant amounts.",
    "denominator": null,
    "formula": "SUM(gross_sales_amount) grouped by marketplace_name and monthly date.",
    "numerator": "SUM(gross_sales_amount)"
  },
  "missing_or_ambiguous": "The exact date column names (e.g., `order_date`, `settlement_date`) and the presence of `is_active` and `order_status = 'COMPLETED'` filters are inferred for `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, and `zs_observe.amazon_oms` based on general database best practices for operational tables and consistency with explicit rules for other sources like Increff and Meesho. The primary sales amount columns are inferred to be `total_amount`, `gmv_amount`, and `charged_amount` based on context. The type casting `TRY_CAST(... AS DOUBLE)` is applied for safety where mentioned or inferred as potentially necessary.",
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
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and includes `group_level_id` for scoping Mensa Brands. An `order_date` field is inferred for trending.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and specifies `group_level_id=22` for Mensa Brands. A `settlement_date` field is inferred for trending.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table is consistently referenced for sales data (`total_amount`), `sales_channel`, and filtering for Mensa Brands (`group_level_id = 22`, `order_status = 'COMPLETED'`, `transaction_type = 'SALES'`). An `order_date` field is inferred for trending.",
      "role": "Source for general sales data across channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` indicates this table is relevant for Mensa Brands (`group_level_id = 22`). As an OMS, it is inferred to contain gross sales (`total_amount`) and an `order_date` for trending.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` and `query_pattern.meesho.007.7_1_gross_gmv_forward_sales` explicitly use this table for sales (`charged_amount`) and indicate filters for `group_level_id` and `order_status = 'Delivered'`. An `order_date` field is inferred for trending.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the sales trend over time, aggregated by month.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish sales performance across different marketplaces. Derived as a literal string for marketplace-specific tables or from `sales_channel` for Increff.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "gross_sales_amount",
      "reason": "The core metric requested, representing the total sales value from each marketplace. Aggregated from respective sales amount fields in each source.",
      "role": "Metric (Gross Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per context.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered') for accurate gross sales metrics, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        DATE_TRUNC('month', oms.order_date) AS month_start_date,\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS gross_sales_amount\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', settlement.settlement_date) AS month_start_date, -- Inferred date field\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS gross_sales_amount\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', sales.order_date) AS month_start_date, -- Inferred date field\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS gross_sales_amount\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', amazon_oms.order_date) AS month_start_date, -- Inferred date field\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS gross_sales_amount -- Inferred sales amount\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', meesho_sales.order_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        meesho_sales.charged_amount AS gross_sales_amount\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    SUM(gross_sales_amount) AS total_gross_sales\nFROM\n    AllMarketplaceSales\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract gross sales data, marketplace identifiers, and order dates from disparate source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Sales amounts are summed per marketplace per month. Duplicate orders within a source are handled by the source table's primary key if applicable, otherwise, standard aggregation sums all relevant amounts.",
    "denominator": null,
    "formula": "SUM(gross_sales_amount) grouped by marketplace_name and monthly date.",
    "numerator": "SUM(gross_sales_amount)"
  },
  "missing_or_ambiguous": "The exact date column names (e.g., `order_date`, `settlement_date`) and the presence of `is_active` and `order_status = 'COMPLETED'` filters are inferred for `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, and `zs_observe.amazon_oms` based on general database best practices for operational tables and consistency with explicit rules for other sources like Increff and Meesho. The primary sales amount columns are inferred to be `total_amount`, `gmv_amount`, and `charged_amount` based on context. The type casting `TRY_CAST(... AS DOUBLE)` is applied for safety where mentioned or inferred as potentially necessary.",
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
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and includes `group_level_id` for scoping Mensa Brands. An `order_date` field is inferred for trending.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and specifies `group_level_id=22` for Mensa Brands. A `settlement_date` field is inferred for trending.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table is consistently referenced for sales data (`total_amount`), `sales_channel`, and filtering for Mensa Brands (`group_level_id = 22`, `order_status = 'COMPLETED'`, `transaction_type = 'SALES'`). An `order_date` field is inferred for trending.",
      "role": "Source for general sales data across channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` indicates this table is relevant for Mensa Brands (`group_level_id = 22`). As an OMS, it is inferred to contain gross sales (`total_amount`) and an `order_date` for trending.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` and `query_pattern.meesho.007.7_1_gross_gmv_forward_sales` explicitly use this table for sales (`charged_amount`) and indicate filters for `group_level_id` and `order_status = 'Delivered'`. An `order_date` field is inferred for trending.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the sales trend over time, aggregated by month.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish sales performance across different marketplaces. Derived as a literal string for marketplace-specific tables or from `sales_channel` for Increff.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "gross_sales_amount",
      "reason": "The core metric requested, representing the total sales value from each marketplace. Aggregated from respective sales amount fields in each source.",
      "role": "Metric (Gross Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per context.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered') for accurate gross sales metrics, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        DATE_TRUNC('month', oms.order_date) AS month_start_date,\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS gross_sales_amount\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', settlement.settlement_date) AS month_start_date, -- Inferred date field\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS gross_sales_amount\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', sales.order_date) AS month_start_date, -- Inferred date field\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS gross_sales_amount\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', amazon_oms.order_date) AS month_start_date, -- Inferred date field\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS gross_sales_amount -- Inferred sales amount\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', meesho_sales.order_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        meesho_sales.charged_amount AS gross_sales_amount\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    SUM(gross_sales_amount) AS total_gross_sales\nFROM\n    AllMarketplaceSales\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}
