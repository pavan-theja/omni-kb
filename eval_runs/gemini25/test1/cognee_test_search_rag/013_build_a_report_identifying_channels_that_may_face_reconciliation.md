## 013. Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

### Query

```text
Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

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
    "metric.settlement_cycle_days",
    "metric.settlement_variance",
    "metric.settlement_velocity",
    "metric.settlement_batch_structure",
    "metric.settlement_batch_summary",
    "metric.settlement_value_b2b_po_value",
    "table.zs_observe.meesho_settlement",
    "column.zs_observe.meesho_settlement.settlement_date",
    "column.zs_observe.meesho_settlement.order_id",
    "column.zs_observe.meesho_settlement.final_settlement_amount",
    "column.zs_observe.meesho_settlement.settled_amount",
    "column.zs_observe.meesho_settlement.group_level_id",
    "column.zs_observe.meesho_settlement.is_active",
    "column.zs_observe.meesho_settlement.invoice_number",
    "table.zs_observe.healthkart_settlement",
    "column.zs_observe.healthkart_settlement.settlement_date",
    "column.zs_observe.healthkart_settlement.order_id",
    "column.zs_observe.healthkart_settlement.settled_amount",
    "column.zs_observe.healthkart_settlement.group_level_id",
    "column.zs_observe.healthkart_settlement.is_active"
  ],
  "entity_names": {
    "tenant": "Mensa Brands",
    "marketplaces": [
      "Flipkart",
      "Myntra",
      "Nykaa",
      "AJIO",
      "Snapdeal",
      "Meesho",
      "HealthKart"
    ]
  },
  "source_tables": [
    {
      "schema_name": "zs_observe",
      "table_name": "meesho_settlement",
      "description": "Settlement and payout data for Meesho marketplace."
    },
    {
      "schema_name": "zs_observe",
      "table_name": "healthkart_settlement",
      "description": "Settlement and payout data for HealthKart marketplace."
    }
  ],
  "required_columns": [
    {
      "column_name": "settlement_date",
      "role": "date column",
      "notes": "To identify the period of settlement for tables where available (e.g., meesho_settlement, healthkart_settlement). Implicit for other marketplaces based on settlement metrics."
    },
    {
      "column_name": "order_id",
      "role": "join/transaction key",
      "notes": "To link settlement records to specific transactions (e.g., meesho_settlement, healthkart_settlement). Implicit for other marketplaces."
    },
    {
      "column_name": "settled_amount",
      "role": "amount column",
      "notes": "Represents the net amount settled (e.g., settled_amount for healthkart_settlement; final_settlement_amount or settled_amount for meesho_settlement). Implicit for other marketplaces."
    },
    {
      "column_name": "invoice_number",
      "role": "primary key / transaction identifier",
      "notes": "Primary key candidate for meesho_settlement, useful for reconciliation."
    },
    {
      "column_name": "group_level_id",
      "role": "filter column",
      "notes": "Used to filter data for the specific tenant (Mensa Brands)."
    },
    {
      "column_name": "is_active",
      "role": "filter column",
      "notes": "Mandatory filter for active records where available (e.g., meesho_settlement, healthkart_settlement)."
    }
  ],
  "relationships_join_paths": "No explicit joins needed between different marketplace settlement data for identifying potential delays. Information is gathered per marketplace.",
  "metrics_formulas": [
    {
      "metric_name": "settlement_cycle_days",
      "formula": "Difference between transaction/capture/created date and settlement/payout date (Flipkart)",
      "aggregation_grain": "per marketplace, averaged over a period",
      "notes": "Direct indicator of reconciliation delay."
    },
    {
      "metric_name": "settlement_variance",
      "formula": "Actual settled amount vs. expected (Myntra, Nykaa)",
      "aggregation_grain": "per marketplace",
      "notes": "Indicator of discrepancies requiring reconciliation effort/delay."
    },
    {
      "metric_name": "settlement_velocity",
      "formula": "Rate of settlement (Myntra)",
      "aggregation_grain": "per marketplace",
      "notes": "Can imply speed or slowness of settlement processes."
    }
  ],
  "tenant_group_platform_account_filters": [
    {
      "type": "tenant",
      "name": "Mensa Brands (HealthKart)",
      "column": "group_level_id",
      "value": "26",
      "operator": "=",
      "tables": [
        "zs_observe.healthkart_settlement"
      ]
    },
    {
      "type": "tenant",
      "name": "Mensa Brands (Meesho)",
      "column": "group_level_id",
      "value": "22",
      "operator": "=",
      "tables": [
        "zs_observe.meesho_settlement"
      ]
    },
    {
      "type": "record_status",
      "column": "is_active",
      "value": "true",
      "operator": "=",
      "notes": "Applied to marketplace settlement tables where an `is_active` column is expected."
    }
  ],
  "assumptions_missing_information_ambiguity": "The exact database table names for settlement data for Flipkart, Myntra, Nykaa, AJIO, and Snapdeal are not explicitly provided as `table` canonical cards in this context, but their existence is strongly implied by the presence of marketplace-specific settlement metrics (e.g., `metric.settlement_cycle_days` for Flipkart, `metric.settlement_variance` for Myntra/Nykaa, `metric.settlement_value_b2b_po_value` for AJIO, `metric.settlement_batch_summary` for Snapdeal). 'Reconciliation delays' are interpreted as issues arising from the nature of marketplace settlements, which can involve varying settlement cycles, complex fee structures, and potential discrepancies (variance). The `group_level_id` for Mensa is assumed to be '22' for Meesho based on common patterns, and '26' for HealthKart based on explicit context. Other marketplace-specific `group_level_id` values are not provided in this context and are assumed to be managed externally.",
  "sql_skeleton": "SELECT 'Meesho' AS marketplace, 'Settlement Table Exists (potential for reconciliation delays)' AS reason, 'zs_observe.meesho_settlement' AS source_table FROM zs_observe.meesho_settlement WHERE group_level_id = 22 AND is_active = true GROUP BY 1,2,3 UNION ALL SELECT 'HealthKart' AS marketplace, 'Settlement Table Exists (potential for reconciliation delays)' AS reason, 'zs_observe.healthkart_settlement' AS source_table FROM zs_observe.healthkart_settlement WHERE group_level_id = 26 AND is_active = true GROUP BY 1,2,3 UNION ALL SELECT 'Flipkart' AS marketplace, 'Known Settlement Cycle Days metric indicates potential delays' AS reason, NULL AS source_table UNION ALL SELECT 'Myntra' AS marketplace, 'Known Settlement Variance and Velocity metrics indicate potential delays' AS reason, NULL AS source_table UNION ALL SELECT 'Nykaa' AS marketplace, 'Known Settlement Variance metric indicates potential delays' AS reason, NULL AS source_table UNION ALL SELECT 'AJIO' AS marketplace, 'Known B2B Settlement Value metric indicates reconciliation process' AS reason, NULL AS source_table UNION ALL SELECT 'Snapdeal' AS marketplace, 'Known Settlement Batch Structure and Summary metrics indicate reconciliation process complexity' AS reason, NULL AS source_table ORDER BY marketplace;"
}
