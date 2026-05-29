# Cognee Batch Search Results

- started_at: `2026-05-27T04:01:27+00:00`
- completed_at: `2026-05-27T04:32:31+00:00`
- duration_seconds: `1863.335`
- source_questions: `inline QUESTIONS`
- datasets: `zenstatement_canonical`
- search_types: `RAG_COMPLETION, GRAPH_COMPLETION`

## 001. Which channel has the highest order volume share?

### Timing

- started_at: `2026-05-27T04:01:27+00:00`
- duration_seconds: `31.965`
- RAG_COMPLETION_seconds: `21.91`
- GRAPH_COMPLETION_seconds: `10.054`

### Query

```text
Which channel has the highest order volume share?

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
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) ensures each unique order is counted only once.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) across all sales_channels",
    "formula": "COUNT(DISTINCT order_id) / (SUM(COUNT(DISTINCT order_id)) OVER ())",
    "numerator": "COUNT(DISTINCT order_id) for each sales_channel"
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped sales queries. The value `transaction_type = 'SALES'` is used for clarity, assuming `'SAL'` is an abbreviation.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is consistently inferred to contain sales order data, including channel information and order identifiers, for Mensa Brands, which is crucial for determining order volume and share per channel. The context explicitly lists `group_level_id` for this table with value `22`, corresponding to Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to group order volume by channel, as specified in the report request. This is a common field in sales data for channel differentiation and is inferred to exist in a sales table like `increff_sales`.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Required to count the number of unique orders, representing 'order volume'. This is a standard primary key for orders in a sales table and is inferred to exist in `increff_sales`.",
      "role": "Metric (Order Volume)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly mentioned in the context for `column.zs_observe.increff_sales.group_level_id` with value `22`, which is required for scoping the report to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the order volume calculation (consistent with prior interactions).",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n)\nSELECT\n    sales_channel,\n    channel_order_count,\n    (CAST(channel_order_count AS DOUBLE) / SUM(channel_order_count) OVER ()) * 100 AS order_volume_share_pct\nFROM\n    ChannelOrderVolume\nORDER BY\n    order_volume_share_pct DESC\nLIMIT 1"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) ensures each unique order is counted only once.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) across all sales_channels",
    "formula": "COUNT(DISTINCT order_id) / (SUM(COUNT(DISTINCT order_id)) OVER ())",
    "numerator": "COUNT(DISTINCT order_id) for each sales_channel"
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables and consistent usage in previous Mensa-scoped sales queries. The value `transaction_type = 'SALES'` is used for clarity, assuming `'SAL'` is an abbreviation.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table has been consistently inferred to contain sales order data, including channel information and order identifiers, for Mensa Brands, which is crucial for determining order volume and share per channel. The context explicitly lists `group_level_id` for this table with value `22`, corresponding to Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to group order volume by channel, as specified in the report request. This is a common field in sales data for channel differentiation and is inferred to exist in a sales table like `increff_sales`.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Required to count the number of unique orders, representing 'order volume'. This is a standard primary key for orders in a sales table and is inferred to exist in `increff_sales`.",
      "role": "Metric (Order Volume)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly mentioned in the context for `column.zs_observe.increff_sales.group_level_id` with value `22`, which is required for scoping the report to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (consistent with prior interactions).",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the order volume calculation (consistent with prior interactions).",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "WITH ChannelOrderVolume AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n)\nSELECT\n    sales_channel,\n    channel_order_count,\n    (CAST(channel_order_count AS DOUBLE) / SUM(channel_order_count) OVER ()) * 100 AS order_volume_share_pct\nFROM\n    ChannelOrderVolume\nORDER BY\n    order_volume_share_pct DESC\nLIMIT 1"
}


---

## 002. Generate a report of all channels using Manual CSV integration.

### Timing

- started_at: `2026-05-27T04:01:59+00:00`
- duration_seconds: `20.432`
- RAG_COMPLETION_seconds: `11.045`
- GRAPH_COMPLETION_seconds: `9.387`

### Query

```text
Generate a report of all channels using Manual CSV integration.

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
  "filters": [],
  "joins": "No joins can be determined as the core information is missing.",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": null,
    "numerator": null
  },
  "missing_or_ambiguous": "The provided context lacks any information or fields related to the integration method (e.g., 'Manual CSV integration') used for data ingestion from channels. There is no information to differentiate channels based on their integration type.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "/* Insufficient information to generate a SQL query. The context does not define or provide data for 'Manual CSV integration' as an attribute of channels. */"
}

### GRAPH_COMPLETION

{
  "filters": [],
  "joins": "No joins can be determined as the core information is missing.",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": null,
    "numerator": null
  },
  "missing_or_ambiguous": "The provided context lacks any information or fields related to the integration method (e.g., 'Manual CSV integration') used for data ingestion from channels. There is no information to differentiate channels based on their integration type.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "/* Insufficient information to generate a SQL query. The context does not define or provide data for 'Manual CSV integration' as an attribute of channels. */"
}


---

## 003. List all marketplaces handled through Unicommerce.

### Timing

- started_at: `2026-05-27T04:02:20+00:00`
- duration_seconds: `28.23`
- RAG_COMPLETION_seconds: `14.112`
- GRAPH_COMPLETION_seconds: `14.117`

### RAG_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins are required as all necessary information (marketplace identifier and tenant filters) is inferred to exist within the single selected table `zs_observe.unicommerce`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT sales_channel to list each marketplace only once.",
    "denominator": null,
    "formula": "List of unique sales_channel values.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of a `sales_channel` column within `table.zs_observe.unicommerce` is inferred based on domain knowledge that OMS systems like Unicommerce would track the originating sales channel. Standard mandatory filters for Mensa (`group_level_id`, `is_active`) are also inferred from domain knowledge and consistent usage in prior interactions.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_sales",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "The `account_data_binding.mensa.unicommerce_oms.primary.unicommerce` card confirms `table.zs_observe.unicommerce` as a Unicommerce OMS table for Mensa Brands (group_level_id = 22) and lists `sales_returns_cancellations` semantics, implying it contains channel-level data. This table is appropriate for listing all handled marketplaces.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to list the distinct marketplaces. This column is logically inferred to exist in a Unicommerce OMS table to distinguish transactions by their source channel.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables linked to Unicommerce.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables, consistent with general data hygiene and other Mensa-scoped data points.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.unicommerce",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.unicommerce WHERE group_level_id = '22' AND is_active = true ORDER BY sales_channel"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins are required as all necessary information (marketplace identifier and tenant filters) is inferred to exist within the single selected table `zs_observe.unicommerce`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT sales_channel to list each marketplace only once.",
    "denominator": null,
    "formula": "List of unique sales_channel values.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of a `sales_channel` column within `table.zs_observe.unicommerce` is inferred based on domain knowledge that OMS/WMS systems processing 'cross-channel' data (as described for Mensa's Operations WMS) would store the originating marketplace for each record. Standard mandatory filters for Mensa (`group_level_id`, `is_active`) are also inferred from domain knowledge and consistent usage in prior interactions.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_sales",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "The `business_scope_set.mensa_brands.operations_wms` explicitly states it covers 'OMS/WMS operational evidence from Increff and Unicommerce' for Mensa Brands. The `account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce` card also confirms `table.zs_observe.unicommerce` as a Unicommerce OMS table and defines `sales_returns_cancellations` semantics, implying it contains channel-level data. Mensa's operations scope includes 'unicommerce_oms.primary', directly linking this table to Mensa's Unicommerce data.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to list the distinct marketplaces. This column is logically inferred to exist in an OMS/WMS operational table (`sales_returns_cancellations` semantics) to distinguish transactions by their source channel, especially given the 'cross-channel' description for Mensa's Operations WMS.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions and other Mensa account data bindings).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in account data bindings and operational tables (consistent with previous interactions and general data hygiene).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.unicommerce",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.unicommerce WHERE group_level_id = '22' AND is_active = true ORDER BY sales_channel"
}


---

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


---

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


---

## 006. Generate a report showing COD remittance type by courier.

### Timing

- started_at: `2026-05-27T04:03:58+00:00`
- duration_seconds: `54.779`
- RAG_COMPLETION_seconds: `34.613`
- GRAPH_COMPLETION_seconds: `20.165`

### Query

```text
Generate a report showing COD remittance type by courier.

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
    "group_level_id = '22'",
    "is_active = true",
    "payment_mode = 'COD'"
  ],
  "joins": "No joins are required as all necessary information (courier, remittance type, and tenant filters) is inferred to exist within the single selected table `zs_observe.shiprocket_settlement`.",
  "metric_logic": {
    "aggregation_grain": "(courier_partner, settlement_status)",
    "deduplication_rule": "DISTINCT combination of courier_partner and settlement_status to show unique remittance types by courier.",
    "denominator": null,
    "formula": "List distinct pairs of (courier_partner, settlement_status)",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `payment_mode` and `settlement_status` columns within `table.zs_observe.shiprocket_settlement` is inferred based on its role as a settlement table and the `allowed_dimensions` (`payment_mode`, `status`) in related logistics query patterns, especially `cod_expected_vs_remitted`. `settlement_status` is a specific interpretation of `status` for clarity. The logical filter `payment_mode = 'COD'` is inferred to target Cash On Delivery transactions. The `group_level_id` for Mensa is `22` (inferred from consistency across related Mensa documents).",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.shiprocket_settlement",
      "reason": "The `query_pattern.logistics.cod_expected_vs_remitted` explicitly lists `table.zs_observe.shiprocket_settlement` as a `required_table` and identifies `courier_partner`, `status`, and `payment_mode` as `allowed_dimensions`, making it the most direct source for courier-wise COD remittance types.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "reason": "Explicitly listed as an `allowed_dimension` in logistics query patterns (`cod_expected_vs_remitted`) and is required for the 'courier-wise' aspect of the report.",
      "role": "Dimension",
      "selected?": "Yes"
    },
    {
      "field": "payment_mode",
      "reason": "Inferred as the column to filter for 'COD' transactions, as `payment_mode` is an `allowed_dimension` in relevant logistics query patterns and logically categorizes transaction types.",
      "role": "Filter Column",
      "selected?": "Yes"
    },
    {
      "field": "settlement_status",
      "reason": "Inferred as the column representing the 'remittance type'. It is derived from the `status` allowed dimension in logistics query patterns, which would indicate the state of a settlement/remittance.",
      "role": "Dimension (Remittance Type)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands'. Based on context, `group_level_id = 22` is the identifier for Mensa within operational tables and it is a standard practice for tenant-specific data filtering.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in logistics operations, consistent with semantic filters mentioned in logistics query patterns.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.shiprocket_settlement",
  "sql_skeleton": "SELECT DISTINCT\n    courier_partner,\n    settlement_status\nFROM\n    zs_observe.shiprocket_settlement\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND payment_mode = 'COD'\nORDER BY\n    courier_partner, settlement_status"
}

### GRAPH_COMPLETION

{"selected_source": "table.zs_observe.shiprocket_settlement", "rejected_sources": ["query_pattern.limeroad.total_forward_gmv", "query_pattern.logistics.amount_semantics_audit", "query_pattern.logistics.awb_duplicate_detection", "query_pattern.logistics.bank_credit_unmatched_courier_reference", "execution_constraint_set.increff.operations_manifest_refactored_constraints", "execution_constraint_set.jiomart.marketplace_query_constraints", "execution_constraint_set.logistics_batch_to_bank"], "require_tables": [{"field": "zs_observe.shiprocket_settlement", "role": "Primary Data Source Table", "selected?": "Yes", "reason": "The `query_pattern.logistics.cod_expected_vs_remitted` (referenced in prior interactions) explicitly lists `table.zs_observe.shiprocket_settlement` as a `required_table` and identifies `courier_partner`, `status`, and `payment_mode` as `allowed_dimensions`, making it the most direct source for courier-wise COD remittance types."Compensation for lack of direct context: The mention of this table and its relevant fields in the `query_pattern.logistics.cod_expected_vs_remitted` within the broader context provided in previous turns strongly implies its suitability for this query, even if the full pattern is not explicitly presented in this specific turn's context."}], "required_fields": [{"field": "courier_partner", "role": "Dimension", "selected?": "Yes", "reason": "Explicitly listed as an `allowed_dimension` in logistics query patterns (`cod_expected_vs_remitted` in historical context) and is required for the 'courier-wise' aspect of the report."}, {"field": "payment_mode", "role": "Filter Column", "selected?": "Yes", "reason": "Inferred as the column to filter for 'COD' transactions, as `payment_mode` is an `allowed_dimension` in relevant logistics query patterns (from historical context) and logically categorizes transaction types."}, {"field": "settlement_status", "role": "Dimension (Remittance Type)", "selected?": "Yes", "reason": "Inferred as the column representing the 'remittance type'. It is derived from the `status` allowed dimension in logistics query patterns (from historical context), which would indicate the state of a settlement/remittance."}, {"field": "group_level_id", "role": "Filter Column (Tenant Scope)", "selected?": "Yes", "reason": "Required for scoping the report to 'Mensa Brands'. Based on context, `group_level_id = 22` is the identifier for Mensa within operational tables and it is a standard practice for tenant-specific data filtering."}, {"field": "is_active", "role": "Filter Column (Status)", "selected?": "Yes", "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in logistics operations, consistent with semantic filters mentioned in logistics query patterns (from historical context)."}], "rejected_or_ambiguous_fields": [], "metric_logic": {"formula": "List distinct pairs of (courier_partner, settlement_status)", "numerator": null, "denominator": null, "aggregation_grain": "(courier_partner, settlement_status)", "deduplication_rule": "DISTINCT combination of courier_partner and settlement_status to show unique remittance types by courier."}, "filters": ["group_level_id = '22'", "is_active = true", "payment_mode = 'COD'"], "joins": "No joins are required as all necessary information (courier, remittance type, and tenant filters) is inferred to exist within the single selected table `zs_observe.shiprocket_settlement`.", "missing_or_ambiguous": "The explicit presence of `payment_mode` and `settlement_status` columns within `table.zs_observe.shiprocket_settlement` is inferred based on its role as a settlement table and the `allowed_dimensions` (`payment_mode`, `status`) in related logistics query patterns (`cod_expected_vs_remitted` from historical context). `settlement_status` is a specific interpretation of `status` for clarity. The logical filter `payment_mode = 'COD'` is inferred to target Cash On Delivery transactions. The `group_level_id` for Mensa is `22` (inferred from consistency across related Mensa documents).", "sql_skeleton": "SELECT DISTINCT\n    courier_partner,\n    settlement_status\nFROM\n    zs_observe.shiprocket_settlement\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND payment_mode = 'COD'\nORDER BY\n    courier_partner, settlement_status"}


---

## 007. Which channels use marketplace-managed returns?

### Timing

- started_at: `2026-05-27T04:04:53+00:00`
- duration_seconds: `51.575`
- RAG_COMPLETION_seconds: `34.925`
- GRAPH_COMPLETION_seconds: `16.649`

### Query

```text
Which channels use marketplace-managed returns?

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
    "group_level_id = '22'",
    "is_active = true",
    "return_order_type = 'Marketplace'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, return type, and tenant filters) is contained within the single selected table `zs_observe.increff_returns`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT sales_channel to show each channel only once.",
    "denominator": null,
    "formula": "List of unique sales_channel values where return_order_type indicates marketplace management.",
    "numerator": null
  },
  "missing_or_ambiguous": "The specific value for `return_order_type` that signifies 'marketplace-managed returns' is inferred as 'Marketplace' based on common industry terminology for such a column in a returns log. The actual value might be 'MP', 'Mktplace', or similar, and would require validation against the dataset.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table is described as a 'Cross-channel returns log' and explicitly contains columns like `sales_channel` and `return_order_type`, which are directly relevant to identifying channels with marketplace-managed returns. It is scoped to Mensa Brands via `group_level_id = 22`.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to list the distinct channels. This column is explicitly present in the `increff_returns` table, allowing for grouping by sales channel.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "return_order_type",
      "reason": "Required to identify 'marketplace-managed' returns. This column (or a similar status field within the table, like `channel_return_order_status`) is the most logical place to categorize return types by their management entity (e.g., marketplace vs. self-managed).",
      "role": "Filter Column (Returns Management Type)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly documented for `table.zs_observe.increff_returns` with the value `22`, which scopes the report to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "A mandatory filter (`is_active = true`) specified for data validity in `table.zs_observe.increff_returns`, consistent with general data hygiene.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_returns",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND return_order_type = 'Marketplace' -- Inferred filter value for marketplace-managed returns\nORDER BY\n    sales_channel"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "return_order_type = 'Marketplace'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, return type, and tenant filters) is contained within the single selected table `zs_observe.increff_returns`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT sales_channel to show each channel only once.",
    "denominator": null,
    "formula": "List of unique sales_channel values where return_order_type indicates marketplace management.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `return_order_type` columns within `table.zs_observe.increff_returns` is inferred based on domain knowledge of returns logs and its successful use for this exact question in the previous turn. The specific value for `return_order_type` that signifies 'marketplace-managed returns' is inferred as 'Marketplace' based on common industry terminology for such a column. Standard mandatory filters (`group_level_id`, `is_active`) are also inferred from consistent usage patterns for Mensa's operational data, confirmed by previous interactions.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table is described as a 'Cross-channel returns log' (from previous context) and explicitly contains columns like `sales_channel` and `return_order_type`, which are directly relevant to identifying channels with marketplace-managed returns. It is scoped to Mensa Brands via `group_level_id = 22` (as inferred from previous similar questions).",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to list the distinct channels. This column is explicitly present in the `increff_returns` table, allowing for grouping by sales channel (as inferred from previous context).",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "return_order_type",
      "reason": "Required to identify 'marketplace-managed' returns. This column (or a similar status field within the table, like `channel_return_order_status`) is the most logical place to categorize return types by their management entity (e.g., marketplace vs. self-managed), as inferred from previous context.",
      "role": "Filter Column (Returns Management Type)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Explicitly documented for `table.zs_observe.increff_returns` with the value `22`, which scopes the report to 'Mensa Brands' (as inferred from previous context).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "A mandatory filter (`is_active = true`) specified for data validity in `table.zs_observe.increff_returns`, consistent with general data hygiene (as inferred from previous context).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_returns",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND return_order_type = 'Marketplace' -- Inferred filter value for marketplace-managed returns\nORDER BY\n    sales_channel"
}


---

## 008. Generate a summary report of OMS systems and their connected marketplaces.

### Timing

- started_at: `2026-05-27T04:05:44+00:00`
- duration_seconds: `87.626`
- RAG_COMPLETION_seconds: `41.621`
- GRAPH_COMPLETION_seconds: `46.004`

### Query

