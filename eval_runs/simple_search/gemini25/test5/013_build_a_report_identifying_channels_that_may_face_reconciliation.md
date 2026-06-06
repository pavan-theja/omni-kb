## 013. Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

### Timing

- started_at: `2026-05-27T07:49:52+00:00`
- duration_seconds: `84.401`
- RAG_COMPLETION_seconds: `70.101`
- GRAPH_COMPLETION_seconds: `14.3`

### Query

```text
Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

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
    "group_level_id = 26 (for JioMart, as Mensa Brands' scope identifier for this platform)",
    "is_active = true (general operational filter)"
  ],
  "joins": "Joining `zs_observe.jiomart_oms` and `zs_observe.jiomart_settlement` on `order_id` (as per `jiomart_marketplace_query_constraints.join_constraints`) would be necessary to identify unreconciled items for JioMart.",
  "metric_logic": {
    "aggregation_grain": "marketplace_channel",
    "deduplication_rule": null,
    "denominator": null,
    "formula": "Count of orders that are present in the OMS but not (yet) in settlement, or vice versa, for a given marketplace, indicating reconciliation discrepancies.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the absence of explicit physical columns that directly represent a generic 'channel_name' or 'marketplace_name' as a data value across multiple sources. Although reconciliation-related patterns are hinted at for JioMart, and settlement tables for LimeRoad exist, a unified way to report reconciliation delays across various marketplaces with their respective channel names as queryable data is not available. Also, specific columns for 'reconciliation delay' duration are not found, only implications of 'unreconciled' status. To fulfill the request comprehensively, a cross-marketplace reconciliation summary table with explicit channel identifiers and delay metrics would be required.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "channel_name",
      "reason": "No explicit physical column exists to represent a generic 'channel_name' across multiple marketplace tables. Inferring channel names from table names (e.g., 'jiomart_settlement' -> 'JioMart') is explicitly disallowed by core rules ('Do not create SQL rows from retrieved metadata using literal SELECT statements')."
    },
    {
      "field": "reconciliation_delay_metric",
      "reason": "While query patterns for JioMart suggest metrics for \"unreconciled orders\" or \"settlement_oms_reconciliation\", specific columns indicating a 'delay' duration or a numerical 'reconciliation delay metric' are not explicitly named in the context."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.jiomart_oms",
      "reason": "This table is implied to contain OMS data for JioMart. It would be a source for orders to be reconciled with settlement data, but its existence and schema are inferred, not explicitly detailed. Additionally, for a cross-marketplace report, this table alone is insufficient without a common channel identifier.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.jiomart_settlement",
      "reason": "This table is implied to contain settlement data for JioMart, based on query patterns and constraints. It would be a source for reconciliation, but its existence and schema are inferred, not explicitly detailed. Without explicit columns for reconciliation status or delays, and a generic channel identifier, it cannot directly fulfill the report request across channels.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.limeroad_settlement",
      "reason": "Contains settlement data for LimeRoad. While a marketplace, the provided context does not explicitly mention any reconciliation status fields or query patterns directly indicating \"reconciliation delays\" for this specific table.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.shiprocket_oms",
      "reason": "A logistics OMS, not a marketplace settlement source directly related to reconciliation delays caused by marketplace-based settlements.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.shiprocket_settlement",
      "reason": "A logistics settlement table, not a marketplace settlement source directly related to reconciliation delays caused by marketplace-based settlements.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.delhivery_settlement",
      "reason": "A courier settlement table. While related to logistics reconciliation, it does not directly address \"marketplace-based settlements\" or contain marketplace channel identifiers for this report.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.dtdc_settlement",
      "reason": "A courier settlement table. While related to logistics reconciliation, it does not directly address \"marketplace-based settlements\" or contain marketplace channel identifiers for this report.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.ekart_settlement",
      "reason": "A courier settlement table. While related to logistics reconciliation, it does not directly address \"marketplace-based settlements\" or contain marketplace channel identifiers for this report.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement",
      "reason": "This query pattern directly implies the existence of a metric for unreconciled orders for JioMart, which is relevant to identifying reconciliation delays. However, it's a pattern, not a physical table for direct querying.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation",
      "reason": "This query pattern suggests reconciliation analysis for JioMart settlements against OMS data, but is not a physical table.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides critical constraints and mentions required filters and join keys for JioMart OMS and settlement data, indicating the potential for reconciliation analysis for this specific marketplace.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to build a report identifying channels facing reconciliation delays due to marketplace-based settlements cannot be fully resolved with the current context.\n-- Blocking gaps:\n-- 1. No explicit physical column exists to represent a generic 'channel_name' across multiple marketplace tables. Creating literal channel names from table metadata is disallowed.\n-- 2. No single data source provides a consolidated view of reconciliation status or delays across all marketplaces for Mensa Brands.\n-- 3. While query patterns for JioMart suggest reconciliation analysis (e.g., 'unreconciled oms orders not in settlement'), a specific metric for 'reconciliation delay' (e.g., duration in days) is not identified.\n\n-- To enable this report, a unified view with a 'channel_name' column (populated from a physical source, not metadata literals), and explicit metrics for reconciliation status and delay across all relevant marketplaces would be required. This could involve a master channel mapping table or direct channel identifiers within each marketplace's reconciliation data."
}

### GRAPH_COMPLETION

{"selected_source":null,"rejected_sources":[],"require_tables":[{"field":"table.zs_observe.jiomart_oms","role":"Risky Candidate","selected?":"No","reason":"This table is implied to contain OMS data for JioMart. Its existence and schema are inferred. It lacks explicit channel identifiers for cross-marketplace reporting and specific reconciliation delay metrics."},{"field":"table.zs_observe.jiomart_settlement","role":"Risky Candidate","selected?":"No","reason":"This table is implied to contain settlement data for JioMart. Its existence and schema are inferred. It lacks explicit channel identifiers for cross-marketplace reporting and specific reconciliation delay metrics."},{"field":"table.zs_observe.limeroad_settlement","role":"Risky Candidate","selected?":"No","reason":"Contains settlement data for LimeRoad, but lacks explicit fields for reconciliation status, delays, or a general channel identifier for cross-marketplace analysis."},{"field":"table.zs_observe.shiprocket_oms","role":"Risky Candidate","selected?":"No","reason":"A logistics OMS, not directly related to marketplace settlement reconciliation delays across multiple channels."},{"field":"table.zs_observe.shiprocket_settlement","role":"Risky Candidate","selected?":"No","reason":"A logistics settlement table, not directly related to marketplace settlement reconciliation delays across multiple channels."},{"field":"table.zs_observe.delhivery_settlement","role":"Risky Candidate","selected?":"No","reason":"A courier settlement table; contains courier info but lacks marketplace channel identifiers or explicit reconciliation delay metrics."},{"field":"table.zs_observe.dtdc_settlement","role":"Risky Candidate","selected?":"No","reason":"A courier settlement table; contains courier info but lacks marketplace channel identifiers or explicit reconciliation delay metrics."},{"field":"table.zs_observe.ekart_settlement","role":"Risky Candidate","selected?":"No","reason":"A courier settlement table; contains courier info but lacks marketplace channel identifiers or explicit reconciliation delay metrics."},{"field":"query_pattern.jiomart.marketplace.7_3_unreconciled_oms_orders_not_in_settlement","role":"Supporting Metadata","selected?":"No","reason":"This pattern indicates a relevant metric for JioMart, but it's a pattern, not a physical table for direct querying, and is marketplace-specific."},{"field":"query_pattern.jiomart.settlement.8_3_settlement_oms_reconciliation","role":"Supporting Metadata","selected?":"No","reason":"This pattern suggests reconciliation analysis for JioMart, but it's a pattern, not a physical table, and is marketplace-specific."},{"field":"execution_constraint_set.jiomart.marketplace_query_constraints","role":"Supporting Metadata","selected?":"No","reason":"Provides constraints for JioMart, suggesting reconciliation is possible for this specific marketplace, but does not generalize to a cross-marketplace report."}],"required_fields":[],"rejected_or_ambiguous_fields":[{"field":"channel_name","reason":"No explicit physical column exists to represent a generic 'channel_name' across multiple marketplace tables for Mensa Brands. Generating literal strings from table names is disallowed."},{"field":"reconciliation_delay_metric","reason":"While some query patterns imply unreconciled states for specific marketplaces (JioMart), an explicit physical column for a quantifiable 'reconciliation delay' (e.g., duration) is not identified."}],"metric_logic":{"formula":"Count of orders/transactions with reconciliation discrepancies (e.g., OMS orders not in settlement) per marketplace channel.","numerator":null,"denominator":null,"aggregation_grain":"marketplace_channel","deduplication_rule":null},"filters":["group_level_id = 26 (for JioMart, as an example for Mensa Brands' scope)","is_active = true (general operational filter)"],"joins":"Joining specific OMS and settlement tables (e.g., `zs_observe.jiomart_oms` and `zs_observe.jiomart_settlement`) on `order_id` could identify unreconciled items for a single marketplace. However, a cross-marketplace join is not supported due to missing common channel identifiers and data structure.","missing_or_ambiguous":"The primary blocking gap is the absence of explicit physical columns that directly represent a generic 'channel_name' or 'marketplace_name' as a data value across multiple marketplace settlement sources for Mensa Brands. This prevents a consolidated, cross-marketplace report. Additionally, specific columns for 'reconciliation delay' duration are not found, only implications of 'unreconciled' status for individual marketplaces. A unified data model with explicit channel identifiers and delay metrics is required for a comprehensive report.","sql_skeleton":"-- The request to build a report identifying channels that may face reconciliation delays due to marketplace-based settlements cannot be fully resolved with the current context.
-- Blocking gaps:
-- 1. No explicit physical column exists to represent a generic 'channel_name' across multiple marketplace tables. Creating literal channel names from table metadata is disallowed.
-- 2. No single physical data source provides a consolidated view of reconciliation status or delays across all marketplaces for Mensa Brands.
-- 3. While query patterns for JioMart suggest reconciliation analysis, a specific metric for 'reconciliation delay' (e.g., duration in days) is not identified across relevant data sources.

-- To enable this report, a unified view with a 'channel_name' column (populated from a physical source, not metadata literals) and explicit metrics for reconciliation status and delay across all relevant marketplaces would be required. This could involve a master channel mapping table or direct channel identifiers within each marketplace's reconciliation data."}
