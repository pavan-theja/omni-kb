## 007. Which channels use marketplace-managed returns?

### Query

```text
Which channels use marketplace-managed returns?

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
  "selected_source": "metadata.account_data_bindings",
  "rejected_sources": [
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.logistics_settlement",
    "business_scope_set.mensa_brands.operations_wms",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources",
    "business_scope_set.mpl_india.bank_reconciliation",
    "business_scope_set.mpl_india.cashfree_expense",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce",
    "table.zs_observe.unicommerce_order_sales_report"
  ],
  "require_tables": [
    {
      "field": "account_data_bindings",
      "role": "Source for Channel Definitions and Integration Types",
      "selected?": "Yes",
      "reason": "This logical table contains all `account_data_binding` card details, which define specific channels and their integration semantics (like returns). This is the appropriate source to identify which channels use 'marketplace-managed returns' for Mensa."
    }
  ],
  "required_fields": [
    {
      "field": "name",
      "role": "Binding Name for Channel Identification",
      "selected?": "Yes",
      "reason": "The 'name' field of the `account_data_binding` card (e.g., 'Amazon Returns') explicitly states the channel and implicitly indicates a returns-related integration. The marketplace name can be extracted from this field."
    },
    {
      "field": "platform_account_id",
      "role": "Filter Column (Marketplace Identification)",
      "selected?": "Yes",
      "reason": "This field (e.g., `platform_account.mensa.amazon_in.primary`) is crucial to confirm that the identified channel belongs to a marketplace, thus fulfilling the 'marketplace-managed' criterion."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id = 22` is consistently used as the identifier for Mensa within its `account_data_binding` cards."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT (SUBSTRING(name, 1, POSITION(' ' IN name) - 1))",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name",
    "deduplication_rule": "DISTINCT on extracted channel name (e.g., 'Amazon') to list unique channels."
  },
  "filters": [
    "group_level_id = '22'",
    "name LIKE '%Returns%'",
    "platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%walmart%'
  ],
  "joins": "No joins are required as all necessary information (binding name, platform account ID, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.",
  "missing_or_ambiguous": "The explicit physical table name for `account_data_bindings` is inferred. The fields `name`, `platform_account_id`, and `group_level_id` are logically inferred to exist within this metadata structure. The condition for 'marketplace-managed' is inferred by checking `platform_account_id` for known Mensa marketplaces ('Amazon', 'Walmart') and 'returns' is inferred from `name LIKE '%Returns%'`.",
  "sql_skeleton": "SELECT DISTINCT SUBSTRING(name, 1, POSITION(' ' IN name) - 1) AS channel_name FROM account_data_bindings WHERE group_level_id = '22' AND name LIKE '%Returns%' AND (platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%walmart%')"
}
