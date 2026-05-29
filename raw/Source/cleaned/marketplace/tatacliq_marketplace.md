# TataCliq Marketplace Clean Markdown — V9 Manifest-Refactored

```yaml
document_metadata:
  document_id: tatacliq_marketplace_clean_md_v9_manifest_refactored
  vendor: TataCliq
  source_docx: /mnt/data/TataCliq Recon KB.docx
  source_md_previous: /mnt/data/tatacliq_marketplace_clean_md_v8_unified_edges.md
  cleanup_manifest: /mnt/data/marketplace_cleanup_manifest_consolidated_v2.md
  generated_on: '2026-05-22'
  scope: marketplace_specific_clean_markdown_for_deterministic_parser
  marketplace_only: true
  refactor_policy: source-backed, correctly typed, executable, and connected to the right semantic neighborhood
  forbidden_card_types:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  removed_card_types:
  - state_transition
  - process_variant
  quality_summary:
    candidate_cards: 263
    candidate_edges: 597
    source_evidence_count: 74
    sql_patterns: 24
    review_items: 5
    open_reviews: 5
    missing_edge_references: 0
    dangling_sql_refs: 0
    missing_evidence_refs: 0
    deleted_card_references: 0
    isolated_cards: 0
    lazy_workflow_steps: 0
    placeholder_metric_formulas: 0
    unsupported_metric_implementations: 0
    process_variants_review_required: 0
    state_transitions_without_state_column: 0
    unresolved_benchmark_reviews_without_reason: 0
    hard_threshold_benchmarks_without_rule: 0
    forbidden_scope_cards_from_scope_ids: 0
    raw_source_sha256: 410ad0a3332ccb4bb39d2c745e2ac486f744af64622dbbbc3db74255d5a02d79
    raw_source_line_count: 1235
```

## 0. Parser Instructions

This V9 refactor applies the consolidated marketplace cleanup manifest to the TataCliq marketplace source. It keeps TataCliq marketplace semantics, table schemas, query SQL, reconciliation logic, rules, caveats, and the raw DOCX capture, while removing or recasting lazy/non-executable cards from the prior V8 source.

Critical rules:

- Treat `group_level_id`, `group_id`, `tenant_id`, seller identifiers, GSTINs, slave/warehouse codes, and similar values as columns, filters, caveats, or documented scope identifiers only.
- Use `order_id` for OMS-settlement joins. Do not model `document_number = parent_id` as a working relationship because the source states 0% coverage.
- Preserve TataCliq settlement sign semantics. Use `ABS(charged_amount)` only for source-backed GMV/payout calculations.
- Use only SQL-backed metric implementations. Prose-only formulas have been recast as rules, formula templates, or review items.
- Return flow is a standalone business process, not a process variant. TSHIP/HD, TSHIP/ED, PREPAID/POSTPAID, GSTIN/state, and brand labels are value profiles or filters, not process variants.
- `state_transition` cards are intentionally omitted because the source describes lifecycle prose and status values, not state-column transitions.

## 1. Applied Manifest Refactor Decisions


```yaml
refactor_decision:
  source_card_or_pattern: metric.return_flow / metric_impl.tatacliq.return_flow
  action: recast
  resolution: Return flow is a business_process with workflow_steps; removed metric and non-SQL implementation.
```


```yaml
refactor_decision:
  source_card_or_pattern: metric.oms_settlement_join / metric_impl.tatacliq.oms_settlement_join
  action: recast
  resolution: Join is relationship + query_pattern, not a metric.
```


```yaml
refactor_decision:
  source_card_or_pattern: metric.oms_settlement_reconciliation / metric.return_oms_settlement_match
  action: recast
  resolution: Reconciliation semantics are reconciliation_profile/query_pattern, not metrics.
```


```yaml
refactor_decision:
  source_card_or_pattern: metric.why_settlement_has_more_orders_than_oms
  action: recast
  resolution: Documented caveat/rule about data coverage, not metric implementation.
```


```yaml
refactor_decision:
  source_card_or_pattern: process_variant.tatacliq.return_flow
  action: remove
  resolution: Return flow is modeled as its own business_process; fulfilment/order/geography labels remain value profiles/rules.
```


```yaml
refactor_decision:
  source_card_or_pattern: 22 source-derived state_transition cards
  action: remove
  resolution: Source gives lifecycle prose and status values, not state-column transitions between values.
```


```yaml
refactor_decision:
  source_card_or_pattern: non-SQL metric implementations for GST/TCS/TDS prose/payout prose
  action: recast_or_remove
  resolution: Only executable SQL-backed metric_implementation cards are retained; prose becomes rule, formula_template, or
    review_item.
```


```yaml
refactor_decision:
  source_card_or_pattern: artificial mismatch categories for commission/timing/status where no detection logic exists
  action: remove
  resolution: Mismatch categories retained only where source SQL yields missing/variance diagnostics.
```


## 2. Source Evidence Registry


```yaml
source_evidence:
  id: ev.tatacliq.overview.background
  source_section: 1.1 Background
  source_line_start: 6
  source_line_end: 18
  evidence_type: prose
  supported_semantics:
  - TataCliq marketplace identity, operator Tata Unistore Limited, curated/phygital positioning, GSTIN/PAN context
  unsupported_semantics:
  - Does not define a financial formula or reconciliation process
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.brands.dataset
  source_section: 1.2 Brands in Dataset
  source_line_start: 19
  source_line_end: 29
  evidence_type: table
  supported_semantics:
  - Brand values, categories, source states, average selling price guidance, HSN code counts
  unsupported_semantics:
  - Does not define a process variant by brand
  allowed_card_types:
  - value_profile
  - column
  - query_pattern
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.warehouse.gstin
  source_section: 1.3 Multi-Warehouse GSTIN Setup
  source_line_start: 30
  source_line_end: 42
  evidence_type: table
  supported_semantics:
  - Seller GSTIN to state/warehouse/slave code mapping; slave_id/slave encoding
  unsupported_semantics:
  - Does not create warehouse/logistics account cards
  allowed_card_types:
  - value_profile
  - column
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.ecom.gstin
  source_section: 1.4 TataCliq E-Commerce GSTINs (33 States/UTs)
  source_line_start: 43
  source_line_end: 51
  evidence_type: prose
  supported_semantics:
  - TataCliq e-commerce GSTIN pattern and place_of_supply selection
  unsupported_semantics:
  - Does not create statutory filing cards
  allowed_card_types:
  - value_profile
  - column
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.fee.structure
  source_section: 2.1 Fee Structure (Validated by Data)
  source_line_start: 54
  source_line_end: 71
  evidence_type: table
  supported_semantics:
  - Referral fee, commission GST, gross commission, TDS, zero shipping/COD/PG fee semantics
  unsupported_semantics:
  - Does not define separate logistics/payment-gateway fee cards
  allowed_card_types:
  - metric
  - rule
  - value_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.payout.calculation
  source_section: 2.2 Payout Calculation
  source_line_start: 72
  source_line_end: 86
  evidence_type: metric_definition
  supported_semantics:
  - Net Settled formula, commission + GST + TDS deduction, example payout ratio
  unsupported_semantics:
  - Does not prove bank reconciliation or ERP posting
  allowed_card_types:
  - formula_template
  - metric
  - metric_implementation
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.fulfilment.tship
  source_section: 2.3 Fulfilment Model — TSHIP
  source_line_start: 87
  source_line_end: 97
  evidence_type: table
  supported_semantics:
  - TSHIP/HD and TSHIP/ED fulfilment channel meanings and no separate fulfilment fee
  unsupported_semantics:
  - Does not create external logistics account cards or process variants by channel
  allowed_card_types:
  - value_profile
  - rule
  - workflow_step
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.order.types
  source_section: 2.4 Order Types
  source_line_start: 98
  source_line_end: 107
  evidence_type: table
  supported_semantics:
  - PREPAID and POSTPAID order_type meanings
  unsupported_semantics:
  - Does not create payment gateway account cards
  allowed_card_types:
  - value_profile
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.lifecycle.forward
  source_section: 3.1 Forward Sale Flow
  source_line_start: 110
  source_line_end: 134
  evidence_type: prose
  supported_semantics:
  - Forward sale lifecycle with OMS invoice, destination e-commerce GSTIN, slave_id, weekly settlement, settlement sign convention
  unsupported_semantics:
  - Does not justify generic one-line workflow steps or bank account cards
  allowed_card_types:
  - business_process
  - workflow_step
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.lifecycle.return
  source_section: 3.2 Return Flow
  source_line_start: 135
  source_line_end: 155
  evidence_type: prose
  supported_semantics:
  - Return lifecycle with OMS credit note, settlement reverse/RRF rows, refund/commission reversal/recovery signs
  unsupported_semantics:
  - Does not require a process_variant if return is modeled as its own process
  allowed_card_types:
  - business_process
  - workflow_step
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.join.coverage
  source_section: 4.2 Join Keys and Coverage
  source_line_start: 166
  source_line_end: 174
  evidence_type: table
  supported_semantics:
  - order_id join coverage 77.8%, document_number-parent_id join 0%, order_id as mandatory join key
  unsupported_semantics:
  - Does not support document_number-parent_id as a working relationship
  allowed_card_types:
  - relationship
  - rule
  - reconciliation_profile
  - query_pattern
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.settlement.more_orders
  source_section: 4.3 Why Settlement Has More Orders Than OMS
  source_line_start: 175
  source_line_end: 189
  evidence_type: table
  supported_semantics:
  - Settlement has 2,116 more orders due to prior-year settlements and returns without current OMS counterpart
  unsupported_semantics:
  - Does not define a metric implementation
  allowed_card_types:
  - rule
  - review_item
  - query_pattern
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.tax.product_gst
  source_section: 5.1 Product GST
  source_line_start: 192
  source_line_end: 205
  evidence_type: table
  supported_semantics:
  - IGST vs CGST+SGST logic and apparel GST rate rule
  unsupported_semantics:
  - Does not create statutory filing cards
  allowed_card_types:
  - rule
  - value_profile
  - query_pattern
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.tax.commission_gst
  source_section: 5.2 GST on Commission (Service Tax)
  source_line_start: 206
  source_line_end: 214
  evidence_type: prose
  supported_semantics:
  - 18% GST on referral fees captured in settlement commission GST/tax columns
  unsupported_semantics:
  - Does not itself define executable SQL
  allowed_card_types:
  - rule
  - metric
  - column
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.tax.tcs_absent
  source_section: 5.3 TCS (Tax Collected at Source — GST §52)
  source_line_start: 215
  source_line_end: 220
  evidence_type: caveat
  supported_semantics:
  - TCS is collected by TUL but absent as explicit column in settlement and OMS reports
  unsupported_semantics:
  - Does not support a platform-specific TCS metric implementation
  allowed_card_types:
  - metric
  - review_item
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.tax.tds
  source_section: 5.4 TDS (Tax Deducted at Source — IT §194-O)
  source_line_start: 221
  source_line_end: 231
  evidence_type: metric_definition
  supported_semantics:
  - TDS rate ~0.1%, settlement columns total_tds and tds_on_e_commerce_operations, forward/reverse sign semantics
  unsupported_semantics:
  - Does not define external income-tax filing workflow
  allowed_card_types:
  - metric
  - rule
  - metric_implementation
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.total_forward_gmv
  source_section: 6.1 Total Forward GMV
  source_line_start: 234
  source_line_end: 250
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.1 Total Forward GMV
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.return_rate
  source_section: 6.2 Return Rate
  source_line_start: 251
  source_line_end: 263
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.2 Return Rate
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.aov_oms_clean
  source_section: 6.3 AOV from OMS (Clean Rows)
  source_line_start: 264
  source_line_end: 279
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.3 AOV from OMS (Clean Rows)
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.net_revenue_after_returns
  source_section: 6.4 Net Revenue After Returns
  source_line_start: 280
  source_line_end: 291
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.4 Net Revenue After Returns
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.monthly_settlement_trend
  source_section: 6.5 Monthly Settlement Trend
  source_line_start: 292
  source_line_end: 306
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.5 Monthly Settlement Trend
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.brand_gmv_oms
  source_section: 6.6 Brand GMV from OMS
  source_line_start: 307
  source_line_end: 325
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 6.6 Brand GMV from OMS
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.recon_oms_settlement
  source_section: 7.1 OMS ↔ Settlement Reconciliation
  source_line_start: 328
  source_line_end: 359
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source SQL/query semantics for 7.1 OMS ↔ Settlement Reconciliation
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.recon_return_oms_settlement
  source_section: 7.2 Return OMS ↔ Settlement Match
  source_line_start: 360
  source_line_end: 378
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source SQL/query semantics for 7.2 Return OMS ↔ Settlement Match
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.commission_rate_validation
  source_section: 7.3 Commission Rate Validation
  source_line_start: 379
  source_line_end: 393
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.3 Commission Rate Validation
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.settlement_batch_completeness
  source_section: 7.4 Settlement Batch Completeness
  source_line_start: 394
  source_line_end: 411
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.4 Settlement Batch Completeness
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.tds_reconciliation
  source_section: 7.5 TDS Reconciliation
  source_line_start: 412
  source_line_end: 430
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.5 TDS Reconciliation
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.filters.mandatory
  source_section: 9. Mandatory Query Filters
  source_line_start: 450
  source_line_end: 475
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 9. Mandatory Query Filters
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.settlement_batch_payout_summary
  source_section: 8.1 Settlement Batch Payout Summary
  source_line_start: 767
  source_line_end: 784
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 8.1 Settlement Batch Payout Summary
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.monthly_financial_waterfall
  source_section: 8.2 Monthly Financial Waterfall
  source_line_start: 785
  source_line_end: 801
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 8.2 Monthly Financial Waterfall
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.settlement_commission_rate_validation
  source_section: 8.3 Commission Rate Validation
  source_line_start: 802
  source_line_end: 816
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 8.3 Commission Rate Validation
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.settlement_oms_reconciliation
  source_section: 8.4 OMS ↔ Settlement Reconciliation
  source_line_start: 817
  source_line_end: 836
  evidence_type: reconciliation_playbook
  supported_semantics:
  - Source SQL/query semantics for 8.4 OMS ↔ Settlement Reconciliation
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.return_impact_analysis
  source_section: 8.5 Return Impact Analysis
  source_line_start: 837
  source_line_end: 853
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 8.5 Return Impact Analysis
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.tds_summary
  source_section: 8.6 TDS Summary
  source_line_start: 854
  source_line_end: 866
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 8.6 TDS Summary
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_monthly_gmv_trend
  source_section: 7.1 Monthly GMV Trend
  source_line_start: 1146
  source_line_end: 1160
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.1 Monthly GMV Trend
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_clean_forward_invoices
  source_section: 7.2 Clean Forward Invoices (Structured Rows)
  source_line_start: 1161
  source_line_end: 1170
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.2 Clean Forward Invoices (Structured Rows)
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_brand_level_performance
  source_section: 7.3 Brand-Level Performance
  source_line_start: 1171
  source_line_end: 1185
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.3 Brand-Level Performance
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_intra_inter_state_gst
  source_section: 7.4 Intra-State vs Inter-State GST
  source_line_start: 1186
  source_line_end: 1199
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.4 Intra-State vs Inter-State GST
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_settlement_join
  source_section: 7.5 OMS → Settlement Join
  source_line_start: 1200
  source_line_end: 1218
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.5 OMS → Settlement Join
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.sql.oms_hsn_distribution
  source_section: 7.6 HSN Distribution
  source_line_start: 1219
  source_line_end: 1235
  evidence_type: query_example
  supported_semantics:
  - Source SQL/query semantics for 7.6 HSN Distribution
  unsupported_semantics:
  - Does not support formulas beyond the referenced columns and filters
  allowed_card_types:
  - query_pattern
  - metric_implementation
  - formula_template
  - reconciliation_profile
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.quality.known_issues
  source_section: 8. Data Quality Observations & Known Issues
  source_line_start: 431
  source_line_end: 449
  evidence_type: caveat
  supported_semantics:
  - Cross-table data quality caveats and mitigations
  unsupported_semantics:
  - Does not require opening reviews where mitigation is explicitly documented
  allowed_card_types:
  - rule
  - review_item
  - validation_test
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.tables.summary
  source_section: 10. Table Summary Reference
  source_line_start: 476
  source_line_end: 482
  evidence_type: table
  supported_semantics:
  - Table purposes, row counts, date ranges, primary keys, join key, group_level_id
  unsupported_semantics:
  - Does not create tenant/group cards
  allowed_card_types:
  - table
  - relationship
  - rule
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.table.settlement.overview
  source_section: 1. Table Overview
  source_line_start: 490
  source_line_end: 505
  evidence_type: prose
  supported_semantics:
  - Settlement table purpose, settlement sign convention, TUL settlement entity, seller code, TSHIP
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.table.settlement.stats
  source_section: 2. Key Statistics
  source_line_start: 506
  source_line_end: 532
  evidence_type: table
  supported_semantics:
  - Settlement table rows, active rows, date range, distinct orders/batches, transaction counts and amounts
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.identity
  source_section: 3.1 Identity Columns
  source_line_start: 535
  source_line_end: 551
  evidence_type: schema_reference
  supported_semantics:
  - Settlement identity column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.date
  source_section: 3.2 Date Columns
  source_line_start: 552
  source_line_end: 559
  evidence_type: schema_reference
  supported_semantics:
  - Settlement date column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.financial
  source_section: 3.3 Financial Columns — SIGN CONVENTION IS CRITICAL
  source_line_start: 560
  source_line_end: 583
  evidence_type: schema_reference
  supported_semantics:
  - Settlement financial column types and forward/reverse sign conventions
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.tax_accounting
  source_section: 3.4 Tax / Accounting Columns
  source_line_start: 584
  source_line_end: 593
  evidence_type: schema_reference
  supported_semantics:
  - Settlement tax/accounting column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.classification
  source_section: 3.5 Classification Columns
  source_line_start: 594
  source_line_end: 604
  evidence_type: schema_reference
  supported_semantics:
  - Settlement classification values and fields
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.settlement.system
  source_section: 3.6 System / Metadata Columns
  source_line_start: 605
  source_line_end: 618
  evidence_type: schema_reference
  supported_semantics:
  - Settlement system/scope metadata fields
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.settlement.breakdown
  source_section: Transaction Type / Order Type / Fulfilment Breakdown
  source_line_start: 621
  source_line_end: 631
  evidence_type: table
  supported_semantics:
  - Settlement observed transaction/order/fulfilment/tag distribution
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.settlement.order_tag
  source_section: '`order_tag` Meanings'
  source_line_start: 632
  source_line_end: 638
  evidence_type: table
  supported_semantics:
  - Settlement order_tag meanings NOR and RRF
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.settlement.fulfilment_channel
  source_section: '`fulfilment_channel` / `fulfillment_type`'
  source_line_start: 639
  source_line_end: 645
  evidence_type: table
  supported_semantics:
  - Settlement fulfilment channel value meanings
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.settlement.order_type
  source_section: '`order_type`'
  source_line_start: 646
  source_line_end: 652
  evidence_type: table
  supported_semantics:
  - Settlement order_type value meanings
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.settlement.batch_structure
  source_section: Settlement Batch Structure
  source_line_start: 653
  source_line_end: 666
  evidence_type: table
  supported_semantics:
  - Settlement batch structure and weekly cadence
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.settlement.waterfall
  source_section: How TataCliq Settlement Is Calculated
  source_line_start: 669
  source_line_end: 692
  evidence_type: metric_definition
  supported_semantics:
  - Settlement financial waterfall and approximate settled_amount formula
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.settlement.quality
  source_section: 7. Data Quality Observations
  source_line_start: 748
  source_line_end: 764
  evidence_type: caveat
  supported_semantics:
  - Settlement-table data quality observations and mitigations
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.table.oms.overview
  source_section: 1. Table Overview
  source_line_start: 874
  source_line_end: 886
  evidence_type: prose
  supported_semantics:
  - OMS table purpose, row grain, seller/operator, brands/categories, column-shift caveat
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.table.oms.stats
  source_section: 2. Key Statistics
  source_line_start: 887
  source_line_end: 911
  evidence_type: table
  supported_semantics:
  - OMS table rows, active rows, date range, distinct orders, GSTINs, transaction counts, GMV
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.identity
  source_section: 3.1 Identity Columns
  source_line_start: 535
  source_line_end: 551
  evidence_type: schema_reference
  supported_semantics:
  - OMS identity column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.date
  source_section: 3.2 Date Columns
  source_line_start: 552
  source_line_end: 559
  evidence_type: schema_reference
  supported_semantics:
  - OMS date column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.financial
  source_section: 3.3 Financial Columns
  source_line_start: 944
  source_line_end: 952
  evidence_type: schema_reference
  supported_semantics:
  - OMS financial column schema
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.tax
  source_section: 3.4 Tax Columns
  source_line_start: 953
  source_line_end: 972
  evidence_type: schema_reference
  supported_semantics:
  - OMS tax column schema including typed and legacy columns
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.classification
  source_section: 3.5 Classification Columns
  source_line_start: 594
  source_line_end: 604
  evidence_type: schema_reference
  supported_semantics:
  - OMS classification columns and values
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.geographic
  source_section: 3.6 Geographic Columns
  source_line_start: 986
  source_line_end: 994
  evidence_type: schema_reference
  supported_semantics:
  - OMS source/destination state columns
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.schema.oms.system
  source_section: 3.7 System / Metadata Columns
  source_line_start: 995
  source_line_end: 1012
  evidence_type: schema_reference
  supported_semantics:
  - OMS system/scope metadata columns
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.transaction_document
  source_section: '`transaction_type` / `document_type` Breakdown'
  source_line_start: 1015
  source_line_end: 1023
  evidence_type: table
  supported_semantics:
  - OMS observed transaction_type/document_type distribution including shifted rows
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.brand_distribution
  source_section: '`brand` Distribution (Forward, structured rows only)'
  source_line_start: 1024
  source_line_end: 1034
  evidence_type: table
  supported_semantics:
  - OMS brand distribution with GMV, average price, HSN counts
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.seller_gstin_warehouse
  source_section: Seller GSTIN → Warehouse Mapping
  source_line_start: 1035
  source_line_end: 1043
  evidence_type: table
  supported_semantics:
  - OMS seller GSTIN to state/slave code mapping
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.ecom_gstin
  source_section: TataCliq E-Commerce GSTINs
  source_line_start: 1044
  source_line_end: 1047
  evidence_type: prose
  supported_semantics:
  - OMS observed TataCliq e-commerce GSTINs and place_of_supply selection
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.place_of_supply
  source_section: '`place_of_supply` Values'
  source_line_start: 1048
  source_line_end: 1051
  evidence_type: table
  supported_semantics:
  - OMS place_of_supply state-code values
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.hsn_codes
  source_section: HSN Codes (Sample — 51 Total)
  source_line_start: 1052
  source_line_end: 1065
  evidence_type: table
  supported_semantics:
  - OMS HSN code category sample
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.values.oms.gst_rates
  source_section: GST Rates Observed
  source_line_start: 1066
  source_line_end: 1079
  evidence_type: table
  supported_semantics:
  - OMS GST rate values and apparel rule
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


```yaml
source_evidence:
  id: ev.tatacliq.oms.quality
  source_section: 6. Data Quality Observations
  source_line_start: 1127
  source_line_end: 1143
  evidence_type: caveat
  supported_semantics:
  - OMS table data quality observations and mitigations
  unsupported_semantics:
  - Does not create out-of-scope account, bank, logistics, ERP, or statutory filing cards
  allowed_card_types:
  - table
  - column
  - value_profile
  - metric
  - rule
  - review_item
  forbidden_card_types: []
  confidence: high
