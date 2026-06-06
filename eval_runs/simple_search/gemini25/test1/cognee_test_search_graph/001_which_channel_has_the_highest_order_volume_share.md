## 001. Which channel has the highest order volume share?

### Query

```text
Which channel has the highest order volume share?

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
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.external_shipment_id",
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa"
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
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To identify different sales channels."
    },
    {
      "column_name": "external_shipment_id",
      "role": "order identifier",
      "notes": "To count distinct orders for volume calculation."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records."
    }
  ],
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.increff_sales' for this query.",
  "metrics_formulas": "Order volume is calculated by `COUNT(DISTINCT external_shipment_id)`. Channel share is `(channel_order_volume * 100.0) / total_order_volume`. Aggregation grain is by `sales_channel`.",
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa",
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
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column accurately represents channel names and 'external_shipment_id' uniquely identifies an order. Assumes 'is_active' column exists in `zs_observe.increff_sales` as indicated in previous similar queries, though not explicitly detailed in the current snippets. Assumes 'group_level_id = 22' is the correct identifier for Mensa within the 'increff_sales' table.",
  "sql_skeleton": "SELECT sales_channel, COUNT(DISTINCT external_shipment_id) AS order_volume, COUNT(DISTINCT external_shipment_id) * 100.0 / SUM(COUNT(DISTINCT external_shipment_id)) OVER () AS volume_share_percentage FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY sales_channel ORDER BY order_volume DESC LIMIT 1;"
}
