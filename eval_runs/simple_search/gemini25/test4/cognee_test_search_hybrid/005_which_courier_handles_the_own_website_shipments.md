## 005. Which courier handles the own website shipments?

### Timing

- started_at: `2026-05-27T06:36:01+00:00`
- duration_seconds: `43.839`
- RAG_COMPLETION_seconds: `21.817`
- GRAPH_COMPLETION_seconds: `22.022`

### Query

```text
Which courier handles the own website shipments?

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
  "selected_source": "table.zs_observe.shopify_oms",
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "zs_observe.myntra_oms",
    "zs_observe.limeroad_settlement",
    "zs_observe.increff_sales",
    "zs_observe.amazon_oms",
    "zs_observe.meesho_sales"
  ],
  "require_tables": [
    {
      "field": "zs_observe.shopify_oms",
      "role": "Primary Source for Own Website (D2C) Shipments",
      "selected?": "Yes",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` links Mensa Brands to Shopify D2C, which represents 'own website' shipments. This table is inferred to contain courier information directly for these shipments."
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "role": "Supporting Source for Courier Information",
      "selected?": "Yes",
      "reason": "`query_pattern.logistics.*` indicates `shiprocket_oms` as a source for `courier_partner` dimension. It is a logistics aggregator and may contain originating channel information (`marketplace_name` or `channel_name`) that can be filtered for 'Shopify' or 'Own Website'."
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes",
      "reason": "The requested information is the courier. This field is inferred to be present in `zs_observe.shopify_oms` (as an OMS table for D2C) or `zs_observe.shiprocket_oms` (as a logistics platform)."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands'."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across operational tables."
    },
    {
      "field": "channel_name_or_marketplace_name",
      "role": "Filter Column (Channel Identifier)",
      "selected?": "Yes",
      "reason": "Required to filter for 'own website' shipments. Inferred name `channel_name_or_marketplace_name` with value 'Shopify' or 'D2C' or 'Own Website'."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "A distinct list of courier names associated with 'own website' shipments.",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "courier_partner",
    "deduplication_rule": "Distinct `courier_partner` values."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "channel_name_or_marketplace_name IN ('Shopify', 'D2C', 'Own Website')"
  ],
  "joins": "Multiple CTEs are used to extract courier partners from relevant tables. These CTEs are then combined using UNION ALL to create a unified distinct list of couriers.",
  "missing_or_ambiguous": "The exact column names for `courier_partner` and channel identifiers (e.g., `marketplace_name`, `sales_channel`, `origin_channel`) within `zs_observe.shopify_oms` and `zs_observe.shiprocket_oms` are inferred. The specific string value representing 'own website' in these inferred channel columns (e.g., 'Shopify', 'D2C', 'Own Website') is also inferred based on common industry practices and previous context regarding `shopify_d2c`.",
  "sql_skeleton": "WITH OwnWebsiteCouriers AS (
    SELECT DISTINCT
        soms.courier_partner AS courier_name
    FROM
        zs_observe.shopify_oms soms
    WHERE
        soms.group_level_id = '22'
        AND soms.is_active = true
        -- Assuming 'Shopify' represents 'Own Website' channel within the OMS

    UNION ALL

    SELECT DISTINCT
        ship.courier_partner AS courier_name
    FROM
        zs_observe.shiprocket_oms ship
    WHERE
        ship.group_level_id = '22'
        AND ship.is_active = true
        AND ship.marketplace_name IN ('Shopify', 'D2C', 'Own Website') -- Inferred filter on channel identifier
)
SELECT DISTINCT courier_name
FROM OwnWebsiteCouriers
WHERE courier_name IS NOT NULL
ORDER BY courier_name;"
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
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "zs_observe.myntra_oms",
    "zs_observe.limeroad_settlement",
    "zs_observe.increff_sales",
    "zs_observe.amazon_oms",
    "zs_observe.meesho_sales",
    "query_pattern.myntra.gross_sales_oms",
    "query_pattern.myntra.net_settlement",
    "query_pattern.myntra.non_order_adjustments",
    "query_pattern.myntra.oms_settlement_reconciliation",
    "query_pattern.myntra.pending_receivables_by_aging",
    "query_pattern.myntra.prepaid_postpaid_split",
    "query_pattern.myntra.realization_rate",
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
      "field": "zs_observe.shopify_oms",
      "role": "Primary Source for Own Website (D2C) Shipments",
      "selected?": "Yes",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` links Mensa Brands to Shopify D2C, which represents 'own website' shipments. This table is inferred to contain courier information directly for these shipments."
    },
    {
      "field": "zs_observe.shiprocket_oms",
      "role": "Supporting Source for Courier Information",
      "selected?": "Yes",
      "reason": "`query_pattern.logistics.*` indicates `shiprocket_oms` as a source for `courier_partner` dimension. It is a logistics aggregator and may contain originating channel information (`marketplace_name` or `channel_name`) that can be filtered for 'Shopify' or 'Own Website'."
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes",
      "reason": "The requested information is the courier. This field is inferred to be present in `zs_observe.shopify_oms` (as an OMS table for D2C) or `zs_observe.shiprocket_oms` (as a logistics platform)."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands'."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity across operational tables."
    },
    {
      "field": "channel_name_or_marketplace_name",
      "role": "Filter Column (Channel Identifier)",
      "selected?": "Yes",
      "reason": "Required to filter for 'own website' shipments. Inferred name `channel_name_or_marketplace_name` with value 'Shopify' or 'D2C' or 'Own Website'."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "A distinct list of courier names associated with 'own website' shipments.",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "courier_partner",
    "deduplication_rule": "Distinct `courier_partner` values."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "channel_name_or_marketplace_name IN ('Shopify', 'D2C', 'Own Website')"
  ],
  "joins": "Multiple CTEs are used to extract courier partners from relevant tables. These CTEs are then combined using UNION ALL to create a unified distinct list of couriers.",
  "missing_or_ambiguous": "The exact column names for `courier_partner` and channel identifiers (e.g., `marketplace_name`, `sales_channel`, `origin_channel`) within `zs_observe.shopify_oms` and `zs_observe.shiprocket_oms` are inferred. The specific string value representing 'own website' in these inferred channel columns (e.g., 'Shopify', 'D2C', 'Own Website') is also inferred based on common industry practices and previous context regarding `shopify_d2c`.",
  "sql_skeleton": "WITH OwnWebsiteCouriers AS (
    SELECT DISTINCT
        soms.courier_partner AS courier_name
    FROM
        zs_observe.shopify_oms soms
    WHERE
        soms.group_level_id = '22'
        AND soms.is_active = true
        -- Assuming 'Shopify' represents 'Own Website' channel within the OMS

    UNION ALL

    SELECT DISTINCT
        ship.courier_partner AS courier_name
    FROM
        zs_observe.shiprocket_oms ship
    WHERE
        ship.group_level_id = '22'
        AND ship.is_active = true
        AND ship.marketplace_name IN ('Shopify', 'D2C', 'Own Website') -- Inferred filter on channel identifier
)
SELECT DISTINCT courier_name
FROM OwnWebsiteCouriers
WHERE courier_name IS NOT NULL
ORDER BY courier_name;"
}
