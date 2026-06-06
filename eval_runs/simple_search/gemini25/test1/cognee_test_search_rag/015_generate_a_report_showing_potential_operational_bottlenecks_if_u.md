## 015. Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

### Query

```text
Generate a report showing potential operational bottlenecks if Unicommerce becomes unavailable.

Scope:
- tenant: Mensa

Answer for SQL query construction. Return concise, source-grounded details:
- relevant canonical ids and entity names
- source tables with schema/table names
- required columns, including join keys, filter columns, date columns, and amount columns
- relationships or join paths between tables/accounts/platforms/workflows
- metrics or formulas needed, including aggregation grain and deduplication rules
- tenant/group/platform/account filters that must appear in SQL
- assumptions, missing information, and any ambiguity
If useful, include a SQL skeleton, but do not invent columns or tables that are not in context.
```

### RAG_COMPLETION

{
    "relevant_canonical_ids": [
        "table.zs_observe.unicommerce",
        "column.zs_observe.unicommerce.sales_channel",
        "column.zs_observe.unicommerce.group_level_id",
        "column.zs_observe.unicommerce.is_active",
        "business_flow_binding.bracheium_brand_technologies.marketplace_to_operations"
    ],
    "entity_names": {
        "tenant": "Mensa Brands (Bracheium Brand Technologies entity)",
        "oms_system": "Unicommerce",
        "dependent_marketplaces_from_flow": [
            "Amazon",
            "Flipkart",
            "Myntra",
            "Meesho",
            "Nykaa",
            "Jiomart",
            "Snapdeal",
            "Tatacliq"
        ]
    },
    "source_tables": [
        {
            "schema_name": "zs_observe",
            "table_name": "unicommerce",
            "description": "Unified transaction ledger in Unicommerce OMS for sales, returns, and cancellations, which directly handles sales channel data."
        }
    ],
    "required_columns": [
        {
            "column_name": "sales_channel",
            "role": "channel identifier",
            "notes": "To identify specific channels/marketplaces whose operations depend on Unicommerce."
        },
        {
            "column_name": "group_level_id",
            "role": "filter column",
            "notes": "Used to filter data for the specific Mensa tenant entity (Bracheium Brand Technologies)."
        },
        {
            "column_name": "is_active",
            "role": "filter column",
            "notes": "Mandatory filter for active records, where available."
        }
    ],
    "relationships_join_paths": "The relationship is conceptual, derived from the 'business_flow_binding.bracheium_brand_technologies.marketplace_to_operations' which indicates that data from various marketplaces feed into an operations flow that includes Unicommerce as an 'oms_operations_source'.",
    "metrics_formulas": "Not applicable; this query identifies dependencies rather than calculates metrics related to bottlenecks.",
    "tenant_group_platform_account_filters": [
        {
            "type": "tenant",
            "name": "Mensa Brands (Unicommerce for Bracheium Brand Technologies)",
            "column": "group_level_id",
            "value": "29",
            "operator": "=",
            "tables": [
                "zs_observe.unicommerce"
            ]
        },
        {
            "type": "record_status",
            "column": "is_active",
            "value": "true",
            "operator": "=",
            "tables": [
                "zs_observe.unicommerce"
            ]
        }
    ],
    "assumptions_missing_information_ambiguity": "Unicommerce being unavailable implies disruption to all channels whose sales, returns, and cancellations data are processed through it, as indicated by its 'sales_returns_cancellations' and 'sales_order_report' semantics. The 'sales_channel' column in `zs_observe.unicommerce` is assumed to identify these directly dependent channels. The `business_flow_binding.bracheium_brand_technologies.marketplace_to_operations` explicitly lists Amazon, Flipkart, Myntra, Meesho, Nykaa, Jiomart, Snapdeal, and Tatacliq as 'marketplace_order_source' accounts feeding into an operational flow where Unicommerce acts as an 'oms_operations_source'. Even though Unicommerce's role in this specific flow is marked as 'required: false', its unavailability would still pose significant operational bottlenecks for processing order data, returns, and cancellations for these marketplaces. The `group_level_id = 29` is used for Mensa's Unicommerce data based on prior context.",
    "sql_skeleton": "SELECT DISTINCT 'Unicommerce' AS oms_system, sales_channel AS affected_channel FROM zs_observe.unicommerce WHERE group_level_id = 29 AND is_active = true UNION ALL SELECT 'Unicommerce' AS oms_system, 'Amazon' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Flipkart' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Myntra' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Meesho' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Nykaa' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Jiomart' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Snapdeal' AS affected_channel UNION ALL SELECT 'Unicommerce' AS oms_system, 'Tatacliq' AS affected_channel ORDER BY affected_channel;"
}
