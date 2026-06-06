## 020. Build an Average order value report per channel.

### Query

```text
Build an Average order value report per channel.

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

### RAG_COMPLETION

{
  "relevant_canonical_ids": [
    "table.zs_observe.unicommerce",
    "column.zs_observe.unicommerce.sales_channel",
    "column.zs_observe.unicommerce.group_level_id",
    "column.zs_observe.unicommerce.is_active",
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.external_shipment_id",
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
      "description": "Unified transaction ledger for sales."
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
      "role": "channel identifier",
      "notes": "To identify channels for Unicommerce and Increff. Inferred for other OMS tables."
    },
    {
      "column_name": "order_id",
      "role": "order identifier",
      "notes": "Placeholder for the column representing unique order IDs in each system. For Increff, 'external_shipment_id' will be used as a proxy. Exact column names needed for Unicommerce, Amazon OMS, Myntra OMS, and Shopify OMS."
    },
    {
      "column_name": "sales_amount",
      "role": "amount column",
      "notes": "Placeholder for the actual column name representing gross sales amount. For Myntra OMS, it is 'total_amount'. For Increff sales, it is typically 'item_price'."
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
      "metric_name": "total_sales_per_channel",
      "formula": "SUM(sales_amount)",
      "aggregation_grain": "per channel"
    },
    {
      "metric_name": "total_orders_per_channel",
      "formula": "COUNT(DISTINCT order_id)",
      "aggregation_grain": "per channel"
    },
    {
      "metric_name": "average_order_value",
      "formula": "total_sales_per_channel / total_orders_per_channel",
      "aggregation_grain": "per channel"
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
  "assumptions_missing_information_ambiguity": "The exact column names for sales amounts and order IDs are placeholders for `unicommerce`, `amazon_oms`, and `shopify_oms`. For `increff_sales`, `item_price` is assumed for sales amount and `external_shipment_id` for order ID. For `myntra_oms`, `total_amount` is confirmed for sales amount, but an order ID column is a placeholder. The `sales_channel` column is explicitly present in `unicommerce` and `increff_sales`, but inferred from table names for `amazon_oms` ('Amazon'), `myntra_oms` ('Myntra'), and `shopify_oms` ('Shopify D2C'). `is_active` column is assumed to exist for most tables based on common patterns.",
  "sql_skeleton": "WITH ChannelSales AS ( SELECT sales_channel AS channel, SUM(CAST(sales_value AS DOUBLE)) AS total_sales, COUNT(DISTINCT order_id) AS total_orders FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true GROUP BY 1 UNION ALL SELECT sales_channel AS channel, SUM(CAST(item_price AS DOUBLE)) AS total_sales, COUNT(DISTINCT external_shipment_id) AS total_orders FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Amazon' AS channel, SUM(CAST(sales_value AS DOUBLE)) AS total_sales, COUNT(DISTINCT order_id) AS total_orders FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Myntra' AS channel, SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales, COUNT(DISTINCT order_id) AS total_orders FROM zs_ingest.myntra_oms WHERE group_level_id = 22 GROUP BY 1 UNION ALL SELECT 'Shopify D2C' AS channel, SUM(CAST(sales_value AS DOUBLE)) AS total_sales, COUNT(DISTINCT order_id) AS total_orders FROM zs_observe.shopify_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 ) SELECT channel, total_sales, total_orders, (total_sales / total_orders) AS average_order_value FROM ChannelSales WHERE total_orders > 0 ORDER BY average_order_value DESC;"
}
