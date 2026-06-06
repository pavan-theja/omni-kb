# Cognee Batch Search Results

- generated_at: `2026-05-26T20:04:17+00:00`
- source_questions: `inline QUESTIONS`
- datasets: `zenstatement_canonical`
- search_types: `GRAPH_COMPLETION`

## 001. Which channel has the highest order volume share?

### Query

```text
Which channel has the highest order volume share?

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "account_data_binding.volans_epic_llc.target_us.primary.target_sales"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table contains `group_level_id` for tenant filtering and `external_shipment_id` for counting order volume. A 'channel' column is logically inferred to exist within this sales table to represent the sales channel."
    }
  ],
  "required_fields": [
    {
      "field": "channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested for grouping in the question ('Which channel'). Although not explicitly listed in the provided schema for `zs_observe.increff_sales`, a 'channel' column is a standard dimension in sales data tables for classification and is logically inferred here."
    },
    {
      "field": "external_shipment_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Used to calculate 'order volume' by counting distinct shipment IDs. This field is explicitly listed for `zs_observe.increff_sales` as an 'identity_or_reference'."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id` column in `table.zs_observe.increff_sales` has a documented description of '22', which is the identifier for Mensa."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "MAX ( (COUNT(DISTINCT external_shipment_id) per channel / Total COUNT(DISTINCT external_shipment_id) for Mensa) * 100 )",
    "numerator": "COUNT(DISTINCT external_shipment_id) GROUPED BY channel",
    "denominator": "TOTAL COUNT(DISTINCT external_shipment_id) for Mensa",
    "aggregation_grain": "channel",
    "deduplication_rule": "COUNT(DISTINCT external_shipment_id) to count unique orders/shipments for volume."
  },
  "filters": [
    "group_level_id = '22'"
  ],
  "joins": "No joins are required as all necessary fields are inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",
  "missing_or_ambiguous": "The explicit column name 'channel' within `zs_observe.increff_sales` is not provided in the context and was inferred as a logical column name. The `fulfilment_channel` column is explicitly for couriers, not sales channels, requiring the inference of a separate 'channel' column for sales classification.",
  "sql_skeleton": "WITH ChannelOrders AS ( SELECT channel, COUNT(DISTINCT external_shipment_id) AS order_count FROM zs_observe.increff_sales WHERE group_level_id = '22' GROUP BY channel ), TotalOrders AS ( SELECT COUNT(DISTINCT external_shipment_id) AS total_order_count FROM zs_observe.increff_sales WHERE group_level_id = '22' ) SELECT co.channel, (CAST(co.order_count AS DECIMAL) / to.total_order_count) * 100 AS order_share FROM ChannelOrders co, TotalOrders to ORDER BY order_share DESC LIMIT 1"
}


---

## 002. Generate a report of all channels using Manual CSV integration.

### Query

```text
Generate a report of all channels using Manual CSV integration.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "metadata.account_data_bindings",
  "rejected_sources": [
    "query_pattern.limeroad.total_forward_gmv",
    "query_pattern.logistics.amount_semantics_audit",
    "query_pattern.logistics.awb_duplicate_detection",
    "query_pattern.logistics.bank_credit_unmatched_courier_reference",
    "query_pattern.logistics.cod_expected_vs_remitted",
    "execution_constraint_set.jiomart.marketplace_query_constraints",
    "execution_constraint_set.logistics_batch_to_bank",
    "table.zs_observe.nykaa_mapper_gst",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce",
    "table.zs_observe.unicommerce_order_sales_report",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report"
  ],
  "require_tables": [
    {
      "field": "account_data_bindings",
      "role": "Source for Channel Definitions and Integration Types",
      "selected?": "Yes",
      "reason": "Inferred as the logical metadata table containing all `account_data_binding` card details. These cards define specific integrations/channels for Mensa Brands and would logically contain properties like integration type."
    }
  ],
  "required_fields": [
    {
      "field": "channel_name",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('all channels'). This is inferred as the column representing the 'name' field of each `account_data_binding` card (e.g., 'Amazon Oms'), which acts as the channel identifier."
    },
    {
      "field": "integration_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly requested for filtering ('using Manual CSV integration'). This column is inferred to exist within the `account_data_bindings` logical table to categorize the integration method for each channel. Its presence and specific value ('Manual CSV') are inferred due to the direct request but lack of explicit mention in the context."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa Brands'. The `group_level_id = 22` is explicitly defined in Mensa's `account_data_binding` cards' `scope_keys`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT [channel_name]",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name",
    "deduplication_rule": "DISTINCT on (channel_name)"
  },
  "filters": [
    "group_level_id = '22'",
    "integration_type = 'Manual CSV'"
  ],
  "joins": "No joins are required as all necessary information (channel name, integration type, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.",
  "missing_or_ambiguous": "The explicit physical table name for `account_data_bindings` and the column names `channel_name` and `integration_type` are inferred based on the request and domain knowledge. The presence of an `integration_type` field and its specific value 'Manual CSV' are also inferred, as they are critical to fulfilling the query's filter condition but are not explicitly mentioned in the context.",
  "sql_skeleton": "SELECT DISTINCT channel_name FROM account_data_bindings WHERE group_level_id = '22' AND integration_type = 'Manual CSV'"
}


---

## 003. List all marketplaces handled through Unicommerce.

### Query

```text
List all marketplaces handled through Unicommerce.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.unicommerce",
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.mensa.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.mensa.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce",
    "account_data_binding.astrotalk.unicommerce_oms.primary.unicommerce_order_sales_report",
    "business_flow_binding.bracheium_brand_technologies.marketplace_to_operations",
    "business_flow_binding.bracheium_brand_technologies.marketplace_transactions_future_context",
    "business_flow_binding.bracheium_brand_technologies.shopify_shiprocket_order_flow",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review"
  ],
  "require_tables": [
    {
      "field": "zs_observe.unicommerce",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table directly represents Unicommerce data, which is explicitly mentioned in the question. Mensa Brands uses Unicommerce for cross-channel OMS/WMS operational evidence, as per `business_scope_set.mensa_brands.operations_wms`."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('List all marketplaces'). This column is identified in `table.zs_observe.unicommerce` as the field for sales channels/marketplaces in previous turns, and is a logical column for OMS data."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. Mensa's `group_level_id` is consistently `22` across its `account_data_binding` cards and is a standard tenant filter for operational tables like `zs_observe.unicommerce`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "DISTINCT on (sales_channel) to list unique marketplaces."
  },
  "filters": [
    "group_level_id = '22'"
  ],
  "joins": "No joins are required as all necessary information (marketplace names and tenant ID) is available within the single selected table `zs_observe.unicommerce`.",
  "missing_or_ambiguous": "None",
  "sql_skeleton": "SELECT DISTINCT sales_channel FROM zs_observe.unicommerce WHERE group_level_id = '22'"
}


---

## 004. Generate a courier-wise channel mapping report.

### Query

```text
Generate a courier-wise channel mapping report.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "platform_domain.increff.operations",
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
    "account_data_binding.ardeur_fashion.flipkart_in.primary.cashback",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "account_data_binding.volans_epic_llc.target_us.primary.target_sales",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note"
  ],
  "require_tables": [
    {
      "field": "increff_operations_data",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "Inferred as the main logical table within the 'platform_domain.increff.operations' domain that would contain both courier and channel information for Mensa. Mensa's account data bindings list 'increff_operations.md' as a source document, implying Mensa utilizes Increff operations."
    }
  ],
  "required_fields": [
    {
      "field": "courier_partner",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('courier-wise'). Its presence is logically inferred within the 'increff_operations_data' table, as this domain typically handles logistics and order fulfillment details."
    },
    {
      "field": "channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('channel mapping'). Its presence is logically inferred within the 'increff_operations_data' table, as this domain typically handles order and sales data linked to various channels."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier in Mensa's `account_data_binding` cards' `scope_keys` and is a standard tenant filter for operational data."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT courier_partner, channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(courier_partner, channel)",
    "deduplication_rule": "DISTINCT on (courier_partner, channel) to list unique pairings."
  },
  "filters": [
    "group_level_id = '22'"
  ],
  "joins": "No joins are specified as all necessary information (courier, channel, and tenant ID) is inferred to exist within the single selected table `increff_operations_data` as per hard rules.",
  "missing_or_ambiguous": "The explicit physical table name for 'increff_operations_data' and the precise column names for 'courier_partner', 'channel', and 'group_level_id' are not provided in the context. These were logically inferred based on domain conventions and the implication that Increff operations handles such data for Mensa.",
  "sql_skeleton": "SELECT DISTINCT courier_partner, channel FROM increff_operations_data WHERE group_level_id = '22'"
}


---

## 005. Which courier handles the own website shipments?

### Query

```text
Which courier handles the own website shipments?

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{  "selected_source": "table.zs_observe.increff_sales",  "rejected_sources": [    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse",    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement",    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment",    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",    "account_data_binding.ardeur_fashion.flipkart_in.primary.cashback",    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",    "account_data_binding.mensa.amazon_in.primary.amazon_oms",    "account_data_binding.mensa.amazon_in.primary.amazon_returns",    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",    "account_data_binding.volans_epic_llc.target_us.primary.target_sales",    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",    "scopespecificationnote",    "scope specification note"  ],  "require_tables": [    {      "field": "zs_observe.increff_sales",      "role": "Primary Data Source Table",      "selected?": "Yes",      "reason": "This table is explicitly mentioned in the context and contains `fulfilment_channel` for courier information and `group_level_id` for tenant identification. It is the most appropriate source for logistics and sales data for Mensa Brands through Increff."    }  ],  "required_fields": [    {      "field": "fulfilment_channel",      "role": "Dimension",      "selected?": "Yes",      "reason": "Explicitly requested in the question ('Which courier handles'). The column description 'Courier/logistics partner used (80+ variants)' directly matches the requirement. This field exists in `table.zs_observe.increff_sales`."    },    {      "field": "channel",      "role": "Filter Column",      "selected?": "Yes",      "reason": "Required to filter for 'own website shipments'. While not explicitly named in the provided context for `zs_observe.increff_sales`, a 'channel' column is a logical necessity for sales data. `value_profile.increff_sales.sales_channel.reference` implies a column for sales channel exists. 'Website' is inferred as a common value for 'own website' channels."    },    {      "field": "group_level_id",      "role": "Filter Column",      "selected?": "Yes",      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id` column in `table.zs_observe.increff_sales` has a documented description of '22' which is the identifier for Mensa."    }  ],  "rejected_or_ambiguous_fields": [],  "metric_logic": {    "formula": "SELECT DISTINCT fulfilment_channel",    "numerator": null,    "denominator": null,    "aggregation_grain": "fulfilment_channel",    "deduplication_rule": "DISTINCT on (fulfilment_channel) to list unique couriers."  },  "filters": [    "group_level_id = '22'",    "channel = 'Website'"  ],  "joins": "No joins are required as all necessary information (courier, channel, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",  "missing_or_ambiguous": "The explicit column name `channel` within `table.zs_observe.increff_sales` and its specific value 'Website' for 'own website shipments' are not provided in the context and were inferred. The inference is based on the need to fulfill the query's filter condition and domain knowledge that a sales channel would be available in such a table.",  "sql_skeleton": "SELECT DISTINCT fulfilment_channel FROM zs_observe.increff_sales WHERE group_level_id = '22' AND channel = 'Website'"}


