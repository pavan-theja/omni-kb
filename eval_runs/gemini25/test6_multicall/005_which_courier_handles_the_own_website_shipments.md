## 005. Which courier handles the own website shipments?

### Timing

- started_at: `2026-05-27T07:43:54+00:00`
- duration_seconds: `65.693`
- validation_ok: `False`

### Error

```text
source_resolution did not return a JSON object: ['{"selected_sources":[],"candidates":[{"field":"table.zs_observe.increff_sales","role":"Risky Candidate","selected?":"No","reason":"While zs_observe.increff_sales contains \'fulfilment_channel\' and \'group_level_id\', the \'fulfilment_channel\' is described as a \'Courier/logistics partner used\', not a sales channel that could be filtered for \'Own Website\' shipments. Thus, it lacks the explicit \'sales_channel\' dimension."},{"field":"table.zs_observe.increff_returns","role":"Risky Candidate","selected?":"No","reason":"zs_observe.increff_returns contains \'fulfilment_channel\' (described as \'Fulfilment partner\') and \'forward_transporter\' (described as \'Original outbound courier\'), but neither serves as the \'sales_channel\' dimension required to filter for \'Own Website\' shipments. It lacks the explicit \'sales_channel\' dimension."}],"supporting_metadata":[{"field":"execution_constraint_set.increff.operations_manifest_refactored_constraints","role":"Supporting Metadata","selected?":"No","reason":"Provides general operational filters like \'is_active = true\' and \'group_level_id = 22\' for Mensa Brands, which are relevant if a suitable source for the main query were found."}},"rejected_sources":[],"missing_or_risky":"The critical blocking gap is the absence of a distinct physical column to represent the \'sales_channel\' that can be explicitly filtered for \'Own Website\' shipments. The existing \'fulfilment_channel\' in both Increff tables is defined as a courier/fulfilment partner, not a sales channel.","reason":"No direct or suitable candidate physical table was found that contains a \'sales_channel\' column which can be filtered for \'Own Website\'. The \'fulfilment_channel\' columns in the available Increff tables explicitly represent couriers or fulfilment partners, not sales channels."}']
```
