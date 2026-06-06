## 009. Calculate the combined marketplace contribution vs own website contribution.

### Timing

- started_at: `2026-05-28T11:14:12+00:00`
- duration_seconds: `19.156`
- GRAPH_COMPLETION_seconds: `19.156`

### Query

```text
Calculate the combined marketplace contribution vs own website contribution.

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
  "required_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ],
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
  "filters": [
    "group_level_id = 22",
    "sales_channel IS NOT NULL"
  ],
  "joins": "No joins are needed as all multi-channel sales and GMV metrics reside in the single consolidated table zs_observe.increff_sales.",
  "metric_logic": {
    "aggregation_grain": "channel_grouping",
    "deduplication_rule": "GROUP BY CASE WHEN sales_channel = 'SHOPIFY' THEN 'Own Website' ELSE 'Marketplace' END",
    "denominator": "SUM(charged_amount)",
    "formula": "SUM(charged_amount) partitioned by channel grouping",
    "numerator": "SUM(CASE WHEN sales_channel = 'SHOPIFY' THEN charged_amount ELSE 0 END)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.nykaa_oms",
    "zs_observe.ajio_oms",
    "zs_observe.amazon_oms",
    "zs_observe.myntra_oms",
    "zs_observe.jiomart_oms"
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Used to classify sales into Own Website ('SHOPIFY') vs Marketplaces.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "charged_amount",
      "reason": "Primary GMV field representing sale price to buyer to determine contribution.",
      "role": "Metric Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "group_level_id",
      "reason": "Filters data for Mensa Brands (group_level_id = 22).",
      "role": "Tenant Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains multi-channel transactions with sales channel markings and order GMV values.",
      "role": "Consolidated sales transactions table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "WITH channel_classification AS (SELECT CASE WHEN sales_channel = 'SHOPIFY' THEN 'Own Website' ELSE 'Marketplace' END AS channel_group, SUM(charged_amount) AS total_gmv FROM zs_observe.increff_sales WHERE group_level_id = 22 AND sales_channel IS NOT NULL GROUP BY 1), total_sales AS (SELECT SUM(total_gmv) AS overall_total FROM channel_classification) SELECT channel_group, total_gmv, (total_gmv * 100.0 / NULLIF((SELECT overall_total FROM total_sales), 0)) AS contribution_pct FROM channel_classification ORDER BY total_gmv DESC;"
}