---

## 006. Generate a report showing COD remittance type by courier.

### Query

```text
Generate a report showing COD remittance type by courier.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "courier_shipment_count",
    "account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement",
    "account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table contains courier information (`fulfilment_channel`) and `group_level_id` for tenant filtering, making it the most suitable source for courier-related sales data for Mensa. Other tables are for a different tenant (Prita Designs) or are metrics/metadata."
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('by courier'). The column description 'Courier/logistics partner used (80+ variants)' in `table.zs_observe.increff_sales` directly matches this requirement."
    },
    {
      "field": "cod_remittance_type",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested in the report ('COD remittance type'). This column is logically inferred to exist within a sales or logistics table (like `increff_sales`) to classify how COD payments are remitted."
    },
    {
      "field": "payment_method",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required to filter for 'COD' shipments. This column is logically inferred to exist within the `increff_sales` table to identify the payment method of an order/shipment."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id` column in `table.zs_observe.increff_sales` has a documented description of '22', which is the identifier for Mensa."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT fulfilment_channel, cod_remittance_type",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(fulfilment_channel, cod_remittance_type)",
    "deduplication_rule": "DISTINCT on (fulfilment_channel, cod_remittance_type) to list unique pairings."
  },
  "filters": [
    "group_level_id = '22'",
    "payment_method = 'COD'"
  ],
  "joins": "No joins are required as all necessary information (courier, COD remittance type, payment method, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales` as per hard rules.",
  "missing_or_ambiguous": "The explicit column names `payment_method` and `cod_remittance_type` within `table.zs_observe.increff_sales` and the specific value 'COD' for `payment_method` are not provided in the context and were inferred. The inference is based on the need to fulfill the query's filter and grouping conditions, assuming such detail would be present in a sales/logistics operational table.",
  "sql_skeleton": "SELECT DISTINCT fulfilment_channel, cod_remittance_type FROM zs_observe.increff_sales WHERE group_level_id = '22' AND payment_method = 'COD'"
}


---

## 007. Which channels use marketplace-managed returns?

### Query

```text
Which channels use marketplace-managed returns?

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "metadata.account_data_bindings",
  "rejected_sources": [
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.logistics_settlement",
    "business_scope_set.mensa_brands.operations_wms",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources",
    "business_scope_set.mpl_india.bank_reconciliation",
    "business_scope_set.mpl_india.cashfree_expense",
    "table.zs_observe.amazon_disbursment",
    "table.zs_observe.amazon_fee_preview",
    "table.zs_observe.amazon_oms",
    "table.zs_observe.amazon_returns",
    "table.zs_observe.amazon_settlement",
    "table.zs_observe.cashfree_expense_report",
    "table.zs_observe.shopify_oms",
    "table.zs_observe.unicommerce",
    "table.zs_observe.unicommerce_order_sales_report"
  ],
  "require_tables": [
    {
      "field": "account_data_bindings",
      "role": "Source for Channel Definitions and Integration Types",
      "selected?": "Yes",
      "reason": "This logical table contains all `account_data_binding` card details, which define specific channels and their integration semantics (like returns). This is the appropriate source to identify which channels use 'marketplace-managed returns' for Mensa."
    }
  ],
  "required_fields": [
    {
      "field": "name",
      "role": "Binding Name for Channel Identification",
      "selected?": "Yes",
      "reason": "The 'name' field of the `account_data_binding` card (e.g., 'Amazon Returns') explicitly states the channel and implicitly indicates a returns-related integration. The marketplace name can be extracted from this field."
    },
    {
      "field": "platform_account_id",
      "role": "Filter Column (Marketplace Identification)",
      "selected?": "Yes",
      "reason": "This field (e.g., `platform_account.mensa.amazon_in.primary`) is crucial to confirm that the identified channel belongs to a marketplace, thus fulfilling the 'marketplace-managed' criterion."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id = 22` is consistently used as the identifier for Mensa within its `account_data_binding` cards."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT (SUBSTRING(name, 1, POSITION(' ' IN name) - 1))",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name",
    "deduplication_rule": "DISTINCT on extracted channel name (e.g., 'Amazon') to list unique channels."
  },
  "filters": [
    "group_level_id = '22'",
    "name LIKE '%Returns%'",
    "platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%walmart%'
  ],
  "joins": "No joins are required as all necessary information (binding name, platform account ID, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.",
  "missing_or_ambiguous": "The explicit physical table name for `account_data_bindings` is inferred. The fields `name`, `platform_account_id`, and `group_level_id` are logically inferred to exist within this metadata structure. The condition for 'marketplace-managed' is inferred by checking `platform_account_id` for known Mensa marketplaces ('Amazon', 'Walmart') and 'returns' is inferred from `name LIKE '%Returns%'`.",
  "sql_skeleton": "SELECT DISTINCT SUBSTRING(name, 1, POSITION(' ' IN name) - 1) AS channel_name FROM account_data_bindings WHERE group_level_id = '22' AND name LIKE '%Returns%' AND (platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%walmart%')"
}


---

## 008. Generate a summary report of OMS systems and their connected marketplaces.

### Query

