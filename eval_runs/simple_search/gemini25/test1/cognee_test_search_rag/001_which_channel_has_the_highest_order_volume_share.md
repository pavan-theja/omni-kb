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

### RAG_COMPLETION

{
  "relevant_canonical_ids": [
    "table.zs_observe.increff_sales",
    "column.zs_observe.increff_sales.sales_channel",
    "column.zs_observe.increff_sales.external_shipment_id",
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
      "description": "Sales data from Increff WMS, likely containing transaction details."
    }
  ],
  "required_columns": [
    {
      "column_name": "sales_channel",
      "role": "channel identifier",
      "notes": "To group orders by channel. This column was referenced in a previous query for Mensa Brands with Increff Sales data."
    },
    {
      "column_name": "external_shipment_id",
      "role": "order volume identifier",
      "notes": "To count distinct shipments as a proxy for order volume. Assumes one shipment generally corresponds to one order or a measurable unit of order volume. If an 'order_id' or 'external_order_id' is available, it would be a more precise measure."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records, commonly found in observational tables."
    }
  ],
  "relationships_join_paths": "No explicit joins needed as all required information is within 'zs_observe.increff_sales' for this query.",
  "metrics_formulas": [
    {
      "metric_name": "total_order_volume",
      "formula": "COUNT(DISTINCT external_shipment_id)",
      "aggregation_grain": "per sales_channel, then overall"
    },
    {
      "metric_name": "order_volume_share",
      "formula": "(total_order_volume_per_channel / total_order_volume_overall) * 100",
      "aggregation_grain": "per sales_channel"
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
  "assumptions_missing_information_ambiguity": "Assumes 'sales_channel' column exists in 'zs_observe.increff_sales' and accurately represents channels. Assumes `external_shipment_id` can serve as a proxy for 'order volume'. The exact definition of 'order volume' (e.g., number of orders, number of items, total value) is not specified; counting distinct shipments is chosen as a common interpretation. Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands within the 'increff_sales' table context.",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT external_shipment_id) AS order_volume\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = 22 AND is_active = true\n    GROUP BY\n        sales_channel\n),\nTotalOrderVolume AS (\n    SELECT\n        SUM(order_volume) AS total_volume\n    FROM\n        ChannelOrderVolume\n)\nSELECT\n    cov.sales_channel,\n    cov.order_volume,\n    (cov.order_volume * 100.0 / tov.total_volume) AS order_volume_share_pct\nFROM\n    ChannelOrderVolume cov,\n    TotalOrderVolume tov\nORDER BY\n    order_volume_share_pct DESC\nLIMIT 1;"
}
