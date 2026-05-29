## 006. Generate a report showing COD remittance type by courier.

### Timing

- started_at: `2026-05-27T07:43:35+00:00`
- duration_seconds: `45.245`
- RAG_COMPLETION_seconds: `30.871`
- GRAPH_COMPLETION_seconds: `14.374`

### Query

```text
Generate a report showing COD remittance type by courier.

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
    "zs_observe.shiprocket_settlement.group_level_id = 22",
    "zs_observe.shiprocket_settlement.is_active = true",
    "zs_observe.shiprocket_settlement.payment_mode = 'COD'"
  ],
  "joins": "No joins are needed as the required dimensions and filters are inferred to be available within the `zs_observe.shiprocket_settlement` table.",
  "metric_logic": {
    "aggregation_grain": "courier_partner, remittance_status",
    "deduplication_rule": "DISTINCT courier_partner, status",
    "denominator": null,
    "formula": "List distinct pairs of (courier_partner, status for COD remittance)",
    "numerator": null
  },
  "missing_or_ambiguous": "The specific column names for 'courier_partner' and 'status' (as 'remittance_type') within `zs_observe.shiprocket_settlement` are inferred based on relevant query patterns and their allowed dimensions, as explicit column cards were not provided. The exact values for 'status' representing remittance types (e.g., 'Remitted', 'Pending', 'Failed') are also inferred.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "table.zs_observe.limeroad_settlement"
  ],
  "require_tables": [
    {
      "field": "table.zs_observe.shiprocket_settlement",
      "reason": "This table is explicitly identified as a required table in `query_pattern.logistics.cod_expected_vs_remitted`, which aligns perfectly with the request for COD remittance information. It is expected to contain both courier and settlement status data.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "query_pattern.logistics.cod_expected_vs_remitted",
      "reason": "This query pattern directly addresses 'COD Expected Vs Remitted' and lists 'courier_partner', 'status', and 'payment_mode' as allowed dimensions, strongly indicating the presence of relevant data in associated tables like `zs_observe.shiprocket_settlement`.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides general operational filters including `group_level_id = 22` for Mensa Brands and `is_active = true`, which are applicable across platforms. Also contains a rule 'Do not create courier-settlement [...] from Increff alone', which guides towards logistics settlement tables.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.bank_credit_unmatched_courier_reference",
      "reason": "Mentions courier_partner and payment_mode, but 'cod_expected_vs_remitted' is more specific to the user's request.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "reason": "Required dimension for the report, inferred from `query_pattern.logistics.cod_expected_vs_remitted` allowed dimensions.",
      "role": "Dimension",
      "selected?": "Yes",
      "table": "zs_observe.shiprocket_settlement"
    },
    {
      "field": "status",
      "reason": "Represents the 'remittance type' as requested, inferred from `query_pattern.logistics.cod_expected_vs_remitted` allowed dimensions which include 'status' for logistics. This column would indicate the state of COD remittance (e.g., 'Remitted', 'Pending').",
      "role": "Dimension",
      "selected?": "Yes",
      "table": "zs_observe.shiprocket_settlement"
    },
    {
      "field": "group_level_id",
      "reason": "Tenant filter for Mensa Brands, with value 22, inferred from `execution_constraint_set.increff.operations_manifest_refactored_constraints` as a general Mensa Brands scope identifier.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.shiprocket_settlement"
    },
    {
      "field": "is_active",
      "reason": "Standard operational filter ('is_active = true') mentioned in logistics query patterns and general constraints.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.shiprocket_settlement"
    },
    {
      "field": "payment_mode",
      "reason": "Filter for COD transactions, inferred from 'COD remittance type' in the question and 'payment_mode' in `query_pattern.logistics.cod_expected_vs_remitted`.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.shiprocket_settlement"
    }
  ],
  "selected_source": "zs_observe.shiprocket_settlement",
  "sql_skeleton": "SELECT DISTINCT\n    courier_partner,\n    status AS remittance_type\nFROM\n    zs_observe.shiprocket_settlement\nWHERE\n    group_level_id = 22 AND\n    is_active = true AND\n    payment_mode = 'COD'\nORDER BY\n    courier_partner, remittance_type;"
}

### GRAPH_COMPLETION

{
  "filters": [],
  "joins": "No joins are applicable as no relevant physical tables for Mensa Brands are identified.",
  "metric_logic": {
    "aggregation_grain": "courier_partner, remittance_type",
    "deduplication_rule": null,
    "denominator": "Total number of COD transactions",
    "formula": "Count of COD remittance types by courier",
    "numerator": "Number of COD transactions with a specific remittance type"
  },
  "missing_or_ambiguous": "The current context explicitly refers to 'Prita Designs Private Limited' with `group_level_id = 24` and related Meesho/Klip tables. It lacks any physical table or associated column definitions for 'Mensa Brands' (expected `group_level_id = 22`) that would contain 'courier' information and 'COD remittance type/status'. Without these, the request for Mensa Brands cannot be fulfilled. The necessary query patterns or constraints for COD remittance by courier, which might have inferred these fields and filters, are also absent from the provided context.",
  "rejected_or_ambiguous_fields": [
    "courier_partner",
    "remittance_type/status",
    "payment_mode",
    "group_level_id"
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.klip_settlement",
      "reason": "This table is associated with Prita Designs Private Limited (group_level_id = 24), not Mensa Brands (group_level_id = 22). It also does not explicitly provide courier or COD remittance type fields for Mensa Brands within the current context.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.marketplace_transactions",
      "reason": "This table is associated with Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It's a generic marketplace transactions table and does not explicitly provide courier or COD remittance type fields for Mensa Brands within the current context.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_brand_mapping",
      "reason": "This table is for brand mapping for Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It does not contain courier or COD remittance type information.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_forward_expenses",
      "reason": "This table is for forward expenses for Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It does not contain courier or COD remittance type information.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_other_charges_expenses",
      "reason": "This table is for other charges expenses for Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It does not contain courier or COD remittance type information.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_returns",
      "reason": "This table is for returns for Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It does not contain courier or COD remittance type information.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.meesho_reverse",
      "reason": "This table is for reverse logistics for Prita Designs Private Limited (group_level_id = 24), not Mensa Brands. It does not contain courier or COD remittance type information.",
      "role": "Irrelevant Candidate",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to generate a COD remittance type by courier report for Mensa Brands cannot be fulfilled with the current context.\n-- The provided context is specific to 'Prita Designs Private Limited' and does not contain physical tables or column definitions for 'Mensa Brands' with courier and COD remittance information.\n-- To resolve this, physical table(s) containing courier and COD remittance type/status for Mensa Brands, along with the correct tenant identifier (group_level_id = 22), must be provided."
}
