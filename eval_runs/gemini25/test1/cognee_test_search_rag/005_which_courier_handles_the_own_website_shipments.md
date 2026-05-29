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

### RAG_COMPLETION

{
  "relevant_canonical_ids": [
    "table.zs_observe.unicommerce",
    "column.zs_observe.unicommerce.fulfilment_channel",
    "column.zs_observe.unicommerce.sales_channel",
    "column.zs_observe.unicommerce.group_level_id",
    "column.zs_observe.unicommerce.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands"
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
      "column_name": "fulfilment_channel",
      "role": "courier identifier",
      "notes": "To identify the courier partner."
    },
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To identify 'own website' shipments. The specific value for 'own website' is not provided in context."
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
    },
    {
      "type": "sales_channel",
      "column": "sales_channel",
      "value": "[Placeholder for 'Own Website' identifier]",
      "operator": "="
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'fulfilment_channel' accurately represents courier names. Assumes 'group_level_id = 29' is the correct identifier for Mensa Brands (Bracheium Brand Technologies entity) within the 'unicommerce' table context, based on previous query history. The specific value within the 'sales_channel' column that identifies 'own website shipments' is missing and needs to be determined from external knowledge.",
  "sql_skeleton": "SELECT DISTINCT fulfilment_channel FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true AND sales_channel = '[OWN_WEBSITE_IDENTIFIER]';"
}
