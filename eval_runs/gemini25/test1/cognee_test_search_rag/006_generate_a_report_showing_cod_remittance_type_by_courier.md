## 006. Generate a report showing COD remittance type by courier.

### Query

```text
Generate a report showing COD remittance type by courier.

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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shiprocket_settlement"
  ],
  "entity_names": {
    "tenant": "Mensa Brands"
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "shiprocket_settlement",
      "description": "Logistics settlement data from Shiprocket, a required table for COD reconciliation patterns."
    }
  ],
  "required_columns": [
    {
      "column_name": "courier_partner",
      "role": "courier identifier",
      "notes": "Dimension allowed by 'cod_expected_vs_remitted' query pattern."
    },
    {
      "column_name": "payment_mode",
      "role": "remittance type identifier",
      "notes": "Dimension allowed by 'cod_expected_vs_remitted' query pattern for payment methods."
    },
    {
      "column_name": "cod_remitted_amount",
      "role": "amount column",
      "notes": "Represents the remitted COD amount, corresponding to 'metric.cod_remitted_amount' produced by the query pattern. Actual column name needs to be identified from schema."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records as per semantic filters in logistics query patterns."
    }
  ],
  "relationships_join_paths": "No explicit joins needed for this report if all columns are within 'zs_observe.shiprocket_settlement'.",
  "metrics_formulas": [
    {
      "metric_name": "total_cod_remitted_amount",
      "formula": "SUM(cod_remitted_amount)",
      "aggregation_grain": "per courier_partner, per payment_mode"
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
  "assumptions_missing_information_ambiguity": "Assumes 'courier_partner', 'payment_mode', and a column for 'cod_remitted_amount' exist in 'zs_observe.shiprocket_settlement'. Assumes 'group_level_id = 22' is the correct identifier for Mensa Brands within this table, based on previous logistics-related queries. The precise column name for 'cod_remitted_amount' needs to be confirmed.",
  "sql_skeleton": "SELECT courier_partner, payment_mode, SUM(cod_remitted_amount) AS total_cod_remitted_amount FROM zs_observe.shiprocket_settlement WHERE group_level_id = 22 AND is_active = true GROUP BY courier_partner, payment_mode ORDER BY total_cod_remitted_amount DESC;"
}
