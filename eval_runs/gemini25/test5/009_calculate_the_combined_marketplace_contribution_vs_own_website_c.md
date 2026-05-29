## 009. Calculate the combined marketplace contribution vs own website contribution.

### Timing

- started_at: `2026-05-27T07:46:46+00:00`
- duration_seconds: `48.804`
- RAG_COMPLETION_seconds: `22.372`
- GRAPH_COMPLETION_seconds: `26.431`

### Query

```text
Calculate the combined marketplace contribution vs own website contribution.

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
    "group_level_id = 22 (for Mensa Brands)",
    "is_active = true (where applicable)"
  ],
  "joins": "No joins can be defined because the core dimensions ('marketplace' vs. 'own website') for comparison are missing or ungrounded across disparate data sources.",
  "metric_logic": {
    "aggregation_grain": "marketplace_vs_own_website_category",
    "deduplication_rule": "Sum of contributions after categorization",
    "denominator": null,
    "formula": "Sum of sales/revenue/GMV, categorized by 'marketplace' vs. 'own website'",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of a unified data model or explicit columns/flags that would allow for a distinction between 'marketplace contribution' and 'own website contribution'. While data for specific marketplaces like Myntra and LimeRoad is present, there is no generic 'marketplace' categorization to combine them, and no data source whatsoever for 'own website' sales. Therefore, the requested comparative report cannot be generated.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "marketplace_vs_own_website_category_field",
      "reason": "There is no explicit column or logical rule within the provided context to categorize sales/contribution records as either belonging to a 'marketplace' or 'own website'. While specific marketplace data sources (Myntra, LimeRoad) are identified, there's no unified dimension to group them as 'combined marketplace' or identify any 'own website' data."
    },
    {
      "field": "combined_marketplace_contribution_metric",
      "reason": "While metrics like `gross_sales` or `total_forward_gmv` exist for individual marketplaces (e.g., Myntra, LimeRoad), there's no defined method or consolidating table to sum these into a single 'combined marketplace contribution' metric across all marketplaces Mensa Brands operates on, nor to compare it against a non-existent 'own website' metric."
    },
    {
      "field": "own_website_contribution_metric",
      "reason": "There is no identifiable physical table, column, or query pattern in the provided context that directly or indirectly captures sales, GMV, or contribution specifically from Mensa Brands' 'own website'."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.myntra_oms",
      "reason": "This table, used by `query_pattern.myntra.gross_sales_oms`, contains gross sales for Myntra (a marketplace). While it contributes to 'marketplace contribution', there's no mechanism to combine it with other marketplace data or to distinguish it from 'own website' sales in a broader context. It represents only one marketplace, not 'combined marketplace'.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.myntra_settlement",
      "reason": "This table is used for Myntra-specific settlement metrics. Similar to `myntra_oms`, it relates to a single marketplace but cannot fulfill the 'combined marketplace vs own website' comparison due to lack of a unifying dimension and data for other channels.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.limeroad_settlement",
      "reason": "This table is used for LimeRoad-specific GMV (`query_pattern.limeroad.total_forward_gmv`). It represents another single marketplace, but without a consolidated view or an 'own website' source, it cannot answer the overall comparison.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.gross_sales_oms",
      "reason": "Identifies `zs_observe.myntra_oms` as a source for gross sales from a marketplace for Mensa Brands, but doesn't solve the 'combined' or 'own website' aspect.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.net_settlement",
      "reason": "Identifies `zs_observe.myntra_settlement` as a source for net settlement from a marketplace for Mensa Brands, but doesn't provide a general solution.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.limeroad.total_forward_gmv",
      "reason": "Identifies `zs_observe.limeroad_settlement` as a source for GMV from a marketplace for Mensa Brands, but doesn't provide a general solution.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to calculate combined marketplace contribution versus own website contribution for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. Absence of a general field or mechanism to categorize sales records as either 'marketplace' or 'own website'. Specific marketplace tables (e.g., zs_observe.myntra_oms, zs_observe.limeroad_settlement) exist, but there's no consolidated view.\n-- 2. No identifiable data source (physical table or column) for 'own website contribution' at all.\n-- 3. No defined method to combine metrics from disparate marketplace tables into a single 'combined marketplace contribution'.\n\n-- To resolve this, a consolidated sales/revenue table is needed, with a clear 'channel_type' or similar column distinguishing 'marketplace' (and specific marketplace names) from 'own website'. Alternatively, separate, identifiable tables for 'own website' sales and a mechanism to unify or compare them with marketplace data would be required."
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = 22 (for Mensa Brands)",
    "is_active = true (where applicable)"
  ],
  "joins": "No joins can be defined because the core dimensions ('marketplace' vs. 'own website') for comparison are missing or ungrounded across disparate data sources.",
  "metric_logic": {
    "aggregation_grain": "marketplace_vs_own_website_category",
    "deduplication_rule": "Sum of contributions after categorization",
    "denominator": null,
    "formula": "Sum of sales/revenue/GMV, categorized by 'marketplace' vs. 'own website'",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of a unified data model or explicit columns/flags that would allow for a distinction between 'marketplace contribution' and 'own website contribution'. While data for specific marketplaces like Myntra and LimeRoad is present, there is no generic 'marketplace' categorization to combine them, and no data source whatsoever for 'own website' sales. Therefore, the requested comparative report cannot be generated.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "marketplace_vs_own_website_category_field",
      "reason": "There is no explicit column or logical rule within the provided context to categorize sales/contribution records as either belonging to a 'marketplace' or 'own website'. While specific marketplace data sources (Myntra, LimeRoad) are identified, there's no unified dimension to group them as 'combined marketplace' or identify any 'own website' data."
    },
    {
      "field": "combined_marketplace_contribution_metric",
      "reason": "While metrics like `gross_sales` or `total_forward_gmv` exist for individual marketplaces (e.g., Myntra, LimeRoad), there's no defined method or consolidating table to sum these into a single 'combined marketplace contribution' metric across all marketplaces Mensa Brands operates on, nor to compare it against a non-existent 'own website' metric."
    },
    {
      "field": "own_website_contribution_metric",
      "reason": "There is no identifiable physical table, column, or query pattern in the provided context that directly or indirectly captures sales, GMV, or contribution specifically from Mensa Brands' 'own website'."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.myntra_oms",
      "reason": "This table, used by `query_pattern.myntra.gross_sales_oms`, contains gross sales for Myntra (a marketplace). While it contributes to 'marketplace contribution', there's no mechanism to combine it with other marketplace data or to distinguish it from 'own website' sales in a broader context. It represents only one marketplace, not 'combined marketplace'.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.myntra_settlement",
      "reason": "This table is used for Myntra-specific settlement metrics. Similar to `myntra_oms`, it relates to a single marketplace but cannot fulfill the 'combined marketplace vs own website' comparison due to lack of a unifying dimension and data for other channels.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.limeroad_settlement",
      "reason": "This table is used for LimeRoad-specific GMV (`query_pattern.limeroad.total_forward_gmv`). It represents another single marketplace, but without a consolidated view or an 'own website' source, it cannot answer the overall comparison.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.gross_sales_oms",
      "reason": "Identifies `zs_observe.myntra_oms` as a source for gross sales from a marketplace for Mensa Brands, but doesn't solve the 'combined' or 'own website' aspect.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.net_settlement",
      "reason": "Identifies `zs_observe.myntra_settlement` as a source for net settlement from a marketplace for Mensa Brands, but doesn't provide a general solution.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.limeroad.total_forward_gmv",
      "reason": "Identifies `zs_observe.limeroad_settlement` as a source for GMV from a marketplace for Mensa Brands, but doesn't provide a general solution.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to calculate combined marketplace contribution versus own website contribution for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. Absence of a general field or mechanism to categorize sales records as either 'marketplace' or 'own website'. Specific marketplace tables (e.g., zs_observe.myntra_oms, zs_observe.limeroad_settlement) exist, but there's no consolidated view.\n-- 2. No identifiable data source (physical table or column) for 'own website contribution' at all.\n-- 3. No defined method to combine metrics from disparate marketplace tables into a single 'combined marketplace contribution'.\n\n-- To resolve this, a consolidated sales/revenue table is needed, with a clear 'channel_type' or similar column distinguishing 'marketplace' (and specific marketplace names) from 'own website'. Alternatively, separate, identifiable tables for 'own website' sales and a mechanism to unify or compare them with marketplace data would be required."
}
