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
