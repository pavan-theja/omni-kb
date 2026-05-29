## 011. Create a marketplace risk report showing which channels depend on the same OMS.

### Timing

- started_at: `2026-05-27T07:48:05+00:00`
- duration_seconds: `47.629`
- RAG_COMPLETION_seconds: `21.201`
- GRAPH_COMPLETION_seconds: `26.428`

### Query

```text
Create a marketplace risk report showing which channels depend on the same OMS.

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
    "group_level_id = 22"
  ],
  "joins": "No joins can be established as the necessary linking dimensions (OMS system name, connected marketplace name) are absent as explicit physical columns.",
  "metric_logic": {
    "aggregation_grain": "oms_system_name, connected_marketplace_name",
    "deduplication_rule": "DISTINCT oms_system_name, connected_marketplace_name",
    "denominator": null,
    "formula": "List distinct pairs of marketplace channels and their dependent OMS systems.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the absence of explicit physical columns or relationships that directly store 'OMS system names' and 'connected marketplace names' as queryable data points. The information is currently implicit in table names or metadata, which cannot be directly used to generate SQL output.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "oms_system_name",
      "reason": "No explicit physical column exists to represent the OMS system name directly. Inferring from table names (e.g., 'amazon_oms' -> 'Amazon OMS') would violate the 'no literal metadata SQL' rule."
    },
    {
      "field": "connected_marketplace_name",
      "reason": "No explicit physical column or logical rule exists in the provided context to identify the 'connected marketplace' for each OMS. While some table names imply a marketplace, this cannot be extracted as a data value."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.amazon_oms",
      "reason": "This table is an OMS for Amazon related to Mensa Brands. However, there's no explicit physical column within this table to identify 'Amazon OMS' as the OMS system name or 'Amazon' as the connected marketplace without generating literal strings from the table name, which is disallowed.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.myntra_oms",
      "reason": "This table is an OMS for Myntra related to Mensa Brands. Similar to amazon_oms, it lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.limeroad_oms",
      "reason": "This table is an OMS for LimeRoad related to Mensa Brands. It lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.shiprocket_oms",
      "reason": "This table is a logistics OMS used by Mensa Brands. It lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.amazon_in.primary.amazon_oms",
      "reason": "Confirms that `zs_observe.amazon_oms` is relevant for Mensa Brands (group_level_id = 22) as an OMS, but does not provide extractable OMS or marketplace names as data.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.gross_sales_oms",
      "reason": "Indicates usage of `zs_observe.myntra_oms` for Mensa Brands, confirming it as an OMS, but doesn't provide a mechanism to extract generic OMS or marketplace names.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.amount_semantics_audit",
      "reason": "Indicates usage of `zs_observe.shiprocket_oms` for Mensa Brands' logistics operations, confirming it as an OMS, but doesn't provide a mechanism to extract generic OMS or marketplace names.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to create a marketplace risk report showing which channels depend on the same OMS cannot be fulfilled with the current context.\n-- The core problem is the lack of explicit physical columns that contain the 'OMS system name' and the 'connected marketplace name' as data values. While tables like `zs_observe.amazon_oms` or `zs_observe.myntra_oms` are identified as OMS systems for Mensa Brands, extracting 'Amazon OMS' or 'Myntra' as values from a database column is not supported by the provided metadata.\n\n-- To resolve this, a physical table or a clear logical rule with concrete columns that explicitly map marketplace channels to their respective OMS systems would be required. This would enable querying for shared OMS dependencies."
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = 22 (for Mensa Brands)"
  ],
  "joins": "No joins can be established as the necessary linking dimensions (OMS system name, connected marketplace name) are absent as explicit physical columns to allow comparison or grouping across channels/OMS.",
  "metric_logic": {
    "aggregation_grain": "oms_system_name, connected_marketplace_name",
    "deduplication_rule": "DISTINCT oms_system_name, connected_marketplace_name",
    "denominator": null,
    "formula": "List distinct pairs of marketplace channels and their dependent OMS systems.",
    "numerator": null
  },
  "missing_or_ambiguous": "The primary blocking gap is the absence of explicit physical columns or relationships that directly store 'OMS system names' and 'connected marketplace names' as queryable data points. The information is currently implicit in table names or metadata, which cannot be directly used to generate SQL output. Additionally, there is no quantifiable metric or definition for 'risk' or 'operational dependency' within the context.",
  "rejected_or_ambiguous_fields": [
    {
      "field": "oms_system_name",
      "reason": "No explicit physical column exists to represent the OMS system name directly. Inferring from table names (e.g., 'amazon_oms' -> 'Amazon OMS') would violate the 'no literal metadata SQL' rule."
    },
    {
      "field": "connected_marketplace_name",
      "reason": "No explicit physical column or logical rule exists in the provided context to identify the 'connected marketplace' for each OMS. While some table names imply a marketplace, this cannot be extracted as a data value."
    }
  ],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "table.zs_observe.amazon_oms",
      "reason": "This table is an OMS for Amazon related to Mensa Brands. However, there is no explicit physical column within this table to identify 'Amazon OMS' as the OMS system name or 'Amazon' as the connected marketplace without generating literal strings from the table name, which is disallowed.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.myntra_oms",
      "reason": "This table is an OMS for Myntra related to Mensa Brands. Similar to amazon_oms, it lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.limeroad_oms",
      "reason": "This table is an OMS for LimeRoad related to Mensa Brands. It lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "table.zs_observe.shiprocket_oms",
      "reason": "This table is a logistics OMS used by Mensa Brands. It lacks explicit physical columns for a generic OMS system name or connected marketplace name.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.amazon_in.primary.amazon_oms",
      "reason": "Confirms that `zs_observe.amazon_oms` is relevant for Mensa Brands (group_level_id = 22) as an OMS, but does not provide extractable OMS or marketplace names as data.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.myntra.gross_sales_oms",
      "reason": "Indicates usage of `zs_observe.myntra_oms` for Mensa Brands, confirming it as an OMS, but doesn't provide a mechanism to extract generic OMS or marketplace names.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "query_pattern.logistics.amount_semantics_audit",
      "reason": "Indicates usage of `zs_observe.shiprocket_oms` for Mensa Brands' logistics operations, confirming it as an OMS, but doesn't provide a mechanism to extract generic OMS or marketplace names.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "business_scope_set.mensa_brands.operations_wms",
      "reason": "Indicates Mensa Brands uses Increff and Unicommerce as 'cross-channel OMS/WMS'. While suggesting multiple channels might use these, no physical table schema or join logic is provided to connect specific marketplace channels to these OMS systems or to quantify 'risk'.",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [],
  "selected_source": null,
  "sql_skeleton": "-- The request to create a marketplace risk report showing which channels depend on the same OMS cannot be fulfilled with the current context.\n-- The core problem is the lack of explicit physical columns that contain the 'OMS system name' and the 'connected marketplace name' as data values. While tables like `zs_observe.amazon_oms` or `zs_observe.myntra_oms` are identified as OMS systems for Mensa Brands, extracting 'Amazon OMS' or 'Myntra' as values from a database column is not supported by the provided metadata, nor are there any columns to indicate shared OMS dependencies.\n\n-- To resolve this, a physical table or a clear logical rule with concrete columns that explicitly map marketplace channels to their respective OMS systems would be required. This would enable querying for shared OMS dependencies and the quantification of 'risk'."
}