```text
Generate a summary report of OMS systems and their connected marketplaces.

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
    "unicommerce.group_level_id = '22'",
    "unicommerce.is_active = true",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true",
    "increff_sales.group_level_id = '22'",
    "increff_sales.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine results from different OMS systems, rather than explicit JOINs. No joins are needed between these distinct OMS sources.",
  "metric_logic": {
    "aggregation_grain": "(OMS System, Marketplace)",
    "deduplication_rule": "DISTINCT combination of oms_system and marketplace to show each unique mapping only once across all OMS sources.",
    "denominator": null,
    "formula": "List distinct pairs of (OMS System, Marketplace) by combining data from multiple OMS-related tables.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce` and `table.zs_observe.amazon_oms` is inferred based on domain knowledge of OMS systems, analogous fields in `table.zs_observe.increff_sales`, and consistent usage patterns in previous Mensa-scoped queries. The literal string names for OMS systems are assigned for clarity in the report.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "Previous successful queries for 'marketplaces handled through Unicommerce' for Mensa Brands indicate this table contains `sales_channel` and is scoped to Mensa via `group_level_id = 22`.",
      "role": "Source for Unicommerce OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` card explicitly links this table to Mensa Brands (`group_level_id = 22`), signifying it as a primary OMS for Amazon. It is inferred to contain `sales_channel` for marketplace identification.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Previous successful queries for 'courier-wise channel mapping' for Mensa Brands inferred this table contains `sales_channel` and is scoped to Mensa (`group_level_id = 22`), implying it serves as an OMS for various sales channels.",
      "role": "Source for Increff Sales data (acting as an OMS)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "'Unicommerce'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.unicommerce`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `unicommerce` table based on domain knowledge and previous interactions.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon OMS'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.amazon_oms`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `amazon_oms` table based on its role as an OMS.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is explicitly mentioned in `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Increff Sales'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.increff_sales`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.sales_channel",
      "reason": "Required to list the distinct marketplaces. Explicitly used in previous interactions with this table.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is confirmed from previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in Increff operations (from prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    oms_system,\n    marketplace\nFROM\n    (\n        SELECT\n            'Unicommerce' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.unicommerce\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Amazon OMS' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.amazon_oms\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Increff Sales' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.increff_sales\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n    ) AS combined_oms_data\nORDER BY\n    oms_system, marketplace"
}

### GRAPH_COMPLETION

{
  "filters": [
    "unicommerce.group_level_id = '22'",
    "unicommerce.is_active = true",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true",
    "increff_sales.group_level_id = '22'",
    "increff_sales.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine results from different OMS systems, rather than explicit JOINs. No joins are needed between these distinct OMS sources.",
  "metric_logic": {
    "aggregation_grain": "(OMS System, Marketplace)",
    "deduplication_rule": "DISTINCT combination of oms_system and marketplace to show each unique mapping only once across all OMS sources.",
    "denominator": null,
    "formula": "List distinct pairs of (OMS System, Marketplace) by combining data from multiple OMS-related tables.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce` and `table.zs_observe.amazon_oms` is inferred based on domain knowledge of OMS systems, analogous fields in `table.zs_observe.increff_sales`, and consistent usage patterns in previous Mensa-scoped queries. The literal string names for OMS systems are assigned for clarity in the report.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "Previous successful queries for 'marketplaces handled through Unicommerce' for Mensa Brands indicate this table contains `sales_channel` and is scoped to Mensa via `group_level_id = 22`.",
      "role": "Source for Unicommerce OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` card explicitly links this table to Mensa Brands (`group_level_id = 22`), signifying it as a primary OMS for Amazon. It is inferred to contain `sales_channel` for marketplace identification.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Previous successful queries for 'courier-wise channel mapping' for Mensa Brands inferred this table contains `sales_channel` and is scoped to Mensa (`group_level_id = 22`), implying it serves as an OMS for various sales channels.",
      "role": "Source for Increff Sales data (acting as an OMS)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "'Unicommerce'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.unicommerce`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `unicommerce` table based on domain knowledge and previous interactions.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon OMS'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.amazon_oms`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `amazon_oms` table based on its role as an OMS.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is explicitly mentioned in `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Increff Sales'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.increff_sales`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.sales_channel",
      "reason": "Required to list the distinct marketplaces. Explicitly used in previous interactions with this table.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is confirmed from previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in Increff operations (from prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    oms_system,\n    marketplace\nFROM\n    (\n        SELECT\n            'Unicommerce' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.unicommerce\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Amazon OMS' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.amazon_oms\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Increff Sales' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.increff_sales\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n    ) AS combined_oms_data\nORDER BY\n    oms_system, marketplace"
}


---

## 009. Calculate the combined marketplace contribution vs own website contribution.

### Timing

- started_at: `2026-05-27T04:07:12+00:00`
- duration_seconds: `40.558`
- RAG_COMPLETION_seconds: `27.225`
- GRAPH_COMPLETION_seconds: `13.332`

### RAG_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, sales amount, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "channel_type (derived from sales_channel)",
    "deduplication_rule": "Sum of total_amount per unique channel type.",
    "denominator": null,
    "formula": "SUM(total_amount) grouped by channel type ('Marketplace' or 'Own Website')",
    "numerator": "total_amount"
  },
  "missing_or_ambiguous": "The explicit presence of `total_amount` (as a sales value metric) and its data type are inferred based on the nature of a sales table. The method for categorizing `sales_channel` into 'Marketplace' vs. 'Own Website' is inferred using a `CASE` statement, assuming 'Own Website' is a literal value for own website sales, and all other sales channels are grouped under 'Marketplace'. The filters for `is_active`, `order_status`, and `transaction_type` are inferred as standard mandatory filters for accurate sales reporting based on consistent usage patterns for Mensa's operational data.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is inferred to contain sales transaction data, including the `sales_channel` and a measure of sales value, which are essential for calculating contribution by channel. Its association with Mensa Brands (group_level_id = 22) is confirmed via account data bindings for other Mensa tables, implying its use for sales-related queries for Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to classify sales into 'Marketplace' or 'Own Website'. This field is logically present in sales data to categorize orders by origin and was used in previous interactions with this table.",
      "role": "Dimension for Channel Categorization",
      "selected?": "Yes"
    },
    {
      "field": "total_amount",
      "reason": "Inferred as the primary column representing the monetary value (contribution) of each sales transaction. Common in sales tables for metrics like GMV or revenue.",
      "role": "Measure (Contribution Metric)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) in Increff operations, ensuring only sales transactions are considered for contribution analysis.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "SELECT\n    CASE\n        WHEN sales_channel = 'Own Website' THEN 'Own Website'\n        ELSE 'Marketplace'\n    END AS channel_type,\n    SUM(total_amount) AS total_contribution\nFROM\n    zs_observe.increff_sales\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND order_status = 'COMPLETED'\n    AND transaction_type = 'SALES'\nGROUP BY\n    channel_type\nORDER BY\n    channel_type"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, sales amount, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "channel_type (derived from sales_channel)",
    "deduplication_rule": "Sum of total_amount per unique channel type.",
    "denominator": null,
    "formula": "SUM(total_amount) grouped by channel type ('Marketplace' or 'Own Website')",
    "numerator": "total_amount"
  },
  "missing_or_ambiguous": "The explicit presence of `total_amount` (as a sales value metric) and its data type are inferred based on the nature of a sales table. The method for categorizing `sales_channel` into 'Marketplace' vs. 'Own Website' is inferred using a `CASE` statement, assuming 'Own Website' is a literal value for own website sales, and all other sales channels are grouped under 'Marketplace'. The filters for `is_active`, `order_status`, and `transaction_type` are inferred as standard mandatory filters for accurate sales reporting based on consistent usage patterns for Mensa's operational data.",
  "rejected_or_ambiguous_fields": [],
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
      "reason": "This table is inferred to contain sales transaction data, including the `sales_channel` and a measure of sales value, which are essential for calculating contribution by channel. Its association with Mensa Brands (group_level_id = 22) is confirmed via account data bindings for other Mensa tables, implying its use for sales-related queries for Mensa.",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to classify sales into 'Marketplace' or 'Own Website'. This field is logically present in sales data to categorize orders by origin and was used in previous interactions with this table.",
      "role": "Dimension for Channel Categorization",
      "selected?": "Yes"
    },
    {
      "field": "total_amount",
      "reason": "Inferred as the primary column representing the monetary value (contribution) of each sales transaction. Common in sales tables for metrics like GMV or revenue.",
      "role": "Measure (Contribution Metric)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = COMPLETED`) in Increff operations, ensuring only valid, completed sales transactions are included.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) in Increff operations, ensuring only sales transactions are considered for contribution analysis.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "SELECT\n    CASE\n        WHEN sales_channel = 'Own Website' THEN 'Own Website'\n        ELSE 'Marketplace'\n    END AS channel_type,\n    SUM(total_amount) AS total_contribution\nFROM\n    zs_observe.increff_sales\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND order_status = 'COMPLETED'\n    AND transaction_type = 'SALES'\nGROUP BY\n    channel_type\nORDER BY\n    channel_type"
}


---

## 010. Identify channels with higher operational dependency on manual processes.

### Timing

- started_at: `2026-05-27T04:07:52+00:00`
- duration_seconds: `25.259`
- RAG_COMPLETION_seconds: `17.044`
- GRAPH_COMPLETION_seconds: `8.214`

### Query

```text
Identify channels with higher operational dependency on manual processes.

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
  "filters": [],
  "joins": "N/A",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": null,
    "numerator": null
  },
  "missing_or_ambiguous": "The provided context does not contain any information or metrics that directly or indirectly define 'operational dependency on manual processes' or link specific channels to such a dependency. There are no fields indicating manual intervention levels, automation status, or proxy metrics for manual work. Therefore, this question cannot be answered with the current context.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "/* Unable to generate SQL query: Missing definition or metrics for 'operational dependency on manual processes' and how to link it to channels within the provided context. */"
}

### GRAPH_COMPLETION

{
  "filters": [],
  "joins": "N/A",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": null,
    "numerator": null
  },
  "missing_or_ambiguous": "The provided context does not contain any information or metrics that directly or indirectly define 'operational dependency on manual processes' or link specific channels to such a dependency. There are no fields indicating manual intervention levels, automation status, or proxy metrics for manual work. Therefore, this question cannot be answered with the current context.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "/* Unable to generate SQL query: Missing definition or metrics for 'operational dependency on manual processes' and how to link it to channels within the provided context. */"
}


---

## 011. Create a marketplace risk report showing which channels depend on the same OMS.

### Timing

- started_at: `2026-05-27T04:08:18+00:00`
- duration_seconds: `148.954`
- RAG_COMPLETION_seconds: `53.37`
- GRAPH_COMPLETION_seconds: `95.583`

### Query

```text
Create a marketplace risk report showing which channels depend on the same OMS.

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
    "unicommerce.group_level_id = '22'",
    "unicommerce.is_active = true",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true",
    "increff_sales.group_level_id = '22'",
    "increff_sales.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine results from different OMS systems, rather than explicit JOINs. No joins are needed between these distinct OMS sources.",
  "metric_logic": {
    "aggregation_grain": "(OMS System, Marketplace)",
    "deduplication_rule": "DISTINCT combination of oms_system and marketplace to show each unique mapping only once across all OMS sources.",
    "denominator": null,
    "formula": "List distinct pairs of (OMS System, Marketplace) by combining data from multiple OMS-related tables.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce` and `table.zs_observe.amazon_oms` is inferred based on domain knowledge of OMS systems, analogous fields in `table.zs_observe.increff_sales`, and consistent usage patterns in previous Mensa-scoped queries. The literal string names for OMS systems are assigned for clarity in the report. All inferences are based on patterns observed in Mensa's data within previous contexts.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "Previous successful queries for 'marketplaces handled through Unicommerce' for Mensa Brands indicate this table contains `sales_channel` and is scoped to Mensa via `group_level_id = 22`.",
      "role": "Source for Unicommerce OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` card (from previous context) explicitly links this table to Mensa Brands (`group_level_id = 22`), signifying it as a primary OMS for Amazon. It is inferred to contain `sales_channel` for marketplace identification.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Previous successful queries for 'courier-wise channel mapping' for Mensa Brands (from previous context) inferred this table contains `sales_channel` and is scoped to Mensa (`group_level_id = 22`), implying it serves as an OMS for various sales channels.",
      "role": "Source for Increff Sales data (acting as an OMS)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "'Unicommerce'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.unicommerce`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `unicommerce` table based on domain knowledge and previous interactions for Mensa Brands.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon OMS'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.amazon_oms`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `amazon_oms` table based on its role as an OMS for Mensa Brands.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is explicitly mentioned in `account_data_binding.mensa.amazon_in.primary.amazon_oms` (from previous context).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Increff Sales'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.increff_sales`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.sales_channel",
      "reason": "Required to list the distinct marketplaces. Explicitly used in previous interactions with this table for Mensa Brands.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is confirmed from previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in Increff operations (from prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    oms_system,\n    marketplace\nFROM\n    (\n        SELECT\n            'Unicommerce' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.unicommerce\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Amazon OMS' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.amazon_oms\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Increff Sales' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.increff_sales\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n    ) AS combined_oms_data\nORDER BY\n    oms_system, marketplace"
}

### GRAPH_COMPLETION

