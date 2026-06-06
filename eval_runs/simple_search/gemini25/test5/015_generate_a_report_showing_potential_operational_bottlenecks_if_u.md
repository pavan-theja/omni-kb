## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Timing

- started_at: `2026-05-27T07:52:47+00:00`
- duration_seconds: `37.662`
- RAG_COMPLETION_seconds: `29.164`
- GRAPH_COMPLETION_seconds: `8.497`

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

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
  "filters": [],
  "joins": "No joins can be defined because the core system (Unicommerce) and its operational dependencies are not identified in the context.",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": "Cannot identify or quantify operational bottlenecks due to Unicommerce unavailability, as Unicommerce's role and its integration points within Mensa Brands' operations are not described in the provided context.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of any mention of 'Unicommerce' in the provided context. To identify potential operational bottlenecks if Unicommerce becomes unavailable, information about Unicommerce's role within Mensa Brands' systems (e.g., as an OMS, WMS, or integration platform), its dependencies, and the data sources/processes it controls is critically missing. Without this information, it is impossible to determine what operations would be impacted.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides constraints for Increff operations data, which is a major operational system for Mensa Brands. This context, while not mentioning Unicommerce, helps define what operational data *is* available (Increff) but does not explain dependencies on other systems like Unicommerce.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides constraints for JioMart marketplace data. Similar to Increff, this defines an operational data source but does not link it to Unicommerce or potential bottlenecks due to its unavailability.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.logistics_batch_to_bank",
      "reason": "Provides constraints for logistics reconciliation patterns, which are part of operations. However, it does not mention Unicommerce as a component or source of bottlenecks.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. There is no mention of 'Unicommerce' in the provided context, making it impossible to identify its role or dependencies within Mensa Brands' operations.\n-- 2. No specific data sources or metrics related to 'Unicommerce unavailability' or its impact on operational bottlenecks are available.\n\n-- To resolve this, context explicitly defining Unicommerce's function, the data it manages or processes, and its integration points with other systems (like Increff, marketplaces, logistics providers) would be required."
}

### GRAPH_COMPLETION

{
  "filters": [],
  "joins": "No joins can be defined because the core system (Unicommerce) and its operational dependencies are not identified in the context.",
  "metric_logic": {
    "aggregation_grain": null,
    "deduplication_rule": null,
    "denominator": null,
    "formula": "Cannot identify or quantify operational bottlenecks due to Unicommerce unavailability, as Unicommerce's role and its integration points within Mensa Brands' operations are not described in the provided context.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of any mention of 'Unicommerce' in the provided context. To identify potential operational bottlenecks if Unicommerce becomes unavailable, information about Unicommerce's role within Mensa Brands' systems (e.g., as an OMS, WMS, or integration platform), its dependencies, and the data sources/processes it controls is critically missing. Without this information, it is impossible to determine what operations would be impacted.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides constraints for Increff operations data, which is a major operational system for Mensa Brands. This context, while not mentioning Unicommerce, helps define what operational data *is* available (Increff) but does not explain dependencies on other systems like Unicommerce.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides constraints for JioMart marketplace data. Similar to Increff, this defines an operational data source but does not link it to Unicommerce or potential bottlenecks due to its unavailability.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.logistics_batch_to_bank",
      "reason": "Provides constraints for logistics reconciliation patterns, which are part of operations. However, it does not mention Unicommerce as a component or source of bottlenecks.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. There is no mention of 'Unicommerce' in the provided context, making it impossible to identify its role or dependencies within Mensa Brands' operations.\n-- 2. No specific data sources or metrics related to 'Unicommerce unavailability' or its impact on operational bottlenecks are available.\n\n-- To resolve this, context explicitly defining Unicommerce's function, the data it manages or processes, and its integration points with other systems (like Increff, marketplaces, logistics providers) would be required."
}
