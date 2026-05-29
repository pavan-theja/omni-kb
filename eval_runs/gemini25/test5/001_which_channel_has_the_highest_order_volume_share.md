## 001. Which channel has the highest order volume share?

### Timing

- started_at: `2026-05-27T07:39:08+00:00`
- duration_seconds: `62.908`
- RAG_COMPLETION_seconds: `40.526`
- GRAPH_COMPLETION_seconds: `22.382`

### Query

```text
Which channel has the highest order volume share?

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
    "zs_observe.increff_sales.metadata_2 = 'mensa brand technologies private limited'",
    "zs_observe.increff_sales.group_level_id = 22",
    "zs_observe.increff_sales.is_active = true",
    "zs_observe.jiomart_oms.group_level_id = 26",
    "zs_observe.jiomart_oms.is_active = true"
  ],
  "joins": "No joins needed between selected physical tables. UNION ALL will be used to combine data from different sources.",
  "metric_logic": {
    "aggregation_grain": "fulfilment_channel",
    "deduplication_rule": "DISTINCT order_id within each source to avoid duplicate order counts",
    "denominator": "SUM(COUNT(DISTINCT order_id)) OVER ()",
    "formula": "(COUNT(DISTINCT order_id) per channel / SUM(COUNT(DISTINCT order_id)) across all channels) * 100",
    "numerator": "COUNT(DISTINCT order_id)"
  },
  "missing_or_ambiguous": "The `group_level_id` values 22 for Increff and 26 for JioMart are inferred from their respective execution constraint sets as the scope identifiers for 'Mensa Brands' or related entities. This assumes these specific IDs correctly map to the requested tenant 'Mensa Brands'. The assumption is also made that 'order_id' is a unique identifier for orders within each system for counting purposes.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains fulfilment_channel and order data for Mensa Brands.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.jiomart_oms",
      "reason": "Contains fulfilment_channel and order data for Mensa Brands.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides filtering rules like is_active = true and group_level_id for Increff.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides filtering rules like is_active = true and group_level_id for JioMart.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "reason": "Explicitly mentioned for channel identification in both sources.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "order_id",
      "reason": "Required for counting order volume (inferred unique order identifier). It is a commonly used identifier for orders.",
      "role": "Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "group_level_id",
      "reason": "Tenant filter for both sources, resolved to specific IDs from execution constraint sets.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "metadata_2",
      "reason": "Specific tenant identifier for increff_sales as per context ('mensa brand technologies private limited').",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "is_active",
      "reason": "Common active filter specified by execution constraint sets for both platforms.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    }
  ],
  "selected_source": null
}

### GRAPH_COMPLETION

{
  "filters": [
    "zs_observe.increff_sales.metadata_2 = 'mensa brand technologies private limited'",
    "zs_observe.increff_sales.group_level_id = 22",
    "zs_observe.increff_sales.is_active = true",
    "zs_observe.increff_sales.order_status = 'COMPLETED'",
    "zs_observe.increff_sales.transaction_type = 'SALES'",
    "zs_observe.jiomart_oms.group_level_id = 26",
    "zs_observe.jiomart_oms.is_active = true"
  ],
  "joins": "No joins needed between selected physical tables. UNION ALL will be used to combine data from different sources.",
  "metric_logic": {
    "aggregation_grain": "fulfilment_channel",
    "deduplication_rule": "DISTINCT order_id within each source to avoid duplicate order counts",
    "denominator": "SUM(COUNT(DISTINCT order_id)) OVER ()",
    "formula": "(COUNT(DISTINCT order_id) per channel / SUM(COUNT(DISTINCT order_id)) across all channels) * 100",
    "numerator": "COUNT(DISTINCT order_id)"
  },
  "missing_or_ambiguous": "The `group_level_id` values 22 for Increff and 26 for JioMart are inferred from their respective execution constraint sets as the scope identifiers for 'Mensa Brands' or related entities. This assumes these specific IDs correctly map to the requested tenant 'Mensa Brands'. The assumption is also made that 'order_id' is a unique identifier for orders within each system for counting purposes. Filters `order_status = 'COMPLETED'` and `transaction_type = 'SALES'` for `increff_sales` are inferred for accurate order volume calculation from execution constraint sets.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "reason": "Contains fulfilment_channel and order data for Mensa Brands.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.jiomart_oms",
      "reason": "Contains fulfilment_channel and order data for Mensa Brands.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides filtering rules like is_active = true and group_level_id for Increff.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides filtering rules like is_active = true and group_level_id for JioMart.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "reason": "Explicitly mentioned for channel identification in both sources.",
      "role": "Channel Identifier",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "order_id",
      "reason": "Required for counting order volume (inferred unique order identifier). It is a commonly used identifier for orders.",
      "role": "Metric",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "group_level_id",
      "reason": "Tenant filter for both sources, resolved to specific IDs from execution constraint sets.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "metadata_2",
      "reason": "Specific tenant identifier for increff_sales as per context ('mensa brand technologies private limited').",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "is_active",
      "reason": "Common active filter specified by execution constraint sets for both platforms.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales, zs_observe.jiomart_oms"
    },
    {
      "field": "order_status",
      "reason": "Standard filter to count only completed orders, inferred from execution constraint sets for Increff sales data.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    },
    {
      "field": "transaction_type",
      "reason": "Standard filter to count only sales transactions, inferred from execution constraint sets for Increff sales data.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_sales"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH combined_orders AS (\n    SELECT\n        fulfilment_channel,\n        COUNT(DISTINCT order_id) AS order_volume\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        metadata_2 = 'mensa brand technologies private limited' AND\n        group_level_id = 22 AND\n        is_active = true AND\n        order_status = 'COMPLETED' AND\n        transaction_type = 'SALES'\n    GROUP BY\n        fulfilment_channel\n\n    UNION ALL\n\n    SELECT\n        fulfilment_channel,\n        COUNT(DISTINCT order_id) AS order_volume\n    FROM\n        zs_observe.jiomart_oms\n    WHERE\n        group_level_id = 26 AND\n        is_active = true\n    GROUP BY\n        fulfilment_channel\n)\nSELECT\n    fulfilment_channel,\n    order_volume,\n    order_volume * 100.0 / SUM(order_volume) OVER () AS order_volume_share\nFROM\n    combined_orders\nORDER BY\n    order_volume_share DESC\nLIMIT 1;"
}