```


## 3. SQL Pattern Registry


```yaml
sql_pattern:
  sql_id: sql.tatacliq.total_forward_gmv
  source_section: 6.1 Total Forward GMV
  source_line_start: 237
  source_line_end: 248
  target_semantic_card: metric.tatacliq.forward_gmv
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - gross_commission_gst_amount
  - is_active
  - referral_fees
  - settled_amount
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  sql: |-
    SELECT
      SUM(ABS(charged_amount)) AS gross_gmv,
      SUM(gross_commission) AS total_commission,
      SUM(referral_fees) AS referral_fee_excl_gst,
      SUM(gross_commission_gst_amount) AS commission_gst,
      SUM(total_tds) AS total_tds,
      SUM(ABS(settled_amount)) AS net_payout,
      ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS commission_rate_pct,
      ROUND(100.0 * SUM(ABS(settled_amount)) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS payout_ratio_pct
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true AND transaction_type = 'forward';
    -- Observed: GMV ₹1.70 Cr | Commission 41.4% | Payout ratio ~58.5%
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.return_rate
  source_section: 6.2 Return Rate
  source_line_start: 254
  source_line_end: 261
  target_semantic_card: metric.tatacliq.return_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - is_active
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.return_rate
  sql: |-
    SELECT
      COUNT_IF(transaction_type = 'reverse') AS returns,
      COUNT_IF(transaction_type = 'forward') AS sales,
      ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
        / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_rate_pct
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true;
    -- Observed: 5,464 returns / 14,884 sales = 36.7%
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.aov_oms_clean
  source_section: 6.3 AOV from OMS (Clean Rows)
  source_line_start: 267
  source_line_end: 277
  target_semantic_card: metric.tatacliq.average_order_value
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - is_active
  - seller_name
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.aov_oms_clean
  sql: |-
    SELECT
      brand,
      COUNT(*) AS invoices,
      AVG(charged_amount) AS aov,
      SUM(charged_amount) AS gmv
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL
    GROUP BY brand ORDER BY gmv DESC;
    -- Ishin highest AOV at ₹2,135; Lilpicks lowest at ₹835
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.net_revenue_after_returns
  source_section: 6.4 Net Revenue After Returns
  source_line_start: 283
  source_line_end: 289
  target_semantic_card: metric.tatacliq.net_revenue_after_returns
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - is_active
  - settled_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.net_revenue_after_returns
  sql: |-
    SELECT
      SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
      SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_settled,
      SUM(settled_amount) AS net_revenue
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true;
    -- Note: forward_settled is negative; return_settled is positive in TataCliq's convention
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.monthly_settlement_trend
  source_section: 6.5 Monthly Settlement Trend
  source_line_start: 295
  source_line_end: 304
  target_semantic_card: metric.tatacliq.monthly_settlement_summary
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - is_active
  - settled_amount
  - settlement_date
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.monthly_settlement_trend
  sql: |-
    SELECT
      DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
      COUNT(*) AS line_items,
      SUM(ABS(charged_amount)) AS gross_gmv,
      SUM(gross_commission) AS commission,
      SUM(total_tds) AS tds,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1 ORDER BY 1;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.brand_gmv_oms
  source_section: 6.6 Brand GMV from OMS
  source_line_start: 310
  source_line_end: 320
  target_semantic_card: metric.tatacliq.brand_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - hsn_code
  - is_active
  - seller_name
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.brand_gmv_oms
  sql: |-
    SELECT
      brand,
      COUNT(*) AS invoices,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS aov,
      COUNT(DISTINCT hsn_code) AS hsn_count
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL
    GROUP BY brand ORDER BY gmv DESC;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.recon_oms_settlement
  source_section: 7.1 OMS ↔ Settlement Reconciliation
  source_line_start: 331
  source_line_end: 357
  target_semantic_card: reconciliation_profile.tatacliq.oms_settlement_forward
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - description
  - document_type
  - gross_commission
  - gross_commission_gst_amount
  - is_active
  - order_id
  - referral_fees
  - seller_name
  - settled_amount
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  sql: |-
    SELECT
      o.order_id,
      o.brand,
      o.description,
      o.charged_amount AS oms_invoice_value,
      o.document_type,
      ABS(s.charged_amount) AS stl_charged,
      s.gross_commission,
      s.referral_fees,
      s.gross_commission_gst_amount AS commission_gst,
      s.total_tds,
      ABS(s.settled_amount) AS net_payout,
      ABS(o.charged_amount - ABS(s.charged_amount)) AS price_variance,
      CASE
        WHEN s.order_id IS NULL THEN 'Not in Settlement (Oct–Dec 2025 gap)'
        WHEN ABS(o.charged_amount - ABS(s.charged_amount)) > 1 THEN 'Price Variance'
        ELSE 'Matched'
      END AS recon_status
    FROM zs_observe.tatacliq_oms o
    LEFT JOIN zs_observe.tatacliq_settlement s
      ON o.order_id = s.order_id
      AND s.is_active = true
      AND s.transaction_type = 'forward'
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.seller_name IS NOT NULL;
    -- Coverage: 10,110 / 12,998 = 77.8%
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.recon_return_oms_settlement
  source_section: 7.2 Return OMS ↔ Settlement Match
  source_line_start: 363
  source_line_end: 376
  target_semantic_card: reconciliation_profile.tatacliq.return_oms_settlement
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  referenced_columns:
  - charged_amount
  - gross_commission
  - is_active
  - order_id
  - settled_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  sql: |-
    SELECT
      o.order_id,
      o.charged_amount AS oms_credit_note_value,
      s.charged_amount AS stl_return_value,
      s.gross_commission AS commission_reversed,
      s.settled_amount AS return_net_settlement,
      ABS(o.charged_amount - s.charged_amount) AS value_variance
    FROM zs_observe.tatacliq_oms o
    LEFT JOIN zs_observe.tatacliq_settlement s
      ON o.order_id = s.order_id
      AND s.is_active = true
      AND s.transaction_type = 'reverse'
    WHERE o.is_active = true
      AND o.transaction_type = 'reverse';
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.commission_rate_validation
  source_section: 7.3 Commission Rate Validation
  source_line_start: 382
  source_line_end: 391
  target_semantic_card: metric.tatacliq.commission_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - gross_commission_gst_amount
  - is_active
  - referral_fees
  - settlement_date
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.commission_rate_validation
  sql: |-
    SELECT
      DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
      SUM(ABS(charged_amount)) AS gmv,
      SUM(gross_commission) AS total_commission,
      SUM(referral_fees) AS referral_fees,
      SUM(gross_commission_gst_amount) AS commission_gst,
      ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS effective_commission_pct
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1 ORDER BY 1;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement_batch_completeness
  source_section: 7.4 Settlement Batch Completeness
  source_line_start: 397
  source_line_end: 409
  target_semantic_card: metric.tatacliq.settlement_batch_completeness
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - is_active
  - order_id
  - settled_amount
  - settlement_date
  - settlement_id
  - total_tds
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  sql: |-
    SELECT
      settlement_id,
      CAST(settlement_date AS DATE) AS stl_date,
      COUNT(*) AS line_items,
      COUNT(DISTINCT order_id) AS orders,
      SUM(ABS(charged_amount)) AS gross_gmv,
      SUM(gross_commission) AS commission,
      SUM(settled_amount) AS net_settled,
      SUM(total_tds) AS tds
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY settlement_id, settlement_date
    ORDER BY settlement_date DESC;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.tds_reconciliation
  source_section: 7.5 TDS Reconciliation
  source_line_start: 415
  source_line_end: 425
  target_semantic_card: metric.tatacliq.effective_tds_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - is_active
  - settlement_date
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.tds_reconciliation
  sql: |-
    SELECT
      DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
      SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds_charged,
      SUM(CASE WHEN transaction_type='reverse' THEN total_tds ELSE 0 END) AS tds_reversed,
      SUM(total_tds) AS net_tds_impact,
      ROUND(100.0 * SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END)
        / NULLIF(SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END), 0), 4) AS effective_tds_rate_pct
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY 1 ORDER BY 1;
    -- Effective TDS rate: ~0.1% consistently
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.mandatory_query_filters
  source_section: 9. Mandatory Query Filters
  source_line_start: 453
  source_line_end: 470
  target_semantic_card: rule.tatacliq.mandatory_query_filters
  source_tables: []
  referenced_columns:
  - charged_amount
  - group_level_id
  - is_active
  - order_tag
  - seller_name
  - transaction_type
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  sql: |-
    -- Both tables (standard)
    WHERE is_active = true
      AND group_level_id = 22

    -- OMS: structured forward invoices only
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL   -- removes column-shifted rows

    -- Settlement: forward sales GMV
    WHERE is_active = true
      AND transaction_type = 'forward'
    -- Note: use ABS(charged_amount) for GMV

    -- Settlement: returns only
    WHERE is_active = true
      AND transaction_type = 'reverse'
      AND order_tag = 'RRF'
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.batch_payout_summary
  source_section: 8.1 Settlement Batch Payout Summary
  source_line_start: 770
  source_line_end: 782
  target_semantic_card: metric.tatacliq.seller_realization_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - is_active
  - settled_amount
  - settlement_date
  - settlement_id
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_payout_summary
  sql: |-
    SELECT
      CAST(settlement_date AS DATE) AS stl_date,
      settlement_id,
      COUNT(*) AS line_items,
      SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END) AS forward_gmv,
      SUM(CASE WHEN transaction_type='reverse' THEN charged_amount ELSE 0 END) AS return_refunds,
      SUM(gross_commission) AS total_commission,
      SUM(total_tds) AS total_tds,
      SUM(settled_amount) AS net_payout
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY settlement_date, settlement_id
    ORDER BY settlement_date DESC;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.monthly_financial_waterfall
  source_section: 8.2 Monthly Financial Waterfall
  source_line_start: 788
  source_line_end: 799
  target_semantic_card: metric.tatacliq.monthly_financial_waterfall
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - gross_commission_gst_amount
  - is_active
  - settled_amount
  - settlement_date
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.monthly_financial_waterfall
  sql: |-
    SELECT
      DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
      SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END) AS forward_gmv,
      SUM(CASE WHEN transaction_type='forward' THEN gross_commission ELSE 0 END) AS forward_commission,
      SUM(CASE WHEN transaction_type='forward' THEN gross_commission_gst_amount ELSE 0 END) AS commission_gst,
      SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds,
      SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_net,
      SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_net,
      SUM(settled_amount) AS total_net
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY 1 ORDER BY 1;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.commission_rate_validation
  source_section: 8.3 Commission Rate Validation
  source_line_start: 805
  source_line_end: 814
  target_semantic_card: metric.tatacliq.commission_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - gross_commission_gst_amount
  - is_active
  - referral_fees
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.settlement_commission_rate_validation
  sql: |-
    SELECT
      COUNT(*) AS orders,
      SUM(ABS(charged_amount)) AS gross_gmv,
      SUM(gross_commission) AS total_commission,
      SUM(referral_fees) AS referral_fees_excl_gst,
      SUM(gross_commission_gst_amount) AS commission_gst,
      ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 4) AS commission_rate_pct,
      ROUND(100.0 * SUM(referral_fees) / NULLIF(SUM(ABS(charged_amount)), 0), 4) AS referral_rate_pct
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true AND transaction_type = 'forward';
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.oms_reconciliation
  source_section: 8.4 OMS ↔ Settlement Reconciliation
  source_line_start: 820
  source_line_end: 834
  target_semantic_card: reconciliation_profile.tatacliq.oms_settlement_forward
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - description
  - gross_commission
  - is_active
  - order_id
  - seller_name
  - settled_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.settlement_oms_reconciliation
  sql: |-
    SELECT
      o.order_id, o.brand, o.description,
      o.charged_amount AS oms_invoice,
      ABS(s.charged_amount) AS stl_charged,
      ABS(o.charged_amount - ABS(s.charged_amount)) AS price_variance,
      s.gross_commission, s.settled_amount,
      CASE WHEN s.order_id IS NULL THEN 'Not in Settlement'
           WHEN ABS(o.charged_amount - ABS(s.charged_amount)) > 1 THEN 'Price Variance'
           ELSE 'Matched' END AS status
    FROM zs_observe.tatacliq_oms o
    LEFT JOIN zs_observe.tatacliq_settlement s
      ON o.order_id = s.order_id AND s.is_active = true AND s.transaction_type = 'forward'
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.seller_name IS NOT NULL;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.return_impact_analysis
  source_section: 8.5 Return Impact Analysis
  source_line_start: 840
  source_line_end: 851
  target_semantic_card: metric.tatacliq.return_impact
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - charged_amount
  - gross_commission
  - is_active
  - order_tag
  - settled_amount
  - transaction_type
  - tul_discount
  evidence_refs:
  - ev.tatacliq.sql.return_impact_analysis
  sql: |-
    SELECT
      order_tag,
      transaction_type,
      COUNT(*) AS cnt,
      SUM(ABS(charged_amount)) AS gmv_abs,
      SUM(gross_commission) AS commission,
      SUM(tul_discount) AS tul_discount,
      SUM(settled_amount) AS net_settled
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY order_tag, transaction_type
    ORDER BY cnt DESC;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.settlement.tds_summary
  source_section: 8.6 TDS Summary
  source_line_start: 857
  source_line_end: 864
  target_semantic_card: metric.tatacliq.tds_deducted
  source_tables:
  - zs_observe.tatacliq_settlement
  referenced_columns:
  - is_active
  - settlement_date
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.tds_summary
  sql: |-
    SELECT
      DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
      SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds_forward,
      SUM(CASE WHEN transaction_type='reverse' THEN total_tds ELSE 0 END) AS tds_reversed,
      SUM(total_tds) AS net_tds
    FROM zs_observe.tatacliq_settlement
    WHERE is_active = true
    GROUP BY 1 ORDER BY 1;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.monthly_gmv_trend
  source_section: 7.1 Monthly GMV Trend
  source_line_start: 1149
  source_line_end: 1158
  target_semantic_card: metric.tatacliq.monthly_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - charged_amount
  - created_date
  - igst
  - is_active
  - tax_cgst_amount
  - tax_igst_amount
  - tax_sgst_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_monthly_gmv_trend
  sql: |-
    SELECT
      CAST(DATE_TRUNC('month', CAST(created_date AS DATE)) AS DATE) AS month,
      transaction_type,
      COUNT(*) AS docs,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
    GROUP BY 1, 2 ORDER BY 1, 2;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.clean_forward_invoices
  source_section: 7.2 Clean Forward Invoices (Structured Rows)
  source_line_start: 1164
  source_line_end: 1168
  target_semantic_card: query_pattern.tatacliq.oms_clean_forward_invoices
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - is_active
  - seller_name
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_clean_forward_invoices
  sql: |-
    SELECT *
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL;  -- removes 1,984 shifted rows
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.brand_level_performance
  source_section: 7.3 Brand-Level Performance
  source_line_start: 1174
  source_line_end: 1183
  target_semantic_card: metric.tatacliq.brand_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - is_active
  - seller_name
  - tax_cgst_amount
  - tax_igst_amount
  - tax_sgst_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_brand_level_performance
  sql: |-
    SELECT brand,
      COUNT(*) AS invoices,
      SUM(charged_amount) AS gmv,
      AVG(charged_amount) AS avg_invoice_value,
      SUM(tax_igst_amount + tax_cgst_amount + tax_sgst_amount) AS total_gst
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL
    GROUP BY brand ORDER BY gmv DESC;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.intra_inter_state_gst
  source_section: 7.4 Intra-State vs Inter-State GST
  source_line_start: 1189
  source_line_end: 1197
  target_semantic_card: metric.tatacliq.product_gst_amount
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - charged_amount
  - igst
  - is_active
  - tax_cgst_amount
  - tax_igst_amount
  - tax_igst_rate
  - tax_sgst_amount
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_intra_inter_state_gst
  sql: |-
    SELECT
      CASE WHEN tax_igst_rate > 0 THEN 'Inter-State (IGST)' ELSE 'Intra-State (CGST+SGST)' END AS gst_type,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      SUM(tax_igst_amount) AS igst,
      SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true AND transaction_type = 'forward'
    GROUP BY 1;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.settlement_join
  source_section: 7.5 OMS → Settlement Join
  source_line_start: 1203
  source_line_end: 1216
  target_semantic_card: relationship.tatacliq.oms_settlement.order_id
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - description
  - document_type
  - gross_commission
  - is_active
  - order_id
  - seller_name
  - settled_amount
  - total_tds
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_settlement_join
  sql: |-
    SELECT
      o.order_id, o.brand, o.description,
      o.charged_amount AS oms_invoice_value,
      o.document_type,
      s.charged_amount AS settlement_charged,
      s.gross_commission, s.settled_amount,
      s.total_tds
    FROM zs_observe.tatacliq_oms o
    LEFT JOIN zs_observe.tatacliq_settlement s
      ON o.order_id = s.order_id
      AND s.is_active = true
    WHERE o.is_active = true
      AND o.transaction_type = 'forward'
      AND o.seller_name IS NOT NULL;
```


```yaml
sql_pattern:
  sql_id: sql.tatacliq.oms.hsn_distribution
  source_section: 7.6 HSN Distribution
  source_line_start: 1222
  source_line_end: 1234
  target_semantic_card: metric.tatacliq.hsn_distribution
  source_tables:
  - zs_observe.tatacliq_oms
  referenced_columns:
  - brand
  - charged_amount
  - hsn_code
  - is_active
  - seller_name
  - tax_igst_rate
  - transaction_type
  evidence_refs:
  - ev.tatacliq.sql.oms_hsn_distribution
  sql: |-
    SELECT hsn_code,
      brand,
      COUNT(*) AS cnt,
      SUM(charged_amount) AS gmv,
      AVG(tax_igst_rate) AS avg_igst_rate
    FROM zs_observe.tatacliq_oms
    WHERE is_active = true
      AND transaction_type = 'forward'
      AND seller_name IS NOT NULL
      AND hsn_code IS NOT NULL
    GROUP BY hsn_code, brand
    ORDER BY cnt DESC
    LIMIT 20;
```


## 4. Candidate Cards


### 4.1 platform


```yaml
candidate_card:
  card_type: platform
  card_id: platform.tatacliq
  display_name: TataCliq
  canonical_name: TataCliq
  aliases:
  - TataCliq
  - Tata CLiQ
  - TataCliq Marketplace
  operator: Tata Unistore Limited
  marketplace_category: curated_ecommerce_marketplace
  source_documents:
  - TataCliq Recon KB.docx
  evidence_refs:
  - ev.tatacliq.overview.background
  confidence: high
  review_status: ready
```


### 4.2 platform_context


```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.tatacliq.in
  display_name: TataCliq India marketplace context
  platform_id: platform.tatacliq
  country_code: IN
  currency: INR
  timezone: Asia/Kolkata
  marketplace_model: curated_invite_only_phygital_marketplace
  fulfilment_models:
  - TSHIP
  tax_model: India GST with e-commerce operator GSTIN/TCS context; marketplace-side tax amounts only
  runtime_scope_policy: group_level_id=22 is source-documented as a filter/value; actual user/account scope binding remains
    external.
  evidence_refs:
  - ev.tatacliq.overview.background
  - ev.tatacliq.fulfilment.tship
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


### 4.3 domain


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.orders
  display_name: TataCliq marketplace OMS/order/invoice semantics
  domain_family: orders
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - orders
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.table.oms.overview
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.settlement
  display_name: TataCliq marketplace settlement and payout ledger semantics
  domain_family: settlement
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - settlement
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.table.settlement.overview
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.fees
  display_name: TataCliq commission, referral fee, bundled fee, and deduction semantics
  domain_family: fees
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - fees
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.fee.structure
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.returns
  display_name: TataCliq returns, reverse rows, RRF, and recovery semantics
  domain_family: returns
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - returns
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.tax
  display_name: TataCliq marketplace-side GST/TDS/TCS amount semantics, not statutory filing
  domain_family: tax
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - tax
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.tax.product_gst
  - ev.tatacliq.tax.tds
  - ev.tatacliq.tax.tcs_absent
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.reconciliation
  display_name: TataCliq marketplace-internal reconciliation semantics
  domain_family: reconciliation
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - reconciliation
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.query_guidance
  display_name: TataCliq deterministic query, filter, SQL, and output guidance
  domain_family: query_guidance
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - query_guidance
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: domain
  card_id: domain.tatacliq.mapping_enrichment
  display_name: TataCliq brand, GSTIN, HSN, seller-code, slave/warehouse, and enrichment references
  domain_family: mapping_enrichment
  scope_note: Marketplace-vendor semantics only; tenant/group/platform-account/bank/logistics/ERP/statutory-filing cards are
    forbidden.
  included_modules:
  - mapping_enrichment
  excluded_modules:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.brands.dataset
  - ev.tatacliq.warehouse.gstin
  confidence: high
  review_status: ready
```


### 4.4 table


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  fully_qualified_name: zs_observe.tatacliq_settlement
  display_name: zs_observe.tatacliq_settlement
  business_purpose: Financial settlement and payout ledger for TataCliq seller account
  semantic_module: settlement
  grain: settlement_line_or_order_settlement_line
  primary_key_candidates:
  - settlement_id
  - order_id
  join_key_candidates:
  - order_id
  required_filters:
  - is_active = true
  scope_filter_columns:
  - group_level_id = 22 (source-documented filter/value; not a group/account card)
  date_range_evidence: 2025-03-20 to 2025-09-25
  row_count_evidence: 20348
  source_section: 'Table: TataCliq Settlement — Table Knowledge Base'
  evidence_refs:
  - ev.tatacliq.table.settlement.overview
  - ev.tatacliq.table.settlement.stats
  - ev.tatacliq.tables.summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  fully_qualified_name: zs_observe.tatacliq_oms
  display_name: zs_observe.tatacliq_oms
  business_purpose: GST invoice / OMS table storing invoices and credit notes
  semantic_module: orders
  grain: gst_document_line_item_or_order_item_line
  primary_key_candidates:
  - order_id
  - document_number
  join_key_candidates:
  - order_id
  required_filters:
  - is_active = true
  scope_filter_columns:
  - group_level_id = 22 (source-documented filter/value; not a group/account card)
  date_range_evidence: 2025-01-01 to 2025-12-31
  row_count_evidence: 18215
  source_section: 'Table: TataCliq OMS — Table Knowledge Base'
  evidence_refs:
  - ev.tatacliq.table.oms.overview
  - ev.tatacliq.table.oms.stats
  - ev.tatacliq.tables.summary
  confidence: high
  review_status: ready
```


