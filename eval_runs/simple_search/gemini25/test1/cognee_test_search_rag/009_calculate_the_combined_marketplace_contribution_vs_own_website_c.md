## 009. Calculate the combined marketplace contribution vs own website contribution.

### Query

```text
Calculate the combined marketplace contribution vs own website contribution.

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
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active",
    "table.zs_observe.amazon_oms",
    "column.zs_observe.amazon_oms.group_level_id",
    "column.zs_observe.amazon_oms.is_active",
    "table.zs_observe.myntra_oms",
    "column.zs_observe.myntra_oms.group_level_id",
    "query_pattern.myntra.gross_sales_oms",
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
      "notes": "To categorize sales as marketplace or own website (applicable to unicommerce, increff_sales). The specific values for categorization are missing."
    },
    {
      "column_name": "gross_sales_amount",
      "role": "amount column",
      "notes": "Placeholder for the actual column name representing gross sales amount in unicommerce, increff_sales, amazon_oms, and shopify_oms. For myntra_oms, the column is 'total_amount' (typecasted to DOUBLE)."
    },
    {
      "column_name": "total_amount",
      "role": "amount column",
      "notes": "Specific gross sales column name for myntra_oms, as per query_pattern.myntra.gross_sales_oms."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records (applicable to unicommerce, increff_sales, amazon_oms, shopify_oms, but not myntra_oms)."
    }
  ],
  "relationships_join_paths": "No explicit joins needed between different source tables; data will be aggregated from each system independently and then combined.",
  "metrics_formulas": [
    {
      "metric_name": "marketplace_contribution",
      "formula": "SUM(gross_sales_amount) for channels identified as marketplaces",
      "aggregation_grain": "total for marketplace channels"
    },
    {
      "metric_name": "own_website_contribution",
      "formula": "SUM(gross_sales_amount) for channels identified as own website",
      "aggregation_grain": "total for own website channels"
    },
    {
      "metric_name": "percentage_marketplace_contribution",
      "formula": "(marketplace_contribution / total_sales) * 100"
    },
    {
      "metric_name": "percentage_own_website_contribution",
      "formula": "(own_website_contribution / total_sales) * 100"
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
      "notes": "Applied to Unicommerce, Increff Sales, Amazon OMS, and Shopify OMS. Not applicable for Myntra OMS as per context."
    }
  ],
  "assumptions_missing_information_ambiguity": "Specific column names for gross sales amounts (e.g., `total_amount`, `sale_amount`) are placeholders for `unicommerce`, `increff_sales`, `amazon_oms`, and `shopify_oms`, as they are not explicitly provided in the context, except for `myntra_oms` ('total_amount'). The exact values within the `sales_channel` column (for `unicommerce` and `increff_sales`) that distinguish between 'marketplace' and 'own website' are missing and need to be determined from external knowledge. `amazon_oms` and `myntra_oms` are assumed to be 'marketplace' channels, while `shopify_oms` is assumed to be an 'own website' (D2C) channel. This report assumes that combining sales from these various platforms provides a comprehensive view of Mensa's sales channels. The current context does not provide information to consolidate these sales into a single logical sales ledger, so a UNION ALL approach across separate platform sales data is proposed.",
  "sql_skeleton": "WITH CombinedSales AS ( SELECT CASE WHEN sales_channel = '[OWN_WEBSITE_IDENTIFIER_UNICOMMERCE]' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type, SUM(gross_sales_amount_unicommerce) AS total_sales_amount FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true GROUP BY 1 UNION ALL SELECT CASE WHEN sales_channel = '[OWN_WEBSITE_IDENTIFIER_INCREFF]' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type, SUM(gross_sales_amount_increff) AS total_sales_amount FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Marketplace' AS channel_type, SUM(gross_sales_amount_amazon) AS total_sales_amount FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Marketplace' AS channel_type, SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales_amount FROM zs_ingest.myntra_oms WHERE group_level_id = 22 GROUP BY 1 UNION ALL SELECT 'Own Website' AS channel_type, SUM(gross_sales_amount_shopify) AS total_sales_amount FROM zs_observe.shopify_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 ) SELECT channel_type, SUM(total_sales_amount) AS combined_sales, SUM(total_sales_amount) * 100.0 / (SELECT SUM(total_sales_amount) FROM CombinedSales) AS percentage_contribution FROM CombinedSales GROUP BY channel_type;"
}
