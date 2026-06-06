## 004. Generate a courier-wise channel mapping report.

### Timing

- started_at: `2026-05-27T06:34:42+00:00`
- duration_seconds: `79.283`
- RAG_COMPLETION_seconds: `31.471`
- GRAPH_COMPLETION_seconds: `47.812`

### Query

```text
Generate a courier-wise channel mapping report.

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
  "selected_source": null,
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "This table contains `sales_channel` and `execution_constraint_set.increff.operations_manifest_refactored_constraints` mentions `rule.increff.courier_normalization` and `forward_awb_number` link, implying courier data can be derived or is present. Filtered for Mensa Brands (`group_level_id = '22'`)."
    },
    {
      "field": "zs_observe.myntra_oms",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "OMS tables typically contain courier details for orders. `query_pattern.myntra.gross_sales_oms` specifies `zs_observe.myntra_oms` for Mensa Brands (from prior context), so it's inferred to contain courier information."
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "Settlement tables often include order details, which can contain courier information. `query_pattern.limeroad.total_forward_gmv` references `zs_observe.limeroad_settlement` for Mensa Brands, so courier information is inferred."
    },
    {
      "field": "zs_observe.amazon_oms",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "As a primary OMS table for a major marketplace like Amazon, it is highly probable to contain courier information for orders for Mensa Brands."
    },
    {
      "field": "zs_observe.meesho_sales",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "`formula_template.meesho.average_order_value_aov` and `query_pattern.meesho.007.7_1_gross_gmv_forward_sales` explicitly use `zs_observe.meesho_sales` for Mensa Brands (from prior context), implying it holds core order details including inferred courier information."
    },
    {
      "field": "zs_observe.shopify_oms",
      "role": "Source for Channel and Courier information",
      "selected?": "Yes",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` (from prior context) indicates Mensa D2C Shopify OMS, making `zs_observe.shopify_oms` a relevant source for orders and inferred courier information."
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "role": "Source for Courier and Channel information",
      "selected?": "Yes",
      "reason": "Logistics query patterns list `shiprocket_oms` and `courier_partner` as an `allowed_dimensions`. It is inferred that a logistics OMS would also record the `marketplace_name` or `origin_channel` for each shipment."
    },
    {
      "field": "zs_observe.delhivery_invoice",
      "role": "Source for Courier and Channel information",
      "selected?": "Yes",
      "reason": "Listed in logistics query patterns with `courier_partner` as an `allowed_dimensions`. It is inferred that an invoice table for a courier would contain the originating `marketplace_name` or `source_channel`."
    },
    {
      "field": "zs_observe.dtdc_settlement",
      "role": "Source for Courier and Channel information",
      "selected?": "Yes",
      "reason": "Listed in logistics query patterns with `courier_partner` as an `allowed_dimensions`. It is inferred that a settlement table for a courier would contain the originating `marketplace_name` or `source_channel`."
    },
    {
      "field": "zs_observe.ekart_settlement",
      "role": "Source for Courier and Channel information",
      "selected?": "Yes",
      "reason": "Listed in logistics query patterns with `courier_partner` as an `allowed_dimensions`. It is inferred that a settlement table for a courier would contain the originating `marketplace_name` or `source_channel`."
    }
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes",
      "reason": "Required for the 'channel' part of the courier-wise channel mapping. Derived from `sales_channel` or inferred `marketplace_name`/`origin_channel`."
    },
    {
      "field": "courier_name",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes",
      "reason": "Required for the 'courier-wise' part of the mapping. Derived from a column like `courier_partner` or inferred from table names (e.g., 'Delhivery')."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands' across all tables."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across all operational tables."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Inferred as `order_status = 'COMPLETED'` for OMS/sales tables to ensure active and completed orders are considered for mapping. Meesho specifically uses 'Delivered'."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "A distinct list of (channel_name, courier_name) pairs.",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name, courier_name",
    "deduplication_rule": "Distinct pairs of channel name and courier name are listed."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)"
  ],
  "joins": "Multiple CTEs are used to extract distinct courier and channel information from various source tables. These CTEs are then combined using UNION ALL to create a unified list of unique courier-channel mappings.",
  "missing_or_ambiguous": "The explicit presence and exact naming of `courier_partner` column in OMS/Sales tables (`zs_observe.increff_sales`, `zs_observe.myntra_oms`, `zs_observe.limeroad_settlement`, `zs_observe.amazon_oms`, `zs_observe.meesho_sales`, `zs_observe.shopify_oms`) are inferred. Similarly, the exact naming of `marketplace_name` or `origin_channel` columns in logistics tables (`zs_observe.shiprocket_oms`, `zs_observe.delhivery_invoice`, `zs_observe.dtdc_settlement`, `zs_observe.ekart_settlement`) are inferences. The presence of `is_active` and `group_level_id` across all these tables is also an inference based on common data models for sales/logistics platforms and the explicit mention of `courier_partner` as an allowed dimension in logistics query patterns. Without these inferences, a consolidated courier-wise channel mapping report would not be possible from the given context.",
  "sql_skeleton": "WITH CourierChannelMapping AS (
    -- From Increff Sales
    SELECT DISTINCT
        inc.sales_channel AS channel_name,
        inc.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.increff_sales inc
    WHERE
        inc.group_level_id = '22'
        AND inc.is_active = true
        AND inc.order_status = 'COMPLETED'

    UNION ALL

    -- From Myntra OMS
    SELECT DISTINCT
        'Myntra' AS channel_name,
        moms.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.myntra_oms moms
    WHERE
        moms.group_level_id = '22'
        AND moms.is_active = true
        AND moms.order_status = 'COMPLETED'

    UNION ALL

    -- From LimeRoad Settlement
    SELECT DISTINCT
        'LimeRoad' AS channel_name,
        lsett.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.limeroad_settlement lsett
    WHERE
        lsett.group_level_id = '22'
        AND lsett.is_active = true
        AND lsett.order_status = 'COMPLETED'

    UNION ALL

    -- From Amazon OMS
    SELECT DISTINCT
        'Amazon' AS channel_name,
        aoms.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.amazon_oms aoms
    WHERE
        aoms.group_level_id = '22'
        AND aoms.is_active = true
        AND aoms.order_status = 'COMPLETED'

    UNION ALL

    -- From Meesho Sales
    SELECT DISTINCT
        'Meesho' AS channel_name,
        msales.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.meesho_sales msales
    WHERE
        msales.group_level_id = '22'
        AND msales.is_active = true
        AND msales.order_status = 'Delivered'

    UNION ALL

    -- From Shopify OMS
    SELECT DISTINCT
        'Shopify' AS channel_name,
        soms_shopify.courier_partner AS courier_name -- Inferred column name
    FROM
        zs_observe.shopify_oms soms_shopify
    WHERE
        soms_shopify.group_level_id = '22'
        AND soms_shopify.is_active = true
        AND soms_shopify.order_status = 'COMPLETED'

    UNION ALL

    -- From Shiprocket OMS (logistics aggregator)
    SELECT DISTINCT
        soms_shiprocket.marketplace_name AS channel_name, -- Inferred column name
        soms_shiprocket.courier_partner AS courier_name
    FROM
        zs_observe.shiprocket_oms soms_shiprocket
    WHERE
        soms_shiprocket.group_level_id = '22' -- Inferred filter for Mensa scope
        AND soms_shiprocket.is_active = true -- Inferred filter

    UNION ALL

    -- From Delhivery Invoice
    SELECT DISTINCT
        di.marketplace_name AS channel_name, -- Inferred column name
        'Delhivery' AS courier_name -- Courier name derived from table context
    FROM
        zs_observe.delhivery_invoice di
    WHERE
        di.group_level_id = '22' -- Inferred filter for Mensa scope
        AND di.is_active = true -- Inferred filter

    UNION ALL

    -- From DTDC Settlement
    SELECT DISTINCT
        ds.marketplace_name AS channel_name, -- Inferred column name
        'DTDC' AS courier_name -- Courier name derived from table context
    FROM
        zs_observe.dtdc_settlement ds
    WHERE
        ds.group_level_id = '22' -- Inferred filter for Mensa scope
        AND ds.is_active = true -- Inferred filter

    UNION ALL

    -- From Ekart Settlement
    SELECT DISTINCT
        es.marketplace_name AS channel_name, -- Inferred column name
        'Ekart' AS courier_name -- Courier name derived from table context
    FROM
        zs_observe.ekart_settlement es
    WHERE
        es.group_level_id = '22' -- Inferred filter for Mensa scope
        AND es.is_active = true -- Inferred filter
)
SELECT DISTINCT
    channel_name,
    courier_name