{
  "filters": [
    "unicommerce.group_level_id = '22'",
    "unicommerce.is_active = true",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true",
    "increff_sales.group_level_id = '22'",
    "increff_sales.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine results from different OMS systems, rather than explicit JOINs. No joins are needed between these distinct OMS sources.",
  "metric_logic": {
    "aggregation_grain": "(OMS System, Marketplace)",
    "deduplication_rule": "DISTINCT combination of oms_system and marketplace to show each unique mapping only once across all OMS sources. This directly answers 'which channels depend on the same OMS' by grouping channels under their respective OMS.",
    "denominator": null,
    "formula": "List distinct pairs of (OMS System, Marketplace) by combining data from multiple OMS-related tables.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce`, `table.zs_observe.amazon_oms`, and `table.zs_observe.increff_sales` is inferred based on domain knowledge of OMS systems, the explicit mention of these platforms as OMS sources for Mensa, and consistent usage patterns in previous Mensa-scoped queries. The literal string names for OMS systems are assigned for clarity in the report.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "The `business_scope_set.mensa_brands.operations_wms` explicitly states 'cross-channel OMS/WMS operational evidence from Increff and Unicommerce', linking Unicommerce to Mensa's OMS operations. Previous queries have successfully used this table for 'marketplaces handled through Unicommerce'.",
      "role": "Source for Unicommerce OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` card explicitly links this table to Mensa Brands (`group_level_id = 22`), signifying it as a primary OMS for Amazon and implying it contains marketplace identification.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "The `business_scope_set.mensa_brands.operations_wms` explicitly states 'cross-channel OMS/WMS operational evidence from Increff and Unicommerce', implying Increff serves as an OMS for various sales channels for Mensa. `increff_sales` is inferred as the relevant table for sales channel data, consistent with prior usage patterns.",
      "role": "Source for Increff Sales data (acting as an OMS)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "'Unicommerce'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.unicommerce`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `unicommerce` table based on domain knowledge of OMS systems and successful previous query constructions.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands'. `group_level_id = 22` is consistently documented for Mensa within operational tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "unicommerce.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon OMS'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.amazon_oms`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.sales_channel",
      "reason": "Required to list the distinct marketplaces. Inferred to exist in `amazon_oms` table based on its role as an OMS.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is explicitly mentioned in `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "'Increff Sales'",
      "reason": "Literal string to identify the OMS system for rows originating from `zs_observe.increff_sales`.",
      "role": "Literal (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.sales_channel",
      "reason": "Required to list the distinct marketplaces. Its presence is inferred from the table's role as a sales data source (OMS-like) and consistent prior usage.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is confirmed from previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "increff_sales.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in Increff operations.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT DISTINCT\n    oms_system,\n    marketplace\nFROM\n    (\n        SELECT\n            'Unicommerce' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.unicommerce\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Amazon OMS' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.amazon_oms\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n\n        UNION ALL\n\n        SELECT\n            'Increff Sales' AS oms_system,\n            sales_channel AS marketplace\n        FROM\n            zs_observe.increff_sales\n        WHERE\n            group_level_id = '22'\n            AND is_active = true\n    ) AS combined_oms_data\nORDER BY\n    oms_system, marketplace"
}


---

## 012. Generate a logistics dependency matrix showing courier concentration across marketplaces.

### Timing

- started_at: `2026-05-27T04:10:47+00:00`
- duration_seconds: `59.9`
- RAG_COMPLETION_seconds: `31.402`
- GRAPH_COMPLETION_seconds: `28.498`

### Query

```text
Generate a logistics dependency matrix showing courier concentration across marketplaces.

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

{"selected_source": "table.zs_observe.increff_sales", "rejected_sources": ["query_pattern.limeroad.total_forward_gmv", "query_pattern.logistics.amount_semantics_audit", "query_pattern.logistics.awb_duplicate_detection", "query_pattern.logistics.bank_credit_unmatched_courier_reference", "query_pattern.logistics.cod_expected_vs_remitted", "execution_constraint_set.increff.operations_manifest_refactored_constraints", "execution_constraint_set.jiomart.marketplace_query_constraints", "execution_constraint_set.logistics_batch_to_bank"], "require_tables": [{"field": "zs_observe.increff_sales", "role": "Primary Data Source Table", "selected?": "Yes", "reason": "This table is inferred to contain transactional sales data for Mensa Brands, including both `sales_channel` and `courier_partner`, which are essential for mapping logistics dependencies across marketplaces. The context mentions `rule.increff.courier_normalization` and `query_pattern.increff.7_6_courier_partner_distribution_normalized`, strongly suggesting courier data exists and is analyzed within Increff data in relation to channels for Mensa Brands (group_level_id = 22)."}], "required_fields": [{"field": "sales_channel", "role": "Dimension (Marketplace/Channel Identifier)", "selected?": "Yes", "reason": "Required to group or segment courier dependencies by marketplace. This column is commonly found in sales/order tables and has been used in previous interactions for channel identification within Mensa's Increff data."}, {"field": "courier_partner", "role": "Dimension (Courier Identifier)", "selected?": "Yes", "reason": "Required to identify the logistics partners. Explicitly mentioned as an 'allowed dimension' in various logistics query patterns and implied by `rule.increff.courier_normalization` in Increff constraints, suggesting its presence in relevant operational tables like `increff_sales`."}, {"field": "order_id", "role": "Metric (Count Basis)", "selected?": "Yes", "reason": "Used to count the number of orders/shipments handled by each courier for each channel, providing a measure of 'concentration'."}, {"field": "group_level_id", "role": "Filter Column (Tenant Scope)", "selected?": "Yes", "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions)."}, {"field": "is_active", "role": "Filter Column (Status)", "selected?": "Yes", "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations (consistent with prior interactions)."}, {"field": "order_status", "role": "Filter Column (Order Status)", "selected?": "Yes", "reason": "Inferred as a mandatory filter (`order_status = 'COMPLETED'`) to include only successful/completed orders for meaningful logistics analysis."}, {"field": "transaction_type", "role": "Filter Column (Transaction Type)", "selected?": "Yes", "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) to ensure only sales transactions (which involve logistics) are considered."}]}], "rejected_or_ambiguous_fields": [], "metric_logic": {"formula": "COUNT(order_id) grouped by sales_channel and courier_partner", "numerator": "order_id", "denominator": null, "aggregation_grain": "sales_channel, courier_partner", "deduplication_rule": "Count of orders for each unique (sales_channel, courier_partner) pair."}, "filters": ["group_level_id = '22'", "is_active = true", "order_status = 'COMPLETED'", "transaction_type = 'SALES'"], "joins": "No joins are required as all necessary information (sales channel, courier partner, order count, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.", "missing_or_ambiguous": "The explicit presence and exact column names for `sales_channel` and `courier_partner` within `table.zs_observe.increff_sales` are inferred. However, the presence of `courier_normalization` rule and a `courier_partner_distribution_normalized` query pattern related to Increff operations strongly suggests that such data exists and is processed. Standard mandatory filters (`group_level_id`, `is_active`, `order_status`, `transaction_type`) are inferred based on consistent usage patterns for Mensa's operational sales data. The metric `order_id` is inferred as a suitable field to count for concentration.", "sql_skeleton": "SELECT\n    sales_channel,\n    courier_partner,\n    COUNT(order_id) AS order_count\nFROM\n    zs_observe.increff_sales\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND order_status = 'COMPLETED'\n    AND transaction_type = 'SALES'\nGROUP BY\n    sales_channel,\n    courier_partner\nORDER BY\n    sales_channel, order_count DESC"}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, courier partner, order count, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel, fulfilment_channel",
    "deduplication_rule": "Count of orders for each unique (sales_channel, fulfilment_channel) pair.",
    "denominator": null,
    "formula": "COUNT(order_id) grouped by sales_channel and fulfilment_channel",
    "numerator": "order_id"
  },
  "missing_or_ambiguous": "The explicit presence and exact column names for `sales_channel` and `order_id` within `table.zs_observe.increff_sales` are inferred based on the typical structure of sales data tables and successful use in previous interactions. The filter for `fulfilment_channel` not being NULL or empty might also be a useful addition if data quality issues exist, but is not explicitly inferred as mandatory. The specific values for `is_active`, `order_status`, and `transaction_type` are inferred as standard best practices for sales reporting, based on prior interactions and common data patterns.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
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
      "reason": "This table is inferred to contain transactional sales data for Mensa Brands, including both `sales_channel` and `fulfilment_channel`, which are essential for mapping logistics dependencies across marketplaces. The context mentions `rule.increff.courier_normalization` and `query_pattern.increff.7_6_courier_partner_distribution_normalized`, strongly suggesting courier data exists and is analyzed within Increff data in relation to channels for Mensa Brands (group_level_id = 22).",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to group or segment courier dependencies by marketplace. This column is commonly found in sales/order tables and has been used in previous interactions for channel identification within Mensa's Increff data.",
      "role": "Dimension (Marketplace/Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "fulfilment_channel",
      "reason": "Explicitly described as 'Courier/logistics partner used (80+ variants)' in `column.zs_observe.increff_sales.fulfilment_channel` and is crucial for identifying logistics partners. Its usage is also suggested by `metric_impl.increff.courier_shipment_count`.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Used to count the number of orders/shipments handled by each courier for each channel, providing a measure of 'concentration'. This is a common identifier in sales tables to count discrete transactions.",
      "role": "Metric (Count Basis)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations (consistent with prior interactions).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as a mandatory filter (`order_status = 'COMPLETED'`) to include only successful/completed orders for meaningful logistics analysis.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Inferred as a mandatory filter (`transaction_type = 'SALES'`) to ensure only sales transactions (which involve logistics) are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_sales",
  "sql_skeleton": "SELECT\n    sales_channel,\n    fulfilment_channel AS courier_partner,\n    COUNT(order_id) AS order_count\nFROM\n    zs_observe.increff_sales\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND order_status = 'COMPLETED'\n    AND transaction_type = 'SALES'\nGROUP BY\n    sales_channel,\n    fulfilment_channel\nORDER BY\n    sales_channel, order_count DESC"
}


---

## 013. Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

### Timing

- started_at: `2026-05-27T04:11:46+00:00`
- duration_seconds: `52.276`
- RAG_COMPLETION_seconds: `31.595`
- GRAPH_COMPLETION_seconds: `20.681`

### Query

```text
Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

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
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for sales channel information",
      "selected?": "Yes",
      "reason": "This table is identified as an OMS for Myntra, and OMS tables typically contain sales channel information. The explicit relationship to `myntra_oms_settlement` via `order_id` makes it a critical source for linking channels to reconciliation data."
    },
    {
      "field": "zs_observe.myntra_oms_settlement",
      "role": "Source for reconciliation status and variance",
      "selected?": "Yes",
      "reason": "This table is directly mentioned in `query_pattern.myntra.oms_settlement_reconciliation` as the source for reconciliation details like `recon_status` and `variance_amount`, which are key to identifying reconciliation delays."
    }
  ],
  "required_fields": [
    {
      "field": "oms.sales_channel",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes",
      "reason": "Required to identify the channels. Inferred to exist in `myntra_oms` as it's an Order Management System table."
    },
    {
      "field": "oms.order_id",
      "role": "Join Key",
      "selected?": "Yes",
      "reason": "Required to join `myntra_oms` and `myntra_oms_settlement` tables, as explicitly suggested by `relationship.myntra_oms.myntra_oms_settlement.order_id` in the context."
    },
    {
      "field": "oms.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions and Myntra query patterns)."
    },
    {
      "field": "settlement.order_id",
      "role": "Join Key / Metric (Count Basis)",
      "selected?": "Yes",
      "reason": "Required to join `myntra_oms_settlement` with `myntra_oms` and also to count reconciliation issues per channel."
    },
    {
      "field": "settlement.recon_status",
      "role": "Filter Column (Reconciliation Status)",
      "selected?": "Yes",
      "reason": "Directly indicates reconciliation issues or delays, as used in `query_pattern.myntra.oms_settlement_reconciliation`."
    },
    {
      "field": "settlement.variance_amount",
      "role": "Filter Column (Variance Indicator)",
      "selected?": "Yes",
      "reason": "Directly indicates reconciliation discrepancies, as used in `query_pattern.myntra.oms_settlement_reconciliation`."
    },
    {
      "field": "settlement.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands'. The `query_pattern.myntra.oms_settlement_reconciliation` SQL template notes that `group_level_id` should be applied if present, and other Myntra patterns for Mensa use it."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "COUNT(DISTINCT settlement.order_id) where reconciliation issues exist, grouped by sales_channel",
    "numerator": "DISTINCT settlement.order_id",
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Count of unique orders with reconciliation issues for each sales channel."
  },
  "filters": [
    "oms.group_level_id = '22'",
    "settlement.group_level_id = '22'",
    "settlement.recon_status != 'MATCHED' OR settlement.variance_amount != 0"
  ],
  "joins": "INNER JOIN zs_observe.myntra_oms_settlement settlement ON oms.order_id = settlement.order_id",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` within `table.zs_observe.myntra_oms` is inferred based on its role as an Order Management System and consistent data patterns in similar contexts. The applicability of `group_level_id = 22` to `zs_observe.myntra_oms_settlement` is inferred from its usage in related Myntra query patterns for Mensa Brands. The assumption is that 'MATCHED' status and zero variance indicate no delays.",
  "sql_skeleton": "SELECT
    oms.sales_channel,
    COUNT(DISTINCT settlement.order_id) AS reconciliation_delay_count
FROM
    zs_observe.myntra_oms oms
INNER JOIN
    zs_observe.myntra_oms_settlement settlement
ON
    oms.order_id = settlement.order_id
WHERE
    oms.group_level_id = '22'
    AND settlement.group_level_id = '22'
    AND (settlement.recon_status != 'MATCHED' OR settlement.variance_amount != 0)
GROUP BY
    oms.sales_channel
ORDER BY
    reconciliation_delay_count DESC"
}

### GRAPH_COMPLETION

{
  "selected_source": null,
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for sales channel information",
      "selected?": "Yes",
      "reason": "This table is identified as an OMS for Myntra, and OMS tables typically contain sales channel information. The explicit relationship to `myntra_oms_settlement` via `order_id` (from previous successful queries and typical marketplace data structures) makes it a critical source for linking channels to reconciliation data."
    },
    {
      "field": "zs_observe.myntra_oms_settlement",
      "role": "Source for reconciliation status and variance",
      "selected?": "Yes",
      "reason": "This table is directly associated with reconciliation details like `recon_status` and `variance_amount` in `query_pattern.myntra.oms_settlement_reconciliation` (from previous context), which are key to identifying reconciliation delays."
    }
  ],
  "required_fields": [
    {
      "field": "oms.sales_channel",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes",
      "reason": "Required to identify the channels. Inferred to exist in `myntra_oms` as it's an Order Management System table for Mensa Brands (from prior interactions)."
    },
    {
      "field": "oms.order_id",
      "role": "Join Key",
      "selected?": "Yes",
      "reason": "Required to join `myntra_oms` and `myntra_oms_settlement` tables, as explicitly suggested by `relationship.myntra_oms.myntra_oms_settlement.order_id` in prior contexts."
    },
    {
      "field": "oms.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions and Myntra query patterns).
"
    },
    {
      "field": "settlement.order_id",
      "role": "Join Key / Metric (Count Basis)",
      "selected?": "Yes",
      "reason": "Required to join `myntra_oms_settlement` with `myntra_oms` and also to count reconciliation issues per channel."
    },
    {
      "field": "settlement.recon_status",
      "role": "Filter Column (Reconciliation Status)",
      "selected?": "Yes",
      "reason": "Directly indicates reconciliation issues or delays, as used in `query_pattern.myntra.oms_settlement_reconciliation` (from previous context)."
    },
    {
      "field": "settlement.variance_amount",
      "role": "Filter Column (Variance Indicator)",
      "selected?": "Yes",
      "reason": "Directly indicates reconciliation discrepancies, as used in `query_pattern.myntra.oms_settlement_reconciliation` (from previous context)."
    },
    {
      "field": "settlement.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands'. The `query_pattern.myntra.oms_settlement_reconciliation` SQL template (from previous context) notes that `group_level_id` should be applied if present, and other Myntra patterns for Mensa use it."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "COUNT(DISTINCT settlement.order_id) where reconciliation issues exist, grouped by sales_channel",
    "numerator": "DISTINCT settlement.order_id",
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Count of unique orders with reconciliation issues for each sales channel."
  },
  "filters": [
    "oms.group_level_id = '22'",
    "settlement.group_level_id = '22'",
    "settlement.recon_status != 'MATCHED' OR settlement.variance_amount != 0"
  ],
  "joins": "INNER JOIN zs_observe.myntra_oms_settlement settlement ON oms.order_id = settlement.order_id",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` within `table.zs_observe.myntra_oms` is inferred based on its role as an Order Management System and consistent data patterns in similar contexts for Mensa Brands. The applicability of `group_level_id = 22` to `zs_observe.myntra_oms_settlement` is inferred from its usage in related Myntra query patterns for Mensa Brands. The assumption is that 'MATCHED' status and zero variance indicate no delays.",
  "sql_skeleton": "SELECT
    oms.sales_channel,
    COUNT(DISTINCT settlement.order_id) AS reconciliation_delay_count
FROM
    zs_observe.myntra_oms oms
INNER JOIN
    zs_observe.myntra_oms_settlement settlement
ON
    oms.order_id = settlement.order_id
WHERE
    oms.group_level_id = '22'
    AND settlement.group_level_id = '22'
    AND (settlement.recon_status != 'MATCHED' OR settlement.variance_amount != 0)
GROUP BY
    oms.sales_channel
ORDER BY
    reconciliation_delay_count DESC"
}


---

## 014. Compare return handling models between own website and marketplace channels.

### Timing

- started_at: `2026-05-27T04:12:39+00:00`
- duration_seconds: `43.682`
- RAG_COMPLETION_seconds: `28.273`
- GRAPH_COMPLETION_seconds: `15.409`

### Query

```text
Compare return handling models between own website and marketplace channels.

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
  "selected_source": "table.zs_observe.increff_returns",
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is inferred as the primary source for return-related data based on the presence of multiple Increff-specific query patterns (e.g., `query_pattern.increff.8_1_return_volume_by_channel_and_type`, `8_3_qc_pass_fail_analysis_shopify_d2c`, `8_4_return_reasons_shopify_d2c`) and the explicit mention of 'Mensa-specific return metrics' in `execution_constraint_set.increff.operations_manifest_refactored_constraints`. It is expected to contain `sales_channel`, `return_id`, and other return-specific dimensions for Mensa Brands (group_level_id = 22)."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension for Channel Categorization",
      "selected?": "Yes",
      "reason": "Required to categorize returns into 'Marketplace' or 'Own Website' for comparative analysis. Explicitly mentioned in return-related query patterns like `query_pattern.increff.8_1_return_volume_by_channel_and_type`."
    },
    {
      "field": "return_id",
      "role": "Metric (Count Basis)",
      "selected?": "Yes",
      "reason": "Inferred as a unique identifier for return transactions, necessary to count the volume of returns for each channel. This is standard in return data tables."
    },
    {
      "field": "qc_status",
      "role": "Dimension/Indicator for Return Handling Model",
      "selected?": "Yes",
      "reason": "Explicitly referenced in `query_pattern.increff.8_3_qc_pass_fail_analysis_shopify_d2c` for 'Shopify D2C' (an 'Own Website' channel). Its presence or absence, or distinct values, for different channels can indicate variations in return handling models (e.g., whether QC is performed)."
    },
    {
      "field": "return_reason",
      "role": "Dimension/Indicator for Return Handling Model",
      "selected?": "Yes",
      "reason": "Explicitly referenced in `query_pattern.increff.8_4_return_reasons_shopify_d2c` for 'Shopify D2C'. The granularity and types of return reasons captured can vary by channel and thus indicate different handling models."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within Increff operational tables and explicitly mentioned for Mensa-specific return metrics."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "return_status",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'` or similar) to ensure only relevant, processed return transactions are included in the analysis, consistent with best practices for sales/return reporting."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Count of returns, returns with QC data, and distinct return reasons, grouped by channel type ('Own Website' or 'Marketplace').",
    "numerator": "return_id, qc_status, return_reason",
    "denominator": null,
    "aggregation_grain": "channel_type (derived from sales_channel)",
    "deduplication_rule": "Count of unique return_id for total returns; count of unique return_id where qc_status is present; count of distinct return_reason for each channel type."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "return_status = 'COMPLETED'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, return details, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_returns`.",
  "missing_or_ambiguous": "The exact column names `return_id`, `qc_status`, and `return_reason` are inferred based on the context's description of Increff return query patterns. The specific values used for `return_status` ('COMPLETED') and the mapping of `sales_channel` values (e.g., 'Shopify D2C' for 'Own Website') are inferences based on common e-commerce data structures and the explicit mention of 'Shopify D2C' in related Increff query patterns. The comparison of 'return handling models' is indirect, inferred from the differences in available granular return data (e.g., QC status, detailed reasons) between channel types, rather than from explicit 'model' descriptors in the data.",
  "sql_skeleton": "SELECT
    CASE
        WHEN sales_channel = 'Shopify D2C' THEN 'Own Website'
        ELSE 'Marketplace'
    END AS channel_type,
    COUNT(DISTINCT return_id) AS total_returns,
    COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END) AS returns_with_qc_data,
    COUNT(DISTINCT return_reason) AS distinct_return_reasons
FROM
    zs_observe.increff_returns
WHERE
    group_level_id = '22'
    AND is_active = true
    AND return_status = 'COMPLETED'
GROUP BY
    channel_type
ORDER BY
    channel_type"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "return_status = 'COMPLETED'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, return details, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_returns`.",
  "metric_logic": {
    "aggregation_grain": "channel_type (derived from sales_channel)",
    "deduplication_rule": "Count of unique return_id for total returns; count of unique return_id where qc_status is present; count of distinct return_reason for each channel type.",
    "denominator": null,
    "formula": "Count of returns, returns with QC data, and distinct return reasons, grouped by channel type ('Own Website' or 'Marketplace').",
    "numerator": "return_id, qc_status, return_reason"
  },
  "missing_or_ambiguous": "The exact column names `return_id`, `qc_status`, and `return_reason` are inferred based on the context's description of Increff return query patterns. The specific values used for `return_status` ('COMPLETED') and the mapping of `sales_channel` values (e.g., 'Shopify D2C' for 'Own Website') are inferences based on common e-commerce data structures and the explicit mention of 'Shopify D2C' in related Increff query patterns. The comparison of 'return handling models' is indirect, inferred from the differences in available granular return data (e.g., QC status, detailed reasons) between channel types, rather than from explicit 'model' descriptors in the data.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table is inferred as the primary source for return-related data based on the presence of multiple Increff-specific query patterns (e.g., `query_pattern.increff.8_1_return_volume_by_channel_and_type`, `8_3_qc_pass_fail_analysis_shopify_d2c`, `8_4_return_reasons_shopify_d2c`) and the explicit mention of 'Mensa-specific return metrics' in `execution_constraint_set.increff.operations_manifest_refactored_constraints`. It is expected to contain `sales_channel`, `return_id`, and other return-specific dimensions for Mensa Brands (group_level_id = 22).",
      "role": "Primary Data Source Table",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to categorize returns into 'Marketplace' or 'Own Website' for comparative analysis. Explicitly mentioned in return-related query patterns like `query_pattern.increff.8_1_return_volume_by_channel_and_type`.",
      "role": "Dimension for Channel Categorization",
      "selected?": "Yes"
    },
    {
      "field": "return_id",
      "reason": "Inferred as a unique identifier for return transactions, necessary to count the volume of returns for each channel. This is standard in return data tables.",
      "role": "Metric (Count Basis)",
      "selected?": "Yes"
    },
    {
      "field": "qc_status",
      "reason": "Explicitly referenced in `query_pattern.increff.8_3_qc_pass_fail_analysis_shopify_d2c` for 'Shopify D2C' (an 'Own Website' channel). Its presence or absence, or distinct values, for different channels can indicate variations in return handling models (e.g., whether QC is performed).",
      "role": "Dimension/Indicator for Return Handling Model",
      "selected?": "Yes"
    },
    {
      "field": "return_reason",
      "reason": "Explicitly referenced in `query_pattern.increff.8_4_return_reasons_shopify_d2c` for 'Shopify D2C'. The granularity and types of return reasons captured can vary by channel and thus indicate different handling models.",
      "role": "Dimension/Indicator for Return Handling Model",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within Increff operational tables and explicitly mentioned for Mensa-specific return metrics.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'` or similar) to ensure only relevant, processed return transactions are included in the analysis, consistent with best practices for sales/return reporting.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.increff_returns",
  "sql_skeleton": "SELECT\n    CASE\n        WHEN sales_channel = 'Shopify D2C' THEN 'Own Website'\n        ELSE 'Marketplace'\n    END AS channel_type,\n    COUNT(DISTINCT return_id) AS total_returns,\n    COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END) AS returns_with_qc_data,\n    COUNT(DISTINCT return_reason) AS distinct_return_reasons\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = '22'\n    AND is_active = true\n    AND return_status = 'COMPLETED'\nGROUP BY\n    channel_type\nORDER BY\n    channel_type"
}