```text
Generate a summary report of OMS systems and their connected marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### Errors

```json
{
  "GRAPH_COMPLETION": "500 Internal Server Error: {\"error\":\"Internal server error\",\"detail\":\"<failed_attempts>\\n\\n<generation number=\\\"1\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Field required [type=missing, input_value={'selected_source': 'meta...ace_to_wms_operations'\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\\n</exception>\\n<completion>\\n    ModelResponse(id='EP8VaovQL8nOpfgPlYnskAk', created=1779826447, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"selected_source\\\": \\\"metadata.business_flow_bindings\\\",\\\\n  \\\"rejected_sources\\\": [\\\\n    \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms\\\",\\\\n    \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_settlement\\\",\\\\n    \\\"account_data_binding.rosenza_international_trading_llc.amazon_us.primary.amazon_settlement\\\",\\\\n    \\\"account_data_binding.rosenza_international_trading_llc.shopify_d2c.primary.shopify_oms\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns\\\",\\\\n    \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse\\\",\\\\n    \\\"business_scope_set.mensa_brands.international_marketplaces\\\",\\\\n    \\\"business_scope_set.mensa_brands.logistics_settlement\\\",\\\\n    \\\"business_scope_set.mensa_brands.operations_wms\\\",\\\\n    \\\"business_scope_set.mensa_brands.payment_gateways\\\",\\\\n    \\\"business_scope_set.mensa_brands.shopify_d2c\\\",\\\\n    \\\"business_scope_set.mpl_india.active_payin_sources\\\",\\\\n    \\\"business_scope_set.mpl_india.active_payout_sources\\\",\\\\n    \\\"business_scope_set.mpl_india.bank_reconciliation\\\",\\\\n    \\\"business_scope_set.mpl_india.cashfree_expense\\\",\\\\n    \\\"account_data_binding.tanvi_fitness_private_limited.blitz_in.primary.blitz_settlement\\\",\\\\n    \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_disbursment\\\",\\\\n    \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_fee_preview\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement\\\",\\\\n    \\\"account_data_binding.ardeur_fashion.flipkart_in.primary.cashback\\\"\\\\n  ],\\\\n  \\\"require_tables\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"business_flow_bindings\\\",\\\\n      \\\"role\\\": \\\"Primary Data Source (Metadata)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"This logical table contains explicit definitions of business flows, including mappings from marketplaces to OMS/WMS systems (like Increff) for the specified tenant, making it the most direct source for \\\\'OMS systems and their connected marketplaces\\\\'.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"required_fields\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"group_id\\\",\\\\n      \\\"role\\\": \\\"Filter Column (Tenant Scope)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa Brands\\\\'. The relevant `business_flow_binding` for marketplace to OMS operations explicitly links to `group.tanvi_fitness_private_limited.mensa_brands`, which represents Mensa\\\\'s scope.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"binding_type\\\",\\\\n      \\\"role\\\": \\\"Filter Column (Flow Type)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Used to identify flows specifically representing marketplace-to-WMS/OMS operations, with the value \\\\'marketplace_to_wms_operations\\\\' being the most appropriate in the context.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"oms_system\\\",\\\\n      \\\"role\\\": \\\"Dimension (Derived)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Inferred logical field representing the OMS system name. This is extracted by parsing the `platform_account_id` from elements within the `participating_accounts` array where `role = \\\\'wms_operations\\\\'`.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"marketplace\\\",\\\\n      \\\"role\\\": \\\"Dimension (Derived)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Inferred logical field representing connected marketplace names. This is extracted by parsing the `platform_account_id` from elements within the `participating_accounts` array where `role = \\\\'marketplace_order_or_settlement_source\\\\'`.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"rejected_or_ambiguous_fields\\\": [\\\\n    \\\"participating_accounts\\\"\\\\n  ],\\\\n  \\\"metric_logic\\\": {\\\\n    \\\"formula\\\": \\\"List unique pairings of OMS system names and connected marketplace names, derived from the `participating_accounts` array within the relevant business flow bindings.\\\",\\\\n    \\\"numerator\\\": null,\\\\n    \\\"denominator\\\": null,\\\\n    \\\"aggregation_grain\\\": \\\"(oms_system, marketplace)\\\",\\\\n    \\\"deduplication_rule\\\": \\\"DISTINCT on (oms_system, marketplace) to show unique mappings.\\\"\\\\n  },\\\\n  \\\"filters\\\": [\\\\n    \\\"group_id = \\\\'group.tanvi_fitness_private_limited.mensa_brands\\\\'\\\",\\\\n    \\\"binding_type = \\\\'marketplace_to_wms_operations\\\\'\\\"\\\\n  ],\\\\n  \\\"joins\\\": \\\"No joins are required as all necessary information for this metadata report is logically contained within the `business_flow_bindings` metadata records.\\\",\\\\n  \\\"missing_or_ambiguous\\\": \\\"The explicit table structure for `metadata.business_flow_bindings` and direct SQL functions for querying JSON arrays are not provided. The logical fields `oms_system` and `marketplace` are inferred to be derived from the `participating_accounts` array using string parsing of `platform_account_id` and filtering by `role`. The context only explicitly details marketplace connections for Increff WMS for Mensa via a \\\\'marketplace_to_wms_operations\\\\' business flow binding; connections for Unicommerce OMS are not explicitly defined through a similar flow binding in the provided context, therefore, the report will be limited to Increff WMS.\\\",\\\\n  \\\"sql_skeleton\\\": \\\"SELECT DISTINCT\\\\\\\\n  [extracted_oms_system_name] AS oms_system,\\\\\\\\n  [extracted_marketplace_name] AS marketplace\\\\\\\\nFROM\\\\\\\\n  business_flow_bindings\\\\\\\\nWHERE\\\\\\\\n  group_id = \\\\'group.tanvi_fitness_private_limited.mensa_brands\\\\'\\\\\\\\n  AND binding_type = \\\\'marketplace_to_wms_operations\\\\'\\\"\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=13557, prompt_tokens=84699, total_tokens=98256, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=11814, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=83872), cache_read_input_tokens=83872), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n<generation number=\\\"2\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'meta....platform_account_id\\\\n\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</exception>\\n<completion>\\n    ModelResponse(id='W_8VaoiVMPWvpfgPoInK-Ak', created=1779826522, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"content\\\": {\\\\n    \\\"selected_source\\\": \\\"metadata.business_flow_bindings\\\",\\\\n    \\\"rejected_sources\\\": [\\\\n      \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms\\\",\\\\n      \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_settlement\\\",\\\\n      \\\"account_data_binding.rosenza_international_trading_llc.amazon_us.primary.amazon_settlement\\\",\\\\n      \\\"account_data_binding.rosenza_international_trading_llc.shopify_d2c.primary.shopify_oms\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns\\\",\\\\n      \\\"account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse\\\",\\\\n      \\\"business_scope_set.mensa_brands.international_marketplaces\\\",\\\\n      \\\"business_scope_set.mensa_brands.logistics_settlement\\\",\\\\n      \\\"business_scope_set.mensa_brands.operations_wms\\\",\\\\n      \\\"business_scope_set.mensa_brands.payment_gateways\\\",\\\\n      \\\"business_scope_set.mensa_brands.shopify_d2c\\\",\\\\n      \\\"business_scope_set.mpl_india.active_payin_sources\\\",\\\\n      \\\"business_scope_set.mpl_india.active_payout_sources\\\",\\\\n      \\\"business_scope_set.mpl_india.bank_reconciliation\\\",\\\\n      \\\"business_scope_set.mpl_india.cashfree_expense\\\",\\\\n      \\\"account_data_binding.tanvi_fitness_private_limited.blitz_in.primary.blitz_settlement\\\",\\\\n      \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_disbursment\\\",\\\\n      \\\"account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_fee_preview\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement\\\",\\\\n      \\\"account_data_binding.ardeur_fashion.flipkart_in.primary.cashback\\\"\\\\n    ],\\\\n    \\\"require_tables\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"business_flow_bindings\\\",\\\\n        \\\"role\\\": \\\"Primary Data Source (Metadata)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"This logical table contains explicit definitions of business flows, including mappings from marketplaces to OMS/WMS systems (like Increff) for the specified tenant, making it the most direct source for \\\\'OMS systems and their connected marketplaces\\\\'.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"required_fields\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"group_id\\\",\\\\n        \\\"role\\\": \\\"Filter Column (Tenant Scope)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa Brands\\\\'. The relevant `business_flow_binding` for marketplace to OMS operations explicitly links to `group.tanvi_fitness_private_limited.mensa_brands`, which represents Mensa\\\\'s scope.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"binding_type\\\",\\\\n        \\\"role\\\": \\\"Filter Column (Flow Type)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Used to identify flows specifically representing marketplace-to-WMS/OMS operations, with the value \\\\'marketplace_to_wms_operations\\\\' being the most appropriate in the context.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"participating_accounts\\\",\\\\n        \\\"role\\\": \\\"Raw Data Source for OMS and Marketplace Extraction\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"This JSON array contains the `platform_account_id` and `role` information necessary to identify both OMS systems (\\\\'wms_operations\\\\') and connected marketplaces (\\\\'marketplace_order_or_settlement_source\\\\').\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"oms_system\\\",\\\\n        \\\"role\\\": \\\"Dimension (Derived)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Inferred logical field representing the OMS system name. This is extracted by parsing the `platform_account_id` from elements within the `participating_accounts` array where `role = \\\\'wms_operations\\\\'`. For Mensa, this is \\\\'increff_wms\\\\' from the available context.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"marketplace\\\",\\\\n        \\\"role\\\": \\\"Dimension (Derived)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Inferred logical field representing connected marketplace names. This is extracted by parsing the `platform_account_id` from elements within the `participating_accounts` array where `role = \\\\'marketplace_order_or_settlement_source\\\\'. Examples include \\\\'amazon_in\\\\', \\\\'flipkart_in\\\\'.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"rejected_or_ambiguous_fields\\\": [],\\\\n    \\\"metric_logic\\\": {\\\\n      \\\"formula\\\": \\\"List unique pairings of OMS system names and connected marketplace names, derived from the `participating_accounts` array within the relevant business flow bindings.\\\",\\\\n      \\\"numerator\\\": null,\\\\n      \\\"denominator\\\": null,\\\\n      \\\"aggregation_grain\\\": \\\"(oms_system, marketplace)\\\",\\\\n      \\\"deduplication_rule\\\": \\\"DISTINCT on (oms_system, marketplace) to show unique mappings.\\\"\\\\n    },\\\\n    \\\"filters\\\": [\\\\n      \\\"group_id = \\\\'group.tanvi_fitness_private_limited.mensa_brands\\\\'\\\",\\\\n      \\\"binding_type = \\\\'marketplace_to_wms_operations\\\\'\\\"\\\\n    ],\\\\n    \\\"joins\\\": \\\"No joins are required as all necessary information for this metadata report is logically contained within the `business_flow_bindings` metadata records.\\\",\\\\n    \\\"missing_or_ambiguous\\\": \\\"The explicit table structure for `metadata.business_flow_bindings` and direct SQL functions for querying JSON arrays are not provided. The logical fields `oms_system` and `marketplace` are inferred to be derived from the `participating_accounts` array using string parsing of `platform_account_id` and filtering by `role`. The context only explicitly details marketplace connections for Increff WMS for Mensa via a \\\\'marketplace_to_wms_operations\\\\' business flow binding; connections for Unicommerce OMS are mentioned as general operational evidence but no specific marketplace-to-Unicommerce flow binding is provided in the context to extract its connected marketplaces. Therefore, the report will currently be limited to Increff WMS.\\\",\\\\n    \\\"sql_skeleton\\\": \\\"WITH ParsedAccounts AS (\\\\\\\\n  SELECT\\\\\\\\n    b.canonical_id AS flow_id,\\\\\\\\n    json_extract_path_text(pa.value::json, \\\\'platform_account_id\\\\') AS platform_account_id,\\\\\\\\n    json_extract_path_text(pa.value::json, \\\\'role\\\\') AS role\\\\\\\\n  FROM\\\\\\\\n    business_flow_bindings b,\\\\\\\\n    json_array_elements(b.participating_accounts) AS pa\\\\\\\\n  WHERE\\\\\\\\n    b.group_id = \\\\'group.tanvi_fitness_private_limited.mensa_brands\\\\'\\\\\\\\n    AND b.binding_type = \\\\'marketplace_to_wms_operations\\\\'\\\\\\\\n)\\\\\\\\nSELECT DISTINCT\\\\\\\\n  SPLIT_PART(MAX(CASE WHEN pa.role = \\\\'wms_operations\\\\' THEN pa.platform_account_id END), \\\\'.\\\\', 4) AS oms_system,\\\\\\\\n  SPLIT_PART(pa_mp.platform_account_id, \\\\'.\\\\', 4) AS marketplace\\\\\\\\nFROM\\\\\\\\n  ParsedAccounts pa\\\\\\\\nJOIN\\\\\\\\n  ParsedAccounts pa_mp ON pa.flow_id = pa_mp.flow_id\\\\\\\\nWHERE\\\\\\\\n  pa.role = \\\\'wms_operations\\\\'\\\\\\\\n  AND pa_mp.role = \\\\'marketplace_order_or_settlement_source\\\\'\\\\\\\\nGROUP BY\\\\\\\\n  pa.flow_id, pa_mp.platform_account_id\\\\\\\\n\\\"\\\\n  }\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=17286, prompt_tokens=173410, total_tokens=190696, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=13432, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=167739), cache_read_input_tokens=83867), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n</failed_attempts>\\n\\n<last_exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'meta....platform_account_id\\\\n\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</last_exception>\"}"
}
```


---

## 009. Calculate the combined marketplace contribution vs own website contribution.

### Query

```text
Calculate the combined marketplace contribution vs own website contribution.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "platform_domain.increff.operations",
  "rejected_sources": [
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_settlement",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_disbursment",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.oms",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.cashback",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.settlement",
    "account_data_binding.tanvi_fitness_private_limited.flipkart_in.primary.commission",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_oms",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_settlement",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_reverse",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_non_order_settlement",
    "account_data_binding.tanvi_fitness_private_limited.myntra_in.primary.myntra_oms_settlement",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_sales",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_settlement",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_reverse",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_reverse_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.tanvi_fitness_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_oms",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_settlement",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_addition_charge",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_mapper_gst",
    "account_data_binding.tanvi_fitness_private_limited.nykaa_in.primary.nykaa_mapping",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_oms",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_settlement",
    "account_data_binding.tanvi_fitness_private_limited.jiomart_in.primary.jiomart_returns",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_oms",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_settlement",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_commission",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_sales_return",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_payments",
    "account_data_binding.tanvi_fitness_private_limited.snapdeal_in.primary.snapdeal_non_order",
    "account_data_binding.tanvi_fitness_private_limited.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.tanvi_fitness_private_limited.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_oms",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_settlement",
    "account_data_binding.tanvi_fitness_private_limited.healthkart_in.primary.healthkart_return",
    "account_data_binding.tanvi_fitness_private_limited.increff_wms.primary.increff_sales",
    "account_data_binding.tanvi_fitness_private_limited.increff_wms.primary.increff_returns",
    "account_data_binding.tanvi_fitness_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_to_increff_operations",
    "business_flow_binding.tanvi_fitness_private_limited.marketplace_transactions_review",
    "table.zs_observe.marketplace_transactions",
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "2026-05-24",
    "snapdeal commission account data binding",
    "tanvi fitness private limited primary snapdeal account",
    "snapdeal non order account data binding"
  ],
  "require_tables": [
    {
      "field": "increff_operations_orders_data",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "Inferred as the main logical table within the 'platform_domain.increff.operations' that contains order-level details including channel information and is scoped for Mensa. Previous queries also utilized this domain for order volume and channel-related metrics, further reinforced by its associated filters (is_active, order_status, transaction_type)."
    }
  ],
  "required_fields": [
    {
      "field": "channel",
      "role": "Dimension for categorization",
      "selected?": "Yes",
      "reason": "Required to categorize orders into 'marketplace' or 'own website' contribution. Inferred as the logical column name for channel within order data for Increff operations."
    },
    {
      "field": "order_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Needed to calculate 'order volume' as a proxy for contribution. Inferred as the logical column name for a unique order identifier within Increff operations order data."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier. This is a standard filter for Mensa's operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`is_active = true`) for general data validity in Increff operations. This ensures only active records are considered for contribution calculation."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order contribution calculation."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `required_filters` (`transaction_type = SALES`) in Increff operations, implying relevance for valid order contribution calculation."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Calculate the percentage of total distinct orders attributed to 'Marketplace' channels and 'Own Website' channels.",
    "numerator": "COUNT(DISTINCT order_id) for 'Marketplace' or 'Own Website' channels",
    "denominator": "Total COUNT(DISTINCT order_id) for Mensa across all channels",
    "aggregation_grain": "channel_category (Marketplace, Own Website)",
    "deduplication_rule": "COUNT(DISTINCT order_id) to count unique orders for volume-based contribution."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No specific joins can be determined from the context as all necessary fields are inferred to exist within the single selected table `increff_operations_orders_data`, adhering to the hard rule for single source tables.",
  "missing_or_ambiguous": "The explicit physical table name for 'increff_operations_orders_data' and precise column names for 'channel', 'order_id', 'group_level_id', 'is_active', 'order_status', and 'transaction_type' are not explicitly stated in the context. These were logically inferred based on domain knowledge, previous query patterns, and the `execution_constraint_set.increff.operations_manifest_refactored_constraints` for Mensa's Increff operations. The specific mapping of channel names to 'Marketplace' or 'Own Website' categories is also an inference based on common channel types.",
  "sql_skeleton": "WITH MensaOrders AS (\n    SELECT\n        CASE\n            WHEN channel = 'Website' THEN 'Own Website'\n            WHEN channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace'\n            ELSE 'Other'\n        END AS channel_category,\n        order_id\n    FROM\n        increff_operations_orders_data\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n),\nCategorizedOrderCounts AS (\n    SELECT\n        channel_category,\n        COUNT(DISTINCT order_id) AS orders_count\n    FROM\n        MensaOrders\n    GROUP BY\n        channel_category\n),\nTotalOrderCount AS (\n    SELECT\n        COUNT(DISTINCT order_id) AS total_orders\n    FROM\n        MensaOrders\n)\nSELECT\n    coc.channel_category,\n    (CAST(coc.orders_count AS DOUBLE) / tot.total_orders) * 100 AS contribution_percentage\nFROM\n    CategorizedOrderCounts coc,\n    TotalOrderCount tot\nWHERE\n    coc.channel_category IN ('Marketplace', 'Own Website')"
}


---

## 010. Identify channels with higher operational dependency on manual processes.

### Query

```text
Identify channels with higher operational dependency on manual processes.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### Errors

```json
{
  "GRAPH_COMPLETION": "500 Internal Server Error: {\"error\":\"Internal server error\",\"detail\":\"<failed_attempts>\\n\\n<generation number=\\\"1\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Field required [type=missing, input_value={'selected_source': 'meta...on_type = 'Manual CSV'\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\\n</exception>\\n<completion>\\n    ModelResponse(id='FAAWaqLMFsnOpfgPlYnskAk', created=1779826707, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"selected_source\\\": \\\"metadata.account_data_bindings\\\",\\\\n  \\\"rejected_sources\\\": [\\\\n    \\\"business_scope_set.mensa_brands.international_marketplaces\\\",\\\\n    \\\"business_scope_set.mensa_brands.logistics_settlement\\\",\\\\n    \\\"business_scope_set.mensa_brands.operations_wms\\\",\\\\n    \\\"business_scope_set.mensa_brands.payment_gateways\\\",\\\\n    \\\"business_scope_set.mensa_brands.shopify_d2c\\\",\\\\n    \\\"business_scope_set.mpl_india.active_payin_sources\\\",\\\\n    \\\"business_scope_set.mpl_india.active_payout_sources\\\",\\\\n    \\\"business_scope_set.mpl_india.bank_reconciliation\\\",\\\\n    \\\"business_scope_set.mpl_india.cashfree_expense\\\",\\\\n    \\\"documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.\\\",\\\\n    \\\"scopespecificationnote\\\",\\\\n    \\\"scope specification note\\\",\\\\n    \\\"scopespecnote\\\"\\\\n  ],\\\\n  \\\"require_tables\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"account_data_bindings\\\",\\\\n      \\\"role\\\": \\\"Source for Channel Definitions and Integration Types\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"This logical table contains information about different channels and their integration types, which is necessary to identify channels with \\\\'manual processes\\\\'. This aligns with previous query patterns for \\\\'Manual CSV integration\\\\'.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"required_fields\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"channel_name\\\",\\\\n      \\\"role\\\": \\\"Dimension\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Explicitly requested to \\\\'Identify channels\\\\'. This is inferred as the column representing the channel\\\\'s identifier or name within the `account_data_bindings`.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"integration_type\\\",\\\\n      \\\"role\\\": \\\"Filter Column\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required to identify channels with \\\\'manual processes\\\\'. \\\\'Manual CSV\\\\' is a known value for manual integration types from previous queries and is inferred to indicate high operational dependency on manual processes.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"group_level_id\\\",\\\\n      \\\"role\\\": \\\"Filter Column\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa\\\\'. The `group_level_id = 22` is consistently used as the identifier for Mensa within its `account_data_binding` cards.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"rejected_or_ambiguous_fields\\\": [],\\\\n  \\\"metric_logic\\\": {\\\\n    \\\"formula\\\": \\\"SELECT DISTINCT channel_name\\\",\\\\n    \\\"numerator\\\": null,\\\\n    \\\"denominator\\\": null,\\\\n    \\\"aggregation_grain\\\": \\\"channel_name\\\",\\\\n    \\\"deduplication_rule\\\": \\\"DISTINCT on (channel_name) to list unique channels.\\\"\\\\n  },\\\\n  \\\"filters\\\": [\\\\n    \\\"group_level_id = \\\\'22\\\\'\\\",\\\\n    \\\"integration_type = \\\\'Manual CSV\\\\'\\\"\\\\n  ],\\\\n  \\\"joins\\\": \\\"No joins are required as all necessary information (channel name, integration type, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.\\\",\\\\n  \\\"missing_or_ambiguous\\\": \\\"The explicit physical table name for `account_data_bindings` and the column names `channel_name` and `integration_type` are not provided in the context and were inferred. The specific value \\\\'Manual CSV\\\\' for `integration_type` is also inferred as the indicator of \\\\'manual processes\\\\'.\\\",\\\\n  \\\"sql_skeleton\\\": \\\"SELECT DISTINCT channel_name FROM account_data_bindings WHERE group_level_id = \\\\'22\\\\' AND integration_type = \\\\'Manual CSV\\\\'\\\"\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=1390, prompt_tokens=54181, total_tokens=55571, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=530, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=54176), cache_read_input_tokens=54176), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n<generation number=\\\"2\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'meta...on_type = 'Manual CSV'\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</exception>\\n<completion>\\n    ModelResponse(id='HAAWavPOO8WimecPi67z-AM', created=1779826716, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"content\\\": {\\\\n    \\\"selected_source\\\": \\\"metadata.account_data_bindings\\\",\\\\n    \\\"rejected_sources\\\": [\\\\n      \\\"business_scope_set.mensa_brands.international_marketplaces\\\",\\\\n      \\\"business_scope_set.mensa_brands.logistics_settlement\\\",\\\\n      \\\"business_scope_set.mensa_brands.operations_wms\\\",\\\\n      \\\"business_scope_set.mensa_brands.payment_gateways\\\",\\\\n      \\\"business_scope_set.mensa_brands.shopify_d2c\\\",\\\\n      \\\"business_scope_set.mpl_india.active_payin_sources\\\",\\\\n      \\\"business_scope_set.mpl_india.active_payout_sources\\\",\\\\n      \\\"business_scope_set.mpl_india.bank_reconciliation\\\",\\\\n      \\\"business_scope_set.mpl_india.cashfree_expense\\\",\\\\n      \\\"documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.\\\",\\\\n      \\\"scopespecificationnote\\\",\\\\n      \\\"scope specification note\\\",\\\\n      \\\"scopespecnote\\\"\\\\n    ],\\\\n    \\\"require_tables\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"account_data_bindings\\\",\\\\n        \\\"role\\\": \\\"Source for Channel Definitions and Integration Types\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"This logical table contains information about different channels and their integration types, which is necessary to identify channels with \\\\'manual processes\\\\'. This aligns with previous query patterns for \\\\'Manual CSV integration\\\\'.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"required_fields\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"channel_name\\\",\\\\n        \\\"role\\\": \\\"Dimension\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Explicitly requested to \\\\'Identify channels\\\\'. This is inferred as the column representing the channel\\\\'s identifier or name within the `account_data_bindings`.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"integration_type\\\",\\\\n        \\\"role\\\": \\\"Filter Column\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required to identify channels with \\\\'manual processes\\\\'. \\\\'Manual CSV\\\\' is a known value for manual integration types from previous queries and is inferred to indicate high operational dependency on manual processes.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"group_level_id\\\",\\\\n        \\\"role\\\": \\\"Filter Column\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa\\\\'. The `group_level_id = 22` is consistently used as the identifier for Mensa within its `account_data_binding` cards.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"rejected_or_ambiguous_fields\\\": [],\\\\n    \\\"metric_logic\\\": {\\\\n      \\\"formula\\\": \\\"SELECT DISTINCT channel_name\\\",\\\\n      \\\"numerator\\\": null,\\\\n      \\\"denominator\\\": null,\\\\n      \\\"aggregation_grain\\\": \\\"channel_name\\\",\\\\n      \\\"deduplication_rule\\\": \\\"DISTINCT on (channel_name) to list unique channels.\\\"\\\\n    },\\\\n    \\\"filters\\\": [\\\\n      \\\"group_level_id = \\\\'22\\\\'\\\",\\\\n      \\\"integration_type = \\\\'Manual CSV\\\\'\\\"\\\\n    ],\\\\n    \\\"joins\\\": \\\"No joins are required as all necessary information (channel name, integration type, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.\\\",\\\\n    \\\"missing_or_ambiguous\\\": \\\"The explicit physical table name for `account_data_bindings` and the column names `channel_name` and `integration_type` are not provided in the context and were inferred. The specific value \\\\'Manual CSV\\\\' for `integration_type` is also inferred as the indicator of \\\\'manual processes\\\\'.\\\",\\\\n    \\\"sql_skeleton\\\": \\\"SELECT DISTINCT channel_name FROM account_data_bindings WHERE group_level_id = \\\\'22\\\\' AND integration_type = \\\\'Manual CSV\\\\'\\\"\\\\n  }\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=2996, prompt_tokens=110582, total_tokens=113578, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=1267, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=108346), cache_read_input_tokens=54170), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n</failed_attempts>\\n\\n<last_exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'meta...on_type = 'Manual CSV'\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</last_exception>\"}"
}
```


---

## 011. Create a marketplace risk report showing which channels depend on the same OMS.

### Query

```text
Create a marketplace risk report showing which channels depend on the same OMS.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_reverse",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_settlement",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_disbursment",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_settlement",
    "account_data_binding.ardeur_fashion.flipkart_in.primary.cashback",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "Mensa's operations often involve Increff for WMS/OMS functionality as per `business_scope_set.mensa_brands.operations_wms`. This table is part of the `platform_domain.increff.operations` and is expected to contain `sales_channel` information for various marketplaces processed by this OMS."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Explicitly requested for the report ('which channels'). This column is logically inferred to exist within an OMS sales table like `increff_sales` to identify the sales channel for each order."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier in Mensa's `account_data_binding` cards and is a standard filter for operational tables."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT 'Increff Operations' AS oms_system, sales_channel",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(oms_system, sales_channel)",
    "deduplication_rule": "DISTINCT on (sales_channel) to list unique marketplace channels processed by the Increff OMS."
  },
  "filters": [
    "group_level_id = '22'",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (sales channel and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of a `sales_channel` column within `table.zs_observe.increff_sales` is inferred from domain knowledge and similar tables. The specific list of marketplace channels for the filter is inferred based on common marketplaces handled by Mensa, as hinted in other `account_data_binding` cards and previous queries. The 'Increff Operations' as the common OMS system is inferred from Mensa's use of Increff for its operations.",
  "sql_skeleton": "SELECT DISTINCT 'Increff Operations' AS oms_system, sales_channel FROM zs_observe.increff_sales WHERE group_level_id = '22' AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
}


---

## 012. Generate a logistics dependency matrix showing courier concentration across marketplaces.

### Query

```text
Generate a logistics dependency matrix showing courier concentration across marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "cleaned_v2`",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "raw cleaned v2 clients mpl usa json",
    "source document",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources",
    "business_scope_set.mpl_india.bank_reconciliation",
    "business_scope_set.mpl_india.cashfree_expense",
    "account_data_binding.mensa.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_returns",
    "account_data_binding.mensa.meesho_in.primary.meesho_reverse",
    "account_data_binding.mensa.meesho_in.primary.meesho_reverse_expenses",
    "account_data_binding.mensa.meesho_in.primary.meesho_sales",
    "account_data_binding.mensa.meesho_in.primary.meesho_settlement",
    "account_data_binding.mensa.myntra_in.primary.myntra_non_order_settlement",
    "account_data_binding.mensa.myntra_in.primary.myntra_oms",
    "account_data_binding.mensa.myntra_in.primary.myntra_oms_settlement",
    "account_data_binding.mensa.xpressbees_in.primary.xpressbees_settlement",
    "account_data_binding.mpl_india.amazon_payin.primary.amazon_payin",
    "account_data_binding.mpl_india.cashfree_expense.primary.cashfree_expense_report",
    "account_data_binding.mpl_india.cashfree_payin.primary.cashfree_payin",
    "account_data_binding.mpl_india.cashfree_payout.primary.cashfree_payout",
    "account_data_binding.mpl_india.easebuzz_payin.primary.easebuzz_payin",
    "account_data_binding.mpl_india.idfc_bank.primary.idfc_bank",
    "account_data_binding.mpl_india.paynimo_payin.primary.paynimo_payin",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_addition_charge",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_mapper_gst",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_mapping",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_oms",
    "account_data_binding.bear_house_clothing.nykaa_in.primary.nykaa_settlement",
    "account_data_binding.bear_house_clothing.tatacliq_in.primary.tatacliq_oms",
    "account_data_binding.bear_house_clothing.tatacliq_in.primary.tatacliq_settlement",
    "account_data_binding.bear_house_clothing.unicommerce_oms.primary.unicommerce"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is suitable for linking couriers (`fulfilment_channel`) and marketplaces (`sales_channel`) for Mensa, as indicated by its inclusion in `business_scope_set.mensa_brands.operations_wms` and its common use in similar previous queries for Mensa's operational data."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify the 'marketplaces' as requested in the report. This column is logically present in a sales table to indicate the origin of the sale."
    },
    {
      "field": "fulfilment_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to identify 'couriers' as requested in the report. The column description 'Courier/logistics partner used (80+ variants)' in `table.zs_observe.increff_sales` directly matches this requirement."
    },
    {
      "field": "order_id",
      "role": "Metric Identifier",
      "selected?": "Yes",
      "reason": "Required to calculate 'concentration' as a count of shipments/orders. Counting distinct order IDs provides the volume metric for the dependency matrix."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa'. The `group_level_id = 22` is the documented identifier for Mensa across its operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set`."
    },
    {
      "field": "order_status",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set`."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "COUNT(DISTINCT order_id)",
    "numerator": "COUNT(DISTINCT order_id)",
    "denominator": null,
    "aggregation_grain": "(sales_channel, fulfilment_channel)",
    "deduplication_rule": "COUNT(DISTINCT order_id) to count unique shipments/orders per marketplace and courier."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (marketplace, courier, order count, and tenant ID) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel`, `order_id`, `is_active`, `order_status`, and `transaction_type` columns within `table.zs_observe.increff_sales` is inferred from domain knowledge of sales/operations tables and previous similar queries for Mensa. These inferences are based on the need to fulfill the query's grouping, metric calculation, and filtering conditions.",
  "sql_skeleton": "SELECT sales_channel, fulfilment_channel, COUNT(DISTINCT order_id) AS shipment_count FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES' GROUP BY sales_channel, fulfilment_channel ORDER BY sales_channel, fulfilment_channel"
}


