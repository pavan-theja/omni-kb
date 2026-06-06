## 004. Generate a courier-wise channel mapping report.

### Timing

- started_at: `2026-05-27T04:02:48+00:00`
- duration_seconds: `36.803`
- RAG_COMPLETION_seconds: `19.721`
- GRAPH_COMPLETION_seconds: `17.082`

### Query

```text
Generate a courier-wise channel mapping report.

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
  "filters": [
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'",
    "oms.group_level_id = '22'",
    "oms.is_active = true"
  ],
  "joins": "INNER JOIN zs_observe.shiprocket_oms AS oms ON sales.order_id = oms.order_id",
  "metric_logic": {
    "aggregation_grain": "(sales_channel, courier_partner)",
    "deduplication_rule": "DISTINCT combination of sales_channel and courier_partner to show unique mappings.",
    "denominator": null,
    "formula": "List distinct pairs of (sales_channel, courier_partner)",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped queries. The presence of `order_id`, `courier_partner`, `group_level_id`, and `is_active` within `table.zs_observe.shiprocket_oms` is inferred based on its expected role as a logistics OMS and the need for tenant-level filtering and active record status.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is consistently used for Mensa's sales data, which contains the 'sales_channel' dimension and order identifiers. Its association with Mensa Brands (group_level_id = 22) is confirmed via account data bindings for other Mensa tables, implying its use for sales-related queries for Mensa.",
      "role": "Primary Source for Sales Channel",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "reason": "This table is a logical source for courier information, as 'Shiprocket' is a known logistics platform. The presence of 'courier_partner' is inferred from its role as an OMS in logistics query patterns (e.g., `query_pattern.logistics.amount_semantics_audit` where `courier_partner` is an allowed dimension). It is a direct fit for courier details.",
      "role": "Primary Source for Courier Partner",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales.sales_channel",
      "reason": "Required to identify the sales channel for the mapping report. This is inferred to be a column in `increff_sales` based on typical sales data structures and prior queries.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "oms.courier_partner",
      "reason": "Required to identify the courier partner for the mapping report. This column is inferred to exist in `shiprocket_oms` based on its role as a logistics OMS and relevant query patterns.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_id",
      "reason": "Inferred as the common key to join sales data with logistics OMS data, based on common data modeling practices for linking sales orders to their shipping details and prior inferences about operational relationship keys.",
      "role": "Join Key",
      "selected?": "Yes"
    },
    {
      "field": "oms.order_id",
      "reason": "Inferred as the common key to join logistics OMS data with sales data, reflecting a unique order identifier in the logistics system.",
      "role": "Join Key",
      "selected?": "Yes"
    },
    {
      "field": "sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "sales.is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are considered for channel mapping.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "oms.group_level_id",
      "reason": "Inferred to scope logistics data to 'Mensa Brands', consistent with other operational tables and to ensure tenant-specific data isolation.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in logistics operations, consistent with data hygiene across Mensa's systems.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    sales.sales_channel,\n    oms.courier_partner\nFROM\n    zs_observe.increff_sales AS sales\nINNER JOIN\n    zs_observe.shiprocket_oms AS oms\nON\n    sales.order_id = oms.order_id\nWHERE\n    sales.group_level_id = '22'\n    AND sales.is_active = true\n    AND sales.order_status = 'COMPLETED'\n    AND sales.transaction_type = 'SALES'\n    AND oms.group_level_id = '22'\n    AND oms.is_active = true\nORDER BY\n    sales.sales_channel, oms.courier_partner"
}

### GRAPH_COMPLETION

{
  "filters": [
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'",
    "oms.group_level_id = '22'",
    "oms.is_active = true"
  ],
  "joins": "INNER JOIN zs_observe.shiprocket_oms AS oms ON sales.order_id = oms.order_id",
  "metric_logic": {
    "aggregation_grain": "(sales_channel, courier_partner)",
    "deduplication_rule": "DISTINCT combination of sales_channel and courier_partner to show unique mappings.",
    "denominator": null,
    "formula": "List distinct pairs of (sales_channel, courier_partner)",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped queries. The presence of `order_id`, `courier_partner`, `group_level_id`, and `is_active` within `table.zs_observe.shiprocket_oms` is inferred based on its expected role as a logistics OMS and the need for tenant-level filtering and active record status.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is consistently used for Mensa's sales data, which contains the 'sales_channel' dimension and order identifiers. Its association with Mensa Brands (group_level_id = 22) is confirmed via account data bindings for other Mensa tables, implying its use for sales-related queries for Mensa.",
      "role": "Primary Source for Sales Channel",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "reason": "This table is a logical source for courier information, as 'Shiprocket' is a known logistics platform. The presence of 'courier_partner' is inferred from its role as an OMS in logistics query patterns (e.g., `query_pattern.logistics.amount_semantics_audit` where `courier_partner` is an allowed dimension). It is a direct fit for courier details.",
      "role": "Primary Source for Courier Partner",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales.sales_channel",
      "reason": "Required to identify the sales channel for the mapping report. This is inferred to be a column in `increff_sales` based on typical sales data structures and prior queries.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "oms.courier_partner",
      "reason": "Required to identify the courier partner for the mapping report. This column is inferred to exist in `shiprocket_oms` based on its role as a logistics OMS and relevant query patterns.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_id",
      "reason": "Inferred as the common key to join sales data with logistics OMS data, based on common data modeling practices for linking sales orders to their shipping details and prior inferences about operational relationship keys.",
      "role": "Join Key",
      "selected?": "Yes"
    },
    {
      "field": "oms.order_id",
      "reason": "Inferred as the common key to join logistics OMS data with sales data, reflecting a unique order identifier in the logistics system.",
      "role": "Join Key",
      "selected?": "Yes"
    },
    {
      "field": "sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "sales.is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) in Increff operations, ensuring only sales transactions are considered for channel mapping.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "oms.group_level_id",
      "reason": "Inferred to scope logistics data to 'Mensa Brands', consistent with other operational tables and to ensure tenant-specific data isolation.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in logistics operations, consistent with data hygiene across Mensa's systems.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    sales.sales_channel,\n    oms.courier_partner\nFROM\n    zs_observe.increff_sales AS sales\nINNER JOIN\n    zs_observe.shiprocket_oms AS oms\nON\n    sales.order_id = oms.order_id\nWHERE\n    sales.group_level_id = '22'\n    AND sales.is_active = true\n    AND sales.order_status = 'COMPLETED'\n    AND sales.transaction_type = 'SALES'\n    AND oms.group_level_id = '22'\n    AND oms.is_active = true\nORDER BY\n    sales.sales_channel, oms.courier_partner"
}