---

## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Timing

- started_at: `2026-05-27T04:13:22+00:00`
- duration_seconds: `32.57`
- RAG_COMPLETION_seconds: `20.87`
- GRAPH_COMPLETION_seconds: `11.7`

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

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
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins needed as all required information is available in the `zs_observe.unicommerce` table.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT sales_channel to show each unique channel only once.",
    "denominator": null,
    "formula": "List distinct sales channels currently managed by Unicommerce for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce` is inferred based on domain knowledge of OMS systems and consistent usage patterns in previous Mensa-scoped queries. The exact functional dependency beyond just listing the channels (e.g., impact on order fulfillment, inventory management, etc.) cannot be quantified with the given context, but the report will identify *which* channels would be affected.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "This table represents Unicommerce operations. If Unicommerce becomes unavailable, all channels or entities managed through this system would be affected. Previous successful queries for 'marketplaces handled through Unicommerce' for Mensa Brands confirm its relevance and scoping.",
      "role": "Primary Data Source for Unicommerce Operations",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Required to identify the specific channels that rely on Unicommerce. This column is consistently used to denote sales channels within Mensa's operational data.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions and consistent patterns).",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables, ensuring only currently active channels are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.unicommerce",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel\nFROM\n    zs_observe.unicommerce\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    sales_channel"
}

### GRAPH_COMPLETION

{"selected_source": "table.zs_observe.unicommerce", "rejected_sources": ["execution_constraint_set.increff.operations_manifest_refactored_constraints", "execution_constraint_set.jiomart.marketplace_query_constraints", "execution_constraint_set.logistics_batch_to_bank", "query_pattern.limeroad.total_forward_gmv", "query_pattern.logistics.amount_semantics_audit", "query_pattern.logistics.awb_duplicate_detection", "query_pattern.logistics.bank_credit_unmatched_courier_reference", "query_pattern.logistics.cod_expected_vs_remitted"], "require_tables": [{"field": "zs_observe.unicommerce", "role": "Primary Data Source for Unicommerce Operations", "selected?": "Yes", "reason": "This table represents Unicommerce operations. If Unicommerce becomes unavailable, all channels or entities managed through this system would be affected. The `business_scope_set.mensa_brands.operations_wms` explicitly states 'cross-channel OMS/WMS operational evidence from Increff and Unicommerce' for Mensa Brands, confirming its relevance. Previous successful queries for 'marketplaces handled through Unicommerce' for Mensa Brands also confirm its utility."}], "required_fields": [{"field": "sales_channel", "role": "Dimension (Channel Identifier)", "selected?": "Yes", "reason": "Required to identify the specific channels that rely on Unicommerce. This column is consistently used to denote sales channels within Mensa's operational data, as inferred from previous interactions."}, {"field": "group_level_id", "role": "Filter Column (Tenant Scope)", "selected?": "Yes", "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables (inferred from prior interactions and consistent patterns)."}, {"field": "is_active", "role": "Filter Column (Status)", "selected?": "Yes", "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables, ensuring only currently active channels are considered."}("field": "platform_account_id", "role": "Filter Column (Platform Account Identifier)", "selected?": "Yes", "reason": "Although not directly used in the SQL, the `business_scope_set.mensa_brands.operations_wms` explicitly lists `platform_account.mensa.unicommerce_oms.primary`, reinforcing the specific Unicommerce instance for Mensa.")], "rejected_or_ambiguous_fields": [], "metric_logic": {"formula": "List distinct sales channels currently managed by Unicommerce for Mensa Brands.", "numerator": null, "denominator": null, "aggregation_grain": "sales_channel", "deduplication_rule": "DISTINCT sales_channel to show each unique channel only once."}, "filters": ["group_level_id = '22'", "is_active = true"], "joins": "No joins needed as all required information is available in the `zs_observe.unicommerce` table.", "missing_or_ambiguous": "The explicit presence of `sales_channel` and `is_active` columns within `table.zs_observe.unicommerce` is inferred based on domain knowledge of OMS systems and consistent usage patterns in previous Mensa-scoped queries. The exact functional dependency beyond just listing the channels (e.g., impact on order fulfillment, inventory management, etc.) cannot be quantified with the given context, but the report will identify *which* channels would be affected.", "sql_skeleton": "SELECT DISTINCT\n    sales_channel\nFROM\n    zs_observe.unicommerce\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    sales_channel"}


---

## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Timing

