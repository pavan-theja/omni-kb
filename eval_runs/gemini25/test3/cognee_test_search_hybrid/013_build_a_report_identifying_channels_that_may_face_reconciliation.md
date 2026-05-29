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
