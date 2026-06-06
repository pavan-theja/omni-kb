## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Timing

- started_at: `2026-05-27T07:54:04+00:00`
- duration_seconds: `59.285`
- RAG_COMPLETION_seconds: `42.028`
- GRAPH_COMPLETION_seconds: `17.257`

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

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
    "group_level_id = 22 (for Mensa Brands in Increff and LimeRoad contexts)",
    "group_level_id = 26 (for Mensa Brands in JioMart context)",
    "is_active = true (where applicable)"
  ],
  "joins": "No joins can be established to create a unified dashboard across such diverse operational areas (sales, OMS, logistics, returns) and different channels (own website, various marketplaces) due to a lack of explicit, universally applicable join keys or a consolidated data model. Cross-source unions are not supported without explicit deduplication and precedence rules.",
  "metric_logic": {
    "aggregation_grain": "channel",
    "deduplication_rule": null,
    "denominator": null,
    "formula": "Cannot generate a unified dashboard as the underlying metrics (sales, OMS dependency, courier dependency, return ownership) and channel identification are disparate and lack a common, joinable data model across all required domains and platforms for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of a unified data model or explicit physical columns that can combine sales, OMS dependency, courier dependency, and return ownership across 'own website' and multiple marketplace channels for Mensa Brands. Each of these components either resides in separate, unjoined systems, lacks a common channel identifier for aggregation, or is a qualitative concept not quantifiable by available data. Safe cross-source consolidation is not supported by the context.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "unified_channel_identifier",
      "reason": "There is no explicit physical column that categorizes data universally across 'own website' and various marketplace channels to allow a consolidated view."
    },
    {
      "field": "oms_dependency_metric",
      "reason": "The concept of 'OMS dependency' is not defined as a quantifiable metric in the context, nor is there a unified OMS data source across all channels."
    },
    {
      "field": "courier_dependency_metric",
      "reason": "The concept of 'courier dependency' is not defined as a quantifiable metric that can be unified with sales or OMS data across all channels."
    },
    {
      "field": "return_ownership_metric",
      "reason": "The concept of 'return ownership' is qualitative and not represented by a physical column or derived metric that can be easily compared or unified across channels."
    },
    {
      "field": "sales_metric_unified_across_channels",
      "reason": "While sales metrics exist for individual channels (Increff, LimeRoad, JioMart), there are no explicit deduplication rules or source precedence to safely UNION or combine these into a single, unified sales metric for a dashboard across all channels."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides constraints and query patterns for Increff operations (sales, returns, dispatch) for Mensa Brands, but does not provide a mechanism to unify this data with other domains (OMS dependency, courier dependency) or other marketplaces, nor does it define 'OMS dependency' or 'return ownership' as metrics.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.jiomart.marketplace_query_constraints",
      "reason": "Provides constraints and query patterns for JioMart marketplace (OMS, returns, settlement) for Mensa Brands. While it covers some aspects (OMS and returns for JioMart), it's specific to one marketplace and cannot be unified with other marketplace data, 'own website' data, or logistics data without explicit cross-domain joins or common channel identifiers.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.logistics_batch_to_bank",
      "reason": "Provides constraints and query patterns related to logistics and courier reconciliation. This data is from a separate domain and lacks explicit mechanisms to connect it to sales, general OMS data, or return ownership across all channels in a unified dashboard.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.limeroad.total_forward_gmv",
      "reason": "Indicates a sales metric for LimeRoad, a single marketplace. It cannot be combined with other marketplaces or other domains without explicit consolidation rules.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.amount_semantics_audit",
      "reason": "A logistics-specific query pattern for data quality, not directly relatable to sales or return ownership across channels in a unified view.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.awb_duplicate_detection",
      "reason": "A logistics-specific query pattern, not directly relevant to sales or return ownership across channels in a unified view.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.bank_credit_unmatched_courier_reference",
      "reason": "A logistics reconciliation pattern related to courier payments, not directly unifying with sales, general OMS, or return ownership.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.cod_expected_vs_remitted",
      "reason": "A logistics reconciliation pattern related to COD, not directly unifying with sales, general OMS, or return ownership.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. No single physical table or a set of explicitly joinable tables exists that integrates 'sales', 'OMS dependency', 'courier dependency', and 'return ownership' across all channels ('own website' and various marketplaces').\n-- 2. There is no generic 'channel_type' or 'marketplace_name' column that spans all relevant data sources to allow aggregation and comparison across channels.\n-- 3. Concepts like 'OMS dependency', 'courier dependency', and 'return ownership' are qualitative or are represented by granular, platform-specific metrics, not unified, dashboard-ready measures.\n-- 4. Safe cross-source consolidation (e.g., via UNION) is not supported due to the absence of explicit deduplication rules and source precedence for disparate data sources.\n\n-- To enable such a dashboard, a comprehensive data integration layer would be required that harmonizes data from various operational systems (e.g., WMS like Increff, various Marketplace OMS/Settlement systems, and Logistics systems), defines explicit channel identifiers, and creates derived metrics for 'dependency' and 'ownership' that are consistent across channels."
}