### 4.5 column


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: ancestry
  data_type: varchar
  description: Lineage
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.ancestry
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: brand
  data_type: varchar
  description: Brand name (`High Star`, `Ishin`, `Anubhutee`, `Dennis Lingo`, `Lilpicks`, `Hubberholme`)
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.brand
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: brand_ref_1
  data_type: varchar
  description: Brand reference slugs
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.brand_ref_1
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: brand_ref_2
  data_type: varchar
  description: Brand reference slugs
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.brand_ref_2
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: cess
  data_type: varchar
  description: Cess amount
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.cess
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: cgst_amount
  data_type: varchar
  description: Legacy CGST columns
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.cgst_amount
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: cgst_rate
  data_type: varchar
  description: Legacy CGST columns
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.cgst_rate
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: charged_amount
  data_type: real
  description: '**Invoice / credit note total value (GST inclusive)**'
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.charged_amount
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: charged_amount_excluding_tax
  data_type: real
  description: Taxable base (excluding GST)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.charged_amount_excluding_tax
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: created_date
  data_type: varchar
  description: 'Record date (stored as varchar, format: `2025-09-24`) — **primary date field**'
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.date
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.created_date
  data_quality_notes:
  - Stored as varchar in source; cast to DATE for date filters.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: currency_type
  data_type: varchar
  description: '`INR`'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.currency_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: description
  data_type: varchar
  description: Product description
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.description
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: destination_state
  data_type: varchar
  description: Buyer state (title case or NULL)
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.geographic
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.destination_state
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: destination_state_code
  data_type: varchar
  description: Destination state code
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.geographic
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.destination_state_code
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_date
  data_type: varchar
  description: 'GST document date (format: `SEPTEMBER 24 2025` — verbose string)'
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.date
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_date
  data_quality_notes:
  - Verbose string; use document_date_temp_old or created_date for reliable date filtering.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_date_temp_old
  data_type: date
  description: Legacy date column (properly typed)
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.date
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_date_temp_old
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_month
  data_type: varchar
  description: Month of document
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.date
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_month
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_number
  data_type: varchar
  description: '**GST document number** (Invoice or Credit Note number, e.g., `D6832725CA001697`) — join key to settlement
    via `parent_id` (partial match)'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_number
  data_quality_notes:
  - Does not join to settlement parent_id in current data; use order_id for OMS-settlement joins.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_type
  data_type: varchar
  description: '`Invoice` or `Credit Note` (NULL for 1,984 shifted rows)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: document_value
  data_type: varchar
  description: Document value (varchar version of `charged_amount`)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.financial
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.document_value
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: file_uuid
  data_type: varchar
  description: Source file UUID
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.file_uuid
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: group_id
  data_type: integer
  description: Internal references
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.group_id
  scope_identifier_policy: documented_source_filter_value_only_not_account_binding
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: group_level_id
  data_type: integer
  description: '`22` — TataCliq / Mensa account'
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.group_level_id
  scope_identifier_policy: documented_source_filter_value_only_not_account_binding
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: gstin_of_e_com
  data_type: varchar
  description: TataCliq's e-commerce GSTIN for the destination state (33 distinct)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: hsn
  data_type: varchar
  description: HSN code (pipeline-derived field)
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.hsn
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: hsn_code
  data_type: varchar
  description: '**Primary HSN code** (structured rows)'
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.hsn_code
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: hsn_description
  data_type: varchar
  description: Product description (raw field — often = description)
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.hsn_description
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: hsn_generated
  data_type: varchar
  description: System-generated HSN
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.hsn_generated
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: igst_amount
  data_type: varchar
  description: Legacy IGST columns (varchar — use typed `tax_igst_*` columns)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.igst_amount
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: igst_rate
  data_type: varchar
  description: Legacy IGST columns (varchar — use typed `tax_igst_*` columns)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.igst_rate
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: is_active
  data_type: boolean
  description: Always `true`
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.is_active
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: order_id
  data_type: varchar
  description: TataCliq order number (e.g., `126957054888163`) — **primary join key to settlement**
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.order_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: order_status
  data_type: varchar
  description: '`Invoice` or `Credit Note` (mirrors `document_type`)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.order_status
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: order_tag
  data_type: varchar
  description: '`NOR` = Normal order (all rows)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.order_tag
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: other_id
  data_type: varchar
  description: Alternate reference ID
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.other_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: parent_id
  data_type: varchar
  description: Parent document reference (= `document_number` for this seller)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.parent_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: place_of_supply
  data_type: varchar
  description: GST place of supply (state code, e.g., `27` = Maharashtra, `32` = Kerala)
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.place_of_supply
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: quantity
  data_type: integer
  description: Quantity (NULL for \~76% of forward rows)
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.quantity
  data_quality_notes:
  - NULL for ~76% of forward OMS rows; use row count as unit proxy where documented.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: seller_code
  data_type: varchar
  description: 'TataCliq seller code: `126957`'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.seller_code
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: seller_gstin
  data_type: varchar
  description: Seller GSTIN (4 distinct — see below)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.seller_gstin
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: seller_name
  data_type: varchar
  description: '`Mensa Brand Technologies Private Limited` (NULL for 1,984 shifted rows)'
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.seller_name
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: sgst_utgst_amount
  data_type: varchar
  description: Legacy SGST/UTGST columns
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.sgst_utgst_amount
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: sgst_utgst_rate
  data_type: varchar
  description: Legacy SGST/UTGST columns
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.sgst_utgst_rate
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: sheetname
  data_type: varchar
  description: Source sheet
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.sheetname
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: sku_id
  data_type: varchar
  description: Seller SKU — **NULL for all 18,215 rows**
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.sku_id
  data_quality_notes:
  - NULL for all OMS rows; SKU-level analysis is not supported from OMS alone.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: slave_id
  data_type: varchar
  description: 'Warehouse + seller code identifier (format: `{seller_code}-{warehouse_code}`, e.g., `126957-BHSS1`)'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.slave_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: slave_state
  data_type: varchar
  description: State code of dispatch warehouse (e.g., `27` = Maharashtra)
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.slave_state
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: source_gst_id
  data_type: varchar
  description: Same as `seller_gstin`
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.source_gst_id
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: source_gst_name
  data_type: varchar
  description: Seller entity name
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.source_gst_name
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: source_state
  data_type: varchar
  description: 'Seller dispatch state (title case: `Haryana`, `Karnataka`, `Maharashtra`, `West Bengal`)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.geographic
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.source_state
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: source_state_code
  data_type: varchar
  description: State code
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.geographic
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.source_state_code
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_cgst_amount
  data_type: real
  description: CGST amount (intra-state)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_cgst_amount
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_cgst_rate
  data_type: real
  description: CGST rate (0, 0.025, 0.06)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_cgst_rate
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_igst_amount
  data_type: real
  description: IGST amount (inter-state)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_igst_amount
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_igst_rate
  data_type: real
  description: IGST rate (0, 0.05, 0.12, 0.18)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_igst_rate
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_sgst_amount
  data_type: real
  description: SGST amount
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_sgst_amount
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tax_sgst_rate
  data_type: real
  description: SGST rate (mirrors CGST)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tax_sgst_rate
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: taxable_value
  data_type: varchar
  description: Taxable value (NULL for shifted rows)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.financial
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.taxable_value
  data_quality_notes:
  - Legacy/varchar field; prefer typed tax_* columns or explicit casts where available.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: _temp_old
  data_type: various
  description: Legacy migration columns
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.temp_old
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: tenant_id
  data_type: integer
  description: Internal references
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.tenant_id
  scope_identifier_policy: documented_source_filter_value_only_not_account_binding
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: transaction_id
  data_type: varchar
  description: TataCliq transaction ID (same as `order_id` for forward rows)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.transaction_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: transaction_type
  data_type: varchar
  description: '`forward` (Invoice) or `reverse` (Credit Note)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.transaction_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: txn_uuid
  data_type: varchar
  description: Pipeline UUID
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.txn_uuid
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: unique_id
  data_type: bigint
  description: System row identifier
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.unique_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: unique_value
  data_type: varchar
  description: Deduplication hash
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.unique_value
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: unnamed__24
  data_type: varchar
  description: Unnamed column from source Excel
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.unnamed_24
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_oms
  schema: zs_observe
  table_name: tatacliq_oms
  column_name: zen_sheet_name
  data_type: varchar
  description: Source sheet
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.oms.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_oms.zen_sheet_name
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: accounting_document_za
  data_type: decimal
  description: SAP accounting document reference
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.tax_accounting
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.accounting_document_za
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: ancestry
  data_type: varchar
  description: Lineage
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.ancestry
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: cgst
  data_type: decimal
  description: CGST on commission (intra-state)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.tax_accounting
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.cgst
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: charged_amount
  data_type: decimal
  description: Gross product value (seller debited)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.charged_amount
  sign_convention: forward NEGATIVE; reverse POSITIVE; use ABS(charged_amount) for forward GMV.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: clearing_doc
  data_type: decimal
  description: SAP clearing document number
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.tax_accounting
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.clearing_doc
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: cod_fees
  data_type: decimal
  description: COD fees (all zero — POSTPAID/PREPAID only)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.cod_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: currency_type
  data_type: varchar
  description: '`INR`'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.currency_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: description
  data_type: varchar
  description: 'Transaction description (= `order_type` value: `PREPAID` / `POSTPAID`)'
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.description
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: fiscal_year
  data_type: decimal
  description: Fiscal year (`2024.0`, `2025.0`)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.date
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.fiscal_year
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: fulfillment_type
  data_type: varchar
  description: Same as `fulfilment_channel`
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.fulfillment_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: fulfilment_channel
  data_type: varchar
  description: '`TSHIP/HD` (Home Delivery) or `TSHIP/ED` (Express Delivery)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: gross_commission
  data_type: decimal
  description: Total TataCliq fee (referral + GST)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.gross_commission
  sign_convention: forward POSITIVE commission charge; reverse NEGATIVE commission reversal.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: gross_commission_gst_amount
  data_type: decimal
  description: 18% GST on gross_commission
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.gross_commission_gst_amount
  sign_convention: commission GST component; positive in documented financial schema.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: group_level_id
  data_type: integer
  description: '`22`'
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.settlement.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.group_level_id
  scope_identifier_policy: documented_source_filter_value_only_not_account_binding
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: igst
  data_type: decimal
  description: IGST on commission (= `gross_commission_gst_amount` for inter-state)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.tax_accounting
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.igst
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: is_active
  data_type: boolean
  description: Always `true`
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.is_active
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: mp_fees
  data_type: decimal
  description: Marketplace fees (all zero)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.mp_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: net_payable
  data_type: decimal
  description: Net payable (not populated)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.net_payable
  data_quality_notes:
  - Not populated; use settled_amount as authoritative net settlement field.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: order_id
  data_type: varchar
  description: TataCliq order number — **primary join key to OMS**
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.order_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: order_reference_no
  data_type: varchar
  description: Order reference number (TataCliq internal, e.g., `139339072`)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.order_reference_no
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: order_tag
  data_type: varchar
  description: '`NOR` (Normal) or `RRF` (Return to Fulfilment Centre)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.order_tag
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: order_type
  data_type: varchar
  description: '`PREPAID` or `POSTPAID`'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.order_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: other_fees
  data_type: decimal
  description: Other fees (all zero in dataset)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.other_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: other_id
  data_type: varchar
  description: Alternate reference
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.other_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: other_transaction_fees
  data_type: decimal
  description: Other transaction fees (all zero)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.other_transaction_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: parent_id
  data_type: varchar
  description: Parent document reference (= `order_id` for most rows)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.parent_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: pg_fees
  data_type: decimal
  description: Payment gateway fees (all zero)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.pg_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: product_value
  data_type: decimal
  description: Product value (absolute)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.product_value
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: referral_fee
  data_type: decimal
  description: Alternate referral fee field
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.referral_fee
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: referral_fees
  data_type: decimal
  description: Commission excl. GST (= referral fee net)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.referral_fees
  data_quality_notes:
  - NULL for reverse rows; use gross_commission for commission analysis across both directions.
  sign_convention: forward POSITIVE net referral fee; reverse NULL/0 in source.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: seller_code
  data_type: varchar
  description: '`126957` — single seller code'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.seller_code
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: settled_amount
  data_type: decimal
  description: Net payout to seller (= charged_amount + gross_commission)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.settled_amount
  sign_convention: forward NEGATIVE net payout; reverse POSITIVE recovery/refund effect.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: settlement_date
  data_type: varchar
  description: '**Settlement date** (stored as varchar; format: `2025-09-25`)'
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.date
  confidence: high
  review_status: ready_with_caveat
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.settlement_date
  data_quality_notes:
  - Stored as varchar in source; cast to DATE for date filters.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: settlement_date_temp_old
  data_type: date
  description: Legacy properly-typed settlement date
  semantic_role: date
  is_key: false
  is_amount: false
  is_date: true
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.date
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.settlement_date_temp_old
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: settlement_id
  data_type: varchar
  description: '**Settlement batch ID** (numeric, e.g., `2200165328`) — groups multiple orders into one payout'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.settlement_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: sgst_ugst
  data_type: decimal
  description: SGST/UGST on commission
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.tax_accounting
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.sgst_ugst
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: shipping_fees
  data_type: decimal
  description: Shipping fees (all zero — included in commission)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.shipping_fees
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: slave
  data_type: varchar
  description: 'Warehouse code (format: `{seller_code}-{warehouse_code}`, e.g., `126957-GWSS1`)'
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: true
  scope_note: Scope-like identifier retained as a column/filter only; do not derive tenant/group/platform-account/logistics/account
    cards.
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.slave
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: tds_on_e_commerce_operations
  data_type: decimal
  description: Duplicate of `total_tds`
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.tds_on_e_commerce_operations
  sign_convention: duplicate of total_tds with same sign semantics.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: total_fees_receivable
  data_type: decimal
  description: Total fees receivable by TataCliq
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.total_fees_receivable
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: total_seller_payable_temp_old
  data_type: decimal
  description: Legacy total payable field
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  scope_note: Scope-like field retained as column only; no tenant/group/account card emitted.
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.total_seller_payable_temp_old
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: total_tds
  data_type: decimal
  description: TDS under Section 194-O
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.total_tds
  sign_convention: forward POSITIVE deduction; reverse NEGATIVE reversal.
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: transaction_id
  data_type: varchar
  description: Individual transaction reference (= `order_id` typically)
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.transaction_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: transaction_type
  data_type: varchar
  description: '`forward` (sale) or `reverse` (return/refund)'
  semantic_role: status_or_classification
  is_key: false
  is_amount: false
  is_date: false
  is_status: true
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.classification
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.transaction_type
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: tul_discount
  data_type: decimal
  description: Discount funded by TUL (TataCliq)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.tul_discount
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: txn_uuid
  data_type: varchar
  description: Pipeline UUID
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.txn_uuid
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: unique_id
  data_type: integer
  description: Row identifier
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.unique_id
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: unique_id_1
  data_type: integer
  description: Legacy unique ID
  semantic_role: key
  is_key: true
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.unique_id_1
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: unique_value
  data_type: varchar
  description: Dedup hash
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.identity
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.unique_value
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: zen_sheet_name
  data_type: varchar
  description: Source sheet
  semantic_role: attribute
  is_key: false
  is_amount: false
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.system
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.zen_sheet_name
```


```yaml
candidate_card:
  table_id: table.zs_observe.tatacliq_settlement
  schema: zs_observe
  table_name: tatacliq_settlement
  column_name: zen_vendor_payout_commission_fee
  data_type: decimal
  description: ZenStatement-computed commission fee (NULL)
  semantic_role: amount
  is_key: false
  is_amount: true
  is_date: false
  is_status: false
  is_scope_field: false
  evidence_refs:
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
  card_type: column
  card_id: column.zs_observe.tatacliq_settlement.zen_vendor_payout_commission_fee
```


### 4.6 relationship


```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.tatacliq.oms_settlement.order_id
  display_name: TataCliq OMS ↔ Settlement order_id join
  source_table_id: table.zs_observe.tatacliq_oms
  target_table_id: table.zs_observe.tatacliq_settlement
  relationship_type: marketplace_internal_join
  join_keys:
  - order_id
  join_condition: tatacliq_oms.order_id = tatacliq_settlement.order_id
  coverage: 10,110 / 12,998 = 77.8% for documented forward comparison
  grain_warning: Pre-aggregate or filter settlement many-side rows before analytical joins where required by query intent.
  invalid_join_warning: document_number = parent_id has 0% coverage in current data and must not be used as a relationship.
  evidence_refs:
  - ev.tatacliq.join.coverage
  confidence: high
  review_status: ready
```


### 4.7 value_profile


```yaml
candidate_card:
  card_id: value_profile.tatacliq.brands
  display_name: TataCliq brand dataset profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.brand
  profile_kind: observed_brand_distribution
  observed_values:
  - High Star
  - Ishin
  - Lilpicks
  - Dennis Lingo
  - Anubhutee
  - Hubberholme
  distribution_summary: Forward structured-row brand distribution with GMV, average price, categories/source states, and HSN
    counts.
  evidence_refs:
  - ev.tatacliq.brands.dataset
  - ev.tatacliq.values.oms.brand_distribution
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.seller_gstin_warehouse
  display_name: TataCliq seller GSTIN to warehouse profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.seller_gstin
  profile_kind: mapping_profile
  observed_values:
  - 29AAOCM5326J1ZY -> Karnataka / 126957-BLSS1
  - 27AAOCM5326J1Z2 -> Maharashtra / 126957-BHSS1
  - 06AAOCM5326J1Z6 -> Haryana / 126957-GWSS1
  - 19AAOCM5326J1ZZ -> West Bengal / 126957-WBSS1
  distribution_summary: Four seller GSTINs map to dispatch warehouse/slave codes.
  evidence_refs:
  - ev.tatacliq.warehouse.gstin
  - ev.tatacliq.values.oms.seller_gstin_warehouse
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.ecommerce_gstin
  display_name: TataCliq e-commerce GSTIN profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
  profile_kind: scope_identifier_value_profile
  observed_values:
  - 33 distinct Tata Unistore Limited GSTINs
  - format {state_code}AACCT7290E1C{check}
  distribution_summary: Selected based on place_of_supply destination state code; retain as source identifier only.
  evidence_refs:
  - ev.tatacliq.ecom.gstin
  - ev.tatacliq.values.oms.ecom_gstin
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.transaction_document_type
  display_name: TataCliq OMS transaction_type/document_type profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.transaction_type
  profile_kind: document_status_profile
  observed_values:
  - forward + Invoice
  - reverse + Credit Note
  - forward + NULL shifted rows
  - reverse + NULL shifted rows
  distribution_summary: OMS forward invoices, reverse credit notes, and shifted-row NULL document types.
  evidence_refs:
  - ev.tatacliq.values.oms.transaction_document
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.place_of_supply
  display_name: TataCliq OMS place_of_supply profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.place_of_supply
  profile_kind: geographic_code_profile
  observed_values:
  - state codes 01-37 observed
  distribution_summary: Pan-India destination state codes; used to select TataCliq e-commerce GSTIN and tax type.
  evidence_refs:
  - ev.tatacliq.values.oms.place_of_supply
  - ev.tatacliq.tax.product_gst
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.gst_rates
  display_name: TataCliq OMS GST rate profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.tax_igst_rate
  profile_kind: tax_rate_profile
  observed_values:
  - 0%
  - 5%
  - 12%
  - 18%
  - 'CGST/SGST: 2.5%+2.5% or 6%+6%'
  distribution_summary: 'Apparel GST rule: 5% when MRP <= 1000, 12% when MRP > 1000; 18% for services/other items.'
  evidence_refs:
  - ev.tatacliq.tax.product_gst
  - ev.tatacliq.values.oms.gst_rates
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.oms.hsn_codes
  display_name: TataCliq OMS HSN code profile
  table_id: table.zs_observe.tatacliq_oms
  column_id: column.zs_observe.tatacliq_oms.hsn_code
  profile_kind: hsn_category_profile
  observed_values:
  - 6206xxxx
  - 6211xxxx
  - 6204xxxx
  - 6205xxxx
  - 6103/6104xxxx
  - '6091000'
  - 6307xxxx
  - 6306xxxx
  - 5207/5408xxxx
  distribution_summary: Sample of 51 total HSN codes across apparel and textile categories.
  evidence_refs:
  - ev.tatacliq.values.oms.hsn_codes
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.settlement.transaction_breakdown
  display_name: TataCliq settlement transaction/order/fulfilment profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.transaction_type
  profile_kind: settlement_distribution_profile
  observed_values:
  - forward/PREPAID/TSHIP-HD/NOR
  - reverse/PREPAID/TSHIP-HD/RRF
  - forward/POSTPAID/TSHIP-HD/NOR
  - reverse/POSTPAID/TSHIP-HD/RRF
  - forward/PREPAID/TSHIP-ED/NOR
  - reverse/PREPAID/TSHIP-ED/RRF
  distribution_summary: Settlement distribution by transaction_type, order_type, fulfilment_channel, and order_tag.
  evidence_refs:
  - ev.tatacliq.values.settlement.breakdown
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.settlement.order_tag
  display_name: TataCliq settlement order_tag profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.order_tag
  profile_kind: status_value_profile
  observed_values:
  - NOR = Normal order / forward sale
  - RRF = Return to Fulfilment Centre / reverse return
  distribution_summary: Order_tag differentiates normal forward sales from RRF reverse returns.
  evidence_refs:
  - ev.tatacliq.values.settlement.order_tag
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.settlement.fulfilment_channel
  display_name: TataCliq TSHIP fulfilment channel profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
  profile_kind: fulfilment_label_profile
  observed_values:
  - TSHIP/HD = Home Delivery / standard
  - TSHIP/ED = Express Delivery / faster premium
  distribution_summary: Fulfilment labels only; not process variants by themselves.
  evidence_refs:
  - ev.tatacliq.fulfilment.tship
  - ev.tatacliq.values.settlement.fulfilment_channel
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.settlement.order_type
  display_name: TataCliq order_type profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.order_type
  profile_kind: payment_label_profile
  observed_values:
  - PREPAID = online payment
  - POSTPAID = pay on delivery / credit-backed payment
  distribution_summary: Payment labels retained as values; do not create payment-gateway account cards.
  evidence_refs:
  - ev.tatacliq.order.types
  - ev.tatacliq.values.settlement.order_type
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.settlement.batch_structure
  display_name: TataCliq settlement batch structure profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.settlement_id
  profile_kind: batch_profile
  observed_values:
  - 54 distinct settlement IDs
  - each covers 1-14 days
  - settlements appear weekly
  distribution_summary: Settlement_id groups multiple orders into payout batches.
  evidence_refs:
  - ev.tatacliq.values.settlement.batch_structure
  card_type: value_profile
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: value_profile.tatacliq.scope.group_level_id_22
  display_name: TataCliq documented scope identifier profile
  table_id: table.zs_observe.tatacliq_settlement
  column_id: column.zs_observe.tatacliq_settlement.group_level_id
  profile_kind: scope_identifier_profile
  observed_values:
  - group_level_id = 22
  distribution_summary: Documented source filter/scope value only; runtime account binding is external.
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  - ev.tatacliq.tables.summary
  card_type: value_profile
  confidence: high
  review_status: ready
```


### 4.8 metric


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.forward_gmv
  display_name: Total Forward GMV
  business_definition: Gross merchandise value of forward settlement rows using ABS(charged_amount).
  metric_family: revenue
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.orders
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  confidence: high
  review_status: ready
  observed_source_value: ₹1.70 Cr forward GMV; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.return_rate
  display_name: Return Rate
  business_definition: Count of reverse rows divided by count of forward rows in settlement.
  metric_family: returns
  default_grain: source_query_defined_grain
  default_unit: percent
  higher_is_better: null
  domain_id: domain.tatacliq.returns
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.return_rate
  confidence: high
  review_status: ready
  observed_source_value: 5,464 returns / 14,884 sales = 36.7%; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.average_order_value
  display_name: AOV from OMS Clean Rows
  business_definition: Average OMS charged_amount for structured forward invoice rows by brand.
  metric_family: revenue
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.orders
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.aov_oms_clean
  confidence: high
  review_status: ready
  observed_source_value: Ishin highest AOV ₹2,135; Lilpicks lowest ₹835; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.net_revenue_after_returns
  display_name: Net Revenue After Returns
  business_definition: Net revenue from settlement by summing forward and reverse settled_amount using TataCliq sign convention.
  metric_family: revenue
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.orders
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.net_revenue_after_returns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.monthly_settlement_summary
  display_name: Monthly Settlement Trend
  business_definition: Monthly line item count, gross GMV, commission, TDS, and net settled from settlement forward rows.
  metric_family: settlement
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.settlement
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.monthly_settlement_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.brand_gmv
  display_name: Brand GMV from OMS
  business_definition: Brand-level GMV/AOV/HSN count for structured forward OMS rows.
  metric_family: revenue
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.orders
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.brand_gmv_oms
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.commission_rate
  display_name: Commission / Take Rate
  business_definition: Gross commission divided by ABS(forward charged_amount); referral rate uses referral_fees as numerator.
  metric_family: fees
  default_grain: source_query_defined_grain
  default_unit: percent
  higher_is_better: null
  domain_id: domain.tatacliq.fees
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.commission_rate_validation
  confidence: high
  review_status: ready
  observed_source_value: ~41.43% gross commission rate; ~35.1% referral fee rate; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.seller_realization_rate
  display_name: Seller Realization / Payout Ratio
  business_definition: ABS(settled_amount) divided by ABS(charged_amount) for forward settlement rows or batch net payout
    versus forward GMV.
  metric_family: settlement
  default_grain: source_query_defined_grain
  default_unit: percent
  higher_is_better: null
  domain_id: domain.tatacliq.settlement
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  confidence: high
  review_status: ready
  observed_source_value: ~58.5% payout ratio; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.settlement_batch_completeness
  display_name: Settlement Batch Completeness
  business_definition: Batch-level line item count, distinct order count, GMV, commission, net settled, and TDS.
  metric_family: settlement
  default_grain: source_query_defined_grain
  default_unit: mixed
  higher_is_better: null
  domain_id: domain.tatacliq.settlement
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.tds_deducted
  display_name: TDS Deducted
  business_definition: TDS amounts from total_tds/tds_on_e_commerce_operations, positive forward and negative reverse.
  metric_family: tax
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.tax
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.tax.tds
  confidence: high
  review_status: ready
  observed_source_value: Total TDS Mar-Sep 2025 ₹15,578.45; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.effective_tds_rate
  display_name: Effective TDS Rate
  business_definition: Forward total_tds divided by forward ABS(charged_amount).
  metric_family: tax
  default_grain: source_query_defined_grain
  default_unit: percent
  higher_is_better: null
  domain_id: domain.tatacliq.tax
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
  observed_source_value: ~0.1% consistently; guidance only
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.return_impact
  display_name: Return Impact Analysis
  business_definition: Settlement impact by order_tag and transaction_type including GMV, commission, TUL discount, and net
    settled.
  metric_family: returns
  default_grain: source_query_defined_grain
  default_unit: mixed
  higher_is_better: null
  domain_id: domain.tatacliq.returns
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.return_impact_analysis
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.monthly_financial_waterfall
  display_name: Monthly Financial Waterfall
  business_definition: Monthly forward GMV, forward commission/GST/TDS, forward net, return net, and total net.
  metric_family: settlement
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.settlement
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.monthly_financial_waterfall
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.monthly_gmv
  display_name: Monthly OMS GMV Trend
  business_definition: Monthly OMS document count, GMV, IGST, and CGST+SGST by transaction_type.
  metric_family: revenue
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.orders
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.oms_monthly_gmv_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.product_gst_amount
  display_name: Product GST Amount
  business_definition: OMS IGST/CGST/SGST amounts by inter-state versus intra-state tax type.
  metric_family: tax
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.tax
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.oms_intra_inter_state_gst
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.hsn_distribution
  display_name: HSN Distribution
  business_definition: Top HSN/brand combinations with count, GMV, and average IGST rate.
  metric_family: mapping_enrichment
  default_grain: source_query_defined_grain
  default_unit: mixed
  higher_is_better: null
  domain_id: domain.tatacliq.mapping_enrichment
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.sql.oms_hsn_distribution
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric
  card_id: metric.tatacliq.tcs_collected
  display_name: TCS Collected
  business_definition: Marketplace-side TCS semantic noted in source but not visible in OMS or settlement columns.
  metric_family: tax
  default_grain: source_query_defined_grain
  default_unit: INR
  higher_is_better: null
  domain_id: domain.tatacliq.tax
  benchmark_policy: guidance_only_not_hard_validation
  evidence_refs:
  - ev.tatacliq.tax.tcs_absent
  confidence: high
  review_status: ready_with_source_gap
  implementation_status: unavailable_in_source_tables; preserve as caveat/review, not executable implementation
```


