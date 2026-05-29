## 001. Which channel has the highest order volume share?

### Timing

- started_at: `2026-05-27T06:29:47+00:00`
- duration_seconds: `142.356`
- RAG_COMPLETION_seconds: `94.84`
- GRAPH_COMPLETION_seconds: `47.515`

### Query

```text
Which channel has the highest order volume share?

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
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract order counts and channel identifiers from disparate source tables. These CTEs are then combined using UNION ALL. The final calculation of order volume and share is performed on the unified dataset, grouped by `marketplace_name`.",
  "metric_logic": {
    "aggregation_grain": "marketplace_name",
    "deduplication_rule": "Each `order_id` represents a unique order within its source. Orders are summed up per channel. If an order appears in multiple sources due to cross-listing or errors (not indicated by context), it would be counted once per source, then aggregated. Consolidation across sources is done at the order_id level within each channel's CTE, then channels are united.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) OVER () (total distinct orders across all channels)",
    "formula": "COUNT(DISTINCT order_id) per channel, then calculate (channel_order_count / total_order_count) * 100 as share.",
    "numerator": "COUNT(DISTINCT order_id) per channel"
  },
  "missing_or_ambiguous": "The explicit presence of `order_id`, `is_active`, and `order_status` for Myntra OMS, LimeRoad Settlement, Amazon OMS, and Shopify OMS is inferred as typical for these systems. Similarly, the exact column names for `order_status` (e.g., `status` vs `order_status`) for these tables are inferred to be `order_status = 'COMPLETED'` for consistency, while Meesho explicitly uses 'Delivered'. The presence of an `is_active` filter is a general best practice inferred across all relevant tables.",
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
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table and specifies `group_level_id` for scoping. It is inferred to contain `order_id` for order volume calculations.",
      "role": "Source for Myntra order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and specifies `group_level_id=22`. It is inferred to contain `order_id` for order volume calculations.",
      "role": "Source for LimeRoad order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` confirms this table contains sales data with `sales_channel`, `order_id`, `order_status`, and relevant filters for Mensa Brands.",
      "role": "Source for Increff order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "As an OMS for a major marketplace, it is inferred to contain `order_id` and sales data relevant for Mensa Brands (`group_level_id = 22`).",
      "role": "Source for Amazon order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` explicitly uses `zs_observe.meesho_sales` with `order_id`, `group_level_id = 22`, and `order_status = 'Delivered'`.",
      "role": "Source for Meesho order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` indicates Mensa D2C Shopify OMS, inferring `zs_observe.shopify_oms` as a source for 'own website' orders with `order_id`, `group_level_id`, and `order_status`.",
      "role": "Source for Shopify (Own Website/D2C) order data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "marketplace_name",
      "reason": "The primary dimension for grouping and calculating order volume share. Derived as a literal string ('Myntra', 'LimeRoad', 'Amazon', 'Meesho', 'Shopify') or from the `sales_channel` column for Increff.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Unique identifier for each order, used to count distinct orders per channel and overall. Inferred to be present in all selected sales/OMS tables.",
      "role": "Metric (Order Identifier for Volume Count)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables.",
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
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered' for Meesho) for accurate order volume, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions contribute to order volume.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH ChannelOrders AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        oms.order_id\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        settlement.order_id\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS marketplace_name,\n        sales.order_id\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS marketplace_name,\n        amazon_oms.order_id\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        'Meesho' AS marketplace_name,\n        meesho_sales.order_id\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n\n    UNION ALL\n\n    SELECT\n        'Shopify' AS marketplace_name,\n        shopify_oms.order_id\n    FROM\n        zs_observe.shopify_oms shopify_oms\n    WHERE\n        shopify_oms.group_level_id = '22'\n        AND shopify_oms.is_active = true -- Inferred filter\n        AND shopify_oms.order_status = 'COMPLETED' -- Inferred filter\n),\nChannelOrderVolume AS (\n    SELECT\n        marketplace_name,\n        COUNT(DISTINCT order_id) AS order_count\n    FROM\n        ChannelOrders\n    GROUP BY\n        marketplace_name\n)\nSELECT\n    cov.marketplace_name,\n    cov.order_count,\n    (cov.order_count * 100.0) / SUM(cov.order_count) OVER () AS order_volume_share_pct\nFROM\n    ChannelOrderVolume cov\nORDER BY\n    order_volume_share_pct DESC;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' OR order_status = 'Delivered' (depending on source)",
    "transaction_type = 'SALES' (where applicable)"
  ],
  "joins": "Multiple CTEs are used to extract order counts and channel identifiers from disparate source tables. These CTEs are then combined using UNION ALL. The final calculation of order volume and share is performed on the unified dataset, grouped by `marketplace_name`.",
  "metric_logic": {
    "aggregation_grain": "marketplace_name",
    "deduplication_rule": "Each `order_id` represents a unique order within its source. Orders are summed up per channel. If an order appears in multiple sources due to cross-listing or errors (not indicated by context), it would be counted once per source, then aggregated. Consolidation across sources is done at the order_id level within each channel's CTE, then channels are united.",
    "denominator": "SUM(COUNT(DISTINCT order_id)) OVER () (total distinct orders across all channels)",
    "formula": "COUNT(DISTINCT order_id) per channel, then calculate (channel_order_count / total_order_count) * 100 as share.",
    "numerator": "COUNT(DISTINCT order_id) per channel"
  },
  "missing_or_ambiguous": "The explicit presence of `order_id`, `is_active`, and `order_status` for Myntra OMS, LimeRoad Settlement, Amazon OMS, and Shopify OMS is inferred as typical for these systems. Similarly, the exact column names for `order_status` (e.g., `status` vs `order_status`) for these tables are inferred to be `order_status = 'COMPLETED'` for consistency, while Meesho explicitly uses 'Delivered'. The presence of an `is_active` filter is a general best practice inferred across all relevant tables.",
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
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.myntra_oms",
      "reason": "`query_pattern.myntra.gross_sales_oms` explicitly uses this table and specifies `group_level_id` for scoping. It is inferred to contain `order_id` for order volume calculations.",
      "role": "Source for Myntra order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.limeroad_settlement",
      "reason": "`query_pattern.limeroad.total_forward_gmv` uses this table for GMV and specifies `group_level_id=22`. It is inferred to contain `order_id` for order volume calculations.",
      "role": "Source for LimeRoad order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`execution_constraint_set.increff.operations_manifest_refactored_constraints` confirms this table contains sales data with `sales_channel`, `order_id`, `order_status`, and relevant filters for Mensa Brands.",
      "role": "Source for Increff order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "As an OMS for a major marketplace, it is inferred to contain `order_id` and sales data relevant for Mensa Brands (`group_level_id = 22`).",
      "role": "Source for Amazon order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "`formula_template.meesho.average_order_value_aov` explicitly uses `zs_observe.meesho_sales` with `order_id`, `group_level_id = 22`, and `order_status = 'Delivered'.",
      "role": "Source for Meesho order data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "`business_scope_set.mensa_brands.shopify_d2c` indicates Mensa D2C Shopify OMS, inferring `zs_observe.shopify_oms` as a source for 'own website' orders with `order_id`, `group_level_id`, and `order_status`.",
      "role": "Source for Shopify (Own Website/D2C) order data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "marketplace_name",
      "reason": "The primary dimension for grouping and calculating order volume share. Derived as a literal string ('Myntra', 'LimeRoad', 'Amazon', 'Meesho', 'Shopify') or from the `sales_channel` column for Increff.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Unique identifier for each order, used to count distinct orders per channel and overall. Inferred to be present in all selected sales/OMS tables.",
      "role": "Metric (Order Identifier for Volume Count)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope all data to 'Mensa Brands', consistently applied across all relevant tables.",
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
      "reason": "Mandatory filter (`order_status = 'COMPLETED'` or equivalent like 'Delivered' for Meesho) for accurate order volume, ensuring only fulfilled orders are counted.",
      "role": "Filter Column (Sales Status)",
      "selected?": "Yes"
    },
    {
      "field": "transaction_type",
      "reason": "Mandatory filter (`transaction_type = 'SALES'`) for `increff_sales` (and inferred for other sales tables if applicable), ensuring only sales transactions contribute to order volume.",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH ChannelOrders AS (\n    SELECT\n        'Myntra' AS marketplace_name,\n        oms.order_id\n    FROM\n        zs_observe.myntra_oms oms\n    WHERE\n        oms.group_level_id = '22'\n        AND oms.is_active = true\n        AND oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        'LimeRoad' AS marketplace_name,\n        settlement.order_id\n    FROM\n        zs_observe.limeroad_settlement settlement\n    WHERE\n        settlement.group_level_id = '22'\n        AND settlement.is_active = true -- Inferred filter\n        AND settlement.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        sales.sales_channel AS marketplace_name,\n        sales.order_id\n    FROM\n        zs_observe.increff_sales sales\n    WHERE\n        sales.group_level_id = '22'\n        AND sales.is_active = true\n        AND sales.order_status = 'COMPLETED'\n        AND sales.transaction_type = 'SALES'\n\n    UNION ALL\n\n    SELECT\n        'Amazon' AS marketplace_name,\n        amazon_oms.order_id\n    FROM\n        zs_observe.amazon_oms amazon_oms\n    WHERE\n        amazon_oms.group_level_id = '22'\n        AND amazon_oms.is_active = true -- Inferred filter\n        AND amazon_oms.order_status = 'COMPLETED' -- Inferred filter\n\n    UNION ALL\n\n    SELECT\n        'Meesho' AS marketplace_name,\n        meesho_sales.order_id\n    FROM\n        zs_observe.meesho_sales meesho_sales\n    WHERE\n        meesho_sales.group_level_id = '22'\n        AND meesho_sales.is_active = true -- Inferred filter\n        AND meesho_sales.order_status = 'Delivered'\n\n    UNION ALL\n\n    SELECT\n        'Shopify' AS marketplace_name,\n        shopify_oms.order_id\n    FROM\n        zs_observe.shopify_oms shopify_oms\n    WHERE\n        shopify_oms.group_level_id = '22'\n        AND shopify_oms.is_active = true -- Inferred filter\n        AND shopify_oms.order_status = 'COMPLETED' -- Inferred filter\n),\nChannelOrderVolume AS (\n    SELECT\n        marketplace_name,\n        COUNT(DISTINCT order_id) AS order_count\n    FROM\n        ChannelOrders\n    GROUP BY\n        marketplace_name\n)\nSELECT\n    cov.marketplace_name,\n    cov.order_count,\n    (cov.order_count * 100.0) / SUM(cov.order_count) OVER () AS order_volume_share_pct\nFROM\n    ChannelOrderVolume cov\nORDER BY\n    order_volume_share_pct DESC;"
}
