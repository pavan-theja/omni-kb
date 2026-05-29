## 004. Generate a courier-wise channel mapping report.

### Timing

- started_at: `2026-05-27T07:42:19+00:00`
- duration_seconds: `95.111`
- validation_ok: `False`

### Result

# Cognee SQL Handoff

- query: `Generate a courier-wise channel mapping report.`
- validation_ok: `False`
- duration_seconds: `95.111`

## Validation

```json
{
  "errors": [
    "sql_skeleton has no FROM clause and is not a commented partial template"
  ],
  "ok": false,
  "warnings": []
}
```

## SQL Handoff

```json
{
  "filters": [
    "zs_observe.increff_returns.group_level_id = 22",
    "zs_observe.increff_returns.is_active = true",
    "zs_observe.increff_returns.order_status = 'COMPLETED'",
    "zs_observe.increff_returns.transaction_type = 'RETURN'"
  ],
  "joins": "No joins are needed as all required dimensions and filters are contained within the single selected table zs_observe.increff_returns.",
  "metric_logic": {
    "aggregation_grain": "forward_transporter, fulfilment_channel",
    "deduplication_rule": "DISTINCT forward_transporter, fulfilment_channel",
    "denominator": null,
    "formula": "LIST(DISTINCT forward_transporter, fulfilment_channel)",
    "numerator": null
  },
  "missing_or_ambiguous": "None.",
  "rejected_or_ambiguous_fields": [],
  "rejected_sources": [],
  "require_tables": [
    {
      "field": "zs_observe.increff_returns",
      "reason": "This table was selected by the Source Resolver as it explicitly contains both 'fulfilment_channel' (channel) and 'forward_transporter' (courier) which directly map to the requested dimensions for Mensa Brands.",
      "role": "Primary Source",
      "selected?": "Yes"
    },
    {
      "field": "table.zs_observe.increff_sales",
      "reason": "While zs_observe.increff_sales contains 'fulfilment_channel', the context describes this column as 'Courier/logistics partner used', meaning it represents the courier, not a distinct channel dimension needed for a 'courier-wise channel mapping report'.",
      "role": "Risky Candidate",
      "selected?": "No"
    },
    {
      "field": "account_data_binding.mensa.increff_wms.primary.increff_returns",
      "reason": "Confirms Mensa Brands uses Increff and provides the tenant filter (group_level_id = 22) for zs_observe.increff_returns.",
      "role": "Supporting Metadata",
      "selected?": "No"
    },
    {
      "field": "execution_constraint_set.increff.operations_manifest_refactored_constraints",
      "reason": "Provides general operational filters and constraints for Increff data, including Mensa-specific scope ('group_level_id = 22' and 'is_active = true').",
      "role": "Supporting Metadata",
      "selected?": "No"
    }
  ],
  "required_fields": [
    {
      "field": "fulfilment_channel",
      "reason": "Requested channel dimension, explicitly available in zs_observe.increff_returns.",
      "role": "Dimension",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "forward_transporter",
      "reason": "Maps to the requested 'courier_partner' dimension as per column description 'Original outbound courier' within zs_observe.increff_returns.",
      "role": "Dimension",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "group_level_id",
      "reason": "Tenant filter for Mensa Brands (value 22), as inferred from the intent and grounded by execution constraints and account data binding.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "is_active",
      "reason": "Standard operational filter for active records, as inferred from the intent and grounded by execution constraints.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "order_status",
      "reason": "Standard filter ('order_status = 'COMPLETED' for relevant sales records) as per Increff operations constraints for completeness, applied by analogy to returns data to ensure relevant operational status.",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    },
    {
      "field": "transaction_type",
      "reason": "Standard filter ('transaction_type = 'RETURN') for relevant return records, inferred based on the table name and the type of report being generated (courier-wise channel mapping for returns).",
      "role": "Filter Column",
      "selected?": "Yes",
      "table": "zs_observe.increff_returns"
    }
  ],
  "selected_source": "zs_observe.increff_returns",
  "sql_skeleton": "SELECT DISTINCT\n    fulfilment_channel,\n    forward_transporter\nFROM\n    zs_observe.increff_returns\nWHERE\n    group_level_id = 22 AND\n    is_active = true AND\n    order_status = 'COMPLETED' AND\n    transaction_type = 'RETURN'\nORDER BY\n    fulfilment_channel, forward_transporter;"
}
```