### 4.9 metric_implementation


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.total_forward_gmv
  metric_id: metric.tatacliq.forward_gmv
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — forward gmv
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - charged_amount
  - gross_commission
  - referral_fees
  - gross_commission_gst_amount
  - total_tds
  - settled_amount
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.total_forward_gmv
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.return_rate
  metric_id: metric.tatacliq.return_rate
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — return rate
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.return_rate
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.aov_oms_clean
  metric_id: metric.tatacliq.average_order_value
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — average order value
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - brand
  - charged_amount
  - transaction_type
  - seller_name
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.aov_oms_clean
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.aov_oms_clean
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.net_revenue_after_returns
  metric_id: metric.tatacliq.net_revenue_after_returns
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — net revenue after returns
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settled_amount
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.net_revenue_after_returns
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.net_revenue_after_returns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.monthly_settlement_trend
  metric_id: metric.tatacliq.monthly_settlement_summary
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — monthly settlement summary
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - charged_amount
  - gross_commission
  - total_tds
  - settled_amount
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.monthly_settlement_trend
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.monthly_settlement_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.brand_gmv_oms
  metric_id: metric.tatacliq.brand_gmv
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — brand gmv
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - brand
  - charged_amount
  - hsn_code
  - transaction_type
  - seller_name
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.brand_gmv_oms
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.brand_gmv_oms
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.commission_rate_validation
  metric_id: metric.tatacliq.commission_rate
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — commission rate
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - charged_amount
  - gross_commission
  - referral_fees
  - gross_commission_gst_amount
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.commission_rate_validation
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.commission_rate_validation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.settlement_batch_completeness
  metric_id: metric.tatacliq.settlement_batch_completeness
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — settlement batch completeness
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_id
  - settlement_date
  - order_id
  - charged_amount
  - gross_commission
  - settled_amount
  - total_tds
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.settlement_batch_completeness
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.seller_realization_batch_summary
  metric_id: metric.tatacliq.seller_realization_rate
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — seller realization rate
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - settlement_id
  - transaction_type
  - charged_amount
  - gross_commission
  - total_tds
  - settled_amount
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.settlement.batch_payout_summary
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_payout_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.monthly_financial_waterfall
  metric_id: metric.tatacliq.monthly_financial_waterfall
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — monthly financial waterfall
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - transaction_type
  - charged_amount
  - gross_commission
  - gross_commission_gst_amount
  - total_tds
  - settled_amount
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.settlement.monthly_financial_waterfall
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.monthly_financial_waterfall
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.return_impact_analysis
  metric_id: metric.tatacliq.return_impact
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — return impact
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - order_tag
  - transaction_type
  - charged_amount
  - gross_commission
  - tul_discount
  - settled_amount
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.settlement.return_impact_analysis
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.return_impact_analysis
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.tds_reconciliation
  metric_id: metric.tatacliq.effective_tds_rate
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — effective tds rate
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - transaction_type
  - total_tds
  - charged_amount
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.tds_reconciliation
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.tds_summary
  metric_id: metric.tatacliq.tds_deducted
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — tds deducted
  source_tables:
  - zs_observe.tatacliq_settlement
  source_columns:
  - settlement_date
  - transaction_type
  - total_tds
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.settlement.tds_summary
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.tds_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.oms_monthly_gmv_trend
  metric_id: metric.tatacliq.monthly_gmv
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — monthly gmv
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - created_date
  - transaction_type
  - charged_amount
  - tax_igst_amount
  - tax_cgst_amount
  - tax_sgst_amount
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.oms.monthly_gmv_trend
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.oms_monthly_gmv_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.oms_brand_level_performance
  metric_id: metric.tatacliq.brand_gmv
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — brand gmv
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - brand
  - charged_amount
  - tax_igst_amount
  - tax_cgst_amount
  - tax_sgst_amount
  - transaction_type
  - seller_name
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.oms.brand_level_performance
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.oms_brand_level_performance
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.oms_intra_inter_state_gst
  metric_id: metric.tatacliq.product_gst_amount
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — product gst amount
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - tax_igst_rate
  - charged_amount
  - tax_igst_amount
  - tax_cgst_amount
  - tax_sgst_amount
  - transaction_type
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.oms.intra_inter_state_gst
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.oms_intra_inter_state_gst
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_impl.tatacliq.oms_hsn_distribution
  metric_id: metric.tatacliq.hsn_distribution
  platform_context_id: platform_context.tatacliq.in
  display_name: TataCliq SQL implementation — hsn distribution
  source_tables:
  - zs_observe.tatacliq_oms
  source_columns:
  - hsn_code
  - brand
  - charged_amount
  - tax_igst_rate
  - transaction_type
  - seller_name
  - is_active
  formula_text: Executable SQL pattern referenced by sql_ref; see SQL Pattern Registry.
  sql_ref: sql.tatacliq.oms.hsn_distribution
  filters: Use source SQL filters exactly; group_level_id scope filters remain column filters, not account bindings.
  grain: as specified in source SQL
  sign_convention: Preserve TataCliq settlement sign convention; use ABS only where source SQL does.
  aggregation_order: Aggregate at source SQL grain before joining or comparing amounts.
  evidence_refs:
  - ev.tatacliq.sql.oms_hsn_distribution
  confidence: high
  review_status: ready
```


### 4.10 formula_template


```yaml
candidate_card:
  card_id: formula_template.tatacliq.payout_calculation
  display_name: TataCliq payout calculation formula
  formula_text: Net Settled = |Charged Amount| - Gross Commission - TDS = |Charged Amount| - (Referral Fee + 18% GST on Referral
    Fee) - 0.1% TDS
  parameters:
  - charged_amount
  - gross_commission
  - referral_fees
  - gross_commission_gst_amount
  - total_tds
  unit: INR
  sign_convention: For settlement rows, forward charged_amount/settled_amount are negative; source formula presents absolute
    seller payout.
  evidence_refs:
  - ev.tatacliq.payout.calculation
  card_type: formula_template
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: formula_template.tatacliq.settlement_waterfall
  display_name: TataCliq settlement debit-model waterfall
  formula_text: settled_amount ≈ charged_amount + gross_commission + total_tds; forward rows are debit-model negative payouts,
    reverse rows positive recoveries.
  parameters:
  - charged_amount
  - gross_commission
  - total_tds
  - settled_amount
  unit: INR
  sign_convention: Do not invert signs globally; interpret by transaction_type.
  evidence_refs:
  - ev.tatacliq.settlement.waterfall
  card_type: formula_template
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: formula_template.tatacliq.commission_rate
  display_name: TataCliq commission rate formula
  formula_text: Forward Commission Rate = SUM(forward gross_commission) / SUM(ABS(forward charged_amount)); referral rate
    uses SUM(referral_fees) numerator.
  parameters:
  - gross_commission
  - referral_fees
  - charged_amount
  - transaction_type
  unit: percent
  sign_convention: Use ABS(charged_amount) for forward settlement GMV.
  evidence_refs:
  - ev.tatacliq.sql.commission_rate_validation
  - ev.tatacliq.settlement.waterfall
  card_type: formula_template
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: formula_template.tatacliq.return_rate
  display_name: TataCliq return rate formula
  formula_text: Return Rate = COUNT_IF(transaction_type = reverse) / COUNT_IF(transaction_type = forward) on active settlement
    rows.
  parameters:
  - transaction_type
  - is_active
  unit: percent
  sign_convention: Count-based metric; no amount sign normalization required.
  evidence_refs:
  - ev.tatacliq.sql.return_rate
  card_type: formula_template
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_id: formula_template.tatacliq.tds_effective_rate
  display_name: TataCliq effective TDS rate formula
  formula_text: Effective TDS Rate = SUM(forward total_tds) / SUM(forward ABS(charged_amount)); reverse rows reverse TDS impact.
  parameters:
  - total_tds
  - charged_amount
  - transaction_type
  unit: percent
  sign_convention: TDS positive for forward deduction and negative for reverse reversal.
  evidence_refs:
  - ev.tatacliq.tax.tds
  - ev.tatacliq.sql.tds_reconciliation
  card_type: formula_template
  confidence: high
  review_status: ready
```


### 4.11 metric_dependency


```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.tatacliq.average_order_value
  parent_metric_id: metric.tatacliq.average_order_value
  dependent_metric_ids:
  - SUM(charged_amount)
  - COUNT(*)
  dependency_type: ratio_or_average
  calculation_order: Compute count and sum at requested brand/period grain before averaging.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.sql.return_rate
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.tatacliq.return_rate
  parent_metric_id: metric.tatacliq.return_rate
  dependent_metric_ids:
  - COUNT_IF(reverse)
  - COUNT_IF(forward)
  dependency_type: ratio
  calculation_order: Compute return and sales counts from active settlement rows before division.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.sql.return_rate
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.tatacliq.commission_rate
  parent_metric_id: metric.tatacliq.commission_rate
  dependent_metric_ids:
  - SUM(gross_commission)
  - SUM(ABS(charged_amount))
  dependency_type: ratio
  calculation_order: Filter to forward rows before ratio calculation.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.sql.return_rate
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.tatacliq.seller_realization_rate
  parent_metric_id: metric.tatacliq.seller_realization_rate
  dependent_metric_ids:
  - SUM(ABS(settled_amount))
  - SUM(ABS(charged_amount))
  dependency_type: ratio
  calculation_order: Use forward rows for payout ratio unless batch query includes returns explicitly.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.sql.return_rate
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.tatacliq.effective_tds_rate
  parent_metric_id: metric.tatacliq.effective_tds_rate
  dependent_metric_ids:
  - SUM(forward total_tds)
  - SUM(forward ABS(charged_amount))
  dependency_type: ratio
  calculation_order: Forward rows determine effective TDS rate; reverse rows quantify reversal impact separately.
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.sql.return_rate
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


### 4.12 business_process


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.tatacliq.forward_sale_flow
  display_name: TataCliq Forward Sale Flow
  process_family: marketplace_transaction_lifecycle
  description: Forward order appears in OMS as invoice, is shipped via TSHIP/slave_id, then settles weekly in tatacliq_settlement
    with forward sign convention.
  entry_condition: Customer places order on TataCliq app/website.
  exit_condition: Forward settlement row has transaction_type=forward, order_tag=NOR, and settled_amount interpreted as net
    payout by absolute value.
  source_tables:
  - zs_observe.tatacliq_oms
  - zs_observe.tatacliq_settlement
  state_fields:
  - transaction_type
  - document_type
  - order_tag
  - charged_amount
  - gross_commission
  - settled_amount
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.tatacliq.return_flow
  display_name: TataCliq Return Flow
  process_family: marketplace_transaction_lifecycle
  description: Return is represented as OMS reverse/Credit Note and settlement reverse/RRF row with refund credit, commission
    reversal, and positive recovery from next payout.
  entry_condition: Customer initiates return; TataCliq logistics picks up RRF return.
  exit_condition: Reverse settlement row has transaction_type=reverse, order_tag=RRF, and settled_amount positive as recovery/refund
    impact.
  source_tables:
  - zs_observe.tatacliq_oms
  - zs_observe.tatacliq_settlement
  state_fields:
  - transaction_type
  - document_type
  - order_tag
  - charged_amount
  - gross_commission
  - settled_amount
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.tatacliq.marketplace_internal_reconciliation
  display_name: TataCliq marketplace-internal reconciliation
  process_family: marketplace_internal_reconciliation
  description: Source-backed reconciliation between OMS invoices/credit notes and settlement rows using order_id and amount
    comparison.
  source_tables:
  - zs_observe.tatacliq_oms
  - zs_observe.tatacliq_settlement
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.sql.recon_oms_settlement
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


### 4.13 workflow_step


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.forward_sale_flow.01
  process_id: business_process.tatacliq.forward_sale_flow
  step_order: 1
  display_name: OMS invoice creation
  description: Order appears in zs_observe.tatacliq_oms with transaction_type=forward and document_type=Invoice; seller GSTIN
    and gstin_of_e_com are assigned from dispatch/destination context.
  input_tables:
  - zs_observe.tatacliq_oms
  status_conditions:
  - transaction_type=forward
  - document_type=Invoice
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.forward_sale_flow.02
  process_id: business_process.tatacliq.forward_sale_flow
  step_order: 2
  display_name: Warehouse and TSHIP dispatch
  description: Mensa dispatches from slave_id warehouse; source describes TSHIP courier pickup and no separate fulfilment
    fee.
  input_tables:
  - zs_observe.tatacliq_oms
  status_conditions:
  - slave_id is populated where structured
  - fulfilment_channel represented in settlement
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.forward_sale_flow.03
  process_id: business_process.tatacliq.forward_sale_flow
  step_order: 3
  display_name: Weekly settlement row creation
  description: Settlement cycle creates zs_observe.tatacliq_settlement rows with transaction_type=forward and order_tag=NOR.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - transaction_type=forward
  - order_tag=NOR
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.forward_sale_flow.04
  process_id: business_process.tatacliq.forward_sale_flow
  step_order: 4
  display_name: Forward settlement signs captured
  description: For forward settlement rows, charged_amount is NEGATIVE, gross_commission is POSITIVE, and settled_amount is
    NEGATIVE.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - charged_amount<0
  - gross_commission>0
  - settled_amount<0
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.forward_sale_flow.05
  process_id: business_process.tatacliq.forward_sale_flow
  step_order: 5
  display_name: Payout interpretation
  description: Use ABS(settled_amount) as seller payout value; do not create bank-account cards from the bank-credit mention.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - ABS(settled_amount) for payout reporting
  evidence_refs:
  - ev.tatacliq.lifecycle.forward
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.return_flow.01
  process_id: business_process.tatacliq.return_flow
  step_order: 1
  display_name: Return pickup and RRF context
  description: Customer return is picked up by TataCliq logistics; settlement return context uses order_tag=RRF.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - order_tag=RRF
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.return_flow.02
  process_id: business_process.tatacliq.return_flow
  step_order: 2
  display_name: OMS credit note creation
  description: Return appears in zs_observe.tatacliq_oms with transaction_type=reverse and document_type=Credit Note.
  input_tables:
  - zs_observe.tatacliq_oms
  status_conditions:
  - transaction_type=reverse
  - document_type=Credit Note
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.return_flow.03
  process_id: business_process.tatacliq.return_flow
  step_order: 3
  display_name: Reverse settlement row creation
  description: Return appears in zs_observe.tatacliq_settlement with transaction_type=reverse and order_tag=RRF.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - transaction_type=reverse
  - order_tag=RRF
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.tatacliq.return_flow.04
  process_id: business_process.tatacliq.return_flow
  step_order: 4
  display_name: Reverse settlement signs captured
  description: For reverse rows, charged_amount is POSITIVE refund credit, gross_commission is NEGATIVE reversal, and settled_amount
    is POSITIVE recovery from seller next payout.
  input_tables:
  - zs_observe.tatacliq_settlement
  status_conditions:
  - charged_amount>0
  - gross_commission<0
  - settled_amount>0
  evidence_refs:
  - ev.tatacliq.lifecycle.return
  confidence: high
  review_status: ready
```


### 4.14 reconciliation_profile


```yaml
candidate_card:
  card_type: reconciliation_profile
  process_id: business_process.tatacliq.marketplace_internal_reconciliation
  reconciliation_family: marketplace_internal_reconciliation
  confidence: high
  review_status: ready
  card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  display_name: TataCliq OMS ↔ Settlement Forward Reconciliation
  expected_side: OMS forward invoice charged_amount
  actual_side: Settlement forward ABS(charged_amount)
  unit_id: reconciliation_unit.tatacliq.order_id
  matching_logic_id: matching_logic.tatacliq.oms_settlement_forward
  tolerance: price variance status uses > 1 as explicit source SQL threshold
  timing_window: Settlement data ends Sep 2025; Q4 OMS rows require settlement_date < 2025-10-01 comparison window when periods
    must match.
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  - ev.tatacliq.join.coverage
```


```yaml
candidate_card:
  card_type: reconciliation_profile
  process_id: business_process.tatacliq.marketplace_internal_reconciliation
  reconciliation_family: marketplace_internal_reconciliation
  confidence: high
  review_status: ready
  card_id: reconciliation_profile.tatacliq.return_oms_settlement
  display_name: TataCliq Return OMS ↔ Settlement Match
  expected_side: OMS reverse credit note charged_amount
  actual_side: Settlement reverse charged_amount
  unit_id: reconciliation_unit.tatacliq.return_order_id
  matching_logic_id: matching_logic.tatacliq.return_oms_settlement
  tolerance: source query computes value_variance but does not define a pass/fail threshold
  timing_window: Use source-documented return/settlement availability; no external logistics/bank timing card.
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
```


### 4.15 reconciliation_side


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.tatacliq.oms_settlement_forward.expected
  profile_id: reconciliation_profile.tatacliq.oms_settlement_forward
  side_role: expected
  source_table_id: table.zs_observe.tatacliq_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  filters:
  - transaction_type=forward
  - seller_name IS NOT NULL
  - is_active=true
  grain: order_id line/order comparison as defined by source SQL
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.tatacliq.oms_settlement_forward.actual
  profile_id: reconciliation_profile.tatacliq.oms_settlement_forward
  side_role: actual
  source_table_id: table.zs_observe.tatacliq_settlement
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  - gross_commission
  - referral_fees
  - gross_commission_gst_amount
  - total_tds
  - settled_amount
  filters:
  - transaction_type=forward
  - is_active=true
  grain: order_id line/order comparison as defined by source SQL
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.tatacliq.return_oms_settlement.expected
  profile_id: reconciliation_profile.tatacliq.return_oms_settlement
  side_role: expected
  source_table_id: table.zs_observe.tatacliq_oms
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  filters:
  - transaction_type=reverse
  - is_active=true
  grain: order_id line/order comparison as defined by source SQL
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.tatacliq.return_oms_settlement.actual
  profile_id: reconciliation_profile.tatacliq.return_oms_settlement
  side_role: actual
  source_table_id: table.zs_observe.tatacliq_settlement
  key_columns:
  - order_id
  amount_columns:
  - charged_amount
  - gross_commission
  - settled_amount
  filters:
  - transaction_type=reverse
  - is_active=true
  grain: order_id line/order comparison as defined by source SQL
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


### 4.16 reconciliation_unit


```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.tatacliq.order_id
  display_name: TataCliq forward reconciliation order_id unit
  unit_type: marketplace_order
  unit_keys:
  - order_id
  grain: OMS order_id compared to settlement order_id after source filters
  aggregation_rule: Use source query grain; pre-aggregate settlement if many-side duplicates would affect downstream analytics.
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.tatacliq.return_order_id
  display_name: TataCliq return reconciliation order_id unit
  unit_type: marketplace_return_order
  unit_keys:
  - order_id
  grain: OMS reverse order_id compared to settlement reverse order_id
  aggregation_rule: Use source query grain; pre-aggregate settlement if many-side duplicates would affect downstream analytics.
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


### 4.17 matching_logic


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.tatacliq.oms_settlement_forward
  display_name: TataCliq matching logic — OMS settlement forward
  match_type: left_join_key_and_amount_status
  join_condition: o.order_id = s.order_id AND s.is_active = true AND s.transaction_type = forward
  key_normalization: Use order_id exactly; document_number/parent_id is forbidden because coverage is 0%.
  amount_comparison: ABS(o.charged_amount - ABS(s.charged_amount)) AS price_variance
  tolerance_rule: Source query classifies Price Variance when variance > 1.
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  - ev.tatacliq.join.coverage
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.tatacliq.return_oms_settlement
  display_name: TataCliq matching logic — return OMS settlement
  match_type: left_join_key_and_amount_variance
  join_condition: o.order_id = s.order_id AND s.is_active = true AND s.transaction_type = reverse
  key_normalization: Use order_id exactly.
  amount_comparison: ABS(o.charged_amount - s.charged_amount) AS value_variance
  tolerance_rule: No pass/fail threshold documented; keep review item open for operational threshold if needed.
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready_with_caveat
```


### 4.18 mismatch_category


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.tatacliq.oms_settlement_forward.not_in_settlement
  display_name: Not In Settlement
  profile_id: reconciliation_profile.tatacliq.oms_settlement_forward
  mismatch_type: not_in_settlement
  detection_logic: s.order_id IS NULL
  business_meaning: OMS invoice lacks settlement row, especially Oct-Dec 2025 gap if periods are not aligned
  review_priority: high
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.tatacliq.oms_settlement_forward.price_variance
  display_name: Price Variance
  profile_id: reconciliation_profile.tatacliq.oms_settlement_forward
  mismatch_type: price_variance
  detection_logic: ABS(o.charged_amount - ABS(s.charged_amount)) > 1
  business_meaning: OMS invoice amount differs from settlement charged amount beyond source SQL threshold
  review_priority: high
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.tatacliq.return_oms_settlement.missing_reverse_settlement
  display_name: Missing Reverse Settlement
  profile_id: reconciliation_profile.tatacliq.return_oms_settlement
  mismatch_type: missing_reverse_settlement
  detection_logic: s.order_id IS NULL after reverse settlement left join
  business_meaning: OMS credit note lacks reverse settlement row
  review_priority: high
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.tatacliq.return_oms_settlement.value_variance
  display_name: Value Variance
  profile_id: reconciliation_profile.tatacliq.return_oms_settlement
  mismatch_type: return_value_variance
  detection_logic: ABS(o.charged_amount - s.charged_amount) is non-zero; threshold not specified
  business_meaning: Return OMS credit note value differs from settlement return value
  review_priority: medium
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready_with_caveat
```


### 4.19 query_pattern


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.total_forward_gmv
  display_name: TataCliq query pattern — 6.1 Total Forward GMV
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.forward_gmv
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.total_forward_gmv
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.return_rate
  display_name: TataCliq query pattern — 6.2 Return Rate
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.return_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.return_rate
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.return_rate
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.aov_oms_clean
  display_name: TataCliq query pattern — 6.3 AOV from OMS (Clean Rows)
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.average_order_value
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.aov_oms_clean
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.aov_oms_clean
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.net_revenue_after_returns
  display_name: TataCliq query pattern — 6.4 Net Revenue After Returns
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.net_revenue_after_returns
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.net_revenue_after_returns
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.net_revenue_after_returns
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.monthly_settlement_trend
  display_name: TataCliq query pattern — 6.5 Monthly Settlement Trend
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.monthly_settlement_summary
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.monthly_settlement_trend
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.monthly_settlement_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.brand_gmv_oms
  display_name: TataCliq query pattern — 6.6 Brand GMV from OMS
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.brand_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.brand_gmv_oms
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.brand_gmv_oms
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.recon_oms_settlement
  display_name: TataCliq query pattern — 7.1 OMS ↔ Settlement Reconciliation
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - reconciliation_profile.tatacliq.oms_settlement_forward
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.recon_oms_settlement
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.reconciliation_status
  evidence_refs:
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.recon_return_oms_settlement
  display_name: TataCliq query pattern — 7.2 Return OMS ↔ Settlement Match
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - reconciliation_profile.tatacliq.return_oms_settlement
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.recon_return_oms_settlement
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.reconciliation_status
  evidence_refs:
  - ev.tatacliq.sql.recon_return_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.commission_rate_validation
  display_name: TataCliq query pattern — 7.3 Commission Rate Validation
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.commission_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.commission_rate_validation
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.commission_rate_validation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement_batch_completeness
  display_name: TataCliq query pattern — 7.4 Settlement Batch Completeness
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.settlement_batch_completeness
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement_batch_completeness
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.tds_reconciliation
  display_name: TataCliq query pattern — 7.5 TDS Reconciliation
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.effective_tds_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.tds_reconciliation
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.tds_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.mandatory_query_filters
  display_name: TataCliq query pattern — 9. Mandatory Query Filters
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - rule.tatacliq.mandatory_query_filters
  source_tables: []
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.mandatory_query_filters
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.record_selection
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.batch_payout_summary
  display_name: TataCliq query pattern — 8.1 Settlement Batch Payout Summary
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.seller_realization_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.batch_payout_summary
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_payout_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.monthly_financial_waterfall
  display_name: TataCliq query pattern — 8.2 Monthly Financial Waterfall
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.monthly_financial_waterfall
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.monthly_financial_waterfall
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.monthly_financial_waterfall
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.commission_rate_validation
  display_name: TataCliq query pattern — 8.3 Commission Rate Validation
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.commission_rate
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.commission_rate_validation
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.settlement_commission_rate_validation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  display_name: TataCliq query pattern — 8.4 OMS ↔ Settlement Reconciliation
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - reconciliation_profile.tatacliq.oms_settlement_forward
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.oms_reconciliation
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.reconciliation_status
  evidence_refs:
  - ev.tatacliq.sql.settlement_oms_reconciliation
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.return_impact_analysis
  display_name: TataCliq query pattern — 8.5 Return Impact Analysis
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.return_impact
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.return_impact_analysis
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.return_impact_analysis
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.settlement.tds_summary
  display_name: TataCliq query pattern — 8.6 TDS Summary
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.tds_deducted
  source_tables:
  - zs_observe.tatacliq_settlement
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.settlement.tds_summary
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.tds_summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.monthly_gmv_trend
  display_name: TataCliq query pattern — 7.1 Monthly GMV Trend
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.monthly_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.monthly_gmv_trend
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.oms_monthly_gmv_trend
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.clean_forward_invoices
  display_name: TataCliq query pattern — 7.2 Clean Forward Invoices (Structured Rows)
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - rule.tatacliq.oms_structured_rows_filter
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.clean_forward_invoices
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.record_selection
  evidence_refs:
  - ev.tatacliq.sql.oms_clean_forward_invoices
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.brand_level_performance
  display_name: TataCliq query pattern — 7.3 Brand-Level Performance
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.brand_gmv
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.brand_level_performance
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.oms_brand_level_performance
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.intra_inter_state_gst
  display_name: TataCliq query pattern — 7.4 Intra-State vs Inter-State GST
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.product_gst_amount
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.intra_inter_state_gst
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.oms_intra_inter_state_gst
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.settlement_join
  display_name: TataCliq query pattern — 7.5 OMS → Settlement Join
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - relationship.tatacliq.oms_settlement.order_id
  source_tables:
  - zs_observe.tatacliq_settlement
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.settlement_join
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.record_selection
  evidence_refs:
  - ev.tatacliq.sql.oms_settlement_join
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.tatacliq.oms.hsn_distribution
  display_name: TataCliq query pattern — 7.6 HSN Distribution
  intent: marketplace_analysis_or_reconciliation_query
  target_cards:
  - metric.tatacliq.hsn_distribution
  source_tables:
  - zs_observe.tatacliq_oms
  required_rules:
  - rule.tatacliq.active_filter
  - rule.tatacliq.scope_fields_are_columns
  sql_ref: sql.tatacliq.oms.hsn_distribution
  parameters:
  - date_range_optional
  - active_filter
  - source_schema
  - documented_scope_filter_if_required
  output_contract_id: output_contract.tatacliq.metric_summary
  evidence_refs:
  - ev.tatacliq.sql.oms_hsn_distribution
  confidence: high
  review_status: ready
