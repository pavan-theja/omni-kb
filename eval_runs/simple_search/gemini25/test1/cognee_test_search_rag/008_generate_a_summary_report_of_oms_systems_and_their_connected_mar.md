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
    "table.zs_observe.shopify_oms"
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
      "description": "Unified transaction ledger in Unicommerce OMS for sales, returns, and cancellations."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "increff_sales",
      "description": "Sales data from Increff WMS, also contains sales channel information."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "amazon_oms",
      "description": "Order Management System data specifically for the Amazon marketplace."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "myntra_oms",
      "description": "Order Management System data specifically for the Myntra marketplace."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "shopify_oms",
      "description": "Order Management System data specifically for the Shopify D2C channel."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "marketplace identifier",
      "notes": "Used in Unicommerce and Increff to identify various marketplaces."
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
  "relationships_join_paths": "No explicit joins needed between different OMS tables; each OMS table is queried independently to identify its associated marketplaces/channels.",
  "metrics_formulas": "Not applicable; this query is for listing distinct values.",
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
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column in `unicommerce` and `increff_sales` accurately represents marketplace names. For `amazon_oms`, `myntra_oms`, and `shopify_oms`, the marketplace is implied by the OMS name itself ('Amazon', 'Myntra', 'Shopify D2C/Website'). Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands for Increff, Amazon, Myntra, and Shopify, and 'group_level_id = 29' for Unicommerce, based on previous query history. An `is_active` column exists for `unicommerce`, `increff_sales`, and `amazon_oms`. The context explicitly indicates that `myntra_oms` does not require an `is_active` filter. The existence of `is_active` in `shopify_oms` is assumed.",
  "sql_skeleton": "SELECT DISTINCT 'Unicommerce' AS oms_system, sales_channel AS marketplace FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true UNION ALL SELECT DISTINCT 'Increff' AS oms_system, sales_channel AS marketplace FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true UNION ALL SELECT 'Amazon OMS' AS oms_system, 'Amazon' AS marketplace FROM zs_observe.amazon_oms WHERE group_level_id = 22 AND is_active = true GROUP BY 1,2 UNION ALL SELECT 'Myntra OMS' AS oms_system, 'Myntra' AS marketplace FROM zs_observe.myntra_oms WHERE group_level_id = <client_id> GROUP BY 1,2 UNION ALL SELECT 'Shopify OMS' AS oms_system, 'Shopify D2C' AS marketplace FROM zs_observe.shopify_oms WHERE group_level_id = <client_id> AND is_active = true GROUP BY 1,2;"
}
