## 003. List all marketplaces handled through Unicommerce.

### Query

```text
List all marketplaces handled through Unicommerce.

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
    "column.zs_observe.unicommerce.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "platform": "Unicommerce"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "unicommerce",
      "description": "Unified transaction ledger in Unicommerce OMS for sales, returns, and cancellations."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "marketplace identifier",
      "notes": "To list the marketplaces"
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands, specifically Bracheium Brand Technologies entity within Mensa Brands)"
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records"
    }
  ],
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.unicommerce' for this query.",
  "metrics_formulas": "Not applicable; this query is for listing distinct values.",
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands",
      "column": "group_level_id",
      "value": "29",
      "operator": "="
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "="
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column accurately represents marketplace names and that 'group_level_id = 29' is the correct identifier for the Bracheium Brand Technologies entity of Mensa Brands within the 'unicommerce' table context. The query will list all relevant sales channels from Unicommerce for this specific tenant entity.",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true;"
}
