## 003. List all marketplaces handled through Unicommerce.

### Timing

- started_at: `2026-05-27T07:40:35+00:00`
- duration_seconds: `38.372`
- RAG_COMPLETION_seconds: `24.588`
- GRAPH_COMPLETION_seconds: `13.784`

### Query

```text
List all marketplaces handled through Unicommerce.

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
    "group_level_id = 22 (for Mensa Brands tenant scope, inferred from Unicommerce account data bindings)"
  ],
  "joins": "No joins can be formed as the primary dimension (marketplace name) is missing from the identified Unicommerce tables.",
  "metric_logic": {
    "aggregation_grain": "marketplace",
    "deduplication_rule": "DISTINCT marketplace_name",
    "denominator": null,
    "formula": "LIST(DISTINCT marketplace_name)",
    "numerator": null
  },
  "missing_or_ambiguous": "Missing a physical column in `zs_observe.unicommerce` or `zs_observe.unicommerce_order_sales_report` that explicitly names the marketplaces handled through Unicommerce. The existing context only confirms Unicommerce is a platform used by Mensa Brands, but not which *marketplaces* it integrates with for this tenant.",
  "rejected_or_ambiguous_fields": [
    "The context identifies `table.zs_observe.unicommerce` and `table.zs_observe.unicommerce_order_sales_report` as physical tables related to Unicommerce for 'Mensa Brands' (filtered by `group_level_id = 22`). However, no specific column within these tables or related metadata is provided that explicitly lists the 'marketplaces handled through Unicommerce'. The query patterns and account data bindings confirm Unicommerce operations but do not expose a list of distinct marketplace names as a queryable dimension."
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.unicommerce",
      "reason": "Identified as a Unicommerce physical table for Mensa Brands, but lacks a specific column to list marketplaces.",
      "role": "Primary Source",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.unicommerce_order_sales_report",
      "reason": "Identified as a Unicommerce physical table for Mensa Brands, but lacks a specific column to list marketplaces.",
      "role": "Primary Source",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.unicommerce_oms.primary.unicommerce",
      "reason": "Provides scope for Mensa Brands for Unicommerce data but does not contain marketplace names directly.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.unicommerce_oms.primary.unicommerce_order_sales_report",
      "reason": "Provides scope for Mensa Brands for Unicommerce data but does not contain marketplace names directly.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "marketplace_name",
      "reason": "A physical column explicitly listing marketplace names handled through Unicommerce for Mensa Brands is not identified in the context.",
      "role": "Dimension",
      "selected?": "No",
      "table": "N/A"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "-- SELECT DISTINCT marketplace_name\n-- FROM <missing_unicommerce_marketplace_table>\n-- WHERE group_level_id = 22;\n-- \n-- The context does not provide a physical table or column within Unicommerce data (e.g., zs_observe.unicommerce or zs_observe.unicommerce_order_sales_report) that lists the distinct marketplaces handled by Unicommerce for 'Mensa Brands'. The existing Unicommerce bindings for Mensa Brands (`group_level_id = 22`) confirm Unicommerce's use but lack the specific marketplace dimension to fulfill the request."
}

### GRAPH_COMPLETION

{"selected_source":null,"rejected_sources":[],"require_tables":[{"field":"table.zs_observe.unicommerce","role":"Primary Source","selected?":"No","reason":"Identified as a Unicommerce physical table for Mensa Brands within the 'Operations WMS' scope, but the context does not explicitly provide a column to list marketplace names."},{"field":"table.zs_observe.unicommerce_order_sales_report","role":"Primary Source","selected?":"No","reason":"Identified as a Unicommerce physical table for Mensa Brands within the 'Operations WMS' scope, but the context does not explicitly provide a column to list marketplace names."},{"field":"account_data_binding.mensa.unicommerce_oms.primary","role":"Supporting Metadata","selected?":"No","reason":"Indicates Unicommerce data exists for Mensa Brands but does not directly bind to a table with marketplace names."},{"field":"business_scope_set.mensa_brands.operations_wms","role":"Supporting Metadata","selected?":"No","reason":"Confirms Unicommerce is used by Mensa Brands for OMS/WMS operations, but does not provide details on specific marketplace names or a physical column to query them."}
],"required_fields":[{"field":"marketplace_name","table":"N/A","role":"Dimension","selected?":"No","reason":"A physical column explicitly listing marketplace names handled through Unicommerce for Mensa Brands is not identified in the context."}
],"rejected_or_ambiguous_fields":["The context indicates that Unicommerce is used by Mensa Brands (via 'Operations WMS' scope), and Unicommerce tables are identified (e.g., zs_observe.unicommerce), but there is no specific column provided within these tables or related metadata that explicitly lists the 'marketplaces handled through Unicommerce' for Mensa Brands. The available account data bindings for Mensa Brands do not directly link to Unicommerce tables with a marketplace dimension. Furthermore, the Unicommerce tables mentioned in the context are associated with 'Fraternitas Ventures' with different group_level_ids."
],"metric_logic":{"formula":null,"numerator":null,"denominator":null,"aggregation_grain":null,"deduplication_rule":null},"filters":["Tenant: Mensa Brands (implicitly group_level_id = 22, inferred from other Mensa Brand account data bindings, but cannot be applied due to missing marketplace column)"
],"joins":"No joins can be formed as the primary dimension (marketplace name) is missing from the identified Unicommerce tables and no explicit physical tables for Mensa Brands' Unicommerce data are sufficiently detailed in the context.","missing_or_ambiguous":"Missing a physical column in any Unicommerce-related table for Mensa Brands that explicitly names the marketplaces handled through Unicommerce. While Unicommerce is recognized as a platform for Mensa Brands, the specific data elements required to list marketplaces are not available in the provided context.","sql_skeleton":"-- Listing marketplaces handled through Unicommerce for Mensa Brands cannot be fulfilled.
-- The provided context does not contain physical tables or columns that explicitly store or identify the 'marketplace name' for Unicommerce data specific to 'Mensa Brands'.
-- To generate this report, a physical table containing a 'marketplace_name' column or similar identifier, applicable to Mensa Brands' Unicommerce operations, would be required."}
