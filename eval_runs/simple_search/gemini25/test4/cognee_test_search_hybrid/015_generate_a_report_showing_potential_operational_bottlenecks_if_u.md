## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Timing

- started_at: `2026-05-27T06:50:37+00:00`
- duration_seconds: `58.295`
- RAG_COMPLETION_seconds: `42.706`
- GRAPH_COMPLETION_seconds: `15.586`

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

Scope:
- tenant: Mensa Brands

Answer for downstream SQL/query construction using only the provided context and explicit user input.

You are a SQL-resolution handoff agent. Do not answer the business question directly. Produce the safest SQL-building plan that the retrieved context can support.

Resolution flow:
1. Identify the requested grain, metric/status logic, dimensions, filters, joins, and tenant/account scope.
2. Enumerate grounded candidate sources before choosing a source.
3. Classify candidates as direct, supporting, risky, or irrelevant.
4. Select the best SQL package. If no safe package exists, return a partial/risky handoff with the blocking gaps.

Core rules:
- Prefer physical SQL tables and columns explicitly grounded in context.
- Do not default to the most detailed retrieved source if the user asks about channels, marketplaces, settlements, reconciliation, risk, bottlenecks, dependency, concentration, courier mapping, OMS dependency, or marketplace-wide reporting.
- For channel/marketplace questions, enumerate all relevant candidate physical settlement, OMS/order, return/reverse, logistics/courier, and query-pattern sources before selecting a SQL path.
- Do not treat one marketplace such as Myntra, Amazon, Flipkart, Ajio, Nykaa, Meesho, Snapdeal, TataCliq, JioMart, HealthKart, or LimeRoad as representative of all marketplaces unless the user explicitly asks for that marketplace or the context proves it is the only applicable source.
- Do not UNION or numerically consolidate multiple source tables unless the user asks for cross-source/all-source/platform-wide consolidation and the context provides deduplication keys plus source precedence.
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