```


### 4.20 rule


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.marketplace_only_boundary
  display_name: TataCliq rule — marketplace only boundary
  rule_type: marketplace_only_boundary
  statement: Do not create tenant, group, platform account, account data binding, business scope/flow, logistics, bank, payment
    gateway, ERP/accounting, or statutory filing cards from this document.
  condition: Always apply.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.overview.background
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.active_filter
  display_name: TataCliq rule — active filter
  rule_type: active_filter
  statement: Apply is_active = true wherever source SQL or table summary requires active rows.
  condition: All table scans unless source query explicitly differs.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  - ev.tatacliq.tables.summary
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.mandatory_query_filters
  display_name: TataCliq rule — mandatory filters
  rule_type: mandatory_filters
  statement: For standard table queries use is_active = true and documented group_level_id = 22; group_level_id remains a
    source filter column, not account binding.
  condition: Both tables standard query patterns.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.scope_fields_are_columns
  display_name: TataCliq rule — scope identifier guardrail
  rule_type: scope_identifier_guardrail
  statement: group_level_id, group_id, tenant_id, seller/supplier identifiers, GSTINs, seller code, slave/warehouse code,
    payout references, and similar IDs are columns/caveats only.
  condition: Always apply.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  - ev.tatacliq.warehouse.gstin
  - ev.tatacliq.ecom.gstin
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.order_id_join_only
  display_name: TataCliq rule — join key rule
  rule_type: join_key_rule
  statement: Use order_id for OMS ↔ Settlement joins; do not use document_number = parent_id because source coverage is 0%.
  condition: OMS-settlement joins and reconciliation.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.join.coverage
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.settlement_sign_convention
  display_name: TataCliq rule — sign semantics
  rule_type: sign_semantics
  statement: Settlement charged_amount is negative for forward and positive for reverse; gross_commission is positive forward
    and negative reverse; settled_amount follows the debit/recovery convention.
  condition: All settlement amount calculations.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.table.settlement.overview
  - ev.tatacliq.schema.settlement.financial
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.abs_charged_for_forward_gmv
  display_name: TataCliq rule — gmv sign rule
  rule_type: gmv_sign_rule
  statement: Use ABS(charged_amount) for forward settlement GMV calculations exactly as source SQL does.
  condition: Forward GMV, commission rate, payout ratio.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.sql.total_forward_gmv
  - ev.tatacliq.settlement.quality
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.tship_fees_bundled
  display_name: TataCliq rule — fee structure rule
  rule_type: fee_structure_rule
  statement: Shipping, COD, PG, and fulfilment costs are bundled into gross commission; do not create separate shipping/COD/PG
    fee reconciliation from settlement zero columns.
  condition: Fee analysis and reconciliation generation.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.fee.structure
  - ev.tatacliq.fulfilment.tship
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.oms_structured_rows_filter
  display_name: TataCliq rule — oms clean rows filter
  rule_type: oms_clean_rows_filter
  statement: Use seller_name IS NOT NULL with is_active=true and transaction_type=forward for structured forward OMS invoice
    analysis.
  condition: OMS clean-row metrics and brand/AOV analysis.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.table.oms.overview
  - ev.tatacliq.sql.oms_clean_forward_invoices
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.typed_tax_columns_preferred
  display_name: TataCliq rule — schema type rule
  rule_type: schema_type_rule
  statement: Prefer typed tax_igst_*, tax_cgst_*, tax_sgst_* columns over legacy varchar tax fields; cast varchar date fields
    where needed.
  condition: OMS tax queries and date filters.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.schema.oms.tax
  - ev.tatacliq.oms.quality
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.tcs_no_table_implementation
  display_name: TataCliq rule — unsupported metric rule
  rule_type: unsupported_metric_rule
  statement: Do not emit an executable TCS implementation because no explicit TCS columns exist in tatacliq_settlement or
    tatacliq_oms.
  condition: TCS reporting requests.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.tax.tcs_absent
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.referral_fees_reverse_null
  display_name: TataCliq rule — commission rule
  rule_type: commission_rule
  statement: Use gross_commission for commission analysis across both forward and reverse because referral_fees is NULL for
    reverse rows.
  condition: Commission analysis across transaction directions.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.settlement.quality
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: rule
  card_id: rule.tatacliq.period_alignment_for_oms_settlement
  display_name: TataCliq rule — comparison period rule
  rule_type: comparison_period_rule
  statement: When comparing OMS to settlement periods, add settlement_date < 2025-10-01 or equivalent period alignment because
    settlement ends Sep 2025 while OMS runs to Dec 2025.
  condition: OMS-settlement reconciliation.
  applies_to_cards: []
  severity: high
  evidence_refs:
  - ev.tatacliq.quality.known_issues
  - ev.tatacliq.join.coverage
  confidence: high
  review_status: ready
```


### 4.21 validation_test


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.no_forbidden_scope_cards
  display_name: TataCliq validation — forbidden scope guardrail
  test_type: forbidden_scope_guardrail
  assertion: No forbidden card types are emitted from scope identifiers or external mentions.
  expected_result: forbidden_scope_cards_from_scope_ids = 0
  failure_meaning: Out-of-scope entity leakage.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.sql_refs_resolve
  display_name: TataCliq validation — sql ref integrity
  test_type: sql_ref_integrity
  assertion: Every sql_ref on query_pattern and metric_implementation resolves to a SQL pattern block.
  expected_result: dangling_sql_refs = 0
  failure_meaning: Parser cannot execute or audit query pattern.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.edge_refs_resolve
  display_name: TataCliq validation — edge referential integrity
  test_type: edge_referential_integrity
  assertion: Every candidate_edge source_card_id and target_card_id exists.
  expected_result: missing_edge_references = 0
  failure_meaning: Graph corruption.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.no_lazy_workflow_steps
  display_name: TataCliq validation — lazy workflow guardrail
  test_type: lazy_workflow_guardrail
  assertion: Workflow steps include table/column/status/sign details rather than generic lifecycle labels.
  expected_result: lazy_workflow_steps = 0
  failure_meaning: Low-material process cards.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.no_process_variants_from_segments
  display_name: TataCliq validation — process variant guardrail
  test_type: process_variant_guardrail
  assertion: No process_variant cards are created from fulfilment/order/geography labels; return is modeled as its own business_process.
  expected_result: process_variants_review_required = 0
  failure_meaning: Segment labels incorrectly modeled as process variants.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.no_unsupported_metric_implementations
  display_name: TataCliq validation — metric executability guardrail
  test_type: metric_executability_guardrail
  assertion: Metric implementations must have executable SQL refs and documented source columns.
  expected_result: unsupported_metric_implementations = 0
  failure_meaning: Prose or placeholder formula treated as executable.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.tatacliq.order_id_join_rule
  display_name: TataCliq validation — join key validation
  test_type: join_key_validation
  assertion: OMS-settlement relationship uses order_id and blocks document_number/parent_id as a working join.
  expected_result: relationship.tatacliq.oms_settlement.order_id is ready; no relationship for document_number-parent_id
  failure_meaning: Incorrect reconciliation key.
  applies_to_cards: []
  evidence_refs:
  - ev.tatacliq.join.coverage
  - ev.tatacliq.filters.mandatory
  confidence: high
  review_status: ready
```


### 4.22 output_contract


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.tatacliq.metric_summary
  display_name: TataCliq output contract — metric_summary
  contract_type: metric_summary
  required_columns:
  - grain_identifier_or_dimension
  - metric_value
  - period_when_time_series
  optional_columns:
  - supporting_components
  - observed_guidance_note
  grain: metric_or_dimensioned_group
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.tatacliq.reconciliation_status
  display_name: TataCliq output contract — reconciliation_status
  contract_type: reconciliation_status
  required_columns:
  - order_id
  - expected_amount
  - actual_amount
  - variance
  - status_or_variance_flag
  optional_columns:
  - brand
  - description
  - commission
  - tds
  - net_payout
  grain: order_id
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.tatacliq.record_selection
  display_name: TataCliq output contract — record_selection
  contract_type: record_selection
  required_columns:
  - source_table_primary_key_or_row_identifier
  - documented_filters_applied
  optional_columns:
  - diagnostic_reason
  - source_period
  grain: source_row_or_documented_selection
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.tatacliq.settlement_batch_summary
  display_name: TataCliq output contract — settlement_batch_summary
  contract_type: settlement_batch_summary
  required_columns:
  - settlement_id
  - settlement_date
  - line_items
  - orders
  - gross_gmv
  - commission
  - net_settled_or_net_payout
  optional_columns:
  - total_tds
  - return_refunds
  grain: settlement_id
  evidence_refs:
  - ev.tatacliq.sql.settlement_batch_completeness
  - ev.tatacliq.sql.recon_oms_settlement
  confidence: high
  review_status: ready
```


### 4.23 execution_constraint_set


```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.tatacliq.marketplace_parser_constraints
  display_name: TataCliq marketplace parser constraints
  constraint_family: marketplace_only_deterministic_parser_constraints
  required_filters:
  - is_active = true where source SQL/table summary requires
  - group_level_id = 22 only as documented source filter column
  aggregation_constraints:
  - Pre-aggregate many-side settlement/reverse rows before joining to order grain when downstream query intent requires it.
  join_constraints:
  - Use order_id for OMS-settlement joins; document_number-parent_id is forbidden as working relationship.
  sign_constraints:
  - Preserve TataCliq settlement debit-model sign convention; use ABS only where source SQL/rules require.
  scope_boundaries:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  - logistics_account
  - bank_account
  - payment_gateway_account
  - erp_accounting_mapping
  - statutory_tax_filing
  evidence_refs:
  - ev.tatacliq.filters.mandatory
  - ev.tatacliq.join.coverage
  - ev.tatacliq.table.settlement.overview
  confidence: high
  review_status: ready
```


## 5. Review Items and Source Caveats


```yaml
review_item:
  id: review_item.tatacliq.tcs_external_source_required
  source_section: 5.3 TCS (Tax Collected at Source — GST §52)
  issue_type: unsupported_column
  issue_or_caveat: TCS is described as collected by TUL, but no explicit TCS column exists in tatacliq_settlement or tatacliq_oms.
  recommended_parser_action: Do not generate executable TCS implementation; surface caveat and request external GSTR-2A/source
    if TCS reconciliation is required.
  related_cards:
  - metric.tatacliq.tcs_collected
  - rule.tatacliq.tcs_no_table_implementation
  severity: high
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.tatacliq.return_match_tolerance
  source_section: 7.2 Return OMS ↔ Settlement Match
  issue_type: ambiguous_threshold
  issue_or_caveat: Return match SQL computes value_variance but does not define a pass/fail threshold.
  recommended_parser_action: Keep return variance output as diagnostic unless runtime supplies a tolerance.
  related_cards:
  - matching_logic.tatacliq.return_oms_settlement
  - reconciliation_profile.tatacliq.return_oms_settlement
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.tatacliq.runtime_scope_selection
  source_section: 9. Mandatory Query Filters
  issue_type: external_runtime_scope
  issue_or_caveat: group_level_id=22 is source-documented, but runtime user/account scope selection remains outside marketplace
    canonical semantics.
  recommended_parser_action: Retain group_level_id as column/filter/value only; runtime scope layer decides whether to apply/change
    it.
  related_cards:
  - rule.tatacliq.scope_fields_are_columns
  - value_profile.tatacliq.scope.group_level_id_22
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.tatacliq.q4_settlement_gap
  source_section: 4.2 Join Keys and Coverage / 8 Data Quality Observations
  issue_type: timing_or_data_availability_gap
  issue_or_caveat: Settlement data ends Sep 2025 while OMS runs to Dec 2025, creating documented Q4 coverage gap.
  recommended_parser_action: For period-aligned reconciliation, apply settlement_date < 2025-10-01 or equivalent period constraints.
  related_cards:
  - rule.tatacliq.period_alignment_for_oms_settlement
  - reconciliation_profile.tatacliq.oms_settlement_forward
  severity: medium
  confidence: high
  review_status: open
```


```yaml
review_item:
  id: review_item.tatacliq.sku_level_analysis_not_supported
  source_section: 8 Data Quality Observations / OMS 6 Data Quality Observations
  issue_type: unsupported_column
  issue_or_caveat: sku_id is NULL for all OMS rows; TataCliq OMS does not support SKU-level analysis from this table alone.
  recommended_parser_action: Use description/HSN/brand or external product mapping if SKU-level analysis is required.
  related_cards:
  - column.zs_observe.tatacliq_oms.sku_id
  severity: medium
  confidence: high
  review_status: open
```