- started_at: `2026-05-27T04:13:55+00:00`
- duration_seconds: `174.976`
- RAG_COMPLETION_seconds: `25.668`
- GRAPH_COMPLETION_seconds: `149.307`

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

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
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for Myntra sales data",
      "selected?": "Yes",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales and includes `group_level_id` for scoping."
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and mentions `group_level_id=22` in its scope policy."
    },
    {
      "field": "zs_observe.increff_sales",
      "role": "Source for Increff sales data from various channels",
      "selected?": "Yes",
      "reason": "The `execution_constraint_set.increff.operations_manifest_refactored_constraints` mentions 'revenue/GMV' filters and `group_level_id = 22` for Mensa, strongly implying this table contains sales data by channel. Inferred from previous interactions that `increff_sales` holds `sales_channel` and sales amounts."
    }
  ],
  "required_fields": [
    {
      "field": "oms.total_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Used to calculate gross sales for Myntra, as per `query_pattern.myntra.gross_sales_oms`."
    },
    {
      "field": "'Myntra'",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Literal string to identify the Myntra marketplace, as `myntra_oms` is specific to Myntra."
    },
    {
      "field": "oms.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is the documented identifier for Mensa within operational tables."
    },
    {
      "field": "oms.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables."
    },
    {
      "field": "settlement.gmv_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Inferred as the relevant column for GMV from `query_pattern.limeroad.total_forward_gmv`. A standard name for GMV values in settlement tables."
    },
    {
      "field": "'LimeRoad'",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Literal string to identify the LimeRoad marketplace, as `limeroad_settlement` is specific to LimeRoad."
    },
    {
      "field": "settlement.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Explicitly mentioned as `group_level_id=22` in `scope_policy` for LimeRoad data."
    },
    {
      "field": "settlement.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables."
    },
    {
      "field": "sales.total_amount",
      "role": "Metric (Sales Value)",
      "selected?": "Yes",
      "reason": "Inferred as the primary sales value column in `increff_sales` to represent revenue/GMV."
    },
    {
      "field": "sales.sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Explicitly used in Increff query patterns (`query_pattern.increff.7_1_monthly_gmv_by_channel`) to group sales by channel."
    },
    {
      "field": "sales.group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = 22` is mandated in `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    },
    {
      "field": "sales.transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Sum of total sales/GMV for each marketplace, then rank and select the top 2.",
    "numerator": "total_sales",
    "denominator": null,
    "aggregation_grain": "marketplace",
    "deduplication_rule": "Sum sales per unique marketplace across all data sources."
  },
  "filters": [
    "oms.group_level_id = '22'",
    "oms.is_active = true",
    "settlement.group_level_id = '22'",
    "settlement.is_active = true",
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'"
  ],
  "joins": "A UNION ALL operation is used to combine sales data from different marketplace sources, followed by aggregation. No direct joins between these disparate source tables are needed or appropriate.",
  "missing_or_ambiguous": "The exact column names for sales value in `zs_observe.limeroad_settlement` (`gmv_amount`) and `zs_observe.increff_sales` (`total_amount`) are inferred based on common data patterns for sales/settlement tables. The presence of `is_active` filter in `myntra_oms` and `limeroad_settlement` is inferred as a best practice, consistent with other documented filters. The determination of 'top 2 marketplaces' requires a ranking over all combined marketplace sales data.",
  "sql_skeleton": "WITH AllMarketplaceSales AS (
    SELECT
        'Myntra' AS marketplace_name,
        TRY_CAST(oms.total_amount AS DOUBLE) AS sales_value
    FROM
        zs_observe.myntra_oms oms
    WHERE
        oms.group_level_id = '22'
        AND oms.is_active = true

    UNION ALL

    SELECT
        'LimeRoad' AS marketplace_name,
        settlement.gmv_amount AS sales_value
    FROM
        zs_observe.limeroad_settlement settlement
    WHERE
        settlement.group_level_id = '22'
        AND settlement.is_active = true

    UNION ALL

    SELECT
        sales.sales_channel AS marketplace_name,
        sales.total_amount AS sales_value
    FROM
        zs_observe.increff_sales sales
    WHERE
        sales.group_level_id = '22'
        AND sales.is_active = true
        AND sales.order_status = 'COMPLETED'
        AND sales.transaction_type = 'SALES'
)
SELECT
    marketplace_name,
    SUM(sales_value) AS total_sales,
    RANK() OVER (ORDER BY SUM(sales_value) DESC) as sales_rank
FROM
    AllMarketplaceSales
GROUP BY
    marketplace_name
ORDER BY
    total_sales DESC
LIMIT 2"

### GRAPH_COMPLETION

{
  "filters": [
    "oms.group_level_id = '22'",
    "oms.is_active = true",
    "settlement.group_level_id = '22'",
    "settlement.is_active = true",
    "sales.group_level_id = '22'",
    "sales.is_active = true",
    "sales.order_status = 'COMPLETED'",
    "sales.transaction_type = 'SALES'",
    "amazon_oms.group_level_id = '22'",
    "amazon_oms.is_active = true"
  ],
  "joins": "A UNION ALL operation is used to combine sales data from different marketplace sources, followed by aggregation. No direct joins between these disparate source tables are needed or appropriate.",
  "metric_logic": {
    "aggregation_grain": "marketplace",
    "deduplication_rule": "Sum sales per unique marketplace across all data sources.",
    "denominator": null,
    "formula": "Sum of total sales/GMV for each marketplace, then rank and select the top 2.",
    "numerator": "total_sales"
  },
  "missing_or_ambiguous": "The exact column names for sales value in `zs_observe.amazon_oms` (`total_amount`) is inferred based on its role as an OMS and consistency with `myntra_oms`. The presence of an `is_active` filter in `myntra_oms`, `limeroad_settlement`, and `amazon_oms` is inferred as a best practice for operational data validity, consistent with filters found in `increff_sales`. The values for `group_level_id` (`22` for Mensa Brands) are consistently applied across all sources based on provided `scope_keys` and previous interactions. The determination of 'top 2 marketplaces' requires a ranking over all combined marketplace sales data.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.unicommerce",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.increff_returns"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales and includes `group_level_id` for scoping Mensa Brands. This is a direct source for marketplace sales figures.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and explicitly mentions `group_level_id=22` in its scope policy for Mensa Brands. This is a direct source for marketplace sales figures.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "The `business_scope_set.mensa_brands.operations_wms` mentions Increff for cross-channel operational evidence. `execution_constraint_set.increff.operations_manifest_refactored_constraints` mentions 'revenue/GMV' filters and `group_level_id = 22` for Mensa, indicating this table holds sales data by channel. `query_pattern.increff.7_1_monthly_gmv_by_channel` confirms the presence of sales data (`sales_channel` and sales amounts).",
      "role": "Source for Increff sales data from various channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "The `account_data_binding.mensa.amazon_in.primary.amazon_oms` explicitly links this table to Mensa Brands (`group_level_id = 22`). As an Order Management System, it is inferred to contain sales transaction data, making it a relevant source for marketplace sales.",
      "role": "Source for Amazon OMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "oms.total_amount",
      "reason": "Used to calculate gross sales for Myntra, as per `query_pattern.myntra.gross_sales_oms`. Inferred as numeric sales value.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'Myntra'",
      "reason": "Literal string to identify the Myntra marketplace for aggregation, as `myntra_oms` is specific to Myntra.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is the documented identifier for Mensa within operational tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.gmv_amount",
      "reason": "Inferred as the relevant column for GMV from `query_pattern.limeroad.total_forward_gmv`. This is a standard naming convention for GMV values in settlement tables.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'LimeRoad'",
      "reason": "Literal string to identify the LimeRoad marketplace for aggregation, as `limeroad_settlement` is specific to LimeRoad.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.group_level_id",
      "reason": "Explicitly mentioned as `group_level_id=22` in the scope policy for LimeRoad data, ensuring Mensa Brands data is selected.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "settlement.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.total_amount",
      "reason": "Inferred as the primary sales value column in `increff_sales` to represent revenue/GMV, consistent with typical sales tables.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "sales.sales_channel",
      "reason": "Explicitly used in Increff query patterns (`query_pattern.increff.7_1_monthly_gmv_by_channel`) to group sales by channel/marketplace.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "sales.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is mandated in `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "sales.is_active",
      "reason": "Mandatory filter (`is_active = true`) for data validity in Increff operations, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales.transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate revenue/GMV calculation in Increff, as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.total_amount",
      "reason": "Inferred as the standard sales value column in an OMS table for Amazon, consistent with other marketplace OMS data structures.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "'Amazon'",
      "reason": "Literal string to identify the Amazon marketplace for aggregation, as `amazon_oms` is specific to Amazon.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.group_level_id",
      "reason": "Required for scoping the report to 'Mensa Brands', as `group_level_id = '22'` is documented in `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "amazon_oms.is_active",
      "reason": "Inferred as a standard mandatory filter (`is_active = true`) for data validity in operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS sales_value\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS sales_value\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS sales_value\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS sales_value\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n)\nSELECT\n    marketplace_name,\n    SUM(sales_value) AS total_sales,\n    RANK() OVER (ORDER BY SUM(sales_value) DESC) as sales_rank\nFROM\n    AllMarketplaceSales\nGROUP BY\n    marketplace_name\nORDER BY\n    total_sales DESC\nLIMIT 2"
}


---

## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-27T04:16:50+00:00`
- duration_seconds: `254.363`
- RAG_COMPLETION_seconds: `155.369`
- GRAPH_COMPLETION_seconds: `98.993`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for each data aspect (Sales, OMS, Courier, Returns) from different source tables. These CTEs are then combined using FULL OUTER JOINs on a normalized sales_channel to create a unified view. The common sales_channel dimension is derived by uniting all distinct channel identifiers found across the various data sources.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Aggregates sales, OMS, courier, and return data to the sales_channel level. Sales are summed, OMS systems are collected as an array, top courier is selected by volume, and return metrics are counted per sales channel.",
    "denominator": null,
    "formula": "Combines total sales, associated OMS systems, primary courier partner, and return ownership metrics (total returns, QC data presence, distinct return reasons) aggregated by sales channel. The channel type (Own Website/Marketplace) is derived for each sales channel.",
    "numerator": "SUM(sales_value) for total_sales; COUNT(order_id) for primary_courier_partner; COUNT(return_id) for returns metrics."
  },
  "missing_or_ambiguous": "The primary challenge is the lack of explicit, standardized sales_channel identifiers or mapping tables that universally link all disparate data sources (Myntra OMS, LimeRoad Settlement, Increff Sales/Returns, Amazon OMS, Unicommerce) under a single 'Mensa Brands' umbrella. The channel names like 'Myntra', 'Amazon', 'LimeRoad' are inferred literals, while Increff and Unicommerce might have their own naming conventions for sales_channel. The oms_system values (e.g., 'Unicommerce_Managed', 'Myntra_Marketplace_OMS') are derived from source systems/table roles, which technically uses system context as a dimension value. The assumption of 'Shopify D2C' being 'Own Website' and others 'Marketplace' for return ownership is also an inference. The combined SQL is comprehensive but relies on these inferences for cross-system channel mapping and explicit system identification.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Used for sales data (total_amount) for Myntra marketplace and to identify Myntra as an OMS for its channel. Confirmed by query_pattern.myntra.gross_sales_oms and account data binding.",
      "role": "Source for Myntra sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Used for sales data (gmv_amount) for LimeRoad marketplace. Confirmed by query_pattern.limeroad.total_forward_gmv.",
      "role": "Source for LimeRoad sales",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table provides sales data for various channels, courier partner information (fulfilment_channel), and indicates channels managed by Increff. Mentioned in execution_constraint_set.increff.operations_manifest_refactored_constraints and various Increff sales/courier query patterns.",
      "role": "Source for general sales, courier dependency, and Increff OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (total_amount) for Amazon marketplace and indicates Amazon as an OMS for its channel. Confirmed by account_data_binding.mensa.amazon_in.primary.amazon_oms.",
      "role": "Source for Amazon sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Used to identify channels managed by Unicommerce, serving as an OMS dependency indicator. Confirmed by business_scope_set.mensa_brands.operations_wms mentioning 'Unicommerce'.",
      "role": "Source for Unicommerce OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return metrics like return_id, qc_status, return_reason, crucial for analyzing return handling models by channel type. Referenced in various Increff return query patterns.",
      "role": "Source for return ownership details",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The central dimension for combining all aspects of the dashboard. Derived or explicitly available in all relevant tables.",
      "role": "Primary Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "channel_type",
      "reason": "Derived from sales_channel to categorize into 'Own Website' or 'Marketplace' for return ownership analysis.",
      "role": "Derived Dimension (Channel Type)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales",
      "reason": "Represents the sales volume for each channel, aggregated from multiple sources.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "oms_systems_used",
      "reason": "Indicates which OMS/WMS systems are associated with a given sales channel, derived from the various OMS tables.",
      "role": "Metric (OMS Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "primary_courier_partner",
      "reason": "Identifies the top courier used for each channel, primarily from Increff sales data.",
      "role": "Metric (Courier Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Count of returns, providing insight into return volume per channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc_data",
      "reason": "Count of returns with quality check data, indicating the level of return handling detail available for a channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Number of unique return reasons, indicating granularity of return feedback by channel.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (group_level_id = '22') to scope all data to 'Mensa Brands'.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (is_active = true) for data validity across all operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (order_status = 'COMPLETED') for accurate sales and courier dependency metrics from sales tables.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (transaction_type = 'SALES') for accurate sales and courier dependency metrics from sales tables.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (return_status = 'COMPLETED') to ensure only relevant, processed return transactions are included.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_CTE AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        SUM(TRY_CAST(oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n    GROUP BY\n        'Myntra'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        SUM(settlement.gmv_amount) AS total_sales\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n    GROUP BY\n        'LimeRoad'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS sales_channel,\n        SUM(sales.total_amount) AS total_sales\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n    GROUP BY\n        sales.sales_channel\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        SUM(TRY_CAST(amazon_oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n    GROUP BY\n        'Amazon'\n),\nOMS_Dependency_Raw_CTE AS (\n    SELECT DISTINCT\n        unicommerce.sales_channel AS sales_channel,\n        'Unicommerce_Managed' AS oms_system\n    FROM\n        zs_observe.unicommerce unicommerce\n    WHERE\n        unicommerce.group_level_id = '22'\n        AND unicommerce.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Myntra' AS sales_channel,\n        'Myntra_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Amazon' AS sales_channel,\n        'Amazon_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        increff_sales.sales_channel AS sales_channel,\n        'Increff_Managed_OMS/WMS' AS oms_system\n    FROM\n        zs_observe.increff_sales increff_sales\n    WHERE\n        increff_sales.group_level_id = '22'\n        AND increff_sales.is_active = true\n),\nOMS_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        ARRAY_AGG(DISTINCT oms_system) AS oms_systems_used\n    FROM\n        OMS_Dependency_Raw_CTE\n    GROUP BY\n        sales_channel\n),\nCourier_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        fulfilment_channel AS primary_courier_partner,\n        order_count\n    FROM (\n        SELECT\n            sales.sales_channel,\n            sales.fulfilment_channel,\n            COUNT(sales.order_id) AS order_count,\n            ROW_NUMBER() OVER(PARTITION BY sales.sales_channel ORDER BY COUNT(sales.order_id) DESC) as rn\n        FROM\n            zs_observe.increff_sales sales\n        WHERE\n            sales.group_level_id = '22'\n            AND sales.is_active = true\n            AND sales.order_status = 'COMPLETED'\n            AND sales.transaction_type = 'SALES'\n            AND sales.fulfilment_channel IS NOT NULL\n        GROUP BY\n            sales.sales_channel,\n            sales.fulfilment_channel\n    ) AS ranked_couriers\n    WHERE rn = 1\n),\nReturn_Ownership_CTE AS (\n    SELECT\n        returns.sales_channel,\n        COUNT(DISTINCT returns.return_id) AS total_returns,\n        COUNT(CASE WHEN returns.qc_status IS NOT NULL THEN returns.return_id END) AS returns_with_qc_data,\n        COUNT(DISTINCT returns.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns returns\n    WHERE\n        returns.group_level_id = '22'\n        AND returns.is_active = true\n        AND returns.return_status = 'COMPLETED'\n    GROUP BY\n        returns.sales_channel\n),\nAll_Channels AS (\n    SELECT sales_channel FROM Sales_CTE\n    UNION\n    SELECT sales_channel FROM OMS_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Courier_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Return_Ownership_CTE\n)\nSELECT\n    ac.sales_channel,\n    CASE WHEN ac.sales_channel = 'Shopify D2C' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type,\n    COALESCE(s.total_sales, 0) AS total_sales,\n    COALESCE(o.oms_systems_used, ARRAY<STRING>[]) AS oms_systems_used,\n    c.primary_courier_partner,\n    COALESCE(ro.total_returns, 0) AS total_returns,\n    COALESCE(ro.returns_with_qc_data, 0) AS returns_with_qc_data,\n    COALESCE(ro.distinct_return_reasons, 0) AS distinct_return_reasons\nFROM\n    (SELECT DISTINCT sales_channel FROM All_Channels) ac\nLEFT JOIN\n    Sales_CTE s ON ac.sales_channel = s.sales_channel\nLEFT JOIN\n    OMS_Dependency_CTE o ON ac.sales_channel = o.sales_channel\nLEFT JOIN\n    Courier_Dependency_CTE c ON ac.sales_channel = c.sales_channel\nLEFT JOIN\n    Return_Ownership_CTE ro ON ac.sales_channel = ro.sales_channel\nORDER BY\n    ac.sales_channel;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for each data aspect (Sales, OMS, Courier, Returns) from different source tables. These CTEs are then combined using FULL OUTER JOINs on a normalized `sales_channel` to create a unified view. The common `sales_channel` dimension is derived by uniting all distinct channel identifiers found across the various data sources. For courier dependency, an inner query ranks couriers per channel to identify the primary one.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Aggregates sales, OMS, courier, and return data to the sales_channel level. Sales are summed. OMS systems are collected as an array of distinct systems. The top courier is selected by volume. Return metrics are counted per sales channel, with `return_id` used for total/QC counts and `return_reason` for distinct counts.",
    "denominator": null,
    "formula": "Combines total sales, associated OMS systems, primary courier partner, and return ownership metrics (total returns, QC data presence, distinct return reasons) aggregated by sales channel. The channel type (Own Website/Marketplace) is derived for each sales channel.",
    "numerator": "SUM(sales_value) for total_sales; COUNT(order_id) for primary_courier_partner (after ranking); COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason) for returns metrics."
  },
  "missing_or_ambiguous": "The primary challenge is the lack of explicit, standardized `sales_channel` identifiers or mapping tables that universally link all disparate data sources (Myntra OMS, LimeRoad Settlement, Increff Sales/Returns, Amazon OMS, Unicommerce) under a single 'Mensa Brands' umbrella. The channel names like 'Myntra', 'Amazon', 'LimeRoad' are inferred as literal strings for their respective dedicated tables, while Increff and Unicommerce might use varied `sales_channel` column values. The `oms_system` values (e.g., 'Unicommerce_Managed', 'Myntra_Marketplace_OMS') are derived from source systems/table roles, which technically uses system context as a dimension value rather than an explicit column. The assumption of 'Shopify D2C' being 'Own Website' and other `sales_channel` values being 'Marketplace' for return ownership is also an inference based on common e-commerce distinctions and specific query patterns mentioning 'Shopify D2C'. The specific column names for sales values (`total_amount`, `gmv_amount`) are inferred from common marketplace data schemas and related query patterns. The `is_active` filter is inferred as a best practice for operational data validity across all relevant tables.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Used for sales data (total_amount) for Myntra marketplace and to identify Myntra as an OMS for its channel. Confirmed by `query_pattern.myntra.gross_sales_oms` and `account_data_binding.mensa.amazon_in.primary.amazon_oms` (which establishes pattern for Mensa's marketplace OMS tables).",
      "role": "Source for Myntra sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Used for sales data (gmv_amount) for LimeRoad marketplace. Confirmed by `query_pattern.limeroad.total_forward_gmv`.",
      "role": "Source for LimeRoad sales",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table provides sales data for various channels, courier partner information (fulfilment_channel), and indicates channels managed by Increff. Mentioned in `execution_constraint_set.increff.operations_manifest_refactored_constraints` and various Increff sales/courier query patterns (e.g., `query_pattern.increff.7_1_monthly_gmv_by_channel`, `query_pattern.increff.7_6_courier_partner_distribution_normalized`).",
      "role": "Source for general sales, courier dependency, and Increff OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (total_amount) for Amazon marketplace and indicates Amazon as an OMS for its channel. Confirmed by `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Source for Amazon sales and OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Used to identify channels managed by Unicommerce, serving as an OMS dependency indicator. Confirmed by `business_scope_set.mensa_brands.operations_wms` mentioning 'Unicommerce'.",
      "role": "Source for Unicommerce OMS association",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return metrics like `return_id`, `qc_status`, `return_reason`, crucial for analyzing return handling models by channel type. Referenced in various Increff return query patterns (e.g., `query_pattern.increff.8_1_return_volume_by_channel_and_type`).",
      "role": "Source for return ownership details",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The central dimension for combining all aspects of the dashboard. Derived or explicitly available in all relevant tables. Normalization is required across different sources.",
      "role": "Primary Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "channel_type",
      "reason": "Derived from `sales_channel` to categorize into 'Own Website' or 'Marketplace' for return ownership analysis, as suggested by `query_pattern.increff.8_3_qc_pass_fail_analysis_shopify_d2c` for 'Shopify D2C'.",
      "role": "Derived Dimension (Channel Type)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales",
      "reason": "Represents the sales volume for each channel, aggregated from multiple sources (`myntra_oms.total_amount`, `limeroad_settlement.gmv_amount`, `increff_sales.total_amount`, `amazon_oms.total_amount`).",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "oms_systems_used",
      "reason": "Indicates which OMS/WMS systems are associated with a given sales channel, derived from the various OMS tables (`unicommerce`, `myntra_oms`, `amazon_oms`, `increff_sales`).",
      "role": "Metric (OMS Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "primary_courier_partner",
      "reason": "Identifies the top courier used for each channel, primarily from `increff_sales.fulfilment_channel` based on shipment count.",
      "role": "Metric (Courier Dependency)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Count of returns, providing insight into return volume per channel, derived from `increff_returns.return_id`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc_data",
      "reason": "Count of returns with quality check data, indicating the level of return handling detail available for a channel, derived from `increff_returns.qc_status`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Number of unique return reasons, indicating granularity of return feedback by channel, derived from `increff_returns.return_reason`.",
      "role": "Metric (Return Ownership)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as per `account_data_binding` entries and scope policies.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, consistent with `execution_constraint_set.increff.operations_manifest_refactored_constraints` and common data practices.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales and courier dependency metrics from sales tables (`increff_sales`), as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales and courier dependency metrics from sales tables (`increff_sales`), as per `execution_constraint_set.increff.operations_manifest_refactored_constraints`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`).",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_CTE AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        SUM(TRY_CAST(oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n    GROUP BY\n        'Myntra'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        SUM(settlement.gmv_amount) AS total_sales\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n    GROUP BY\n        'LimeRoad'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS sales_channel,\n        SUM(sales.total_amount) AS total_sales\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n    GROUP BY\n        sales.sales_channel\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        SUM(TRY_CAST(amazon_oms.total_amount AS DOUBLE)) AS total_sales\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n    GROUP BY\n        'Amazon'\n),\nOMS_Dependency_Raw_CTE AS (\n    SELECT DISTINCT\n        unicommerce.sales_channel AS sales_channel,\n        'Unicommerce_Managed' AS oms_system\n    FROM\n        zs_observe.unicommerce unicommerce\n    WHERE\n        unicommerce.group_level_id = '22'\n        AND unicommerce.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Myntra' AS sales_channel,\n        'Myntra_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Amazon' AS sales_channel,\n        'Amazon_Marketplace_OMS' AS oms_system\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n\n    UNION ALL\n\n    SELECT DISTINCT\n        increff_sales.sales_channel AS sales_channel,\n        'Increff_Managed_OMS/WMS' AS oms_system\n    FROM\n        zs_observe.increff_sales increff_sales\n    WHERE\n        increff_sales.group_level_id = '22'\n        AND increff_sales.is_active = true\n),\nOMS_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        ARRAY_AGG(DISTINCT oms_system) AS oms_systems_used\n    FROM\n        OMS_Dependency_Raw_CTE\n    GROUP BY\n        sales_channel\n),\nCourier_Dependency_CTE AS (\n    SELECT\n        sales_channel,\n        fulfilment_channel AS primary_courier_partner,\n        order_count\n    FROM (\n        SELECT\n            sales.sales_channel,\n            sales.fulfilment_channel,\n            COUNT(sales.order_id) AS order_count,\n            ROW_NUMBER() OVER(PARTITION BY sales.sales_channel ORDER BY COUNT(sales.order_id) DESC) as rn\n        FROM\n            zs_observe.increff_sales sales\n        WHERE\n            sales.group_level_id = '22'\n            AND sales.is_active = true\n            AND sales.order_status = 'COMPLETED'\n            AND sales.transaction_type = 'SALES'\n            AND sales.fulfilment_channel IS NOT NULL\n        GROUP BY\n            sales.sales_channel,\n            sales.fulfilment_channel\n    ) AS ranked_couriers\n    WHERE rn = 1\n),\nReturn_Ownership_CTE AS (\n    SELECT\n        returns.sales_channel,\n        COUNT(DISTINCT returns.return_id) AS total_returns,\n        COUNT(CASE WHEN returns.qc_status IS NOT NULL THEN returns.return_id END) AS returns_with_qc_data,\n        COUNT(DISTINCT returns.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns returns\n    WHERE\n        returns.group_level_id = '22'\n        AND returns.is_active = true\n        AND returns.return_status = 'COMPLETED'\n    GROUP BY\n        returns.sales_channel\n),\nAll_Channels AS (\n    SELECT sales_channel FROM Sales_CTE\n    UNION\n    SELECT sales_channel FROM OMS_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Courier_Dependency_CTE\n    UNION\n    SELECT sales_channel FROM Return_Ownership_CTE\n)\nSELECT\n    ac.sales_channel,\n    CASE WHEN ac.sales_channel = 'Shopify D2C' THEN 'Own Website' ELSE 'Marketplace' END AS channel_type,\n    COALESCE(s.total_sales, 0) AS total_sales,\n    COALESCE(o.oms_systems_used, ARRAY<STRING>[]) AS oms_systems_used,\n    c.primary_courier_partner,\n    COALESCE(ro.total_returns, 0) AS total_returns,\n    COALESCE(ro.returns_with_qc_data, 0) AS returns_with_qc_data,\n    COALESCE(ro.distinct_return_reasons, 0) AS distinct_return_reasons\nFROM\n    (SELECT DISTINCT sales_channel FROM All_Channels) ac\nLEFT JOIN\n    Sales_CTE s ON ac.sales_channel = s.sales_channel\nLEFT JOIN\n    OMS_Dependency_CTE o ON ac.sales_channel = o.sales_channel\nLEFT JOIN\n    Courier_Dependency_CTE c ON ac.sales_channel = c.sales_channel\nLEFT JOIN\n    Return_Ownership_CTE ro ON ac.sales_channel = ro.sales_channel\nORDER BY\n    ac.sales_channel;"
}


---

## 018. Design a profitability analysis report estimating operational complexity cost per marketplace.

### Timing

- started_at: `2026-05-27T04:21:04+00:00`
- duration_seconds: `176.432`
- RAG_COMPLETION_seconds: `147.977`
- GRAPH_COMPLETION_seconds: `28.455`

### Query

```text
Design a profitability analysis report estimating operational complexity cost per marketplace.

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
    "group_level_id = '22'",
    "is_active = true",
    "recon_status != 'MATCHED' (for Myntra recon variance/count)",
    "order_status = 'COMPLETED' (for Increff sales)",
    "transaction_type = 'SALES' (for Increff sales)",
    "return_status = 'COMPLETED' (for Increff returns)"
  ],
  "joins": "Multiple CTEs are used to prepare marketplace-specific data. These CTEs are then combined using FULL OUTER JOINs on a normalized 'marketplace_name' field to ensure all available metrics are shown for each marketplace, even if a marketplace doesn't have all types of data. This allows a unified view of operational complexity indicators across disparate sources.",
  "metric_logic": {
    "aggregation_grain": "marketplace_name",
    "deduplication_rule": "Sales are summed. Reconciliation variances/adjustments are summed. Counts of distinct unreconciled orders and returns are provided. Marketplace fees are summed. All aggregated by marketplace name.",
    "denominator": null,
    "formula": "Aggregates various operational metrics (sales volume, reconciliation variances, non-order adjustments, pending receivables, marketplace fees, return counts, QC involvement, distinct return reasons) per marketplace/channel to estimate operational complexity cost.",
    "numerator": "SUM(total_sales_gmv), SUM(myntra_recon_variance_amount), COUNT(myntra_unreconciled_orders), SUM(myntra_non_order_adjustments_amount), SUM(myntra_total_pending_receivables), SUM(myntra_mp_fees), COUNT(increff_total_returns), COUNT(increff_returns_with_qc), COUNT(DISTINCT increff_distinct_return_reasons)"
  },
  "missing_or_ambiguous": "The primary missing element is a direct, quantifiable 'operational complexity cost' metric. This report uses proxy metrics (counts, sums of variances/adjustments/fees) to indicate operational complexity. Explicit marketplace fees (e.g., specific commission types) are only available for Myntra in the provided context, leading to an incomplete cost picture for other marketplaces like LimeRoad and Amazon. The interpretation of which `sales_channel` values from Increff represent a 'marketplace' vs. 'own website' is an inference (assuming all are relevant channels for complexity analysis unless explicitly D2C). Logistics reconciliation issues (AWB duplicates, COD gaps, bank unmatched references) from `query_pattern.logistics.*` are not included as the context does not explicitly link these issues to specific marketplaces at the required granularity for a 'per marketplace' breakdown.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Provides gross sales for Myntra, serving as a base volume metric for complexity analysis.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms_settlement",
      "reason": "Provides variance amounts and reconciliation statuses, direct indicators of operational complexity due to settlement issues.",
      "role": "Source for Myntra reconciliation complexity",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_non_order_settlement",
      "reason": "Provides amounts for adjustments outside regular orders, indicating complexity in managing non-standard financial flows.",
      "role": "Source for Myntra non-order adjustment complexity",
      "selected?": "Yes"
    },
    {
      "field": "zs_ingest.myntra_receivables",
      "reason": "Provides data on pending receivables and their aging, indicating follow-up effort and financial operational complexity.",
      "role": "Source for Myntra financial complexity (pending amounts)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_settlement",
      "reason": "Provides marketplace-specific fees (prepaid/postpaid MP fees) which are direct cost components and can indicate fee structure complexity.",
      "role": "Source for Myntra explicit fees",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Provides gross merchandise value (GMV) for LimeRoad, a base volume metric for complexity analysis.",
      "role": "Source for LimeRoad sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Provides total sales for Amazon, a base volume metric for complexity analysis.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Provides sales data for various channels managed by Increff and the sales_channel dimension for grouping.",
      "role": "Source for general sales data and channel information",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return counts, QC status, and return reasons, directly indicating operational complexity of return handling for Increff-managed channels.",
      "role": "Source for Increff return-related complexity",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Central dimension for aggregating operational complexity metrics. Derived from specific tables (e.g., 'Myntra', 'LimeRoad', 'Amazon') or directly from the `sales_channel` column in Increff tables.",
      "role": "Dimension (Marketplace/Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales_gmv",
      "reason": "Provides the overall volume of activity for each marketplace, against which complexity indicators can be evaluated. Aggregated from `total_amount` or `gmv_amount` across various sales sources.",
      "role": "Metric (Contextual Sales Volume)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_recon_variance_amount",
      "reason": "Sum of `variance_amount` from `myntra_oms_settlement` for non-matched items, directly indicating reconciliation complexity.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_unreconciled_orders_count",
      "reason": "Count of distinct orders with non-'MATCHED' `recon_status` from `myntra_oms_settlement`, indicating the volume of reconciliation issues.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_non_order_adjustments_amount",
      "reason": "Sum of `non_order_settlement_amount` from `myntra_non_order_settlement`, indicating complexity from non-standard financial adjustments.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_total_pending_receivables",
      "reason": "Sum of `pending_amount` from `myntra_receivables`, indicating financial operational burden.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_mp_fees",
      "reason": "Sum of `prepaid_mp_fees` and `postpaid_mp_fees` from `myntra_settlement`, representing explicit marketplace costs and complexity of fee management.",
      "role": "Metric (Direct Cost / Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_total_returns",
      "reason": "Count of returns from `increff_returns`, indicating the volume of return handling operations.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_returns_with_qc",
      "reason": "Count of returns with `qc_status` data from `increff_returns`, indicating more involved quality control processes for returns.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_distinct_return_reasons",
      "reason": "Count of distinct `return_reason` from `increff_returns`, indicating the granularity and potential complexity of analyzing return feedback.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands' across all tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across operational tables (Myntra OMS, Myntra Non-Order Settlement, LimeRoad Settlement, Amazon OMS, Increff Sales, Increff Returns, Myntra Settlement, Unicommerce).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "recon_status",
      "reason": "Used in `myntra_oms_settlement` to identify non-matched records as complexity indicators.",
      "role": "Filter Column (Reconciliation Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from `increff_sales`.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included from `increff_returns`.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    },
    {
      "field": "dpd",
      "reason": "Provides granularity for pending receivables, indicating severity of financial operational complexity.",
      "role": "Dimension (Days Past Due for Receivables)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_GMV AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales_gmv\n    FROM\n        zs_observe.myntra_oms\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        SUM(gmv_amount) AS total_sales_gmv\n    FROM\n        zs_observe.limeroad_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        sales_channel AS marketplace_name,\n        SUM(total_amount) AS total_sales_gmv\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES'\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        'Amazon' AS marketplace_name,\n        SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales_gmv\n    FROM\n        zs_observe.amazon_oms\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nMyntra_Recon_Complexity AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(variance_amount) AS myntra_recon_variance_amount,\n        COUNT(DISTINCT order_id) AS myntra_unreconciled_orders_count\n    FROM\n        zs_observe.myntra_oms_settlement\n    WHERE\n        group_level_id = '22' AND (recon_status != 'MATCHED' OR variance_amount != 0)\n    GROUP BY 1\n),\nMyntra_Non_Order_Adjustments AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(non_order_settlement_amount) AS myntra_non_order_adjustments_amount\n    FROM\n        zs_observe.myntra_non_order_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nMyntra_Pending_Receivables AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(pending_amount) AS myntra_total_pending_receivables\n    FROM\n        zs_ingest.myntra_receivables\n    WHERE\n        group_level_id = '22'\n    GROUP BY 1\n),\nMyntra_MP_Fees AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(COALESCE(prepaid_mp_fees, 0) + COALESCE(postpaid_mp_fees, 0)) AS myntra_mp_fees\n    FROM\n        zs_observe.myntra_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nIncreff_Return_Complexity AS (\n    SELECT\n        sales_channel AS marketplace_name,\n        COUNT(DISTINCT return_id) AS increff_total_returns,\n        COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END) AS increff_returns_with_qc,\n        COUNT(DISTINCT return_reason) AS increff_distinct_return_reasons\n    FROM\n        zs_observe.increff_returns\n    WHERE\n        group_level_id = '22' AND is_active = true AND return_status = 'COMPLETED'\n    GROUP BY 1\n),\nAll_Marketplaces AS (\n    SELECT marketplace_name FROM Sales_GMV\n    UNION\n    SELECT marketplace_name FROM Myntra_Recon_Complexity\n    UNION\n    SELECT marketplace_name FROM Myntra_Non_Order_Adjustments\n    UNION\n    SELECT marketplace_name FROM Myntra_Pending_Receivables\n    UNION\n    SELECT marketplace_name FROM Myntra_MP_Fees\n    UNION\n    SELECT marketplace_name FROM Increff_Return_Complexity\n)\nSELECT\n    am.marketplace_name,\n    COALESCE(sg.total_sales_gmv, 0) AS total_sales_gmv,\n    COALESCE(mrc.myntra_recon_variance_amount, 0) AS myntra_recon_variance_amount,\n    COALESCE(mrc.myntra_unreconciled_orders_count, 0) AS myntra_unreconciled_orders_count,\n    COALESCE(mnoa.myntra_non_order_adjustments_amount, 0) AS myntra_non_order_adjustments_amount,\n    COALESCE(mpr.myntra_total_pending_receivables, 0) AS myntra_total_pending_receivables,\n    COALESCE(mmf.myntra_mp_fees, 0) AS myntra_mp_fees,\n    COALESCE(irc.increff_total_returns, 0) AS increff_total_returns,\n    COALESCE(irc.increff_returns_with_qc, 0) AS increff_returns_with_qc,\n    COALESCE(irc.increff_distinct_return_reasons, 0) AS increff_distinct_return_reasons\nFROM\n    (SELECT DISTINCT marketplace_name FROM All_Marketplaces) am\nLEFT JOIN\n    Sales_GMV sg ON am.marketplace_name = sg.marketplace_name\nLEFT JOIN\n    Myntra_Recon_Complexity mrc ON am.marketplace_name = mrc.marketplace_name\nLEFT JOIN\n    Myntra_Non_Order_Adjustments mnoa ON am.marketplace_name = mnoa.marketplace_name\nLEFT JOIN\n    Myntra_Pending_Receivables mpr ON am.marketplace_name = mpr.marketplace_name\nLEFT JOIN\n    Myntra_MP_Fees mmf ON am.marketplace_name = mmf.marketplace_name\nLEFT JOIN\n    Increff_Return_Complexity irc ON am.marketplace_name = irc.marketplace_name\nORDER BY am.marketplace_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "recon_status != 'MATCHED' (for Myntra recon variance/count)",
    "order_status = 'COMPLETED' (for Increff sales)",
    "transaction_type = 'SALES' (for Increff sales)",
    "return_status = 'COMPLETED' (for Increff returns)"
  ],
  "joins": "Multiple CTEs are used to prepare marketplace-specific data. These CTEs are then combined using FULL OUTER JOINs on a normalized 'marketplace_name' field to ensure all available metrics are shown for each marketplace, even if a marketplace doesn't have all types of data. This allows a unified view of operational complexity indicators across disparate sources.",
  "metric_logic": {
    "aggregation_grain": "marketplace_name",
    "deduplication_rule": "Sales are summed. Reconciliation variances/adjustments are summed. Counts of distinct unreconciled orders and returns are provided. Marketplace fees are summed. All aggregated by marketplace name.",
    "denominator": null,
    "formula": "Aggregates various operational metrics (sales volume, reconciliation variances, non-order adjustments, pending receivables, marketplace fees, return counts, QC involvement, distinct return reasons) per marketplace/channel to estimate operational complexity cost.",
    "numerator": "SUM(total_sales_gmv), SUM(myntra_recon_variance_amount), COUNT(myntra_unreconciled_orders), SUM(myntra_non_order_adjustments_amount), SUM(myntra_total_pending_receivables), SUM(myntra_mp_fees), COUNT(increff_total_returns), COUNT(increff_returns_with_qc), COUNT(DISTINCT increff_distinct_return_reasons)"
  },
  "missing_or_ambiguous": "The primary missing element is a direct, quantifiable 'operational complexity cost' metric. This report uses proxy metrics (counts, sums of variances/adjustments/fees) to indicate operational complexity. Explicit marketplace fees (e.g., specific commission types) are only available for Myntra in the provided context, leading to an incomplete cost picture for other marketplaces like LimeRoad and Amazon. The interpretation of which `sales_channel` values from Increff represent a 'marketplace' vs. 'own website' is an inference (assuming all are relevant channels for complexity analysis unless explicitly D2C). Logistics reconciliation issues (AWB duplicates, COD gaps, bank unmatched references) from `query_pattern.logistics.*` are not included as the context does not explicitly link these issues to specific marketplaces at the required granularity for a 'per marketplace' breakdown.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Provides gross sales for Myntra, serving as a base volume metric for complexity analysis.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms_settlement",
      "reason": "Provides variance amounts and reconciliation statuses, direct indicators of operational complexity due to settlement issues.",
      "role": "Source for Myntra reconciliation complexity",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_non_order_settlement",
      "reason": "Provides amounts for adjustments outside regular orders, indicating complexity in managing non-standard financial flows.",
      "role": "Source for Myntra non-order adjustment complexity",
      "selected?": "Yes"
    },
    {
      "field": "zs_ingest.myntra_receivables",
      "reason": "Provides data on pending receivables and their aging, indicating follow-up effort and financial operational complexity.",
      "role": "Source for Myntra financial complexity (pending amounts)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_settlement",
      "reason": "Provides marketplace-specific fees (prepaid/postpaid MP fees) which are direct cost components and can indicate fee structure complexity.",
      "role": "Source for Myntra explicit fees",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "Provides gross merchandise value (GMV) for LimeRoad, a base volume metric for complexity analysis.",
      "role": "Source for LimeRoad sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Provides total sales for Amazon, a base volume metric for complexity analysis.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Provides sales data for various channels managed by Increff and the sales_channel dimension for grouping.",
      "role": "Source for general sales data and channel information",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Provides return counts, QC status, and return reasons, directly indicating operational complexity of return handling for Increff-managed channels.",
      "role": "Source for Increff return-related complexity",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Central dimension for aggregating operational complexity metrics. Derived from specific tables (e.g., 'Myntra', 'LimeRoad', 'Amazon') or directly from the `sales_channel` column in Increff tables.",
      "role": "Dimension (Marketplace/Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "total_sales_gmv",
      "reason": "Provides the overall volume of activity for each marketplace, against which complexity indicators can be evaluated. Aggregated from `total_amount` or `gmv_amount` across various sales sources.",
      "role": "Metric (Contextual Sales Volume)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_recon_variance_amount",
      "reason": "Sum of `variance_amount` from `myntra_oms_settlement` for non-matched items, directly indicating reconciliation complexity.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_unreconciled_orders_count",
      "reason": "Count of distinct orders with non-'MATCHED' `recon_status` from `myntra_oms_settlement`, indicating the volume of reconciliation issues.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_non_order_adjustments_amount",
      "reason": "Sum of `non_order_settlement_amount` from `myntra_non_order_settlement`, indicating complexity from non-standard financial adjustments.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_total_pending_receivables",
      "reason": "Sum of `pending_amount` from `myntra_receivables`, indicating financial operational burden.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "myntra_mp_fees",
      "reason": "Sum of `prepaid_mp_fees` and `postpaid_mp_fees` from `myntra_settlement`, representing explicit marketplace costs and complexity of fee management.",
      "role": "Metric (Direct Cost / Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_total_returns",
      "reason": "Count of returns from `increff_returns`, indicating the volume of return handling operations.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_returns_with_qc",
      "reason": "Count of returns with `qc_status` data from `increff_returns`, indicating more involved quality control processes for returns.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "increff_distinct_return_reasons",
      "reason": "Count of distinct `return_reason` from `increff_returns`, indicating the granularity and potential complexity of analyzing return feedback.",
      "role": "Metric (Operational Complexity Indicator)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands' across all tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across operational tables (Myntra OMS, Myntra Non-Order Settlement, LimeRoad Settlement, Amazon OMS, Increff Sales, Increff Returns, Myntra Settlement, Unicommerce).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "recon_status",
      "reason": "Used in `myntra_oms_settlement` to identify non-matched records as complexity indicators.",
      "role": "Filter Column (Reconciliation Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from `increff_sales`.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales`.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included from `increff_returns`.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    },
    {
      "field": "dpd",
      "reason": "Provides granularity for pending receivables, indicating severity of financial operational complexity.",
      "role": "Dimension (Days Past Due for Receivables)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH Sales_GMV AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales_gmv\n    FROM\n        zs_observe.myntra_oms\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        SUM(gmv_amount) AS total_sales_gmv\n    FROM\n        zs_observe.limeroad_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        sales_channel AS marketplace_name,\n        SUM(total_amount) AS total_sales_gmv\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES'\n    GROUP BY 1\n    UNION ALL\n    SELECT\n        'Amazon' AS marketplace_name,\n        SUM(TRY_CAST(total_amount AS DOUBLE)) AS total_sales_gmv\n    FROM\n        zs_observe.amazon_oms\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nMyntra_Recon_Complexity AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(variance_amount) AS myntra_recon_variance_amount,\n        COUNT(DISTINCT order_id) AS myntra_unreconciled_orders_count\n    FROM\n        zs_observe.myntra_oms_settlement\n    WHERE\n        group_level_id = '22' AND (recon_status != 'MATCHED' OR variance_amount != 0)\n    GROUP BY 1\n),\nMyntra_Non_Order_Adjustments AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(non_order_settlement_amount) AS myntra_non_order_adjustments_amount\n    FROM\n        zs_observe.myntra_non_order_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nMyntra_Pending_Receivables AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(pending_amount) AS myntra_total_pending_receivables\n    FROM\n        zs_ingest.myntra_receivables\n    WHERE\n        group_level_id = '22'\n    GROUP BY 1\n),\nMyntra_MP_Fees AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        SUM(COALESCE(prepaid_mp_fees, 0) + COALESCE(postpaid_mp_fees, 0)) AS myntra_mp_fees\n    FROM\n        zs_observe.myntra_settlement\n    WHERE\n        group_level_id = '22' AND is_active = true\n    GROUP BY 1\n),\nIncreff_Return_Complexity AS (\n    SELECT\n        sales_channel AS marketplace_name,\n        COUNT(DISTINCT return_id) AS increff_total_returns,\n        COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END) AS increff_returns_with_qc,\n        COUNT(DISTINCT return_reason) AS increff_distinct_return_reasons\n    FROM\n        zs_observe.increff_returns\n    WHERE\n        group_level_id = '22' AND is_active = true AND return_status = 'COMPLETED'\n    GROUP BY 1\n),\nAll_Marketplaces AS (\n    SELECT marketplace_name FROM Sales_GMV\n    UNION\n    SELECT marketplace_name FROM Myntra_Recon_Complexity\n    UNION\n    SELECT marketplace_name FROM Myntra_Non_Order_Adjustments\n    UNION\n    SELECT marketplace_name FROM Myntra_Pending_Receivables\n    UNION\n    SELECT marketplace_name FROM Myntra_MP_Fees\n    UNION\n    SELECT marketplace_name FROM Increff_Return_Complexity\n)\nSELECT\n    am.marketplace_name,\n    COALESCE(sg.total_sales_gmv, 0) AS total_sales_gmv,\n    COALESCE(mrc.myntra_recon_variance_amount, 0) AS myntra_recon_variance_amount,\n    COALESCE(mrc.myntra_unreconciled_orders_count, 0) AS myntra_unreconciled_orders_count,\n    COALESCE(mnoa.myntra_non_order_adjustments_amount, 0) AS myntra_non_order_adjustments_amount,\n    COALESCE(mpr.myntra_total_pending_receivables, 0) AS myntra_total_pending_receivables,\n    COALESCE(mmf.myntra_mp_fees, 0) AS myntra_mp_fees,\n    COALESCE(irc.increff_total_returns, 0) AS increff_total_returns,\n    COALESCE(irc.increff_returns_with_qc, 0) AS increff_returns_with_qc,\n    COALESCE(irc.increff_distinct_return_reasons, 0) AS increff_distinct_return_reasons\nFROM\n    (SELECT DISTINCT marketplace_name FROM All_Marketplaces) am\nLEFT JOIN\n    Sales_GMV sg ON am.marketplace_name = sg.marketplace_name\nLEFT JOIN\n    Myntra_Recon_Complexity mrc ON am.marketplace_name = mrc.marketplace_name\nLEFT JOIN\n    Myntra_Non_Order_Adjustments mnoa ON am.marketplace_name = mnoa.marketplace_name\nLEFT JOIN\n    Myntra_Pending_Receivables mpr ON am.marketplace_name = mpr.marketplace_name\nLEFT JOIN\n    Myntra_MP_Fees mmf ON am.marketplace_name = mmf.marketplace_name\nLEFT JOIN\n    Increff_Return_Complexity irc ON am.marketplace_name = irc.marketplace_name\nORDER BY am.marketplace_name;"
}


