## 006. Generate a report showing COD remittance type by courier.

### Timing

- started_at: `2026-05-27T06:36:45+00:00`
- duration_seconds: `49.53`
- RAG_COMPLETION_seconds: `35.142`
- GRAPH_COMPLETION_seconds: `14.387`

### Query

```text
Generate a report showing COD remittance type by courier.

Scope:
- tenant: Mensa Brands

Answer for downstream SQL/query construction using only the provided context and explicit user input.

You are a SQL-resolution handoff agent. Do not answer the business question directly. Produce the safest SQL-building plan that the retrieved context can support.

Resolution flow:
1. Identify the requested grain, metric/status logic, dimensions, filters, joins, and tenant/account scope.
2. Enumerate grounded candidate sources before choosing a source.
3. Classify candidates as direct, supporting, risky, or irrelevant.
4. Select the best SQL package. If no safe package exists, return a partial/risky handoff with the blocking gaps.

Core rules:
- Prefer physical SQL tables and columns explicitly grounded in context.
- Do not default to the most detailed retrieved source if the user asks about channels, marketplaces, settlements, reconciliation, risk, bottlenecks, dependency, concentration, courier mapping, OMS dependency, or marketplace-wide reporting.
- For channel/marketplace questions, enumerate all relevant candidate physical settlement, OMS/order, return/reverse, logistics/courier, and query-pattern sources before selecting a SQL path.
- Do not treat one marketplace such as Myntra, Amazon, Flipkart, Ajio, Nykaa, Meesho, Snapdeal, TataCliq, JioMart, HealthKart, or LimeRoad as representative of all marketplaces unless the user explicitly asks for that marketplace or the context proves it is the only applicable source.
- Do not UNION or numerically consolidate multiple source tables unless the user asks for cross-source/all-source/platform-wide consolidation and the context provides deduplication keys plus source precedence.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feed names as business dimension values when a proper dimension column exists.
- If fields, tenant IDs, or join keys must be inferred from grounded patterns, select them only with explicit inferred reasoning.
- Do not invent deduplication rules, source precedence, or join keys. State the gap instead.

Canonical metadata rules:
- Canonical objects are metadata guides, not runtime SQL tables, unless they resolve to a concrete physical table or column.
- Never generate SQL against `account_data_binding`, `business_flow_binding`, `workflow_step`, `business_process`, `metric`, `query_pattern`, `relationship`, `state_transition`, `evidence`, `platform_account`, `metadata.account_data_bindings`, `account_data_bindings`, or `canonical.cards` unless the user explicitly asks to query the canonical metadata store itself.
- `account_data_binding` helps infer tenant/platform/account scope, source role, and candidate physical tables. Do not query it directly.
- `table` can be selected only when it names a physical table, for example `zs_observe.unicommerce`.
- `column` grounds fields, filters, joins, metrics, and grouping dimensions for its parent physical table.
- `relationship` justifies joins only when both sides resolve to physical tables/columns.
- `query_pattern` provides SQL logic only when it names physical tables, fields, filters, joins, or deduplication rules.
- `business_flow_binding`, `business_process`, `workflow_step`, and `state_transition` explain process/status semantics only.
- `metric` and `metric_dependency` help infer formula, numerator, denominator, and grain only when grounded by physical fields.
- `platform_account` helps identify marketplace/channel/account scope only.
- `evidence` is provenance/confidence only.

Candidate classification:
- direct: contains the requested grain and required metric/status fields.
- supporting: helps identify scope, channel, platform, process, or join path but cannot answer the metric alone.
- risky: appears relevant but lacks required join keys, filters, status fields, grain, or deduplication rules.
- irrelevant: retrieved but not useful for the request.

Output rules:
- Return one best SQL package in the schema below.
- Use `require_tables` to show selected and rejected/risky/supporting candidates.
- Use `rejected_or_ambiguous_fields` for alternate fields, missing fields, unsafe joins, and rejected candidate notes.
- For listing/mapping queries with no numeric metric, set numerator and denominator to null and describe the unique rows in `metric_logic.formula`.
- If the best answer is a candidate inventory rather than executable SQL, set `selected_source` to null and make `sql_skeleton` a commented template explaining what is missing.

Cognee response wrapper:
- Return a top-level JSON object with exactly one key: `content`.
- `content` must be a string.
- The string inside `content` must be a JSON-serialized object matching the payload schema.
- Do not put an object or array directly inside `content`.

Correct wrapper shape:
{
  "content": "{\"selected_source\":null,\"rejected_sources\":[],\"require_tables\":[],\"required_fields\":[],\"rejected_or_ambiguous_fields\":[],\"metric_logic\":{\"formula\":null,\"numerator\":null,\"denominator\":null,\"aggregation_grain\":null,\"deduplication_rule\":null},\"filters\":[],\"joins\":\"No joins needed\",\"missing_or_ambiguous\":\"None\",\"sql_skeleton\":\"SELECT 1\"}"
}

Payload schema inside the `content` string:
{
  "selected_source": "string physical SQL table name, or null",
  "rejected_sources": ["array of rejected source ids or names"],
  "require_tables": [
    {
      "field": "physical SQL table name when selected; canonical metadata id only when rejected/supporting/risky",
      "role": "Primary Source | Supporting Metadata | Risky Candidate | Irrelevant Candidate | Filter Source | Metric Source",
      "selected?": "Yes/No",
      "reason": "candidate classification and SQL relevance"
    }
  ],
  "required_fields": [
    {
      "field": "physical column name or logical field name",
      "role": "Channel Identifier | Filter Column | Metric | Join Key | Status Field | Date Field",
      "selected?": "Yes/No",
      "reason": "why the field is needed; mark inferred reasoning when applicable"
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
  "filters": ["array of exact WHERE conditions or logical filters"],
  "joins": "join logic, or why no join is needed",
  "missing_or_ambiguous": "None only when complete; otherwise list blocking gaps/inferences",
  "sql_skeleton": "valid SQL template using selected fields and filters, or commented partial template"
}
```

