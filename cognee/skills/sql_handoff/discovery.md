# SQL Handoff Discovery Skill

Find canonical context for the user question using the raw intent as routing guidance. Return compact evidence only, not final SQL and not final intent.

Question:
{{query}}

{{scope}}

Raw Intent JSON:
{{raw_intent_json}}

Use raw intent only to decide what evidence to retrieve:
- For `metric` or `report_generation`, look for physical runtime tables, columns, metric formulas, filters, grain, query patterns, and deduplication rules.
- For `business_process` or `workflow`, look for business_flow_binding, business_process, workflow_step, state_transition, account/platform bindings, and any physical tables attached to those flows.
- For `source_mapping` or `metadata_inventory`, look for account_data_binding, platform_account, business flow, source binding, and table cards that prove the mapping.
- For `reconciliation`, look for settlement, OMS/order, return/reverse, payment, remittance, join-key, and source-precedence evidence.
- For `logistics`, look for courier/shipment/AWB/remittance tables, columns, query patterns, and relationship cards.

Rules:
- Do not answer the user question.
- Do not produce SQL.
- Do not refine or rewrite the raw intent.
- Canonical metadata is evidence only unless a later stage marks this as a metadata inventory handoff.
- Prefer compact evidence with source ids, table names, columns, filters, and relationship paths.
