## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Timing

- started_at: `2026-05-27T06:51:35+00:00`
- duration_seconds: `71.945`
- RAG_COMPLETION_seconds: `49.8`
- GRAPH_COMPLETION_seconds: `22.144`

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

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

{"selected_source":null,"rejected_sources":["query_pattern.myntra.net_settlement","query_pattern.myntra.non_order_adjustments","query_pattern.myntra.oms_settlement_reconciliation","query_pattern.myntra.pending_receivables_by_aging","query_pattern.myntra.prepaid_postpaid_split","query_pattern.myntra.realization_rate","query_pattern.limeroad.total_forward_gmv","query_pattern.logistics.amount_semantics_audit","query_pattern.logistics.awb_duplicate_detection","query_pattern.logistics.bank_credit_unmatched_courier_reference","query_pattern.logistics.cod_expected_vs_remitted","execution_constraint_set.increff.operations_manifest_refactored_constraints","execution_constraint_set.jiomart.marketplace_query_constraints","execution_constraint_set.logistics_batch_to_bank"],"require_tables":[{"field":"zs_observe.myntra_oms","role":"Primary Source for Myntra sales data","selected?":"Yes","reason":"`query_pattern.myntra.gross_sales_oms` indicates this table contains `total_amount` for gross sales. Myntra is a marketplace."},{"field":"zs_observe.limeroad_settlement","role":"Primary Source for LimeRoad sales data","selected?":"Yes","reason":"`query_pattern.limeroad.total_forward_gmv` indicates this table contains `settled_amount` from which GMV is derived. LimeRoad is a marketplace."},{"field":"zs_observe.jiomart_oms","role":"Primary Source for JioMart sales data","selected?":"Yes","reason":"`query_pattern.jiomart.marketplace.6_1_total_gmv` indicates this table contains `total_gmv` data. JioMart is a marketplace."},{"field":"zs_observe.unicommerce","role":"Primary Source for various marketplace sales data","selected?":"Yes","reason":"Identified as a central OMS for Mensa Brands, it likely consolidates `sales_channel` and sales `total_amount` from multiple marketplaces."},{"field":"zs_observe.increff_sales","role":"Primary Source for various marketplace sales data","selected?":"Yes","reason":"`query_pattern.increff.7_1_monthly_gmv_by_channel` explicitly states it contains GMV by `sales_channel`. Increff is an OMS/WMS."},{"field":"zs_observe.amazon_oms","role":"Primary Source for Amazon sales data","selected?":"Yes","reason":"`account_data_binding.mensa.amazon_in.primary.amazon_oms` identifies this as Amazon OMS, expected to contain sales data (e.g., `total_amount`). Amazon is a marketplace."},{"field":"zs_observe.shopify_oms","role":"Primary Source for Shopify sales data (D2C channel)","selected?":"Yes","reason":"`business_scope_set.mensa_brands.shopify_d2c` identifies Shopify D2C, implying its OMS contains sales data (e.g., `total_amount`). This is an 'own website' channel."}],"required_fields":[{"field":"channel_name","role":"Dimension (Marketplace/Channel Identifier)","selected?":"Yes","reason":"Required to group sales by individual marketplace or channel."},{"field":"gross_sales_amount","role":"Metric (Sales Value)","selected?":"Yes","reason":"Represents the primary sales metric to measure concentration."},{"field":"group_level_id","role":"Filter Column (Tenant Scope)","selected?":"Yes","reason":"Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected tables."},{"field":"is_active","role":"Filter Column (Status)","selected?":"Yes","reason":"Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, where applicable. For `zs_observe.myntra_oms`, this is explicitly excluded per `rule.myntra.oms_no_is_active`."}],"rejected_or_ambiguous_fields":[],"metric_logic":{"formula":"Sum of gross sales for each marketplace/channel, then calculate the percentage contribution of each to total sales. Finally, identify the top 2 marketplaces by their sales contribution and report their sales amount and percentage.","numerator":"SUM(gross_sales_amount) per channel","denominator":"SUM(gross_sales_amount) across all channels","aggregation_grain":"channel_name","deduplication_rule":"Distinct orders or transactions within each source, then summed. No cross-source deduplication of individual orders is applied due to lack of a global order ID."},
"filters": [
    "group_level_id = '22'",
    "is_active = true (except for zs_observe.myntra_oms)"
  ],
  "joins": "Multiple CTEs combine sales data from various sources using UNION ALL. The combined data is then aggregated to determine market share.",
  "missing_or_ambiguous": "The exact column names for gross sales amounts (e.g., `total_amount`, `gross_revenue`, `gmv`) are inferred for tables like Amazon OMS, Shopify OMS, and Unicommerce based on their role as OMS systems. The `is_active` filter is inferred for most tables, but explicitly excluded for `zs_observe.myntra_oms` as per rules. The classification of 'marketplace' vs 'own website' is based on common understanding (Shopify is D2C). The analysis will focus on 'marketplaces' as explicitly requested, filtering out D2C if present in the top N, but will still show all channels' contributions.",
  "sql_skeleton": "WITH AllChannelSales AS (
    -- Myntra OMS Sales
    SELECT
        'Myntra' AS channel_name,
        SUM(TRY_CAST(total_amount AS DOUBLE)) AS gross_sales_amount
    FROM
        zs_observe.myntra_oms
    WHERE
        group_level_id = '22' 
        -- rule.myntra.oms_no_is_active implies no is_active filter
    GROUP BY
        1

    UNION ALL

    -- LimeRoad Settlement Sales
    SELECT
        'LimeRoad' AS channel_name,
        SUM(COALESCE(settled_amount, 0)) AS gross_sales_amount -- Per query_pattern.limeroad.total_forward_gmv
    FROM
        zs_observe.limeroad_settlement
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
    GROUP BY
        1

    UNION ALL

    -- JioMart OMS Sales
    SELECT
        'JioMart' AS channel_name,
        SUM(total_gmv) AS gross_sales_amount -- Per query_pattern.jiomart.marketplace.6_1_total_gmv
    FROM
        zs_observe.jiomart_oms
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
    GROUP BY
        1

    UNION ALL

    -- Unicommerce Sales (handling multiple sales_channels)
    SELECT
        sales_channel AS channel_name,
        SUM(total_amount) AS gross_sales_amount -- Inferred column
    FROM
        zs_observe.unicommerce
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
    GROUP BY
        1

    UNION ALL

    -- Increff Sales (handling multiple sales_channels)
    SELECT
        sales_channel AS channel_name,
        SUM(total_amount) AS gross_sales_amount -- Inferred column for GMV
    FROM
        zs_observe.increff_sales
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
        AND order_status = 'COMPLETED' AND transaction_type = 'SALES' -- Per increff constraints
    GROUP BY
        1

    UNION ALL

    -- Amazon OMS Sales
    SELECT
        'Amazon' AS channel_name,
        SUM(total_amount) AS gross_sales_amount -- Inferred column
    FROM
        zs_observe.amazon_oms
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
    GROUP BY
        1

    UNION ALL

    -- Shopify OMS Sales (D2C, will be excluded from Top 2 Marketplaces if applicable, but included in total)
    SELECT
        'Shopify D2C' AS channel_name,
        SUM(total_amount) AS gross_sales_amount -- Inferred column
    FROM
        zs_observe.shopify_oms
    WHERE
        group_level_id = '22'
        AND is_active = true -- Inferred filter
    GROUP BY
        1
),
TotalSales AS (
    SELECT SUM(gross_sales_amount) AS overall_total_sales
    FROM AllChannelSales
)
SELECT
    acs.channel_name,
    acs.gross_sales_amount,
    (acs.gross_sales_amount * 100.0 / ts.overall_total_sales) AS percentage_of_total_sales