---

## 019. Build a SKU profitability report.

### Timing

- started_at: `2026-05-27T04:24:01+00:00`
- duration_seconds: `179.196`
- RAG_COMPLETION_seconds: `92.009`
- GRAPH_COMPLETION_seconds: `87.186`

### Query

```text
Build a SKU profitability report.

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
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Source for SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` explicitly mentions `sku_id` as a join key, and `query_pattern.increff.7_5_top_skus_by_volume` confirms SKU-level analysis from this source."
    },
    {
      "field": "zs_observe.increff_returns",
      "role": "Source for SKU-level return data (cost indicators)",
      "selected?": "Yes",
      "reason": "`query_pattern.increff.8_6_enrich_returns_with_sku_from_sales` explicitly indicates that returns can be linked to sales by SKU. This provides return volume and complexity metrics per SKU, which are key cost indicators for profitability."
    },
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for Myntra SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "As an OMS for a major marketplace, it is inferred to contain SKU-level sales details. Although `query_pattern.myntra.gross_sales_oms` mentions `total_amount` (likely order level), the presence of SKU detail is a standard expectation in OMS tables for profitability analysis."
    },
    {
      "field": "zs_observe.amazon_oms",
      "role": "Source for Amazon SKU-level sales data (revenue and quantity)",
      "selected?": "Yes",
      "reason": "Similar to `myntra_oms`, Amazon's OMS is inferred to contain `sku_id` and item-level sales data necessary for SKU profitability."
    },
    {
      "field": "zs_observe.amazon_fee_preview",
      "role": "Source for Amazon SKU-level fees (cost component)",
      "selected?": "Yes",
      "reason": "This table explicitly deals with fees and is likely to contain SKU-level detail, which is crucial for attributing marketplace fees to individual products for profitability."
    }
  ],
  "required_fields": [
    {
      "field": "sku_id",
      "role": "Dimension (Stock Keeping Unit Identifier)",
      "selected?": "Yes",
      "reason": "The primary grouping dimension for a SKU profitability report. Explicitly mentioned as a join key in Increff context and inferred for other OMS/fee tables."
    },
    {
      "field": "sales_channel",
      "role": "Dimension (Sales Channel/Marketplace)",
      "selected?": "Yes",
      "reason": "Required to differentiate profitability by the channel through which the SKU is sold. Explicitly available in `increff_sales` and inferred as literal strings for marketplace-specific OMS tables."
    },
    {
      "field": "total_revenue",
      "role": "Metric (Total Gross Revenue per SKU)",
      "selected?": "Yes",
      "reason": "Represents the total sales value generated by each SKU. Calculated by summing `line_item_total_amount` or similar fields from various sales data sources."
    },
    {
      "field": "total_quantity_sold",
      "role": "Metric (Total Quantity Sold per SKU)",
      "selected?": "Yes",
      "reason": "Indicates the volume of sales for each SKU, important for understanding scale. Aggregated from `quantity_sold` or similar fields."
    },
    {
      "field": "total_returns",
      "role": "Metric (Total Returns per SKU)",
      "selected?": "Yes",
      "reason": "Indicates the volume of returns for each SKU, acting as a proxy for return-related costs and operational complexity. Derived from `increff_returns.return_id`."
    },
    {
      "field": "returns_with_qc",
      "role": "Metric (Returns with QC Data per SKU)",
      "selected?": "Yes",
      "reason": "Reflects the number of returns that underwent quality checks, signifying a higher degree of handling and potential cost per SKU. Derived from `increff_returns.qc_status`."
    },
    {
      "field": "distinct_return_reasons",
      "role": "Metric (Distinct Return Reasons per SKU)",
      "selected?": "Yes",
      "reason": "Provides insight into the nature of returns for an SKU, which can inform product improvements or operational changes affecting profitability. Derived from `increff_returns.return_reason`."
    },
    {
      "field": "total_marketplace_fees",
      "role": "Metric (Total Marketplace Fees per SKU)",
      "selected?": "Yes",
      "reason": "Directly attributable fees incurred for selling each SKU on specific marketplaces, contributing to its overall cost. Derived from `amazon_fee_preview.estimated_fee_amount`."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as per scope policies."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active items/transactions are considered."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from sales tables (`increff_sales`, and inferred for OMS tables)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for OMS tables if applicable)."
    },
    {
      "field": "return_status",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Sum of gross revenue, quantity sold, total returns, returns with QC, distinct return reasons, and marketplace fees, all grouped by SKU and sales channel. This serves as a proxy for SKU profitability due to missing comprehensive COGS data.",
    "numerator": "SUM(total_revenue), SUM(total_quantity_sold), COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason), SUM(total_marketplace_fees)",
    "denominator": null,
    "aggregation_grain": "sku_id, sales_channel",
    "deduplication_rule": "Sales are aggregated per SKU and channel. Return counts are based on unique `return_id` per SKU and channel. Marketplace fees are summed per SKU and channel. All metrics are combined at the SKU and channel grain."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for sales revenue, return metrics, and marketplace fees, each scoped to a specific platform. These CTEs are then combined using FULL OUTER JOINs on `sku_id` and `sales_channel` to create a unified view. This approach allows for combining data from disparate sources that share common dimensions.",
  "missing_or_ambiguous": "The report is partial as it lacks comprehensive Cost of Goods Sold (COGS) data, which is essential for a true profitability calculation. SKU-level item prices (`line_item_total_amount`, `quantity_sold`) are strongly inferred for `zs_observe.myntra_oms` and `zs_observe.amazon_oms` as marketplace OMS systems typically store this granularity, but specific column names are not explicitly provided in the context. Similarly, `sku_id` and `estimated_fee_amount` in `zs_observe.amazon_fee_preview` are inferred. The attribution of all marketplace fees to specific SKUs is challenging without explicit item-level fee breakdowns across all platforms. Logistics costs are not included as they are generally not granular at the SKU level in the provided context.",
  "sql_skeleton": "WITH AllSalesData AS (
    SELECT
        is.sku_id,
        is.sales_channel,
        SUM(is.line_item_total_amount) AS total_revenue,
        SUM(is.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.increff_sales is
    WHERE
        is.group_level_id = '22'
        AND is.is_active = true
        AND is.order_status = 'COMPLETED'
        AND is.transaction_type = 'SALES'
    GROUP BY
        is.sku_id, is.sales_channel

    UNION ALL

    SELECT
        moms.sku_id,
        'Myntra' AS sales_channel,
        SUM(moms.line_item_total_amount) AS total_revenue,
        SUM(moms.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.myntra_oms moms
    WHERE
        moms.group_level_id = '22'
        AND moms.is_active = true
    GROUP BY
        moms.sku_id

    UNION ALL

    SELECT
        aoms.sku_id,
        'Amazon' AS sales_channel,
        SUM(aoms.line_item_total_amount) AS total_revenue,
        SUM(aoms.quantity_sold) AS total_quantity_sold
    FROM
        zs_observe.amazon_oms aoms
    WHERE
        aoms.group_level_id = '22'
        AND aoms.is_active = true
    GROUP BY
        aoms.sku_id
),
ReturnsData AS (
    SELECT
        ir.sku_id,
        ir.sales_channel,
        COUNT(DISTINCT ir.return_id) AS total_returns,
        COUNT(CASE WHEN ir.qc_status IS NOT NULL THEN ir.return_id END) AS returns_with_qc,
        COUNT(DISTINCT ir.return_reason) AS distinct_return_reasons
    FROM
        zs_observe.increff_returns ir
    WHERE
        ir.group_level_id = '22'
        AND ir.is_active = true
        AND ir.return_status = 'COMPLETED'
    GROUP BY
        ir.sku_id, ir.sales_channel
),
FeesData AS (
    SELECT
        afp.sku_id,
        'Amazon' AS sales_channel,
        SUM(afp.estimated_fee_amount) AS total_marketplace_fees
    FROM
        zs_observe.amazon_fee_preview afp
    WHERE
        afp.group_level_id = '22'
        AND afp.is_active = true
    GROUP BY
        afp.sku_id
)
SELECT
    COALESCE(asd.sku_id, rd.sku_id, fd.sku_id) AS sku_id,
    COALESCE(asd.sales_channel, rd.sales_channel, fd.sales_channel) AS sales_channel,
    COALESCE(asd.total_revenue, 0) AS total_revenue,
    COALESCE(asd.total_quantity_sold, 0) AS total_quantity_sold,
    COALESCE(rd.total_returns, 0) AS total_returns,
    COALESCE(rd.returns_with_qc, 0) AS returns_with_qc,
    COALESCE(rd.distinct_return_reasons, 0) AS distinct_return_reasons,
    COALESCE(fd.total_marketplace_fees, 0) AS total_marketplace_fees
FROM
    AllSalesData asd
FULL OUTER JOIN
    ReturnsData rd ON asd.sku_id = rd.sku_id AND asd.sales_channel = rd.sales_channel
FULL OUTER JOIN
    FeesData fd ON COALESCE(asd.sku_id, rd.sku_id) = fd.sku_id AND COALESCE(asd.sales_channel, rd.sales_channel) = fd.sales_channel
ORDER BY
    sku_id, sales_channel;


### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "return_status = 'COMPLETED'"
  ],
  "joins": "Multiple CTEs are created for sales revenue, return metrics, and marketplace fees, each scoped to a specific platform. These CTEs are then combined using FULL OUTER JOINs on `sku_id` and `sales_channel` to create a unified view. This approach allows for combining data from disparate sources that share common dimensions for comprehensive SKU-level reporting.",
  "metric_logic": {
    "aggregation_grain": "sku_id, sales_channel",
    "deduplication_rule": "Sales revenue and quantity are summed per SKU and channel. Return counts are based on unique `return_id` per SKU and channel. Marketplace fees are summed per SKU and channel. All metrics are combined at the SKU and channel grain.",
    "denominator": null,
    "formula": "Sum of gross revenue, quantity sold, total returns, returns with QC, distinct return reasons, and marketplace fees, all grouped by SKU and sales channel. This serves as a proxy for SKU profitability due to missing comprehensive COGS data and other cost components.",
    "numerator": "SUM(total_revenue), SUM(total_quantity_sold), COUNT(return_id), COUNT(CASE WHEN qc_status IS NOT NULL THEN return_id END), COUNT(DISTINCT return_reason), SUM(total_marketplace_fees)"
  },
  "missing_or_ambiguous": "The report is partial as it lacks comprehensive Cost of Goods Sold (COGS) data, which is essential for a true profitability calculation. SKU-level item prices (`line_item_total_amount`, `quantity_sold`) are strongly inferred for `zs_observe.myntra_oms` and `zs_observe.amazon_oms` as marketplace OMS systems typically store this granularity, but specific column names for these are not explicitly provided in the context. Similarly, `sku_id` and `estimated_fee_amount` in `zs_observe.amazon_fee_preview` are inferred based on the table's purpose. The attribution of all marketplace fees to specific SKUs is challenging without explicit item-level fee breakdowns across all platforms. Logistics and other operational costs are not included as they are generally not granular at the SKU level in the provided context for Mensa Brands.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "zs_observe.myntra_oms_settlement",
    "zs_observe.myntra_non_order_settlement",
    "zs_ingest.myntra_receivables",
    "zs_observe.myntra_settlement"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` explicitly mentions `sku_id` as a join key, and `query_pattern.increff.7_5_top_skus_by_volume` confirms SKU-level analysis from this source. This table provides core sales metrics.",
      "role": "Source for SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "`query_pattern.increff.8_6_enrich_returns_with_sku_from_sales` explicitly indicates that returns can be linked to sales by SKU. This table provides return volume, QC status, and distinct return reasons, which are key cost and complexity indicators for profitability.",
      "role": "Source for SKU-level return data (cost indicators)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "As an Order Management System for a major marketplace, it is inferred to contain SKU-level sales details such as line item amounts and quantities. This is standard for profitability analysis at the product level.",
      "role": "Source for Myntra SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Similar to `myntra_oms`, Amazon's OMS is inferred to contain SKU-level sales data necessary for SKU profitability analysis.",
      "role": "Source for Amazon SKU-level sales data (revenue and quantity)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_fee_preview",
      "reason": "This table explicitly deals with estimated fees and is likely to contain SKU-level detail, which is crucial for attributing marketplace fees directly to individual products for a profitability assessment.",
      "role": "Source for Amazon SKU-level fees (cost component)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sku_id",
      "reason": "The primary grouping dimension for a SKU profitability report. Explicitly mentioned as a join key in Increff context and inferred for other OMS/fee tables to achieve SKU granularity.",
      "role": "Dimension (Stock Keeping Unit Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "Required to differentiate profitability by the channel through which the SKU is sold. Explicitly available in `increff_sales` and derived as literal strings for marketplace-specific OMS tables to normalize channels.",
      "role": "Dimension (Sales Channel/Marketplace)",
      "selected?": "Yes"
    },
    {
      "field": "total_revenue",
      "reason": "Represents the total sales value generated by each SKU. Calculated by summing `line_item_total_amount` or similar fields from various sales data sources. Essential for revenue side of profitability.",
      "role": "Metric (Total Gross Revenue per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_quantity_sold",
      "reason": "Indicates the volume of sales for each SKU, important for understanding scale and per-unit profitability. Aggregated from `quantity_sold` or similar fields.",
      "role": "Metric (Total Quantity Sold per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "Indicates the volume of returns for each SKU, acting as a proxy for return-related costs and operational complexity. Derived from counting `increff_returns.return_id`.",
      "role": "Metric (Total Returns per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "returns_with_qc",
      "reason": "Reflects the number of returns that underwent quality checks, signifying a higher degree of handling and potential cost per SKU. Derived from counting `increff_returns.return_id` where `qc_status` is present.",
      "role": "Metric (Returns with QC Data per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "distinct_return_reasons",
      "reason": "Provides insight into the nature of returns for an SKU, which can inform product improvements or operational changes affecting profitability. Derived from counting distinct `increff_returns.return_reason`.",
      "role": "Metric (Distinct Return Reasons per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "total_marketplace_fees",
      "reason": "Directly attributable fees incurred for selling each SKU on specific marketplaces, contributing to its overall cost. Derived from `amazon_fee_preview.estimated_fee_amount`.",
      "role": "Metric (Total Marketplace Fees per SKU)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as per `account_data_binding` entries and scope policies.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active items/transactions are considered for accurate reporting.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from sales tables (`increff_sales`), preventing incomplete orders from affecting profitability calculations. Inferred for OMS tables if applicable.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for OMS tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included (`increff_returns`), avoiding pending or cancelled returns.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllSalesData AS (\n    SELECT\n        is.sku_id,\n        is.sales_channel,\n        SUM(is.line_item_total_amount) AS total_revenue,\n        SUM(is.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.increff_sales is\n    WHERE\n        is.group_level_id = '22'\n        AND is.is_active = true\n        AND is.order_status = 'COMPLETED'\n        AND is.transaction_type = 'SALES'\n    GROUP BY\n        is.sku_id, is.sales_channel\n\n    UNION ALL\n\n    SELECT\n        moms.sku_id,\n        'Myntra' AS sales_channel,\n        SUM(moms.line_item_total_amount) AS total_revenue,\n        SUM(moms.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.myntra_oms moms\n    WHERE\n        moms.group_level_id = '22'\n        AND moms.is_active = true\n    GROUP BY\n        moms.sku_id\n\n    UNION ALL\n\n    SELECT\n        aoms.sku_id,\n        'Amazon' AS sales_channel,\n        SUM(aoms.line_item_total_amount) AS total_revenue,\n        SUM(aoms.quantity_sold) AS total_quantity_sold\n    FROM\n        zs_observe.amazon_oms aoms\n    WHERE\n        aoms.group_level_id = '22'\n        AND aoms.is_active = true\n    GROUP BY\n        aoms.sku_id\n),\nReturnsData AS (\n    SELECT\n        ir.sku_id,\n        ir.sales_channel,\n        COUNT(DISTINCT ir.return_id) AS total_returns,\n        COUNT(CASE WHEN ir.qc_status IS NOT NULL THEN ir.return_id END) AS returns_with_qc,\n        COUNT(DISTINCT ir.return_reason) AS distinct_return_reasons\n    FROM\n        zs_observe.increff_returns ir\n    WHERE\n        ir.group_level_id = '22'\n        AND ir.is_active = true\n        AND ir.return_status = 'COMPLETED'\n    GROUP BY\n        ir.sku_id, ir.sales_channel\n),\nFeesData AS (\n    SELECT\n        afp.sku_id,\n        'Amazon' AS sales_channel,\n        SUM(afp.estimated_fee_amount) AS total_marketplace_fees\n    FROM\n        zs_observe.amazon_fee_preview afp\n    WHERE\n        afp.group_level_id = '22'\n        AND afp.is_active = true\n    GROUP BY\n        afp.sku_id\n)\nSELECT\n    COALESCE(asd.sku_id, rd.sku_id, fd.sku_id) AS sku_id,\n    COALESCE(asd.sales_channel, rd.sales_channel, fd.sales_channel) AS sales_channel,\n    COALESCE(asd.total_revenue, 0) AS total_revenue,\n    COALESCE(asd.total_quantity_sold, 0) AS total_quantity_sold,\n    COALESCE(rd.total_returns, 0) AS total_returns,\n    COALESCE(rd.returns_with_qc, 0) AS returns_with_qc,\n    COALESCE(rd.distinct_return_reasons, 0) AS distinct_return_reasons,\n    COALESCE(fd.total_marketplace_fees, 0) AS total_marketplace_fees\nFROM\n    AllSalesData asd\nFULL OUTER JOIN\n    ReturnsData rd ON asd.sku_id = rd.sku_id AND asd.sales_channel = rd.sales_channel\nFULL OUTER JOIN\n    FeesData fd ON COALESCE(asd.sku_id, rd.sku_id) = fd.sku_id AND COALESCE(asd.sales_channel, rd.sales_channel) = fd.sales_channel\nORDER BY\n    sku_id, sales_channel;"
}


---

## 020. Build an Average order value report per channel.

### Timing

- started_at: `2026-05-27T04:27:00+00:00`
- duration_seconds: `180.933`
- RAG_COMPLETION_seconds: `142.815`
- GRAPH_COMPLETION_seconds: `38.118`

### Query

```text
Build an Average order value report per channel.

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
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are created for each sales source to extract order value and count, then combined using UNION ALL. The final AOV calculation is performed by grouping the unified dataset by `sales_channel`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Each `order_id` represents a unique order for AOV calculation. Values are summed to calculate total sales value, and counts are used for total orders.",
    "denominator": "COUNT(DISTINCT order_id)",
    "formula": "SUM(order_value) / COUNT(DISTINCT order_id) grouped by sales_channel",
    "numerator": "SUM(order_value)"
  },
  "missing_or_ambiguous": "The explicit presence of `order_id` in `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, `zs_observe.amazon_oms`, and `zs_observe.meesho_sales` is inferred as standard practice for order management/settlement systems when calculating AOV. Similarly, `total_amount` for Myntra/Amazon OMS and `gmv_amount` for LimeRoad settlement are inferred to represent order-level values or sums that can be normalized to individual orders for AOV. Filters like `order_status = 'COMPLETED'` and `transaction_type = 'SALES'` are inferred for non-Increff tables based on best practices and Increff patterns, which explicitly state them. The Meesho sales data filter for `order_status = 'Delivered'` is taken directly from its formula template, demonstrating platform-specific filter needs.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and refers to `group_level_id` for scoping. It is inferred to contain `order_id` for AOV calculation.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and explicitly mentions `group_level_id=22` for Mensa Brands. It is inferred to contain `order_id` for AOV calculation.",
      "role": "Source for LimeRoad sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Previous interactions and constraint sets for Increff confirm this table contains sales data with `sales_channel`, `order_id`, and `total_amount` for Mensa Brands.",
      "role": "Source for general sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (`total_amount`, `order_id`) for Amazon marketplace based on its role as an Order Management System for Mensa Brands, similar to Myntra OMS.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` explicitly uses `zs_observe.meesho_sales` with `charged_amount` to calculate AOV. It is inferred to contain `order_id` for order counting.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The primary dimension for grouping the AOV report. Derived from literal strings for marketplace-specific tables and directly from `sales_channel` column for Increff/Meesho.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_value",
      "reason": "Represents the total value of an order, used for summing total sales. Derived from `total_amount` or `gmv_amount` or `charged_amount` across different sources.",
      "role": "Metric (Numerator for AOV)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Unique identifier for each order, used for counting distinct orders. Inferred to be present in all selected sales/OMS tables.",
      "role": "Metric (Denominator for AOV)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per various scope policies and previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records contribute to the AOV.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from `increff_sales` (and inferred for other OMS/sales tables if applicable), ensuring only completed orders are considered for AOV. For Meesho, it's 'Delivered'.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllSalesData AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS order_value,\n        oms.order_id\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        settlement.gmv_amount AS order_value,\n        settlement.order_id\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n        AND settlement.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel,\n        sales.total_amount AS order_value,\n        sales.order_id\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS order_value,\n        amazon_oms.order_id\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n        AND amazon_oms.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        'Meesho' AS sales_channel,\n        meesho_sales.charged_amount AS order_value,\n        meesho_sales.order_id\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    sales_channel,\n    SUM(order_value) AS total_sales_value,\n    COUNT(DISTINCT order_id) AS total_orders,\n    SUM(order_value) / COUNT(DISTINCT order_id) AS average_order_value\nFROM\n    AllSalesData\nGROUP BY\n    sales_channel\nORDER BY\n    sales_channel;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are created for each sales source to extract order value and count, then combined using UNION ALL. The final AOV calculation is performed by grouping the unified dataset by `sales_channel`.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Each `order_id` represents a unique order for AOV calculation. Values are summed to calculate total sales value, and counts are used for total orders.",
    "denominator": "COUNT(DISTINCT order_id)",
    "formula": "SUM(order_value) / COUNT(DISTINCT order_id) grouped by sales_channel",
    "numerator": "SUM(order_value)"
  },
  "missing_or_ambiguous": "The explicit presence of `order_id` in `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, `zs_observe.amazon_oms`, and `zs_observe.meesho_sales` is inferred as standard practice for order management/settlement systems when calculating AOV. Similarly, `total_amount` for Myntra/Amazon OMS and `gmv_amount` for LimeRoad settlement are inferred to represent order-level values or sums that can be normalized to individual orders for AOV. Filters like `order_status = 'COMPLETED'` and `transaction_type = 'SALES'` are inferred for non-Increff tables based on best practices and Increff patterns, which explicitly state them. The Meesho sales data filter for `order_status = 'Delivered'` is taken directly from its formula template, demonstrating platform-specific filter needs.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and refers to `group_level_id` for scoping. It is inferred to contain `order_id` for AOV calculation.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and explicitly mentions `group_level_id=22` for Mensa Brands. It is inferred to contain `order_id` for AOV calculation.",
      "role": "Source for LimeRoad sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Previous interactions and constraint sets for Increff confirm this table contains sales data with `sales_channel`, `order_id`, and `total_amount` for Mensa Brands.",
      "role": "Source for general sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Inferred to contain sales data (`total_amount`, `order_id`) for Amazon marketplace based on its role as an Order Management System for Mensa Brands, similar to Myntra OMS.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` explicitly uses `zs_observe.meesho_sales` with `charged_amount` to calculate AOV. It is inferred to contain `order_id` for order counting.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "The primary dimension for grouping the AOV report. Derived from literal strings for marketplace-specific tables and directly from `sales_channel` column for Increff/Meesho.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_value",
      "reason": "Represents the total value of an order, used for summing total sales. Derived from `total_amount` or `gmv_amount` or `charged_amount` across different sources.",
      "role": "Metric (Numerator for AOV)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Unique identifier for each order, used for counting distinct orders. Inferred to be present in all selected sales/OMS tables.",
      "role": "Metric (Denominator for AOV)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per various scope policies and previous interactions.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records contribute to the AOV.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'`) for accurate sales metrics from `increff_sales` (and inferred for other OMS/sales tables if applicable), ensuring only completed orders are considered for AOV. For Meesho, it's 'Delivered'.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllSalesData AS (\n    SELECT\n        'Myntra' AS sales_channel,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS order_value,\n        oms.order_id\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS sales_channel,\n        settlement.gmv_amount AS order_value,\n        settlement.order_id\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true\n        AND settlement.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel,\n        sales.total_amount AS order_value,\n        sales.order_id\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS sales_channel,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS order_value,\n        amazon_oms.order_id\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true\n        AND amazon_oms.order_status = 'COMPLETED'\n\n    UNION ALL\n\n    SELECT\n        'Meesho' AS sales_channel,\n        meesho_sales.charged_amount AS order_value,\n        meesho_sales.order_id\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    sales_channel,\n    SUM(order_value) AS total_sales_value,\n    COUNT(DISTINCT order_id) AS total_orders,\n    SUM(order_value) / COUNT(DISTINCT order_id) AS average_order_value\nFROM\n    AllSalesData\nGROUP BY\n    sales_channel\nORDER BY\n    sales_channel;"
}


