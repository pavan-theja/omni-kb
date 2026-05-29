## 006. Generate a report showing COD remittance type by courier.

### Query

```text
Generate a report showing COD remittance type by courier.

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

### RAG_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "courier_shipment_count",
    "account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement",
    "account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table contains courier information (`fulfilment_channel`) and `group_level_id` for tenant filtering, making it the most suitable source for courier-related sales data for Mensa. Other tables are for a different tenant (Prita Designs) or are logistics query patterns."
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('by courier'). The column description 'Courier/logistics partner used (80+ variants)' in `table.zs_observe.increff_sales` directly matches this requirement."
    },
    {
      "field": "cod_remittance_type",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('COD remittance type'). This column is logically inferred to exist within a sales or logistics table (like `increff_sales`) to classify how COD payments are remitted."
    },
    {
      "field": "payment_method",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required to filter for 'COD' shipments. This column is logically inferred to exist within the `increff_sales` table to identify the payment method of an order/shipment."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id` column in `table.zs_observe.increff_sales` has a documented description of '22', which is the identifier for Mensa."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT fulfilment_channel, cod_remittance_type",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(fulfilment_channel, cod_remittance_type)",
    "deduplication_rule": "DISTINCT on (fulfilment_channel, cod_remittance_type) to list unique pairings."
  },
  "filters": [
    "group_level_id = '22'",
    "payment_method = 'COD'"
  ],
  "joins": "No joins are required as all necessary information (courier, COD remittance type, payment method, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",
  "missing_or_ambiguous": "The explicit column names `payment_method` and `cod_remittance_type` within `table.zs_observe.increff_sales` and the specific value 'COD' for `payment_method` are not provided in the context and were inferred. The inference is based on the need to fulfill the query's filter and grouping conditions, assuming such detail would be present in a sales/logistics operational table.",
  "sql_skeleton": "SELECT DISTINCT fulfilment_channel, cod_remittance_type FROM zs_observe.increff_sales WHERE group_level_id = '22' AND payment_method = 'COD'"
}
