## 020. Build an Average order value report per channel.

### Timing

- started_at: `2026-05-27T07:56:28+00:00`
- duration_seconds: `92.1`
- RAG_COMPLETION_seconds: `72.735`
- GRAPH_COMPLETION_seconds: `19.365`

### Query

```text
Build an Average order value report per channel.

Scope:
- tenant: Mensa Brands

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

### RAG_COMPLETION

{
  "filters": [
    {
      "column": "group_level_id",
      "operator": "=",
      "reason": "Tenant filter for Mensa Brands (applicable to LimeRoad and Myntra, if sales data exists)",
      "value": "22"
    },
    {
      "column": "is_active",
      "operator": "=",
      "reason": "Standard filter for active records (applicable to Meesho and Myntra settlement data as per patterns)",
      "value": "true"
    }
  ],
  "joins": "No joins can be established to combine data from different channels (e.g., LimeRoad, Myntra, Meesho) into a single report, as there are no explicit join keys or a unified data model across these independent sources. Cross-source consolidation via UNION is not supported without explicit deduplication and source precedence rules.",
  "metric_logic": {
    "aggregation_grain": "channel",
    "deduplication_rule": null,
    "denominator": "Total Number of Orders (inferable per individual channel)",
    "formula": "Cannot consolidate AOV per channel across disparate sources into a single report due to lack of a unified channel identifier and explicit cross-source consolidation rules.",
    "numerator": "Total Sales Amount / GMV (available per individual channel)"
  },
  "missing_or_ambiguous": "The primary blocking gap is the absence of a unified data model or explicit metadata to consolidate sales data from various marketplaces (LimeRoad, Myntra, Meesho) and assign a generic 'channel' dimension. While AOV components exist for individual channels, a single query producing an AOV report 'per channel' is not possible without violating rules against inventing literal channel names or consolidating sources without explicit instructions. Specific definitions for order count (denominator) are also not explicitly found in query patterns for all sources.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "average_order_value",
      "reason": "While components for AOV (total sales/GMV and implicitly, order counts) are present for individual channels (Meesho, Myntra, LimeRoad), there is no unified metric definition or mechanism (e.g., a common formula across all channels) to calculate a consistent AOV across all channels simultaneously."
    },
    {
      "field": "channel_identifier",
      "reason": "There is no explicit physical column that categorizes data by a generic 'channel' or 'marketplace_name' across disparate marketplace tables (LimeRoad, Myntra, Meesho). Without this, a 'per channel' report requiring a single unified query cannot be built safely using literal column names from metadata."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.limeroad_settlement",
      "reason": "Contains gross merchandise value (GMV) data for LimeRoad, which is a component for Average Order Value (AOV) calculation. However, it lacks an explicit order count for the denominator and cannot be unified with other channels for a 'per channel' report without explicit consolidation rules or a common channel identifier.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.myntra_oms",
      "reason": "Contains gross sales data for Myntra, a component for AOV. However, it lacks an explicit order count for the denominator and cannot be unified with other channels for a 'per channel' report without explicit consolidation rules or a common channel identifier.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_sales",
      "reason": "Explicitly used in the Meesho AOV formula, providing the 'charged_amount' which is the numerator. It would also implicitly provide the order count for the denominator. However, it's specific to Meesho and cannot be unified with other channels for a 'per channel' report without explicit consolidation rules or a common channel identifier.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "formula_template.meesho.average_order_value_aov",
      "reason": "Provides a direct formula for Average Order Value (AOV) specifically for Meesho, but cannot be directly applied or unified across other distinct channels for a consolidated report.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.limeroad.total_forward_gmv",
      "reason": "Indicates the metric 'gross_gmv' is available from `limeroad_settlement` for LimeRoad, which is a component of AOV. However, it does not explicitly provide order count and cannot be combined with other channels.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.gross_sales_oms",
      "reason": "Indicates 'gross_sales' is available from `myntra_oms` for Myntra, which is a component of AOV. However, it does not explicitly provide order count and cannot be combined with other channels.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to build an Average Order Value report per channel for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. There is no unified physical table or view that consolidates sales and order data from all relevant channels (e.g., LimeRoad, Myntra, Meesho) into a single source.\n-- 2. The context lacks an explicit 'channel' or 'marketplace_name' column that can be used universally across disparate sources for aggregation.\n-- 3. While individual query patterns provide ways to calculate sales amounts (e.g., GMV, gross sales) and infer order counts for AOV per channel, there are no explicit deduplication rules or source precedence guidelines to safely UNION or combine these results into a single report.\n\n-- To resolve this, a data integration layer would be required that:\n--    a) Consolidates sales and order data from all Mensa Brands' channels.\n--    b) Provides a common 'channel' or 'marketplace_name' dimension for each order.\n--    c) Clearly defines the total sales amount and the number of orders (or an AOV metric) for each channel, along with any necessary deduplication rules if combining multiple sources for the same channel type."
}

### GRAPH_COMPLETION

{
  "filters": [
    {
      "column": "group_level_id",
      "operator": "=",
      "reason": "Tenant filter for Mensa Brands, applicable to Amazon data.",
      "value": 22
    }
  ],
  "joins": "No joins can be established to combine data from different channels into a single report, as there are no explicit join keys or a unified data model across these independent sources. Cross-source consolidation via UNION is not supported without explicit deduplication and source precedence rules.",
  "metric_logic": {
    "aggregation_grain": "channel",
    "deduplication_rule": null,
    "denominator": "Total Number of Orders (per individual channel, if inferable)",
    "formula": "Cannot generate a unified AOV report 'per channel' due to the absence of a common 'channel identifier' across different data sources and lack of explicit rules for consolidating data from disparate marketplace/sales tables.",
    "numerator": "Total Sales Amount (per individual channel, if available)"
  },
  "missing_or_ambiguous": "The primary blocking gap is the absence of a unified data model or explicit metadata to consolidate sales and order data from various channels Mensa Brands operates on (e.g., Amazon, potential Shopify D2C) and assign a generic 'channel' dimension. Without a common channel identifier and explicit rules for data consolidation (e.g., deduplication keys, source precedence), a single SQL query cannot produce a comprehensive 'Average Order Value report per channel'.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "channel_identifier",
      "reason": "There is no explicit physical column that categorizes sales data by a generic 'channel' or 'marketplace_name' across disparate physical tables (e.g., Amazon OMS/Settlement). Literal enumeration or interpretation of table names as channel names is not permitted for SQL generation."
    },
    {
      "field": "average_order_value",
      "reason": "While components for AOV (total sales amount and total number of orders) can be inferred for individual channels (like Amazon for Mensa), there is no unified metric definition or explicit mechanism (e.g., common formula, deduplication rules) to calculate a consistent AOV across all channels Mensa Brands operates on for a consolidated report."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.amazon_oms",
      "reason": "This table likely contains sales and order data for Amazon, a channel Mensa Brands operates on. It could contribute to AOV for Amazon, but cannot be unified with other channels for a 'per channel' report due to lack of a common channel identifier and consolidation rules.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.amazon_settlement",
      "reason": "This table likely contains settlement data for Amazon, including sales figures. Similar to amazon_oms, it could contribute to AOV for Amazon, but cannot be unified with other channels for a 'per channel' report due to lack of a common channel identifier and consolidation rules.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.shopify_oms",
      "reason": "While Shopify OMS data exists, the provided account data bindings for Mensa Brands do not explicitly link Mensa Brands to a physical Shopify OMS table. The mention of 'shopify_d2c_prepaid_oms_to_pg' is a business flow, not a direct table binding.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.unicommerce",
      "reason": "Unicommerce data is explicitly linked to Fraternitas Ventures, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.unicommerce_order_sales_report",
      "reason": "Unicommerce data is explicitly linked to Fraternitas Ventures, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.klip_settlement",
      "reason": "Klip settlement data is explicitly linked to Prita Designs Private Limited, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.marketplace_transactions",
      "reason": "Marketplace transaction data is explicitly linked to Prita Designs Private Limited, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_sales",
      "reason": "Meesho sales data is explicitly linked to Prita Designs Private Limited, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.ajio_oms",
      "reason": "Ajio OMS data is explicitly linked to Ardeur Fashion, not Mensa Brands.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "formula_template.meesho.average_order_value_aov",
      "reason": "Provides the calculation logic for AOV for Meesho, but cannot be universally applied or consolidated across all channels for Mensa Brands due to platform-specific data structures and lack of a unified channel identifier.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to build an Average Order Value report per channel for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. There is no unified physical table or view that consolidates sales and order data from all relevant channels into a single source.\n-- 2. The context lacks an explicit 'channel' or 'marketplace_name' column that can be used universally across disparate sources for aggregation.\n-- 3. While individual query patterns provide ways to calculate sales amounts (e.g., GMV, gross sales) and infer order counts for AOV per channel, there are no explicit deduplication rules or source precedence guidelines to safely UNION or combine these results into a single report.\n\n-- To resolve this, a data integration layer would be required that:\n--    a) Consolidates sales and order data from all Mensa Brands' channels.\n--    b) Provides a common 'channel' or 'marketplace_name' dimension for each order.\n--    c) Clearly defines the total sales amount and the number of orders (or an AOV metric) for each channel, along with any necessary deduplication rules if combining multiple sources for the same channel type."
}