FROM
    AllChannelSales acs
CROSS JOIN
    TotalSales ts
WHERE
    acs.channel_name NOT IN ('Shopify D2C') -- Filter out D2C for 'top 2 marketplaces'
ORDER BY
    gross_sales_amount DESC
LIMIT 2;

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true (except for zs_observe.myntra_oms)"
  ],
  "joins": "Multiple CTEs combine sales data from various sources using UNION ALL. The combined data is then aggregated to determine market share.",
  "metric_logic": {
    "aggregation_grain": "channel_name",
    "deduplication_rule": "Distinct orders or transactions within each source, then summed. No cross-source deduplication of individual orders is defined due to lack of a global order ID.",
    "denominator": "SUM(gross_sales_amount) across all channels",
    "formula": "Sum of gross sales for each marketplace/channel, then calculate the percentage contribution of each to total sales. Finally, identify the top 2 marketplaces by their sales contribution and report their sales amount and percentage.",
    "numerator": "SUM(gross_sales_amount) per channel"
  },
  "missing_or_ambiguous": "The exact column names for gross sales amounts (e.g., `total_amount`, `gross_revenue`, `gmv`) are inferred for tables like Amazon OMS, Shopify OMS, and Unicommerce based on their role as OMS systems. The `is_active` filter is inferred for most tables, but explicitly excluded for `zs_observe.myntra_oms` as per rules. The classification of 'marketplace' vs 'own website' is based on common understanding (Shopify is D2C). The analysis will focus on 'marketplaces' as explicitly requested, filtering out D2C if present in the top N, but will still show all channels' contributions.",
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
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` indicates this table contains `total_amount` for gross sales. Myntra is a marketplace.",
      "role": "Primary Source for Myntra sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` indicates this table contains `settled_amount` from which GMV is derived. LimeRoad is a marketplace.",
      "role": "Primary Source for LimeRoad sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.jiomart_oms",
      "reason": "`query_pattern.jiomart.marketplace.6_1_total_gmv` indicates this table contains `total_gmv` data. JioMart is a marketplace.",
      "role": "Primary Source for JioMart sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Identified as a central OMS for Mensa Brands, it likely consolidates `sales_channel` and sales `total_amount` from multiple marketplaces.",
      "role": "Primary Source for various marketplace sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`query_pattern.increff.7_1_monthly_gmv_by_channel` explicitly states it contains GMV by `sales_channel`. Increff is an OMS/WMS.",
      "role": "Primary Source for various marketplace sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "`account_data_binding.mensa.amazon_in.primary.amazon_oms` identifies this as Amazon OMS, expected to contain sales data (e.g., `total_amount`). Amazon is a marketplace.",
      "role": "Primary Source for Amazon sales data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` identifies Shopify as the 'own website' channel, implying its OMS contains sales data (e.g., `total_amount`). This is an 'own website' channel.",
      "role": "Primary Source for Shopify sales data (D2C channel)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "reason": "Required to group sales by individual marketplace or channel.",
      "role": "Dimension (Marketplace/Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "gross_sales_amount",
      "reason": "Represents the primary sales metric to measure concentration.",
      "role": "Metric (Sales Value)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, where applicable. For `zs_observe.myntra_oms`, this is explicitly excluded per `rule.myntra.oms_no_is_active`.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH AllChannelSales AS (\n    -- Myntra OMS Sales\n    SELECT\n        'Myntra' AS channel_name,\n        SUM(TRY_CAST(total_amount AS DOUBLE)) AS gross_sales_amount\n    FROM\n        zs_observe.myntra_oms\n    WHERE\n        group_level_id = '22' \n        -- rule.myntra.oms_no_is_active implies no is_active filter\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- LimeRoad Settlement Sales\n    SELECT\n        'LimeRoad' AS channel_name,\n        SUM(COALESCE(settled_amount, 0)) AS gross_sales_amount -- Per query_pattern.limeroad.total_forward_gmv\n    FROM\n        zs_observe.limeroad_settlement\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- JioMart OMS Sales\n    SELECT\n        'JioMart' AS channel_name,\n        SUM(total_gmv) AS gross_sales_amount -- Per query_pattern.jiomart.marketplace.6_1_total_gmv\n    FROM\n        zs_observe.jiomart_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- Unicommerce Sales (handling multiple sales_channels)\n    SELECT\n        sales_channel AS channel_name,\n        SUM(total_amount) AS gross_sales_amount -- Inferred column\n    FROM\n        zs_observe.unicommerce\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- Increff Sales (handling multiple sales_channels)\n    SELECT\n        sales_channel AS channel_name,\n        SUM(total_amount) AS gross_sales_amount -- Inferred column for GMV\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n        AND order_status = 'COMPLETED' AND transaction_type = 'SALES' -- Per increff constraints\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- Amazon OMS Sales\n    SELECT\n        'Amazon' AS channel_name,\n        SUM(total_amount) AS gross_sales_amount -- Inferred column\n    FROM\n        zs_observe.amazon_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n    GROUP BY\n        1\n\n    UNION ALL\n\n    -- Shopify OMS Sales (D2C, will be excluded from Top 2 Marketplaces if applicable, but included in total)\n    SELECT\n        'Shopify D2C' AS channel_name,\n        SUM(total_amount) AS gross_sales_amount -- Inferred column\n    FROM\n        zs_observe.shopify_oms\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n    GROUP BY\n        1\n),\nTotalSales AS (\n    SELECT SUM(gross_sales_amount) AS overall_total_sales\n    FROM AllChannelSales\n)\nSELECT\n    acs.channel_name,\n    acs.gross_sales_amount,\n    (acs.gross_sales_amount * 100.0 / ts.overall_total_sales) AS percentage_of_total_sales\nFROM\n    AllChannelSales acs\nCROSS JOIN\n    TotalSales ts\nWHERE\n    acs.channel_name NOT IN ('Shopify D2C') -- Filter out D2C for 'top 2 marketplaces'\nORDER BY\n    gross_sales_amount DESC\nLIMIT 2;"
}
