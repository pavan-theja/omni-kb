## 021. Gross sales trend across all marketplaces.

### Query

```text
Gross sales trend across all marketplaces.

Scope:
- tenant: Mensa

Answer for SQL query construction. Return concise, source-grounded details:
- relevant canonical ids and entity names
- source tables with schema/table names
- required columns, including join keys, filter columns, date columns, and amount columns
- relationships or join paths between tables/accounts/platforms/workflows
- metrics or formulas needed, including aggregation grain and deduplication rules
- tenant/group/platform/account filters that must appear in SQL
- assumptions, missing information, and any ambiguity
If useful, include a SQL skeleton, but do not invent columns or tables that are not in context.
```

### GRAPH_COMPLETION

{
  "relevant_canonical_ids": [
    "table.zs_observe.unicommerce",
    "column.zs_observe.unicommerce.sales_channel",
    "column.zs_observe.unicommerce.group_level_id",
    "column.zs_observe.unicommerce.is_active",
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.item_price",
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active",
    "table.zs_observe.amazon_oms",
    "column.zs_observe.amazon_oms.group_level_id",
    "column.zs_observe.amazon_oms.is_active",
    "table.zs_ingest.myntra_oms",
    "column.zs_ingest.myntra_oms.total_amount",
    "column.zs_ingest.myntra_oms.group_level_id",
    "table.zs_observe.shopify_oms",
    "column.zs_observe.shopify_oms.group_level_id",
    "column.zs_observe.shopify_oms.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "platforms": [
      "Unicommerce",
      "Increff",
      "Amazon OMS",
      "Myntra OMS",
      "Shopify OMS"
    ]
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "unicommerce",
      "description": "Unified transaction ledger for sales, returns, and cancellations."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "increff_sales",
      "description": "Sales data from Increff WMS."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "amazon_oms",
      "description": "Order Management System data for Amazon marketplace."
    },
    {
      "schema_name": "zs_ingest",
      "table_name": "myntra_oms",
      "description": "Order Management System data for Myntra marketplace."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "shopify_oms",
      "description": "Order Management System data for Shopify D2C channel."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "marketplace identifier",
      "notes": "To identify marketplaces (applicable to Unicommerce, Increff). Inferred for other OMS tables."
    },
    {
      "column_name": "gross_sales_amount",
      "role": "amount column",
      "notes": "Placeholder for the actual column name representing gross sales amount in Unicommerce, Amazon OMS, and Shopify OMS. For Increff sales, it's 'item_price'. For Myntra OMS, it's 'total_amount'."
    },
    {
      "column_name": "item_price",
      "role": "amount column",
      "notes": "Specific gross sales column name for increff_sales."
    },
    {
      "column_name": "total_amount",
      "role": "amount column",
      "notes": "Specific gross sales column name for myntra_oms."
    },
    {
      "column_name": "order_date",
      "role": "date column",
      "notes": "Placeholder for the column representing the order or transaction date in each system, essential for trend analysis."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records, where available."
    }
  ],
  "relationships_join_paths": "No explicit joins needed between different source tables; data will be aggregated from each system independently and then combined using UNION ALL.",
  "metrics_formulas": [
    {
      "metric_name": "total_gross_sales",
      "formula": "SUM(gross_sales_amount)",
      "aggregation_grain": "per marketplace and time period (e.g., month, quarter)"
    }
  ],
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands (Unicommerce)",
      "column": "group_level_id",
      "value": "29",
      "operator": "="
    },
    {
      "type": "tenant",
      "name": "Mensa Brands (Increff, Amazon, Myntra, Shopify)",
      "column": "group_level_id",
      "value": "22",
      "operator": "="
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "=",
      "notes": "Applied to Unicommerce, Increff Sales, Amazon OMS, and Shopify OMS. Not applicable for Myntra OMS."
    }
  ],
  "assumptions_missing_information_ambiguity": "A common date column (`order_date` used as placeholder) is assumed to exist across all tables to enable trend analysis. The exact column names for sales amounts (`gross_sales_amount` used as placeholder) are not explicitly provided for `unicommerce`, `amazon_oms`, and `shopify_oms`. The `sales_channel` column is explicitly present in `unicommerce` and `increff_sales`, but inferred from table names for `amazon_oms` ('Amazon'), `myntra_oms` ('Myntra'), and `shopify_oms` ('Shopify D2C'). `is_active` filter is assumed for `zs_observe` tables but not for `zs_ingest.myntra_oms`.",
  "sql_skeleton": "WITH AllMarketplaceSales AS ( SELECT sales_channel AS marketplace, DATE_TRUNC('month', order_date) AS sales_month, SUM(CAST(gross_sales_amount AS DOUBLE)) AS monthly_gross_sales FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true GROUP BY 1, 2 UNION ALL SELECT sales_channel AS marketplace, DATE_TRUNC('month', order_date) AS sales_month, SUM(CAST(item_price AS DOUBLE)) AS monthly_gross_sales FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY 1, 2 UNION ALL SELECT 'Amazon' AS marketplace, DATE_TRUNC('month', order_date) AS sales_month, SUM(CAST(gross_sales_amount AS DOUBLE)) AS monthly_gross_sales FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1, 2 UNION ALL SELECT 'Myntra' AS marketplace, DATE_TRUNC('month', order_date) AS sales_month, SUM(TRY_CAST(total_amount AS DOUBLE)) AS monthly_gross_sales FROM zs_ingest.myntra_oms WHERE group_level_id = 22 GROUP BY 1, 2 UNION ALL SELECT 'Shopify D2C' AS marketplace, DATE_TRUNC('month', order_date) AS sales_month, SUM(CAST(gross_sales_amount AS DOUBLE)) AS monthly_gross_sales FROM zs_observe.shopify_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1, 2 ) SELECT marketplace, sales_month, monthly_gross_sales FROM AllMarketplaceSales ORDER BY marketplace, sales_month;"
}
