## 005. Which courier handles the own website shipments?

### Timing

- started_at: `2026-05-27T04:03:25+00:00`
- duration_seconds: `33.106`
- RAG_COMPLETION_seconds: `16.453`
- GRAPH_COMPLETION_seconds: `16.652`

### Query

```text
Which courier handles the own website shipments?

Scope:
- tenant: Mensa Brands

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Do not default to a single source table. First identify all grounded candidate sources or relationship paths that could answer the request. Then mark each candidate as direct, supporting, risky, or irrelevant based on whether it contains the required grain, dimensions, measures, filters, and joins. If no candidate is fully grounded, return a partial recommended path with usable fields, risks, and blocking gaps.
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

Return up to 3 recommended SQL packages:
- include only packages grounded in the provided context
- rank packages by directness, completeness, and SQL safety
- mark each package as complete, partial, or risky
- explain what each package can answer and what it cannot answer
- do not merge packages unless the context provides grounded join keys and deduplication rules

Response Format:
Cognee validates completion answers with a wrapper schema where `content` must be a string. To avoid parser failures, the top-level response MUST be a JSON object with exactly one key named `content`, and the value of `content` MUST be a string.

The `content` string must contain one valid JSON object serialized as text. Do not put a JSON object or array directly inside `content`.

Correct top-level shape:
{
  "content": "{\"selected_source\":\"table.example\",\"rejected_sources\":[],\"require_tables\":[],\"required_fields\":[],\"rejected_or_ambiguous_fields\":[],\"metric_logic\":{\"formula\":null,\"numerator\":null,\"denominator\":null,\"aggregation_grain\":null,\"deduplication_rule\":null},\"filters\":[],\"joins\":\"No joins needed\",\"missing_or_ambiguous\":\"None\",\"sql_skeleton\":\"SELECT 1\"}"
}

Incorrect top-level shape:
{
  "content": {
    "selected_source": "table.example"
  }
}

The JSON object inside the `content` string must strictly match this structural schema:
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
  "selected_source": null,
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Source for Sales Channel and Order ID",
      "selected?": "Yes",
      "reason": "This table has been consistently inferred to contain sales order data, including channel information and order identifiers, for Mensa Brands (group_level_id = 22). It is essential for identifying 'own website' sales."
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "role": "Primary Source for Courier Partner",
      "selected?": "Yes",
      "reason": "This table is a logical source for courier information, as 'Shiprocket' is a known logistics platform. The presence of 'courier_partner' is confirmed as an allowed dimension in `query_pattern.logistics.amount_semantics_audit` and it contains order identifiers for joining."
    }
  ],
  "required_fields": [
    {
      "field": "sales.sales_channel",
      "role": "Filter Dimension",
      "selected?": "Yes",
      "reason": "Required to filter for 'Own Website' shipments. This field is logically present in sales data to categorize orders by origin."
    },
    {
      "field": "oms.courier_partner",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify the courier partner(s) for the report. This field is explicitly mentioned as an allowed dimension in logistics query patterns."
    },
    {
      "field": "sales.order_id",
      "role": "Join Key",
      "selected?": "Yes",
      "reason": "Inferred as the common key to join sales data with logistics OMS data, based on common data modeling practices for linking sales orders to their shipping details."
    },
    {
      "field": "oms.order_id",
      "role": "Join Key",
      "selected?": "Yes",
      "reason": "Inferred as the common key to join logistics OMS data with sales data, reflecting a unique order identifier in the logistics system."
    },
    {
      "field": "sales.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`."
    },
    {
      "field": "sales.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set`."
    },
    {
      "field": "sales.order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included."
    },
    {
      "field": "sales.transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) in Increff operations, ensuring only sales transactions are considered."
    },
    {
      "field": "oms.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Inferred to scope logistics data to 'Mensa Brands', consistent with other operational tables and to ensure tenant-specific data isolation."
    },
    {
      "field": "oms.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in logistics operations, consistent with data hygiene across Mensa's systems."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "List distinct courier_partner values for 'Own Website' sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "courier_partner",
    "deduplication_rule": "DISTINCT courier_partner to list each unique courier handling 'Own Website' shipments."
  },
  "filters": [
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'",
    "sales.sales_channel = 'Own Website'",
    "oms.group_level_id = '22'",
    "oms.is_active = true"
  ],
  "joins": "INNER JOIN zs_observe.shiprocket_oms AS oms ON sales.order_id = oms.order_id",
  "missing_or_ambiguous": "The explicit value for `sales_channel` representing 'Own Website' is inferred as 'Own Website' (a common naming convention); actual column values might vary (e.g., 'D2C', 'Website'). The presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped queries. The presence of `order_id`, `courier_partner`, `group_level_id`, and `is_active` within `table.zs_observe.shiprocket_oms` is inferred based on its expected role as a logistics OMS and the need for tenant-level filtering and active record status.",
  "sql_skeleton": "SELECT DISTINCT
    oms.courier_partner
FROM
    zs_observe.increff_sales AS sales
INNER JOIN
    zs_observe.shiprocket_oms AS oms
ON
    sales.order_id = oms.order_id
WHERE
    sales.group_level_id = '22'
    AND sales.is_active = true
    AND sales.order_status = 'COMPLETED'
    AND sales.transaction_type = 'SALES'
    AND sales.sales_channel = 'Own Website' -- Inferred channel name for 'own website'
    AND oms.group_level_id = '22'
    AND oms.is_active = true
ORDER BY
    oms.courier_partner"
}

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table contains the `fulfilment_channel` (courier/logistics partner) and is inferred to contain `sales_channel` and `order_id` for Mensa Brands (group_level_id = 22), making it suitable for linking sales channels to couriers."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Filter Dimension",
      "selected?": "Yes",
      "reason": "Required to filter for 'Own Website' shipments. This column is logically inferred to exist in a sales table like `increff_sales` to categorize orders by origin."
    },
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify the courier partner(s) handling the shipments. The context explicitly describes `column.zs_observe.increff_sales.fulfilment_channel` as 'Courier/logistics partner used (80+ variants)'."
    },
    {
      "field": "order_id",
      "role": "Primary Key / Join Key (for logical integrity)",
      "selected?": "Yes",
      "reason": "Although not directly selected, `order_id` is essential for ensuring that each shipment is linked to a specific order, which is critical for accurate filtering of sales by channel and linking to fulfillment details. It is inferred to exist in a sales transaction table."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Explicitly mentioned in the context for `column.zs_observe.increff_sales.group_level_id` with value `22`, which is required for scoping the report to 'Mensa Brands'."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions)."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) in Increff operations, ensuring only sales transactions are considered for courier analysis."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "List distinct fulfilment_channel values for 'Own Website' sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "fulfilment_channel",
    "deduplication_rule": "DISTINCT fulfilment_channel to list each unique courier handling 'Own Website' shipments."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "sales_channel = 'Own Website'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, courier, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `order_id` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped sales queries. The specific value for `sales_channel` representing 'Own Website' is inferred as 'Own Website' (a common naming convention for Direct-to-Consumer channels); actual column values might vary (e.g., 'D2C', 'Website'). Standard mandatory filters (`is_active`, `order_status`, `transaction_type`) are inferred from consistent usage patterns for Mensa's operational data.",
  "sql_skeleton": "SELECT DISTINCT
    fulfilment_channel
FROM
    zs_observe.increff_sales
WHERE
    group_level_id = '22'
    AND is_active = true
    AND order_status = 'COMPLETED'
    AND transaction_type = 'SALES'
    AND sales_channel = 'Own Website' -- Inferred channel name for 'own website'
ORDER BY
    fulfilment_channel"
}
