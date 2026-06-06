## 007. Which channels use marketplace-managed returns?

### Query

```text
Which channels use marketplace-managed returns?

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
    "table.zs_observe.increff_returns",
    "column.zs_observe.increff_returns.sales_channel",
    "column.zs_observe.increff_returns.return_order_type",
    "column.zs_observe.increff_returns.group_level_id",
    "column.zs_observe.increff_returns.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "increff_returns",
      "description": "Cross-channel returns log (ops view)"
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To identify the sales channels."
    },
    {
      "column_name": "return_order_type",
      "role": "return management type identifier",
      "notes": "To determine if the return is marketplace-managed."
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
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.increff_returns'.",
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
      "type": "return_management",
      "column": "return_order_type",
      "value": "[Marketplace Managed Return Identifier]",
      "operator": "="
    }
  ],
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column accurately represents channel names. Assumes a specific value within the 'return_order_type' column identifies 'marketplace-managed returns'. The exact identifier for 'marketplace-managed returns' in 'return_order_type' is missing and needs to be determined from external knowledge (e.g., 'MP_MANAGED', 'MARKETPLACE_RETURN'). Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands within the 'increff_returns' table.",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.increff_returns WHERE group_level_id = 22 AND is_active = true AND return_order_type = '[MARKETPLACE_MANAGED_RETURN_IDENTIFIER]';"
}