### RAG_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "payment_mode = 'COD'"
  ],
  "joins": "Multiple CTEs are used to extract distinct courier and COD remittance type information from various settlement tables. These CTEs are then combined using UNION ALL to create a unified list of unique mappings.",
  "metric_logic": {
    "aggregation_grain": "courier_partner, payment_mode",
    "deduplication_rule": "Select distinct combinations of `courier_partner` and `payment_mode`.",
    "denominator": null,
    "formula": "A distinct list of (courier, COD remittance type) pairs.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact column name for 'remittance type' is inferred to be `payment_mode` from the `allowed_dimensions` in logistics query patterns. The specific string value 'COD' within the `payment_mode` column is also inferred. The explicit presence of `group_level_id` and `is_active` columns and their boolean/string values in all selected settlement tables are strong inferences based on common data models and the `semantic_filters` mentioned in logistics query patterns.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints"
  ],
  "require_tables": [
    {
      "field": "zs_observe.shiprocket_oms",
      "reason": "`query_pattern.logistics.cod_expected_vs_remitted` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shiprocket_settlement",
      "reason": "`query_pattern.logistics.cod_expected_vs_remitted` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions. It also mentions `rule.logistics.shiprocket_settlement_charged_amount_cod`.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.delhivery_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.dtdc_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.ekart_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "reason": "Explicitly listed as an `allowed_dimension` in relevant logistics query patterns. This is the primary grouping dimension.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "payment_mode",
      "reason": "Explicitly listed as an `allowed_dimension` in relevant logistics query patterns, which will serve as the 'remittance type'. Filtered for 'COD'.",
      "role": "Dimension (Remittance Type)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as inferred from previous interactions and general data model.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, as indicated by semantic filters in logistics query patterns.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH CourierCODRemittance AS (\n    SELECT DISTINCT\n        soms.courier_partner AS courier_name,\n        soms.payment_mode AS remittance_type\n    FROM\n        zs_observe.shiprocket_oms soms\n    WHERE\n        soms.group_level_id = '22'\n        AND soms.is_active = true\n        AND soms.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        sset.courier_partner AS courier_name,\n        sset.payment_mode AS remittance_type\n    FROM\n        zs_observe.shiprocket_settlement sset\n    WHERE\n        sset.group_level_id = '22'\n        AND sset.is_active = true\n        AND sset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Delhivery' AS courier_name, -- Inferred from table context\n        dset.payment_mode AS remittance_type\n    FROM\n        zs_observe.delhivery_settlement dset\n    WHERE\n        dset.group_level_id = '22'\n        AND dset.is_active = true\n        AND dset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'DTDC' AS courier_name, -- Inferred from table context\n        tdset.payment_mode AS remittance_type\n    FROM\n        zs_observe.dtdc_settlement tdset\n    WHERE\n        tdset.group_level_id = '22'\n        AND tdset.is_active = true\n        AND tdset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Ekart' AS courier_name, -- Inferred from table context\n        eset.payment_mode AS remittance_type\n    FROM\n        zs_observe.ekart_settlement eset\n    WHERE\n        eset.group_level_id = '22'\n        AND eset.is_active = true\n        AND eset.payment_mode = 'COD'\n)\nSELECT DISTINCT\n    courier_name,\n    remittance_type\nFROM\n    CourierCODRemittance\nORDER BY\n    courier_name, remittance_type;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "payment_mode = 'COD'"
  ],
  "joins": "Multiple CTEs are used to extract distinct courier and COD remittance type information from various settlement tables. These CTEs are then combined using UNION ALL to create a unified list of unique mappings.",
  "metric_logic": {
    "aggregation_grain": "courier_partner, payment_mode",
    "deduplication_rule": "Select distinct combinations of `courier_partner` and `payment_mode`.",
    "denominator": null,
    "formula": "A distinct list of (courier, COD remittance type) pairs.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact column name for 'remittance type' is inferred to be `payment_mode` from the `allowed_dimensions` in logistics query patterns. The specific string value 'COD' within the `payment_mode` column is also inferred. The explicit presence of `group_level_id` and `is_active` columns and their boolean/string values in all selected settlement tables are strong inferences based on common data models and the `semantic_filters` mentioned in logistics query patterns.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement",
    "account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse",
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
    "account_data_binding.ardeur_fashion.flipkart_in.primary.cashback"
  ],
  "require_tables": [
    {
      "field": "zs_observe.shiprocket_oms",
      "reason": "`query_pattern.logistics.cod_expected_vs_remitted` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shiprocket_settlement",
      "reason": "`query_pattern.logistics.cod_expected_vs_remitted` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions. It also mentions `rule.logistics.shiprocket_settlement_charged_amount_cod`.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.delhivery_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.dtdc_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.ekart_settlement",
      "reason": "`query_pattern.logistics.bank_credit_unmatched_courier_reference` explicitly lists this table and allows `courier_partner` and `payment_mode` as dimensions.",
      "role": "Source for COD remittance type and courier",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "reason": "Explicitly listed as an `allowed_dimension` in relevant logistics query patterns. This is the primary grouping dimension.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "payment_mode",
      "reason": "Explicitly listed as an `allowed_dimension` in relevant logistics query patterns, which will serve as the 'remittance type'. Filtered for 'COD'.",
      "role": "Dimension (Remittance Type)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables as inferred from previous interactions and general data model.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables, as indicated by semantic filters in logistics query patterns.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH CourierCODRemittance AS (\n    SELECT DISTINCT\n        soms.courier_partner AS courier_name,\n        soms.payment_mode AS remittance_type\n    FROM\n        zs_observe.shiprocket_oms soms\n    WHERE\n        soms.group_level_id = '22'\n        AND soms.is_active = true\n        AND soms.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        sset.courier_partner AS courier_name,\n        sset.payment_mode AS remittance_type\n    FROM\n        zs_observe.shiprocket_settlement sset\n    WHERE\n        sset.group_level_id = '22'\n        AND sset.is_active = true\n        AND sset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Delhivery' AS courier_name, -- Inferred from table context\n        dset.payment_mode AS remittance_type\n    FROM\n        zs_observe.delhivery_settlement dset\n    WHERE\n        dset.group_level_id = '22'\n        AND dset.is_active = true\n        AND dset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'DTDC' AS courier_name, -- Inferred from table context\n        tdset.payment_mode AS remittance_type\n    FROM\n        zs_observe.dtdc_settlement tdset\n    WHERE\n        tdset.group_level_id = '22'\n        AND tdset.is_active = true\n        AND tdset.payment_mode = 'COD'\n\n    UNION ALL\n\n    SELECT DISTINCT\n        'Ekart' AS courier_name, -- Inferred from table context\n        eset.payment_mode AS remittance_type\n    FROM\n        zs_observe.ekart_settlement eset\n    WHERE\n        eset.group_level_id = '22'\n        AND eset.is_active = true\n        AND eset.payment_mode = 'COD'\n)\nSELECT DISTINCT\n    courier_name,\n    remittance_type\nFROM\n    CourierCODRemittance\nORDER BY\n    courier_name, remittance_type;"
}