---

## 013. Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

### Query

```text
Build a report identifying channels that may face reconciliation delays due to marketplace-based settlements.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "metadata.account_data_bindings",
  "rejected_sources": [
    "account_data_binding.prita_designs_private_limited.klip_in.primary.klip_settlement",
    "account_data_binding.prita_designs_private_limited.marketplace_transactions.primary.marketplace_transactions",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_brand_mapping",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_forward_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_other_charges_expenses",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_returns",
    "account_data_binding.prita_designs_private_limited.meesho_in.primary.meesho_reverse"
  ],
  "require_tables": [
    {
      "field": "account_data_bindings",
      "role": "Source for Channel and Settlement Definitions",
      "selected?": "Yes",
      "reason": "This logical table (representing account data binding metadata) contains configurations for how different platforms/channels are integrated, including settlement processes. It is the appropriate source to identify which marketplace channels have settlement definitions."
    }
  ],
  "required_fields": [
    {
      "field": "name",
      "role": "Dimension (Channel/Settlement Type)",
      "selected?": "Yes",
      "reason": "The 'name' field of an `account_data_binding` card (e.g., 'Amazon Settlement') explicitly indicates the channel and that it's a settlement binding, which is crucial for identifying channels with marketplace-based settlements."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier used in Mensa's operational data."
    },
    {
      "field": "platform_account_id",
      "role": "Filter Column (Marketplace Identification)",
      "selected?": "Yes",
      "reason": "This field (e.g., `platform_account.mensa.amazon_in.primary`) is necessary to confirm that the identified settlement binding is indeed for a 'marketplace' and to help extract the marketplace name."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SELECT DISTINCT SUBSTRING(name, 1, POSITION(' ' IN name) - 1)",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "channel_name",
    "deduplication_rule": "DISTINCT on extracted channel name to list unique marketplace channels with settlement bindings."
  },
  "filters": [
    "group_level_id = '22'",
    "name LIKE '%Settlement%'",
    "platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%flipkart%' OR platform_account_id LIKE '%myntra%' OR platform_account_id LIKE '%meesho%' OR platform_account_id LIKE '%nykaa%' OR platform_account_id LIKE '%jiomart%' OR platform_account_id LIKE '%snapdeal%' OR platform_account_id LIKE '%tatacliq%' OR platform_account_id LIKE '%healthkart%'"
  ],
  "joins": "No joins are required as all necessary information (binding name, platform account ID, and tenant scope) is inferred to exist within a single logical metadata table representing the account data bindings.",
  "missing_or_ambiguous": "The explicit physical table name for `account_data_bindings` is inferred. The fields `name`, `platform_account_id`, and `group_level_id` are logically inferred to exist within this metadata structure. The condition for 'marketplace-based' is inferred by checking `platform_account_id` for known Mensa marketplaces ('Amazon', 'Flipkart', etc.) and 'settlements' is inferred from `name LIKE '%Settlement%'`. The link between marketplace settlements and 'reconciliation delays' is a business context inference; this query identifies the channels susceptible to such delays.",
  "sql_skeleton": "SELECT DISTINCT SUBSTRING(name, 1, POSITION(' ' IN name) - 1) AS channel_name FROM metadata.account_data_bindings WHERE group_level_id = '22' AND name LIKE '%Settlement%' AND (platform_account_id LIKE '%amazon%' OR platform_account_id LIKE '%flipkart%' OR platform_account_id LIKE '%myntra%' OR platform_account_id LIKE '%meesho%' OR platform_account_id LIKE '%nykaa%' OR platform_account_id LIKE '%jiomart%' OR platform_account_id LIKE '%snapdeal%' OR platform_account_id LIKE '%tatacliq%' OR platform_account_id LIKE '%healthkart%')"
}


---

## 014. Compare return handling models between own website and marketplace channels.

### Query

```text
Compare return handling models between own website and marketplace channels.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_returns",
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is described as a 'Cross-channel returns log (ops view)' and explicitly includes 'returns fulfilment evidence' for Increff operations, which processes both marketplace and own website orders for Mensa."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension for comparison",
      "selected?": "Yes",
      "reason": "Required to distinguish between 'own website' and 'marketplace' channels to compare their return handling models. This column is logically present in a cross-channel returns log."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', where `group_level_id = 22` is the documented identifier in Mensa's operational data."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`is_active = true`) for data validity in `table.zs_observe.increff_returns`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Categorize sales_channel into 'Marketplace Returns' or 'Own Website Returns' to compare their handling models.",
    "numerator": null,
    "denominator": null,
    "aggregation_grain": "(sales_channel, return_handling_model)",
    "deduplication_rule": "DISTINCT on (sales_channel) to identify unique channels and their inferred return handling model."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true"
  ],
  "joins": "No joins are required as all necessary information (sales channel, tenant ID, and activity status) is inferred to exist within the single selected table `zs_observe.increff_returns`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` within `table.zs_observe.increff_returns` is inferred based on domain knowledge of cross-channel return logs. The categorization into 'Marketplace Returns' and 'Own Website Returns' based on the `sales_channel` value is an inference using common channel types and Mensa's known platforms (Shopify for D2C/own website; Amazon, Flipkart, etc. for marketplaces).",
  "sql_skeleton": "SELECT DISTINCT\n    sales_channel,\n    CASE\n        WHEN sales_channel IN ('Shopify', 'Website') THEN 'Own Website Returns'\n        WHEN sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace Returns'\n        ELSE 'Other/Unspecified Returns'\n    END AS return_handling_model\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = '22'\n    AND is_active = true\nORDER BY\n    return_handling_model, sales_channel"
}


