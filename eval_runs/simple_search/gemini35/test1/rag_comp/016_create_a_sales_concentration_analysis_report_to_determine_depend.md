## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Timing

- started_at: `2026-05-28T10:15:05+00:00`
- duration_seconds: `18.437`
- RAG_COMPLETION_seconds: `18.436`

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

Scope:
- platform account: Mensa

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

### RAG_COMPLETION

{
  "filters": [
    "group_level_id = 22",
    "sales_channel IS NOT NULL"
  ],
  "joins": "No joins needed as multi-channel sales are consolidated inside the single zs_observe.increff_sales table.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "GROUP BY sales_channel",
    "denominator": "SUM(selling_price)",
    "formula": "SUM(selling_price) of top 2 channels / SUM(selling_price) of all channels",
    "numerator": "SUM(selling_price) FILTER (WHERE sales_rank <= 2)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.meesho_sales",
    "zs_observe.amazon_oms",
    "zs_observe.amazon_settlement",
    "zs_observe.shopify_oms",
    "zs_observe.target_sales"
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Identifies the marketplace channel to rank and calculate concentration.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "selling_price",
      "reason": "Used to aggregate total sales volume per channel for ranking.",
      "role": "Revenue Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "group_level_id",
      "reason": "Filters transactions to Mensa Brands (group_level_id = 22).",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Consolidates sales from active marketplaces like Myntra, Flipkart, and Amazon, enabling rank-based concentration analysis.",
      "role": "Multi-channel sales transactions table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "WITH channel_sales AS (SELECT sales_channel, SUM(TRY_CAST(selling_price AS DOUBLE)) AS total_sales FROM zs_observe.increff_sales WHERE group_level_id = 22 AND sales_channel IS NOT NULL GROUP BY 1), ranked_sales AS (SELECT sales_channel, total_sales, SUM(total_sales) OVER() AS grand_total, ROW_NUMBER() OVER(ORDER BY total_sales DESC) AS sales_rank FROM channel_sales) SELECT sales_channel, total_sales, grand_total, total_sales * 100.0 / grand_total AS concentration_percentage, CASE WHEN sales_rank <= 2 THEN 'Top 2 Dependent' ELSE 'Other' END AS dependency_classification FROM ranked_sales ORDER BY sales_rank;"
}
