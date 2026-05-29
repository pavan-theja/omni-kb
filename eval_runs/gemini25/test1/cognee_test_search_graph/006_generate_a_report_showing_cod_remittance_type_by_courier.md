## 006. Generate a report showing COD remittance type by courier.

### Query

```text
Generate a report showing COD remittance type by courier.

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

### GRAPH_COMPLETION

The provided context does not contain information about 'COD remittance type' or specific columns for 'COD remitted amount' in the available tables (`increff_sales`, `dtdc_invoice`, `myntra_oms`). While `myntra_oms.postpaid_amount` is related to COD, it is not explicitly a remitted amount, nor is a 'remittance type' column present.
