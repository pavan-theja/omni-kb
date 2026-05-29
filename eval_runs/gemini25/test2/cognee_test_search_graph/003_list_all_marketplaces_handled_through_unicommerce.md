## 003. List all marketplaces handled through Unicommerce.

### Query

```text
List all marketplaces handled through Unicommerce.

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
  "selected_source": "table.zs_observe.unicommerce",
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce_order_sales_report",
    "business_flow_binding.bracheium_brand_technologies.marketplace_to_operations",
    "business_flow_binding.bracheium_brand_technologies.marketplace_transactions_future_context",
    "business_flow_binding.bracheium_brand_technologies.shopify_shiprocket_order_flow",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table directly represents Unicommerce data, which is explicitly mentioned in the question. Mensa Brands uses Unicommerce for cross-channel OMS/WMS operational evidence, as per `business_scope_set.mensa_brands.operations_wms`."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('List all marketplaces'). This column is identified in `table.zs_observe.unicommerce` as the field for sales channels/marketplaces in previous turns, and is a logical column for OMS data."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. Mensa's `group_level_id` is consistently `22` across its `account_data_binding` cards and is a standard tenant filter for operational tables like `zs_observe.unicommerce`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT on (sales_channel) to list unique marketplaces."
  },
  "filters": [
    "group_level_id = '22'"
  ],
  "joins": "No joins are required as all necessary information (marketplace names and tenant ID) is available within the single selected table `zs_observe.unicommerce`.",
  "missing_or_ambiguous": "None",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.unicommerce WHERE group_level_id = '22'"
}