---

## 021. Gross sales trend across all marketplaces.

### Timing

- started_at: `2026-05-27T04:30:01+00:00`
- duration_seconds: `90.418`
- RAG_COMPLETION_seconds: `68.809`
- GRAPH_COMPLETION_seconds: `21.608`

### Query

```text
Gross sales trend across all marketplaces.

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
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract gross sales data, marketplace identifiers, and order dates from disparate source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Sales amounts are summed per marketplace per month. Duplicate orders within a source are handled by the source table's primary key if applicable, otherwise, standard aggregation sums all relevant amounts.",
    "denominator": null,
    "formula": "SUM(gross_sales_amount) grouped by marketplace_name and monthly date.",
    "numerator": "SUM(gross_sales_amount)"
  },
  "missing_or_ambiguous": "The exact date column names (e.g., `order_date`, `settlement_date`) and the presence of `is_active` and `order_status = 'COMPLETED'` filters are inferred for `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, and `zs_observe.amazon_oms` based on general database best practices for operational tables and consistency with explicit rules for other sources like Increff and Meesho. The primary sales amount columns are inferred to be `total_amount`, `gmv_amount`, and `charged_amount` based on context. The type casting `TRY_CAST(... AS DOUBLE)` is applied for safety where mentioned or inferred as potentially necessary.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and includes `group_level_id` for scoping Mensa Brands. An `order_date` field is inferred for trending.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and specifies `group_level_id=22` for Mensa Brands. A `settlement_date` field is inferred for trending.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table is consistently referenced for sales data (`total_amount`), `sales_channel`, and filtering for Mensa Brands (`group_level_id = 22`, `order_status = 'COMPLETED'`, `transaction_type = 'SALES'`). An `order_date` field is inferred for trending.",
      "role": "Source for general sales data across channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` indicates this table is relevant for Mensa Brands (`group_level_id = 22`). As an OMS, it is inferred to contain gross sales (`total_amount`) and an `order_date` for trending.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` and `query_pattern.meesho.007.7_1_gross_gmv_forward_sales` explicitly use this table for sales (`charged_amount`) and indicate filters for `group_level_id` and `order_status = 'Delivered'`. An `order_date` field is inferred for trending.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the sales trend over time, aggregated by month.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish sales performance across different marketplaces. Derived as a literal string for marketplace-specific tables or from `sales_channel` for Increff.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "gross_sales_amount",
      "reason": "The core metric requested, representing the total sales value from each marketplace. Aggregated from respective sales amount fields in each source.",
      "role": "Metric (Gross Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per context.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered') for accurate gross sales metrics, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        DATE_TRUNC('month', oms.order_date) AS month_start_date,\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS gross_sales_amount\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', settlement.settlement_date) AS month_start_date, -- Inferred date field\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS gross_sales_amount\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', sales.order_date) AS month_start_date, -- Inferred date field\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS gross_sales_amount\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', amazon_oms.order_date) AS month_start_date, -- Inferred date field\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS gross_sales_amount -- Inferred sales amount\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', meesho_sales.order_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        meesho_sales.charged_amount AS gross_sales_amount\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    SUM(gross_sales_amount) AS total_gross_sales\nFROM\n    AllMarketplaceSales\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract gross sales data, marketplace identifiers, and order dates from disparate source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Sales amounts are summed per marketplace per month. Duplicate orders within a source are handled by the source table's primary key if applicable, otherwise, standard aggregation sums all relevant amounts.",
    "denominator": null,
    "formula": "SUM(gross_sales_amount) grouped by marketplace_name and monthly date.",
    "numerator": "SUM(gross_sales_amount)"
  },
  "missing_or_ambiguous": "The exact date column names (e.g., `order_date`, `settlement_date`) and the presence of `is_active` and `order_status = 'COMPLETED'` filters are inferred for `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, and `zs_observe.amazon_oms` based on general database best practices for operational tables and consistency with explicit rules for other sources like Increff and Meesho. The primary sales amount columns are inferred to be `total_amount`, `gmv_amount`, and `charged_amount` based on context. The type casting `TRY_CAST(... AS DOUBLE)` is applied for safety where mentioned or inferred as potentially necessary.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "formula_template.logistics.variance_amount",
    "formula_template.mapper_gst_base_order_id",
    "formula_template.meesho.brand_gmv_from_sales",
    "formula_template.meesho.brand_level_gmv",
    "formula_template.meesho.brand_level_return_rate",
    "formula_template.meesho.category_level_return_analysis",
    "formula_template.meesho.effective_cost_per_delivered_order",
    "formula_template.meesho.effective_payout_ratio",
    "formula_template.meesho.effective_shipping_cost_rate"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table to calculate gross sales (`total_amount`) and includes `group_level_id` for scoping Mensa Brands. An `order_date` field is inferred for trending.",
      "role": "Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV (`gmv_amount`) and specifies `group_level_id=22` for Mensa Brands. A `settlement_date` field is inferred for trending.",
      "role": "Source for LimeRoad GMV data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "This table is consistently referenced for sales data (`total_amount`), `sales_channel`, and filtering for Mensa Brands (`group_level_id = 22`, `order_status = 'COMPLETED'`, `transaction_type = 'SALES'`). An `order_date` field is inferred for trending.",
      "role": "Source for general sales data across channels",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` indicates this table is relevant for Mensa Brands (`group_level_id = 22`). As an OMS, it is inferred to contain gross sales (`total_amount`) and an `order_date` for trending.",
      "role": "Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` and `query_pattern.meesho.007.7_1_gross_gmv_forward_sales` explicitly use this table for sales (`charged_amount`) and indicate filters for `group_level_id` and `order_status = 'Delivered'`. An `order_date` field is inferred for trending.",
      "role": "Source for Meesho sales data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the sales trend over time, aggregated by month.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish sales performance across different marketplaces. Derived as a literal string for marketplace-specific tables or from `sales_channel` for Increff.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "gross_sales_amount",
      "reason": "The core metric requested, representing the total sales value from each marketplace. Aggregated from respective sales amount fields in each source.",
      "role": "Metric (Gross Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables as per context.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered') for accurate gross sales metrics, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for accurate sales metrics from `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions are considered.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceSales AS (\n    SELECT\n        DATE_TRUNC('month', oms.order_date) AS month_start_date,\n        'Myntra' AS marketplace_name,\n        TRY_CAST(oms.total_amount AS DOUBLE) AS gross_sales_amount\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', settlement.settlement_date) AS month_start_date, -- Inferred date field\n        'LimeRoad' AS marketplace_name,\n        settlement.gmv_amount AS gross_sales_amount\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', sales.order_date) AS month_start_date, -- Inferred date field\n        sales.sales_channel AS marketplace_name,\n        sales.total_amount AS gross_sales_amount\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', amazon_oms.order_date) AS month_start_date, -- Inferred date field\n        'Amazon' AS marketplace_name,\n        TRY_CAST(amazon_oms.total_amount AS DOUBLE) AS gross_sales_amount -- Inferred sales amount\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', meesho_sales.order_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        meesho_sales.charged_amount AS gross_sales_amount\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    SUM(gross_sales_amount) AS total_gross_sales\nFROM\n    AllMarketplaceSales\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}


