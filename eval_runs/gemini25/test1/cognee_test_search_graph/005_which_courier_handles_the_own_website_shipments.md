## 005. Which courier handles the own website shipments?

### Query

```text
Which courier handles the own website shipments?

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
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.fulfilment_channel",
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
      "description": "Sales data from Increff WMS, containing courier and sales channel information."
    }
  ],
  "required_columns": [
    {
      "column_name": "fulfilment_channel",
      "role": "courier identifier",
      "notes": "To identify the courier partner, described in the provided context."
    },
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To identify 'own website' shipments. Presence in `increff_sales` is assumed based on previous queries for this tenant and table, but not explicitly detailed in the current context."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands), with the value '22' specified in the provided context for this table."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records, assumed to be present based on common schema patterns and previous answers."
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
    },
    {
      "type": "sales_channel",
      "column": "sales_channel",
      "value": "[Placeholder for 'Own Website' identifier]",
      "operator": "="
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'fulfilment_channel' accurately represents courier names. Assumes 'sales_channel' column exists in `zs_observe.increff_sales` as indicated by prior query history for Mensa, although not explicitly mentioned in the provided context for this turn. Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands within the 'increff_sales' table context, as specified in the provided context. The specific value within the 'sales_channel' column that identifies 'own website shipments' is missing and needs to be determined from external knowledge. Previous answers for this exact question (for Mensa Brands) utilized `zs_observe.unicommerce` with `group_level_id = 29`, presenting a conflict; this response prioritizes the table and `group_level_id` explicitly detailed in the *current* context.",
  "sql_skeleton": "SELECT DISTINCT fulfilment_channel FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true AND sales_channel = '[OWN_WEBSITE_IDENTIFIER]';"
}
