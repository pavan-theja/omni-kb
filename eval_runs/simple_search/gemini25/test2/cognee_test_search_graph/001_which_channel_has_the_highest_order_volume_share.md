## 001. Which channel has the highest order volume share?

### Query

```text
Which channel has the highest order volume share?

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
    "account_data_binding.volans_epic_llc.target_us.primary.target_sales"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table contains `group_level_id` for tenant filtering and `external_shipment_id` for counting order volume. A 'channel' column is logically inferred to exist within this sales table to represent the sales channel."
    }
  ],
  "required_fields": [
    {
      "field": "channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested for grouping in the question ('Which channel'). Although not explicitly listed in the provided schema for `zs_observe.increff_sales`, a 'channel' column is a standard dimension in sales data tables for classification and is logically inferred here."
    },
    {
      "field": "external_shipment_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Used to calculate 'order volume' by counting distinct shipment IDs. This field is explicitly listed for `zs_observe.increff_sales` as an 'identity_or_reference'."
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
    "formula": "MAX ( (COUNT(DISTINCT external_shipment_id) per channel / Total COUNT(DISTINCT external_shipment_id) for Mensa) * 100 )",
    "numerator": "COUNT(DISTINCT external_shipment_id) GROUPED BY channel",
    "denominator": "TOTAL COUNT(DISTINCT external_shipment_id) for Mensa",
    "aggregation_grain": "channel",
    "deduplication_rule": "COUNT(DISTINCT external_shipment_id) to count unique orders/shipments for volume."
  },
  "filters": [
    "group_level_id = '22'"
  ],
  "joins": "No joins are required as all necessary fields are inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",
  "missing_or_ambiguous": "The explicit column name 'channel' within `zs_observe.increff_sales` is not provided in the context and was inferred as a logical column name. The `fulfilment_channel` column is explicitly for couriers, not sales channels, requiring the inference of a separate 'channel' column for sales classification.",
  "sql_skeleton": "WITH ChannelOrders AS ( SELECT channel, COUNT(DISTINCT external_shipment_id) AS order_count FROM zs_observe.increff_sales WHERE group_level_id = '22' GROUP BY channel ), TotalOrders AS ( SELECT COUNT(DISTINCT external_shipment_id) AS total_order_count FROM zs_observe.increff_sales WHERE group_level_id = '22' ) SELECT co.channel, (CAST(co.order_count AS DECIMAL) / to.total_order_count) * 100 AS order_share FROM ChannelOrders co, TotalOrders to ORDER BY order_share DESC LIMIT 1"
}
