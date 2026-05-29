## 004. Generate a courier-wise channel mapping report.

### Query

```text
Generate a courier-wise channel mapping report.

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
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.transporter",
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "increff_sales",
      "description": "Sales data from Increff WMS."
    }
  ],
  "required_columns": [
    {
      "column_name": "transporter",
      "role": "courier identifier",
      "notes": "To identify the courier partner."
    },
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To identify the sales channel/marketplace."
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
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.increff_sales' for this query.",
  "metrics_formulas": "Not applicable; this query is for listing distinct values.",
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands",
      "column": "group_level_id",
      "value": "22",
      "operator": "="
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "="
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'transporter' column accurately represents courier names and 'sales_channel' represents marketplace names. Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands within the 'increff_sales' table.",
  "sql_skeleton": "SELECT DISTINCT transporter, sales_channel FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true;"
}
