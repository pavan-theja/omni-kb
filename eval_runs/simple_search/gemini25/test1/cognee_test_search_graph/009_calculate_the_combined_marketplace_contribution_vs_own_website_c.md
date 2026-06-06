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

### GRAPH_COMPLETION

{
  "relevant_canonical_ids": [
    "table.zs_observe.unicommerce",
    "column.zs_observe.unicommerce.sales_channel",
    "column.zs_observe.unicommerce.group_level_id",
    "column.zs_observe.unicommerce.is_active",
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "platform_oms_1": "Unicommerce",
    "platform_wms_1": "Increff"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "unicommerce",
      "description": "Unified transaction ledger in Unicommerce OMS for sales, returns, and cancellations."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "increff_sales",
      "description": "Sales data from Increff WMS."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To distinguish between marketplace and own website sales."
    },
    {
      "column_name": "[SALES_AMOUNT_COLUMN_UNICOMMERCE]",
      "role": "amount column",
      "notes": "Placeholder for the column representing sales or revenue amount in 'zs_observe.unicommerce'. This column is not explicitly provided in the context."
    },
    {
      "column_name": "[SALES_AMOUNT_COLUMN_INCREFF]",
      "role": "amount column",
      "notes": "Placeholder for the column representing sales or revenue amount in 'zs_observe.increff_sales'. The 'gross_commission' column exists but is noted as not authoritative for settlement evidence. This column is not explicitly provided in the context."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records."
    }
  ],
  "relationships_join_paths": "No explicit joins needed. Data from 'unicommerce' and 'increff_sales' will be combined using UNION ALL.",
  "metrics_formulas": [
    {
      "metric_name": "combined_marketplace_contribution",
      "formula": "SUM([SALES_AMOUNT_COLUMN])",
      "aggregation_grain": "total"
    },
    {
      "metric_name": "own_website_contribution",
      "formula": "SUM([SALES_AMOUNT_COLUMN])",
      "aggregation_grain": "total"
    }
  ],
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands (Unicommerce)",
      "column": "group_level_id",
      "value": "29",
      "operator": "=",
      "tables": [
        "zs_observe.unicommerce"
      ]
    },
    {
      "type": "tenant",
      "name": "Mensa Brands (Increff)",
      "column": "group_level_id",
      "value": "22",
      "operator": "=",
      "tables": [
        "zs_observe.increff_sales"
      ]
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "=",
      "tables": [
        "zs_observe.unicommerce",
        "zs_observe.increff_sales"
      ]
    },
    {
      "type": "channel_type",
      "column": "sales_channel",
      "value": "[Placeholder for 'Own Website' identifier]",
      "operator": "=",
      "notes": "Filter for 'own website' contribution."
    },
    {
      "type": "channel_type",
      "column": "sales_channel",
      "value": "[Placeholder for 'Own Website' identifier]",
      "operator": "!=",
      "notes": "Filter for 'marketplace' contribution (all channels not 'own website')."
    }
  ],
  "assumptions_missing_information_ambiguity": "The most critical missing information is a column that represents the sales or revenue amount (e.g., `total_sale_amount`, `order_value`) in both `zs_observe.unicommerce` and `zs_observe.increff_sales`. While `increff_sales` has a `gross_commission` column, its description explicitly states it should not be used as authoritative settlement evidence, hence a general sales amount column is considered missing. The specific identifier for 'own website' within the `sales_channel` column is also missing and needs to be determined from external knowledge. It is assumed that all sales channels not identified as 'own website' are considered 'marketplaces' for this report. `group_level_id = 29` is used for Unicommerce and `group_level_id = 22` for Increff based on previous Mensa queries.",
  "sql_skeleton": "WITH CombinedSales AS ( SELECT sales_channel, [SALES_AMOUNT_COLUMN_UNICOMMERCE] AS sales_amount FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true UNION ALL SELECT sales_channel, [SALES_AMOUNT_COLUMN_INCREFF] AS sales_amount FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true ) SELECT SUM(CASE WHEN sales_channel = '[OWN_WEBSITE_IDENTIFIER]' THEN sales_amount ELSE 0 END) AS own_website_contribution, SUM(CASE WHEN sales_channel != '[OWN_WEBSITE_IDENTIFIER]' THEN sales_amount ELSE 0 END) AS combined_marketplace_contribution FROM CombinedSales;"
}
