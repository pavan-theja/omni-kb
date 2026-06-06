## 003. List all marketplaces handled through Unicommerce.

### Timing

- started_at: `2026-05-27T06:32:56+00:00`
- duration_seconds: `106.165`
- RAG_COMPLETION_seconds: `58.995`
- GRAPH_COMPLETION_seconds: `47.17`

### Query

```text
List all marketplaces handled through Unicommerce.

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
  "joins": "No joins are needed as all required information is available in the `zs_observe.unicommerce` table.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Distinct `sales_channel` values.",
    "denominator": null,
    "formula": "A distinct list of marketplace names (identified by `sales_channel`) handled through Unicommerce for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary inference is that the `sales_channel` column within `zs_observe.unicommerce` directly represents the marketplace name. This is a strong and logical inference given the context of Unicommerce as an OMS for various sales channels.",
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
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_return_dump",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_sales_dump",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_wallet_ledger",
    "account_data_binding.aza_fashions.delhivery_in.primary.delhivery_invoice",
    "account_data_binding.aza_fashions.delhivery_in.primary.delhivery_settlement",
    "account_data_binding.aza_fashions.dtdc_in.primary.dtdc_invoice",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bracheium_brand_technologies.shopify_d2c.primary.shopify_oms",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.bracheium_brand_technologies.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.bracheium_brand_technologies.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bracheium_brand_technologies.unicommerce_oms.primary.unicommerce"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "The `table.zs_observe.unicommerce` card explicitly lists `sales_channel` as a column, which is suitable for identifying marketplaces. The `account_data_binding.mensa.unicommerce_oms.primary.unicommerce` card confirms Mensa Brands (`group_level_id = 22`) uses this table.",
      "role": "Primary Source for Unicommerce data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Explicitly listed as a column in `table.zs_observe.unicommerce`, used to identify marketplaces.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands', as specified in `account_data_binding.mensa.unicommerce_oms.primary.unicommerce` and confirmed as a column in `table.zs_observe.unicommerce`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Listed as a mandatory filter in the `table.zs_observe.unicommerce` card, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.unicommerce",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel AS marketplace_name\nFROM\n    zs_observe.unicommerce\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    marketplace_name;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins are needed as all required information is available in the `zs_observe.unicommerce` table.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Distinct `sales_channel` values.",
    "denominator": null,
    "formula": "A distinct list of marketplace names (identified by `sales_channel`) handled through Unicommerce for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary inference is that the `sales_channel` column within `zs_observe.unicommerce` directly represents the marketplace name. This is a strong and logical inference given the context of Unicommerce as an OMS for various sales channels.",
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
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_return_dump",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_sales_dump",
    "account_data_binding.aza_fashions.aza_own_platform.primary.aza_wallet_ledger",
    "account_data_binding.aza_fashions.delhivery_in.primary.delhivery_invoice",
    "account_data_binding.aza_fashions.delhivery_in.primary.delhivery_settlement",
    "account_data_binding.aza_fashions.dtdc_in.primary.dtdc_invoice",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bracheium_brand_technologies.shopify_d2c.primary.shopify_oms",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.bracheium_brand_technologies.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.bracheium_brand_technologies.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.bracheium_brand_technologies.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bracheium_brand_technologies.unicommerce_oms.primary.unicommerce"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "The `table.zs_observe.unicommerce` card explicitly lists `sales_channel` as a column, which is suitable for identifying marketplaces. The `account_data_binding.mensa.unicommerce_oms.primary.unicommerce` card confirms Mensa Brands (`group_level_id = 22`) uses this table.",
      "role": "Primary Source for Unicommerce data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Explicitly listed as a column in `table.zs_observe.unicommerce`, used to identify marketplaces.",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands', as specified in `account_data_binding.mensa.unicommerce_oms.primary.unicommerce` and confirmed as a column in `table.zs_observe.unicommerce`.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Listed as a mandatory filter in the `table.zs_observe.unicommerce` card, ensuring only active records are considered.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    }
  ],
  "selected_source": "table.zs_observe.unicommerce",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel AS marketplace_name\nFROM\n    zs_observe.unicommerce\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    marketplace_name;"
}