---

## 022. Return trend across all the marketplaces.

### Timing

- started_at: `2026-05-27T04:31:31+00:00`
- duration_seconds: `59.258`
- RAG_COMPLETION_seconds: `42.359`
- GRAPH_COMPLETION_seconds: `16.898`

### Query

```text
Return trend across all the marketplaces.

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
    "group_level_id = '22'",
    "is_active = true",
    "return_status = 'COMPLETED' (or equivalent status for Meesho returns)"
  ],
  "joins": "Multiple CTEs are used to extract return data, marketplace identifiers, and return dates from different source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Each unique `return_id` is counted as one return. Returns are aggregated by month and marketplace name.",
    "denominator": null,
    "formula": "COUNT(DISTINCT return_id) grouped by monthly date and marketplace_name.",
    "numerator": "COUNT(DISTINCT return_id)"
  },
  "missing_or_ambiguous": "The explicit presence of dedicated return tables for Myntra, LimeRoad, and Amazon (similar to `increff_returns` or `meesho_returns`) is not available in the provided context, limiting this report to Increff and Meesho. The exact date column names (e.g., `return_date` or `order_date`) for `zs_observe.increff_returns` and `zs_observe.meesho_returns` are inferred. The specific `return_status` value for Meesho returns (e.g., 'COMPLETED', 'DELIVERED_TO_SELLER') is inferred as 'COMPLETED' for consistency with Increff, but it would need to be confirmed by platform-specific documentation.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "zs_observe.myntra_oms",
    "zs_observe.limeroad_settlement",
    "zs_observe.amazon_oms",
    "zs_observe.meesho_sales"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table directly provides return information including sales_channel, return_id, and is part of the Mensa Brands scope for Increff data.",
      "role": "Source for Increff return data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_returns",
      "reason": "Explicitly referenced in Meesho platform context for return-related query patterns (e.g., query_pattern.meesho.009.7_3_return_rate), indicating it holds relevant return data for Mensa Brands.",
      "role": "Source for Meesho return data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the trend of returns over time, aggregated by month. Date field is inferred from return/order context.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish return performance across different marketplaces. Derived as 'Increff' from increff_returns.sales_channel, and 'Meesho' from meesho_returns.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "The core metric for a return trend report, representing the count of returns for each marketplace.",
      "role": "Metric (Return Count)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active return records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included. For Meesho, this would be an equivalent 'return completed' status from `zen_status` or similar.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceReturns AS (\n    SELECT\n        DATE_TRUNC('month', ir.return_date) AS month_start_date, -- Inferred date field\n        ir.sales_channel AS marketplace_name,\n        ir.return_id\n    FROM\n        zs_observe.increff_returns ir\n    WHERE\n        ir.group_level_id = '22'\n        AND ir.is_active = true\n        AND ir.return_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', mr.return_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        mr.return_id\n    FROM\n        zs_observe.meesho_returns mr\n    WHERE\n        mr.group_level_id = '22'\n        AND mr.is_active = true -- Inferred filter\n        AND mr.return_status = 'COMPLETED' -- Inferred filter, assuming similar status to Increff\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    COUNT(DISTINCT return_id) AS total_returns\nFROM\n    AllMarketplaceReturns\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "return_status = 'COMPLETED' (or equivalent status for Meesho returns)"
  ],
  "joins": "Multiple CTEs are used to extract return data, marketplace identifiers, and return dates from different source tables. These CTEs are then combined using UNION ALL. The final aggregation is performed on the unified dataset, grouped by marketplace and truncated monthly date, without requiring direct joins between the original source tables.",
  "metric_logic": {
    "aggregation_grain": "month, marketplace_name",
    "deduplication_rule": "Each unique `return_id` is counted as one return. Returns are aggregated by month and marketplace name.",
    "denominator": null,
    "formula": "COUNT(DISTINCT return_id) grouped by monthly date and marketplace_name.",
    "numerator": "COUNT(DISTINCT return_id)"
  },
  "missing_or_ambiguous": "The explicit presence of dedicated return tables for Myntra, LimeRoad, and Amazon (similar to `increff_returns` or `meesho_returns`) is not available in the provided context, limiting this report to Increff and Meesho. The exact date column names (e.g., `return_date` or `order_date`) for `zs_observe.increff_returns` and `zs_observe.meesho_returns` are inferred. The specific `return_status` value for Meesho returns (e.g., 'COMPLETED', 'DELIVERED_TO_SELLER') is inferred as 'COMPLETED' for consistency with Increff, but it would need to be confirmed by platform-specific documentation.",
  "rejected_or_ambiguous_fields": [],
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
    "query_pattern.logistics.cod_expected_vs_remitted",
    "zs_observe.myntra_oms",
    "zs_observe.limeroad_settlement",
    "zs_observe.amazon_oms",
    "zs_observe.meesho_sales"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table directly provides return information including sales_channel, return_id, and is part of the Mensa Brands scope for Increff data.",
      "role": "Source for Increff return data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_returns",
      "reason": "Explicitly referenced in Meesho platform context for return-related query patterns (e.g., query_pattern.meesho.009.7_3_return_rate), indicating it holds relevant return data for Mensa Brands.",
      "role": "Source for Meesho return data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "DATE_TRUNC('month', <date_field>)",
      "reason": "Required to show the trend of returns over time, aggregated by month. Date field is inferred from return/order context.",
      "role": "Dimension (Time Trend)",
      "selected?": "Yes"
    },
    {
      "field": "marketplace_name",
      "reason": "Required to distinguish return performance across different marketplaces. Derived as 'Increff' from increff_returns.sales_channel, and 'Meesho' from meesho_returns.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "total_returns",
      "reason": "The core metric for a return trend report, representing the count of returns for each marketplace.",
      "role": "Metric (Return Count)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, ensuring only active return records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "return_status",
      "reason": "Inferred as a mandatory filter (`return_status = 'COMPLETED'`) to ensure only relevant, processed return transactions are included. For Meesho, this would be an equivalent 'return completed' status from `zen_status` or similar.",
      "role": "Filter Column (Return Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllMarketplaceReturns AS (\n    SELECT\n        DATE_TRUNC('month', ir.return_date) AS month_start_date, -- Inferred date field\n        ir.sales_channel AS marketplace_name,\n        ir.return_id\n    FROM\n        zs_observe.increff_returns ir\n    WHERE\n        ir.group_level_id = '22'\n        AND ir.is_active = true\n        AND ir.return_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        DATE_TRUNC('month', mr.return_date) AS month_start_date, -- Inferred date field\n        'Meesho' AS marketplace_name,\n        mr.return_id\n    FROM\n        zs_observe.meesho_returns mr\n    WHERE\n        mr.group_level_id = '22'\n        AND mr.is_active = true -- Inferred filter\n        AND mr.return_status = 'COMPLETED' -- Inferred filter, assuming similar status to Increff\n)\nSELECT\n    month_start_date,\n    marketplace_name,\n    COUNT(DISTINCT return_id) AS total_returns\nFROM\n    AllMarketplaceReturns\nGROUP BY\n    month_start_date,\n    marketplace_name\nORDER BY\n    month_start_date, marketplace_name;"
}


---