## 6. Candidate Edges — Refactored Unified Taxonomy


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00001.has_platform_context
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_card_id: platform.tatacliq
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00002.belongs_to_platform
  canonical_edge_type: BELONGS_TO_PLATFORM
  source_card_id: platform_context.tatacliq.in
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00003.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.orders
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00004.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.orders
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00005.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00006.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.settlement
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00007.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.fees
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00008.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.fees
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00009.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.returns
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00010.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.returns
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00011.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.tax
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00012.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.tax
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00013.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.reconciliation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00014.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.reconciliation
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00015.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.query_guidance
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00016.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.query_guidance
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00017.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: domain.tatacliq.mapping_enrichment
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00018.applies_to_platform
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_card_id: domain.tatacliq.mapping_enrichment
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00019.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00020.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00021.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00022.sourced_from_platform
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: platform.tatacliq
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00023.sourced_from_platform_context
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00024.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00025.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: domain.tatacliq.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00026.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00027.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.ancestry
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00028.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.ancestry
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00029.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.brand
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00030.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.brand
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00031.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.brand_ref_1
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00032.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.brand_ref_1
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00033.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.brand_ref_2
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00034.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.brand_ref_2
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00035.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.cess
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00036.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.cess
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00037.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00038.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.cgst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00039.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.cgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00040.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.cgst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00041.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00042.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.charged_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00043.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.charged_amount_excluding_tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00044.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.charged_amount_excluding_tax
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00045.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.created_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00046.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.created_date
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00047.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00048.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.currency_type
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00049.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00050.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.description
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00051.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.destination_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00052.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.destination_state
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00053.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.destination_state_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00054.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.destination_state_code
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00055.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00056.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_date
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00057.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_date_temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00058.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_date_temp_old
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00059.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_month
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00060.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_month
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00061.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_number
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00062.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_number
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00063.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00064.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_type
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00065.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.document_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00066.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.document_value
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00067.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.file_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00068.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.file_uuid
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00069.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00070.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.group_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00071.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00072.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.group_level_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00073.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00074.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00075.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.hsn
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00076.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.hsn
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00077.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.hsn_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00078.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.hsn_code
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00079.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.hsn_description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00080.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.hsn_description
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00081.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.hsn_generated
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00082.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.hsn_generated
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00083.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00084.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.igst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00085.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00086.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.igst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00087.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00088.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.is_active
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00089.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00090.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.order_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00091.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.order_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00092.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.order_status
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00093.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.order_tag
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00094.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.order_tag
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00095.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.other_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00096.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.other_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00097.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.parent_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00098.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.parent_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00099.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.place_of_supply
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00100.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.place_of_supply
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00101.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.quantity
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00102.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.quantity
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00103.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.seller_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00104.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.seller_code
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00105.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.seller_gstin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00106.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.seller_gstin
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00107.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.seller_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00108.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.seller_name
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00109.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.sgst_utgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00110.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.sgst_utgst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00111.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.sgst_utgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00112.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.sgst_utgst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00113.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.sheetname
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00114.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.sheetname
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00115.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.sku_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00116.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.sku_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00117.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.slave_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00118.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.slave_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00119.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.slave_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00120.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.slave_state
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00121.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.source_gst_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00122.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.source_gst_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00123.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.source_gst_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00124.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.source_gst_name
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00125.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.source_state
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00126.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.source_state
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00127.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.source_state_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00128.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.source_state_code
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00129.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_cgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00130.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_cgst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00131.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_cgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00132.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_cgst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00133.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_igst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00134.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_igst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00135.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00136.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_igst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00137.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_sgst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00138.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_sgst_amount
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00139.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tax_sgst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00140.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tax_sgst_rate
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00141.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.taxable_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00142.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.taxable_value
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00143.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00144.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.temp_old
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00145.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.tenant_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00146.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.tenant_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00147.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.transaction_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00148.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.transaction_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00149.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00150.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.transaction_type
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00151.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00152.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.txn_uuid
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00153.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00154.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.unique_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00155.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00156.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.unique_value
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00157.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.unnamed_24
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00158.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.unnamed_24
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00159.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00160.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_oms.zen_sheet_name
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00161.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.accounting_document_za
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00162.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.accounting_document_za
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00163.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.ancestry
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00164.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.ancestry
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00165.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.cgst
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00166.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.cgst
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00167.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.charged_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00168.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.charged_amount
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00169.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.clearing_doc
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00170.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.clearing_doc
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00171.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.cod_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00172.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.cod_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00173.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.currency_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00174.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.currency_type
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00175.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.description
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00176.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.description
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00177.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.fiscal_year
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00178.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.fiscal_year
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00179.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.fulfillment_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00180.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.fulfillment_type
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00181.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00182.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00183.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.gross_commission
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00184.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.gross_commission
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00185.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.gross_commission_gst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00186.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.gross_commission_gst_amount
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00187.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00188.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00189.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.igst
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00190.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.igst
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00191.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.is_active
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00192.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.is_active
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00193.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.mp_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00194.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.mp_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00195.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.net_payable
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00196.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.net_payable
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00197.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00198.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.order_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00199.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.order_reference_no
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00200.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.order_reference_no
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00201.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.order_tag
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00202.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.order_tag
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00203.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00204.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.order_type
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00205.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.other_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00206.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.other_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00207.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.other_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00208.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.other_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00209.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.other_transaction_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00210.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.other_transaction_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00211.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.parent_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00212.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.parent_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00213.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.pg_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00214.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.pg_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00215.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.product_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00216.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.product_value
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00217.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.referral_fee
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00218.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.referral_fee
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00219.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.referral_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00220.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.referral_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00221.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.seller_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00222.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.seller_code
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00223.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.settled_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00224.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.settled_amount
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00225.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.settlement_date
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00226.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.settlement_date
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00227.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.settlement_date_temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00228.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.settlement_date_temp_old
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00229.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.settlement_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00230.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.settlement_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00231.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.sgst_ugst
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00232.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.sgst_ugst
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00233.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.shipping_fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00234.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.shipping_fees
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00235.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.slave
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00236.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.slave
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00237.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.tds_on_e_commerce_operations
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00238.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.tds_on_e_commerce_operations
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00239.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.total_fees_receivable
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00240.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.total_fees_receivable
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00241.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.total_seller_payable_temp_old
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00242.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.total_seller_payable_temp_old
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00243.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.total_tds
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00244.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.total_tds
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00245.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.transaction_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00246.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.transaction_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00247.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00248.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.transaction_type
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00249.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.tul_discount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00250.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.tul_discount
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00251.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.txn_uuid
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00252.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.txn_uuid
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00253.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.unique_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00254.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.unique_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00255.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.unique_id_1
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00256.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.unique_id_1
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00257.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.unique_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00258.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.unique_value
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00259.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.zen_sheet_name
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00260.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.zen_sheet_name
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00261.has_column
  canonical_edge_type: HAS_COLUMN
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.zen_vendor_payout_commission_fee
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00262.belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_card_id: column.zs_observe.tatacliq_settlement.zen_vendor_payout_commission_fee
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00263.has_relationship
  canonical_edge_type: HAS_RELATIONSHIP
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: relationship.tatacliq.oms_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: relationship
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00264.has_relationship
  canonical_edge_type: HAS_RELATIONSHIP
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: relationship.tatacliq.oms_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: relationship
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00265.source_table
  canonical_edge_type: SOURCE_TABLE
  source_card_id: relationship.tatacliq.oms_settlement.order_id
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00266.target_table
  canonical_edge_type: TARGET_TABLE
  source_card_id: relationship.tatacliq.oms_settlement.order_id
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00267.uses_source_column
  canonical_edge_type: USES_SOURCE_COLUMN
  source_card_id: relationship.tatacliq.oms_settlement.order_id
  target_card_id: column.zs_observe.tatacliq_oms.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00268.uses_target_column
  canonical_edge_type: USES_TARGET_COLUMN
  source_card_id: relationship.tatacliq.oms_settlement.order_id
  target_card_id: column.zs_observe.tatacliq_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: relationship
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00269.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.brands
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00270.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.brand
  target_card_id: value_profile.tatacliq.brands
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00271.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.brands
  target_card_id: column.zs_observe.tatacliq_oms.brand
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00272.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.brands
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00273.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.seller_gstin_warehouse
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00274.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.seller_gstin
  target_card_id: value_profile.tatacliq.oms.seller_gstin_warehouse
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00275.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.seller_gstin_warehouse
  target_card_id: column.zs_observe.tatacliq_oms.seller_gstin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00276.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.seller_gstin_warehouse
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00277.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.ecommerce_gstin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00278.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
  target_card_id: value_profile.tatacliq.oms.ecommerce_gstin
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00279.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.ecommerce_gstin
  target_card_id: column.zs_observe.tatacliq_oms.gstin_of_e_com
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00280.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.ecommerce_gstin
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00281.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.transaction_document_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00282.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.transaction_type
  target_card_id: value_profile.tatacliq.oms.transaction_document_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00283.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.transaction_document_type
  target_card_id: column.zs_observe.tatacliq_oms.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00284.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.transaction_document_type
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00285.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.place_of_supply
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00286.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.place_of_supply
  target_card_id: value_profile.tatacliq.oms.place_of_supply
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00287.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.place_of_supply
  target_card_id: column.zs_observe.tatacliq_oms.place_of_supply
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00288.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.place_of_supply
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00289.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.gst_rates
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00290.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.tax_igst_rate
  target_card_id: value_profile.tatacliq.oms.gst_rates
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00291.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.gst_rates
  target_card_id: column.zs_observe.tatacliq_oms.tax_igst_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00292.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.gst_rates
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00293.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_oms
  target_card_id: value_profile.tatacliq.oms.hsn_codes
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00294.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_oms.hsn_code
  target_card_id: value_profile.tatacliq.oms.hsn_codes
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00295.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.oms.hsn_codes
  target_card_id: column.zs_observe.tatacliq_oms.hsn_code
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00296.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.oms.hsn_codes
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00297.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.settlement.transaction_breakdown
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00298.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.transaction_type
  target_card_id: value_profile.tatacliq.settlement.transaction_breakdown
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00299.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.settlement.transaction_breakdown
  target_card_id: column.zs_observe.tatacliq_settlement.transaction_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00300.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.settlement.transaction_breakdown
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00301.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.settlement.order_tag
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00302.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.order_tag
  target_card_id: value_profile.tatacliq.settlement.order_tag
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00303.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.settlement.order_tag
  target_card_id: column.zs_observe.tatacliq_settlement.order_tag
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00304.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.settlement.order_tag
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00305.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.settlement.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00306.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
  target_card_id: value_profile.tatacliq.settlement.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00307.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.settlement.fulfilment_channel
  target_card_id: column.zs_observe.tatacliq_settlement.fulfilment_channel
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00308.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.settlement.fulfilment_channel
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00309.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.settlement.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00310.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.order_type
  target_card_id: value_profile.tatacliq.settlement.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00311.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.settlement.order_type
  target_card_id: column.zs_observe.tatacliq_settlement.order_type
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00312.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.settlement.order_type
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00313.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.settlement.batch_structure
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00314.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.settlement_id
  target_card_id: value_profile.tatacliq.settlement.batch_structure
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00315.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.settlement.batch_structure
  target_card_id: column.zs_observe.tatacliq_settlement.settlement_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00316.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.settlement.batch_structure
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00317.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: table.zs_observe.tatacliq_settlement
  target_card_id: value_profile.tatacliq.scope.group_level_id_22
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: table
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00318.has_value_profile
  canonical_edge_type: HAS_VALUE_PROFILE
  source_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  target_card_id: value_profile.tatacliq.scope.group_level_id_22
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: column
  target_type: value_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00319.profiles_column
  canonical_edge_type: PROFILES_COLUMN
  source_card_id: value_profile.tatacliq.scope.group_level_id_22
  target_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: column
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00320.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: value_profile.tatacliq.scope.group_level_id_22
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: value_profile
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00321.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.forward_gmv
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00322.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.forward_gmv
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00323.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.return_rate
  target_card_id: domain.tatacliq.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00324.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.return_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00325.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.average_order_value
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00326.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.average_order_value
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00327.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.net_revenue_after_returns
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00328.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.net_revenue_after_returns
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00329.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.monthly_settlement_summary
  target_card_id: domain.tatacliq.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00330.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.monthly_settlement_summary
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00331.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.brand_gmv
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00332.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.brand_gmv
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00333.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.commission_rate
  target_card_id: domain.tatacliq.fees
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00334.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.commission_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00335.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.seller_realization_rate
  target_card_id: domain.tatacliq.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00336.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.seller_realization_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00337.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.settlement_batch_completeness
  target_card_id: domain.tatacliq.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00338.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.settlement_batch_completeness
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00339.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.tds_deducted
  target_card_id: domain.tatacliq.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00340.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.tds_deducted
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00341.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.effective_tds_rate
  target_card_id: domain.tatacliq.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00342.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.effective_tds_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00343.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.return_impact
  target_card_id: domain.tatacliq.returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00344.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.return_impact
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00345.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.monthly_financial_waterfall
  target_card_id: domain.tatacliq.settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00346.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.monthly_financial_waterfall
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00347.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.monthly_gmv
  target_card_id: domain.tatacliq.orders
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00348.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.monthly_gmv
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00349.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.product_gst_amount
  target_card_id: domain.tatacliq.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00350.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.product_gst_amount
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00351.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.hsn_distribution
  target_card_id: domain.tatacliq.mapping_enrichment
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00352.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.hsn_distribution
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00353.belongs_to_domain
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_card_id: metric.tatacliq.tcs_collected
  target_card_id: domain.tatacliq.tax
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: domain
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00354.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric.tatacliq.tcs_collected
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00355.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.forward_gmv
  target_card_id: metric_impl.tatacliq.total_forward_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00356.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.total_forward_gmv
  target_card_id: metric.tatacliq.forward_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00357.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.total_forward_gmv
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00358.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.return_rate
  target_card_id: metric_impl.tatacliq.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00359.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.return_rate
  target_card_id: metric.tatacliq.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00360.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.return_rate
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00361.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.average_order_value
  target_card_id: metric_impl.tatacliq.aov_oms_clean
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00362.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.aov_oms_clean
  target_card_id: metric.tatacliq.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00363.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.aov_oms_clean
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00364.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.net_revenue_after_returns
  target_card_id: metric_impl.tatacliq.net_revenue_after_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00365.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.net_revenue_after_returns
  target_card_id: metric.tatacliq.net_revenue_after_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00366.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.net_revenue_after_returns
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00367.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.monthly_settlement_summary
  target_card_id: metric_impl.tatacliq.monthly_settlement_trend
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00368.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.monthly_settlement_trend
  target_card_id: metric.tatacliq.monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00369.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.monthly_settlement_trend
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00370.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.brand_gmv
  target_card_id: metric_impl.tatacliq.brand_gmv_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00371.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.brand_gmv_oms
  target_card_id: metric.tatacliq.brand_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00372.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.brand_gmv_oms
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00373.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.commission_rate
  target_card_id: metric_impl.tatacliq.commission_rate_validation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00374.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.commission_rate_validation
  target_card_id: metric.tatacliq.commission_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00375.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.commission_rate_validation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00376.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.settlement_batch_completeness
  target_card_id: metric_impl.tatacliq.settlement_batch_completeness
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00377.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.settlement_batch_completeness
  target_card_id: metric.tatacliq.settlement_batch_completeness
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00378.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.settlement_batch_completeness
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00379.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.seller_realization_rate
  target_card_id: metric_impl.tatacliq.seller_realization_batch_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00380.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.seller_realization_batch_summary
  target_card_id: metric.tatacliq.seller_realization_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00381.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.seller_realization_batch_summary
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00382.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.monthly_financial_waterfall
  target_card_id: metric_impl.tatacliq.monthly_financial_waterfall
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00383.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.monthly_financial_waterfall
  target_card_id: metric.tatacliq.monthly_financial_waterfall
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00384.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.monthly_financial_waterfall
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00385.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.return_impact
  target_card_id: metric_impl.tatacliq.return_impact_analysis
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00386.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.return_impact_analysis
  target_card_id: metric.tatacliq.return_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00387.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.return_impact_analysis
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00388.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.effective_tds_rate
  target_card_id: metric_impl.tatacliq.tds_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00389.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.tds_reconciliation
  target_card_id: metric.tatacliq.effective_tds_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00390.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.tds_reconciliation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00391.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.tds_deducted
  target_card_id: metric_impl.tatacliq.tds_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00392.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.tds_summary
  target_card_id: metric.tatacliq.tds_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00393.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.tds_summary
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00394.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.monthly_gmv
  target_card_id: metric_impl.tatacliq.oms_monthly_gmv_trend
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00395.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.oms_monthly_gmv_trend
  target_card_id: metric.tatacliq.monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00396.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.oms_monthly_gmv_trend
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00397.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.brand_gmv
  target_card_id: metric_impl.tatacliq.oms_brand_level_performance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00398.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.oms_brand_level_performance
  target_card_id: metric.tatacliq.brand_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00399.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.oms_brand_level_performance
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00400.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.product_gst_amount
  target_card_id: metric_impl.tatacliq.oms_intra_inter_state_gst
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00401.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.oms_intra_inter_state_gst
  target_card_id: metric.tatacliq.product_gst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00402.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.oms_intra_inter_state_gst
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00403.has_implementation
  canonical_edge_type: HAS_IMPLEMENTATION
  source_card_id: metric.tatacliq.hsn_distribution
  target_card_id: metric_impl.tatacliq.oms_hsn_distribution
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: metric_implementation
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00404.implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_card_id: metric_impl.tatacliq.oms_hsn_distribution
  target_card_id: metric.tatacliq.hsn_distribution
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00405.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: metric_impl.tatacliq.oms_hsn_distribution
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_implementation
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00406.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.tatacliq.payout_calculation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00407.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.tatacliq.settlement_waterfall
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00408.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.tatacliq.commission_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00409.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.tatacliq.return_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00410.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: formula_template.tatacliq.tds_effective_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: formula_template
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00411.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric.tatacliq.seller_realization_rate
  target_card_id: formula_template.tatacliq.payout_calculation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: formula_template
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00412.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric.tatacliq.commission_rate
  target_card_id: formula_template.tatacliq.commission_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: formula_template
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00413.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric.tatacliq.return_rate
  target_card_id: formula_template.tatacliq.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: formula_template
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00414.uses_formula_template
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_card_id: metric.tatacliq.effective_tds_rate
  target_card_id: formula_template.tatacliq.tds_effective_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric
  target_type: formula_template
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00415.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.tatacliq.average_order_value
  target_card_id: metric.tatacliq.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00416.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric_dependency.tatacliq.average_order_value
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00417.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.tatacliq.return_rate
  target_card_id: metric.tatacliq.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00418.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric_dependency.tatacliq.return_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00419.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.tatacliq.commission_rate
  target_card_id: metric.tatacliq.commission_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00420.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric_dependency.tatacliq.commission_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00421.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.tatacliq.seller_realization_rate
  target_card_id: metric.tatacliq.seller_realization_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00422.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric_dependency.tatacliq.seller_realization_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00423.parent_metric
  canonical_edge_type: PARENT_METRIC
  source_card_id: metric_dependency.tatacliq.effective_tds_rate
  target_card_id: metric.tatacliq.effective_tds_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00424.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: metric_dependency.tatacliq.effective_tds_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: metric_dependency
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00425.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: platform_context.tatacliq.in
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00426.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: platform_context.tatacliq.in
  target_card_id: business_process.tatacliq.return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00427.has_business_process
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_card_id: platform_context.tatacliq.in
  target_card_id: business_process.tatacliq.marketplace_internal_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00428.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.forward_sale_flow
  target_card_id: workflow_step.tatacliq.forward_sale_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00429.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.forward_sale_flow.01
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00430.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.forward_sale_flow
  target_card_id: workflow_step.tatacliq.forward_sale_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00431.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.forward_sale_flow.02
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00432.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.forward_sale_flow
  target_card_id: workflow_step.tatacliq.forward_sale_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00433.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.forward_sale_flow.03
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00434.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.forward_sale_flow
  target_card_id: workflow_step.tatacliq.forward_sale_flow.04
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00435.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.forward_sale_flow.04
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00436.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.forward_sale_flow
  target_card_id: workflow_step.tatacliq.forward_sale_flow.05
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00437.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.forward_sale_flow.05
  target_card_id: business_process.tatacliq.forward_sale_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00438.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.return_flow
  target_card_id: workflow_step.tatacliq.return_flow.01
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00439.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.return_flow.01
  target_card_id: business_process.tatacliq.return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00440.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.return_flow
  target_card_id: workflow_step.tatacliq.return_flow.02
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00441.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.return_flow.02
  target_card_id: business_process.tatacliq.return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00442.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.return_flow
  target_card_id: workflow_step.tatacliq.return_flow.03
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00443.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.return_flow.03
  target_card_id: business_process.tatacliq.return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00444.has_workflow_step
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_card_id: business_process.tatacliq.return_flow
  target_card_id: workflow_step.tatacliq.return_flow.04
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: business_process
  target_type: workflow_step
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00445.belongs_to_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_card_id: workflow_step.tatacliq.return_flow.04
  target_card_id: business_process.tatacliq.return_flow
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: workflow_step
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00446.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: domain.tatacliq.reconciliation
  target_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00447.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: business_process.tatacliq.marketplace_internal_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00448.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: reconciliation_unit.tatacliq.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00449.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: matching_logic.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00450.has_reconciliation_profile
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_card_id: domain.tatacliq.reconciliation
  target_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: domain
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00451.supports_process
  canonical_edge_type: SUPPORTS_PROCESS
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: business_process.tatacliq.marketplace_internal_reconciliation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: business_process
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00452.has_primary_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: reconciliation_unit.tatacliq.return_order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_unit
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00453.uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: matching_logic.tatacliq.return_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: matching_logic
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00454.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: reconciliation_side.tatacliq.oms_settlement_forward.expected
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00455.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.tatacliq.oms_settlement_forward.expected
  target_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00456.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.tatacliq.oms_settlement_forward.expected
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00457.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: reconciliation_side.tatacliq.oms_settlement_forward.actual
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00458.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.tatacliq.oms_settlement_forward.actual
  target_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00459.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.tatacliq.oms_settlement_forward.actual
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00460.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: reconciliation_side.tatacliq.return_oms_settlement.expected
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00461.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.tatacliq.return_oms_settlement.expected
  target_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00462.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.tatacliq.return_oms_settlement.expected
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00463.has_reconciliation_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: reconciliation_side.tatacliq.return_oms_settlement.actual
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: reconciliation_side
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00464.belongs_to_reconciliation_profile
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_card_id: reconciliation_side.tatacliq.return_oms_settlement.actual
  target_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00465.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: reconciliation_side.tatacliq.return_oms_settlement.actual
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_side
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00466.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: reconciliation_unit.tatacliq.order_id
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_unit
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00467.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: reconciliation_unit.tatacliq.return_order_id
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_unit
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00468.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.tatacliq.oms_settlement_forward
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00469.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: matching_logic.tatacliq.return_oms_settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: matching_logic
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00470.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: mismatch_category.tatacliq.oms_settlement_forward.not_in_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00471.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  target_card_id: mismatch_category.tatacliq.oms_settlement_forward.price_variance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00472.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: mismatch_category.tatacliq.return_oms_settlement.missing_reverse_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00473.has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  target_card_id: mismatch_category.tatacliq.return_oms_settlement.value_variance
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: reconciliation_profile
  target_type: mismatch_category
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00474.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.total_forward_gmv
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00475.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.total_forward_gmv
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00476.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.total_forward_gmv
  target_card_id: metric.tatacliq.forward_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00477.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.total_forward_gmv
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00478.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.return_rate
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00479.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.return_rate
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00480.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.return_rate
  target_card_id: metric.tatacliq.return_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00481.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.return_rate
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00482.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.aov_oms_clean
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00483.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.aov_oms_clean
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00484.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.aov_oms_clean
  target_card_id: metric.tatacliq.average_order_value
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00485.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.aov_oms_clean
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00486.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.net_revenue_after_returns
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00487.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.net_revenue_after_returns
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00488.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.net_revenue_after_returns
  target_card_id: metric.tatacliq.net_revenue_after_returns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00489.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.net_revenue_after_returns
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00490.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.monthly_settlement_trend
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00491.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.monthly_settlement_trend
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00492.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.monthly_settlement_trend
  target_card_id: metric.tatacliq.monthly_settlement_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00493.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.monthly_settlement_trend
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00494.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.brand_gmv_oms
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00495.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.brand_gmv_oms
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00496.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.brand_gmv_oms
  target_card_id: metric.tatacliq.brand_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00497.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.brand_gmv_oms
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00498.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.recon_oms_settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00499.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.recon_oms_settlement
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00500.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.recon_oms_settlement
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00501.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.tatacliq.recon_oms_settlement
  target_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00502.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.recon_oms_settlement
  target_card_id: output_contract.tatacliq.reconciliation_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00503.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.recon_return_oms_settlement
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00504.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.recon_return_oms_settlement
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00505.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.recon_return_oms_settlement
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00506.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.tatacliq.recon_return_oms_settlement
  target_card_id: reconciliation_profile.tatacliq.return_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00507.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.recon_return_oms_settlement
  target_card_id: output_contract.tatacliq.reconciliation_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00508.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.commission_rate_validation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00509.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.commission_rate_validation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00510.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.commission_rate_validation
  target_card_id: metric.tatacliq.commission_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00511.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.commission_rate_validation
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00512.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement_batch_completeness
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00513.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement_batch_completeness
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00514.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement_batch_completeness
  target_card_id: metric.tatacliq.settlement_batch_completeness
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00515.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement_batch_completeness
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00516.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.tds_reconciliation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00517.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.tds_reconciliation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00518.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.tds_reconciliation
  target_card_id: metric.tatacliq.effective_tds_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00519.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.tds_reconciliation
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00520.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.mandatory_query_filters
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00521.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.tatacliq.mandatory_query_filters
  target_card_id: rule.tatacliq.mandatory_query_filters
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00522.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.mandatory_query_filters
  target_card_id: output_contract.tatacliq.record_selection
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00523.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.batch_payout_summary
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00524.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.batch_payout_summary
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00525.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement.batch_payout_summary
  target_card_id: metric.tatacliq.seller_realization_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00526.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.batch_payout_summary
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00527.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.monthly_financial_waterfall
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00528.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.monthly_financial_waterfall
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00529.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement.monthly_financial_waterfall
  target_card_id: metric.tatacliq.monthly_financial_waterfall
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00530.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.monthly_financial_waterfall
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00531.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.commission_rate_validation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00532.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.commission_rate_validation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00533.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement.commission_rate_validation
  target_card_id: metric.tatacliq.commission_rate
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00534.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.commission_rate_validation
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00535.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00536.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00537.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00538.uses_reconciliation_profile
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  target_card_id: reconciliation_profile.tatacliq.oms_settlement_forward
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: reconciliation_profile
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00539.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.oms_reconciliation
  target_card_id: output_contract.tatacliq.reconciliation_status
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00540.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.return_impact_analysis
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00541.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.return_impact_analysis
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00542.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement.return_impact_analysis
  target_card_id: metric.tatacliq.return_impact
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00543.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.return_impact_analysis
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00544.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.settlement.tds_summary
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00545.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.settlement.tds_summary
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00546.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.settlement.tds_summary
  target_card_id: metric.tatacliq.tds_deducted
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00547.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.settlement.tds_summary
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00548.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.monthly_gmv_trend
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00549.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.monthly_gmv_trend
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00550.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.oms.monthly_gmv_trend
  target_card_id: metric.tatacliq.monthly_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00551.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.monthly_gmv_trend
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00552.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.clean_forward_invoices
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00553.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.clean_forward_invoices
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00554.requires_rule
  canonical_edge_type: REQUIRES_RULE
  source_card_id: query_pattern.tatacliq.oms.clean_forward_invoices
  target_card_id: rule.tatacliq.oms_structured_rows_filter
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00555.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.clean_forward_invoices
  target_card_id: output_contract.tatacliq.record_selection
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00556.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.brand_level_performance
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00557.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.brand_level_performance
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00558.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.oms.brand_level_performance
  target_card_id: metric.tatacliq.brand_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00559.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.brand_level_performance
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00560.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.intra_inter_state_gst
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00561.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.intra_inter_state_gst
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00562.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.oms.intra_inter_state_gst
  target_card_id: metric.tatacliq.product_gst_amount
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00563.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.intra_inter_state_gst
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00564.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.settlement_join
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00565.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.settlement_join
  target_card_id: table.zs_observe.tatacliq_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00566.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.settlement_join
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00567.has_relationship
  canonical_edge_type: HAS_RELATIONSHIP
  source_card_id: query_pattern.tatacliq.oms.settlement_join
  target_card_id: relationship.tatacliq.oms_settlement.order_id
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: relationship
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00568.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.settlement_join
  target_card_id: output_contract.tatacliq.record_selection
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00569.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: query_pattern.tatacliq.oms.hsn_distribution
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00570.uses_table
  canonical_edge_type: USES_TABLE
  source_card_id: query_pattern.tatacliq.oms.hsn_distribution
  target_card_id: table.zs_observe.tatacliq_oms
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: table
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00571.produces_metric
  canonical_edge_type: PRODUCES_METRIC
  source_card_id: query_pattern.tatacliq.oms.hsn_distribution
  target_card_id: metric.tatacliq.hsn_distribution
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: metric
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00572.uses_output_contract
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_card_id: query_pattern.tatacliq.oms.hsn_distribution
  target_card_id: output_contract.tatacliq.metric_summary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: query_pattern
  target_type: output_contract
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00573.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.marketplace_only_boundary
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00574.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.active_filter
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00575.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.mandatory_query_filters
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00576.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.scope_fields_are_columns
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00577.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.order_id_join_only
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00578.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.settlement_sign_convention
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00579.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.abs_charged_for_forward_gmv
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00580.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.tship_fees_bundled
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00581.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.oms_structured_rows_filter
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00582.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.typed_tax_columns_preferred
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00583.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.tcs_no_table_implementation
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00584.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.referral_fees_reverse_null
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00585.includes_rule
  canonical_edge_type: INCLUDES_RULE
  source_card_id: platform_context.tatacliq.in
  target_card_id: rule.tatacliq.period_alignment_for_oms_settlement
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: rule
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00586.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.no_forbidden_scope_cards
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00587.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.sql_refs_resolve
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00588.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.edge_refs_resolve
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00589.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.no_lazy_workflow_steps
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00590.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.no_process_variants_from_segments
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00591.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.no_unsupported_metric_implementations
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00592.includes_validation_test
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_card_id: platform_context.tatacliq.in
  target_card_id: validation_test.tatacliq.order_id_join_rule
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: platform_context
  target_type: validation_test
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00593.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.tatacliq.metric_summary
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00594.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.tatacliq.reconciliation_status
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00595.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.tatacliq.record_selection
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00596.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: output_contract.tatacliq.settlement_batch_summary
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: output_contract
  target_type: platform_context
```


```yaml
candidate_edge:
  edge_id: edge.tatacliq.v9.00597.applies_to_platform_context
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_card_id: execution_constraint_set.tatacliq.marketplace_parser_constraints
  target_card_id: platform_context.tatacliq.in
  edge_class: canonical
  canonical_cognee_edge: true
  source_type: execution_constraint_set
  target_type: platform_context
```


## 7. Parser QA Summary


```yaml
parser_quality_manifest:
  candidate_cards: 263
  candidate_edges: 597
  source_evidence_count: 74
  sql_patterns: 24
  review_items: 5
  open_reviews: 5
  missing_edge_references: 0
  dangling_sql_refs: 0
  missing_evidence_refs: 0
  deleted_card_references: 0
  isolated_cards: 0
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variants_review_required: 0
  state_transitions_without_state_column: 0
  unresolved_benchmark_reviews_without_reason: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
  raw_source_sha256: 410ad0a3332ccb4bb39d2c745e2ac486f744af64622dbbbc3db74255d5a02d79
  raw_source_line_count: 1235
qa_details:
  missing_edge_references: []
  dangling_sql_refs: []
  missing_evidence_refs: []
  unsupported_metric_implementations: []
  forbidden_scope_cards_from_scope_ids: []
```


## 8. Source Capture Appendix — Full DOCX Text

The source DOCX text is preserved below for audit. Parser ingestion may use this appendix for evidence/backfill, but it must not create forbidden card types from it.

````text

Tab 1
# TataCliq — Business Knowledge Base

## 1. TataCliq Marketplace Overview

### 1.1 Background

TataCliq is India's premium, curated online marketplace operated by **Tata Unistore Limited (TUL)** — a joint venture between Tata Sons and Tata Industries. Launched in 2016, it positions itself as a trusted, brand-verified marketplace with a focus on authentic products and a **phygital (physical + digital) shopping experience** — integrating TataCliq's online platform with Tata's extensive offline retail network.

**Corporate identity in data:** All TataCliq e-commerce GSTINs follow the pattern `{state_code}AACCT7290E1C{x}`, confirming the PAN `AACCT7290E` belongs to Tata Unistore Limited. Seller agreements are physically signed on ₹300 stamp paper and sent to Tata Unistore Limited's Mumbai office.

**Key characteristics:**

* **Curated, invite-only:** TataCliq does not allow open seller registration — brands and sellers are hand-picked based on brand authenticity, product quality, and seller reliability
* **Phygital model:** Allows customers to buy online and pick up / return at Tata brand stores
* **100% authentic:** Only authorized sellers and genuine brands are permitted
* **Commission not publicly disclosed:** Exact rates are shared privately in seller agreements; validated at \~41.4% in the dataset

### 1.2 Brands in Dataset

| Brand | Category | Source State | Avg Selling Price | HSN Codes |
|-------|----------|--------------|-------------------|-----------|
| High Star | Men's casual & formal wear | Maharashtra, Karnataka, Haryana | ₹973              | 26        |
| Ishin | Premium women's ethnic sets, dresses | Karnataka, Maharashtra, Haryana | ₹2,135            | 22        |
| Lilpicks | Kids' ethnic & occasion wear | Maharashtra, Karnataka | ₹835              | 2         |
| Dennis Lingo | Men's casual shirts, trousers | Haryana, Karnataka, Maharashtra | ₹866              | 7         |
| Anubhutee | Women's ethnic kurta sets | Haryana, Karnataka, Maharashtra | ₹975              | 7         |
| Hubberholme | Men's outdoor / travel wear | All warehouses | —                 | —         |

### 1.3 Multi-Warehouse GSTIN Setup

Mensa operates 4 dispatch warehouses for TataCliq, each with its own GSTIN:

| Seller GSTIN | State | Slave Code | Warehouse |
|--------------|-------|------------|-----------|
| `29AAOCM5326J1ZY` | Karnataka | `126957-BLSS1` | Bangalore |
| `27AAOCM5326J1Z2` | Maharashtra | `126957-BHSS1` | Maharashtra |
| `06AAOCM5326J1Z6` | Haryana | `126957-GWSS1` | Gurgaon   |
| `19AAOCM5326J1ZZ` | West Bengal | `126957-WBSS1` | West Bengal |

The `slave_id` in OMS and `slave` in settlement encode the seller code + warehouse: `{seller_code}-{warehouse_code}`.

### 1.4 TataCliq E-Commerce GSTINs (33 States/UTs)

TataCliq (Tata Unistore Limited, PAN: `AACCT7290E`) maintains a GSTIN in **every Indian state and UT** to comply with GST law for e-commerce operators collecting TCS across state lines. Format: `{state_code}AACCT7290E1C{check}`.

The correct state GSTIN is selected based on the `place_of_supply` (destination state code) in each OMS transaction.


---

## 2. TataCliq Business Model

### 2.1 Fee Structure (Validated by Data)

TataCliq charges sellers a **commission (referral fee)** on every sale. Commission rates are not publicly disclosed — they are negotiated privately via the seller agreement annexure.

**Validated from settlement data:**

| Component | Rate | Basis | Observed Total |
|-----------|------|-------|----------------|
| Referral fee (net commission) | \~35.1% |       | charged_amount |
| GST on referral fee (18% IGST) | 18% of referral | Service tax | ₹6,45,999      |
| **Gross Commission (total deduction)** | **\~41.4%** | \`    | charged_amount |
| TDS (Section 194-O) | \~0.1% | \`    | charged_amount |
| Shipping fees | ₹0   | —     | 0 (bundled in commission) |
| COD fees  | ₹0   | —     | 0              |
| PG fees   | ₹0   | —     | 0              |

> **Key insight:** TataCliq bundles logistics, handling, and payment costs into the gross commission. There are no separate shipping, COD, or PG line items in settlement — making TataCliq's fee structure simpler to track but resulting in a relatively higher commission rate (\~41.4%) compared to marketplaces that itemize these separately.

### 2.2 Payout Calculation

```
Net Settled = |Charged Amount| − Gross Commission − TDS
            = |Charged Amount| − (Referral Fee + 18% GST on Referral Fee) − 0.1% TDS

