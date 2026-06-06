## 005. Which courier handles the own website shipments?

### Query

```text
Which courier handles the own website shipments?

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
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
    "account_data_binding.ardeur_fashion.flipkart_in.primary.cashback",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.volans_epic_llc.target_us.primary.target_sales",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is explicitly mentioned in the context and contains `fulfilment_channel` for courier information and `group_level_id` for tenant identification. It is the most appropriate source for logistics and sales data for Mensa Brands through Increff."
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the question ('Which courier handles'). The column description 'Courier/logistics partner used (80+ variants)' directly matches the requirement. This field exists in `table.zs_observe.increff_sales`."
    },
    {
      "field": "channel",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required to filter for 'own website shipments'. While not explicitly named in the provided context for `zs_observe.increff_sales`, a 'channel' column is a logical necessity for sales data. `value_profile.increff_sales.sales_channel.reference` implies a column for sales channel exists. 'Website' is inferred as a common value for 'own website' channels."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id` column in `table.zs_observe.increff_sales` has a documented description of '22' which is the identifier for Mensa."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT fulfilment_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "fulfilment_channel",
    "deduplication_rule": "DISTINCT on (fulfilment_channel) to list unique couriers."
  },
  "filters": [
    "group_level_id = '22'",
    "channel = 'Website'"
  ],
  "joins": "No joins are required as all necessary information (courier, channel, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",
  "missing_or_ambiguous": "The explicit column name `channel` within `table.zs_observe.increff_sales` and its specific value 'Website' for 'own website shipments' are not provided in the context and were inferred. The inference is based on the need to fulfill the query's filter condition and domain knowledge that a sales channel would be available in such a table.",
  "sql_skeleton": "SELECT DISTINCT fulfilment_channel FROM zs_observe.increff_sales WHERE group_level_id = '22' AND channel = 'Website'"
}
