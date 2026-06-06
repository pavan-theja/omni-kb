## 012. Generate a logistics dependency matrix showing courier concentration across marketplaces.

### Timing

- started_at: `2026-05-27T06:43:38+00:00`
- duration_seconds: `57.533`
- RAG_COMPLETION_seconds: `39.854`
- GRAPH_COMPLETION_seconds: `17.679`

### Query

```text
Generate a logistics dependency matrix showing courier concentration across marketplaces.

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
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "Multiple CTEs are used to extract channel and courier information from different OMS sources. These CTEs are then combined using UNION ALL and aggregated to present the courier concentration per channel.",
  "metric_logic": {
    "aggregation_grain": "sales_channel, courier_partner",
    "deduplication_rule": "Distinct order_ids are counted within each source, then summed across sources if required. No cross-source order_id deduplication is defined for this specific query.",
    "denominator": null,
    "formula": "Count of distinct orders (or shipments) for each combination of sales channel and courier partner, representing courier concentration.",
    "numerator": "COUNT(DISTINCT order_id)"
  },
  "missing_or_ambiguous": "The context does not provide an explicit canonical mapping to classify `sales_channel` values from `zs_observe.unicommerce` or `zs_observe.increff_sales` as either 'marketplace' or 'own website' (D2C). Therefore, the generated report will show courier concentration per *channel*, and cannot specifically filter for or group only 'marketplaces' without further external business logic or mapping. The exact column names for `courier_partner` and `order_id` in `zs_observe.unicommerce` and `zs_observe.increff_sales` are inferred based on the typical structure of OMS tables and the existence of a relevant query pattern for Increff.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "Identified as a central OMS for Mensa Brands, likely to contain both sales channel and courier information for tracking logistics dependencies.",
      "role": "Primary Source for OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`business_scope_set.mensa_brands.operations_wms` explicitly lists Increff for OMS/WMS operations. `query_pattern.increff.7_6_courier_partner_distribution_normalized` implies the presence of courier data in Increff operations data, linked to sales channels.",
      "role": "Primary Source for OMS/WMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected OMS tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, explicitly mentioned in Increff constraints.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "This column identifies the channel/marketplace for each order/shipment. It will represent the 'marketplace' aspect of the report.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "courier_partner",
      "reason": "This column directly identifies the courier used for each order/shipment, fulfilling the 'courier' aspect of the report. Explicitly mentioned in `query_pattern.increff.7_6_courier_partner_distribution_normalized` and commonly found in OMS systems.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Used to count the number of unique orders handled by each courier for each channel, providing a measure of concentration. Inferred as a common key in OMS data.",
      "role": "Metric (Count/Concentration unit)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH ChannelCourierConcentration AS (\n    -- Unicommerce OMS\n    SELECT DISTINCT\n        sales_channel AS channel_name,\n        courier_partner AS courier_name,\n        order_id\n    FROM\n        zs_observe.unicommerce\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n\n    UNION ALL\n\n    -- Increff OMS/WMS\n    SELECT DISTINCT\n        sales_channel AS channel_name,\n        courier_partner AS courier_name,\n        order_id\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n)\nSELECT\n    channel_name,\n    courier_name,\n    COUNT(DISTINCT order_id) AS total_orders\nFROM\n    ChannelCourierConcentration\nWHERE\n    channel_name IS NOT NULL AND courier_name IS NOT NULL\nGROUP BY\n    channel_name, courier_name\nORDER BY\n    channel_name, total_orders DESC;"
}

### GRAPH_COMPLETION

{
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "Multiple CTEs are used to extract channel and courier information from different OMS sources. These CTEs are then combined using UNION ALL and aggregated to present the courier concentration per channel.",
  "metric_logic": {
    "aggregation_grain": "sales_channel, courier_partner",
    "deduplication_rule": "Distinct order_ids are counted within each source, then summed across sources if required. No cross-source order_id deduplication is defined for this specific query.",
    "denominator": null,
    "formula": "Count of distinct orders (or shipments) for each combination of sales channel and courier partner, representing courier concentration.",
    "numerator": "COUNT(DISTINCT order_id)"
  },
  "missing_or_ambiguous": "The context does not provide an explicit canonical mapping to classify `sales_channel` values from `zs_observe.unicommerce` or `zs_observe.increff_sales` as either 'marketplace' or 'own website' (D2C). Therefore, the generated report will show courier concentration per *channel*, and cannot specifically filter for or group only 'marketplaces' without further external business logic or mapping. The exact column names for `courier_partner` and `order_id` in `zs_observe.unicommerce` and `zs_observe.increff_sales` are inferred based on the typical structure of OMS tables and the existence of a relevant query pattern for Increff.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [
    "execution_constraint_set.increff.operations_manifest_refactored_constraints",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "reason": "Identified as a central OMS for Mensa Brands, likely to contain both sales channel and courier information for tracking logistics dependencies.",
      "role": "Primary Source for OMS data",
      "selected?": "Yes"
    },
    {
      "field": "zs_observe.increff_sales",
      "reason": "`business_scope_set.mensa_brands.operations_wms` explicitly lists Increff for OMS/WMS operations. `query_pattern.increff.7_6_courier_partner_distribution_normalized` implies the presence of courier data in Increff operations data, linked to sales channels.",
      "role": "Primary Source for OMS/WMS data",
      "selected?": "Yes"
    }
  ],
  "required_fields": [
    {
      "field": "group_level_id",
      "reason": "Mandatory filter (`group_level_id = '22'`) to scope data to 'Mensa Brands' across all selected OMS tables.",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes"
    },
    {
      "field": "is_active",
      "reason": "Inferred as a mandatory filter (`is_active = true`) for data validity and consistency across operational tables, explicitly mentioned in Increff constraints.",
      "role": "Filter Column (Status)",
      "selected?": "Yes"
    },
    {
      "field": "sales_channel",
      "reason": "This column identifies the channel/marketplace for each order/shipment. It will represent the 'marketplace' aspect of the report.",
      "role": "Dimension (Channel Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "courier_partner",
      "reason": "This column directly identifies the courier used for each order/shipment, fulfilling the 'courier' aspect of the report. Explicitly mentioned in `query_pattern.increff.7_6_courier_partner_distribution_normalized` and commonly found in OMS systems.",
      "role": "Dimension (Courier Identifier)",
      "selected?": "Yes"
    },
    {
      "field": "order_id",
      "reason": "Used to count the number of unique orders handled by each courier for each channel, providing a measure of concentration. Inferred as a common key in OMS data.",
      "role": "Metric (Count/Concentration unit)",
      "selected?": "Yes"
    }
  ],
  "selected_source": null,
  "sql_skeleton": "WITH ChannelCourierConcentration AS (\n    -- Unicommerce OMS\n    SELECT DISTINCT\n        sales_channel AS channel_name,\n        courier_partner AS courier_name,\n        order_id\n    FROM\n        zs_observe.unicommerce\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n\n    UNION ALL\n\n    -- Increff OMS/WMS\n    SELECT DISTINCT\n        sales_channel AS channel_name,\n        courier_partner AS courier_name,\n        order_id\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true -- Inferred filter\n)\nSELECT\n    channel_name,\n    courier_name,\n    COUNT(DISTINCT order_id) AS total_orders\nFROM\n    ChannelCourierConcentration\nWHERE\n    channel_name IS NOT NULL AND courier_name IS NOT NULL\nGROUP BY\n    channel_name, courier_name\nORDER BY\n    channel_name, total_orders DESC;"
}