---

## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": null,
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.mensa.amazon_in.primary.amazon_disbursment",
    "account_data_binding.mensa.amazon_in.primary.amazon_fee_preview",
    "account_data_binding.mensa.amazon_in.primary.amazon_oms",
    "account_data_binding.mensa.amazon_in.primary.amazon_returns",
    "account_data_binding.mensa.amazon_in.primary.amazon_settlement",
    "account_data_binding.mensa.cashfree_in.primary.cashfree_expense_report",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "astrotalk marketplace to unicommerce operations",
    "businessflowbinding",
    "business flow binding",
    "2026-05-24"
  ],
  "require_tables": [],
  "required_fields": [],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": null,
    "numerator": null,
    "denominator": null,
    "aggregation_grain": null,
    "deduplication_rule": null
  },
  "filters": [],
  "joins": "No joins can be determined as the core information is missing.",
  "missing_or_ambiguous": "The provided context explicitly indicates that Unicommerce data bindings are for 'Fraternitas Ventures' (group_level_id 337), not 'Mensa Brands' (group_level_id 22). Therefore, no operational dependencies for Mensa on Unicommerce can be identified from the given context.",
  "sql_skeleton": "/* Insufficient information to generate a SQL query. The context does not establish any dependency of Mensa Brands on Unicommerce. */"
}


---

## 016. Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

### Query