Example (₹1,499 product):
  |charged_amount|         = ₹1,499.00
  referral_fees (excl GST) = ₹526.35  (35.1%)
  commission GST (18%)     = ₹94.74
  gross_commission total   = ₹621.09  (41.4%)
  total_tds (0.1%)         = ₹1.50
  settled_amount           = ₹876.41  (58.5% payout ratio)
```

### 2.3 Fulfilment Model — TSHIP

TataCliq uses its own logistics network branded **TSHIP**:

| Channel | Meaning | Speed |
|---------|---------|-------|
| `TSHIP/HD` | TataCliq Ship — Home Delivery | Standard (3–7 days) |
| `TSHIP/ED` | TataCliq Ship — Express Delivery | Express (1–2 days) |

Sellers dispatch from their own warehouses. TataCliq arranges pickup and last-mile delivery through its logistics partners. No fulfilment fee is charged separately.

### 2.4 Order Types

| Type | Meaning |
|------|---------|
| `PREPAID` | Customer pays online at order placement (UPI, card, net banking) |
| `POSTPAID` | Pay on delivery / credit-backed payment model |


---

## 3. Transaction Lifecycle

### 3.1 Forward Sale Flow

```
Customer places order on TataCliq (app / website)
        ↓
Order created → appears in tatacliq_oms
(transaction_type='forward', document_type='Invoice')
(invoice generated by Mensa's GSTIN for dispatch state)
(gstin_of_e_com assigned based on destination state)
        ↓
Mensa ships from nearest warehouse (slave_id assigned)
(TSHIP courier picks up)
        ↓
Product delivered to customer
        ↓
Settlement cycle runs (weekly)
→ tatacliq_settlement
(transaction_type='forward', order_tag='NOR')
(charged_amount = NEGATIVE, gross_commission = POSITIVE)
(settled_amount = NEGATIVE = net payout)
        ↓
Net amount credited to Mensa's bank account
(absolute payout = |settled_amount|)
```

### 3.2 Return Flow

```
Customer initiates return
        ↓
TataCliq logistics picks up from customer (RRF — Return to Fulfilment Centre)
        ↓
tatacliq_oms: transaction_type='reverse', document_type='Credit Note'
(Credit Note generated by Mensa for the returned item)
        ↓
tatacliq_settlement: transaction_type='reverse', order_tag='RRF'
(charged_amount = POSITIVE = refund credited)
(gross_commission = NEGATIVE = commission reversed)
(settled_amount = POSITIVE = recovery from seller's next payout)
        ↓
Return net amount deducted from seller's next settlement
```


---

## 4. Entity Relationships

### 4.1 Join Map

```
tatacliq_oms
  order_id  ←──────────────────────────→  order_id   tatacliq_settlement
  document_number  ← (partial match) →  parent_id  tatacliq_settlement
```

### 4.2 Join Keys and Coverage

| Join | Key | Coverage | Notes |
|------|-----|----------|-------|
| OMS → Settlement | `order_id` = `order_id` | 10,110 / 12,998 = **77.8%** | Coverage gap due to settlement ending Sep 2025 vs OMS Dec 2025 |
| OMS → Settlement | `document_number` = `parent_id` | **0%**   | Format mismatch — `document_number` uses `D{code}{date}...` vs numeric `parent_id` |

> **Always use** `**order_id**` **for OMS ↔ Settlement joins.** The `document_number` / `parent_id` join does not work in the current data.

### 4.3 Why Settlement Has More Orders Than OMS

| Table | Distinct Orders | Date Range |
|-------|-----------------|------------|
| tatacliq_oms | 12,998          | Jan–Dec 2025 |
| tatacliq_settlement | 15,114          | Mar–Sep 2025 |

Settlement has 2,116 more orders — these are orders that:

* Were placed before Jan 2025 (fiscal year 2024 entries) and settled in 2025
* Represent returns settled without a corresponding OMS entry in current data


---

## 5. GST / Tax Framework

### 5.1 Product GST

| Condition | Tax Type | Rate |
|-----------|----------|------|
| Source state ≠ Destination state | IGST     | 5% or 12% |
| Source state = Destination state | CGST + SGST | 2.5%+2.5% or 6%+6% |

**Apparel GST rate rule:**

* ≤ ₹1,000 MRP → 5% GST
* > ₹1,000 MRP → 12% GST

This explains the split between 5% and 12% rates in the data: Lilpicks kids' ethnic wear and Dennis Lingo casual shirts at lower price points attract 5%; Ishin premium sets and High Star higher-value items attract 12%.

### 5.2 GST on Commission (Service Tax)

TataCliq charges **18% GST** on its referral fees (SAC Code `998599` — Support services for e-commerce). This is captured as:

* `gross_commission_gst_amount` in settlement
* `igst` / `cgst` / `sgst_ugst` in settlement (breakdown by state)

Sellers can claim this as **Input Tax Credit (ITC)** on their GST returns.

### 5.3 TCS (Tax Collected at Source — GST §52)

TataCliq (Tata Unistore Limited) collects TCS on behalf of sellers under Section 52 of the CGST Act.

> **Note:** TCS is **not visible as a separate line item** in `tatacliq_settlement`. The settlement shows `total_tds` (Income Tax TDS) but no explicit TCS deduction. TCS is expected to be present in the OMS report — however, no TCS columns exist in `tatacliq_oms` either. TCS may be collected by TUL separately and visible on seller's GSTR-2A rather than in the settlement report.

### 5.4 TDS (Tax Deducted at Source — IT §194-O)

* **Rate:** \~0.1% of `|charged_amount|`
* **In settlement:** `total_tds` and `tds_on_e_commerce_operations` (duplicates)
* **Total TDS (Mar–Sep 2025):** ₹15,578.45
* **Seller recovery:** Form 26AS (annual IT return)
* **Sign:** Positive for forward (deducted), Negative for reverse (reversed)


---

## 6. Key Business Metrics (with SQL)

### 6.1 Total Forward GMV

```sql
SELECT
  SUM(ABS(charged_amount)) AS gross_gmv,
  SUM(gross_commission) AS total_commission,
  SUM(referral_fees) AS referral_fee_excl_gst,
  SUM(gross_commission_gst_amount) AS commission_gst,
  SUM(total_tds) AS total_tds,
  SUM(ABS(settled_amount)) AS net_payout,
  ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS commission_rate_pct,
  ROUND(100.0 * SUM(ABS(settled_amount)) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS payout_ratio_pct
FROM zs_observe.tatacliq_settlement
WHERE is_active = true AND transaction_type = 'forward';
-- Observed: GMV ₹1.70 Cr | Commission 41.4% | Payout ratio ~58.5%
```

### 6.2 Return Rate

```sql
SELECT
  COUNT_IF(transaction_type = 'reverse') AS returns,
  COUNT_IF(transaction_type = 'forward') AS sales,
  ROUND(100.0 * COUNT_IF(transaction_type = 'reverse')
    / NULLIF(COUNT_IF(transaction_type = 'forward'), 0), 2) AS return_rate_pct
FROM zs_observe.tatacliq_settlement
WHERE is_active = true;
-- Observed: 5,464 returns / 14,884 sales = 36.7%
```

### 6.3 AOV from OMS (Clean Rows)

```sql
SELECT
  brand,
  COUNT(*) AS invoices,
  AVG(charged_amount) AS aov,
  SUM(charged_amount) AS gmv
FROM zs_observe.tatacliq_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL
GROUP BY brand ORDER BY gmv DESC;
-- Ishin highest AOV at ₹2,135; Lilpicks lowest at ₹835
```

### 6.4 Net Revenue After Returns

```sql
SELECT
  SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_settled,
  SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_settled,
  SUM(settled_amount) AS net_revenue
FROM zs_observe.tatacliq_settlement
WHERE is_active = true;
-- Note: forward_settled is negative; return_settled is positive in TataCliq's convention
```

### 6.5 Monthly Settlement Trend

```sql
SELECT
  DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
  COUNT(*) AS line_items,
  SUM(ABS(charged_amount)) AS gross_gmv,
  SUM(gross_commission) AS commission,
  SUM(total_tds) AS tds,
  SUM(settled_amount) AS net_settled
FROM zs_observe.tatacliq_settlement
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY 1 ORDER BY 1;
```

### 6.6 Brand GMV from OMS

```sql
SELECT
  brand,
  COUNT(*) AS invoices,
  SUM(charged_amount) AS gmv,
  AVG(charged_amount) AS aov,
  COUNT(DISTINCT hsn_code) AS hsn_count
FROM zs_observe.tatacliq_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL
GROUP BY brand ORDER BY gmv DESC;
```


---

## 7. Reconciliation Use Cases

### 7.1 OMS ↔ Settlement Reconciliation

```sql
SELECT
  o.order_id,
  o.brand,
  o.description,
  o.charged_amount AS oms_invoice_value,
  o.document_type,
  ABS(s.charged_amount) AS stl_charged,
  s.gross_commission,
  s.referral_fees,
  s.gross_commission_gst_amount AS commission_gst,
  s.total_tds,
  ABS(s.settled_amount) AS net_payout,
  ABS(o.charged_amount - ABS(s.charged_amount)) AS price_variance,
  CASE
    WHEN s.order_id IS NULL THEN 'Not in Settlement (Oct–Dec 2025 gap)'
    WHEN ABS(o.charged_amount - ABS(s.charged_amount)) > 1 THEN 'Price Variance'
    ELSE 'Matched'
  END AS recon_status
FROM zs_observe.tatacliq_oms o
LEFT JOIN zs_observe.tatacliq_settlement s
  ON o.order_id = s.order_id
  AND s.is_active = true
  AND s.transaction_type = 'forward'
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.seller_name IS NOT NULL;
-- Coverage: 10,110 / 12,998 = 77.8%
```

### 7.2 Return OMS ↔ Settlement Match

```sql
SELECT
  o.order_id,
  o.charged_amount AS oms_credit_note_value,
  s.charged_amount AS stl_return_value,
  s.gross_commission AS commission_reversed,
  s.settled_amount AS return_net_settlement,
  ABS(o.charged_amount - s.charged_amount) AS value_variance
FROM zs_observe.tatacliq_oms o
LEFT JOIN zs_observe.tatacliq_settlement s
  ON o.order_id = s.order_id
  AND s.is_active = true
  AND s.transaction_type = 'reverse'
WHERE o.is_active = true
  AND o.transaction_type = 'reverse';
```

### 7.3 Commission Rate Validation

```sql
SELECT
  DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
  SUM(ABS(charged_amount)) AS gmv,
  SUM(gross_commission) AS total_commission,
  SUM(referral_fees) AS referral_fees,
  SUM(gross_commission_gst_amount) AS commission_gst,
  ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 2) AS effective_commission_pct
FROM zs_observe.tatacliq_settlement
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY 1 ORDER BY 1;
```

### 7.4 Settlement Batch Completeness

```sql
SELECT
  settlement_id,
  CAST(settlement_date AS DATE) AS stl_date,
  COUNT(*) AS line_items,
  COUNT(DISTINCT order_id) AS orders,
  SUM(ABS(charged_amount)) AS gross_gmv,
  SUM(gross_commission) AS commission,
  SUM(settled_amount) AS net_settled,
  SUM(total_tds) AS tds
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY settlement_id, settlement_date
ORDER BY settlement_date DESC;
```

### 7.5 TDS Reconciliation

```sql
SELECT
  DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
  SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds_charged,
  SUM(CASE WHEN transaction_type='reverse' THEN total_tds ELSE 0 END) AS tds_reversed,
  SUM(total_tds) AS net_tds_impact,
  ROUND(100.0 * SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END)
    / NULLIF(SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END), 0), 4) AS effective_tds_rate_pct
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY 1 ORDER BY 1;
-- Effective TDS rate: ~0.1% consistently
```


---

## 8. Data Quality Observations & Known Issues

| Issue | Table | Detail | Mitigation |
|-------|-------|--------|------------|
| `sku_id` = NULL for 100% of OMS rows | tatacliq_oms | TataCliq OMS report does not carry SKU — cannot do SKU-level analysis from OMS | Use `description` for product identification; join settlement on `order_id` |
| 1,984 OMS rows with column shifting | tatacliq_oms | Older format — `seller_name`, `document_number`, `taxable_value` NULL; financial data valid | Use `seller_name IS NOT NULL` for structured rows; include all for GMV totals |
| `created_date` and `settlement_date` stored as varchar | Both  | Cannot date-filter natively | `CAST(created_date AS DATE)` / `CAST(settlement_date AS DATE)` |
| `document_date` verbose string | tatacliq_oms | `"SEPTEMBER 24 2025"` — not directly castable | Use `document_date_temp_old` (properly typed DATE) or `created_date` |
| `charged_amount` NEGATIVE for forward | tatacliq_settlement | Sign convention reversal — forward = seller debited | Always use `ABS(charged_amount)` for GMV calculations |
| OMS ↔ Settlement 77.8% coverage | Both  | Settlement ends Sep 2025; OMS runs to Dec 2025 — Q4 gap | Add date filter `settlement_date < '2025-10-01'` when comparing periods |
| Settlement has 2,116 more orders | tatacliq_settlement | Fiscal year 2024 orders settled in 2025; returns without OMS counterpart | Expected — not a data quality issue |
| Legacy varchar tax columns | tatacliq_oms | `igst_rate`, `cgst_rate`, `sgst_utgst_rate`, `igst_amount`, `cgst_amount`, `sgst_utgst_amount` are varchar | Use typed counterparts: `tax_igst_rate`, `tax_igst_amount`, etc. |
| `quantity` NULL for 76% of OMS rows | tatacliq_oms | Not consistently reported in TataCliq's invoice export | Use row count as unit proxy |
| No TCS visible in settlement | tatacliq_settlement | TCS not reported in settlement report — collected by TUL separately | Check seller's GSTR-2A for TCS credit |
| `referral_fees` NULL for reverse rows | tatacliq_settlement | Reverse rows don't populate `referral_fees`; use `gross_commission` for full picture | Use `gross_commission` for commission analysis across both directions |


---

## 9. Mandatory Query Filters

```sql
-- Both tables (standard)
WHERE is_active = true
  AND group_level_id = 22

-- OMS: structured forward invoices only
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL   -- removes column-shifted rows

-- Settlement: forward sales GMV
WHERE is_active = true
  AND transaction_type = 'forward'
-- Note: use ABS(charged_amount) for GMV

-- Settlement: returns only
WHERE is_active = true
  AND transaction_type = 'reverse'
  AND order_tag = 'RRF'
```


---

## 10. Table Summary Reference

| Table | Purpose | Active Rows | Date Range | Primary Key | Join Key | group_level_id |
|-------|---------|-------------|------------|-------------|----------|----------------|
| `tatacliq_oms` | GST invoice / OMS (Invoice + Credit Note) | 18,215      | Jan–Dec 2025 | `order_id` + `document_number` | `order_id` | 22             |
| `tatacliq_settlement` | Financial settlement & payout ledger | 20,348      | Mar–Sep 2025 | `settlement_id` + `order_id` | `order_id` | 22             |
Tab 2
# Table: TataCliq Settlement — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `tatacliq_settlement`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`tatacliq_settlement` is the **financial settlement and payout ledger** for TataCliq. It records every financial event in Mensa's TataCliq seller account — capturing the gross sale amount, TataCliq's commission (referral fee), GST on the commission, TDS deduction, and the final net amount settled to the seller.

**Critical sign convention:** TataCliq's settlement uses a **reverse sign** from most marketplaces:

* `charged_amount` is **NEGATIVE** for forward sales (seller's account is debited for the product value)
* `charged_amount` is **POSITIVE** for reverse/return rows (refund credited back)
* `settled_amount` follows the same convention
* `gross_commission` is **POSITIVE** for forward (TataCliq charges the seller), **NEGATIVE** for reverse (commission refunded)

**Settlement entity:** Tata Unistore Limited (TUL)\n**Seller code:** `126957` (single seller account)\n**Fulfilment:** TSHIP model — TataCliq's own logistics network


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 20,348 |
| Active rows (`is_active = true`) | 20,348 (100%) |
| group_level_id | 22    |
| Date range (`settlement_date`) | 2025-03-20 → 2025-09-25 |
| Fiscal years | 2024, 2025 |
| Distinct orders | 15,114 |
| Distinct settlement batches | 54    |
| Forward transactions | 14,884 |
| Reverse transactions | 5,464 |
| Forward gross GMV (absolute) | ₹1,70,29,796 |
| Return refunds (absolute) | ₹68,08,040 |
| Forward commission charged | ₹70,55,676 |
| Forward commission rate | **\~41.43%** of GMV |
| Total referral fees | ₹59,79,370 |
| Commission GST (IGST) | ₹6,45,999 |
| Total TDS | ₹15,578.45 |
| Total net settled (absolute) | ₹1,39,43,102 |
| Seller code | `126957` |
| Currency | INR (100%) |


---

## 3. Schema Details (70 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | integer | Row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Dedup hash  |
| `settlement_id` | varchar | **Settlement batch ID** (numeric, e.g., `2200165328`) — groups multiple orders into one payout |
| `transaction_id` | varchar | Individual transaction reference (= `order_id` typically) |
| `order_id` | varchar | TataCliq order number — **primary join key to OMS** |
| `order_reference_no` | varchar | Order reference number (TataCliq internal, e.g., `139339072`) |
| `parent_id` | varchar | Parent document reference (= `order_id` for most rows) |
| `other_id` | varchar | Alternate reference |
| `slave` | varchar | Warehouse code (format: `{seller_code}-{warehouse_code}`, e.g., `126957-GWSS1`) |
| `seller_code` | varchar | `126957` — single seller code |
| `unique_id_1` | integer | Legacy unique ID |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `settlement_date` | varchar | **Settlement date** (stored as varchar; format: `2025-09-25`) |
| `settlement_date_temp_old` | date | Legacy properly-typed settlement date |
| `fiscal_year` | decimal | Fiscal year (`2024.0`, `2025.0`) |

### 3.3 Financial Columns — SIGN CONVENTION IS CRITICAL

| Column | Type | Sign (Forward) | Sign (Reverse) | Description |
|--------|------|----------------|----------------|-------------|
| `charged_amount` | decimal | **NEGATIVE**   | POSITIVE       | Gross product value (seller debited) |
| `gross_commission` | decimal | POSITIVE       | NEGATIVE       | Total TataCliq fee (referral + GST) |
| `referral_fees` | decimal | POSITIVE       | NULL/0         | Commission excl. GST (= referral fee net) |
| `referral_fee` | decimal | NULL           | —              | Alternate referral fee field |
| `gross_commission_gst_amount` | decimal | POSITIVE       | POSITIVE       | 18% GST on gross_commission |
| `settled_amount` | decimal | **NEGATIVE**   | POSITIVE       | Net payout to seller (= charged_amount + gross_commission) |
| `total_tds` | decimal | POSITIVE (debit) | NEGATIVE (reversal) | TDS under Section 194-O |
| `tds_on_e_commerce_operations` | decimal | POSITIVE       | NEGATIVE       | Duplicate of `total_tds` |
| `tul_discount` | decimal | 0 or POSITIVE  | POSITIVE       | Discount funded by TUL (TataCliq) |
| `other_fees` | decimal | 0              | 0              | Other fees (all zero in dataset) |
| `other_transaction_fees` | decimal | 0              | 0              | Other transaction fees (all zero) |
| `mp_fees` | decimal | 0              | 0              | Marketplace fees (all zero) |
| `shipping_fees` | decimal | 0              | 0              | Shipping fees (all zero — included in commission) |
| `cod_fees` | decimal | 0              | 0              | COD fees (all zero — POSTPAID/PREPAID only) |
| `pg_fees` | decimal | 0              | 0              | Payment gateway fees (all zero) |
| `net_payable` | decimal | NULL           | NULL           | Net payable (not populated) |
| `total_fees_receivable` | decimal | POSITIVE       | 0/POSITIVE     | Total fees receivable by TataCliq |
| `total_seller_payable_temp_old` | decimal | NEGATIVE       | POSITIVE       | Legacy total payable field |
| `product_value` | decimal | POSITIVE       | POSITIVE       | Product value (absolute) |

### 3.4 Tax / Accounting Columns

| Column | Type | Description |
|--------|------|-------------|
| `igst` | decimal | IGST on commission (= `gross_commission_gst_amount` for inter-state) |
| `cgst` | decimal | CGST on commission (intra-state) |
| `sgst_ugst` | decimal | SGST/UGST on commission |
| `accounting_document_za` | decimal | SAP accounting document reference |
| `clearing_doc` | decimal | SAP clearing document number |

### 3.5 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` (sale) or `reverse` (return/refund) |
| `order_type` | varchar | `PREPAID` or `POSTPAID` |
| `fulfilment_channel` | varchar | `TSHIP/HD` (Home Delivery) or `TSHIP/ED` (Express Delivery) |
| `fulfillment_type` | varchar | Same as `fulfilment_channel` |
| `order_tag` | varchar | `NOR` (Normal) or `RRF` (Return to Fulfilment Centre) |
| `description` | varchar | Transaction description (= `order_type` value: `PREPAID` / `POSTPAID`) |

### 3.6 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `22`        |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `zen_vendor_payout_commission_fee` | decimal | ZenStatement-computed commission fee (NULL) |
| `ancestry` | varchar | Lineage     |
| `zen_sheet_name` | varchar | Source sheet |


---

## 4. Distinct Value Analysis

### Transaction Type / Order Type / Fulfilment Breakdown

| Txn Type | Order Type | Channel | Order Tag | Count | Forward GMV | Commission | Settled |
|----------|------------|---------|-----------|-------|-------------|------------|---------|
| `forward` | `PREPAID`  | `TSHIP/HD` | `NOR`     | 12,025 | ₹1,34,64,680 | ₹55,77,309 | −₹78,74,015 |
| `reverse` | `PREPAID`  | `TSHIP/HD` | `RRF`     | 4,373 | +₹53,19,991 | −₹22,04,081 | +₹31,14,897 |
| `forward` | `POSTPAID` | `TSHIP/HD` | `NOR`     | 2,785 | ₹34,86,059  | ₹14,45,668 | −₹20,36,938 |
| `reverse` | `POSTPAID` | `TSHIP/HD` | `RRF`     | 1,065 | +₹14,59,467 | −₹6,04,966 | +₹8,54,205 |
| `forward` | `PREPAID`  | `TSHIP/ED` | `NOR`     | 68    | ₹70,045     | ₹28,966    | −₹41,009 |
| `reverse` | `PREPAID`  | `TSHIP/ED` | `RRF`     | 19    | +₹22,573    | −₹9,167    | +₹13,367 |

### `order_tag` Meanings

| Tag | Meaning |
|-----|---------|
| `NOR` | Normal order — forward sale |
| `RRF` | Return to Fulfilment Centre — reverse/return |

### `fulfilment_channel` / `fulfillment_type`

| Code | Meaning |
|------|---------|
| `TSHIP/HD` | TataCliq Ship — Home Delivery (standard) |
| `TSHIP/ED` | TataCliq Ship — Express Delivery (faster, premium) |

### `order_type`

| Value | Meaning |
|-------|---------|
| `PREPAID` | Online payment (UPI, card, net banking) |
| `POSTPAID` | Pay on delivery / credit-based payment |

### Settlement Batch Structure

