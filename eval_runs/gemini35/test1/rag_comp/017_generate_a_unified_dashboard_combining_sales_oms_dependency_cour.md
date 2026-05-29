## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-28T10:15:23+00:00`
- duration_seconds: `40.872`
- RAG_COMPLETION_seconds: `40.87`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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
    "increff_sales.group_level_id = 22",
    "increff_sales.sales_channel IS NOT NULL"
  ],
  "joins": "FULL OUTER JOIN between increff_sales aggregation CTE and increff_returns aggregation CTE on sales_channel.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "GROUP BY sales_channel",
    "denominator": null,
    "formula": "COUNT(DISTINCT order_id) for sales volume, predominant courier per channel, and customer return share %",
    "numerator": null
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.meesho_sales",
    "zs_observe.meesho_returns",
    "zs_observe.shopify_oms",
    "zs_observe.shopify_returns"
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Identifies the channel (e.g. Myntra, Amazon, Shopify) to determine sales share and OMS dependency.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "fulfilment_channel",
      "reason": "Identifies the logistics/courier partner handling the dispatch to map logistics dependency.",
      "role": "Courier Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "order_id",
      "reason": "Used to aggregate order volume and rank channels by performance.",
      "role": "Order Metric Key",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "group_level_id",
      "reason": "Filters records to Mensa Brands (group_level_id = 22).",
      "role": "Tenant Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "return_order_item_id",
      "reason": "Used to count return transaction items to calculate return rates and ownership distribution.",
      "role": "Return Metric Key",
      "selected?": "Selected",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "return_order_type",
      "reason": "Differentiates between Customer Returns (warehouse-handling) and RTO (courier-handled) to show return ownership.",
      "role": "Return Ownership Classification",
      "selected?": "Selected",
      "table": "zs_observe.increff_returns"
    }
  ],
  "required_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Provides consolidated sales channels, order volumes, and fulfillment courier data for Mensa Operations.",
      "role": "Core warehouse-level sales transactions table",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides consolidated return channels, return items volume, and QC/handling status for Mensa Returns.",
      "role": "Core warehouse-level returns table",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH sales_summary AS (SELECT sales_channel, COUNT(DISTINCT order_id) AS total_orders, MAX(fulfilment_channel) AS primary_courier FROM zs_observe.increff_sales WHERE group_level_id = 22 AND sales_channel IS NOT NULL GROUP BY 1), returns_summary AS (SELECT sales_channel, COUNT(DISTINCT return_order_item_id) AS returned_items, SUM(CASE WHEN return_order_type = 'CUSTOMER_RETURN' THEN 1 ELSE 0 END) * 100.0 / NULLIF(COUNT(*), 0) AS customer_return_share_pct FROM zs_observe.increff_returns GROUP BY 1) SELECT COALESCE(s.sales_channel, r.sales_channel) AS channel_name, CASE WHEN COALESCE(s.sales_channel, r.sales_channel) = 'SHOPIFY' THEN 'Direct D2C (Shopify)' WHEN COALESCE(s.sales_channel, r.sales_channel) IN ('AMAZON_SC', 'FLIPKARTV3', 'MYNTRAV4') THEN 'Integrated WMS / OMS' ELSE 'Multi-OMS / Unicommerce' END AS oms_dependency_model, s.total_orders, s.primary_courier AS courier_dependency, r.returned_items, r.customer_return_share_pct AS customer_return_ownership_pct FROM sales_summary s FULL OUTER JOIN returns_summary r ON s.sales_channel = r.sales_channel ORDER BY s.total_orders DESC;"
}