```text
Create a sales concentration analysis report to determine dependency on top 2 marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "This chunk is about two business flow...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0081\" pack_index: 81...",
    "This chunk is about eight active \"account_data_binding\"...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0061\" pack_index: 61...",
    "canonical_pack_0024",
    "canonical_pack_0081",
    "primary` - scope_keys: ```json [ { \"business_key\":...",
    "canonical_pack_0061",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "This chunk describes nine active \"account_data_binding\" cards..."
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is an evidence table for marketplace operations and sales data for Mensa (group_level_id=22), containing both sales channel information and order details necessary for a sales concentration analysis."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Marketplace Identifier)",
      "selected?": "Yes",
      "reason": "Required to group sales by marketplace and identify the top performers, directly addressing 'top 2 marketplaces'."
    },
    {
      "field": "order_id",
      "role": "Metric (Sales Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used to calculate the sales concentration by counting unique orders, serving as a proxy for sales volume per channel, as an explicit sales amount column is not detailed in the context."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`is_active = true`) for data validity in Increff operations, ensuring only active records are considered."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Order Status)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`order_status = COMPLETED`) in Increff operations, crucial for analyzing valid sales transactions."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Transaction Type)",
      "selected?": "Yes",
      "reason": "Explicitly listed as a `mandatory_filter` (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions contribute to the analysis."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Calculate the total count of distinct orders per marketplace and then determine the percentage contribution of the top 2 marketplaces to the total marketplace orders.",
    "numerator": "COUNT(DISTINCT order_id) for a specific marketplace",
    "denominator": "SUM(COUNT(DISTINCT order_id)) for all marketplaces",
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) to ensure each unique order is counted once for volume calculation."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')"
  ],
  "joins": "No joins are required as all necessary information (marketplace, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `sales_channel` and `order_id` columns within `table.zs_observe.increff_sales` is inferred from domain knowledge of sales/operations tables and previous Mensa queries. The list of marketplace channels used in the filter is consistently inferred from previous Mensa-specific queries.",
  "sql_skeleton": "WITH MarketplaceOrders AS (\n    SELECT\n        sales_channel,\n        COUNT(DISTINCT order_id) AS channel_order_count\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n        AND sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart')\n    GROUP BY\n        sales_channel\n),\nRankedMarketplaces AS (\n    SELECT\n        sales_channel,\n        channel_order_count,\n        RANK() OVER (ORDER BY channel_order_count DESC) as rnk\n    FROM\n        MarketplaceOrders\n),\nTotalMarketplaceOrders AS (\n    SELECT\n        SUM(channel_order_count) AS total_orders\n    FROM\n        MarketplaceOrders\n)\nSELECT\n    rm.sales_channel,\n    rm.channel_order_count,\n    (CAST(rm.channel_order_count AS DOUBLE) / tmo.total_orders) * 100 AS percentage_of_total_marketplace_orders\nFROM\n    RankedMarketplaces rm, TotalMarketplaceOrders tmo\nWHERE\n    rm.rnk <= 2\nORDER BY\n    rm.rnk"
}


---

## 017. Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

### Query

```text
Generate a unified dashboard combining sales, OMS dependency, courier dependency, and return ownership.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": null,
  "rejected_sources": [
    "account_data_binding.fraternitas.shopify_d2c.primary.shopify_oms",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce",
    "account_data_binding.fraternitas.unicommerce_oms.primary.unicommerce_order_sales_report",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_credit_note",
    "account_data_binding.ardeur_fashion.ajio_in.primary.ajio_oms",
    "account_data_binding.ardeur_fashion.amazon_in.primary.amazon_oms",
    "account_data_binding.rosenza_international_trading_llc.amazon_us.primary.amazon_settlement",
    "account_data_binding.rosenza_international_trading_llc.shopify_d2c.primary.shopify_oms",
    "account_data_binding.tanvi_fitness_private_limited.amazon_in.primary.amazon_oms",
    "business_scope_set.mensa_brands.international_marketplaces",
    "business_scope_set.mensa_brands.logistics_settlement",
    "business_scope_set.mensa_brands.payment_gateways",
    "business_scope_set.mensa_brands.shopify_d2c",
    "business_scope_set.mpl_india.active_payin_sources",
    "business_scope_set.mpl_india.active_payout_sources"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table (Sales, OMS, Courier)",
      "selected?": "Yes",
      "reason": "This table is central to Mensa's operations (via Increff WMS/OMS) and provides sales data, channel information, and fulfilment details (couriers) as identified in previous queries."
    },
    {
      "field": "zs_observe.increff_returns",
      "role": "Primary Data Source Table (Returns)",
      "selected?": "Yes",
      "reason": "This table is explicitly a 'Cross-channel returns log (ops view)' for Mensa's Increff operations and is necessary to gather data on return ownership/handling models, as identified in previous queries."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension (Common Grouping Key)",
      "selected?": "Yes",
      "reason": "This field is present in both `increff_sales` and `increff_returns` and is essential for combining data by channel and categorizing into marketplace vs. own website."
    },
    {
      "field": "order_id",
      "role": "Metric (Sales Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used in `increff_sales` to quantify sales volume and concentration. Inferred as the unique identifier for sales transactions."
    },
    {
      "field": "fulfilment_channel",
      "role": "Dimension (Courier Dependency)",
      "selected?": "Yes",
      "reason": "From `increff_sales`, this column directly identifies the courier/logistics partner for sales orders, crucial for courier concentration analysis."
    },
    {
      "field": "return_id",
      "role": "Metric (Return Volume Proxy)",
      "selected?": "Yes",
      "reason": "Used in `increff_returns` to quantify return volume. Inferred as the unique identifier for return transactions."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column (Tenant Scope)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`group_level_id = 22`) for all Mensa-scoped data in both `increff_sales` and `increff_returns`."
    },
    {
      "field": "is_active",
      "role": "Filter Column (Record Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`is_active = true`) for data validity in both `increff_sales` and `increff_returns`."
    },
    {
      "field": "order_status",
      "role": "Filter Column (Sales Order Status)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`order_status = COMPLETED`) for valid sales transactions in `increff_sales`."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column (Sales Transaction Type)",
      "selected?": "Yes",
      "reason": "Mandatory filter (`transaction_type = SALES`) for valid sales transactions in `increff_sales`."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "Consolidate sales volume, OMS dependency (implicit 'Increff Operations'), courier concentration, and return volume/handling model by sales channel.",
    "numerator": "COUNT(DISTINCT order_id) for sales; COUNT(DISTINCT return_id) for returns.",
    "denominator": null,
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) and COUNT(DISTINCT return_id) to count unique sales and return transactions respectively."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED' (for sales)",
    "transaction_type = 'SALES' (for sales)",
    "sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart', 'Shopify', 'Website') (inferred categories)"
  ],
  "joins": "A FULL OUTER JOIN is used to combine aggregated sales data (from `zs_observe.increff_sales`) and aggregated returns data (from `zs_observe.increff_returns`) based on the common dimension `sales_channel`. This allows for a unified view where a channel might have sales but no returns, or vice versa.",
  "missing_or_ambiguous": "The request for a 'unified dashboard combining' multiple distinct data points (sales, OMS, courier, returns) implies consolidation of data from multiple sources. While the hard rules usually default to a single source, 'combining' is interpreted here as an explicit request for consolidation. The specific column names `order_id` in `increff_sales` and `return_id` in `increff_returns` are inferred as unique identifiers. The identification of 'Increff Operations' as the OMS and the categorization of `sales_channel` into 'Own Website' vs. 'Marketplace' for return handling are strong inferences from previous query patterns and domain knowledge.",
  "sql_skeleton": "WITH SalesData AS (\n    SELECT\n        sales_channel,\n        'Increff Operations' AS oms_system,\n        COUNT(DISTINCT order_id) AS total_sales_orders,\n        COUNT(DISTINCT fulfilment_channel) AS num_unique_couriers_for_sales\n    FROM\n        zs_observe.increff_sales\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n        AND order_status = 'COMPLETED'\n        AND transaction_type = 'SALES'\n    GROUP BY\n        sales_channel\n),\nReturnsData AS (\n    SELECT\n        sales_channel,\n        CASE\n            WHEN sales_channel IN ('Shopify', 'Website') THEN 'Own Website Returns'\n            WHEN sales_channel IN ('Amazon', 'Flipkart', 'Myntra', 'Meesho', 'Nykaa', 'Jiomart', 'Snapdeal', 'Tatacliq', 'Healthkart') THEN 'Marketplace Returns'\n            ELSE 'Other/Unspecified Returns'\n        END AS return_handling_model,\n        COUNT(DISTINCT return_id) AS total_returns\n    FROM\n        zs_observe.increff_returns\n    WHERE\n        group_level_id = '22'\n        AND is_active = true\n    GROUP BY\n        sales_channel\n)\nSELECT\n    COALESCE(sd.sales_channel, rd.sales_channel) AS sales_channel,\n    sd.oms_system,\n    COALESCE(sd.total_sales_orders, 0) AS total_sales_orders,\n    sd.num_unique_couriers_for_sales,\n    rd.return_handling_model,\n    COALESCE(rd.total_returns, 0) AS total_returns\nFROM\n    SalesData sd\nFULL OUTER JOIN\n    ReturnsData rd ON sd.sales_channel = rd.sales_channel\nORDER BY\n    COALESCE(sd.sales_channel, rd.sales_channel)"
}


---

## 018. Design a profitability analysis report estimating operational complexity cost per marketplace.

### Query

```text
Design a profitability analysis report estimating operational complexity cost per marketplace.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": null,
  "rejected_sources": [],
  "require_tables": [],
  "required_fields": [],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": null,
    "numerator": null,
    "denominator": null,
    "aggregation_grain": null,
    "deduplication_rule": null
  },
  "filters": [],
  "joins": "No joins can be determined as the core information is missing.",
  "missing_or_ambiguous": "The provided context does not contain any information or metrics that could be used to directly estimate 'operational complexity cost' per marketplace. There are no fields that quantify operational complexity (e.g., manual process metrics, time spent, error rates) or associated costs.",
  "sql_skeleton": "/* Insufficient information to generate a SQL query. The context does not define or provide data for 'operational complexity cost'. */"
}


---

## 019. Build a SKU profitability report.

### Query

```text
Build a SKU profitability report.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": null,
  "rejected_sources": [],
  "require_tables": [],
  "required_fields": [],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": null,
    "numerator": null,
    "denominator": null,
    "aggregation_grain": null,
    "deduplication_rule": null
  },
  "filters": [],
  "joins": "No joins can be determined as the core information is missing.",
  "missing_or_ambiguous": "The provided context lacks any information or metrics related to SKU-level costs (e.g., Cost of Goods Sold, specific marketplace fees per SKU, operational costs per SKU). Without cost data, a true 'profitability' report cannot be generated, as profitability requires both revenue and cost components.",
  "sql_skeleton": "/* Insufficient information to generate a SQL query. The context does not define or provide data for SKU-level costs, which are essential for a profitability report. */"
}


---

## 020. Build an Average order value report per channel.

### Query

