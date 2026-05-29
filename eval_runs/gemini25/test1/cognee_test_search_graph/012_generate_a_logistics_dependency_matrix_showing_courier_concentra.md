## 012. Generate a logistics dependency matrix showing courier concentration across marketplaces.

### Query

```text
Generate a logistics dependency matrix showing courier concentration across marketplaces.

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
    "column.zs_observe.increff_sales.fulfilment_channel",
    "column.zs_observe.increff_sales.external_shipment_id",
    "column.zs_observe.increff_sales.group_level_id",
    "column.zs_observe.increff_sales.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "platform": "Increff"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "increff_sales",
      "description": "Sales data from Increff WMS, which contains sales channel and fulfilment channel information."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "marketplace identifier",
      "notes": "To identify the marketplaces."
    },
    {
      "column_name": "fulfilment_channel",
      "role": "courier/logistics partner identifier",
      "notes": "To identify the couriers used for fulfilment. Described as having 80+ variants."
    },
    {
      "column_name": "external_shipment_id",
      "role": "shipment identifier",
      "notes": "To count individual shipments for concentration metrics."
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
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.increff_sales'.",
  "metrics_formulas": [
    {
      "metric_name": "courier_shipment_count",
      "formula": "COUNT(DISTINCT external_shipment_id)",
      "aggregation_grain": "per sales_channel and fulfilment_channel"
    }
  ],
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
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column in `zs_observe.increff_sales` accurately represents marketplace names. Assumes 'is_active' column exists in `zs_observe.increff_sales` as per common schema patterns and previous context. The term 'concentration' is interpreted as the count of distinct shipments per marketplace and courier combination.",
  "sql_skeleton": "SELECT sales_channel, fulfilment_channel, COUNT(DISTINCT external_shipment_id) AS shipment_count FROM zs_observe.increff_sales WHERE group_level_id = 22 AND is_active = true GROUP BY sales_channel, fulfilment_channel ORDER BY sales_channel, shipment_count DESC;"
}
