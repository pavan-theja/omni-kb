## 019. Build a SKU profitability report.

### Timing

- started_at: `2026-05-27T04:24:01+00:00`
- duration_seconds: `179.196`
- RAG_COMPLETION_seconds: `92.009`
- GRAPH_COMPLETION_seconds: `87.186`

### Query

```text
Build a SKU profitability report.

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
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Source for SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` explicitly mentions `sku_id` as a join key, and `query_pattern.increff.7_5_top_skus_by_volume` confirms SKU-level analysis from this source."
    },
    {
      "field": "zs_observe.increff_returns",
      "role": "Source for SKU-level return data (cost indicators)",
      "selected?": "Yes",
      "reason": "`query_pattern.increff.8_6_enrich_returns_with_sku_from_sales` explicitly indicates that returns can be linked to sales by SKU. This provides return volume and complexity metrics per SKU, which are key cost indicators for profitability."
    },
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for Myntra SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "As an OMS for a major marketplace, it is inferred to contain SKU-level sales details. Although `query_pattern.myntra.gross_sales_oms` mentions `total_amount` (likely order level), the presence of SKU detail is a standard expectation in OMS tables for profitability analysis."
    },
    {
      "field": "zs_observe.amazon_oms",
      "role": "Source for Amazon SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "Similar to `myntra_oms`, Amazon's OMS is inferred to contain `sku_id` and item-level sales data necessary for SKU profitability."
    },
    {
      "field": "zs_observe.amazon_fee_preview",
      "role": "Source for Amazon SKU-level fees (cost component)",
      "selected?": "Yes",
      "reason": "This table explicitly deals with fees and is likely to contain SKU-level detail, which is crucial for attributing marketplace fees to individual products for profitability."
    }
  ],
  "required_fields": [
    {
      "field": "sku_id",
      "role": "Dimension (Stock Keeping Unit Identifier)",
      "selected?": "Yes",
      "reason": "The primary grouping dimension for a SKU profitability report. Explicitly mentioned as a join key in Increff context and inferred for other OMS/fee tables."
    },
    {
      "field": "sales_channel",
      "role": "Dimension (Sales Channel/Marketplace)",
      "selected?": "Yes",
      "reason": "Required to differentiate profitability by the channel through which the SKU is sold. Explicitly available in `increff_sales` and inferred as literal strings for marketplace-specific OMS tables."
    },
    {
      "field": "total_revenue",
      "role": "Metric (Total Gross Revenue per SKU)",
      "selected?": "Yes",
      "reason": "Represents the total sales value generated by each SKU. Calculated by summing `line_item_total_amount` or similar fields from various sales data sources."
    },
    {
      "field": "total_quantity_sold",
      "role": "Metric (Total Quantity Sold per SKU)",
      "selected?": "Yes",
      "reason": "Indicates the volume of sales for each SKU, important for understanding scale. Aggregated from `quantity_sold` or similar fields."
    },
    {
      "field": "total_returns",
      "role": "Metric (Total Returns per SKU)",
      "selected?": "Yes",
      "reason": "Indicates the volume of returns for each SKU, acting as a proxy for return-related costs and operational complexity. Derived from `increff_returns.return_id`."
    },
    {
      "field": "returns_with_qc",
      "role": "Metric (Returns with QC Data per SKU)",
      "selected?": "Yes",
      "reason": "Reflects the number of returns that underwent quality checks, signifying a higher degree of handling and potential cost per SKU. Derived from `increff_returns.qc_status`."
    },
    {
      "field": "distinct_return_reasons",
      "role": "Metric (Distinct Return Reasons per SKU)",
      "selected?": "Yes",
      "reason": "Provides insight into the nature of returns for an SKU, which can inform product improvements or operational changes affecting profitability. Derived from `increff_returns.return_reason`."
    },
    {
      "field": "total_marketplace_fees",
      "role": "Metric (Total Marketplace Fees per SKU)",
      "selected?": "Yes",
      "reason": "Directly attributable fees incurred for selling each SKU on specific marketplaces, contributing to its overall cost. Derived from `amazon_fee_preview.estimated_fee_amount`."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as per scope policies."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active items/transactions are considered."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from sales tables (`increff_sales`, and inferred for OMS tables)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for OMS tables if applicable)."
    },
    {
      "field": "return_status",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Sum of gross revenue, quantity sold, total returns, returns with QC, distinct return reasons, and marketplace fees, all grouped by SKU and sales channel. This serves as a proxy for SKU profitability due to missing comprehensive COGS data.",
    "numerator": "SUM(total_revenue), SUM(total_quantity_sold), COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason), SUM(total_marketplace_fees)",
    "denominator": null,
    "aggregation_grain": "sku_id, sales_channel",
    "deduplication_rule": "Sales are aggregated per SKU and channel. Return counts are based on unique `return_id` per SKU and channel. Marketplace fees are summed per SKU and channel. All metrics are combined at the SKU and channel grain."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for sales revenue, return metrics, and marketplace fees, each scoped to a specific platform. These CTEs are then combined using FULL OUTER JOINs on `sku_id` and `sales_channel` to create a unified view. This approach allows for combining data from disparate sources that share common dimensions.",
  "missing_or_ambiguous": "The report is partial as it lacks comprehensive Cost of Goods Sold (COGS) data, which is essential for a true profitability calculation. SKU-level item prices (`line_item_total_amount`, `quantity_sold`) are strongly inferred for `zs_observe.myntra_oms` and `zs_observe.amazon_oms` as marketplace OMS systems typically store this granularity, but specific column names are not explicitly provided in the context. Similarly, `sku_id` and `estimated_fee_amount` in `zs_observe.amazon_fee_preview` are inferred. The attribution of all marketplace fees to specific SKUs is challenging without explicit item-level fee breakdowns across all platforms. Logistics costs are not included as they are generally not granular at the SKU level in the provided context.",
  "sql_skeleton": "WITH AllSalesData AS (
    SELECT
        is.sku_id,
        is.sales_channel,
        SUM(is.line_item_total_amount) AS total_revenue,
        SUM(is.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.increff_sales is
    WHERE
        is.group_level_id = '22'
        AND is.is_active = true
        AND is.order_status = 'COMPLETED'
        AND is.transaction_type = 'SALES'
    GROUP BY
        is.sku_id, is.sales_channel

    UNION ALL

    SELECT
        moms.sku_id,
        'Myntra' AS sales_channel,
        SUM(moms.line_item_total_amount) AS total_revenue,
        SUM(moms.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.myntra_oms moms
    WHERE
        moms.group_level_id = '22'
        AND moms.is_active = true
    GROUP BY
        moms.sku_id

    UNION ALL

    SELECT
        aoms.sku_id,
        'Amazon' AS sales_channel,
        SUM(aoms.line_item_total_amount) AS total_revenue,
        SUM(aoms.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.amazon_oms aoms
    WHERE
        aoms.group_level_id = '22'
        AND aoms.is_active = true
    GROUP BY
        aoms.sku_id
),
ReturnsData AS (
    SELECT
        ir.sku_id,
        ir.sales_channel,
        COUNT(DISTINCT ir.return_id) AS total_returns,
        COUNT(CASE WHEN ir.qc_status IS NOT NULL THEN ir.return_id END) AS returns_with_qc,
        COUNT(DISTINCT ir.return_reason) AS distinct_return_reasons
    FROM
        zs_observe.increff_returns ir
    WHERE
        ir.group_level_id = '22'
        AND ir.is_active = true
        AND ir.return_status = 'COMPLETED'
    GROUP BY
        ir.sku_id, ir.sales_channel
),
FeesData AS (
    SELECT
        afp.sku_id,
        'Amazon' AS sales_channel,
        SUM(afp.estimated_fee_amount) AS total_marketplace_fees
    FROM
        zs_observe.amazon_fee_preview afp
    WHERE
        afp.group_level_id = '22'
        AND afp.is_active = true
    GROUP BY
        afp.sku_id
)
SELECT
    COALESCE(asd.sku_id, rd.sku_id, fd.sku_id) AS sku_id,
    COALESCE(asd.sales_channel, rd.sales_channel, fd.sales_channel) AS sales_channel,
    COALESCE(asd.total_revenue, 0) AS total_revenue,
    COALESCE(asd.total_quantity_sold, 0) AS total_quantity_sold,
    COALESCE(rd.total_returns, 0) AS total_returns,
    COALESCE(rd.returns_with_qc, 0) AS returns_with_qc,
    COALESCE(rd.distinct_return_reasons, 0) AS distinct_return_reasons,
    COALESCE(fd.total_marketplace_fees, 0) AS total_marketplace_fees
FROM
    AllSalesData asd
FULL OUTER JOIN
    ReturnsData rd ON asd.sku_id = rd.sku_id AND asd.sales_channel = rd.sales_channel
FULL OUTER JOIN
    FeesData fd ON COALESCE(asd.sku_id, rd.sku_id) = fd.sku_id AND COALESCE(asd.sales_channel, rd.sales_channel) = fd.sales_channel
ORDER BY
    sku_id, sales_channel;


### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for sales revenue, return metrics, and marketplace fees, each scoped to a specific platform. These CTEs are then combined using FULL OUTER JOINs on `sku_id` and `sales_channel` to create a unified view. This approach allows for combining data from disparate sources that share common dimensions for comprehensive SKU-level reporting.",
  "metric_logic": {
    "aggregation_grain": "sku_id, sales_channel",
    "deduplication_rule": "Sales revenue and quantity are summed per SKU and channel. Return counts are based on unique `return_id` per SKU and channel. Marketplace fees are summed per SKU and channel. All metrics are combined at the SKU and channel grain.",
    "denominator": null,
    "formula": "Sum of gross revenue, quantity sold, total returns, returns with QC, distinct return reasons, and marketplace fees, all grouped by SKU and sales channel. This serves as a proxy for SKU profitability due to missing comprehensive COGS data and other cost components.",
    "numerator": "SUM(total_revenue), SUM(total_quantity_sold), COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason), SUM(total_marketplace_fees)"
  },
  "missing_or_ambiguous": "The report is partial as it lacks comprehensive Cost of Goods Sold (COGS) data, which is essential for a true profitability calculation. SKU-level item prices (`line_item_total_amount`, `quantity_sold`) are strongly inferred for `zs_observe.myntra_oms` and `zs_observe.amazon_oms` as marketplace OMS systems typically store this granularity, but specific column names for these are not explicitly provided in the context. Similarly, `sku_id` and `estimated_fee_amount` in `zs_observe.amazon_fee_preview` are inferred based on the table's purpose. The attribution of all marketplace fees to specific SKUs is challenging without explicit item-level fee breakdowns across all platforms. Logistics and other operational costs are not included as they are generally not granular at the SKU level in the provided context for Mensa Brands.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "zs_observe.myntra_oms_settlement",
    "zs_observe.myntra_non_order_settlement",
    "zs_ingest.myntra_receivables",
    "zs_observe.myntra_settlement"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` explicitly mentions `sku_id` as a join key, and `query_pattern.increff.7_5_top_skus_by_volume` confirms SKU-level analysis from this source. This table provides core sales metrics.",
      "role": "Source for SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "`query_pattern.increff.8_6_enrich_returns_with_sku_from_sales` explicitly indicates that returns can be linked to sales by SKU. This table provides return volume, QC status, and distinct return reasons, which are key cost and complexity indicators for profitability.",
      "role": "Source for SKU-level return data (cost indicators)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "As an Order Management System for a major marketplace, it is inferred to contain SKU-level sales details such as line item amounts and quantities. This is standard for profitability analysis at the product level.",
      "role": "Source for Myntra SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Similar to `myntra_oms`, Amazon's OMS is inferred to contain SKU-level sales data necessary for SKU profitability analysis.",
      "role": "Source for Amazon SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_fee_preview",
      "reason": "This table explicitly deals with estimated fees and is likely to contain SKU-level detail, which is crucial for attributing marketplace fees directly to individual products for a profitability assessment.",
      "role": "Source for Amazon SKU-level fees (cost component)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sku_id",
      "reason": "The primary grouping dimension for a SKU profitability report. Explicitly mentioned as a join key in Increff context and inferred for other OMS/fee tables to achieve SKU granularity.",
      "role": "Dimension (Stock Keeping Unit Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "Required to differentiate profitability by the channel through which the SKU is sold. Explicitly available in `increff_sales` and derived as literal strings for marketplace-specific OMS tables to normalize channels.",
      "role": "Dimension (Sales Channel/Marketplace)",
      "selected?": "Yes"
    },
    {
      "field": "total_revenue",
      "reason": "Represents the total sales value generated by each SKU. Calculated by summing `line_item_total_amount` or similar fields from various sales data sources. Essential for revenue side of profitability.",
      "role": "Metric (Total Gross Revenue per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_quantity_sold",
      "reason": "Indicates the volume of sales for each SKU, important for understanding scale and per-unit profitability. Aggregated from `quantity_sold` or similar fields.",
      "role": "Metric (Total Quantity Sold per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Indicates the volume of returns for each SKU, acting as a proxy for return-related costs and operational complexity. Derived from counting `increff_returns.return_id`.",
      "role": "Metric (Total Returns per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc",
      "reason": "Reflects the number of returns that underwent quality checks, signifying a higher degree of handling and potential cost per SKU. Derived from counting `increff_returns.return_id` where `qc_status` is present.",
      "role": "Metric (Returns with QC Data per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Provides insight into the nature of returns for an SKU, which can inform product improvements or operational changes affecting profitability. Derived from counting distinct `increff_returns.return_reason`.",
      "role": "Metric (Distinct Return Reasons per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_marketplace_fees",
      "reason": "Directly attributable fees incurred for selling each SKU on specific marketplaces, contributing to its overall cost. Derived from `amazon_fee_preview.estimated_fee_amount`.",
      "role": "Metric (Total Marketplace Fees per SKU)",
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
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active items/transactions are considered for accurate reporting.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from sales tables (`increff_sales`), preventing incomplete orders from affecting profitability calculations. Inferred for OMS tables if applicable.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for OMS tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`), avoiding pending or cancelled returns.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllSalesData AS (\n    SELECT\n        is.sku_id,\n        is.sales_channel,\n        SUM(is.line_item_total_amount) AS total_revenue,\n        SUM(is.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.increff_sales is\n    WHERE\n        is.group_level_id = '22'\n        AND is.is_active = true\n        AND is.order_status = 'COMPLETED'\n        AND is.transaction_type = 'SALES'\n    GROUP BY\n        is.sku_id, is.sales_channel\n\n    UNION ALL\n\n    SELECT\n        moms.sku_id,\n        'Myntra' AS sales_channel,\n        SUM(moms.line_item_total_amount) AS total_revenue,\n        SUM(moms.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.myntra_oms moms\n    WHERE\n        moms.group_level_id = '22'\n        AND moms.is_active = true\n    GROUP BY\n        moms.sku_id\n\n    UNION ALL\n\n    SELECT\n        aoms.sku_id,\n        'Amazon' AS sales_channel,\n        SUM(aoms.line_item_total_amount) AS total_revenue,\n        SUM(aoms.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.amazon_oms aoms\n    WHERE\n        aoms.group_level_id = '22'\n        AND aoms.is_active = true\n    GROUP BY\n        aoms.sku_id\n),\nReturnsData AS (\n    SELECT\n        ir.sku_id,\n        ir.sales_channel,\n        COUNT(DISTINCT ir.return_id) AS total_returns,\n        COUNT(CASE WHEN ir.qc_status IS NOT NULL THEN ir.return_id END) AS returns_with_qc,\n        COUNT(DISTINCT ir.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns ir\n    WHERE\n        ir.group_level_id = '22'\n        AND ir.is_active = true\n        AND ir.return_status = 'COMPLETED'\n    GROUP BY\n        ir.sku_id, ir.sales_channel\n),\nFeesData AS (\n    SELECT\n        afp.sku_id,\n        'Amazon' AS sales_channel,\n        SUM(afp.estimated_fee_amount) AS total_marketplace_fees\n    FROM\n        zs_observe.amazon_fee_preview afp\n    WHERE\n        afp.group_level_id = '22'\n        AND afp.is_active = true\n    GROUP BY\n        afp.sku_id\n)\nSELECT\n    COALESCE(asd.sku_id, rd.sku_id, fd.sku_id) AS sku_id,\n    COALESCE(asd.sales_channel, rd.sales_channel, fd.sales_channel) AS sales_channel,\n    COALESCE(asd.total_revenue, 0) AS total_revenue,\n    COALESCE(asd.total_quantity_sold, 0) AS total_quantity_sold,\n    COALESCE(rd.total_returns, 0) AS total_returns,\n    COALESCE(rd.returns_with_qc, 0) AS returns_with_qc,\n    COALESCE(rd.distinct_return_reasons, 0) AS distinct_return_reasons,\n    COALESCE(fd.total_marketplace_fees, 0) AS total_marketplace_fees\nFROM\n    AllSalesData asd\nFULL OUTER JOIN\n    ReturnsData rd ON asd.sku_id = rd.sku_id AND asd.sales_channel = rd.sales_channel\nFULL OUTER JOIN\n    FeesData fd ON COALESCE(asd.sku_id, rd.sku_id) = fd.sku_id AND COALESCE(asd.sales_channel, rd.sales_channel) = fd.sales_channel\nORDER BY\n    sku_id, sales_channel;"
}
