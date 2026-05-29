## 021. Gross sales trend across all marketplaces.

### Timing

- started_at: `2026-05-27T07:58:00+00:00`
- duration_seconds: `33.999`
- RAG_COMPLETION_seconds: `16.611`
- GRAPH_COMPLETION_seconds: `17.388`

### Query

```text
Gross sales trend across all marketplaces.

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

{"selected_source":null,"rejected_sources":[],"require_tables":[{"field":"table.zs_observe.myntra_oms","role":"Risky Candidate","selected?":"No","reason":"Contains gross sales data for Myntra. Cannot be safely consolidated with other marketplace sales data without explicit deduplication keys, source precedence, or a unified schema for cross-marketplace reporting."},{"field":"table.zs_observe.limeroad_settlement","role":"Risky Candidate","selected?":"No","reason":"Contains gross merchandise value (GMV) data for LimeRoad. Cannot be safely consolidated with other marketplace sales data without explicit deduplication keys, source precedence, or a unified schema for cross-marketplace reporting."},{"field":"query_pattern.myntra.gross_sales_oms","role":"Supporting Metadata","selected?":"No","reason":"Provides a method to calculate gross sales for Myntra, but does not provide a mechanism to combine this data with other marketplaces or a common date dimension for a unified trend report."},{"field":"query_pattern.limeroad.total_forward_gmv","role":"Supporting Metadata","selected?":"No","reason":"Provides a method to calculate GMV for LimeRoad, but does not provide a mechanism to combine this data with other marketplaces or a common date dimension for a unified trend report."},{"field":"execution_constraint_set.jiomart.marketplace_query_constraints","role":"Supporting Metadata","selected?":"No","reason":"Mentions JioMart sales metrics (total_gmv) and date fields, but cannot be safely consolidated with other marketplace data for a cross-marketplace trend report without explicit deduplication keys, source precedence, or a unified schema."}],"required_fields":[],"rejected_or_ambiguous_fields":[{"field":"marketplace_name","reason":"No explicit physical column exists to categorize sales records by a generic 'marketplace_name' across multiple marketplace tables. Literal enumeration from table names is disallowed, and there's no common identifier for grouping."},{"field":"gross_sales_metric_unified_across_marketplaces","reason":"While individual gross sales/GMV metrics are available for specific marketplaces, there is no grounded mechanism (e.g., deduplication rules, source precedence, or a common schema/date dimension) to combine these into a unified 'gross sales' metric suitable for trending across all marketplaces."},{"field":"date_dimension_unified","reason":"Date column names and granularity likely vary across marketplace tables, and no unified date dimension or explicit mapping is provided to create a consistent 'trend' across all sources."}],"metric_logic":{"formula":"Cannot calculate gross sales trend across all marketplaces; requires a unified sales metric and a common date dimension across disparate marketplace data, along with explicit consolidation rules. The ability to calculate this for individual marketplaces exists but cannot be aggregated as requested.","numerator":null,"denominator":null,"aggregation_grain":"marketplace, date","deduplication_rule":null},"filters":["group_level_id = <client_id> (as applicable per marketplace, e.g., 22 for Myntra/LimeRoad, 26 for JioMart)","is_active = true (where specified in query patterns)"],"joins":"No joins can be established for a cross-marketplace gross sales trend report due to the absence of a unified data source or explicit rules for combining disparate marketplace tables. Cross-source UNIONs are not supported without explicit consolidation rules.","missing_or_ambiguous":"The primary blocking gap is the explicit absence of a unified physical table, common 'marketplace_name' dimension, common date dimension, or clear instructions/metadata (deduplication keys, source precedence) to combine sales data from different marketplaces (Myntra, LimeRoad, JioMart, Amazon, etc.) into a single, comparable dataset for a 'gross sales trend across all marketplaces' report. Individual marketplace sales can be calculated, but not unified and trended together safely.","sql_skeleton":"-- The request to build a 'Gross sales trend across all marketplaces' report for Mensa Brands cannot be fulfilled with the current context.
-- Blocking gaps:
-- 1. There is no single physical table that consolidates gross sales data from all marketplaces Mensa Brands operates on.
-- 2. While individual marketplace tables (e.g., zs_observe.myntra_oms, zs_observe.limeroad_settlement) contain sales figures, the context does not provide explicit deduplication keys or source precedence rules to safely UNION or combine their sales metrics.
-- 3. There is no common 'marketplace_name' or 'channel_identifier' column across disparate marketplace tables that would allow for a generic cross-marketplace aggregation and grouping by marketplace.
-- 4. Date fields for trending are not explicitly unified or standardized across available marketplace sources.

-- To resolve this, a unified data source containing a 'marketplace_name' or 'channel' dimension, a standardized gross sales metric, and a consistent date field for all relevant marketplaces, along with clear consolidation rules, would be required."}

### GRAPH_COMPLETION

{"selected_source":null,"rejected_sources":[],"require_tables":[{"field":"table.zs_observe.klip_settlement","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.marketplace_transactions","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.meesho_brand_mapping","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.meesho_forward_expenses","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.meesho_other_charges_expenses","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.meesho_returns","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."},{"field":"table.zs_observe.meesho_reverse","role":"Irrelevant Candidate","selected?":"No","reason":"This table is bound to 'Prita Designs Private Limited' (group_id=9, group_level_id=24) as per the provided context, not 'Mensa Brands'."}],"required_fields":[],"rejected_or_ambiguous_fields":[{"field":"gross_sales_metric_unified_across_marketplaces","reason":"No unified gross sales metric or explicit consolidation rules are provided to combine sales data from various marketplaces into a single, trendable metric."},
{"field":"marketplace_name","reason":"No explicit physical column exists to categorize sales records by a generic 'marketplace_name' across multiple marketplace tables. Literal enumeration from table names is disallowed, and there's no common identifier for grouping."},
{"field":"date_dimension_unified","reason":"No unified date dimension or explicit mapping is provided to create a consistent 'trend' across potentially disparate marketplace sources."}
],"metric_logic":{"formula":"Cannot calculate gross sales trend across all marketplaces due to tenant mismatch and lack of unified data model for consolidation.","numerator":null,"denominator":null,"aggregation_grain":"marketplace, date","deduplication_rule":null},"filters":[],"joins":"No joins can be established for a cross-marketplace gross sales trend report due to the absence of a unified data source or explicit rules for combining disparate marketplace tables.","missing_or_ambiguous":"The primary blocking gap is that the provided context (canonical_pack_0041) only contains account data bindings for 'Prita Designs Private Limited' (group_id=9, group_level_id=24), not for the requested tenant 'Mensa Brands'. Therefore, no physical tables can be identified for the requested scope. Even if the tenant mismatch was resolved, there is no unified physical table, common 'marketplace_name' dimension, common date dimension, or clear instructions/metadata (deduplication keys, source precedence) to combine sales data from different marketplaces into a single, comparable dataset for a 'gross sales trend across all marketplaces' report. Individual marketplace sales can be calculated, but not unified and trended together safely.","sql_skeleton":"-- The request to build a 'Gross sales trend across all marketplaces' report for Mensa Brands cannot be fulfilled with the current context.
-- Blocking gaps:
-- 1. **Tenant Mismatch**: The provided context only includes `account_data_binding` cards for 'Prita Designs Private Limited' (group_id=9, group_level_id=24), not for the requested tenant 'Mensa Brands'. Therefore, no physical tables are identified for the 'Mensa Brands' scope within this context.
-- 2. **No Unified Sales Source**: There is no single physical table that consolidates gross sales data from all marketplaces Mensa Brands operates on.
-- 3. **Missing Consolidation Rules**: The context does not provide explicit deduplication keys or source precedence rules to safely UNION or combine sales metrics from different marketplace tables.
-- 4. **No Common Marketplace Identifier**: There is no common 'marketplace_name' or 'channel_identifier' column across disparate marketplace tables that would allow for generic cross-marketplace aggregation and grouping.
-- 5. **No Unified Date Dimension**: Date fields for trending are not explicitly unified or standardized across available marketplace sources.

-- To resolve this, a unified data source containing a 'marketplace_name' or 'channel' dimension, a standardized gross sales metric, and a consistent date field for all relevant marketplaces, along with clear consolidation rules and tenant-specific bindings, would be required."}