```text
Build an Average order value report per channel.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "This chunk is about an account data...",
    "primary` - scope_keys: ```json [ { \"business_key\":...",
    "This chunk describes nine active \"account_data_binding\" cards...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0024\" pack_index: 24...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0048\" pack_index: 48...",
    "bind platform_account.tanvi_fitness_private_limited.amazon_in.primary to table.zs_observe.amazon_settlement using client-level group_id and group_level_id scope filters.",
    "canonical_pack_0024",
    "canonical_pack_0061",
    "canonical_pack_0048",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0061\" pack_index: 61...",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "effective_cost_per_delivered_order",
    "metricimplementation",
    "metric implementation"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is consistently used for Mensa's sales and operational data, containing information about sales channels and orders, which are necessary for calculating Average Order Value per channel."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to group the Average Order Value by each sales channel, as specified in the report request. This column is logically present in a sales table."
    },
    {
      "field": "order_total_amount",
      "role": "Metric (Numerator)",
      "selected?": "Yes",
      "reason": "Required to sum the total monetary value of orders for the AOV calculation. This is inferred as a standard column for the total amount of a sales order in a sales table."
    },
    {
      "field": "order_id",
      "role": "Metric (Denominator)",
      "selected?": "Yes",
      "reason": "Required to count the number of distinct orders for the AOV calculation (total sales amount / number of orders). This is a common identifier in sales tables."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "order_status",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the AOV calculation (inferred from prior interactions)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SUM(order_total_amount) / COUNT(DISTINCT order_id)",
    "numerator": "SUM(order_total_amount)",
    "denominator": "COUNT(DISTINCT order_id)",
    "aggregation_grain": "sales_channel",
    "deduplication_rule": "COUNT(DISTINCT order_id) to ensure each unique order contributes once to the order count, and SUM(order_total_amount) aggregates the value for each distinct order."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, order value, order ID, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `order_total_amount` column within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables for calculating Average Order Value. The `sales_channel` and `order_id` columns are inferred from consistent usage in previous Mensa-scoped sales queries. Standard mandatory filters for Mensa's Increff operations (`is_active`, `order_status`, `transaction_type`) are also inferred from domain knowledge and prior interactions.",
  "sql_skeleton": "SELECT sales_channel, SUM(order_total_amount) / COUNT(DISTINCT order_id) AS average_order_value FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES' GROUP BY sales_channel ORDER BY average_order_value DESC"
}


---

## 021. Gross sales trend across all marketplaces.

### Query

```text
Gross sales trend across all marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### GRAPH_COMPLETION

{
  "selected_source": "table.zs_observe.increff_sales",
  "rejected_sources": [
    "This chunk is about an account data...",
    "primary` - scope_keys: ```json [ { \"business_key\":...",
    "--- source: \"canonical\" pack_id: \"canonical_pack_0024\" pack_index: 24...",
    "canonical_pack_0024",
    "canonical_pack_0061",
    "documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.",
    "scopespecificationnote",
    "scope specification note",
    "scopespecnote",
    "This chunk describes nine active \"account_data_binding\" cards...",
    "2026-05-24",
    "kb_pipeline.cleaned_v2",
    "business_flow_binding.mensa_brands.marketplace_settlement_to_bank.pending_bank"
  ],
  "require_tables": [
    {
      "field": "zs_observe.increff_sales",
      "role": "Primary Data Source Table",
      "selected?": "Yes",
      "reason": "This table is consistently used for Mensa's sales and operational data, containing sales channel information and order details necessary for a gross sales trend analysis."
    }
  ],
  "required_fields": [
    {
      "field": "sales_channel",
      "role": "Dimension",
      "selected?": "Yes",
      "reason": "Required to group sales by each marketplace, as specified in the report request. This column is logically present in a sales table."
    },
    {
      "field": "transaction_date",
      "role": "Dimension (Time for Trend)",
      "selected?": "Yes",
      "reason": "Required to analyze the 'trend' of gross sales over time. This is inferred as a standard date column in a sales transaction table."
    },
    {
      "field": "order_total_amount",
      "role": "Metric (Gross Sales)",
      "selected?": "Yes",
      "reason": "Required to calculate 'Gross sales'. This is inferred as the column representing the total monetary value of an order in a sales table."
    },
    {
      "field": "group_level_id",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Required for scoping the report to 'Mensa', as `group_level_id = 22` is the documented identifier for Mensa within operational tables like `increff_sales`."
    },
    {
      "field": "is_active",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations within Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "order_status",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`order_status = COMPLETED`) in Increff operations, implying relevance for valid order analysis in Mensa's `execution_constraint_set` (inferred from prior interactions)."
    },
    {
      "field": "transaction_type",
      "role": "Filter Column",
      "selected?": "Yes",
      "reason": "Explicitly listed as a mandatory filter (`transaction_type = SALES`) in Increff operations, ensuring only sales transactions are included in the gross sales calculation (inferred from prior interactions)."
    }
  ],
  "rejected_or_ambiguous_fields": [],
  "metric_logic": {
    "formula": "SUM(order_total_amount)",
    "numerator": "SUM(order_total_amount)",
    "denominator": null,
    "aggregation_grain": "(sales_channel, transaction_date)",
    "deduplication_rule": "SUM(order_total_amount) per unique combination of sales_channel and transaction_date to represent gross sales."
  },
  "filters": [
    "group_level_id = '22'",
    "is_active = true",
    "order_status = 'COMPLETED'",
    "transaction_type = 'SALES'"
  ],
  "joins": "No joins are required as all necessary information (sales channel, transaction date, gross sales amount, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_sales`.",
  "missing_or_ambiguous": "The explicit presence of `transaction_date` and `order_total_amount` columns within `table.zs_observe.increff_sales` is inferred based on domain knowledge of sales/operations tables for calculating sales trends. The `sales_channel` column is inferred from consistent usage in previous Mensa-scoped sales queries. Standard mandatory filters for Mensa's Increff operations (`is_active`, `order_status`, `transaction_type`) are also inferred from domain knowledge and prior interactions.",
  "sql_skeleton": "SELECT sales_channel, DATE_TRUNC('month', transaction_date) AS sales_month, SUM(order_total_amount) AS gross_sales FROM zs_observe.increff_sales WHERE group_level_id = '22' AND is_active = true AND order_status = 'COMPLETED' AND transaction_type = 'SALES' GROUP BY sales_channel, sales_month ORDER BY sales_channel, sales_month"
}


---

## 022. Return trend across all the marketplaces.

### Query

```text
Return trend across all the marketplaces.

Scope:
- tenant: Mensa

Answer for downstream SQL/query construction using only the provided context and explicit user input.

This is a one-pass handoff. Your task is to provide the strongest useful SQL-building context available from the retrieved context. 

Hard rules:
- Default to a single source table or single relationship path.
- Prefer the source that directly contains both the requested metric grain and requested grouping/filter dimensions.
- Do not consolidate multiple source tables unless the user explicitly asks for cross-source, all-source, or platform-wide consolidation.
- Do not treat table names, source systems, workflows, ingestion feeds, or platform-specific feeds as business dimension values.
- If a requested business dimension exists as a column in one source, prefer that column over inferring dimension values from multiple table names.
- If multiple tables may represent the same business event, do not UNION them unless the context provides a deduplication key and source precedence rule.

For dimensional mapping, grouping, or listing queries (No numeric metric):
- Set `metric_logic.formula` to describe the unique pairings or rows.
- Set `metric_logic.numerator` and `denominator` to null.
- Define `metric_logic.aggregation_grain` and `deduplication_rule` clearly.

Inference & Fallback Rule:
- If physical table names, column names, or tenant IDs are not explicitly stated in the context, you MUST NOT leave fields null or emit an empty payload. 
- You must infer the most logical parameters based on domain knowledge or historical context patterns. Treat your inferences as definitive selections, list them as "Selected", and explain the reasoning within the JSON.

Response Format:
Return a single answer string containing one valid JSON object.
Do not wrap it in Markdown or code fences.
The JSON object must be emitted as plain text, not as a nested object under a content key.

The JSON object must strictly match this structural schema:
{
  "selected_source": "string or null",
  "rejected_sources": ["array of strings"],
  "require_tables":[
        {
      "field": "string (table name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
    }
  ]
  "required_fields": [
    {
      "field": "string (column name)",
      "role": "string (e.g., Channel Identifier, Filter Column, Metric)",
      "selected?": "Yes/No",
      "reason": "string explaining why this field belongs in the query"
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
  "filters": ["array of strings showing exact WHERE clause conditions"],
  "joins": "string explaining join logic or stating why no joins are needed",
  "missing_or_ambiguous": "string ('None' if fallback inference was used successfully)",
  "sql_skeleton": "string containing a valid SQL query template utilizing the selected fields and filters"
}
```

### Errors

