## 008. Generate a summary report of OMS systems and their connected marketplaces.

### Timing

- started_at: `2026-05-27T06:38:39+00:00`
- duration_seconds: `58.491`
- RAG_COMPLETION_seconds: `27.767`
- GRAPH_COMPLETION_seconds: `30.723`

### Query

```text
Generate a summary report of OMS systems and their connected marketplaces.

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
    "is_active = true"
  ],
  "joins": "Multiple CTEs are used to extract OMS system and marketplace information from various source tables. These CTEs are then combined using UNION ALL to create a unified list of unique mappings.",
  "metric_logic": {
    "aggregation_grain": "oms_system_name, connected_marketplace",
    "deduplication_rule": "Distinct pairs of OMS system name and connected marketplace.",
    "denominator": null,
    "formula": "A distinct list of OMS systems and their connected marketplaces/channels for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact presence and naming of an `is_active` column in `zs_observe.amazon_oms` and `zs_observe.myntra_oms` are inferred based on common data modeling practices and the explicit mention of `is_active` filters for Myntra data. The identification of 'OMS systems' relies on tables explicitly named `*_oms` or known to be OMS systems (like Unicommerce) and their primary purpose as inferred from context.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
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
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report"
  ],
  "require_tables": [
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Explicitly identified as an OMS table for Mensa Brands via `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Primary Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Inferred as an OMS table for Mensa Brands through `query_pattern.myntra.gross_sales_oms` which uses this table and has client-specific filtering logic.",
      "role": "Primary Source for Myntra OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Identified as an OMS system for Mensa Brands from previous questions, containing `sales_channel` to list connected marketplaces.",
      "role": "Primary Source for Unicommerce OMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, supported by patterns in other query patterns (e.g., Myntra).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "Used in `zs_observe.unicommerce` to identify distinct connected marketplaces.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "oms_system_name",
      "reason": "Literal string to represent the OMS system (e.g., 'Amazon OMS', 'Myntra OMS', 'Unicommerce OMS').",
      "role": "Dimension (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "connected_marketplace",
      "reason": "Literal string for direct OMS-to-marketplace mappings (e.g., 'Amazon', 'Myntra') or derived from `sales_channel` for Unicommerce.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH OMSSystemsAndMarketplaces AS (\n    -- Amazon OMS\n    SELECT DISTINCT\n        'Amazon OMS' AS oms_system_name,\n        'Amazon' AS connected_marketplace\n    FROM\n        zs_observe.amazon_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n\n    UNION ALL\n\n    -- Myntra OMS\n    SELECT DISTINCT\n        'Myntra OMS' AS oms_system_name,\n        'Myntra' AS connected_marketplace\n    FROM\n        zs_observe.myntra_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n\n    UNION ALL\n\n    -- Unicommerce OMS and its various sales channels (marketplaces)\n    SELECT DISTINCT\n        'Unicommerce OMS' AS oms_system_name,\n        sales_channel AS connected_marketplace\n    FROM\n        zs_observe.unicommerce\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n)\nSELECT\n    oms_system_name,\n    connected_marketplace\nFROM\n    OMSSystemsAndMarketplaces\nWHERE connected_marketplace IS NOT NULL\nORDER BY\n    oms_system_name, connected_marketplace;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "Multiple CTEs are used to extract OMS system and marketplace information from various source tables. These CTEs are then combined using UNION ALL to create a unified list of unique mappings.",
  "metric_logic": {
    "aggregation_grain": "oms_system_name, connected_marketplace",
    "deduplication_rule": "Distinct pairs of OMS system name and connected marketplace.",
    "denominator": null,
    "formula": "A distinct list of OMS systems and their connected marketplaces/channels for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact presence and naming of an `is_active` column in `zs_observe.amazon_oms`, `zs_observe.myntra_oms`, `zs_observe.increff_sales`, and `zs_observe.shopify_oms` are inferred based on common data modeling practices and the explicit mention of `is_active` filters for Myntra data. The presence of a `sales_channel` column in `zs_observe.increff_sales` is also inferred based on its role as an OMS/WMS for cross-channel operations. The exact string values for directly mapped marketplaces (e.g., 'Amazon', 'Myntra', 'Shopify' or 'D2C') are inferred from the platform context.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
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
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement",
    "account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse",
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
      "field": "zs_observe.amazon_oms",
      "reason": "Explicitly identified as an OMS table for Mensa Brands via `account_data_binding.mensa.amazon_in.primary.amazon_oms`.",
      "role": "Primary Source for Amazon OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Inferred as an OMS table for Mensa Brands through `query_pattern.myntra.gross_sales_oms` which uses this table and has client-specific filtering logic.",
      "role": "Primary Source for Myntra OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Identified as an OMS system for Mensa Brands from previous questions, containing `sales_channel` to list connected marketplaces.",
      "role": "Primary Source for Unicommerce OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`business_scope_set.mensa_brands.operations_wms` explicitly lists Increff for OMS/WMS operations for Mensa Brands. It is inferred that `zs_observe.increff_sales` is the relevant table and contains `sales_channel`.",
      "role": "Primary Source for Increff OMS/WMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` explicitly mentions Shopify D2C OMS for Mensa Brands, implying `zs_observe.shopify_oms` is the relevant table.",
      "role": "Primary Source for Shopify D2C OMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, supported by patterns in other query patterns (e.g., Myntra).",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "Used in `zs_observe.unicommerce` and `zs_observe.increff_sales` to identify distinct connected marketplaces/channels.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "oms_system_name",
      "reason": "Literal string to represent the OMS system (e.g., 'Amazon OMS', 'Myntra OMS', 'Unicommerce OMS').",
      "role": "Dimension (OMS System Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "connected_marketplace",
      "reason": "Literal string for direct OMS-to-marketplace mappings (e.g., 'Amazon', 'Myntra', 'Shopify') or derived from `sales_channel` for Unicommerce and Increff.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH OMSSystemsAndMarketplaces AS (\n    -- Amazon OMS\n    SELECT DISTINCT\n        'Amazon OMS' AS oms_system_name,\n        'Amazon' AS connected_marketplace\n    FROM\n        zs_observe.amazon_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n\n    UNION ALL\n\n    -- Myntra OMS\n    SELECT DISTINCT\n        'Myntra OMS' AS oms_system_name,\n        'Myntra' AS connected_marketplace\n    FROM\n        zs_observe.myntra_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n\n    UNION ALL\n\n    -- Unicommerce OMS and its various sales channels (marketplaces)\n    SELECT DISTINCT\n        'Unicommerce OMS' AS oms_system_name,\n        sales_channel AS connected_marketplace\n    FROM\n        zs_observe.unicommerce\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n\n    UNION ALL\n\n    -- Increff OMS/WMS and its various sales channels (marketplaces)\n    SELECT DISTINCT\n        'Increff OMS/WMS' AS oms_system_name,\n        sales_channel AS connected_marketplace -- Inferred column name\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n\n    UNION ALL\n\n    -- Shopify D2C OMS\n    SELECT DISTINCT\n        'Shopify OMS' AS oms_system_name,\n        'Shopify' AS connected_marketplace -- Inferred as the primary channel for Shopify OMS\n    FROM\n        zs_observe.shopify_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n)\nSELECT\n    oms_system_name,\n    connected_marketplace\nFROM\n    OMSSystemsAndMarketplaces\nWHERE connected_marketplace IS NOT NULL\nORDER BY\n    oms_system_name, connected_marketplace;"
}
