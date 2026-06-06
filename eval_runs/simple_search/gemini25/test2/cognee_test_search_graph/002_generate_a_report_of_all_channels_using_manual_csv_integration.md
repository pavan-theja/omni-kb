## 002. Generate a report of all channels using Manual CSV integration.

### Query

```text
Generate a report of all channels using Manual CSV integration.

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
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "table.zs_observe.nykaa_mapper_gst",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report"
  ],
  "require_tables": [
    {
      "field": "account_data_bindings",
      "role": "Source for Channel Definitions and Integration Types",
      "selected?": "Yes",
      "reason": "Inferred as the logical metadata table containing all `account_data_binding` card details. These cards define specific integrations/channels for Mensa Brands and would logically contain properties like integration type."
    }
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('all channels'). This is inferred as the column representing the 'name' field of each `account_data_binding` card (e.g., 'Amazon Oms'), which acts as the channel identifier."
    },
    {
      "field": "integration_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly requested for filtering ('using Manual CSV integration'). This column is inferred to exist within the `account_data_bindings` logical table to categorize the integration method for each channel. Its presence and specific value ('Manual CSV') are inferred due to the direct request but lack of explicit mention in the context."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands'. The `group_level_id = 22` is explicitly defined in Mensa's `account_data_binding` cards' `scope_keys`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT [channel_name]",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name",
    "deduplication_rule": "DISTINCT on (channel_name)"
  },
  "filters": [
    "group_level_id = '22'",
    "integration_type = 'Manual CSV'"
  ],
  "joins": "No joins are required as all necessary information (channel name, integration type, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.",
  "missing_or_ambiguous": "The explicit physical table name for `account_data_bindings` and the column names `channel_name` and `integration_type` are inferred based on the request and domain knowledge. The presence of an `integration_type` field and its specific value 'Manual CSV' are also inferred, as they are critical to fulfilling the query's filter condition but are not explicitly mentioned in the context.",
  "sql_skeleton": "SELECT DISTINCT channel_name FROM account_data_bindings WHERE group_level_id = '22' AND integration_type = 'Manual CSV'"
}