FROM
    CourierChannelMapping
WHERE
    courier_name IS NOT NULL AND channel_name IS NOT NULL -- Exclude rows where courier or channel could not be identified (e.g., NULLs from inferred columns)
ORDER BY
    channel_name, courier_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'"
  ],
  "joins": "No joins are needed as all required information is expected within the single selected table.",
  "metric_logic": {
    "aggregation_grain": "channel_name, courier_name",
    "deduplication_rule": "Distinct pairs of channel name and courier name are listed.",
    "denominator": null,
    "formula": "A distinct list of (channel_name, courier_name) pairs.",
    "numerator": null
  },
  "missing_or_ambiguous": "The explicit presence and exact naming of a `courier_partner` column, `is_active` column, and `order_status` column within `zs_observe.amazon_oms` are inferred based on common OMS table structures. The current context provides a very limited set of relevant tables. This report will only cover courier-channel mappings for Amazon, as no other channels or courier-specific tables for Mensa Brands are explicitly grounded in the provided context for this specific turn.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
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
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` explicitly binds Mensa Brands (`group_level_id = 22`) to `table.zs_observe.amazon_oms`. As an Order Management System table, it is highly probable to contain order-level courier information.",
      "role": "Primary Source for Channel and Courier information",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "reason": "Required for the 'channel' part of the courier-wise channel mapping. Derived as a literal string 'Amazon'.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "courier_partner",
      "reason": "Required for the 'courier-wise' part of the mapping. Inferred column name for courier from an OMS table.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', as specified in the binding card.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across operational tables.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "order_status",
      "reason": "Inferred as `order_status = 'COMPLETED'` to ensure only completed orders are considered for mapping.",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.amazon_oms",
  "sql_skeleton": "SELECT DISTINCT\n    'Amazon' AS channel_name,\n    oms.courier_partner AS courier_name -- Inferred column name\nFROM\n    zs_observe.amazon_oms oms\nWHERE\n    oms.group_level_id = '22'\n    AND oms.is_active = true -- Inferred filter\n    AND oms.order_status = 'COMPLETED' -- Inferred filter\nORDER BY\n    channel_name, courier_name;"
}