### GRAPH_COMPLETION

{
  "filters": [
    {
      "column": "group_level_id",
      "operator": "=",
      "reason": "Tenant filter for Mensa Brands",
      "value": 22
    }
  ],
  "joins": "No joins can be established to create a unified dashboard across such diverse operational areas (sales, OMS, logistics, returns) and different channels (own website, various marketplaces) due to a lack of explicit, universally applicable join keys or a consolidated data model. Cross-source unions are not supported without explicit deduplication and precedence rules.",
  "metric_logic": {
    "aggregation_grain": "channel",
    "deduplication_rule": null,
    "denominator": null,
    "formula": "Cannot generate a unified dashboard as the underlying metrics (sales, OMS dependency, courier dependency, return ownership) and channel identification are disparate and lack a common, joinable data model across all required domains and platforms for Mensa Brands.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the complete absence of a unified data model or explicit physical columns that can combine sales, OMS dependency, courier dependency, and return ownership across 'own website' and multiple marketplace channels for Mensa Brands. Each of these components either resides in separate, unjoined systems, lacks a common channel identifier for aggregation, or is a qualitative concept not quantifiable by available data. Safe cross-source consolidation is not supported by the context.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "unified_channel_identifier",
      "reason": "There is no explicit physical column that categorizes data universally across 'own website' and various marketplace channels to allow a consolidated view for a unified dashboard."
    },
    {
      "field": "sales_metric_unified_across_channels",
      "reason": "While sales data exists for specific marketplaces (like Amazon), there are no explicit deduplication rules or a common schema to unify sales metrics across different channels (own website, various marketplaces) into a single dashboard-ready metric."
    },
    {
      "field": "oms_dependency_metric",
      "reason": "The concept of 'OMS dependency' is qualitative and is not defined as a quantifiable metric with physical columns across all relevant channels for Mensa Brands."
    },
    {
      "field": "courier_dependency_metric",
      "reason": "The concept of 'courier dependency' is qualitative and is not defined as a quantifiable metric with physical columns that can be unified across channels."
    },
    {
      "field": "return_ownership_metric",
      "reason": "The concept of 'return ownership' is qualitative and not represented by a physical column or derived metric that can be easily compared or unified across all channels."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "account_data_binding.mensa.amazon_in.primary.amazon_oms",
      "reason": "This binding points to Amazon OMS data for Mensa Brands, which is one component of the request (OMS data for a marketplace). However, it cannot be unified with other data domains (sales, courier, returns) or other channels due to lack of explicit joins or common identifiers for a dashboard.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.amazon_in.primary.amazon_returns",
      "reason": "This binding points to Amazon Returns data for Mensa Brands, which is one component of the request (returns data for a marketplace). It cannot be unified with other data domains or channels for a comprehensive dashboard.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
      "reason": "This binding points to Amazon Settlement data for Mensa Brands, relevant to sales and potentially other aspects. However, it lacks a mechanism to be unified with other domains or channels for a holistic dashboard.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
      "reason": "This binding points to Cashfree expense reports for Mensa Brands. While it might relate to payment processes, it is not directly relevant to sales, OMS, courier, or returns in a way that can be unified for the requested dashboard.",
      "role": "Risky Candidate",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership for Mensa Brands cannot be fulfilled with the current context.\n-- Blocking gaps:\n-- 1. No single physical table or a set of explicitly joinable tables exists that integrates 'sales', 'OMS dependency', 'courier dependency', and 'return ownership' across all channels ('own website' and various marketplaces').\n-- 2. There is no generic 'channel_type' or 'marketplace_name' column that spans all relevant data sources to allow aggregation and comparison across channels.\n-- 3. Concepts like 'OMS dependency', 'courier dependency', and 'return ownership' are qualitative or are represented by granular, platform-specific metrics, not unified, dashboard-ready measures.\n-- 4. Safe cross-source consolidation (e.g., via UNION) is not supported due to the absence of explicit deduplication rules and source precedence for disparate data sources.\n\n-- To enable such a dashboard, a comprehensive data integration layer would be required that harmonizes data from various operational systems (e.g., WMS like Increff, various Marketplace OMS/Settlement systems, and Logistics systems), defines explicit channel identifiers, and creates derived metrics for 'dependency' and 'ownership' that are consistent across channels."
}
