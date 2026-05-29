## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-28T11:32:35+00:00`
- duration_seconds: `80.533`
- GRAPH_COMPLETION_seconds: `80.533`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

You are a SQL-resolution handoff agent. Do not answer the business question directly. Produce the safest SQL-building plan that the retrieved context can support.

Resolution flow:
1. Identify the requested grain, metric/status logic, dimensions, filters, joins, and tenant/account scope.
2. Resolve sources in this order:
   - tenant/account scope from user input
   - account_data_binding/platform_account only to identify candidate platforms and source bindings
   - physical table cards for those bindings
   - column cards for selected physical tables
   - relationship cards for join keys between selected physical tables
   - query_pattern cards only to reuse grounded SQL logic
   - business_flow_binding/business_process only for process context if table/relationship context is insufficient
3. Stop once when enough physical tables are identified to answer the query safely.
4. Classify candidates as direct, supporting, risky, or irrelevant.
5. Select the smallest safe SQL package. If no safe package exists, return a partial/risky handoff with blocking gaps.

Core rules:
- Prefer physical SQL tables and columns explicitly grounded in context.
- Prefer the smallest complete physical table set; avoid expanding into every retrieved artifact.
- Do not default to the most detailed retrieved source if the user asks about channels, marketplaces, settlements, reconciliation, risk, bottlenecks, dependency, concentration, courier mapping, OMS dependency, or marketplace-wide reporting.
- For channel/marketplace questions, enumerate candidate platforms/sources first, then select only the physical tables needed per package.
- Do not treat one marketplace such as Myntra, Amazon, Flipkart, Ajio, Nykaa, Meesho, Snapdeal, TataCliq, JioMart, HealthKart, or LimeRoad as representative of all marketplaces unless the user explicitly asks for that marketplace or the context proves it is the only applicable source.
- Do not UNION or numerically consolidate multiple source tables unless the user asks for cross-source/all-source/platform-wide consolidation and the context provides deduplication keys plus source precedence.
- Do not create SQL rows from retrieved metadata using literal SELECT statements such as `SELECT 'Meesho' AS channel_name`.
- `sql_skeleton` must query physical runtime tables only.
- If no physical table path is grounded, set `selected_source = null` and make `sql_skeleton` a SQL comment explaining missing physical tables, columns, joins, or deduplication rules.
- Do not generate qualitative metadata reports as executable SQL.
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

Selected table rule:
- In `require_tables`, mark `selected? = Yes` only for physical SQL tables used in `sql_skeleton`.
- Canonical metadata, query patterns, rules, value profiles, relationships, and business flows must be `selected? = No` unless they resolve to a physical table used in the SQL.
- Supporting metadata can appear in `require_tables`, but only with `selected? = No`.
- If a source is useful only as evidence for table/field selection, keep it out of `selected_source`.

Output rules:
- Return one best SQL package in the schema below.
- Use `require_tables` to show selected physical tables and important rejected/risky/supporting candidates.
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
      "table": "which physical table or tables this field comes from",
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
}
```

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = 22"
  ],
  "joins": "LEFT JOIN on sales_channel between aggregated sales and returns summary CTEs.",
  "metric_logic": {
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "Grounded aggregation per sales_channel to avoid cartesian products.",
    "denominator": "None",
    "formula": "Unified aggregation of sales value, order count, return count, and return rate per sales channel.",
    "numerator": "SUM(charged_amount), COUNT(DISTINCT channel_order_id), COUNT(DISTINCT channel_return_id)"
  },
  "missing_or_ambiguous": "None",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "zs_observe.meesho_sales",
    "zs_observe.meesho_returns",
    "zs_observe.shopify_oms",
    "zs_observe.shiprocket_oms"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Consolidated physical sales table managed via Increff OMS/WMS for Mensa Brands, containing courier mappings.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_returns",
      "reason": "Consolidated physical returns table managed via Increff OMS/WMS for Mensa Brands, containing return ownership models (fulfillment types).",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.meesho_sales",
      "reason": "Channel-specific sales table, not suitable for unified dashboard.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "reason": "Identifies the marketplace/sales channel.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "fulfilment_channel",
      "reason": "Identifies the courier/logistics partner.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "charged_amount",
      "reason": "Used to calculate sales value.",
      "role": "Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "channel_order_id",
      "reason": "Used to count order volumes.",
      "role": "Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "fulfillment_type",
      "reason": "Identifies the return ownership/handling model (e.g. merchant vs marketplace managed).",
      "role": "Status Field",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "channel_return_id",
      "reason": "Used to count return volumes.",
      "role": "Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "group_level_id",
      "reason": "Filters data specifically for the Mensa tenant (group_level_id = 22).",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "Multiple tables"
    }
  ],
  "selected_source": "zs_observe.increff_sales",
  "sql_skeleton": "WITH sales_summary AS (\n  SELECT\n    sales_channel,\n    'Increff' AS oms_system,\n    COUNT(DISTINCT channel_order_id) AS total_orders,\n    SUM(charged_amount) AS total_sales,\n    MAX(fulfilment_channel) AS primary_courier\n  FROM zs_observe.increff_sales\n  WHERE group_level_id = 22 AND sales_channel IS NOT NULL\n  GROUP BY 1, 2\n),\nreturns_summary AS (\n  SELECT\n    sales_channel,\n    MAX(fulfillment_type) AS return_ownership_model,\n    COUNT(DISTINCT channel_return_id) AS total_returns\n  FROM zs_observe.increff_returns\n  WHERE group_level_id = 22 AND sales_channel IS NOT NULL\n  GROUP BY 1\n)\nSELECT\n  s.sales_channel,\n  s.oms_system,\n  s.primary_courier,\n  r.return_ownership_model,\n  s.total_orders,\n  s.total_sales,\n  COALESCE(r.total_returns, 0) AS total_returns,\n  COALESCE(r.total_returns, 0) * 100.0 / NULLIF(s.total_orders, 0) AS return_rate_pct\nFROM sales_summary s\nLEFT JOIN returns_summary r ON s.sales_channel = r.sales_channel\nORDER BY s.total_sales DESC;"
}