54 distinct settlement IDs, each covering a date range of 1–14 days. Settlements appear weekly. Sample batch:

| Settlement ID | Date | Line Items | Net Settled |
|---------------|------|------------|-------------|
| `2200165328`  | 2025-09-25 | 155        | −₹56,398    |
| `2200165329`  | 2025-09-25 | 38         | −₹893       |
| `2200159131`  | 2025-09-18 | 147        | −₹50,231    |
| `2200153805`  | 2025-09-11 | 134        | −₹34,346    |


---

## 5. Financial Waterfall

### How TataCliq Settlement Is Calculated

TataCliq's settlement works on a **debit model** — all forward rows have negative `charged_amount` and negative `settled_amount`:

```
Forward Sale:
  charged_amount (seller's account debited)    −₹1,499.00
  + gross_commission (TataCliq charges)        +₹  620.09   (~41.4%)
  └─ referral_fees (fee excl. GST)             ₹ 526.35
  └─ gross_commission_gst_amount (18% IGST)    ₹  94.74
  + total_tds (TDS deducted from seller)       +₹    1.50   (~0.1%)
                                             ─────────────
  settled_amount (net payout to seller)        −₹  879.41

Return/Reverse:
  charged_amount (refund credited to seller)   +₹1,499.00
  + gross_commission (reversed)                −₹  620.09
  + total_tds (TDS reversed)                   −₹    1.50
                                             ─────────────
  settled_amount (net recovery from seller)    +₹  877.91
```

> **Note:** `settled_amount = charged_amount + gross_commission + total_tds` approximately.

### Observed Commission Rate

```
Forward Commission Rate = SUM(forward gross_commission) / SUM(|forward charged_amount|)
                        = ₹7,05,56,76 / ₹1,70,29,796 = 41.43%

Referral Fee (excl. GST) = ₹5,97,93,70 (= gross_commission / 1.18 approx.)
GST on Commission = ₹6,45,999 (18% on referral fees)
```


---

## 6. Sample Records

**Forward Sale:**

```
order_id                : 126957054719913
settlement_id           : 2200165328
settlement_date         : 2025-09-25
transaction_type        : forward
order_type              : PREPAID
fulfilment_channel      : TSHIP/HD
order_tag               : NOR
seller_code             : 126957
slave                   : 126957-GWSS1
description             : PREPAID
charged_amount          : -4236.00   ← NEGATIVE (seller debited)
gross_commission        : 1749.47    ← TataCliq fee (41.3%)
gross_commission_gst    : 266.87     ← 18% IGST on commission
referral_fees           : 1482.60    ← fee excl. GST
total_tds               : 4.24       ← 0.1% TDS
settled_amount          : -2482.29   ← net payout (negative)
total_fees_receivable   : 1749.47
igst                    : 266.87
fiscal_year             : 2025.0
group_level_id          : 22
```

**Reverse/Return:**

```
transaction_type        : reverse
order_tag               : RRF
charged_amount          : +1216.55   ← POSITIVE (refund)
gross_commission        : -504.02    ← commission reversed
tul_discount            : 213.83     ← TUL-funded discount reversal
settled_amount          : +854.21    ← net recovery
total_tds               : -1.01      ← TDS reversed
```


---

## 7. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| `charged_amount` is NEGATIVE for forward rows | Counter-intuitive sign convention | Use `ABS(charged_amount)` for GMV calculations; always check sign |
| `settlement_date` stored as varchar | Format `2025-09-25` — cast to DATE | `CAST(settlement_date AS DATE)` |
| `shipping_fees`, `cod_fees`, `pg_fees` all zero | TataCliq bundles these into commission; no separate logistics charge in settlement | No shipping reconciliation needed |
| `referral_fees` NULL for reverse rows | Commission reversal only shows in `gross_commission` for reverse | Use `gross_commission` for commission analysis across both directions |
| `net_payable` always NULL | Not populated from source | Use `settled_amount` as authoritative net field |
| `tul_discount` only on reverse rows | Represents TUL-funded discounts reversed on return | Non-zero only for 1,492 rows; mostly 0 |
| Settlement ends Sep 2025 | Data only covers Mar–Sep 2025 despite OMS running to Dec 2025 | Q4 2025 settlement data not yet ingested |
| Dual `fiscal_year` values | 2024.0 and 2025.0 — some older orders settled in 2025 report | Filter `fiscal_year = 2025.0` for current year |
| `gross_commission` vs `referral_fees` | `gross_commission = referral_fees + gross_commission_gst_amount` | Use `referral_fees` for net fee; `gross_commission` for total deduction |


---

## 8. Common Query Patterns

### 8.1 Settlement Batch Payout Summary

```sql
SELECT
  CAST(settlement_date AS DATE) AS stl_date,
  settlement_id,
  COUNT(*) AS line_items,
  SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END) AS forward_gmv,
  SUM(CASE WHEN transaction_type='reverse' THEN charged_amount ELSE 0 END) AS return_refunds,
  SUM(gross_commission) AS total_commission,
  SUM(total_tds) AS total_tds,
  SUM(settled_amount) AS net_payout
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY settlement_date, settlement_id
ORDER BY settlement_date DESC;
```

### 8.2 Monthly Financial Waterfall

```sql
SELECT
  DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
  SUM(CASE WHEN transaction_type='forward' THEN ABS(charged_amount) ELSE 0 END) AS forward_gmv,
  SUM(CASE WHEN transaction_type='forward' THEN gross_commission ELSE 0 END) AS forward_commission,
  SUM(CASE WHEN transaction_type='forward' THEN gross_commission_gst_amount ELSE 0 END) AS commission_gst,
  SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds,
  SUM(CASE WHEN transaction_type='forward' THEN settled_amount ELSE 0 END) AS forward_net,
  SUM(CASE WHEN transaction_type='reverse' THEN settled_amount ELSE 0 END) AS return_net,
  SUM(settled_amount) AS total_net
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY 1 ORDER BY 1;
```

### 8.3 Commission Rate Validation

```sql
SELECT
  COUNT(*) AS orders,
  SUM(ABS(charged_amount)) AS gross_gmv,
  SUM(gross_commission) AS total_commission,
  SUM(referral_fees) AS referral_fees_excl_gst,
  SUM(gross_commission_gst_amount) AS commission_gst,
  ROUND(100.0 * SUM(gross_commission) / NULLIF(SUM(ABS(charged_amount)), 0), 4) AS commission_rate_pct,
  ROUND(100.0 * SUM(referral_fees) / NULLIF(SUM(ABS(charged_amount)), 0), 4) AS referral_rate_pct
FROM zs_observe.tatacliq_settlement
WHERE is_active = true AND transaction_type = 'forward';
```

### 8.4 OMS ↔ Settlement Reconciliation

```sql
SELECT
  o.order_id, o.brand, o.description,
  o.charged_amount AS oms_invoice,
  ABS(s.charged_amount) AS stl_charged,
  ABS(o.charged_amount - ABS(s.charged_amount)) AS price_variance,
  s.gross_commission, s.settled_amount,
  CASE WHEN s.order_id IS NULL THEN 'Not in Settlement'
       WHEN ABS(o.charged_amount - ABS(s.charged_amount)) > 1 THEN 'Price Variance'
       ELSE 'Matched' END AS status
FROM zs_observe.tatacliq_oms o
LEFT JOIN zs_observe.tatacliq_settlement s
  ON o.order_id = s.order_id AND s.is_active = true AND s.transaction_type = 'forward'
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.seller_name IS NOT NULL;
```

### 8.5 Return Impact Analysis

```sql
SELECT
  order_tag,
  transaction_type,
  COUNT(*) AS cnt,
  SUM(ABS(charged_amount)) AS gmv_abs,
  SUM(gross_commission) AS commission,
  SUM(tul_discount) AS tul_discount,
  SUM(settled_amount) AS net_settled
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY order_tag, transaction_type
ORDER BY cnt DESC;
```

### 8.6 TDS Summary

```sql
SELECT
  DATE_TRUNC('month', CAST(settlement_date AS DATE)) AS month,
  SUM(CASE WHEN transaction_type='forward' THEN total_tds ELSE 0 END) AS tds_forward,
  SUM(CASE WHEN transaction_type='reverse' THEN total_tds ELSE 0 END) AS tds_reversed,
  SUM(total_tds) AS net_tds
FROM zs_observe.tatacliq_settlement
WHERE is_active = true
GROUP BY 1 ORDER BY 1;
```
Tab 3
# Table: TataCliq OMS — Table Knowledge Base

**Schema:** `zs_observe`  **Table:** `tatacliq_oms`  **Last Updated:** April 2025  **Maintained By:** ZenStatement Data Team


---

## 1. Table Overview

`tatacliq_oms` is the **GST invoice / Order Management System (OMS) table** for TataCliq. It stores the formal GST tax documents — Invoices (forward sales) and Credit Notes (return reversals) — generated by Mensa Brand Technologies as the seller, with Tata Unistore Limited (TUL) acting as the e-commerce operator. TataCliq is Tata Group's premium, curated online marketplace operating under the entity **Tata Unistore Limited**.

Each row represents one line-item on a GST document — a single product sold or returned. The table is sourced from the TataCliq seller portal's GSTR-1 / invoice report and is critical for GST compliance, TCS tracking, and OMS-to-settlement reconciliation.

**Seller:** Mensa Brand Technologies Private Limited\n**E-commerce Operator:** Tata Unistore Limited (PAN: `AACCT7290E`)\n**Brands:** Anubhutee, Dennis Lingo, High Star, Hubberholme, Ishin, Lilpicks\n**Categories:** Apparel — ethnic wear, menswear, kidswear, accessories

> **Data quality note:** \~1,984 rows have **column shifting** (older data format). These rows have `seller_name IS NULL`, `document_number IS NULL`, and `taxable_value IS NULL`. Financial data is still present in `charged_amount`. Use `seller_name IS NOT NULL` to filter to clean, fully-structured rows.


---

## 2. Key Statistics

| Metric | Value |
|--------|-------|
| Total rows | 18,215 |
| Active rows (`is_active = true`) | 18,215 (100%) |
| group_level_id | 22    |
| Date range (`created_date`) | 2025-01-01 → 2025-12-31 |
| Distinct orders | 12,998 |
| Distinct HSN codes | 51    |
| Distinct seller GSTINs | 4     |
| TataCliq e-commerce GSTINs | 33 (one per state/UT) |
| Forward transactions (Invoice) | 12,998 |
| Reverse transactions (Credit Note) | 5,217 |
| Brands | 6     |
| Total GMV | ₹2,12,90,414 |
| Avg forward invoice value | ₹1,138 |
| Avg return credit note | ₹1,235 |
| Seller entity | Mensa Brand Technologies Private Limited |
| Seller code (settlement) | `126957` |
| Currency | INR (100%) |


---

## 3. Schema Details (80 Columns)

### 3.1 Identity Columns

| Column | Type | Description |
|--------|------|-------------|
| `unique_id` | bigint | System row identifier |
| `txn_uuid` | varchar | Pipeline UUID |
| `unique_value` | varchar | Deduplication hash |
| `document_number` | varchar | **GST document number** (Invoice or Credit Note number, e.g., `D6832725CA001697`) — join key to settlement via `parent_id` (partial match) |
| `transaction_id` | varchar | TataCliq transaction ID (same as `order_id` for forward rows) |
| `order_id` | varchar | TataCliq order number (e.g., `126957054888163`) — **primary join key to settlement** |
| `parent_id` | varchar | Parent document reference (= `document_number` for this seller) |
| `other_id` | varchar | Alternate reference ID |
| `slave_id` | varchar | Warehouse + seller code identifier (format: `{seller_code}-{warehouse_code}`, e.g., `126957-BHSS1`) |
| `slave_state` | varchar | State code of dispatch warehouse (e.g., `27` = Maharashtra) |
| `seller_code` | varchar | TataCliq seller code: `126957` |
| `seller_name` | varchar | `Mensa Brand Technologies Private Limited` (NULL for 1,984 shifted rows) |
| `seller_gstin` | varchar | Seller GSTIN (4 distinct — see below) |
| `source_gst_id` | varchar | Same as `seller_gstin` |
| `source_gst_name` | varchar | Seller entity name |
| `gstin_of_e_com` | varchar | TataCliq's e-commerce GSTIN for the destination state (33 distinct) |

### 3.2 Date Columns

| Column | Type | Description |
|--------|------|-------------|
| `created_date` | varchar | Record date (stored as varchar, format: `2025-09-24`) — **primary date field** |
| `document_date` | varchar | GST document date (format: `SEPTEMBER 24 2025` — verbose string) |
| `document_date_temp_old` | date | Legacy date column (properly typed) |
| `document_month` | varchar | Month of document |

### 3.3 Financial Columns

| Column | Type | Description |
|--------|------|-------------|
| `charged_amount` | real | **Invoice / credit note total value (GST inclusive)** |
| `charged_amount_excluding_tax` | real | Taxable base (excluding GST) |
| `document_value` | varchar | Document value (varchar version of `charged_amount`) |
| `taxable_value` | varchar | Taxable value (NULL for shifted rows) |

### 3.4 Tax Columns

| Column | Type | Description |
|--------|------|-------------|
| `tax_igst_rate` | real | IGST rate (0, 0.05, 0.12, 0.18) |
| `tax_igst_amount` | real | IGST amount (inter-state) |
| `igst_rate` / `igst_amount` | varchar | Legacy IGST columns (varchar — use typed `tax_igst_*` columns) |
| `tax_cgst_rate` | real | CGST rate (0, 0.025, 0.06) |
| `tax_cgst_amount` | real | CGST amount (intra-state) |
| `cgst_rate` / `cgst_amount` | varchar | Legacy CGST columns |
| `tax_sgst_rate` | real | SGST rate (mirrors CGST) |
| `tax_sgst_amount` | real | SGST amount |
| `sgst_utgst_rate` / `sgst_utgst_amount` | varchar | Legacy SGST/UTGST columns |
| `cess` | varchar | Cess amount |
| `hsn_code` | varchar | **Primary HSN code** (structured rows) |
| `hsn_description` | varchar | Product description (raw field — often = description) |
| `hsn`  | varchar | HSN code (pipeline-derived field) |
| `hsn_generated` | varchar | System-generated HSN |
| `place_of_supply` | varchar | GST place of supply (state code, e.g., `27` = Maharashtra, `32` = Kerala) |

### 3.5 Classification Columns

| Column | Type | Description |
|--------|------|-------------|
| `transaction_type` | varchar | `forward` (Invoice) or `reverse` (Credit Note) |
| `document_type` | varchar | `Invoice` or `Credit Note` (NULL for 1,984 shifted rows) |
| `order_status` | varchar | `Invoice` or `Credit Note` (mirrors `document_type`) |
| `order_tag` | varchar | `NOR` = Normal order (all rows) |
| `brand` | varchar | Brand name (`High Star`, `Ishin`, `Anubhutee`, `Dennis Lingo`, `Lilpicks`, `Hubberholme`) |
| `description` | varchar | Product description |
| `sku_id` | varchar | Seller SKU — **NULL for all 18,215 rows** |
| `quantity` | integer | Quantity (NULL for \~76% of forward rows) |

### 3.6 Geographic Columns

| Column | Type | Description |
|--------|------|-------------|
| `source_state` | varchar | Seller dispatch state (title case: `Haryana`, `Karnataka`, `Maharashtra`, `West Bengal`) |
| `source_state_code` | varchar | State code  |
| `destination_state` | varchar | Buyer state (title case or NULL) |
| `destination_state_code` | varchar | Destination state code |

### 3.7 System / Metadata Columns

| Column | Type | Description |
|--------|------|-------------|
| `group_level_id` | integer | `22` — TataCliq / Mensa account |
| `group_id` / `tenant_id` | integer | Internal references |
| `file_uuid` | varchar | Source file UUID |
| `currency_type` | varchar | `INR`       |
| `is_active` | boolean | Always `true` |
| `ancestry` | varchar | Lineage     |
| `sheetname` / `zen_sheet_name` | varchar | Source sheet |
| `brand_ref_1` / `brand_ref_2` | varchar | Brand reference slugs |
| `unnamed__24` | varchar | Unnamed column from source Excel |
| `*_temp_old` | various | Legacy migration columns |


---

## 4. Distinct Value Analysis

### `transaction_type` / `document_type` Breakdown

| Txn Type | Document Type | Count | Total GMV | Avg Value |
|----------|---------------|-------|-----------|-----------|
| `forward` | `Invoice`     | 11,014 | ₹1,25,35,319 | ₹1,138    |
| `reverse` | `Credit Note` | 4,311 | ₹53,24,029 | ₹1,235    |
| `forward` | NULL (shifted rows) | 1,984 | ₹23,08,656 | ₹1,164    |
| `reverse` | NULL (shifted rows) | 906   | ₹11,22,410 | ₹1,239    |

### `brand` Distribution (Forward, structured rows only)

| Brand | Orders | Total GMV | Avg Price | HSN Codes |
|-------|--------|-----------|-----------|-----------|
| High Star | 4,490  | ₹43,70,978 | ₹973      | 26        |
| Ishin | 1,746  | ₹37,27,714 | ₹2,135    | 22        |
| Lilpicks | 1,921  | ₹16,04,393 | ₹835      | 2         |
| Dennis Lingo | 1,285  | ₹11,13,015 | ₹866      | 7         |
| Anubhutee | 827    | ₹8,06,734 | ₹975      | 7         |
| Hubberholme | few    | —         | —         | —         |

### Seller GSTIN → Warehouse Mapping

| Seller GSTIN | State | Slave Code |
|--------------|-------|------------|
| `29AAOCM5326J1ZY` | Karnataka | `126957-BLSS1` |
| `27AAOCM5326J1Z2` | Maharashtra | `126957-BHSS1` |
| `06AAOCM5326J1Z6` | Haryana | `126957-GWSS1` |
| `19AAOCM5326J1ZZ` | West Bengal | `126957-WBSS1` |

### TataCliq E-Commerce GSTINs

TataCliq (Tata Unistore Limited, PAN: `AACCT7290E`) holds a GSTIN in **every Indian state and UT** — 33 distinct GSTINs observed (format: `{state_code}AACCT7290E1C{check_digit}`). This is required under GST law for e-commerce operators collecting TCS across states. The correct GSTIN for each transaction is selected based on `place_of_supply` (destination state code).

### `place_of_supply` Values

State codes 01–37 (all Indian states/UTs) observed — confirms pan-India reach.

### HSN Codes (Sample — 51 Total)

| HSN Prefix | Category |
|------------|----------|
| `6206xxxx` | Women's blouses / kurta sets |
| `6211xxxx` | Other women's garments |
| `6204xxxx` | Women's suits / dresses |
| `6205xxxx` | Men's shirts |
| `6103/6104xxxx` | Men's suits / women's suits (knitted) |
| `6091000`  | T-shirts (knitted cotton) |
| `6307xxxx` | Other made-up textile articles |
| `6306xxxx` | Textile floor coverings |
| `5207/5408xxxx` | Fabrics  |

### GST Rates Observed

| IGST Rate | Product Type |
|-----------|--------------|
| 0%        | Exempt items |
| 5%        | Apparel (most garments < ₹1,000 MRP) |
| 12%       | Apparel (garments > ₹1,000 MRP) / some accessories |
| 18%       | Other items / marketplace services |

> **GST rate rule for apparel (India):** 5% if MRP ≤ ₹1,000; 12% if MRP > ₹1,000 — explains the mix of rates in the data.


---

## 5. Sample Records

**Structured Forward Invoice:**

```
seller_name         : Mensa Brand Technologies Private Limited
seller_gstin        : 27AAOCM5326J1Z2
seller_code         : 126957
document_number     : D6832725CA001697
document_date       : SEPTEMBER 24 2025
document_type       : Invoice
transaction_type    : forward
order_id            : 126957054888163
parent_id           : D6832725CA001697
slave_id            : 126957-BHSS1
slave_state         : 27   ← Maharashtra
brand               : High Star
description         : High Star Brown Regular Fit Cargos
hsn_code            : 62034200
source_state        : Maharashtra
place_of_supply     : 36   ← Telangana
charged_amount      : 1499.00
charged_amount_excl : 1427.62
tax_igst_rate       : 0.05   ← inter-state IGST 5%
tax_igst_amount     : 71.38
gstin_of_e_com      : 36AACCT7290E1CJ
order_tag           : NOR
created_date        : 2025-09-24
group_level_id      : 22
```

**Intra-State Invoice (CGST+SGST):**

```
source_state        : Karnataka
place_of_supply     : 29   ← Karnataka
tax_igst_rate       : 0.0   ← no IGST
tax_cgst_rate       : 0.06  ← CGST 6%
tax_cgst_amount     : 57.80
tax_sgst_rate       : 0.06  ← SGST 6%
tax_sgst_amount     : 57.80
gstin_of_e_com      : 29AACCT7290E1CE
```


---

## 6. Data Quality Observations

| Issue | Detail | Mitigation |
|-------|--------|------------|
| 1,984 rows with column shifting | Older format — `seller_name`, `document_number`, `taxable_value` are NULL; financial data still valid | Filter `seller_name IS NOT NULL` for fully structured rows; include all for GMV totals |
| `sku_id` = NULL for all 18,215 rows | TataCliq OMS report does not carry SKU | Cannot do SKU-level analysis from OMS alone |
| `quantity` NULL for \~76% | Not consistently reported | Use count of rows as proxy for units |
| `created_date` stored as varchar | Format `2025-09-24` — cast to DATE | `CAST(created_date AS DATE)` |
| `document_date` verbose string | `SEPTEMBER 24 2025` — not directly castable | Use `document_date_temp_old` (DATE type) or `created_date` |
| Legacy varchar columns | `igst_rate`, `cgst_rate`, `sgst_utgst_rate`, `taxable_value` stored as varchar | Always use typed counterparts: `tax_igst_rate`, `tax_cgst_rate`, etc. |
| `document_number` format | `D{seller_code}{date_code}{sequence}` — joins to settlement's `parent_id` field at 0% (format mismatch) | Use `order_id` for settlement joins |
| `hsn_description` often = description | `hsn_description` stores product description not HSN text for many rows | Use `hsn_code` or `hsn` for HSN; `description` for product name |
| `destination_state` NULL for \~1,903 forward rows | Older format | Use `place_of_supply` (state code) as fallback |


---

## 7. Common Query Patterns

### 7.1 Monthly GMV Trend

```sql
SELECT
  CAST(DATE_TRUNC('month', CAST(created_date AS DATE)) AS DATE) AS month,
  transaction_type,
  COUNT(*) AS docs,
  SUM(charged_amount) AS gmv,
  SUM(tax_igst_amount) AS igst,
  SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
FROM zs_observe.tatacliq_oms
WHERE is_active = true
GROUP BY 1, 2 ORDER BY 1, 2;
```

### 7.2 Clean Forward Invoices (Structured Rows)

```sql
SELECT *
FROM zs_observe.tatacliq_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL;  -- removes 1,984 shifted rows
```

### 7.3 Brand-Level Performance

```sql
SELECT brand,
  COUNT(*) AS invoices,
  SUM(charged_amount) AS gmv,
  AVG(charged_amount) AS avg_invoice_value,
  SUM(tax_igst_amount + tax_cgst_amount + tax_sgst_amount) AS total_gst
FROM zs_observe.tatacliq_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL
GROUP BY brand ORDER BY gmv DESC;
```

### 7.4 Intra-State vs Inter-State GST

```sql
SELECT
  CASE WHEN tax_igst_rate > 0 THEN 'Inter-State (IGST)' ELSE 'Intra-State (CGST+SGST)' END AS gst_type,
  COUNT(*) AS cnt,
  SUM(charged_amount) AS gmv,
  SUM(tax_igst_amount) AS igst,
  SUM(tax_cgst_amount + tax_sgst_amount) AS cgst_sgst
FROM zs_observe.tatacliq_oms
WHERE is_active = true AND transaction_type = 'forward'
GROUP BY 1;
```

### 7.5 OMS → Settlement Join

```sql
SELECT
  o.order_id, o.brand, o.description,
  o.charged_amount AS oms_invoice_value,
  o.document_type,
  s.charged_amount AS settlement_charged,
  s.gross_commission, s.settled_amount,
  s.total_tds
FROM zs_observe.tatacliq_oms o
LEFT JOIN zs_observe.tatacliq_settlement s
  ON o.order_id = s.order_id
  AND s.is_active = true
WHERE o.is_active = true
  AND o.transaction_type = 'forward'
  AND o.seller_name IS NOT NULL;
```

### 7.6 HSN Distribution

```sql
SELECT hsn_code,
  brand,
  COUNT(*) AS cnt,
  SUM(charged_amount) AS gmv,
  AVG(tax_igst_rate) AS avg_igst_rate
FROM zs_observe.tatacliq_oms
WHERE is_active = true
  AND transaction_type = 'forward'
  AND seller_name IS NOT NULL
  AND hsn_code IS NOT NULL
GROUP BY hsn_code, brand
ORDER BY cnt DESC
LIMIT 20;
```

````
