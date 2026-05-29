## 012. Generate a logistics dependency matrix showing courier concentration across marketplaces.

### Query

```text
Generate a logistics dependency matrix showing courier concentration across marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ],
  "rejected_or_ambiguous_fields": ["array of objects or strings"],
  "metric_logic": {
    "formula": "string or null",
    "numerator": "string or null",
    "denominator": "string or null",
    "aggregation_grain": "string or null",
    "deduplication_rule": "string or null"
  },
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "cleaned_v2`",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "raw cleaned v2 clients mpl usa json",
    "source document",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources",
    "business_scope_set.mpl_india.bank_reconciliation",
    "business_scope_set.mpl_india.cashfree_expense",
    "account_data_binding.mensa.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_returns",
    "account_data_binding.mensa.meesho_in.primary.meesho_reverse",
    "account_data_binding.mensa.meesho_in.primary.meesho_reverse_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_sales",
    "account_data_binding.mensa.meesho_in.primary.meesho_settlement",
    "account_data_binding.mensa.myntra_in.primary.myntra_non_order_settlement",
    "account_data_binding.mensa.myntra_in.primary.myntra_oms",
    "account_data_binding.mensa.myntra_in.primary.myntra_oms_settlement",
    "account_data_binding.mensa.xpressbees_in.primary.xpressbees_settlement",
    "account_data_binding.mpl_india.amazon_payin.primary.amazon_payin",
    "account_data_binding.mpl_india.cashfree_expense.primary.cashfree_expense_report",
    "account_data_binding.mpl_india.cashfree_payin.primary.cashfree_payin",
    "account_data_binding.mpl_india.cashfree_payout.primary.cashfree_payout",
    "account_data_binding.mpl_india.easebuzz_payin.primary.easebuzz_payin",
    "account_data_binding.mpl_india.idfc_bank.primary.idfc_bank",
    "account_data_binding.mpl_india.paynimo_payin.primary.paynimo_payin",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_addition_charge",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_mapper_gst",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_mapping",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_oms",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_settlement",
    "account_data_binding.bear_house_clothing.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.bear_house_clothing.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bear_house_clothing.unicommerce_oms.primary.unicommerce"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is suitable for linking couriers (`fulfilment_channel`) and marketplaces (`sales_channel`) for Mensa, as indicated by its inclusion in `business_scope_set.mensa_brands.operations_wms` and its common use in similar previous queries for Mensa's operational data."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify the 'marketplaces' as requested in the report. This column is logically present in a sales table to indicate the origin of the sale."
    },
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify 'couriers' as requested in the report. The column description 'Courier/logistics partner used (80+ variants)' in `table.zs_observe.increff_sales` directly matches this requirement."
    },
    {
      "field": "order_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Required to calculate 'concentration' as a count of shipments/orders. Counting distinct order IDs provides the volume metric for the dependency matrix."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id = 22` is the documented identifier for Mensa across its operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set`."
    },
    {
      "field": "order_status",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set`."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "COUNT(DISTINCT order_id)",
    "numerator": "COUNT(DISTINCT order_id)",
    "denominator": null,
    "aggregation_grain": "(sales_channel, fulfilment_channel)",
    "deduplication_rule": "COUNT(DISTINCT order_id) to count unique shipments/orders per marketplace and courier."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (marketplace, courier, order count, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred from domain knowledge of sales/operations tables and previous similar queries for Mensa. These inferences are based on the need to fulfill the query's grouping, metric calculation, and filtering conditions.",
  "sql_skeleton": "SELECT sales_channel, fulfilment_channel, COUNT(DISTINCT order_id) AS shipment_count FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES' GROUP BY sales_channel, fulfilment_channel ORDER BY sales_channel, fulfilment_channel"
}