```json
{
  "GRAPH_COMPLETION": "500 Internal Server Error: {\"error\":\"Internal server error\",\"detail\":\"<failed_attempts>\\n\\n<generation number=\\\"1\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Field required [type=missing, input_value={'selected_source': 'tabl..._channel, return_month\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/missing\\n</exception>\\n<completion>\\n    ModelResponse(id='fgMWao3FEpKAzvgP4LHGiAk', created=1779827581, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"selected_source\\\": \\\"table.zs_observe.increff_returns\\\",\\\\n  \\\"rejected_sources\\\": [\\\\n    \\\"use only with marketplace-specific semantics.\\\",\\\\n    \\\"marketplace-specific semantics\\\",\\\\n    \\\"documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.\\\",\\\\n    \\\"scopespecificationnote\\\",\\\\n    \\\"scope specification note\\\",\\\\n    \\\"scopespecnote\\\",\\\\n    \\\"This chunk is about `business_scope_set` definitions for... [scope, active, set]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0109\\\\\\\\\\\" pack_index: 109... [json, confidence=`unknown, outgoing]\\\",\\\\n    \\\"This chunk is about account data binding... [binding, account, data]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0027\\\\\\\\\\\" pack_index: 27... [json, raw/cleaned_v2/clients/mensa_business.json, active]\\\",\\\\n    \\\"This chunk is about column definitions for... [column, each, settlement]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0332\\\\\\\\\\\" pack_index: 332... [confidence=`unknown, json, raw/cleaned_v2/marketplace/myntra_marketplace.md]\\\",\\\\n    \\\"This chunk is about two business flow... [marketplace, binding, flow]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0081\\\\\\\\\\\" pack_index: 81... [confidence=`unknown, outgoing, uses_account_data_binding]\\\",\\\\n    \\\"This chunk is about eight active \\\\\\\\\\\"account_data_binding\\\\\\\\\\\"... [confidence, data, mapping]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0061\\\\\\\\\\\" pack_index: 61... [json, client, raw/cleaned_v2/clients/volans_epic_llc.json]\\\",\\\\n    \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0041\\\\\\\\\\\" pack_index: 41... [json, group_id, group_level_id]\\\",\\\\n    \\\"marketplace transactions extraction\\\"\\\\n  ],\\\\n  \\\"require_tables\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"zs_observe.increff_returns\\\",\\\\n      \\\"role\\\": \\\"Primary Data Source Table\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"This table is explicitly described as a \\\\'Cross-channel returns log (ops view)\\\\' for Mensa\\\\'s Increff operations and contains sales channel information, making it suitable for analyzing return trends across marketplaces.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"required_fields\\\": [\\\\n    {\\\\n      \\\"field\\\": \\\"sales_channel\\\",\\\\n      \\\"role\\\": \\\"Dimension (Marketplace Identifier)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required to group return data by marketplace and provide a trend \\\\'across all marketplaces\\\\'.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"return_date\\\",\\\\n      \\\"role\\\": \\\"Dimension (Time for Trend)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required to establish the \\\\'trend\\\\' over time. This is inferred as a standard date column in a returns log.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"return_id\\\",\\\\n      \\\"role\\\": \\\"Metric (Return Volume)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Used to count the number of unique returns, providing the metric for the \\\\'return trend\\\\'. This is inferred as the unique identifier for return transactions.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"group_level_id\\\",\\\\n      \\\"role\\\": \\\"Filter Column (Tenant Scope)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa\\\\', as `group_level_id = 22` is the documented identifier for Mensa within operational tables.\\\"\\\\n    },\\\\n    {\\\\n      \\\"field\\\": \\\"is_active\\\",\\\\n      \\\"role\\\": \\\"Filter Column (Status)\\\",\\\\n      \\\"selected?\\\": \\\"Yes\\\",\\\\n      \\\"reason\\\": \\\"Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations.\\\"\\\\n    }\\\\n  ],\\\\n  \\\"rejected_or_ambiguous_fields\\\": [],\\\\n  \\\"metric_logic\\\": {\\\\n    \\\"formula\\\": \\\"COUNT(DISTINCT return_id)\\\",\\\\n    \\\"numerator\\\": \\\"COUNT(DISTINCT return_id)\\\",\\\\n    \\\"denominator\\\": null,\\\\n    \\\"aggregation_grain\\\": \\\"(sales_channel, return_date_truncated_to_month)\\\",\\\\n    \\\"deduplication_rule\\\": \\\"COUNT(DISTINCT return_id) to ensure each unique return transaction is counted once for volume calculation.\\\"\\\\n  },\\\\n  \\\"filters\\\": [\\\\n    \\\"group_level_id = \\\\'22\\\\'\\\",\\\\n    \\\"is_active = true\\\",\\\\n    \\\"sales_channel IN (\\\\'Amazon\\\\', \\\\'Flipkart\\\\', \\\\'Myntra\\\\', \\\\'Meesho\\\\', \\\\'Nykaa\\\\', \\\\'Jiomart\\\\', \\\\'Snapdeal\\\\', \\\\'Tatacliq\\\\', \\\\'Healthkart\\\\', \\\\'Shopify\\\\', \\\\'Website\\\\')\\\"\\\\n  ],\\\\n  \\\"joins\\\": \\\"No joins are required as all necessary information (marketplace, return ID, return date, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_returns`.\\\",\\\\n  \\\"missing_or_ambiguous\\\": \\\"The explicit presence of `return_date` and `return_id` columns within `table.zs_observe.increff_returns` is inferred based on domain knowledge of return logs. The `sales_channel` column is inferred from consistent usage in previous Mensa-scoped sales/returns queries. The list of marketplace channels used in the filter is consistently inferred from previous Mensa-specific queries.\\\",\\\\n  \\\"sql_skeleton\\\": \\\"SELECT sales_channel, DATE_TRUNC(\\\\'month\\\\', return_date) AS return_month, COUNT(DISTINCT return_id) AS total_returns FROM zs_observe.increff_returns WHERE group_level_id = \\\\'22\\\\' AND is_active = true AND sales_channel IN (\\\\'Amazon\\\\', \\\\'Flipkart\\\\', \\\\'Myntra\\\\', \\\\'Meesho\\\\', \\\\'Nykaa\\\\', \\\\'Jiomart\\\\', \\\\'Snapdeal\\\\', \\\\'Tatacliq\\\\', \\\\'Healthkart\\\\', \\\\'Shopify\\\\', \\\\'Website\\\\') GROUP BY sales_channel, return_month ORDER BY sales_channel, return_month\\\"\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=2163, prompt_tokens=80753, total_tokens=82916, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=742, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=79777), cache_read_input_tokens=79777), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n<generation number=\\\"2\\\">\\n<exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'tabl..._channel, return_month\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</exception>\\n<completion>\\n    ModelResponse(id='iwMWaoSOHfuB48APj_yVgAo', created=1779827594, model='gemini-2.5-flash', object='chat.completion', system_fingerprint=None, choices=[Choices(finish_reason='stop', index=0, message=Message(content='{\\\\n  \\\"content\\\": {\\\\n    \\\"selected_source\\\": \\\"table.zs_observe.increff_returns\\\",\\\\n    \\\"rejected_sources\\\": [\\\\n      \\\"use only with marketplace-specific semantics.\\\",\\\\n      \\\"marketplace-specific semantics\\\",\\\\n      \\\"documented nykaa fashion dataset scope value; keep as column/filter caveat only, not tenant/group/account binding.\\\",\\\\n      \\\"scopespecificationnote\\\",\\\\n      \\\"scope specification note\\\",\\\\n      \\\"scopespecnote\\\",\\\\n      \\\"This chunk is about `business_scope_set` definitions for... [scope, active, set]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0109\\\\\\\\\\\" pack_index: 109... [json, confidence=`unknown, outgoing]\\\",\\\\n      \\\"This chunk is about account data binding... [binding, account, data]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0027\\\\\\\\\\\" pack_index: 27... [json, raw/cleaned_v2/clients/mensa_business.json, active]\\\",\\\\n      \\\"This chunk is about column definitions for... [column, each, settlement]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0332\\\\\\\\\\\" pack_index: 332... [confidence=`unknown, json, raw/cleaned_v2/marketplace/myntra_marketplace.md]\\\",\\\\n      \\\"This chunk is about two business flow... [marketplace, binding, flow]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0081\\\\\\\\\\\" pack_index: 81... [confidence=`unknown, outgoing, uses_account_data_binding]\\\",\\\\n      \\\"This chunk is about eight active \\\\\\\\\\\"account_data_binding\\\\\\\\\\\"... [confidence, data, mapping]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0061\\\\\\\\\\\" pack_index: 61... [json, client, raw/cleaned_v2/clients/volans_epic_llc.json]\\\",\\\\n      \\\"--- source: \\\\\\\\\\\"canonical\\\\\\\\\\\" pack_id: \\\\\\\\\\\"canonical_pack_0041\\\\\\\\\\\" pack_index: 41... [json, group_id, group_level_id]\\\",\\\\n      \\\"marketplace transactions extraction\\\"\\\\n    ],\\\\n    \\\"require_tables\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"zs_observe.increff_returns\\\",\\\\n        \\\"role\\\": \\\"Primary Data Source Table\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"This table is explicitly described as a \\\\'Cross-channel returns log (ops view)\\\\' for Mensa\\\\'s Increff operations and contains sales channel information, making it suitable for analyzing return trends across marketplaces.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"required_fields\\\": [\\\\n      {\\\\n        \\\"field\\\": \\\"sales_channel\\\",\\\\n        \\\"role\\\": \\\"Dimension (Marketplace Identifier)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required to group return data by marketplace and provide a trend \\\\'across all marketplaces\\\\'.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"return_date\\\",\\\\n        \\\"role\\\": \\\"Dimension (Time for Trend)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required to establish the \\\\'trend\\\\' over time. This is inferred as a standard date column in a returns log.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"return_id\\\",\\\\n        \\\"role\\\": \\\"Metric (Return Volume)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Used to count the number of unique returns, providing the metric for the \\\\'return trend\\\\'. This is inferred as the unique identifier for return transactions.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"group_level_id\\\",\\\\n        \\\"role\\\": \\\"Filter Column (Tenant Scope)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Required for scoping the report to \\\\'Mensa\\\\', as `group_level_id = 22` is the documented identifier for Mensa within operational tables.\\\"\\\\n      },\\\\n      {\\\\n        \\\"field\\\": \\\"is_active\\\",\\\\n        \\\"role\\\": \\\"Filter Column (Status)\\\",\\\\n        \\\"selected?\\\": \\\"Yes\\\",\\\\n        \\\"reason\\\": \\\"Explicitly listed as a mandatory filter (`is_active = true`) for data validity in Increff operations.\\\"\\\\n      }\\\\n    ],\\\\n    \\\"rejected_or_ambiguous_fields\\\": [],\\\\n    \\\"metric_logic\\\": {\\\\n      \\\"formula\\\": \\\"COUNT(DISTINCT return_id)\\\",\\\\n      \\\"numerator\\\": \\\"COUNT(DISTINCT return_id)\\\",\\\\n      \\\"denominator\\\": null,\\\\n      \\\"aggregation_grain\\\": \\\"(sales_channel, return_date_truncated_to_month)\\\",\\\\n      \\\"deduplication_rule\\\": \\\"COUNT(DISTINCT return_id) to ensure each unique return transaction is counted once for volume calculation.\\\"\\\\n    },\\\\n    \\\"filters\\\": [\\\\n      \\\"group_level_id = \\\\'22\\\\'\\\",\\\\n      \\\"is_active = true\\\",\\\\n      \\\"sales_channel IN (\\\\'Amazon\\\\', \\\\'Flipkart\\\\', \\\\'Myntra\\\\', \\\\'Meesho\\\\', \\\\'Nykaa\\\\', \\\\'Jiomart\\\\', \\\\'Snapdeal\\\\', \\\\'Tatacliq\\\\', \\\\'Healthkart\\\\', \\\\'Shopify\\\\', \\\\'Website\\\\')\\\"\\\\n    ],\\\\n    \\\"joins\\\": \\\"No joins are required as all necessary information (marketplace, return ID, return date, and tenant filters) is inferred to exist within the single selected table `zs_observe.increff_returns`.\\\",\\\\n    \\\"missing_or_ambiguous\\\": \\\"The explicit presence of `return_date` and `return_id` columns within `table.zs_observe.increff_returns` is inferred based on domain knowledge of return logs. The `sales_channel` column is inferred from consistent usage in previous Mensa-scoped sales/returns queries. The list of marketplace channels used in the filter is consistently inferred from previous Mensa-specific queries.\\\",\\\\n    \\\"sql_skeleton\\\": \\\"SELECT sales_channel, DATE_TRUNC(\\\\'month\\\\', return_date) AS return_month, COUNT(DISTINCT return_id) AS total_returns FROM zs_observe.increff_returns WHERE group_level_id = \\\\'22\\\\' AND is_active = true AND sales_channel IN (\\\\'Amazon\\\\', \\\\'Flipkart\\\\', \\\\'Myntra\\\\', \\\\'Meesho\\\\', \\\\'Nykaa\\\\', \\\\'Jiomart\\\\', \\\\'Snapdeal\\\\', \\\\'Tatacliq\\\\', \\\\'Healthkart\\\\', \\\\'Shopify\\\\', \\\\'Website\\\\') GROUP BY sales_channel, return_month ORDER BY sales_channel, return_month\\\"\\\\n  }\\\\n}', role='assistant', tool_calls=None, function_call=None, images=[], thinking_blocks=[], provider_specific_fields=None))], usage=Usage(completion_tokens=3644, prompt_tokens=164898, total_tokens=168542, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=None, audio_tokens=0, reasoning_tokens=793, rejected_prediction_tokens=None), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=160571), cache_read_input_tokens=80794), vertex_ai_grounding_metadata=[], vertex_ai_url_context_metadata=[], vertex_ai_safety_results=[], vertex_ai_citation_metadata=[])\\n</completion>\\n</generation>\\n\\n</failed_attempts>\\n\\n<last_exception>\\n    1 validation error for Response\\ncontent\\n  Input should be a valid string [type=string_type, input_value={'selected_source': 'tabl..._channel, return_month\\\"}, input_type=dict]\\n    For further information visit https://errors.pydantic.dev/2.13/v/string_type\\n</last_exception>\"}"
}
```


---
