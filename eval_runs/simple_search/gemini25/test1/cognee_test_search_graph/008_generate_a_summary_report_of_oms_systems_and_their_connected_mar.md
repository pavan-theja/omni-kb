## 008. Generate a summary report of OMS systems and their connected marketplaces.

### Query

```text
Generate a summary report of OMS systems and their connected marketplaces.

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
    "column.zs_observe.increff_sales.is_active",
    "table.zs_observe.amazon_oms"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "platform_oms_1": "Unicommerce",
    "platform_oms_2": "Increff",
    "platform_oms_3": "Amazon OMS"
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
    },
    {
      "schema_name": "zs_observe",
      "table_name": "amazon_oms",
      "description": "Represents the Amazon OMS table."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "marketplace identifier",
      "notes": "To identify the marketplaces connected to Unicommerce and Increff. Explicit presence in amazon_oms is unknown from context."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for specific Mensa Brands entities (22 for general Mensa, 29 for Bracheium Brand Technologies)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records for Unicommerce and Increff tables."
    }
  ],
  "relationships_join_paths": "No explicit joins between tables are needed. Results from different OMS-related tables will be combined using UNION ALL.",
  "metrics_formulas": "Not applicable; this query is for listing distinct OMS systems and their associated marketplaces.",
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands (general)",
      "column": "group_level_id",
      "value": "22",
      "operator": "=",
      "tables": [
        "zs_observe.increff_sales",
        "zs_observe.amazon_oms"
      ]
    },
    {
      "type": "tenant",
      "name": "Mensa Brands (Bracheium Brand Technologies entity)",
      "column": "group_level_id",
      "value": "29",
      "operator": "=",
      "tables": [
        "zs_observe.unicommerce"
      ]
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "=",
      "tables": [
        "zs_observe.unicommerce",
        "zs_observe.increff_sales",
        "zs_observe.amazon_oms"
      ]
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column in 'zs_observe.unicommerce' and 'zs_observe.increff_sales' accurately represents marketplace names. The 'zs_observe.amazon_oms' table is identified as an OMS for Mensa, but the context does not explicitly state a 'sales_channel' or similar column to dynamically list connected marketplaces within that table. It is assumed to implicitly handle the 'Amazon' marketplace. The 'is_active' filter is assumed to apply to 'amazon_oms' as well, based on common schema patterns.",
  "sql_skeleton": "SELECT DISTINCT 'Unicommerce' AS oms_system, sales_channel FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true UNION ALL SELECT DISTINCT 'Increff' AS oms_system, sales_channel FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true UNION ALL SELECT DISTINCT 'Amazon OMS' AS oms_system, 'Amazon' AS sales_channel FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true;"
}