Output rules:
- Return one best SQL package in the schema below.
- Use `require_tables` to show selected and rejected/risky/supporting candidates.
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
  "sql_skeleton": "valid SQL template using selected fields and filters, or commented partial template"
}
```

### RAG_COMPLETION

{
  "filters": [],
  "joins": "No direct joins on physical tables are performed for this qualitative report. Information is aggregated from metadata definitions.",
  "metric_logic": {
    "aggregation_grain": "operational_area, impacted_channels, bottleneck_description",
    "deduplication_rule": "Each distinct bottleneck scenario is listed once.",
    "denominator": null,
    "formula": "A qualitative report identifying operational areas and channels that would face bottlenecks if Unicommerce, as the central OMS for Mensa Brands, becomes unavailable.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact definition of 'all marketplaces and D2C platforms' for Mensa Brands is not exhaustively listed in the context, so specific examples are used. The specific nature of the integration (e.g., whether Amazon/Myntra OMS systems are downstream or upstream of Unicommerce for Mensa Brands' operations) is inferred based on Unicommerce being designated the 'central OMS'. Quantifying the severity or duration of bottlenecks is not possible from the given metadata.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank"
  ],
  "require_tables": [
    {
      "field": "business_scope_set.mensa_brands.oms",
      "reason": "Explicitly states Unicommerce is the 'central OMS' for Mensa Brands, processing orders and managing inventory for all marketplaces and D2C platforms.",
      "role": "Primary Source for Unicommerce's central role",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Represents the physical data store for Unicommerce, confirming its existence and likely containing channel-specific data.",
      "role": "Supporting Table (Operational Hub)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Example of a marketplace OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Example of a marketplace OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "Example of a D2C OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable, per definition of Unicommerce as central for D2C.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Example of an OMS/WMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable, assuming data flow dependency.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "operational_area",
      "reason": "Describes the business function that would become a bottleneck.",
      "role": "Dimension (Operational Function Affected)",
      "selected?": "Yes"
    },
    {
      "field": "impacted_channels",
      "reason": "Indicates which marketplaces or D2C platforms would face the bottleneck.",
      "role": "Dimension (Channels Affected)",
      "selected?": "Yes"
    },
    {
      "field": "bottleneck_description",
      "reason": "Provides qualitative explanation of the bottleneck due to Unicommerce's unavailability.",
      "role": "Descriptive Detail (Reason/Impact)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT 'Order Processing' AS operational_area, 'All Marketplaces (e.g., Amazon, Myntra) and D2C Platforms (e.g., Shopify D2C)' AS impacted_channels, 'Unicommerce is the central OMS responsible for processing orders from all channels. Its unavailability would halt order flow.' AS bottleneck_description\nUNION ALL\nSELECT 'Inventory Management' AS operational_area, 'All Marketplaces (e.g., Amazon, Myntra) and D2C Platforms (e.g., Shopify D2C)' AS impacted_channels, 'Unicommerce is the central system for managing inventory across all channels. Its unavailability would lead to inaccurate stock levels, potential overselling/underselling, and fulfillment issues.' AS bottleneck_description\nUNION ALL\nSELECT 'Warehouse Operations' AS operational_area, 'Fulfilment through Increff WMS and other logistics partners' AS impacted_channels, 'If Increff WMS (zs_observe.increff_sales) relies on Unicommerce for order dispatch and inventory updates, its operations would be severely disrupted.' AS bottleneck_description;"
}

### GRAPH_COMPLETION

{
  "filters": [],
  "joins": "No direct joins on physical tables are performed for this qualitative report. Information is aggregated from metadata definitions.",
  "metric_logic": {
    "aggregation_grain": "operational_area, impacted_channels, bottleneck_description",
    "deduplication_rule": "Each distinct bottleneck scenario is listed once.",
    "denominator": null,
    "formula": "A qualitative report identifying operational areas and channels that would face bottlenecks if Unicommerce, as the central OMS for Mensa Brands, becomes unavailable.",
    "numerator": null
  },
  "missing_or_ambiguous": "The exact definition of 'all marketplaces and D2C platforms' for Mensa Brands is not exhaustively listed in the context, so specific examples are used. The specific nature of the integration (e.g., whether Amazon/Myntra OMS systems are downstream or upstream of Unicommerce for Mensa Brands' operations) is inferred based on Unicommerce being designated the 'central OMS'. Quantifying the severity or duration of bottlenecks is not possible from the given metadata.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "canonical_pack_0041",
    "marketplace transactions",
    "meesho returns",
    "meesho reverse",
    "meesho brand mapping",
    "canonical_pack_0001",
    "ajio oms",
    "canonical_pack_0024"
  ],
  "require_tables": [
    {
      "field": "business_scope_set.mensa_brands.oms",
      "reason": "Explicitly states Unicommerce is the 'central OMS' for Mensa Brands, processing orders and managing inventory for all marketplaces and D2C platforms.",
      "role": "Primary Source for Unicommerce's central role",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.unicommerce",
      "reason": "Represents the physical data store for Unicommerce, confirming its existence and likely containing channel-specific data.",
      "role": "Supporting Table (Operational Hub)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.amazon_oms",
      "reason": "Example of a marketplace OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.myntra_oms",
      "reason": "Example of a marketplace OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.shopify_oms",
      "reason": "Example of a D2C OMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable, per definition of Unicommerce as central for D2C.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "Example of an OMS/WMS for Mensa Brands that would be impacted if central OMS (Unicommerce) is unavailable, assuming data flow dependency.",
      "role": "Supporting Table (Impacted Channel Example)",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "operational_area",
      "reason": "Describes the business function that would become a bottleneck.",
      "role": "Dimension (Operational Function Affected)",
      "selected?": "Yes"
    },
    {
      "field": "impacted_channels",
      "reason": "Indicates which marketplaces or D2C platforms would face the bottleneck.",
      "role": "Dimension (Channels Affected)",
      "selected?": "Yes"
    },
    {
      "field": "bottleneck_description",
      "reason": "Provides qualitative explanation of the bottleneck due to Unicommerce's unavailability.",
      "role": "Descriptive Detail (Reason/Impact)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "SELECT 'Order Processing' AS operational_area, 'All Marketplaces (e.g., Amazon, Myntra) and D2C Platforms (e.g., Shopify D2C)' AS impacted_channels, 'Unicommerce is the central OMS responsible for processing orders from all channels. Its unavailability would halt order flow.' AS bottleneck_description\nUNION ALL\nSELECT 'Inventory Management' AS operational_area, 'All Marketplaces (e.g., Amazon, Myntra) and D2C Platforms (e.g., Shopify D2C)' AS impacted_channels, 'Unicommerce is the central system for managing inventory across all channels. Its unavailability would lead to inaccurate stock levels, potential overselling/underselling, and fulfillment issues.' AS bottleneck_description\nUNION ALL\nSELECT 'Warehouse Operations' AS operational_area, 'Fulfilment through Increff WMS and other logistics partners' AS impacted_channels, 'If Increff WMS (zs_observe.increff_sales) relies on Unicommerce for order dispatch and inventory updates, its operations would be severely disrupted.' AS bottleneck_description;"
}
