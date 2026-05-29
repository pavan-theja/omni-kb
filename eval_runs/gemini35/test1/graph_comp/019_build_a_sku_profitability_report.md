## 019. Build a SKU profitability report.

### Timing

- started_at: `2026-05-28T11:19:53+00:00`
- duration_seconds: `78.11`
- GRAPH_COMPLETION_seconds: `78.109`

### Query

```text
Build a SKU profitability report.

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
    "sku_id IS NOT NULL"
  ],
  "joins": "No joins are needed as SKU transaction volume, gross revenue, description, and settlement data reside in the single consolidated table zs_observe.increff_sales.",
  "metric_logic": {
    "aggregation_grain": "sku_id",
    "deduplication_rule": "GROUP BY sku_id, sku_description",
    "denominator": "SUM(TRY_CAST(settled_amount AS DOUBLE))",
    "formula": "SUM(charged_amount) - SUM(TRY_CAST(settled_amount AS DOUBLE))",
    "numerator": "SUM(charged_amount)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.amazon_oms",
    "zs_observe.nykaa_oms",
    "zs_observe.healthkart_oms",
    "zs_observe.jiomart_returns",
    "zs_observe.meesho_brand_mapping"
  ],
  "required_fields": [
    {
      "field": "sku_id",
      "reason": "Identifies individual SKUs to aggregate profit and revenue metrics.",
      "role": "SKU Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "sku_description",
      "reason": "Provides descriptive names for catalog display inside the report.",
      "role": "SKU Description",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "charged_amount",
      "reason": "Fulfills the revenue metric to evaluate product value generated.",
      "role": "Gross Revenue Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "settled_amount",
      "reason": "Fulfills the estimated payout/realization metric to subtract against baseline costs.",
      "role": "Settled Amount Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "group_level_id",
      "reason": "Filters results specifically to Mensa Brands (group_level_id = 22).",
      "role": "Tenant Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains unified SKU-level transactions, gross charged amounts, and settled payout fields required for profitability metrics.",
      "role": "Consolidated sales transactions table",
      "selected?": "Yes"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "SELECT sku_id, sku_description, COUNT(*) AS units_sold, SUM(charged_amount) AS gross_revenue, SUM(TRY_CAST(settled_amount AS DOUBLE)) AS estimated_settlement, (SUM(TRY_CAST(settled_amount AS DOUBLE)) * 100.0 / NULLIF(SUM(charged_amount), 0)) AS recovery_rate_pct FROM zs_observe.increff_sales WHERE group_level_id = 22 AND sku_id IS NOT NULL GROUP BY 1, 2 ORDER BY gross_revenue DESC;"
}
