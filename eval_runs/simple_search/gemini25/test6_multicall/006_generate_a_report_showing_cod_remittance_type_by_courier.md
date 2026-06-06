## 006. Generate a report showing COD remittance type by courier.

### Timing

- started_at: `2026-05-27T07:45:00+00:00`
- duration_seconds: `56.053`
- validation_ok: `False`

### Error

```text
intent did not return a JSON object: ['{"grain":"cod_remittance_type_by_courier","metric_or_status_logic":"list distinct COD remittance types for each courier","dimensions":["courier_partner","remittance_type"],"filters":[{"column":"group_level_id","value":22,"operator":"=","reason":"Tenant filter for Mensa Brands."},{"column":"is_active","value":true,"operator":"=","reason":"Standard operational filter from logistics query patterns."},{"column":"payment_mode","value":"COD","operator":"=","reason":"Explicit filter for Cash on Delivery transactions."자를}],"scope":{"tenant":"Mensa Brands"},"source_mode":"single_source","must_enumerate_sources":false,"table_limit":1,"reason":"The `zs_observe.shiprocket_settlement` table, explicitly mentioned in `query_pattern.logistics.cod_expected_vs_remitted`, contains all necessary dimensions (courier_partner, status/remittance_type) and filters (payment_mode = \'COD\', group_level_id for Mensa Brands) to address the question within a single source."}']
```
