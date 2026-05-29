## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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
  "selected_source": null,
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.rosenza_international_trading_llc.amazon_us.primary.amazon_settlement",
    "account_data_binding.rosenza_international_trading_llc.shopify_d2c.primary.shopify_oms",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.logistics_settlement",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table (Sales, OMS, Courier)",
      "selected?": "Yes",
      "reason": "This table is central to Mensa's operations (via Increff WMS/OMS) and provides sales data, channel information, and fulfilment details (couriers) as identified in previous queries."
    },
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table (Returns)",
      "selected?": "Yes",
      "reason": "This table is explicitly a 'Cross-channel returns log (ops view)' for Mensa's Increff operations and is necessary to gather data on return ownership/handling models, as identified in previous queries."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Common Grouping Key)",
      "selected?": "Yes",
      "reason": "This field is present in both `increff_sales` and `increff_returns` and is essential for combining data by channel and categorizing into marketplace vs. own website."
    },
    {
      "field": "order_id",
      "role": "Metric (Sales Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used in `increff_sales` to quantify sales volume and concentration. Inferred as the unique identifier for sales transactions."
    },
    {
      "field": "fulfilment_channel",
      "role": "Dimension (Courier Dependency)",
      "selected?": "Yes",
      "reason": "From `increff_sales`, this column directly identifies the courier/logistics partner for sales orders, crucial for courier concentration analysis."
    },
    {
      "field": "return_id",
      "role": "Metric (Return Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used in `increff_returns` to quantify return volume. Inferred as the unique identifier for return transactions."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = 22`) for all Mensa-scoped data in both `increff_sales` and `increff_returns`."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Record Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`is_active = true`) for data validity in both `increff_sales` and `increff_returns`."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Sales Order Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = COMPLETED`) for valid sales transactions in `increff_sales`."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Sales Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = SALES`) for valid sales transactions in `increff_sales`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Consolidate sales volume, OMS dependency (implicit 'Increff Operations'), courier concentration, and return volume/handling model by sales channel.",
    "numerator": "COUNT(DISTINCT order_id) for sales; COUNT(DISTINCT return_id) for returns.",
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) and COUNT(DISTINCT return_id) to count unique sales and return transactions respectively."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' (for sales)",
    "transaction_type = 'SALES' (for sales)",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart', 'Shopify', 'Website') (inferred categories)"
  ],
  "joins": "A FULL OUTER JOIN is used to combine aggregated sales data (from `zs_observe.increff_sales`) and aggregated returns data (from `zs_observe.increff_returns`) based on the common dimension `sales_channel`. This allows for a unified view where a channel might have sales but no returns, or vice versa.",
  "missing_or_ambiguous": "The request for a 'unified dashboard combining' multiple distinct data points (sales, OMS, courier, returns) implies consolidation of data from multiple sources. While the hard rules usually default to a single source, 'combining' is interpreted here as an explicit request for consolidation. The specific column names `order_id` in `increff_sales` and `return_id` in `increff_returns` are inferred as unique identifiers. The identification of 'Increff Operations' as the OMS and the categorization of `sales_channel` into 'Own Website' vs. 'Marketplace' for return handling are strong inferences from previous query patterns and domain knowledge.",
  "sql_skeleton": "WITH SalesData AS (\n    SELECT\n        sales_channel,\n        'Increff Operations' AS oms_system,\n        COUNT(DISTINCT order_id) AS total_sales_orders,\n        COUNT(DISTINCT fulfilment_channel) AS num_unique_couriers_for_sales\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n),\nReturnsData AS (\n    SELECT\n        sales_channel,\n        CASE\n            WHEN sales_channel IN ('Shopify', 'Website') THEN 'Own Website Returns'\n            WHEN sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace Returns'\n            ELSE 'Other/Unspecified Returns'\n        END AS return_handling_model,\n        COUNT(DISTINCT return_id) AS total_returns\n    FROM\n        zs_observe.increff_returns\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n    GROUP BY\n        sales_channel\n)\nSELECT\n    COALESCE(sd.sales_channel, rd.sales_channel) AS sales_channel,\n    sd.oms_system,\n    COALESCE(sd.total_sales_orders, 0) AS total_sales_orders,\n    sd.num_unique_couriers_for_sales,\n    rd.return_handling_model,\n    COALESCE(rd.total_returns, 0) AS total_returns\nFROM\n    SalesData sd\nFULL OUTER JOIN\n    ReturnsData rd ON sd.sales_channel = rd.sales_channel\nORDER BY\n    COALESCE(sd.sales_channel, rd.sales_channel)"
}
