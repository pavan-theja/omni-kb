## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

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
    "table.zs_ingest.myntra_oms",
    "table.zs_observe.shopify_oms",
    "column.zs_observe.shopify_oms.group_level_id",
    "column.zs_observe.shopify_oms.is_active",
    "column.zs_observe.increff_sales.gross_commission"
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
      "role": "marketplace identifier",
      "notes": "To identify marketplaces (applicable to Unicommerce, Increff)."
    },
    {
      "column_name": "gross_sales_amount",
      "role": "amount column",
      "notes": "Placeholder for the actual column name representing gross sales amount in unicommerce, increff_sales, amazon_oms, and shopify_oms. For myntra_oms, the column is 'total_amount'."
    },
    {
      "column_name": "total_amount",
      "role": "amount column",
      "notes": "Specific gross sales column name for myntra_oms."
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
  "relationships_join_paths": "No explicit joins needed between different source tables; data will be aggregated from each system independently and then combined using UNION ALL.",
  "metrics_formulas": [
    {
      "metric_name": "total_sales_per_marketplace",
      "formula": "SUM([SALES_AMOUNT_COLUMN])",
      "aggregation_grain": "per marketplace"
    },
    {
      "metric_name": "marketplace_rank",
      "formula": "RANK() OVER (ORDER BY total_sales_per_marketplace DESC)",
      "aggregation_grain": "across all marketplaces"
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
  "assumptions_missing_information_ambiguity": "The exact column name for sales amounts is a placeholder `[SALES_AMOUNT_COLUMN]` for `unicommerce`, `increff_sales`, `amazon_oms`, and `shopify_oms`, as it's not explicitly provided. For `increff_sales`, `gross_commission` is explicitly stated as not authoritative for settlement evidence. For `amazon_oms`, `myntra_oms`, and `shopify_oms`, the marketplace is inferred from the OMS name ('Amazon', 'Myntra', 'Shopify D2C' respectively), as a `sales_channel` column is not explicitly available in their context. Mensa's `group_level_id` is assumed to be `29` for Unicommerce and `22` for others, based on previous interactions.",
  "sql_skeleton": "WITH MarketplaceSales AS ( SELECT sales_channel AS marketplace, SUM([SALES_AMOUNT_COLUMN_UNICOMMERCE]) AS total_sales FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true GROUP BY 1 UNION ALL SELECT sales_channel AS marketplace, SUM([SALES_AMOUNT_COLUMN_INCREFF]) AS total_sales FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Amazon' AS marketplace, SUM([SALES_AMOUNT_COLUMN_AMAZON]) AS total_sales FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 UNION ALL SELECT 'Myntra' AS marketplace, SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales FROM zs_ingest.myntra_oms WHERE group_level_id = 22 GROUP BY 1 UNION ALL SELECT 'Shopify D2C' AS marketplace, SUM([SALES_AMOUNT_COLUMN_SHOPIFY]) AS total_sales FROM zs_observe.shopify_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1 ) SELECT marketplace, total_sales, RANK() OVER (ORDER BY total_sales DESC) AS sales_rank FROM MarketplaceSales ORDER BY sales_rank LIMIT 2;"
}
