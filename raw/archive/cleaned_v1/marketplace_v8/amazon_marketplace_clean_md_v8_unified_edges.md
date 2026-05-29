# Amazon Marketplace Clean Markdown — V8 Card-Ready Reference, Unified Edges

```yaml
document_metadata:
  document_id: amazon_marketplace_clean_md_v8_unified_edges
  vendor: Amazon
  source_docx: /mnt/data/Amazon Recon Doc.docx
  frame_of_reference: marketplace_gold_standard_docx_to_clean_md_reference_v3
  generated_on: '2026-05-20'
  scope: marketplace_specific_clean_markdown_for_deterministic_parser_with_unified_edges
  marketplace_only: true
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
  allowed_card_types:
  - platform
  - platform_context
  - domain
  - table
  - column
  - relationship
  - value_profile
  - metric
  - metric_implementation
  - formula_template
  - metric_dependency
  - business_process
  - workflow_step
  - state_transition
  - process_variant
  - reconciliation_profile
  - reconciliation_side
  - reconciliation_unit
  - matching_logic
  - mismatch_category
  - reconciliation_variant
  - query_pattern
  - rule
  - validation_test
  - output_contract
  - execution_constraint_set
```
## 0.1 Redraft Notes — Unified Edges

This V8 redraft keeps the Amazon marketplace candidate-card semantics from the v3/v5 card-ready markdown and replaces the edge layer with the unified taxonomy used for the Flipkart/Myntra/Nykaa v8 files. The edge layer now supports canonical uppercase edge types, legacy parser-helper aliases, explicit inverse metadata, materialization rules, and canonical-vs-parser-helper classification.

Edge count after unification: **933** candidate edges, including **4** materialized inverse edges.

## 0. Parser Instructions

This document is intended to be parsed deterministically. It is not a prose-only summary. Every `candidate_card`, `candidate_edge`, `source_evidence`, `review_item`, and SQL reference block is machine-readable while preserving the marketplace-only boundary.

Critical parser rules:

- Create only Amazon marketplace semantic cards from this document.
- Do not create tenant, group, platform account, account binding, business scope, business flow, external logistics, bank, payment gateway, ERP/accounting, or statutory filing cards.
- Treat `group_id`, `group_level_id`, account labels, GSTIN-like values, settlement references, fulfilment labels, and UTR-like mentions only as columns/caveats where documented.
- Preserve the source table spelling `amazon_disbursment` exactly.
- Treat Amazon fulfilment, shipping, advertising service fees, SAFE-T, TCS/TDS, GST, and settlement payout fields as marketplace semantics only.
- Normalize all legacy edge aliases into canonical uppercase edge types before graph ingestion.
- Materialize inverse edges only when `materialize_inverse: true`; otherwise use reverse graph indexes.

## 1. Source Intake and Evidence Registry

```yaml
source_evidence:
  id: ev.amazon.intake.001
  source_document: Amazon Recon Doc.docx
  source_section: Amazon Marketplace — Business Skills & Analytics Playbook > Purpose
  evidence_type: prose
  summary: DOCX states this is Amazon domain knowledge, metric definitions, business rules, and analytical framework for a ZenStatement Amazon analytics agent.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.financial_stack.001
  source_document: Amazon Recon Doc.docx
  source_section: 1. The Amazon Seller Financial Stacks
  evidence_type: workflow
  summary: Buyer payment flows through Amazon deductions including commission, shipping, closing, tech, pick-and-pack, TCS, TDS, promotions, and net settlement.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.kpi.revenue.001
  source_document: Amazon Recon Doc.docx
  source_section: 2. Core Financial KPI > Revenue Metrics
  evidence_type: metric_definition
  summary: Defines Gross Revenue, Net Revenue, Taxable Revenue, Principal Revenue, AOV, and Revenue per Unit formulas.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.kpi.fee_cost.001
  source_document: Amazon Recon Doc.docx
  source_section: 2. Core Financial KPI > Fee & Cost Metrics
  evidence_type: metric_definition
  summary: Defines effective commission rate, effective fee rate, logistics cost rate, fee burden, and forward fee.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.kpi.settlement.001
  source_document: Amazon Recon Doc.docx
  source_section: 2. Core Financial KPI > Settlement & Realization Metrics
  evidence_type: metric_definition
  summary: Defines seller realization rate, net settlement per order, and fee recovery rate with benchmark context.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.kpi.return_cancel.001
  source_document: Amazon Recon Doc.docx
  source_section: 2. Core Financial KPI > Return & Cancellation Metrics
  evidence_type: metric_definition
  summary: Defines return rate, cancellation rate, net revenue per forward order, and return value rate.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.fee_taxonomy.001
  source_document: Amazon Recon Doc.docx
  source_section: 3. Amazon Fee Taxonomy
  evidence_type: rule_list
  summary: Defines commission, shipping fee, closing fee, tech fee, pick-and-pack fee, TCS, TDS, and fee recovery behavior.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.gst.001
  source_document: Amazon Recon Doc.docx
  source_section: 4. GST Framework for India Orders
  evidence_type: rule_list
  summary: Defines GST geography logic, tax-type classification, effective tax-rate denominator rule, and TCS/TDS differences.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.segmentation.001
  source_document: Amazon Recon Doc.docx
  source_section: 5. Market Segmentation Framework
  evidence_type: table
  summary: Defines India B2C, India B2B, International, AFN/FBA, MFN/Easyship, and delivery-zone segmentation.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.recon.oms_settlement.001
  source_document: Amazon Recon Doc.docx
  source_section: 6. Reconciliation Frameworks > OMS ↔ Settlement Reconciliation
  evidence_type: reconciliation_playbook
  summary: OMS forward revenue is reconciled against settlement product_sales for Order type; gaps can be yet-to-be-settled timing differences.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.recon.settlement_disbursement.001
  source_document: Amazon Recon Doc.docx
  source_section: 6. Reconciliation Frameworks > Settlement ↔ Disbursement Reconciliation
  evidence_type: reconciliation_playbook
  summary: Settlement total per order should equal sum of charged_amount in disbursement for that order, with possible timing or mapping differences.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.recon.fee_preview_actual.001
  source_document: Amazon Recon Doc.docx
  source_section: 6. Reconciliation Frameworks > Fee Preview ↔ Actual Fee Reconciliation
  evidence_type: reconciliation_playbook
  summary: Expected fee from amazon_fee_preview.gross_commission is compared to actual ItemFees from amazon_disbursment aggregated to SKU; variance is expected plus actual because actual
    ItemFees are negative.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.settlement_cycle.001
  source_document: Amazon Recon Doc.docx
  source_section: 7. Settlement Cycle & Cash Flow Concepts
  evidence_type: workflow
  summary: Amazon groups transactions into roughly two-week settlement periods; yet-to-be-settled is a legitimate timing gap.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.return_analysis.001
  source_document: Amazon Recon Doc.docx
  source_section: 8. Return Analysis Framework
  evidence_type: rule_list
  summary: Defines root-cause return categories, health benchmarks, and true cost of return formula including non-recovered fees.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.safet.001
  source_document: Amazon Recon Doc.docx
  source_section: 9. SAFE-T Reimbursement Program
  evidence_type: rule_list
  summary: Defines SAFE-T triggers, data signatures in settlement and disbursement, and SAFE-T recovery-rate formula.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.packaging_weight.001
  source_document: Amazon Recon Doc.docx
  source_section: 10. Packaging & Weight Optimisation
  evidence_type: formula
  summary: Defines volumetric weight, billable weight rule, and diagnostic query approach for packaging optimization.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.analytical_patterns.001
  source_document: Amazon Recon Doc.docx
  source_section: 11. Analytical Patterns & Common Questions
  evidence_type: query_example
  summary: 'Lists common Amazon questions: realization rate, return-rate SKUs, fee overcharge, return margin impact, ad spend, cash position, state revenue, TDS/TCS, and fee chargebacks.'
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.data_integrity.001
  source_document: Amazon Recon Doc.docx
  source_section: 12. Data Integrity Checks
  evidence_type: query_example
  summary: Defines active record rate, date coverage, OMS-settlement order-count match, and fee-preview coverage checks.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.tenant_scope_mention.001
  source_document: Amazon Recon Doc.docx
  source_section: 13. Tenant & Group Configuration
  evidence_type: caveat
  summary: DOCX mentions group_id and group_level_id partitioning, but marketplace-only gold standard treats these as filterable columns/caveats rather than tenant/account cards.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon.join_patterns.001
  source_document: Amazon Recon Doc.docx
  source_section: 14. Cross-Table Join Patterns
  evidence_type: query_example
  summary: Defines OMS-disbursement, fee-preview-disbursement, and OMS-settlement join patterns, including aggregate-before-join behavior.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.purpose.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > Purpose'
  evidence_type: schema_reference
  summary: amazon_oms is master order record and source of truth for order-level revenue, GST fields, return analytics, and upstream reconciliation anchor.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.quality.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > Data Quality — Mandatory Filter'
  evidence_type: caveat
  summary: Always filter is_active = true; optional zen_status = true and is_duplicated = false because inactive duplicates dominate.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.transaction_types.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > Transaction Types — Business Meaning'
  evidence_type: table
  summary: Defines forward, reverse, cancel, replacement, einvoicecancel, and null transaction semantics and charged_amount sign behavior.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.columns.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > Financial Columns & Types; Date Columns; Key Columns Reference'
  evidence_type: schema_reference
  summary: 'Defines key OMS columns: order identifiers, dates, geography, GST, fulfillment, transaction type, revenue, tax, discounts, commissions, settlement, group scope, and quality
    flags.'
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.kpis.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > KPI Definitions'
  evidence_type: metric_definition
  summary: Defines OMS implementations for gross revenue, net revenue, cancellation rate, return rate, AOV, net revenue per order, effective tax rate, and discount depth.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_oms.pitfalls.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_oms > Analytical Pitfalls'
  evidence_type: caveat
  summary: Warns against missing is_active filter, ignoring cancel rows, mixing transaction types, wrong tax denominator, and treating zen_vendor_payout fields as actual fees.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_settlement.purpose.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_settlement > Purpose'
  evidence_type: schema_reference
  summary: amazon_settlement is Amazon financial ledger and ground truth for cash flow, seller realization, and settlement waterfall.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_settlement.quality.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_settlement > Data Quality'
  evidence_type: caveat
  summary: Settlement has is_active, zen_status, is_duplicated; active rows can have type NULL; group_level_id is integer.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_settlement.columns.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_settlement > Financial Columns — Data Types; Key Non-Financial Columns'
  evidence_type: schema_reference
  summary: Defines settlement financial columns, transaction types, dates, settlement_id, order_id, marketplace, account_type, fulfillment, and group_level_id.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_settlement.kpis.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_settlement > Seller Realization Rate; Common Query Patterns'
  evidence_type: metric_definition
  summary: Defines seller realization rate, settlement trend, fee deduction breakdown, ad spend, and reimbursements/SAFE-T query patterns.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_settlement.pitfalls.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_settlement > Analytical Pitfalls'
  evidence_type: caveat
  summary: Warns against forgetting is_active, using date_time for filtering, string group_level_id, ignoring NULL type rows, and mixing revenue/cash-flow types.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.purpose.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Purpose'
  evidence_type: schema_reference
  summary: amazon_disbursment is granular line-level disbursement detail and primary source for per-order fee analysis and actual-vs-expected fee reconciliation.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.quality.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Data Quality'
  evidence_type: caveat
  summary: Always apply is_active = true; table name spelling is amazon_disbursment exactly.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.taxonomy.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Two-Level Fee Classification'
  evidence_type: table
  summary: Defines mp_fee_type and charged_amount_type classification for ItemPrice, ItemFees, Promotion, ItemTCS, ItemTDS, adjustments, reimbursements, and other transactions.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.transaction_types.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Transaction Types; Return Economics'
  evidence_type: rule_list
  summary: Defines Order, Refund, Fulfillment Fee Refund, SAFE-T Reimbursement and fee reversal behavior.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.columns.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Key Columns Reference'
  evidence_type: schema_reference
  summary: Defines order, item, SKU, settlement, posted date, transaction type, fee type, amount type, charged amount, group scope, currency, and quality columns.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_disbursment.queries.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_disbursment > Common Query Patterns'
  evidence_type: query_example
  summary: Defines fee breakdown, effective commission by SKU, fee recovery on returns, and SAFE-T/reimbursement queries.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_fee_preview.purpose.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_fee_preview > Purpose'
  evidence_type: schema_reference
  summary: amazon_fee_preview is SKU-level expected-fee estimate table for Amazon India and is used for expected fee vs actual charged fee reconciliation.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_fee_preview.quality.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_fee_preview > Data Quality'
  evidence_type: caveat
  summary: Use is_active = true and zen_status = true; zen_status and is_duplicated are boolean; fee_preview is India-only.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_fee_preview.weights.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_fee_preview > Weight Calculation Logic'
  evidence_type: formula
  summary: Defines gross weight, volumetric weight, final weight, and volumetric formula from dimensions.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_fee_preview.columns.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_fee_preview > Fee Columns Reference; Product Identification Columns'
  evidence_type: schema_reference
  summary: Defines SKU, ASIN, FNSKU, product fields, Amazon store, fulfilled_by, HSN, weight/dimension and fee columns including referral, fixed, shipping, pick-and-pack, and gross_commission.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_fee_preview.recon.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_fee_preview > Fee Reconciliation Framework'
  evidence_type: reconciliation_playbook
  summary: Expected gross_commission is compared against actual ItemFees from amazon_disbursment aggregated at SKU level.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_returns.purpose.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_returns > Purpose'
  evidence_type: schema_reference
  summary: amazon_returns tracks international US/Canada returns with reason codes, FC data, and comments; India returns are in amazon_oms reverse transactions.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_returns.quality.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_returns > Current State; Data Quality'
  evidence_type: caveat
  summary: All amazon_returns records are inactive due to FILE_DELETED; query patterns are ready for re-ingest only.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_returns.taxonomy.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_returns > Return Reason Taxonomy'
  evidence_type: table
  summary: Defines return reason codes grouped into quality, listing, sizing, buyer choice, buyer error, price, delivery, damage, fraud, and unknown categories.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_returns.columns.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_returns > Key Columns; Fulfilment Centre Codes'
  evidence_type: schema_reference
  summary: Defines return order ID, dates, SKU, quantity, reason, customer comments, FC code, currency, refund amounts, brand, and group_level_id.
  confidence: high
  notes: ''
```
```yaml
source_evidence:
  id: ev.amazon_returns.queries.001
  source_document: Amazon Recon Doc.docx
  source_section: 'Table: amazon_returns > Query Patterns'
  evidence_type: query_example
  summary: Defines return volume by reason, controllable vs non-controllable returns, warehouse damage rate, and fraud-signal queries.
  confidence: high
  notes: ''
```

## 2. Out-of-Scope Registry

```yaml
out_of_scope_item:
  id: oos.amazon.tenant_group.001
  topic: tenant
  source_section: 13. Tenant & Group Configuration
  mention: tenant, group, seller account, group_id, group_level_id values
  instruction: 'Allowed marketplace treatment: May appear as scope/filter columns and caveats only. Do not create: tenant; group; platform_account; account_data_binding; business_scope_set;
    business_flow_binding.'
  allowed_as: May appear as scope/filter columns and caveats only.
  forbidden_card_population:
  - tenant
  - group
  - platform_account
  - account_data_binding
  - business_scope_set
  - business_flow_binding
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
out_of_scope_item:
  id: oos.amazon.bank_payout.001
  topic: banking
  source_section: 7. Settlement Cycle & Cash Flow Concepts
  mention: seller bank transfer / payout to bank
  instruction: 'Allowed marketplace treatment: May describe marketplace settlement total or payout-cycle semantics only. Do not create: bank_account; bank_statement; settlement_to_bank_reconciliation.'
  allowed_as: May describe marketplace settlement total or payout-cycle semantics only.
  forbidden_card_population:
  - bank_account
  - bank_statement
  - settlement_to_bank_reconciliation
  evidence_refs:
  - ev.amazon.settlement_cycle.001
```
```yaml
out_of_scope_item:
  id: oos.amazon.tax_filing.001
  topic: statutory_tax
  source_section: 4. GST Framework for India Orders
  mention: GST return, income tax return, TCS/TDS claim/credit process
  instruction: 'Allowed marketplace treatment: May represent marketplace deduction columns and cash-flow caveats only. Do not create: statutory_tax_compliance_cards; filing_rules; tax_return_reconciliation.'
  allowed_as: May represent marketplace deduction columns and cash-flow caveats only.
  forbidden_card_population:
  - statutory_tax_compliance_cards
  - filing_rules
  - tax_return_reconciliation
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon.fee_taxonomy.001
```
```yaml
out_of_scope_item:
  id: oos.amazon.external_logistics.001
  topic: logistics
  source_section: 5. Market Segmentation Framework; 10. Packaging & Weight Optimisation
  mention: carrier performance, shipping invoice, AWB lifecycle, delivery operations
  instruction: 'Allowed marketplace treatment: May represent marketplace shipping fee, fulfilment segment, FC code, or weight-billing semantics only. Do not create: logistics_domain_cards;
    courier_shipment; carrier_reconciliation.'
  allowed_as: May represent marketplace shipping fee, fulfilment segment, FC code, or weight-billing semantics only.
  forbidden_card_population:
  - logistics_domain_cards
  - courier_shipment
  - carrier_reconciliation
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon.packaging_weight.001
```
```yaml
out_of_scope_item:
  id: oos.amazon.erp_accounting.001
  topic: erp_accounting
  source_section: Amazon Marketplace Playbook
  mention: GL posting, revenue recognition, journal entries, ERP/accounting close
  instruction: 'Allowed marketplace treatment: May represent marketplace fees, settlement total, and tax deduction fields only. Do not create: erp_accounting_domain_cards; ledger_posting;
    accounting_close.'
  allowed_as: May represent marketplace fees, settlement total, and tax deduction fields only.
  forbidden_card_population:
  - erp_accounting_domain_cards
  - ledger_posting
  - accounting_close
  evidence_refs:
  - ev.amazon.financial_stack.001
```
```yaml
out_of_scope_item:
  id: oos.amazon.pipeline_ops.001
  topic: pipeline_ops
  source_section: 12. Data Integrity Checks
  mention: ingestion duplicates, deleted source files, active flags
  instruction: 'Allowed marketplace treatment: May represent semantic quality filters and review caveats only. Do not create: connector_config; ingestion_schedule; pipeline_retry_policy;
    dbt_test_cards.'
  allowed_as: May represent semantic quality filters and review caveats only.
  forbidden_card_population:
  - connector_config
  - ingestion_schedule
  - pipeline_retry_policy
  - dbt_test_cards
  evidence_refs:
  - ev.amazon_oms.quality.001
  - ev.amazon_returns.quality.001
```

## 3. Optional Semantic Field Contract by Canonical Card Type

The candidate-card blocks below preserve optional semantic fields from the v3/v5 Amazon field registry. Missing optional fields must not be invented by the parser; emit review items when required semantic evidence is absent.

```yaml
semantic_field_contract:
- card_type: platform
  semantic_fields_observed:
  - allowed_scope
  - display_name
  - excluded_scope
  - platform_key
  - platform_type
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: platform_context
  semantic_fields_observed:
  - business_segments
  - country_or_region
  - currency_context
  - data_availability
  - fulfilment_models
  - marketplace_ids_or_labels
  - platform
  - scope_filter_columns
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: domain
  semantic_fields_observed:
  - domain_key
  - domain_scope
  - out_of_scope_guardrail
  - platform_context
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: table
  semantic_fields_observed:
  - date_column
  - domain
  - engine
  - full
  - grain
  - mandatory_filters
  - optional_filters
  - platform_context
  - quality_notes
  - schema
  - scope
  - table_name
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: column
  semantic_fields_observed:
  - business_meaning
  - column_name
  - data_type
  - scope_guardrail
  - semantic_category
  - table
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: relationship
  semantic_fields_observed:
  - business_semantics
  - from_table
  - join_keys
  - join_safety_rule
  - relationship_grain
  - to_table
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: value_profile
  semantic_fields_observed:
  - column
  - known_values
  - unknown_or_null_handling
  - value_semantics
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: metric
  semantic_fields_observed:
  - business_definition
  - colloquial_names
  - default_grain
  - domain
  - metric_key
  - metric_pattern
  - scope
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: metric_implementation
  semantic_fields_observed:
  - formula
  - grain
  - implements_metric
  - metric_pattern
  - notes
  - platform_context
  - required_filters
  - source_tables
  - sql_ref
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: formula_template
  semantic_fields_observed:
  - formula_expression
  - formula_key
  - notes
  - platform_context
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: metric_dependency
  semantic_fields_observed:
  - dependency_notes
  - dependency_relationship
  - from_metric
  - to_metric
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: business_process
  semantic_fields_observed:
  - domain
  - platform_context
  - process_description
  - process_key
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: workflow_step
  semantic_fields_observed:
  - process
  - step_description
  - step_key
  - step_order
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: state_transition
  semantic_fields_observed:
  - from_state
  - state_column
  - to_state
  - transition_meaning
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: process_variant
  semantic_fields_observed:
  - variant_creation_reason
  - variant_description
  - variant_key
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: reconciliation_profile
  semantic_fields_observed:
  - actual_side
  - description
  - expected_side
  - matching_logic
  - profile_key
  - reconciliation_scope
  - unit
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: reconciliation_side
  semantic_fields_observed:
  - business_role
  - profile
  - side_role
  - source_table
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: reconciliation_unit
  semantic_fields_observed:
  - grain
  - join_keys
  - profile
  - unit_key
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: matching_logic
  semantic_fields_observed:
  - aggregation_rule
  - join_keys
  - matching_rule
  - profile
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: mismatch_category
  semantic_fields_observed:
  - category_key
  - description
  - profile
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: reconciliation_variant
  semantic_fields_observed:
  - profile
  - variant_key
  - variant_reason
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: query_pattern
  semantic_fields_observed:
  - natural_language_patterns
  - primary_metric
  - query_logic
  - scope_policy
  - source_tables
  - sql_ref
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: rule
  semantic_fields_observed:
  - related_canonical_id
  - rule_text
  - rule_type
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: validation_test
  semantic_fields_observed:
  - related_canonical_id
  - sql_ref
  - test_description
  - test_type
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: output_contract
  semantic_fields_observed:
  - contract_type
  - output_columns
  - related_canonical_id
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
- card_type: execution_constraint_set
  semantic_fields_observed:
  - constraint_key
  - constraint_scope
  - constraint_text
  parser_instruction: populate only evidence-backed marketplace-specific fields; skip or review if evidence is absent
```

## 4. Source Tables and Marketplace Modules

```yaml
source_table_summary:
- table_id: table.zs_observe.amazon_oms
  table_name: zs_observe.amazon_oms
  grain: transaction row at order/item/event level
  mandatory_filters: is_active = true
  domain: domain.marketplace.amazon.orders
  notes: Active rate is very low due to duplication; transaction_type must be explicitly filtered.
- table_id: table.zs_observe.amazon_settlement
  table_name: zs_observe.amazon_settlement
  grain: settlement ledger row within settlement period
  mandatory_filters: is_active = true
  domain: domain.marketplace.amazon.settlement
  notes: type can be NULL and still carry financial values; group_level_id is integer column caveat.
- table_id: table.zs_observe.amazon_disbursment
  table_name: zs_observe.amazon_disbursment
  grain: line-level financial component row per order/item/fee/tax/promotion
  mandatory_filters: is_active = true
  domain: domain.marketplace.amazon.disbursement
  notes: Table name is misspelled in source as amazon_disbursment; match exactly.
- table_id: table.zs_observe.amazon_fee_preview
  table_name: zs_observe.amazon_fee_preview
  grain: SKU-level expected-fee estimate row
  mandatory_filters:
  - is_active = true
  - zen_status = true
  domain: domain.marketplace.amazon.fee_preview
  notes: zen_status and is_duplicated are boolean; estimated fee string columns may need TRY_CAST.
- table_id: table.zs_observe.amazon_returns
  table_name: zs_observe.amazon_returns
  grain: international return/refund row
  mandatory_filters: is_active = true
  domain: domain.marketplace.amazon.returns
  notes: All rows currently inactive due to FILE_DELETED; prepared for re-ingest.
```

## 5. Candidate Cards

### 5.1 Platform Cards

```yaml
candidate_card:
  card_type: platform
  card_id: platform.amazon
  name: Amazon
  fields:
    platform_key: amazon
    platform_type: marketplace
    display_name: Amazon
    allowed_scope: marketplace_domain_semantics_only
    excluded_scope:
    - tenant
    - group
    - platform_account
    - account_data_binding
    - business_scope_set
    - business_flow_binding
    - logistics_domain_cards
    - banking_domain_cards
    - payment_gateway_domain_cards
    - erp_accounting_domain_cards
    - statutory_tax_compliance_cards
    - data_pipeline_or_connector_operations
    evidence_refs:
    - ev.amazon.intake.001
    - ev.amazon.financial_stack.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace platform only; not a seller account.
```
### 5.2 Platform Context Cards

```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.amazon.in
  name: Amazon India marketplace context
  fields:
    platform: platform.amazon
    country_or_region: India
    marketplace_ids_or_labels:
    - amazon.in
    - IN
    currency_context: INR primary; not hardcoded for all rows
    business_segments:
    - India B2C
    - India B2B
    - International mentioned separately
    fulfilment_models:
    - AFN/FBA
    - MFN/Easyship
    - MFN
    scope_filter_columns:
    - group_level_id
    - marketplace
    - metadata
    - amazon_store
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon_oms.purpose.001
    - ev.amazon_settlement.purpose.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: 'Primary context: amazon.in marketplace semantics.'
```
```yaml
candidate_card:
  card_type: platform_context
  card_id: platform_context.amazon.international
  name: Amazon International marketplace context
  fields:
    platform: platform.amazon
    country_or_region: US; Canada; France; Spain; International
    currency_context: USD; CAD; international currencies
    data_availability: amazon_returns currently inactive; international OMS/settlement present as mentioned in DOCX
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon_returns.purpose.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: Context exists because DOCX mentions international orders and returns; active returns are unavailable.
```
### 5.3 Domain Cards

```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.orders
  name: Amazon marketplace orders and OMS
  fields:
    platform_context: platform_context.amazon.in
    domain_key: orders
    domain_scope: order capture, revenue, GST, returns, cancellation, segmentation
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon_oms.purpose.001
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: order capture, revenue, GST, returns, cancellation, segmentation
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.settlement
  name: Amazon marketplace settlement and cash flow
  fields:
    platform_context: platform_context.amazon.in
    domain_key: settlement
    domain_scope: settlement ledger, cash flow, seller realization, settlement waterfall
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon_settlement.purpose.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: settlement ledger, cash flow, seller realization, settlement waterfall
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.disbursement
  name: Amazon line-level disbursement and fee detail
  fields:
    platform_context: platform_context.amazon.in
    domain_key: disbursement
    domain_scope: line-level item price, fees, promotions, tax deductions, reimbursements
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon_disbursment.purpose.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: line-level item price, fees, promotions, tax deductions, reimbursements
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.fees
  name: Amazon marketplace fees and commission
  fields:
    platform_context: platform_context.amazon.in
    domain_key: fees
    domain_scope: commission, shipping fee, closing fee, tech fee, pickup fee, FBA fees
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.fee_taxonomy.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: commission, shipping fee, closing fee, tech fee, pickup fee, FBA fees
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.fee_preview
  name: Amazon expected-fee preview
  fields:
    platform_context: platform_context.amazon.in
    domain_key: fee_preview
    domain_scope: SKU-level fee estimates and expected-vs-actual fee comparison
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon_fee_preview.purpose.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SKU-level fee estimates and expected-vs-actual fee comparison
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.returns
  name: Amazon returns and refund economics
  fields:
    platform_context: platform_context.amazon.in
    domain_key: returns
    domain_scope: India reverse transactions plus international return reason taxonomy
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: India reverse transactions plus international return reason taxonomy
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.reimbursements_claims
  name: Amazon reimbursements and SAFE-T claims
  fields:
    platform_context: platform_context.amazon.in
    domain_key: reimbursements_claims
    domain_scope: SAFE-T reimbursements, adjustments, fulfillment fee refunds, inventory reimbursements
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SAFE-T reimbursements, adjustments, fulfillment fee refunds, inventory reimbursements
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.fulfilment_shipping
  name: Amazon fulfilment and marketplace shipping-charge semantics
  fields:
    platform_context: platform_context.amazon.in
    domain_key: fulfilment_shipping
    domain_scope: AFN/FBA, MFN/Easyship, shipping fees, weight and volumetric billing
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon.packaging_weight.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: AFN/FBA, MFN/Easyship, shipping fees, weight and volumetric billing
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.tax_deductions
  name: Amazon marketplace tax deduction fields
  fields:
    platform_context: platform_context.amazon.in
    domain_key: tax_deductions
    domain_scope: GST fields, TCS, TDS as marketplace deduction columns, not tax filing compliance
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.gst.001
    - ev.amazon.fee_taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: GST fields, TCS, TDS as marketplace deduction columns, not tax filing compliance
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.advertising_fees
  name: Amazon marketplace advertising service fees
  fields:
    platform_context: platform_context.amazon.in
    domain_key: advertising_fees
    domain_scope: Advertising spend appears as Service Fee rows with Advertising description
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Advertising spend appears as Service Fee rows with Advertising description
```
```yaml
candidate_card:
  card_type: domain
  card_id: domain.marketplace.amazon.reconciliation
  name: Amazon marketplace-internal reconciliation
  fields:
    platform_context: platform_context.amazon.in
    domain_key: reconciliation
    domain_scope: OMS-settlement, settlement-disbursement, fee preview-actual fee, returns-settlement
    out_of_scope_guardrail: no tenant/account/logistics/bank/ERP/statutory filing card creation
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.recon.settlement_disbursement.001
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: OMS-settlement, settlement-disbursement, fee preview-actual fee, returns-settlement
```
### 5.4 Table Cards

```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_oms
  name: Amazon OMS order management system
  fields:
    schema: zs_observe
    table_name: amazon_oms
    full: zs_observe.amazon_oms
    engine: Athena v3 / Trino SQL
    grain: transaction row at order/item/event level
    scope: Amazon India B2B, B2C, and international order rows
    mandatory_filters: is_active = true
    optional_filters:
    - zen_status = true
    - is_duplicated = false
    date_column: created_date
    quality_notes: Active rate is very low due to duplication; transaction_type must be explicitly filtered.
    platform_context: platform_context.amazon.in
    domain: domain.marketplace.amazon.orders
    evidence_refs:
    - ev.amazon_oms.purpose.001
    - ev.amazon_oms.quality.001
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Active rate is very low due to duplication; transaction_type must be explicitly filtered.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_settlement
  name: Amazon settlement reports
  fields:
    schema: zs_observe
    table_name: amazon_settlement
    full: zs_observe.amazon_settlement
    engine: Athena v3 / Trino SQL
    grain: settlement ledger row within settlement period
    scope: Amazon India active data with US/EU present in schema
    mandatory_filters: is_active = true
    optional_filters: zen_status = true
    date_column: settlement_date; created_date
    quality_notes: type can be NULL and still carry financial values; group_level_id is integer column caveat.
    platform_context: platform_context.amazon.in
    domain: domain.marketplace.amazon.settlement
    evidence_refs:
    - ev.amazon_settlement.purpose.001
    - ev.amazon_settlement.quality.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: type can be NULL and still carry financial values; group_level_id is integer column caveat.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_disbursment
  name: Amazon line-level disbursement detail
  fields:
    schema: zs_observe
    table_name: amazon_disbursment
    full: zs_observe.amazon_disbursment
    engine: Athena v3 / Trino SQL
    grain: line-level financial component row per order/item/fee/tax/promotion
    scope: Amazon India only
    mandatory_filters: is_active = true
    optional_filters: none specified
    date_column: posted_date; settlement_date
    quality_notes: Table name is misspelled in source as amazon_disbursment; match exactly.
    platform_context: platform_context.amazon.in
    domain: domain.marketplace.amazon.disbursement
    evidence_refs:
    - ev.amazon_disbursment.purpose.001
    - ev.amazon_disbursment.quality.001
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Table name is misspelled in source as amazon_disbursment; match exactly.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_fee_preview
  name: Amazon SKU-level fee preview
  fields:
    schema: zs_observe
    table_name: amazon_fee_preview
    full: zs_observe.amazon_fee_preview
    engine: Athena v3 / Trino SQL
    grain: SKU-level expected-fee estimate row
    scope: Amazon India fee preview only
    mandatory_filters:
    - is_active = true
    - zen_status = true
    optional_filters: is_duplicated = false
    date_column: not specified
    quality_notes: zen_status and is_duplicated are boolean; estimated fee string columns may need TRY_CAST.
    platform_context: platform_context.amazon.in
    domain: domain.marketplace.amazon.fee_preview
    evidence_refs:
    - ev.amazon_fee_preview.purpose.001
    - ev.amazon_fee_preview.quality.001
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: zen_status and is_duplicated are boolean; estimated fee string columns may need TRY_CAST.
```
```yaml
candidate_card:
  card_type: table
  card_id: table.zs_observe.amazon_returns
  name: Amazon customer returns international
  fields:
    schema: zs_observe
    table_name: amazon_returns
    full: zs_observe.amazon_returns
    engine: Athena v3 / Trino SQL
    grain: international return/refund row
    scope:
    - Amazon international US/Canada returns
    - currently inactive
    mandatory_filters: is_active = true
    optional_filters: zen_status = true
    date_column: created_date; return_date_str is string and not for filtering
    quality_notes: All rows currently inactive due to FILE_DELETED; prepared for re-ingest.
    platform_context: platform_context.amazon.international
    domain: domain.marketplace.amazon.returns
    evidence_refs:
    - ev.amazon_returns.purpose.001
    - ev.amazon_returns.quality.001
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: All rows currently inactive due to FILE_DELETED; prepared for re-ingest.
```
### 5.5 Column Cards

```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.order_id
  name: amazon_oms.order_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: order_id
    data_type: varchar
    business_meaning: Amazon order identifier and primary cross-table join key
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon order identifier and primary cross-table join key
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.item_id
  name: amazon_oms.item_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: item_id
    data_type: varchar
    business_meaning: Order item identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order item identifier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.sku_id
  name: amazon_oms.sku_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU identifier; joins to fee_preview.sku
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller SKU identifier; joins to fee_preview.sku
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.asin
  name: amazon_oms.asin
  fields:
    table: table.zs_observe.amazon_oms
    column_name: asin
    data_type: varchar
    business_meaning: Amazon ASIN product identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon ASIN product identifier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.transaction_type
  name: amazon_oms.transaction_type
  fields:
    table: table.zs_observe.amazon_oms
    column_name: transaction_type
    data_type: varchar
    business_meaning: 'Business event type: forward, reverse, cancel, replacement, einvoicecancel, null'
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Always filter explicitly.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.metadata
  name: amazon_oms.metadata
  fields:
    table: table.zs_observe.amazon_oms
    column_name: metadata
    data_type: varchar
    business_meaning: 'Segment signal: B2C, B2B, or NULL for international'
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: 'Segment signal: B2C, B2B, or NULL for international'
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.fulfilment_channel
  name: amazon_oms.fulfilment_channel
  fields:
    table: table.zs_observe.amazon_oms
    column_name: fulfilment_channel
    data_type: varchar
    business_meaning: Fulfilment channel such as AFN or MFN
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fulfilment channel such as AFN or MFN
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.fulfilment_type
  name: amazon_oms.fulfilment_type
  fields:
    table: table.zs_observe.amazon_oms
    column_name: fulfilment_type
    data_type: varchar
    business_meaning: Fulfilment model such as FBA, Other, Easyship
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fulfilment model such as FBA, Other, Easyship
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.zone
  name: amazon_oms.zone
  fields:
    table: table.zs_observe.amazon_oms
    column_name: zone
    data_type: varchar
    business_meaning: Delivery zone tier
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Delivery zone tier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.zone_new
  name: amazon_oms.zone_new
  fields:
    table: table.zs_observe.amazon_oms
    column_name: zone_new
    data_type: varchar
    business_meaning: Alternative delivery zone tier
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Alternative delivery zone tier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.source_state
  name: amazon_oms.source_state
  fields:
    table: table.zs_observe.amazon_oms
    column_name: source_state
    data_type: varchar
    business_meaning: Seller/source state for GST geography
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.gst.001
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller/source state for GST geography
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.destination_state
  name: amazon_oms.destination_state
  fields:
    table: table.zs_observe.amazon_oms
    column_name: destination_state
    data_type: varchar
    business_meaning: Buyer destination state for GST and geography analysis
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.gst.001
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Buyer destination state for GST and geography analysis
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.source_gst_id
  name: amazon_oms.source_gst_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: source_gst_id
    data_type: varchar
    business_meaning: Seller/source GST identifier as marketplace column
    semantic_category: tax_identifier
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column only; not tax compliance card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.destination_gst_id
  name: amazon_oms.destination_gst_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: destination_gst_id
    data_type: varchar
    business_meaning: Buyer GSTIN signal for B2B orders
    semantic_category: tax_identifier
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon.segmentation.001
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column only; not tenant/customer card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.invoice_number
  name: amazon_oms.invoice_number
  fields:
    table: table.zs_observe.amazon_oms
    column_name: invoice_number
    data_type: varchar
    business_meaning: GST invoice number / validation field
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.quality.001
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: GST invoice number / validation field
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.created_date
  name: amazon_oms.created_date
  fields:
    table: table.zs_observe.amazon_oms
    column_name: created_date
    data_type: date
    business_meaning: Primary date dimension for OMS time-series analysis
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Primary date dimension for OMS time-series analysis
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.order_date
  name: amazon_oms.order_date
  fields:
    table: table.zs_observe.amazon_oms
    column_name: order_date
    data_type: timestamp
    business_meaning: Order placement timestamp
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order placement timestamp
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.invoice_date
  name: amazon_oms.invoice_date
  fields:
    table: table.zs_observe.amazon_oms
    column_name: invoice_date
    data_type: timestamp
    business_meaning: GST invoice timestamp
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: GST invoice timestamp
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.order_shipped_date
  name: amazon_oms.order_shipped_date
  fields:
    table: table.zs_observe.amazon_oms
    column_name: order_shipped_date
    data_type: date
    business_meaning: Shipment date safe for date operations
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Shipment date safe for date operations
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.settlement_date
  name: amazon_oms.settlement_date
  fields:
    table: table.zs_observe.amazon_oms
    column_name: settlement_date
    data_type: date
    business_meaning: Settlement date associated with order row
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement date associated with order row
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.charged_amount
  name: amazon_oms.charged_amount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: charged_amount
    data_type: decimal(10,4)
    business_meaning: Gross revenue including tax; primary revenue metric
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Gross revenue including tax; primary revenue metric
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.charged_amount_excluding_tax
  name: amazon_oms.charged_amount_excluding_tax
  fields:
    table: table.zs_observe.amazon_oms
    column_name: charged_amount_excluding_tax
    data_type: decimal(10,4)
    business_meaning: Revenue excluding GST; denominator for tax verification
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Revenue excluding GST; denominator for tax verification
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.total_tax
  name: amazon_oms.total_tax
  fields:
    table: table.zs_observe.amazon_oms
    column_name: total_tax
    data_type: decimal(10,4)
    business_meaning: Total GST collected
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Total GST collected
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.item_amount_excluding_tax
  name: amazon_oms.item_amount_excluding_tax
  fields:
    table: table.zs_observe.amazon_oms
    column_name: item_amount_excluding_tax
    data_type: decimal(10,4)
    business_meaning: Base item price before tax
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Base item price before tax
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.shipping_amount
  name: amazon_oms.shipping_amount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: shipping_amount
    data_type: decimal(10,4)
    business_meaning: Shipping recovered from customer
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Shipping recovered from customer
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.item_promo_discount
  name: amazon_oms.item_promo_discount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: item_promo_discount
    data_type: decimal(10,4)
    business_meaning: Promotional discount on item
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotional discount on item
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.shipping_promo_discount
  name: amazon_oms.shipping_promo_discount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: shipping_promo_discount
    data_type: decimal(10,4)
    business_meaning: Promotional discount on shipping
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotional discount on shipping
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.mrp
  name: amazon_oms.mrp
  fields:
    table: table.zs_observe.amazon_oms
    column_name: mrp
    data_type: decimal(10,4)
    business_meaning: Maximum retail price for discount-to-MRP analysis
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Maximum retail price for discount-to-MRP analysis
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.principal_amount
  name: amazon_oms.principal_amount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: principal_amount
    data_type: decimal(10,4)
    business_meaning: Principal portion of transaction
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Principal portion of transaction
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.gross_commission
  name: amazon_oms.gross_commission
  fields:
    table: table.zs_observe.amazon_oms
    column_name: gross_commission
    data_type: decimal(10,4)
    business_meaning: Pre-computed gross commission estimate in OMS
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon_oms.pitfalls.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Estimate, not exact actual fee.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.settled_amount
  name: amazon_oms.settled_amount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: settled_amount
    data_type: decimal(10,4)
    business_meaning: Amount settled for the order
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amount settled for the order
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.total_tcs_amount
  name: amazon_oms.total_tcs_amount
  fields:
    table: table.zs_observe.amazon_oms
    column_name: total_tcs_amount
    data_type: decimal(10,4)
    business_meaning: TCS deducted amount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column; not statutory filing card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.total_tds
  name: amazon_oms.total_tds
  fields:
    table: table.zs_observe.amazon_oms
    column_name: total_tds
    data_type: decimal(10,4)
    business_meaning: TDS deducted amount under Section 194-O
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column; not statutory filing card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.tax_igst_rate
  name: amazon_oms.tax_igst_rate
  fields:
    table: table.zs_observe.amazon_oms
    column_name: tax_igst_rate
    data_type: decimal
    business_meaning: IGST rate indicator for inter-state classification
    semantic_category: tax
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: IGST rate indicator for inter-state classification
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.tax_cgst_rate
  name: amazon_oms.tax_cgst_rate
  fields:
    table: table.zs_observe.amazon_oms
    column_name: tax_cgst_rate
    data_type: decimal
    business_meaning: CGST rate indicator for intra-state classification
    semantic_category: tax
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: CGST rate indicator for intra-state classification
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.tax_ugst_rate
  name: amazon_oms.tax_ugst_rate
  fields:
    table: table.zs_observe.amazon_oms
    column_name: tax_ugst_rate
    data_type: decimal
    business_meaning: UGST rate indicator for Union Territory classification
    semantic_category: tax
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: UGST rate indicator for Union Territory classification
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.is_active
  name: amazon_oms.is_active
  fields:
    table: table.zs_observe.amazon_oms
    column_name: is_active
    data_type: boolean
    business_meaning: Active-row quality flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mandatory filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.zen_status
  name: amazon_oms.zen_status
  fields:
    table: table.zs_observe.amazon_oms
    column_name: zen_status
    data_type: boolean
    business_meaning: ZenStatement row status flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Recommended optional filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.is_duplicated
  name: amazon_oms.is_duplicated
  fields:
    table: table.zs_observe.amazon_oms
    column_name: is_duplicated
    data_type: boolean
    business_meaning: Duplicate-row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_oms.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Recommended optional exclusion.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.group_id
  name: amazon_oms.group_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: group_id
    data_type: integer
    business_meaning: Data partition identifier mentioned by DOCX
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no group card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.group_level_id
  name: amazon_oms.group_level_id
  fields:
    table: table.zs_observe.amazon_oms
    column_name: group_level_id
    data_type: integer
    business_meaning: Marketplace account partition/scope column mentioned by DOCX
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no account-binding card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_oms.currency_type
  name: amazon_oms.currency_type
  fields:
    table: table.zs_observe.amazon_oms
    column_name: currency_type
    data_type: varchar
    business_meaning: Currency context for order rows
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Currency context for order rows
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.settlement_id
  name: amazon_settlement.settlement_id
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: settlement_id
    data_type: varchar
    business_meaning: Settlement period ID grouping payout-cycle rows
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.settlement_cycle.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement period ID grouping payout-cycle rows
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.order_id
  name: amazon_settlement.order_id
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: order_id
    data_type: varchar
    business_meaning: Amazon order identifier; joins to OMS and disbursement
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon order identifier; joins to OMS and disbursement
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.sku
  name: amazon_settlement.sku
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: sku
    data_type: varchar
    business_meaning: Raw seller SKU field
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Raw seller SKU field
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.sku_id
  name: amazon_settlement.sku_id
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller SKU identifier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.type
  name: amazon_settlement.type
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: type
    data_type: varchar
    business_meaning: Settlement transaction type including Order, Refund, Service Fee, SAFE-T, NULL
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon_settlement.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: NULL values carry financial data.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.description
  name: amazon_settlement.description
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: description
    data_type: varchar
    business_meaning: Settlement description used for fee/ad identification
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.kpis.001
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement description used for fee/ad identification
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.marketplace
  name: amazon_settlement.marketplace
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: marketplace
    data_type: varchar
    business_meaning: Marketplace label such as amazon.in or international marketplace
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace label such as amazon.in or international marketplace
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.account_type
  name: amazon_settlement.account_type
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: account_type
    data_type: varchar
    business_meaning: Settlement account type e.g. Electronic/COD or Standard/Invoiced
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column only; no platform_account card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.destination_state
  name: amazon_settlement.destination_state
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: destination_state
    data_type: varchar
    business_meaning: Buyer state for settlement/geography analysis
    semantic_category: geography
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Buyer state for settlement/geography analysis
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.fulfillment
  name: amazon_settlement.fulfillment
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: fulfillment
    data_type: varchar
    business_meaning: Fulfilment method on settlement row
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fulfilment method on settlement row
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.created_date
  name: amazon_settlement.created_date
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: created_date
    data_type: timestamp
    business_meaning: Settlement row timestamp used in common patterns
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement row timestamp used in common patterns
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.settlement_date
  name: amazon_settlement.settlement_date
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: settlement_date
    data_type: timestamp
    business_meaning: Recommended settlement date for date-based queries
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Recommended settlement date for date-based queries
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.date_time
  name: amazon_settlement.date_time
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: date_time
    data_type: varchar
    business_meaning: Human-readable timestamp string, not for filtering
    semantic_category: date_string
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon_settlement.pitfalls.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not filter on date_time.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.product_sales
  name: amazon_settlement.product_sales
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: product_sales
    data_type: decimal
    business_meaning: Revenue from product sold; positive order and negative refund semantics
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Revenue from product sold; positive order and negative refund semantics
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.selling_fees
  name: amazon_settlement.selling_fees
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: selling_fees
    data_type: decimal
    business_meaning: Referral/commission fees, normally negative
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Referral/commission fees, normally negative
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.fba_fees
  name: amazon_settlement.fba_fees
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: fba_fees
    data_type: decimal
    business_meaning: FBA fulfilment and storage fees, normally negative
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: FBA fulfilment and storage fees, normally negative
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.shipping_credits
  name: amazon_settlement.shipping_credits
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: shipping_credits
    data_type: decimal
    business_meaning: Shipping charged to buyer
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Shipping charged to buyer
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.promotional_rebates
  name: amazon_settlement.promotional_rebates
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: promotional_rebates
    data_type: decimal
    business_meaning: Promotional discounts/rebates, normally negative
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotional discounts/rebates, normally negative
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.gift_wrap_credits
  name: amazon_settlement.gift_wrap_credits
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: gift_wrap_credits
    data_type: decimal
    business_meaning: Gift wrap credits/charges
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Gift wrap credits/charges
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.other_transaction_fees
  name: amazon_settlement.other_transaction_fees
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: other_transaction_fees
    data_type: decimal
    business_meaning: Closing, tech, and other transaction fees
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Closing, tech, and other transaction fees
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.other
  name: amazon_settlement.other
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: other
    data_type: decimal
    business_meaning: Miscellaneous adjustment amount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Miscellaneous adjustment amount
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.tcs_cgst
  name: amazon_settlement.tcs_cgst
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: tcs_cgst
    data_type: decimal
    business_meaning: TCS CGST deduction component
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column only.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.tcs_sgst
  name: amazon_settlement.tcs_sgst
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: tcs_sgst
    data_type: decimal
    business_meaning: TCS SGST deduction component
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column only.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.tcs_igst
  name: amazon_settlement.tcs_igst
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: tcs_igst
    data_type: decimal
    business_meaning: TCS IGST deduction component
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column only.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.tds
  name: amazon_settlement.tds
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: tds
    data_type: decimal
    business_meaning: TDS deduction under Section 194-O
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction column only.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.marketplace_withheld_tax
  name: amazon_settlement.marketplace_withheld_tax
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: marketplace_withheld_tax
    data_type: decimal
    business_meaning: Tax withheld for US/EU marketplace rows
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace column only.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.gross_commission
  name: amazon_settlement.gross_commission
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: gross_commission
    data_type: decimal
    business_meaning: Pre-computed commission amount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Pre-computed commission amount
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.mp_fees
  name: amazon_settlement.mp_fees
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: mp_fees
    data_type: decimal
    business_meaning: Marketplace fee aggregate
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace fee aggregate
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.settled_amount
  name: amazon_settlement.settled_amount
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: settled_amount
    data_type: decimal
    business_meaning: Pre-computed settled amount
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Pre-computed settled amount
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.total
  name: amazon_settlement.total
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: total
    data_type: decimal
    business_meaning: Net amount credited/debited for settlement row
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.columns.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Net amount credited/debited for settlement row
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.is_active
  name: amazon_settlement.is_active
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: is_active
    data_type: boolean
    business_meaning: Active row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mandatory filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.zen_status
  name: amazon_settlement.zen_status
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: zen_status
    data_type: boolean
    business_meaning: Zen status row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Recommended optional filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.is_duplicated
  name: amazon_settlement.is_duplicated
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: is_duplicated
    data_type: boolean
    business_meaning: Duplicate row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_settlement.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Duplicate row flag
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_settlement.group_level_id
  name: amazon_settlement.group_level_id
  fields:
    table: table.zs_observe.amazon_settlement
    column_name: group_level_id
    data_type: integer
    business_meaning: Data partition/scope column, integer type
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon_settlement.quality.001
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no account-binding card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.order_id
  name: amazon_disbursment.order_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: order_id
    data_type: varchar
    business_meaning: Amazon order ID; join key to OMS and settlement
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon order ID; join key to OMS and settlement
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.item_id
  name: amazon_disbursment.item_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: item_id
    data_type: varchar
    business_meaning: Item-level identifier
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Item-level identifier
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.sku_id
  name: amazon_disbursment.sku_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU identifier; joins to fee_preview.sku
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller SKU identifier; joins to fee_preview.sku
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.sku
  name: amazon_disbursment.sku
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: sku
    data_type: varchar
    business_meaning: Seller SKU raw value if present
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller SKU raw value if present
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.settlement_id
  name: amazon_disbursment.settlement_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: settlement_id
    data_type: varchar
    business_meaning: Settlement period ID; joins to settlement
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement period ID; joins to settlement
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.settlement_date
  name: amazon_disbursment.settlement_date
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: settlement_date
    data_type: date
    business_meaning: Settlement date
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement date
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.posted_date
  name: amazon_disbursment.posted_date
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: posted_date
    data_type: date
    business_meaning: Posted date for disbursement row
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Posted date for disbursement row
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.transaction_type
  name: amazon_disbursment.transaction_type
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: transaction_type
    data_type: varchar
    business_meaning: Order, Refund, Fulfillment Fee Refund, SAFE-T Reimbursement, Other, other-transaction
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Always specify in fee computations.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.mp_fee_type
  name: amazon_disbursment.mp_fee_type
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: mp_fee_type
    data_type: varchar
    business_meaning: First-level fee category such as ItemPrice, ItemFees, Promotion, ItemTCS, ItemTDS
    semantic_category: taxonomy
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: First-level fee category such as ItemPrice, ItemFees, Promotion, ItemTCS, ItemTDS
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.charged_amount_type
  name: amazon_disbursment.charged_amount_type
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: charged_amount_type
    data_type: varchar
    business_meaning: Second-level line-item type such as principal, commission, shipping fee, tds, reimbursement
    semantic_category: taxonomy
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Second-level line-item type such as principal, commission, shipping fee, tds, reimbursement
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.charged_amount
  name: amazon_disbursment.charged_amount
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: charged_amount
    data_type: decimal
    business_meaning: Financial value for the line item; signs depend on category and transaction_type
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Financial value for the line item; signs depend on category and transaction_type
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.order_level_total
  name: amazon_disbursment.order_level_total
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: order_level_total
    data_type: decimal
    business_meaning: Order-level total if present
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order-level total if present
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.item_fee_type
  name: amazon_disbursment.item_fee_type
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: item_fee_type
    data_type: varchar
    business_meaning: Fee subtype when present
    semantic_category: taxonomy
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fee subtype when present
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.promotion_id
  name: amazon_disbursment.promotion_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: promotion_id
    data_type: varchar
    business_meaning: Promotion identifier if row is promotion-related
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotion identifier if row is promotion-related
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.group_id
  name: amazon_disbursment.group_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: group_id
    data_type: integer
    business_meaning: Data partition identifier
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no group card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.group_level_id
  name: amazon_disbursment.group_level_id
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: group_level_id
    data_type: integer
    business_meaning: Data partition/scope column
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no account-binding card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.currency_type
  name: amazon_disbursment.currency_type
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: currency_type
    data_type: varchar
    business_meaning: Currency code for disbursement amount
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Currency code for disbursement amount
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_disbursment.is_active
  name: amazon_disbursment.is_active
  fields:
    table: table.zs_observe.amazon_disbursment
    column_name: is_active
    data_type: boolean
    business_meaning: Active row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_disbursment.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mandatory filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.sku
  name: amazon_fee_preview.sku
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: sku
    data_type: varchar
    business_meaning: SKU primary key for fee preview; joins to OMS sku_id and disbursement sku_id
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SKU primary key for fee preview; joins to OMS sku_id and disbursement sku_id
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.asin
  name: amazon_fee_preview.asin
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: asin
    data_type: varchar
    business_meaning: Amazon ASIN
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon ASIN
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.fnsku
  name: amazon_fee_preview.fnsku
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: fnsku
    data_type: varchar
    business_meaning: Fulfilment network SKU
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fulfilment network SKU
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.brand
  name: amazon_fee_preview.brand
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: brand
    data_type: varchar
    business_meaning: Brand name
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Brand name
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.description
  name: amazon_fee_preview.description
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: description
    data_type: varchar
    business_meaning: Product description
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Product description
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.product_name
  name: amazon_fee_preview.product_name
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: product_name
    data_type: varchar
    business_meaning: Product name
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Product name
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.product_group
  name: amazon_fee_preview.product_group
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: product_group
    data_type: varchar
    business_meaning: Amazon product category/group
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon product category/group
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.amazon_store
  name: amazon_fee_preview.amazon_store
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: amazon_store
    data_type: varchar
    business_meaning: Store/marketplace indicator; India-only in DOCX
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Store/marketplace indicator; India-only in DOCX
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.fulfilled_by
  name: amazon_fee_preview.fulfilled_by
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: fulfilled_by
    data_type: varchar
    business_meaning: Fulfilment mode for expected fee estimate
    semantic_category: segment
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fulfilment mode for expected fee estimate
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.hsn
  name: amazon_fee_preview.hsn
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: hsn
    data_type: varchar
    business_meaning: HSN code as product tax classification column
    semantic_category: tax_identifier
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column only; no statutory tax card.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.charged_amount
  name: amazon_fee_preview.charged_amount
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: charged_amount
    data_type: decimal
    business_meaning: Selling price or base charged amount used in fee estimate
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Selling price or base charged amount used in fee estimate
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.referral_fee
  name: amazon_fee_preview.referral_fee
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: referral_fee
    data_type: decimal
    business_meaning: Referral fee amount in rupees
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Referral fee amount in rupees
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.referal_fee
  name: amazon_fee_preview.referal_fee
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: referal_fee
    data_type: decimal_or_varchar
    business_meaning: Referral fee percentage field; spelling/source caveat
    semantic_category: amount_or_rate
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: DOCX warns this is a percentage (0.19 = 19%), not rupee amount.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.fixed_fee
  name: amazon_fee_preview.fixed_fee
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: fixed_fee
    data_type: decimal
    business_meaning: Fixed closing/transaction fee estimate
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fixed closing/transaction fee estimate
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.pick_and_pack_fee
  name: amazon_fee_preview.pick_and_pack_fee
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: pick_and_pack_fee
    data_type: decimal
    business_meaning: Pick-and-pack fee estimate
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Pick-and-pack fee estimate
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.shipping_amount
  name: amazon_fee_preview.shipping_amount
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: shipping_amount
    data_type: decimal
    business_meaning: Expected shipping/weight handling fee
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon.packaging_weight.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected shipping/weight handling fee
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.gross_commission
  name: amazon_fee_preview.gross_commission
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: gross_commission
    data_type: decimal
    business_meaning: Expected total gross commission/fee estimate for SKU
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected total gross commission/fee estimate for SKU
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.gross_weight
  name: amazon_fee_preview.gross_weight
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: gross_weight
    data_type: decimal
    business_meaning: Actual gross weight
    semantic_category: weight
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Actual gross weight
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.volumetric_weight
  name: amazon_fee_preview.volumetric_weight
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: volumetric_weight
    data_type: decimal
    business_meaning: Volumetric weight computed from dimensions
    semantic_category: weight
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Volumetric weight computed from dimensions
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.final_weight
  name: amazon_fee_preview.final_weight
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: final_weight
    data_type: decimal
    business_meaning: 'Billable weight: max(gross_weight, volumetric_weight)'
    semantic_category: weight
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: 'Billable weight: max(gross_weight, volumetric_weight)'
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.longest_side
  name: amazon_fee_preview.longest_side
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: longest_side
    data_type: decimal
    business_meaning: Longest package side in cm
    semantic_category: dimension
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Longest package side in cm
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.median_side
  name: amazon_fee_preview.median_side
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: median_side
    data_type: decimal
    business_meaning: Median package side in cm
    semantic_category: dimension
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Median package side in cm
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.shortest_side
  name: amazon_fee_preview.shortest_side
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: shortest_side
    data_type: decimal
    business_meaning: Shortest package side in cm
    semantic_category: dimension
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Shortest package side in cm
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.estimated_fee_total
  name: amazon_fee_preview.estimated_fee_total
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: estimated_fee_total
    data_type: decimal_or_varchar
    business_meaning: Amazon estimated total fee; cast if stored as string
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon estimated total fee; cast if stored as string
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.is_active
  name: amazon_fee_preview.is_active
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: is_active
    data_type: boolean
    business_meaning: Active row flag
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mandatory filter.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.zen_status
  name: amazon_fee_preview.zen_status
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: zen_status
    data_type: boolean
    business_meaning: Zen status flag; boolean here
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mandatory/recommended filter per DOCX.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_fee_preview.is_duplicated
  name: amazon_fee_preview.is_duplicated
  fields:
    table: table.zs_observe.amazon_fee_preview
    column_name: is_duplicated
    data_type: boolean
    business_meaning: Duplicate flag; boolean here
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Duplicate flag; boolean here
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.order_id
  name: amazon_returns.order_id
  fields:
    table: table.zs_observe.amazon_returns
    column_name: order_id
    data_type: varchar
    business_meaning: Amazon order ID primary join key
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon order ID primary join key
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.created_date
  name: amazon_returns.created_date
  fields:
    table: table.zs_observe.amazon_returns
    column_name: created_date
    data_type: date
    business_meaning: Record creation date; use for date operations
    semantic_category: date
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Record creation date; use for date operations
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.return_date_str
  name: amazon_returns.return_date_str
  fields:
    table: table.zs_observe.amazon_returns
    column_name: return_date_str
    data_type: varchar
    business_meaning: Return initiation date string; do not use for filtering
    semantic_category: date_string
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Return initiation date string; do not use for filtering
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.sku_id
  name: amazon_returns.sku_id
  fields:
    table: table.zs_observe.amazon_returns
    column_name: sku_id
    data_type: varchar
    business_meaning: Seller SKU
    semantic_category: identifier
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Seller SKU
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.quantity
  name: amazon_returns.quantity
  fields:
    table: table.zs_observe.amazon_returns
    column_name: quantity
    data_type: integer
    business_meaning: Quantity returned
    semantic_category: measure
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Quantity returned
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.return_reason
  name: amazon_returns.return_reason
  fields:
    table: table.zs_observe.amazon_returns
    column_name: return_reason
    data_type: varchar
    business_meaning: Standardized return reason code
    semantic_category: taxonomy
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Standardized return reason code
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.customer_comments
  name: amazon_returns.customer_comments
  fields:
    table: table.zs_observe.amazon_returns
    column_name: customer_comments
    data_type: varchar
    business_meaning: Buyer free-text return comments
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Buyer free-text return comments
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.fulfilment_channel
  name: amazon_returns.fulfilment_channel
  fields:
    table: table.zs_observe.amazon_returns
    column_name: fulfilment_channel
    data_type: varchar
    business_meaning: Amazon FC warehouse code such as YYZ1/LAS2, not AFN/MFN
    semantic_category: location_code
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon FC warehouse code such as YYZ1/LAS2, not AFN/MFN
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.currency_type
  name: amazon_returns.currency_type
  fields:
    table: table.zs_observe.amazon_returns
    column_name: currency_type
    data_type: varchar
    business_meaning: USD or CAD
    semantic_category: currency
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: USD or CAD
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.charged_amount
  name: amazon_returns.charged_amount
  fields:
    table: table.zs_observe.amazon_returns
    column_name: charged_amount
    data_type: decimal(16,4)
    business_meaning: Refund amount inclusive of tax
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Refund amount inclusive of tax
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.charged_amount_excluding_tax
  name: amazon_returns.charged_amount_excluding_tax
  fields:
    table: table.zs_observe.amazon_returns
    column_name: charged_amount_excluding_tax
    data_type: decimal(16,6)
    business_meaning: Refund amount excluding tax
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Refund amount excluding tax
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.shipping_amount
  name: amazon_returns.shipping_amount
  fields:
    table: table.zs_observe.amazon_returns
    column_name: shipping_amount
    data_type: decimal(16,6)
    business_meaning: Return shipping cost
    semantic_category: amount
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Return shipping cost
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.brand
  name: amazon_returns.brand
  fields:
    table: table.zs_observe.amazon_returns
    column_name: brand
    data_type: varchar
    business_meaning: Brand name
    semantic_category: descriptor
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Brand name
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.transaction_type
  name: amazon_returns.transaction_type
  fields:
    table: table.zs_observe.amazon_returns
    column_name: transaction_type
    data_type: varchar
    business_meaning: reverse for customer-initiated return/refund
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: reverse for customer-initiated return/refund
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.internal_transaction_type
  name: amazon_returns.internal_transaction_type
  fields:
    table: table.zs_observe.amazon_returns
    column_name: internal_transaction_type
    data_type: varchar
    business_meaning: refunds for international returns
    semantic_category: status
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: refunds for international returns
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.is_active
  name: amazon_returns.is_active
  fields:
    table: table.zs_observe.amazon_returns
    column_name: is_active
    data_type: boolean
    business_meaning: Active row flag; currently all false
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: No active records until re-ingested.
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.zen_status
  name: amazon_returns.zen_status
  fields:
    table: table.zs_observe.amazon_returns
    column_name: zen_status
    data_type: boolean
    business_meaning: Zen status flag; currently all false
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Zen status flag; currently all false
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.is_duplicated
  name: amazon_returns.is_duplicated
  fields:
    table: table.zs_observe.amazon_returns
    column_name: is_duplicated
    data_type: boolean
    business_meaning: Duplicate flag; currently all false
    semantic_category: quality
    scope_guardrail: marketplace_semantic_column
    evidence_refs:
    - ev.amazon_returns.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Duplicate flag; currently all false
```
```yaml
candidate_card:
  card_type: column
  card_id: column.zs_observe.amazon_returns.group_level_id
  name: amazon_returns.group_level_id
  fields:
    table: table.zs_observe.amazon_returns
    column_name: group_level_id
    data_type: integer
    business_meaning: International group scope column 123 mentioned by DOCX
    semantic_category: scope_column
    scope_guardrail: column_only_not_domain_ownership
    evidence_refs:
    - ev.amazon_returns.columns.001
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Column/caveat only; no account-binding card.
```
### 5.6 Relationship Cards

```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.oms_to_disbursment.order_id
  name: amazon_oms to amazon_disbursment
  fields:
    from_table: table.zs_observe.amazon_oms
    to_table: table.zs_observe.amazon_disbursment
    join_keys: order_id
    relationship_grain: OMS row to aggregated disbursement rows
    business_semantics: Order-level fee breakdown; aggregate disbursement first to avoid row multiplication
    join_safety_rule: Aggregate amazon_disbursment by order_id before joining to amazon_oms.
    evidence_refs:
    - ev.amazon.join_patterns.001
    - ev.amazon_disbursment.purpose.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order-level fee breakdown; aggregate disbursement first to avoid row multiplication
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.oms_to_settlement.order_id
  name: amazon_oms to amazon_settlement
  fields:
    from_table: table.zs_observe.amazon_oms
    to_table: table.zs_observe.amazon_settlement
    join_keys: order_id
    relationship_grain: OMS order to settlement ledger rows
    business_semantics: Settlement waterfall links OMS revenue to settled product sales and net settled amount
    join_safety_rule: Filter settlement type = Order for forward sales comparison; handle timing gaps.
    evidence_refs:
    - ev.amazon.join_patterns.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement waterfall links OMS revenue to settled product sales and net settled amount
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  name: amazon_settlement to amazon_disbursment
  fields:
    from_table: table.zs_observe.amazon_settlement
    to_table: table.zs_observe.amazon_disbursment
    join_keys:
    - order_id
    - settlement_id
    relationship_grain: Settlement ledger to line-level disbursement rows
    business_semantics: Settlement total reconciles to sum charged_amount in disbursement for same order/settlement
    join_safety_rule: Use both order_id and settlement_id when available; account for timing and mapping differences.
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement total reconciles to sum charged_amount in disbursement for same order/settlement
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.fee_preview_to_disbursment.sku
  name: amazon_fee_preview to amazon_disbursment
  fields:
    from_table: table.zs_observe.amazon_fee_preview
    to_table: table.zs_observe.amazon_disbursment
    join_keys: amazon_fee_preview.sku = amazon_disbursment.sku_id
    relationship_grain: SKU-level expected fee to actual fee aggregation
    business_semantics: Expected fee vs actual charged fee by SKU
    join_safety_rule: Aggregate actual ItemFees at SKU level before joining.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected fee vs actual charged fee by SKU
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.fee_preview_to_oms.sku
  name: amazon_fee_preview to amazon_oms
  fields:
    from_table: table.zs_observe.amazon_fee_preview
    to_table: table.zs_observe.amazon_oms
    join_keys: amazon_fee_preview.sku = amazon_oms.sku_id
    relationship_grain: SKU-level fee estimate to order volume and selling price
    business_semantics: Use order volume and selling price to contextualize expected fees
    join_safety_rule: Do not compare one SKU preview row to raw order rows without aggregation.
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use order volume and selling price to contextualize expected fees
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.returns_to_oms.order_id
  name: amazon_returns to amazon_oms
  fields:
    from_table: table.zs_observe.amazon_returns
    to_table: table.zs_observe.amazon_oms
    join_keys: order_id
    relationship_grain: International returns to OMS reverse rows
    business_semantics: International returns table relates to OMS reverse semantics; India returns are in OMS, not returns table
    join_safety_rule: Current returns table inactive; use only when re-ingested.
    evidence_refs:
    - ev.amazon_returns.purpose.001
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: International returns table relates to OMS reverse semantics; India returns are in OMS, not returns table
```
```yaml
candidate_card:
  card_type: relationship
  card_id: relationship.amazon.returns_to_settlement.order_id
  name: amazon_returns to amazon_settlement
  fields:
    from_table: table.zs_observe.amazon_returns
    to_table: table.zs_observe.amazon_settlement
    join_keys: order_id
    relationship_grain: Returns to settlement refund rows
    business_semantics: International return refund rows can be matched to settlement Refund rows
    join_safety_rule: Current returns table inactive; marketplace-internal only.
    evidence_refs:
    - ev.amazon_returns.purpose.001
    - ev.amazon_returns.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: International return refund rows can be matched to settlement Refund rows
```
### 5.7 Value Profile Cards

```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_oms.transaction_type
  name: Value profile for amazon_oms.transaction_type
  fields:
    column: column.zs_observe.amazon_oms.transaction_type
    known_values:
    - forward
    - reverse
    - cancel
    - replacement
    - einvoicecancel
    - 'null'
    value_semantics: forward=positive shipped sale; reverse=negative customer return; cancel=zero pre-ship cancellation; replacement=zero replacement; einvoicecancel=zero GST e-invoice
      cancellation; null=international rows
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: forward=positive shipped sale; reverse=negative customer return; cancel=zero pre-ship cancellation; replacement=zero replacement; einvoicecancel=zero GST e-invoice
      cancellation; null=international rows
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_oms.metadata
  name: Value profile for amazon_oms.metadata
  fields:
    column: column.zs_observe.amazon_oms.metadata
    known_values:
    - B2C
    - B2B
    - 'NULL'
    value_semantics: B2C=India retail; B2B=India business buyer; NULL=International
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: B2C=India retail; B2B=India business buyer; NULL=International
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_oms.fulfilment_channel
  name: Value profile for amazon_oms.fulfilment_channel
  fields:
    column: column.zs_observe.amazon_oms.fulfilment_channel
    known_values:
    - AFN
    - MFN
    value_semantics: AFN and MFN fulfilment channel semantics
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: AFN and MFN fulfilment channel semantics
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_oms.fulfilment_type
  name: Value profile for amazon_oms.fulfilment_type
  fields:
    column: column.zs_observe.amazon_oms.fulfilment_type
    known_values:
    - FBA
    - Other
    - Easyship
    value_semantics: FBA, Other, Easyship fulfilment type semantics
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: FBA, Other, Easyship fulfilment type semantics
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_oms.zone
  name: Value profile for amazon_oms.zone
  fields:
    column: column.zs_observe.amazon_oms.zone
    known_values:
    - Local
    - Regional
    - National
    - Remote
    value_semantics: Delivery-zone cost tier semantics
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Delivery-zone cost tier semantics
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_settlement.type
  name: Value profile for amazon_settlement.type
  fields:
    column: column.zs_observe.amazon_settlement.type
    known_values:
    - Order
    - Refund
    - Fulfilment Fee Refund
    - Adjustment
    - Service Fee
    - FBA Inventory Fee
    - SAFE-T Reimbursement
    - Reimbursements
    - Transfer
    - Clawbacks
    - Others
    - 'NULL'
    value_semantics: Settlement ledger transaction type and revenue/cash-flow semantics including NULL rows
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement ledger transaction type and revenue/cash-flow semantics including NULL rows
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_disbursment.mp_fee_type
  name: Value profile for amazon_disbursment.mp_fee_type
  fields:
    column: column.zs_observe.amazon_disbursment.mp_fee_type
    known_values:
    - ItemPrice
    - ItemFees
    - Promotion
    - ItemTCS
    - ItemTDS
    - Item Fee Adjustment
    - Other Transactions
    - FBA Inventory Reimbursement
    - other-transaction
    value_semantics: First-level fee/revenue/tax/promotion/reimbursement taxonomy
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: First-level fee/revenue/tax/promotion/reimbursement taxonomy
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_disbursment.charged_amount_type
  name: Value profile for amazon_disbursment.charged_amount_type
  fields:
    column: column.zs_observe.amazon_disbursment.charged_amount_type
    known_values:
    - principal
    - product tax
    - shipping
    - shipping tax
    - cod
    - cod tax
    - commission
    - shipping fee
    - closing fee
    - tech fee
    - pickup fee
    - shipping chargeback
    - refund commission
    - tcs gst
    - tds
    - reimbursement
    - fba inventory
    - removal complete
    value_semantics: Specific line-item fee/price/tax/reimbursement taxonomy
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Specific line-item fee/price/tax/reimbursement taxonomy
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_disbursment.transaction_type
  name: Value profile for amazon_disbursment.transaction_type
  fields:
    column: column.zs_observe.amazon_disbursment.transaction_type
    known_values:
    - Order
    - Refund
    - Fulfillment Fee Refund
    - SAFE-T Reimbursement
    - Other
    - other-transaction
    value_semantics: Disbursement transaction event type for correct sign interpretation
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Disbursement transaction event type for correct sign interpretation
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_fee_preview.amazon_store
  name: Value profile for amazon_fee_preview.amazon_store
  fields:
    column: column.zs_observe.amazon_fee_preview.amazon_store
    known_values: IN
    value_semantics: Amazon store/marketplace indicator for expected-fee preview
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon store/marketplace indicator for expected-fee preview
```
```yaml
candidate_card:
  card_type: value_profile
  card_id: value_profile.zs_observe.amazon_returns.return_reason
  name: Value profile for amazon_returns.return_reason
  fields:
    column: column.zs_observe.amazon_returns.return_reason
    known_values:
    - QUALITY_UNACCEPTABLE
    - DEFECTIVE
    - MISSING_PARTS
    - NOT_AS_DESCRIBED
    - NOT_COMPATIBLE
    - APPAREL_TOO_LARGE
    - APPAREL_TOO_SMALL
    - POOR_FIT
    - UNWANTED_ITEM
    - ORDERED_WRONG_ITEM
    - FOUND_BETTER_PRICE
    - NEVER_ARRIVED
    - MISSED_ESTIMATED_DELIVERY
    - UNDELIVERABLE_UNKNOWN
    - UNDELIVERABLE_REFUSED
    - DAMAGED_BY_CARRIER
    - DAMAGED_BY_FC
    - SWITCHEROO
    - UNAUTHORIZED_PURCHASE
    - NO_REASON_GIVEN
    value_semantics: International return reason taxonomy grouped by controllability and cause
    unknown_or_null_handling: explicitly documented; do not drop NULL values unless rule says so
    evidence_refs:
    - ev.amazon_returns.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: International return reason taxonomy grouped by controllability and cause
```
### 5.8 Metric Cards with Colloquial Names

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.gross_revenue
  name: Gross revenue
  fields:
    metric_key: gross_revenue
    business_definition: Total forward sales value including tax.
    colloquial_names:
    - Gross revenue
    - GMV
    - gross sales
    - topline
    - sales
    metric_pattern: sum_amount_filtered_positive_sale
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Total forward sales value including tax.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.net_revenue
  name: Net revenue
  fields:
    metric_key: net_revenue
    business_definition: Revenue after returns using forward plus reverse rows.
    colloquial_names:
    - Net revenue
    - net sales
    - sales after returns
    metric_pattern: sum_amount_netting_reversals
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Revenue after returns using forward plus reverse rows.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.taxable_revenue
  name: Taxable revenue
  fields:
    metric_key: taxable_revenue
    business_definition: Revenue excluding GST used for profitability and tax-rate denominator checks.
    colloquial_names:
    - Taxable revenue
    - pre-GST revenue
    - revenue excluding tax
    metric_pattern: sum_excluding_tax_forward
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Revenue excluding GST used for profitability and tax-rate denominator checks.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.principal_revenue
  name: Principal revenue
  fields:
    metric_key: principal_revenue
    business_definition: Base item revenue from disbursement principal lines.
    colloquial_names:
    - Principal revenue
    - item principal
    - base sales
    metric_pattern: sum_disbursement_principal_lines
    default_grain: order_item
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Base item revenue from disbursement principal lines.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.average_order_value
  name: Average order value
  fields:
    metric_key: average_order_value
    business_definition: Gross forward revenue divided by distinct forward orders.
    colloquial_names:
    - AOV
    - average basket value
    - average order size
    metric_pattern: sum_amount_over_distinct_orders
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Gross forward revenue divided by distinct forward orders.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.revenue_per_unit
  name: Revenue per unit
  fields:
    metric_key: revenue_per_unit
    business_definition: Gross revenue divided by sold quantity.
    colloquial_names:
    - RPU
    - revenue per item
    - unit revenue
    metric_pattern: sum_amount_over_quantity
    default_grain: item
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Gross revenue divided by sold quantity.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.effective_commission_rate
  name: Effective commission rate
  fields:
    metric_key: effective_commission_rate
    business_definition: Absolute commission divided by principal.
    colloquial_names:
    - Commission rate
    - referral fee rate
    - effective referral rate
    metric_pattern: absolute_fee_sum_over_principal
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Absolute commission divided by principal.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.effective_fee_rate
  name: Effective fee rate
  fields:
    metric_key: effective_fee_rate
    business_definition: All fees as percentage of principal.
    colloquial_names:
    - Fee rate
    - marketplace fee rate
    - take rate
    metric_pattern: absolute_total_fee_over_principal
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: All fees as percentage of principal.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.marketplace_shipping_cost_rate
  name: Marketplace shipping cost rate
  fields:
    metric_key: marketplace_shipping_cost_rate
    business_definition: Amazon shipping/weight handling fee as percentage of principal.
    colloquial_names:
    - Logistics cost rate
    - shipping fee rate
    - weight handling rate
    metric_pattern: absolute_shipping_fee_over_principal
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon shipping/weight handling fee as percentage of principal.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.fee_burden
  name: Fee burden
  fields:
    metric_key: fee_burden
    business_definition: Marketplace fee burden as percentage of gross revenue or SKU charged amount.
    colloquial_names:
    - Fee burden
    - fee load
    - fee pressure
    metric_pattern: gross_commission_over_revenue
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace fee burden as percentage of gross revenue or SKU charged amount.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.forward_fee
  name: Forward fee
  fields:
    metric_key: forward_fee
    business_definition: Total forward fee applied on product for forward transactions.
    colloquial_names:
    - Forward fee
    - order fee
    - fee on sale
    metric_pattern: absolute_commission_forward_filter
    default_grain: order_item
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Total forward fee applied on product for forward transactions.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.seller_realization_rate
  name: Seller realization rate
  fields:
    metric_key: seller_realization_rate
    business_definition: Percentage of gross product sales received as settlement after deductions.
    colloquial_names:
    - Realization rate
    - seller payout rate
    - net realization
    - received percentage
    metric_pattern: net_settlement_over_gross_product_sales
    default_grain: settlement_period
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Percentage of gross product sales received as settlement after deductions.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.net_settlement_per_order
  name: Net settlement per order
  fields:
    metric_key: net_settlement_per_order
    business_definition: Average cash received per order.
    colloquial_names:
    - Net settlement per order
    - average payout per order
    metric_pattern: net_settlement_over_distinct_orders
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Average cash received per order.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.fee_recovery_rate
  name: Fee recovery rate
  fields:
    metric_key: fee_recovery_rate
    business_definition: Percentage of charged fees recovered on returns.
    colloquial_names:
    - Fee recovery
    - recovered fee rate
    - return fee recovery
    metric_pattern: reversed_fees_over_charged_fees
    default_grain: fee_type
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Percentage of charged fees recovered on returns.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_rate
  name: Return rate
  fields:
    metric_key: return_rate
    business_definition: Returned orders divided by forward orders.
    colloquial_names:
    - Return rate
    - returns percentage
    - refund rate
    metric_pattern: reverse_count_over_forward_count
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Returned orders divided by forward orders.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.cancellation_rate
  name: Cancellation rate
  fields:
    metric_key: cancellation_rate
    business_definition: Cancelled orders divided by forward plus cancelled orders.
    colloquial_names:
    - Cancellation rate
    - cancel percentage
    metric_pattern: cancel_count_over_forward_plus_cancel_count
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Cancelled orders divided by forward plus cancelled orders.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.net_revenue_per_forward_order
  name: Net revenue per forward order
  fields:
    metric_key: net_revenue_per_forward_order
    business_definition: Net revenue accounting for returns divided by forward order count.
    colloquial_names:
    - Net revenue per order
    - net AOV after returns
    metric_pattern: net_forward_reverse_revenue_over_forward_orders
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Net revenue accounting for returns divided by forward order count.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_value_rate
  name: Return value rate
  fields:
    metric_key: return_value_rate
    business_definition: Average absolute return value divided by average forward value.
    colloquial_names:
    - Return value rate
    - high-value return ratio
    metric_pattern: avg_abs_reverse_amount_over_avg_forward_amount
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Average absolute return value divided by average forward value.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.effective_tax_rate
  name: Effective tax rate
  fields:
    metric_key: effective_tax_rate
    business_definition: GST tax amount over charged_amount_excluding_tax.
    colloquial_names:
    - GST rate
    - effective GST rate
    - tax rate check
    metric_pattern: tax_over_excluding_tax_amount
    default_grain: order
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: GST tax amount over charged_amount_excluding_tax.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.discount_depth
  name: Discount depth
  fields:
    metric_key: discount_depth
    business_definition: Promotional discount divided by item amount excluding tax.
    colloquial_names:
    - Discount depth
    - promo depth
    - discount rate
    metric_pattern: promo_discount_over_item_amount_excluding_tax
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotional discount divided by item amount excluding tax.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.safe_t_recovery_rate
  name: SAFE-T recovery rate
  fields:
    metric_key: safe_t_recovery_rate
    business_definition: SAFE-T credits divided by eligible return refund value.
    colloquial_names:
    - SAFE-T recovery
    - reimbursement recovery rate
    metric_pattern: safe_t_credits_over_eligible_return_value
    default_grain: return
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.safet.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SAFE-T credits divided by eligible return refund value.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.return_loss
  name: Return loss
  fields:
    metric_key: return_loss
    business_definition: Refunded principal plus permanent/non-recovered fee components.
    colloquial_names:
    - Return loss
    - true return cost
    - return margin hit
    metric_pattern: refunded_principal_plus_non_recovered_fees
    default_grain: return
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Refunded principal plus permanent/non-recovered fee components.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.volumetric_excess_percent
  name: Volumetric excess percent
  fields:
    metric_key: volumetric_excess_percent
    business_definition: Volumetric weight excess over gross weight.
    colloquial_names:
    - Volumetric gap
    - packaging inefficiency
    - billable weight gap
    metric_pattern: volumetric_weight_over_gross_weight_minus_one
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.packaging_weight.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Volumetric weight excess over gross weight.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.advertising_spend
  name: Advertising spend
  fields:
    metric_key: advertising_spend
    business_definition: Advertising service fee rows summed from settlement.
    colloquial_names:
    - Ad spend
    - advertising fees
    - sponsored ads cost
    metric_pattern: service_fee_advertising_sum
    default_grain: month
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Advertising service fee rows summed from settlement.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.tds_tcs_deductions
  name: TDS/TCS deductions
  fields:
    metric_key: tds_tcs_deductions
    business_definition: Marketplace deducted TDS and TCS amounts by period.
    colloquial_names:
    - Tax deductions
    - TDS/TCS loss
    - withheld taxes
    metric_pattern: sum_tds_plus_tcs_marketplace_fields
    default_grain: month
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deducted TDS and TCS amounts by period.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.settlement_cash_position
  name: Settlement cash position
  fields:
    metric_key: settlement_cash_position
    business_definition: Net total across all settlement row types for latest or selected settlement period.
    colloquial_names:
    - Cash position
    - settlement payout
    - net cash after settlement
    metric_pattern: sum_total_all_settlement_types
    default_grain: settlement_period
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Net total across all settlement row types for latest or selected settlement period.
```
```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.actual_fee_variance
  name: Actual fee variance
  fields:
    metric_key: actual_fee_variance
    business_definition: Expected fee plus actual fee because actual ItemFees are negative.
    colloquial_names:
    - Fee variance
    - overcharge
    - expected vs actual fee gap
    metric_pattern: expected_fee_plus_negative_actual_fee
    default_grain: sku
    domain: domain.marketplace.amazon.orders; domain.marketplace.amazon.settlement; domain.marketplace.amazon.fees; domain.marketplace.amazon.returns
    scope: generic marketplace metric implemented by Amazon-specific metric_implementation cards
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected fee plus actual fee because actual ItemFees are negative.
```
### 5.9 Amazon-Specific Metric Implementation Cards

```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.gross_revenue
  name: 'Amazon implementation: gross_revenue on amazon_oms'
  fields:
    implements_metric: metric.marketplace.gross_revenue
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(charged_amount)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: order
    sql_ref: sql.amazon.oms.gross_revenue
    metric_pattern: sum_amount_filtered_positive_sale
    notes: Includes GST and shipping; use forward only.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Includes GST and shipping; use forward only.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.net_revenue
  name: 'Amazon implementation: net_revenue on amazon_oms'
  fields:
    implements_metric: metric.marketplace.net_revenue
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(charged_amount)
    required_filters: is_active = true AND transaction_type IN ('forward', 'reverse')
    grain: order
    sql_ref: sql.amazon.oms.net_revenue
    metric_pattern: sum_amount_netting_reversals
    notes: Reverse rows are negative and auto-net.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Reverse rows are negative and auto-net.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  name: 'Amazon implementation: taxable_revenue on amazon_oms'
  fields:
    implements_metric: metric.marketplace.taxable_revenue
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(charged_amount_excluding_tax)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: order
    sql_ref: sql.amazon.oms.taxable_revenue
    metric_pattern: sum_excluding_tax_forward
    notes: Use for profitability and tax-rate verification.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use for profitability and tax-rate verification.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  name: 'Amazon implementation: principal_revenue on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.principal_revenue
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: SUM(CASE WHEN mp_fee_type = 'ItemPrice' AND charged_amount_type = 'principal' THEN charged_amount ELSE 0 END)
    required_filters: is_active = true
    grain: order_item
    sql_ref: sql.amazon.disbursement.principal_revenue
    metric_pattern: sum_disbursement_principal_lines
    notes: Principal lines only.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Principal lines only.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.average_order_value
  name: 'Amazon implementation: average_order_value on amazon_oms'
  fields:
    implements_metric: metric.marketplace.average_order_value
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(charged_amount) / COUNT(DISTINCT order_id)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: order
    sql_ref: sql.amazon.oms.average_order_value
    metric_pattern: sum_amount_over_distinct_orders
    notes: Forward orders only.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Forward orders only.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  name: 'Amazon implementation: revenue_per_unit on amazon_oms'
  fields:
    implements_metric: metric.marketplace.revenue_per_unit
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(charged_amount) / SUM(quantity)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: item
    sql_ref: sql.amazon.oms.revenue_per_unit
    metric_pattern: sum_amount_over_quantity
    notes: DOCX defines metric but OMS column list in available text does not clearly evidence quantity; keep review item open.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: DOCX defines metric but OMS column list in available text does not clearly evidence quantity; keep review item open.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  name: 'Amazon implementation: effective_commission_rate on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.effective_commission_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: ABS(SUM(CASE WHEN mp_fee_type = 'ItemFees' AND charged_amount_type = 'commission' THEN charged_amount ELSE 0 END)) / NULLIF(SUM(CASE WHEN mp_fee_type = 'ItemPrice' AND charged_amount_type
      = 'principal' THEN charged_amount ELSE 0 END), 0)
    required_filters: is_active = true AND transaction_type = 'Order'
    grain: sku
    sql_ref: sql.amazon.disbursement.effective_commission_by_sku
    metric_pattern: absolute_fee_sum_over_principal
    notes: Use transaction_type context to avoid refund commission double-counting.
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    - ev.amazon_disbursment.taxonomy.001
    - ev.amazon_disbursment.queries.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use transaction_type context to avoid refund commission double-counting.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  name: 'Amazon implementation: effective_fee_rate on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.effective_fee_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: ABS(SUM(CASE WHEN mp_fee_type = 'ItemFees' THEN charged_amount ELSE 0 END)) / NULLIF(SUM(CASE WHEN mp_fee_type = 'ItemPrice' AND charged_amount_type = 'principal' THEN charged_amount
      ELSE 0 END), 0)
    required_filters: is_active = true AND transaction_type = 'Order'
    grain: sku
    sql_ref: sql.amazon.disbursement.fee_breakdown_summary
    metric_pattern: absolute_total_fee_over_principal
    notes: All ItemFees as percentage of principal.
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: All ItemFees as percentage of principal.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  name: 'Amazon implementation: marketplace_shipping_cost_rate on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.marketplace_shipping_cost_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: ABS(SUM(CASE WHEN mp_fee_type = 'ItemFees' AND charged_amount_type IN ('shipping fee', 'shipping chargeback') THEN charged_amount ELSE 0 END)) / NULLIF(SUM(CASE WHEN mp_fee_type
      = 'ItemPrice' AND charged_amount_type = 'principal' THEN charged_amount ELSE 0 END), 0)
    required_filters: is_active = true AND transaction_type = 'Order'
    grain: sku
    sql_ref: sql.amazon.disbursement.shipping_cost_rate
    metric_pattern: absolute_shipping_fee_over_principal
    notes: Marketplace shipping/weight handling semantics only; not external logistics.
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace shipping/weight handling semantics only; not external logistics.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  name: 'Amazon implementation: fee_burden on amazon_fee_preview'
  fields:
    implements_metric: metric.marketplace.fee_burden
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_fee_preview
    formula: gross_commission / NULLIF(charged_amount, 0)
    required_filters: is_active = true AND zen_status = true
    grain: sku
    sql_ref: sql.amazon.fee_preview.sku_fee_summary
    metric_pattern: gross_commission_over_revenue
    notes: SKU-level estimate; not actual fee.
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SKU-level estimate; not actual fee.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  name: 'Amazon implementation: forward_fee on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.forward_fee
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: ABS(SUM(CASE WHEN mp_fee_type = 'ItemFees' AND transaction_type = 'Order' THEN charged_amount ELSE 0 END))
    required_filters: is_active = true
    grain: order_item
    sql_ref: sql.amazon.disbursement.forward_fee
    metric_pattern: absolute_commission_forward_filter
    notes: Forward fees on Order transactions.
    evidence_refs:
    - ev.amazon.kpi.fee_cost.001
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Forward fees on Order transactions.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  name: 'Amazon implementation: seller_realization_rate on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.seller_realization_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(total) / NULLIF(SUM(CASE WHEN type = 'Order' THEN product_sales ELSE 0 END), 0)
    required_filters: is_active = true
    grain: settlement_period
    sql_ref: sql.amazon.settlement.realization_rate
    metric_pattern: net_settlement_over_gross_product_sales
    notes: No hardcoded group_level_id; runtime scope should be external.
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: No hardcoded group_level_id; runtime scope should be external.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  name: 'Amazon implementation: net_settlement_per_order on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.net_settlement_per_order
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(settled_amount) / COUNT(DISTINCT order_id)
    required_filters: is_active = true
    grain: order
    sql_ref: sql.amazon.settlement.net_settlement_per_order
    metric_pattern: net_settlement_over_distinct_orders
    notes: Use settlement rows at appropriate scope.
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use settlement rows at appropriate scope.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  name: 'Amazon implementation: fee_recovery_rate on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.fee_recovery_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: SUM(reversed fees + fulfillment fee refunds) / NULLIF(SUM(charged fees), 0)
    required_filters: is_active = true; transaction_type context required
    grain: fee_type
    sql_ref: sql.amazon.disbursement.fee_recovery_on_returns
    metric_pattern: reversed_fees_over_charged_fees
    notes: Varies by fee type; create fee-type level outputs.
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    - ev.amazon_disbursment.transaction_types.001
    - ev.amazon_disbursment.queries.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Varies by fee type; create fee-type level outputs.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.return_rate
  name: 'Amazon implementation: return_rate on amazon_oms'
  fields:
    implements_metric: metric.marketplace.return_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: COUNT(DISTINCT order_id) FILTER (WHERE transaction_type = 'reverse') / NULLIF(COUNT(DISTINCT order_id) FILTER (WHERE transaction_type = 'forward'), 0)
    required_filters: is_active = true
    grain: sku
    sql_ref: sql.amazon.oms.return_rate_by_sku
    metric_pattern: reverse_count_over_forward_count
    notes: India returns in OMS reverse rows.
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    - ev.amazon_oms.transaction_types.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: India returns in OMS reverse rows.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  name: 'Amazon implementation: cancellation_rate on amazon_oms'
  fields:
    implements_metric: metric.marketplace.cancellation_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: COUNT(DISTINCT order_id) FILTER (WHERE transaction_type = 'cancel') / NULLIF(COUNT(DISTINCT order_id) FILTER (WHERE transaction_type IN ('forward', 'cancel')), 0)
    required_filters: is_active = true
    grain: sku
    sql_ref: sql.amazon.oms.cancellation_rate
    metric_pattern: cancel_count_over_forward_plus_cancel_count
    notes: Cancel rows are zero-value and common by volume.
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Cancel rows are zero-value and common by volume.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  name: 'Amazon implementation: net_revenue_per_forward_order on amazon_oms'
  fields:
    implements_metric: metric.marketplace.net_revenue_per_forward_order
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(CASE WHEN transaction_type IN ('forward', 'reverse') THEN charged_amount ELSE 0 END) / NULLIF(COUNT(DISTINCT CASE WHEN transaction_type='forward' THEN order_id END),
      0)
    required_filters: is_active = true
    grain: order
    sql_ref: sql.amazon.oms.net_revenue_per_forward_order
    metric_pattern: net_forward_reverse_revenue_over_forward_orders
    notes: Accounts for return loss at order level.
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Accounts for return loss at order level.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.return_value_rate
  name: 'Amazon implementation: return_value_rate on amazon_oms'
  fields:
    implements_metric: metric.marketplace.return_value_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: AVG(ABS(CASE WHEN transaction_type='reverse' THEN charged_amount END)) / NULLIF(AVG(CASE WHEN transaction_type='forward' THEN charged_amount END), 0)
    required_filters: is_active = true
    grain: sku
    sql_ref: sql.amazon.oms.return_value_rate
    metric_pattern: avg_abs_reverse_amount_over_avg_forward_amount
    notes: Use to see whether higher-value items are returned more.
    evidence_refs:
    - ev.amazon.kpi.return_cancel.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use to see whether higher-value items are returned more.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  name: 'Amazon implementation: effective_tax_rate on amazon_oms'
  fields:
    implements_metric: metric.marketplace.effective_tax_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(total_tax) / NULLIF(SUM(charged_amount_excluding_tax), 0)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: order
    sql_ref: sql.amazon.oms.gst_breakdown
    metric_pattern: tax_over_excluding_tax_amount
    notes: Use excluding-tax denominator; charged_amount denominator gives lower structural rate.
    evidence_refs:
    - ev.amazon.gst.001
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use excluding-tax denominator; charged_amount denominator gives lower structural rate.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_oms.discount_depth
  name: 'Amazon implementation: discount_depth on amazon_oms'
  fields:
    implements_metric: metric.marketplace.discount_depth
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_oms
    formula: SUM(item_promo_discount) / NULLIF(SUM(item_amount_excluding_tax), 0)
    required_filters: is_active = true AND transaction_type = 'forward'
    grain: sku
    sql_ref: sql.amazon.oms.discount_depth
    metric_pattern: promo_discount_over_item_amount_excluding_tax
    notes: Promotional margin impact.
    evidence_refs:
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Promotional margin impact.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  name: 'Amazon implementation: safe_t_recovery_rate on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.safe_t_recovery_rate
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(CASE WHEN type = 'SAFE-T Reimbursement' THEN total ELSE 0 END) / NULLIF(SUM(eligible return refund value), 0)
    required_filters: is_active = true
    grain: return
    sql_ref: sql.amazon.settlement.reimbursements_safet
    metric_pattern: safe_t_credits_over_eligible_return_value
    notes: Eligible-return denominator requires business review.
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Eligible-return denominator requires business review.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_disbursment.return_loss
  name: 'Amazon implementation: return_loss on amazon_disbursment'
  fields:
    implements_metric: metric.marketplace.return_loss
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_disbursment
    formula: principal_refunded + shipping_fee_non_recovered + tech_fee_non_recovered + pickup_fee_non_recovered + unrecovered_commission + unrecovered_closing_fee + unrecovered_tcs_timing_loss
    required_filters: is_active = true; transaction_type IN ('Refund', 'Order', 'Fulfillment Fee Refund')
    grain: return
    sql_ref: sql.amazon.disbursement.return_loss
    metric_pattern: refunded_principal_plus_non_recovered_fees
    notes: Formula is a framework; component extraction needs fee-type mapping.
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Formula is a framework; component extraction needs fee-type mapping.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  name: 'Amazon implementation: volumetric_excess_percent on amazon_fee_preview'
  fields:
    implements_metric: metric.marketplace.volumetric_excess_percent
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_fee_preview
    formula: (volumetric_weight / NULLIF(gross_weight, 0)) - 1
    required_filters: is_active = true AND zen_status = true
    grain: sku
    sql_ref: sql.amazon.fee_preview.volumetric_gap
    metric_pattern: volumetric_weight_over_gross_weight_minus_one
    notes: Flag SKUs where volumetric_weight > gross_weight * 1.5.
    evidence_refs:
    - ev.amazon.packaging_weight.001
    - ev.amazon_fee_preview.weights.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Flag SKUs where volumetric_weight > gross_weight * 1.5.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  name: 'Amazon implementation: advertising_spend on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.advertising_spend
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(total)
    required_filters: is_active = true AND type = 'Service Fee' AND description LIKE '%Advertising%'
    grain: month
    sql_ref: sql.amazon.settlement.advertising_spend
    metric_pattern: service_fee_advertising_sum
    notes: Marketplace service-fee rows only.
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace service-fee rows only.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  name: 'Amazon implementation: tds_tcs_deductions on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.tds_tcs_deductions
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(tds) + SUM(tcs_igst + tcs_cgst + tcs_sgst)
    required_filters: is_active = true
    grain: month
    sql_ref: sql.amazon.settlement.tds_tcs_deductions
    metric_pattern: sum_tds_plus_tcs_marketplace_fields
    notes: Marketplace deduction fields only; not statutory filing.
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    - ev.amazon_settlement.columns.001
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Marketplace deduction fields only; not statutory filing.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  name: 'Amazon implementation: settlement_cash_position on amazon_settlement'
  fields:
    implements_metric: metric.marketplace.settlement_cash_position
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_settlement
    formula: SUM(total)
    required_filters: is_active = true; selected latest or runtime settlement_id
    grain: settlement_period
    sql_ref: sql.amazon.settlement.cash_position
    metric_pattern: sum_total_all_settlement_types
    notes: All type values affect payout; do not restrict to revenue types for cash flow.
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    - ev.amazon.settlement_cycle.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: All type values affect payout; do not restrict to revenue types for cash flow.
```
```yaml
candidate_card:
  card_type: metric_implementation
  card_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  name: 'Amazon implementation: actual_fee_variance on amazon_fee_preview'
  fields:
    implements_metric: metric.marketplace.actual_fee_variance
    platform_context: platform_context.amazon.in
    source_tables: table.zs_observe.amazon_fee_preview
    formula: amazon_fee_preview.gross_commission + SUM(actual ItemFees from amazon_disbursment)
    required_filters: fee_preview.is_active = true AND fee_preview.zen_status = true; disbursement.is_active = true; aggregate by sku_id before join
    grain: sku
    sql_ref: sql.amazon.fee_preview.expected_vs_actual
    metric_pattern: expected_fee_plus_negative_actual_fee
    notes: Actual ItemFees are negative, so expected + actual yields variance.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Actual ItemFees are negative, so expected + actual yields variance.
```
### 5.10 Formula Template Cards

```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_oms_revenue_formula
  name: OMS charged amount formula
  fields:
    formula_key: amazon_oms_revenue_formula
    formula_expression: charged_amount = item_amount_excluding_tax + total_tax + shipping_amount + gift_wrap_amount - item_promo_discount - shipping_promo_discount - gift_wrap_promo_discount
    platform_context: platform_context.amazon.in
    notes: Revenue decomposition as documented; gift-wrap columns may be present even if not enumerated in compact column list.
    evidence_refs:
    - ev.amazon_oms.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Revenue decomposition as documented; gift-wrap columns may be present even if not enumerated in compact column list.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_return_rate
  name: Amazon OMS return rate
  fields:
    formula_key: amazon_return_rate
    formula_expression: COUNT(DISTINCT reverse order_id) / NULLIF(COUNT(DISTINCT forward order_id), 0)
    platform_context: platform_context.amazon.in
    notes: Use transaction_type values only after is_active filter.
    evidence_refs:
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use transaction_type values only after is_active filter.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_cancellation_rate
  name: Amazon OMS cancellation rate
  fields:
    formula_key: amazon_cancellation_rate
    formula_expression: COUNT(DISTINCT cancel order_id) / NULLIF(COUNT(DISTINCT forward or cancel order_id), 0)
    platform_context: platform_context.amazon.in
    notes: Cancel rows are zero-value and common.
    evidence_refs:
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Cancel rows are zero-value and common.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_effective_tax_rate
  name: Amazon effective GST rate
  fields:
    formula_key: amazon_effective_tax_rate
    formula_expression: SUM(total_tax) / NULLIF(SUM(charged_amount_excluding_tax), 0)
    platform_context: platform_context.amazon.in
    notes: Do not divide by charged_amount for tax rate verification.
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not divide by charged_amount for tax rate verification.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_settlement_total
  name: Amazon India settlement total formula
  fields:
    formula_key: amazon_settlement_total
    formula_expression: total ≈ product_sales + selling_fees + fba_fees + shipping_credits + promotional_rebates + gift_wrap_credits + other_transaction_fees + other - tcs_igst - tcs_cgst
      - tcs_sgst - tds
    platform_context: platform_context.amazon.in
    notes: Formula from settlement section; sign conventions must be preserved.
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Formula from settlement section; sign conventions must be preserved.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_seller_realization_rate
  name: Amazon seller realization rate
  fields:
    formula_key: amazon_seller_realization_rate
    formula_expression: SUM(total) / NULLIF(SUM(CASE WHEN type = 'Order' THEN product_sales ELSE 0 END), 0)
    platform_context: platform_context.amazon.in
    notes: No hardcoded group_level_id in canonical implementation.
    evidence_refs:
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: No hardcoded group_level_id in canonical implementation.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_fee_preview_total_fee
  name: Amazon fee-preview total fee estimate
  fields:
    formula_key: amazon_fee_preview_total_fee
    formula_expression: gross_commission as expected total fee estimate; component fields include referral_fee, fixed_fee, pick_and_pack_fee, shipping_amount
    platform_context: platform_context.amazon.in
    notes: Use component detail for diagnostics.
    evidence_refs:
    - ev.amazon_fee_preview.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use component detail for diagnostics.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_fee_variance
  name: Amazon expected vs actual fee variance
  fields:
    formula_key: amazon_fee_variance
    formula_expression: expected_fee + actual_fee because actual ItemFees are negative
    platform_context: platform_context.amazon.in
    notes: Aggregate actual fees by SKU before comparison.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Aggregate actual fees by SKU before comparison.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_volumetric_weight
  name: Amazon volumetric weight
  fields:
    formula_key: amazon_volumetric_weight
    formula_expression: volumetric_weight = (longest_side × median_side × shortest_side) / 5000
    platform_context: platform_context.amazon.in
    notes: Dimensions in cm; compare against gross_weight for billable weight.
    evidence_refs:
    - ev.amazon.packaging_weight.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Dimensions in cm; compare against gross_weight for billable weight.
```
```yaml
candidate_card:
  card_type: formula_template
  card_id: formula_template.amazon.amazon_return_loss
  name: Amazon true return loss
  fields:
    formula_key: amazon_return_loss
    formula_expression: principal_refunded + shipping_fee_non_recoverable + tech_fee_non_recoverable + pick_pack_fee_non_recoverable + approx 50% commission + approx 58% closing_fee
      + approx 60% TCS timing loss
    platform_context: platform_context.amazon.in
    notes: Framework formula; component availability varies.
    evidence_refs:
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Framework formula; component availability varies.
```
### 5.11 Metric Dependency Cards

```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.amazon.net_revenue_depends_on_gross_revenue
  name: 'Amazon metric dependency: net_revenue_depends_on_gross_revenue'
  fields:
    from_metric: metric.marketplace.net_revenue
    dependency_relationship: DEPENDS_ON
    to_metric: metric.marketplace.gross_revenue
    dependency_notes: Net revenue is forward/reverse netting of gross revenue semantics.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Net revenue is forward/reverse netting of gross revenue semantics.
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.amazon.aov_depends_on_gross_revenue
  name: 'Amazon metric dependency: aov_depends_on_gross_revenue'
  fields:
    from_metric: metric.marketplace.average_order_value
    dependency_relationship: DEPENDS_ON
    to_metric: metric.marketplace.gross_revenue
    dependency_notes: AOV numerator is forward gross revenue.
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: AOV numerator is forward gross revenue.
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.amazon.return_loss_depends_on_return_rate
  name: 'Amazon metric dependency: return_loss_depends_on_return_rate'
  fields:
    from_metric: metric.marketplace.return_loss
    dependency_relationship: RELATED_TO
    to_metric: metric.marketplace.return_rate
    dependency_notes: Return loss analysis depends on identifying returned orders and fee recovery.
    evidence_refs:
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Return loss analysis depends on identifying returned orders and fee recovery.
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.amazon.seller_realization_depends_on_settlement_cash_position
  name: 'Amazon metric dependency: seller_realization_depends_on_settlement_cash_position'
  fields:
    from_metric: metric.marketplace.seller_realization_rate
    dependency_relationship: RELATED_TO
    to_metric: metric.marketplace.settlement_cash_position
    dependency_notes: Both use settlement total but realization divides by product_sales orders.
    evidence_refs:
    - ev.amazon.kpi.settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Both use settlement total but realization divides by product_sales orders.
```
```yaml
candidate_card:
  card_type: metric_dependency
  card_id: metric_dependency.amazon.actual_fee_variance_depends_on_effective_fee_rate
  name: 'Amazon metric dependency: actual_fee_variance_depends_on_effective_fee_rate'
  fields:
    from_metric: metric.marketplace.actual_fee_variance
    dependency_relationship: RELATED_TO
    to_metric: metric.marketplace.effective_fee_rate
    dependency_notes: Both compare actual fee behavior; variance uses fee preview expected values.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Both compare actual fee behavior; variance uses fee preview expected values.
```
### 5.12 Business Process Cards

```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.amazon.order_to_settlement
  name: Amazon order to settlement lifecycle
  fields:
    process_key: order_to_settlement
    platform_context: platform_context.amazon.in
    process_description: Order captured in OMS, deductions applied, settlement period closes, net settlement rows appear.
    domain: domain.marketplace.amazon.reconciliation
    evidence_refs:
    - ev.amazon.financial_stack.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order captured in OMS, deductions applied, settlement period closes, net settlement rows appear.
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.amazon.return_to_settlement
  name: Amazon return to settlement lifecycle
  fields:
    process_key: return_to_settlement
    platform_context: platform_context.amazon.in
    process_description: Return/reverse event reduces revenue and can debit next settlement period with partial fee recovery.
    domain: domain.marketplace.amazon.reconciliation
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Return/reverse event reduces revenue and can debit next settlement period with partial fee recovery.
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.amazon.expected_vs_actual_fee_validation
  name: Amazon expected vs actual fee validation lifecycle
  fields:
    process_key: expected_vs_actual_fee_validation
    platform_context: platform_context.amazon.in
    process_description: Expected SKU fee preview is compared with aggregated actual ItemFees from disbursement.
    domain: domain.marketplace.amazon.reconciliation
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected SKU fee preview is compared with aggregated actual ItemFees from disbursement.
```
```yaml
candidate_card:
  card_type: business_process
  card_id: business_process.amazon.safe_t_reimbursement
  name: Amazon SAFE-T reimbursement lifecycle
  fields:
    process_key: safe_t_reimbursement
    platform_context: platform_context.amazon.in
    process_description: Eligible Amazon-caused or buyer-fraud returns can be reimbursed through SAFE-T credits.
    domain: domain.marketplace.amazon.returns
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Eligible Amazon-caused or buyer-fraud returns can be reimbursed through SAFE-T credits.
```
### 5.13 Workflow Step Cards

```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.order_to_settlement.order_recorded
  name: 'Amazon order to settlement lifecycle: order recorded'
  fields:
    process: business_process.amazon.order_to_settlement
    step_key: order_recorded
    step_order: '1'
    step_description: order recorded
    evidence_refs:
    - ev.amazon.financial_stack.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 1 in Amazon order to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.order_to_settlement.marketplace_deductions_applied
  name: 'Amazon order to settlement lifecycle: marketplace deductions applied'
  fields:
    process: business_process.amazon.order_to_settlement
    step_key: marketplace_deductions_applied
    step_order: '2'
    step_description: marketplace deductions applied
    evidence_refs:
    - ev.amazon.financial_stack.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 2 in Amazon order to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.order_to_settlement.settlement_period_netted
  name: 'Amazon order to settlement lifecycle: settlement period netted'
  fields:
    process: business_process.amazon.order_to_settlement
    step_key: settlement_period_netted
    step_order: '3'
    step_description: settlement period netted
    evidence_refs:
    - ev.amazon.financial_stack.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 3 in Amazon order to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.order_to_settlement.net_settlement_posted
  name: 'Amazon order to settlement lifecycle: net settlement posted'
  fields:
    process: business_process.amazon.order_to_settlement
    step_key: net_settlement_posted
    step_order: '4'
    step_description: net settlement posted
    evidence_refs:
    - ev.amazon.financial_stack.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon.recon.oms_settlement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 4 in Amazon order to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.return_to_settlement.return_recorded
  name: 'Amazon return to settlement lifecycle: return recorded'
  fields:
    process: business_process.amazon.return_to_settlement
    step_key: return_recorded
    step_order: '1'
    step_description: return recorded
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 1 in Amazon return to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.return_to_settlement.refund_debited
  name: 'Amazon return to settlement lifecycle: refund debited'
  fields:
    process: business_process.amazon.return_to_settlement
    step_key: refund_debited
    step_order: '2'
    step_description: refund debited
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 2 in Amazon return to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.return_to_settlement.fee_recovery_assessed
  name: 'Amazon return to settlement lifecycle: fee recovery assessed'
  fields:
    process: business_process.amazon.return_to_settlement
    step_key: fee_recovery_assessed
    step_order: '3'
    step_description: fee recovery assessed
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 3 in Amazon return to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.return_to_settlement.non_recovered_fees_recorded
  name: 'Amazon return to settlement lifecycle: non recovered fees recorded'
  fields:
    process: business_process.amazon.return_to_settlement
    step_key: non_recovered_fees_recorded
    step_order: '4'
    step_description: non recovered fees recorded
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon.settlement_cycle.001
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 4 in Amazon return to settlement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.expected_vs_actual_fee_validation.expected_fee_loaded
  name: 'Amazon expected vs actual fee validation lifecycle: expected fee loaded'
  fields:
    process: business_process.amazon.expected_vs_actual_fee_validation
    step_key: expected_fee_loaded
    step_order: '1'
    step_description: expected fee loaded
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 1 in Amazon expected vs actual fee validation lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.expected_vs_actual_fee_validation.actual_fee_aggregated
  name: 'Amazon expected vs actual fee validation lifecycle: actual fee aggregated'
  fields:
    process: business_process.amazon.expected_vs_actual_fee_validation
    step_key: actual_fee_aggregated
    step_order: '2'
    step_description: actual fee aggregated
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 2 in Amazon expected vs actual fee validation lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.expected_vs_actual_fee_validation.variance_computed
  name: 'Amazon expected vs actual fee validation lifecycle: variance computed'
  fields:
    process: business_process.amazon.expected_vs_actual_fee_validation
    step_key: variance_computed
    step_order: '3'
    step_description: variance computed
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 3 in Amazon expected vs actual fee validation lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.expected_vs_actual_fee_validation.root_cause_reviewed
  name: 'Amazon expected vs actual fee validation lifecycle: root cause reviewed'
  fields:
    process: business_process.amazon.expected_vs_actual_fee_validation
    step_key: root_cause_reviewed
    step_order: '4'
    step_description: root cause reviewed
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 4 in Amazon expected vs actual fee validation lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.safe_t_reimbursement.eligible_return_identified
  name: 'Amazon SAFE-T reimbursement lifecycle: eligible return identified'
  fields:
    process: business_process.amazon.safe_t_reimbursement
    step_key: eligible_return_identified
    step_order: '1'
    step_description: eligible return identified
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 1 in Amazon SAFE-T reimbursement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.safe_t_reimbursement.claim_or_reimbursement_detected
  name: 'Amazon SAFE-T reimbursement lifecycle: claim or reimbursement detected'
  fields:
    process: business_process.amazon.safe_t_reimbursement
    step_key: claim_or_reimbursement_detected
    step_order: '2'
    step_description: claim or reimbursement detected
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 2 in Amazon SAFE-T reimbursement lifecycle.
```
```yaml
candidate_card:
  card_type: workflow_step
  card_id: workflow_step.amazon.safe_t_reimbursement.recovery_amount_recorded
  name: 'Amazon SAFE-T reimbursement lifecycle: recovery amount recorded'
  fields:
    process: business_process.amazon.safe_t_reimbursement
    step_key: recovery_amount_recorded
    step_order: '3'
    step_description: recovery amount recorded
    evidence_refs:
    - ev.amazon.safet.001
    - ev.amazon.return_analysis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Step 3 in Amazon SAFE-T reimbursement lifecycle.
```
### 5.14 State Transition Cards

```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.amazon.oms_forward_to_reverse
  name: 'Amazon state transition: forward to reverse'
  fields:
    state_column: column.zs_observe.amazon_oms.transaction_type
    from_state: forward
    to_state: reverse
    transition_meaning: A shipped sale can later become a customer return represented by reverse transaction type.
    evidence_refs:
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: A shipped sale can later become a customer return represented by reverse transaction type.
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.amazon.settlement_order_to_refund
  name: 'Amazon state transition: Order to Refund'
  fields:
    state_column: column.zs_observe.amazon_settlement.type
    from_state: Order
    to_state: Refund
    transition_meaning: Settlement sale can later be offset by refund rows.
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement sale can later be offset by refund rows.
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.amazon.disbursment_order_fee_to_refund_fee
  name: 'Amazon state transition: Order to Refund'
  fields:
    state_column: column.zs_observe.amazon_disbursment.transaction_type
    from_state: Order
    to_state: Refund
    transition_meaning: Order fee charge may later be partially reversed or refunded.
    evidence_refs:
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order fee charge may later be partially reversed or refunded.
```
```yaml
candidate_card:
  card_type: state_transition
  card_id: state_transition.amazon.fee_charge_to_fulfillment_fee_refund
  name: 'Amazon state transition: Order to Fulfillment Fee Refund'
  fields:
    state_column: column.zs_observe.amazon_disbursment.transaction_type
    from_state: Order
    to_state: Fulfillment Fee Refund
    transition_meaning: Shipping/tech/pickup fee corrections can appear as Fulfillment Fee Refund.
    evidence_refs:
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Shipping/tech/pickup fee corrections can appear as Fulfillment Fee Refund.
```
### 5.15 Process Variant Cards

```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.amazon.fba_fulfilment_variant
  name: FBA fulfilment variant
  fields:
    variant_key: fba_fulfilment_variant
    variant_description: FBA/AFN has higher fees including pick-and-pack and FBA fees.
    variant_creation_reason: material marketplace behavior difference documented in DOCX
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: FBA/AFN has higher fees including pick-and-pack and FBA fees.
```
```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.amazon.mfn_easyship_variant
  name: MFN/Easyship fulfilment variant
  fields:
    variant_key: mfn_easyship_variant
    variant_description: MFN/Easyship has lower Amazon fees but seller logistics risk.
    variant_creation_reason: material marketplace behavior difference documented in DOCX
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: MFN/Easyship has lower Amazon fees but seller logistics risk.
```
```yaml
candidate_card:
  card_type: process_variant
  card_id: process_variant.amazon.india_vs_international_returns_variant
  name: India vs international return handling variant
  fields:
    variant_key: india_vs_international_returns_variant
    variant_description: India returns are represented in OMS reverse rows; international returns have amazon_returns reason-code table but currently inactive.
    variant_creation_reason: material marketplace behavior difference documented in DOCX
    evidence_refs:
    - ev.amazon_returns.purpose.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: India returns are represented in OMS reverse rows; international returns have amazon_returns reason-code table but currently inactive.
```
### 5.16 Marketplace-Internal Reconciliation Profile Cards

```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.amazon.oms_to_settlement
  name: Amazon OMS to Settlement Reconciliation
  fields:
    profile_key: oms_to_settlement
    reconciliation_scope: marketplace_internal_only
    description: Aligns OMS forward revenue with settlement Order product_sales and identifies timing gaps.
    expected_side: reconciliation_side.amazon.oms_to_settlement.expected
    actual_side: reconciliation_side.amazon.oms_to_settlement.actual
    unit: reconciliation_unit.amazon.oms_to_settlement.order
    matching_logic: matching_logic.amazon.oms_to_settlement.primary
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Aligns OMS forward revenue with settlement Order product_sales and identifies timing gaps.
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.amazon.settlement_to_disbursement
  name: Amazon Settlement to Disbursement Reconciliation
  fields:
    profile_key: settlement_to_disbursement
    reconciliation_scope: marketplace_internal_only
    description: Reconciles settlement order-level total with line-level disbursement charged_amount sums.
    expected_side: reconciliation_side.amazon.settlement_to_disbursement.expected
    actual_side: reconciliation_side.amazon.settlement_to_disbursement.actual
    unit: reconciliation_unit.amazon.settlement_to_disbursement.order_settlement
    matching_logic: matching_logic.amazon.settlement_to_disbursement.primary
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Reconciles settlement order-level total with line-level disbursement charged_amount sums.
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  name: Amazon Fee Preview to Actual Fee Reconciliation
  fields:
    profile_key: fee_preview_to_actual_fee
    reconciliation_scope: marketplace_internal_only
    description: Compares expected SKU-level fees to actual disbursement ItemFees aggregated to SKU.
    expected_side: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
    actual_side: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
    unit: reconciliation_unit.amazon.fee_preview_to_actual_fee.sku
    matching_logic: matching_logic.amazon.fee_preview_to_actual_fee.primary
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compares expected SKU-level fees to actual disbursement ItemFees aggregated to SKU.
```
```yaml
candidate_card:
  card_type: reconciliation_profile
  card_id: reconciliation_profile.amazon.returns_to_settlement
  name: Amazon Returns to Settlement Reconciliation
  fields:
    profile_key: returns_to_settlement
    reconciliation_scope: marketplace_internal_only
    description: Relates return/reverse evidence to settlement refund and fee-recovery behavior.
    expected_side: reconciliation_side.amazon.returns_to_settlement.expected
    actual_side: reconciliation_side.amazon.returns_to_settlement.actual
    unit: reconciliation_unit.amazon.returns_to_settlement.return_order
    matching_logic: matching_logic.amazon.returns_to_settlement.primary
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Relates return/reverse evidence to settlement refund and fee-recovery behavior.
```
### 5.17 Reconciliation Side Cards

```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.oms_to_settlement.expected
  name: OMS forward revenue side
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    side_role: expected
    source_table: table.zs_observe.amazon_oms
    business_role: source of truth for gross sales
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: source of truth for gross sales
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.oms_to_settlement.actual
  name: Settlement product sales side
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    side_role: actual
    source_table: table.zs_observe.amazon_settlement
    business_role: Amazon settlement view of those sales
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon settlement view of those sales
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  name: Settlement ledger side
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    side_role: expected
    source_table: table.zs_observe.amazon_settlement
    business_role: order-level total for settlement row
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: order-level total for settlement row
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  name: Disbursement line-detail side
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    side_role: actual
    source_table: table.zs_observe.amazon_disbursment
    business_role: line-level amount components that sum to settlement total
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: line-level amount components that sum to settlement total
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  name: Expected fee preview side
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    side_role: expected
    source_table: table.zs_observe.amazon_fee_preview
    business_role: expected SKU-level fee estimate
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: expected SKU-level fee estimate
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  name: Actual fee disbursement side
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    side_role: actual
    source_table: table.zs_observe.amazon_disbursment
    business_role: actual ItemFees charged by Amazon
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: actual ItemFees charged by Amazon
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.returns_to_settlement.expected
  name: Return/reverse side
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    side_role: expected
    source_table: table.zs_observe.amazon_oms
    business_role: India reverse transaction rows; international return table when active
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: India reverse transaction rows; international return table when active
```
```yaml
candidate_card:
  card_type: reconciliation_side
  card_id: reconciliation_side.amazon.returns_to_settlement.actual
  name: Settlement refund side
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    side_role: actual
    source_table: table.zs_observe.amazon_settlement
    business_role: Refund, Fulfilment Fee Refund, SAFE-T, reimbursement rows
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Refund, Fulfilment Fee Refund, SAFE-T, reimbursement rows
```
### 5.18 Reconciliation Unit Cards

```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amazon.oms_to_settlement.order
  name: 'Amazon OMS to Settlement Reconciliation unit: order'
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    unit_key: order
    grain: order-level or order-period grain
    join_keys: order_id
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: order-level or order-period grain
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amazon.settlement_to_disbursement.order_settlement
  name: 'Amazon Settlement to Disbursement Reconciliation unit: order_settlement'
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    unit_key: order_settlement
    grain: order plus settlement period grain
    join_keys:
    - order_id
    - settlement_id
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: order plus settlement period grain
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amazon.fee_preview_to_actual_fee.sku
  name: 'Amazon Fee Preview to Actual Fee Reconciliation unit: sku'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    unit_key: sku
    grain: SKU-level grain after actual-fee aggregation
    join_keys: amazon_fee_preview.sku = amazon_disbursment.sku_id
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SKU-level grain after actual-fee aggregation
```
```yaml
candidate_card:
  card_type: reconciliation_unit
  card_id: reconciliation_unit.amazon.returns_to_settlement.return_order
  name: 'Amazon Returns to Settlement Reconciliation unit: return_order'
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    unit_key: return_order
    grain: return order grain
    join_keys: order_id
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: return order grain
```
### 5.19 Matching Logic Cards

```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.amazon.oms_to_settlement.primary
  name: Amazon OMS to Settlement Reconciliation matching logic
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    join_keys: order_id
    matching_rule: Compare count distinct order_id and sum OMS charged_amount against settlement product_sales for type = Order; identify OMS orders not yet in settlement as timing gaps.
    aggregation_rule: aggregate to reconciliation unit before comparison
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compare count distinct order_id and sum OMS charged_amount against settlement product_sales for type = Order; identify OMS orders not yet in settlement as timing
      gaps.
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.amazon.settlement_to_disbursement.primary
  name: Amazon Settlement to Disbursement Reconciliation matching logic
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    join_keys:
    - order_id
    - settlement_id
    matching_rule: For each order/settlement_id, settlement total should equal SUM(disbursement.charged_amount) after line-level aggregation.
    aggregation_rule: aggregate to reconciliation unit before comparison
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: For each order/settlement_id, settlement total should equal SUM(disbursement.charged_amount) after line-level aggregation.
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.amazon.fee_preview_to_actual_fee.primary
  name: Amazon Fee Preview to Actual Fee Reconciliation matching logic
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    join_keys: amazon_fee_preview.sku = amazon_disbursment.sku_id
    matching_rule: Aggregate disbursement ItemFees to SKU, then compute variance as expected gross_commission + actual_fee because actual fees are negative.
    aggregation_rule: aggregate to reconciliation unit before comparison
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Aggregate disbursement ItemFees to SKU, then compute variance as expected gross_commission + actual_fee because actual fees are negative.
```
```yaml
candidate_card:
  card_type: matching_logic
  card_id: matching_logic.amazon.returns_to_settlement.primary
  name: Amazon Returns to Settlement Reconciliation matching logic
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    join_keys: order_id
    matching_rule: Match return/reverse order_id to settlement Refund rows and evaluate recovered versus non-recovered fees.
    aggregation_rule: aggregate to reconciliation unit before comparison
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Match return/reverse order_id to settlement Refund rows and evaluate recovered versus non-recovered fees.
```
### 5.20 Mismatch Category Cards

```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.oms_to_settlement.yet_to_be_settled
  name: 'Amazon OMS to Settlement Reconciliation: yet to be settled'
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    category_key: yet_to_be_settled
    description: OMS revenue in period not yet appearing in settlement; legitimate timing gap.
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: OMS revenue in period not yet appearing in settlement; legitimate timing gap.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.oms_to_settlement.order_count_mismatch
  name: 'Amazon OMS to Settlement Reconciliation: order count mismatch'
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    category_key: order_count_mismatch
    description: Distinct OMS forward orders do not align with settlement Order rows.
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Distinct OMS forward orders do not align with settlement Order rows.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.oms_to_settlement.revenue_mismatch
  name: 'Amazon OMS to Settlement Reconciliation: revenue mismatch'
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    category_key: revenue_mismatch
    description: Sum charged_amount differs from settlement product_sales beyond review tolerance.
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Sum charged_amount differs from settlement product_sales beyond review tolerance.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.settlement_to_disbursement.missing_disbursement_rows
  name: 'Amazon Settlement to Disbursement Reconciliation: missing disbursement rows'
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    category_key: missing_disbursement_rows
    description: Settlement exists but line-level disbursement rows are missing.
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Settlement exists but line-level disbursement rows are missing.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.settlement_to_disbursement.different_settlement_id_mapping
  name: 'Amazon Settlement to Disbursement Reconciliation: different settlement id mapping'
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    category_key: different_settlement_id_mapping
    description: Rows map to a different settlement_id or period.
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Rows map to a different settlement_id or period.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.settlement_to_disbursement.timing_difference
  name: 'Amazon Settlement to Disbursement Reconciliation: timing difference'
  fields:
    profile: reconciliation_profile.amazon.settlement_to_disbursement
    category_key: timing_difference
    description: Order, adjustment, or refund appears in different settlement period.
    evidence_refs:
    - ev.amazon.recon.settlement_disbursement.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Order, adjustment, or refund appears in different settlement period.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.fee_preview_to_actual_fee.price_difference
  name: 'Amazon Fee Preview to Actual Fee Reconciliation: price difference'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    category_key: price_difference
    description: Selling price differs from MRP or fee-preview basis.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Selling price differs from MRP or fee-preview basis.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.fee_preview_to_actual_fee.weight_dimension_mismatch
  name: 'Amazon Fee Preview to Actual Fee Reconciliation: weight dimension mismatch'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    category_key: weight_dimension_mismatch
    description: Gross/volumetric/dimension mismatch affects shipping fee.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Gross/volumetric/dimension mismatch affects shipping fee.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.fee_preview_to_actual_fee.category_reclassification
  name: 'Amazon Fee Preview to Actual Fee Reconciliation: category reclassification'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    category_key: category_reclassification
    description: Amazon category changed and referral fee tier differs.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Amazon category changed and referral fee tier differs.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.fee_preview_to_actual_fee.fee_tier_change
  name: 'Amazon Fee Preview to Actual Fee Reconciliation: fee tier change'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    category_key: fee_tier_change
    description: Fee tier changed mid-period.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Fee tier changed mid-period.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.fee_preview_to_actual_fee.overcharge_variance
  name: 'Amazon Fee Preview to Actual Fee Reconciliation: overcharge variance'
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    category_key: overcharge_variance
    description: Positive variance indicates possible overcharge requiring review.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Positive variance indicates possible overcharge requiring review.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.returns_to_settlement.missing_refund_settlement
  name: 'Amazon Returns to Settlement Reconciliation: missing refund settlement'
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    category_key: missing_refund_settlement
    description: Return/reverse exists but no matching settlement Refund row.
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Return/reverse exists but no matching settlement Refund row.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.returns_to_settlement.fee_recovery_gap
  name: 'Amazon Returns to Settlement Reconciliation: fee recovery gap'
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    category_key: fee_recovery_gap
    description: Expected fee recovery or reimbursement not visible in settlement/disbursement rows.
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Expected fee recovery or reimbursement not visible in settlement/disbursement rows.
```
```yaml
candidate_card:
  card_type: mismatch_category
  card_id: mismatch_category.amazon.returns_to_settlement.inactive_return_source
  name: 'Amazon Returns to Settlement Reconciliation: inactive return source'
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    category_key: inactive_return_source
    description: amazon_returns has no active rows until re-ingested; use OMS reverse for India.
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: amazon_returns has no active rows until re-ingested; use OMS reverse for India.
```
### 5.21 Reconciliation Variant Cards

```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.amazon.oms_to_settlement.india_vs_international
  name: India vs international OMS-settlement variant
  fields:
    profile: reconciliation_profile.amazon.oms_to_settlement
    variant_key: india_vs_international
    variant_reason: Group/context differences affect marketplace labels and realization benchmarks; not account-binding.
    evidence_refs:
    - ev.amazon.recon.oms_settlement.001
    - ev.amazon.join_patterns.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: Group/context differences affect marketplace labels and realization benchmarks; not account-binding.
```
```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.amazon.fee_preview_to_actual_fee.component_level
  name: Component-level fee variance variant
  fields:
    profile: reconciliation_profile.amazon.fee_preview_to_actual_fee
    variant_key: component_level
    variant_reason: Use when component fields exist and the variance needs referral, fixed, shipping, or pick-and-pack breakdown.
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    - ev.amazon_fee_preview.recon.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: Use when component fields exist and the variance needs referral, fixed, shipping, or pick-and-pack breakdown.
```
```yaml
candidate_card:
  card_type: reconciliation_variant
  card_id: reconciliation_variant.amazon.returns_to_settlement.india_oms_reverse_vs_international_returns
  name: India OMS reverse vs international returns table variant
  fields:
    profile: reconciliation_profile.amazon.returns_to_settlement
    variant_key: india_oms_reverse_vs_international_returns
    variant_reason: India return tracking uses OMS reverse, while international return reasons use amazon_returns when active.
    evidence_refs:
    - ev.amazon.return_analysis.001
    - ev.amazon_returns.purpose.001
    - ev.amazon_settlement.columns.001
    confidence: medium
    review_status: review_required
    create_action: create
    marketplace_only: true
    candidate_notes: India return tracking uses OMS reverse, while international return reasons use amazon_returns when active.
```
### 5.22 Query Pattern Cards

```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.realization_rate_month
  name: What is our realization rate this month?
  fields:
    natural_language_patterns: What is our realization rate this month?
    primary_metric: metric.marketplace.seller_realization_rate
    source_tables: table.zs_observe.amazon_settlement
    query_logic: SUM(total) / SUM(product_sales on Order rows), grouped by period
    sql_ref: sql.amazon.settlement.realization_rate
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SUM(total) / SUM(product_sales on Order rows), grouped by period
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.worst_return_rate_skus
  name: Which SKUs have the worst return rates?
  fields:
    natural_language_patterns: Which SKUs have the worst return rates?
    primary_metric: metric.marketplace.return_rate
    source_tables: table.zs_observe.amazon_oms
    query_logic: COUNT(reverse) / COUNT(forward) grouped by sku_id
    sql_ref: sql.amazon.oms.return_rate_by_sku
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: COUNT(reverse) / COUNT(forward) grouped by sku_id
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.fee_overcharge
  name: Are we being overcharged on fees?
  fields:
    natural_language_patterns: Are we being overcharged on fees?
    primary_metric: metric.marketplace.actual_fee_variance
    source_tables:
    - table.zs_observe.amazon_fee_preview
    - table.zs_observe.amazon_disbursment
    query_logic: Join expected gross_commission to aggregated actual ItemFees by SKU
    sql_ref: sql.amazon.fee_preview.expected_vs_actual
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Join expected gross_commission to aggregated actual ItemFees by SKU
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.return_margin_impact
  name: What is the true margin impact of our return rate?
  fields:
    natural_language_patterns: What is the true margin impact of our return rate?
    primary_metric: metric.marketplace.return_loss
    source_tables:
    - table.zs_observe.amazon_disbursment
    - table.zs_observe.amazon_oms
    query_logic: Compute net revenue less return-driven non-recoverable fees
    sql_ref: sql.amazon.disbursement.return_loss
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compute net revenue less return-driven non-recoverable fees
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.advertising_spend
  name: How much did we spend on advertising?
  fields:
    natural_language_patterns: How much did we spend on advertising?
    primary_metric: metric.marketplace.advertising_spend
    source_tables: table.zs_observe.amazon_settlement
    query_logic: type = Service Fee and description LIKE Advertising
    sql_ref: sql.amazon.settlement.advertising_spend
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: type = Service Fee and description LIKE Advertising
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.settlement_cash_position
  name: What is our cash position after this settlement?
  fields:
    natural_language_patterns: What is our cash position after this settlement?
    primary_metric: metric.marketplace.settlement_cash_position
    source_tables: table.zs_observe.amazon_settlement
    query_logic: SUM(total) across all types in selected settlement_id
    sql_ref: sql.amazon.settlement.cash_position
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SUM(total) across all types in selected settlement_id
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.revenue_by_state
  name: Which states generate the most revenue?
  fields:
    natural_language_patterns: Which states generate the most revenue?
    primary_metric: metric.marketplace.gross_revenue
    source_tables: table.zs_observe.amazon_oms
    query_logic: Group forward charged_amount by destination_state
    sql_ref: sql.amazon.oms.revenue_by_state
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Group forward charged_amount by destination_state
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.tds_tcs_month
  name: How much TDS/TCS are deducted per month?
  fields:
    natural_language_patterns: How much TDS/TCS are deducted per month?
    primary_metric: metric.marketplace.tds_tcs_deductions
    source_tables:
    - table.zs_observe.amazon_settlement
    - table.zs_observe.amazon_oms
    query_logic: Sum tds and TCS fields by month
    sql_ref: sql.amazon.settlement.tds_tcs_deductions
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Sum tds and TCS fields by month
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.fee_chargebacks
  name: Which orders had fee chargebacks and why?
  fields:
    natural_language_patterns: Which orders had fee chargebacks and why?
    primary_metric: metric.marketplace.marketplace_shipping_cost_rate
    source_tables: table.zs_observe.amazon_disbursment
    query_logic: Filter charged_amount_type = shipping chargeback
    sql_ref: sql.amazon.disbursement.shipping_chargebacks
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Filter charged_amount_type = shipping chargeback
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.gst_breakdown
  name: GST breakdown by geography
  fields:
    natural_language_patterns: GST breakdown by geography
    primary_metric: metric.marketplace.effective_tax_rate
    source_tables: table.zs_observe.amazon_oms
    query_logic: Classify IGST/CGST+SGST/UGST via tax rate columns
    sql_ref: sql.amazon.oms.gst_breakdown
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon_oms.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Classify IGST/CGST+SGST/UGST via tax rate columns
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.b2b_b2c_split
  name: B2B vs B2C revenue split
  fields:
    natural_language_patterns: B2B vs B2C revenue split
    primary_metric: metric.marketplace.gross_revenue
    source_tables: table.zs_observe.amazon_oms
    query_logic: Group by metadata or destination_gst_id signal
    sql_ref: sql.amazon.oms.b2b_b2c_split
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.segmentation.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Group by metadata or destination_gst_id signal
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.returns_reason_volume
  name: Return volume by reason
  fields:
    natural_language_patterns: Return volume by reason
    primary_metric: metric.marketplace.return_rate
    source_tables: table.zs_observe.amazon_returns
    query_logic: Group active amazon_returns by return_reason
    sql_ref: sql.amazon.returns.volume_by_reason
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon_returns.queries.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Group active amazon_returns by return_reason
```
```yaml
candidate_card:
  card_type: query_pattern
  card_id: query_pattern.amazon.volumetric_gap
  name: SKUs with volumetric weight gap
  fields:
    natural_language_patterns: SKUs with volumetric weight gap
    primary_metric: metric.marketplace.volumetric_excess_percent
    source_tables: table.zs_observe.amazon_fee_preview
    query_logic: Find volumetric_weight > gross_weight * 1.5
    sql_ref: sql.amazon.fee_preview.volumetric_gap
    scope_policy: runtime filters may be applied externally; do not hardcode group_level_id in canonical pattern
    evidence_refs:
    - ev.amazon.packaging_weight.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Find volumetric_weight > gross_weight * 1.5
```
### 5.23 Rule Cards

```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_oms_active_filter
  name: Always filter active OMS rows
  fields:
    related_canonical_id: table.zs_observe.amazon_oms
    rule_text: WHERE is_active = true; optional zen_status = true and is_duplicated = false
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_oms.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: WHERE is_active = true; optional zen_status = true and is_duplicated = false
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_forward_revenue_filter
  name: Revenue queries must isolate forward sales
  fields:
    related_canonical_id: table.zs_observe.amazon_oms
    rule_text: Use transaction_type = forward for gross revenue; do not mix cancel/replacement/reverse unless netting deliberately.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_oms.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use transaction_type = forward for gross revenue; do not mix cancel/replacement/reverse unless netting deliberately.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_net_revenue_netting
  name: Net revenue uses forward plus reverse
  fields:
    related_canonical_id: table.zs_observe.amazon_oms
    rule_text: Reverse rows are negative and can auto-net when included intentionally.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon.kpi.revenue.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Reverse rows are negative and can auto-net when included intentionally.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_tax_denominator
  name: Use excluding-tax denominator for effective tax rate
  fields:
    related_canonical_id: metric.marketplace.effective_tax_rate
    rule_text: SUM(total_tax) / SUM(charged_amount_excluding_tax), not total_tax / charged_amount.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: SUM(total_tax) / SUM(charged_amount_excluding_tax), not total_tax / charged_amount.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_disbursment_spelling
  name: Use exact table spelling amazon_disbursment
  fields:
    related_canonical_id: table.zs_observe.amazon_disbursment
    rule_text: The source table name omits the e before ment; SQL must match exactly.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_disbursment.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: The source table name omits the e before ment; SQL must match exactly.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_disbursment_fee_context
  name: Always specify disbursement transaction_type for fee calculations
  fields:
    related_canonical_id: table.zs_observe.amazon_disbursment
    rule_text: Mixing Order and Refund transactions gives misleading net fee results.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_disbursment.transaction_types.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Mixing Order and Refund transactions gives misleading net fee results.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_refund_commission_positive
  name: Refund commission is a positive ItemFees line
  fields:
    related_canonical_id: column.zs_observe.amazon_disbursment.charged_amount_type
    rule_text: Do not treat all ItemFees as negative charges without transaction context.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not treat all ItemFees as negative charges without transaction context.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_fee_preview_filters
  name: Use boolean filters in fee preview
  fields:
    related_canonical_id: table.zs_observe.amazon_fee_preview
    rule_text: Use is_active = true and zen_status = true; zen_status/is_duplicated are booleans here.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_fee_preview.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use is_active = true and zen_status = true; zen_status/is_duplicated are booleans here.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_aggregate_before_fee_preview_join
  name: Aggregate actual fees before joining fee_preview
  fields:
    related_canonical_id: relationship.amazon.fee_preview_to_disbursment.sku
    rule_text: Disbursement has many rows per SKU; fee preview has one row per SKU.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Disbursement has many rows per SKU; fee preview has one row per SKU.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_settlement_null_type
  name: Do not drop settlement NULL type rows by default
  fields:
    related_canonical_id: column.zs_observe.amazon_settlement.type
    rule_text: 64K+ active rows can have type NULL and financial values.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon_settlement.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: 64K+ active rows can have type NULL and financial values.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_no_hardcoded_group_level
  name: No hardcoded group_level_id in canonical cards
  fields:
    related_canonical_id: column.zs_observe.amazon_settlement.group_level_id
    rule_text: Treat group_level_id as a filterable column/caveat only; scope resolution is external.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Treat group_level_id as a filterable column/caveat only; scope resolution is external.
```
```yaml
candidate_card:
  card_type: rule
  card_id: rule.amazon.amazon_tax_filing_out_of_scope
  name: Tax fields are marketplace deduction fields, not tax filing cards
  fields:
    related_canonical_id: domain.marketplace.amazon.tax_deductions
    rule_text: Do not create statutory GST/TDS/TCS compliance cards from this markdown.
    rule_type: business_semantic_rule
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not create statutory GST/TDS/TCS compliance cards from this markdown.
```
### 5.24 Validation Test Cards

```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.oms_active_record_rate
  name: OMS active record rate check
  fields:
    related_canonical_id: table.zs_observe.amazon_oms
    test_description: Compute percentage of rows with is_active = true; known active rate is very low due to duplication issue.
    sql_ref: sql.amazon.validation.oms_active_record_rate
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon.data_integrity.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compute percentage of rows with is_active = true; known active rate is very low due to duplication issue.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.oms_date_coverage
  name: OMS active date coverage check
  fields:
    related_canonical_id: table.zs_observe.amazon_oms
    test_description: Verify min/max created_date and month count for active forward orders.
    sql_ref: sql.amazon.validation.oms_date_coverage
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon.data_integrity.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Verify min/max created_date and month count for active forward orders.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.oms_settlement_order_count
  name: OMS-settlement order-count match
  fields:
    related_canonical_id: reconciliation_profile.amazon.oms_to_settlement
    test_description: Compare forward OMS order count and revenue to settlement Order count and product_sales for same period.
    sql_ref: sql.amazon.validation.oms_settlement_order_count
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon.data_integrity.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compare forward OMS order count and revenue to settlement Order count and product_sales for same period.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.fee_preview_coverage
  name: Fee preview coverage check
  fields:
    related_canonical_id: table.zs_observe.amazon_fee_preview
    test_description: Compute percentage of active OMS SKUs with fee preview rows.
    sql_ref: sql.amazon.validation.fee_preview_coverage
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon.data_integrity.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Compute percentage of active OMS SKUs with fee preview rows.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.effective_tax_denominator
  name: Effective tax denominator check
  fields:
    related_canonical_id: metric.marketplace.effective_tax_rate
    test_description: Validate tax rate using charged_amount_excluding_tax denominator.
    sql_ref: sql.amazon.validation.effective_tax_denominator
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon.gst.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Validate tax rate using charged_amount_excluding_tax denominator.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.settlement_total_formula
  name: Settlement total formula check
  fields:
    related_canonical_id: table.zs_observe.amazon_settlement
    test_description: Validate settlement total against product_sales, fees, rebates, tax deductions, and other fields.
    sql_ref: sql.amazon.validation.settlement_total_formula
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Validate settlement total against product_sales, fees, rebates, tax deductions, and other fields.
```
```yaml
candidate_card:
  card_type: validation_test
  card_id: validation_test.amazon.returns_source_active
  name: Returns source active-state check
  fields:
    related_canonical_id: table.zs_observe.amazon_returns
    test_description: Confirm amazon_returns is re-ingested before using return reason queries.
    sql_ref: sql.amazon.validation.returns_source_active
    test_type: marketplace_semantic_validation
    evidence_refs:
    - ev.amazon_returns.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Confirm amazon_returns is re-ingested before using return reason queries.
```
### 5.25 Output Contract Cards

```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.amazon.oms_settlement_recon
  name: OMS to settlement reconciliation output
  fields:
    related_canonical_id: reconciliation_profile.amazon.oms_to_settlement
    output_columns:
    - order_id
    - created_date
    - oms_revenue
    - settled_sales
    - net_settled
    - settlement_id
    - variance_status
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Output shape explicitly supported by DOCX query or reconciliation pattern.
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.amazon.fee_variance
  name: Fee variance output
  fields:
    related_canonical_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
    output_columns:
    - sku
    - expected_fee
    - actual_fee
    - order_count
    - variance
    - variance_reason_candidate
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.amazon.recon.fee_preview_actual.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Output shape explicitly supported by DOCX query or reconciliation pattern.
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.amazon.return_rate
  name: Return-rate analysis output
  fields:
    related_canonical_id: metric.marketplace.return_rate
    output_columns:
    - sku_id
    - description
    - forward_orders
    - returns
    - return_rate_pct
    - benchmark_band
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.amazon.analytical_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Output shape explicitly supported by DOCX query or reconciliation pattern.
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.amazon.settlement_waterfall
  name: Settlement waterfall output
  fields:
    related_canonical_id: metric.marketplace.seller_realization_rate
    output_columns:
    - settlement_id
    - gross_sales
    - commissions
    - fba_fees
    - other_fees
    - promo_rebates
    - tds
    - tcs
    - net_settled
    - realization_pct
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.amazon_settlement.kpis.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Output shape explicitly supported by DOCX query or reconciliation pattern.
```
```yaml
candidate_card:
  card_type: output_contract
  card_id: output_contract.amazon.returns_reason
  name: Returns reason output
  fields:
    related_canonical_id: table.zs_observe.amazon_returns
    output_columns:
    - return_reason
    - return_count
    - total_refund
    - controllability_category
    - action_hint
    contract_type: marketplace_analysis_output
    evidence_refs:
    - ev.amazon_returns.queries.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Output shape explicitly supported by DOCX query or reconciliation pattern.
```
### 5.26 Execution Constraint Set Cards

```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.active_records
  name: Active-record execution constraint
  fields:
    constraint_key: active_records
    constraint_text: Apply is_active = true for all core Amazon tables unless the analysis explicitly audits inactive records.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon_oms.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Apply is_active = true for all core Amazon tables unless the analysis explicitly audits inactive records.
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.aggregate_before_join
  name: Aggregate-before-join execution constraint
  fields:
    constraint_key: aggregate_before_join
    constraint_text: Aggregate amazon_disbursment to order/SKU grain before joining to OMS or fee_preview.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon.join_patterns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Aggregate amazon_disbursment to order/SKU grain before joining to OMS or fee_preview.
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.no_hardcoded_scope
  name: No hardcoded account-scope execution constraint
  fields:
    constraint_key: no_hardcoded_scope
    constraint_text: Do not hardcode group_level_id values in canonical cards; runtime or separate scope layer supplies them.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon.tenant_scope_mention.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not hardcode group_level_id values in canonical cards; runtime or separate scope layer supplies them.
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.revenue_vs_cashflow
  name: Revenue versus cash-flow constraint
  fields:
    constraint_key: revenue_vs_cashflow
    constraint_text: Use Order/Refund type filters for revenue reporting; use all settlement types for cash-flow reporting.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon_settlement.columns.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use Order/Refund type filters for revenue reporting; use all settlement types for cash-flow reporting.
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.fee_sign_semantics
  name: Fee sign-semantics constraint
  fields:
    constraint_key: fee_sign_semantics
    constraint_text: Use mp_fee_type, charged_amount_type, and transaction_type together to interpret fee signs.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon_disbursment.taxonomy.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Use mp_fee_type, charged_amount_type, and transaction_type together to interpret fee signs.
```
```yaml
candidate_card:
  card_type: execution_constraint_set
  card_id: execution_constraint_set.amazon.returns_availability
  name: Returns-table availability constraint
  fields:
    constraint_key: returns_availability
    constraint_text: Do not use amazon_returns for active analysis until source is re-ingested; India returns use amazon_oms reverse rows.
    constraint_scope: marketplace_semantic_execution
    evidence_refs:
    - ev.amazon_returns.quality.001
    confidence: high
    review_status: accepted
    create_action: create
    marketplace_only: true
    candidate_notes: Do not use amazon_returns for active analysis until source is re-ingested; India returns use amazon_oms reverse rows.
```
## 6. Candidate Edges — Unified Edge Taxonomy

> This section uses one umbrella taxonomy for old parser-helper names and new Cognee-style edge names. Each edge stores a canonical uppercase `edge_type`, any `legacy_edge_aliases`, `inverse_edge_type`, and `materialize_inverse`.
>
> Dual-side rule: core containment and membership edges are materialized in both directions. Usage/provenance edges remain single directed edges with reverse lookup through graph indexes unless `materialize_inverse: true` is set.
>
> Marketplace-only exclusions remain active: this file does not create tenant, group, platform account, account data binding, business scope, business flow, bank, logistics, payment-gateway, ERP/accounting, or statutory-filing edges.

### 6.0 Unified Edge Rules

```yaml
unified_edge_rules:
  canonical_edge_format: UPPERCASE_UNDERSCORE
  accepted_legacy_aliases: true
  canonicalize_legacy_aliases_before_ingestion: true
  store_directed_edge_as_source_of_truth: true
  include_inverse_edge_type_on_every_edge: true
  materialize_inverse_when_materialize_inverse_true: true
  materialize_inverse_defaults:
    always_materialize:
    - HAS_PLATFORM_CONTEXT <-> BELONGS_TO_PLATFORM
    - HAS_COLUMN <-> BELONGS_TO_TABLE
    - HAS_VALUE_PROFILE <-> PROFILES_COLUMN_OR_PROFILES_TABLE
    - HAS_IMPLEMENTATION <-> IMPLEMENTS_METRIC
    - HAS_BUSINESS_PROCESS <-> BELONGS_TO_DOMAIN_FOR_PROCESS
    - HAS_WORKFLOW_STEP <-> BELONGS_TO_PROCESS
    - HAS_STATE_TRANSITION <-> BELONGS_TO_PROCESS
    - HAS_PROCESS_VARIANT <-> EXTENDS_PROCESS
    - HAS_RECONCILIATION_PROFILE <-> SUPPORTS_PROCESS
    - HAS_RECONCILIATION_SIDE <-> BELONGS_TO_RECONCILIATION_PROFILE
    - USES_MATCHING_LOGIC <-> SUPPORTS_RECONCILIATION_PROFILE
    - RULE_HAS_VALIDATION_TEST <-> VALIDATION_TEST_ENFORCES_RULE
    index_reverse_lookup_only:
    - SOURCED_FROM_PLATFORM
    - SOURCED_FROM_PLATFORM_CONTEXT
    - APPLIES_TO_PLATFORM
    - APPLIES_TO_PLATFORM_CONTEXT
    - USES_TABLE
    - USES_COLUMN
    - USES_FORMULA_TEMPLATE
    - DEPENDS_ON_METRIC
    - PRODUCES_METRIC
    - USES_RECONCILIATION_PROFILE
    - REQUIRES_RULE
    - USES_OUTPUT_CONTRACT
    - INCLUDES_RULE
    - INCLUDES_VALIDATION_TEST
    - APPLIES_TO_QUERY_PATTERN
  parser_helper_policy:
    retain_parser_helper_edges: true
    parser_helper_edges_may_be_collapsed_into_fields: true
    parser_helper_edge_class: parser_helper
```

### 6.1 Unified Edge Taxonomy Registry

```yaml
unified_edge_taxonomy_registry:
- edge_type: HAS_PLATFORM_CONTEXT
  source_type: platform
  target_type: platform_context
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse_default: true
- edge_type: BELONGS_TO_PLATFORM
  source_type: platform_context
  target_type: platform
  inverse_edge_type: HAS_PLATFORM_CONTEXT
  materialize_inverse_default: true
- edge_type: SOURCED_FROM_PLATFORM
  source_type: table
  target_type: platform
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse_default: false
- edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_type: table
  target_type: platform_context
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse_default: false
- edge_type: APPLIES_TO_PLATFORM
  source_type: any_marketplace_card
  target_type: platform
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse_default: false
- edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_type: any_marketplace_card
  target_type: platform_context
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse_default: false
- edge_type: HAS_COLUMN
  source_type: table
  target_type: column
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse_default: true
- edge_type: BELONGS_TO_TABLE
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse_default: true
- edge_type: HAS_VALUE_PROFILE
  source_type: table_or_column
  target_type: value_profile
  inverse_edge_type: PROFILES_COLUMN_OR_PROFILES_TABLE
  materialize_inverse_default: true
- edge_type: PROFILES_COLUMN
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: true
- edge_type: PROFILES_TABLE
  source_type: value_profile
  target_type: table
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_RELATIONSHIP
  source_type: table
  target_type: relationship
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse_default: false
- edge_type: SOURCE_TABLE
  source_type: relationship
  target_type: table
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: TARGET_TABLE
  source_type: relationship
  target_type: table
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: USES_SOURCE_COLUMN
  source_type: relationship
  target_type: column
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: USES_TARGET_COLUMN
  source_type: relationship
  target_type: column
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse_default: false
- edge_type: HAS_IMPLEMENTATION
  source_type: metric
  target_type: metric_implementation
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse_default: true
- edge_type: IMPLEMENTS_METRIC
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse_default: true
- edge_type: USES_TABLE
  source_type: metric_implementation_or_query_pattern_or_process_or_reconciliation_side
  target_type: table
  inverse_edge_type: USED_BY_*
  materialize_inverse_default: false
- edge_type: USES_COLUMN
  source_type: metric_implementation_or_reconciliation_side_or_relationship_or_validation
  target_type: column
  inverse_edge_type: USED_BY_*
  materialize_inverse_default: false
- edge_type: USES_FORMULA_TEMPLATE
  source_type: metric_implementation
  target_type: formula_template
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse_default: false
- edge_type: DEPENDS_ON_METRIC
  source_type: metric
  target_type: metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse_default: false
- edge_type: PARENT_METRIC
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse_default: false
- edge_type: USES_DEPENDENT_METRIC
  source_type: metric_dependency
  target_type: metric
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse_default: false
- edge_type: BELONGS_TO_DOMAIN
  source_type: metric_or_process_or_table
  target_type: domain
  inverse_edge_type: HAS_METRIC_OR_HAS_BUSINESS_PROCESS
  materialize_inverse_default: false
- edge_type: HAS_BUSINESS_PROCESS
  source_type: domain
  target_type: business_process
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse_default: true
- edge_type: HAS_WORKFLOW_STEP
  source_type: business_process
  target_type: workflow_step
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse_default: true
- edge_type: BELONGS_TO_PROCESS
  source_type: workflow_step_or_state_transition
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP_OR_HAS_STATE_TRANSITION
  materialize_inverse_default: true
- edge_type: HAS_STATE_TRANSITION
  source_type: business_process
  target_type: state_transition
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse_default: true
- edge_type: TRIGGERED_BY_STEP
  source_type: state_transition
  target_type: workflow_step
  inverse_edge_type: TRIGGERS_TRANSITION
  materialize_inverse_default: false
- edge_type: HAS_PROCESS_VARIANT
  source_type: business_process
  target_type: process_variant
  inverse_edge_type: EXTENDS_PROCESS
  materialize_inverse_default: true
- edge_type: EXTENDS_PROCESS
  source_type: process_variant
  target_type: business_process
  inverse_edge_type: HAS_PROCESS_VARIANT
  materialize_inverse_default: true
- edge_type: HAS_RECONCILIATION_PROFILE
  source_type: domain_or_business_process
  target_type: reconciliation_profile
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse_default: true
- edge_type: SUPPORTS_PROCESS
  source_type: reconciliation_profile
  target_type: business_process
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse_default: true
- edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse_default: true
- edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_type: reconciliation_side
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse_default: true
- edge_type: HAS_PRIMARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
- edge_type: HAS_SECONDARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: SECONDARY_UNIT_OF_PROFILE
  materialize_inverse_default: false
- edge_type: USES_MATCHING_LOGIC
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse_default: true
- edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_type: matching_logic
  target_type: reconciliation_profile
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse_default: true
- edge_type: HAS_MISMATCH_CATEGORY
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse_default: false
- edge_type: EXTENDS_RECONCILIATION_PROFILE
  source_type: reconciliation_variant
  target_type: reconciliation_profile
  inverse_edge_type: HAS_RECONCILIATION_VARIANT
  materialize_inverse_default: false
- edge_type: OVERRIDES_MATCHING_LOGIC
  source_type: reconciliation_variant
  target_type: matching_logic
  inverse_edge_type: OVERRIDDEN_BY_VARIANT
  materialize_inverse_default: false
- edge_type: PRODUCES_METRIC
  source_type: query_pattern
  target_type: metric
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: USES_RECONCILIATION_PROFILE
  source_type: query_pattern
  target_type: reconciliation_profile
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: USES_RELATIONSHIP
  source_type: query_pattern
  target_type: relationship
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: TARGETS_CARD
  source_type: query_pattern_or_rule_or_validation_test
  target_type: any_canonical_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: REQUIRES_RULE
  source_type: query_pattern
  target_type: rule
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse_default: false
- edge_type: HAS_VALIDATION_TEST
  source_type: query_pattern_or_rule
  target_type: validation_test
  inverse_edge_type: VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE
  materialize_inverse_default: true
- edge_type: ENFORCES_RULE
  source_type: validation_test
  target_type: rule
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse_default: true
- edge_type: USES_OUTPUT_CONTRACT
  source_type: query_pattern_or_execution_constraint_set
  target_type: output_contract
  inverse_edge_type: USED_BY_*
  materialize_inverse_default: false
- edge_type: INCLUDES_RULE
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: INCLUDES_VALIDATION_TEST
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: APPLIES_TO_QUERY_PATTERN
  source_type: execution_constraint_set
  target_type: query_pattern
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse_default: false
- edge_type: USES_METRIC
  source_type: business_process
  target_type: metric
  inverse_edge_type: USED_IN_PROCESS
  materialize_inverse_default: true
- edge_type: USED_IN_PROCESS
  source_type: metric
  target_type: business_process
  inverse_edge_type: USES_METRIC
  materialize_inverse_default: true
```

### 6.2 Legacy Alias Normalization Registry

```yaml
legacy_alias_normalization_registry:
- legacy_edge_alias: column_belongs_to_table
  canonical_edge_type: BELONGS_TO_TABLE
  source_type: column
  target_type: table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: value_profile_describes_column
  canonical_edge_type: PROFILES_COLUMN
  source_type: value_profile
  target_type: column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: implementation_uses_table
  canonical_edge_type: USES_TABLE
  source_type: metric_implementation
  target_type: table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: implementation_uses_column
  canonical_edge_type: USES_COLUMN
  source_type: metric_implementation
  target_type: column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: implements_metric
  canonical_edge_type: IMPLEMENTS_METRIC
  source_type: metric_implementation
  target_type: metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: metric_depends_on_metric
  canonical_edge_type: DEPENDS_ON_METRIC
  source_type: metric
  target_type: metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: query_requires_table
  canonical_edge_type: USES_TABLE
  source_type: query_pattern
  target_type: table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: query_targets_card
  canonical_edge_type: TARGETS_CARD
  source_type: query_pattern
  target_type: any_canonical_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  canonical_cognee_edge: false
  parser_note: Fallback alias only; prefer PRODUCES_METRIC, USES_RECONCILIATION_PROFILE, USES_OUTPUT_CONTRACT, or REQUIRES_RULE when target type is known.
- legacy_edge_alias: process_uses_table
  canonical_edge_type: USES_TABLE
  source_type: business_process
  target_type: table
  inverse_edge_type: USED_BY_PROCESS
  materialize_inverse: false
  canonical_cognee_edge: false
  edge_class: parser_helper
- legacy_edge_alias: step_in_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_type: workflow_step
  target_type: business_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: transition_in_process
  canonical_edge_type: BELONGS_TO_PROCESS
  source_type: state_transition
  target_type: business_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: profile_expected_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  canonical_cognee_edge: true
  edge_properties:
    side_role: expected
- legacy_edge_alias: profile_actual_side
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_type: reconciliation_profile
  target_type: reconciliation_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  canonical_cognee_edge: true
  edge_properties:
    side_role: actual
- legacy_edge_alias: profile_uses_unit
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_type: reconciliation_profile
  target_type: reconciliation_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: profile_uses_matching_logic
  canonical_edge_type: USES_MATCHING_LOGIC
  source_type: reconciliation_profile
  target_type: matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  canonical_cognee_edge: true
- legacy_edge_alias: profile_has_mismatch_category
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_type: reconciliation_profile
  target_type: mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  canonical_cognee_edge: true
- legacy_edge_alias: side_uses_table
  canonical_edge_type: USES_TABLE
  source_type: reconciliation_side
  target_type: table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  canonical_cognee_edge: false
  edge_class: parser_helper
- legacy_edge_alias: side_uses_key_column
  canonical_edge_type: USES_COLUMN
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  canonical_cognee_edge: false
  edge_class: parser_helper
  edge_properties:
    column_role: key
- legacy_edge_alias: side_uses_amount_column
  canonical_edge_type: USES_COLUMN
  source_type: reconciliation_side
  target_type: column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  canonical_cognee_edge: false
  edge_class: parser_helper
  edge_properties:
    column_role: amount
- legacy_edge_alias: validation_enforces_constraint
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_type: execution_constraint_set
  target_type: validation_test
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  canonical_cognee_edge: true
  parser_note: Reverse old direction during canonicalization.
- legacy_edge_alias: rule_enforced_by_constraint
  canonical_edge_type: INCLUDES_RULE
  source_type: execution_constraint_set
  target_type: rule
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  canonical_cognee_edge: true
  parser_note: Reverse old direction during canonicalization.
```

### 6.3 Edge Coverage Summary

```yaml
edge_coverage_summary:
  candidate_edge_count: 933
  canonical_cognee_edge_count: 865
  parser_helper_edge_count: 68
  edges_with_legacy_aliases: 436
  materialized_inverse_edges: 4
  edge_type_counts:
  - edge_type: APPLIES_TO_PLATFORM
    candidate_edge_count: 11
  - edge_type: APPLIES_TO_PLATFORM_CONTEXT
    candidate_edge_count: 11
  - edge_type: APPLIES_TO_QUERY_PATTERN
    candidate_edge_count: 19
  - edge_type: BELONGS_TO_DOMAIN
    candidate_edge_count: 9
  - edge_type: BELONGS_TO_PLATFORM
    candidate_edge_count: 2
  - edge_type: BELONGS_TO_PROCESS
    candidate_edge_count: 19
  - edge_type: BELONGS_TO_RECONCILIATION_PROFILE
    candidate_edge_count: 8
  - edge_type: BELONGS_TO_TABLE
    candidate_edge_count: 140
  - edge_type: DEPENDS_ON_METRIC
    candidate_edge_count: 5
  - edge_type: ENFORCES_RULE
    candidate_edge_count: 8
  - edge_type: EXTENDS_PROCESS
    candidate_edge_count: 3
  - edge_type: EXTENDS_RECONCILIATION_PROFILE
    candidate_edge_count: 3
  - edge_type: HAS_BUSINESS_PROCESS
    candidate_edge_count: 4
  - edge_type: HAS_COLUMN
    candidate_edge_count: 140
  - edge_type: HAS_IMPLEMENTATION
    candidate_edge_count: 27
  - edge_type: HAS_MISMATCH_CATEGORY
    candidate_edge_count: 14
  - edge_type: HAS_PLATFORM_CONTEXT
    candidate_edge_count: 2
  - edge_type: HAS_PRIMARY_UNIT
    candidate_edge_count: 4
  - edge_type: HAS_PROCESS_VARIANT
    candidate_edge_count: 3
  - edge_type: HAS_RECONCILIATION_PROFILE
    candidate_edge_count: 4
  - edge_type: HAS_RECONCILIATION_SIDE
    candidate_edge_count: 8
  - edge_type: HAS_RELATIONSHIP
    candidate_edge_count: 14
  - edge_type: HAS_STATE_TRANSITION
    candidate_edge_count: 4
  - edge_type: HAS_VALIDATION_TEST
    candidate_edge_count: 28
  - edge_type: HAS_VALUE_PROFILE
    candidate_edge_count: 22
  - edge_type: HAS_WORKFLOW_STEP
    candidate_edge_count: 15
  - edge_type: IMPLEMENTS_METRIC
    candidate_edge_count: 27
  - edge_type: INCLUDES_RULE
    candidate_edge_count: 8
  - edge_type: INCLUDES_VALIDATION_TEST
    candidate_edge_count: 6
  - edge_type: PARENT_METRIC
    candidate_edge_count: 5
  - edge_type: PRODUCES_METRIC
    candidate_edge_count: 13
  - edge_type: PROFILES_COLUMN
    candidate_edge_count: 11
  - edge_type: PROFILES_TABLE
    candidate_edge_count: 11
  - edge_type: REQUIRES_RULE
    candidate_edge_count: 27
  - edge_type: SOURCED_FROM_PLATFORM
    candidate_edge_count: 5
  - edge_type: SOURCED_FROM_PLATFORM_CONTEXT
    candidate_edge_count: 5
  - edge_type: SOURCE_TABLE
    candidate_edge_count: 7
  - edge_type: SUPPORTS_PROCESS
    candidate_edge_count: 4
  - edge_type: SUPPORTS_RECONCILIATION_PROFILE
    candidate_edge_count: 4
  - edge_type: TARGETS_CARD
    candidate_edge_count: 37
  - edge_type: TARGET_TABLE
    candidate_edge_count: 7
  - edge_type: USES_COLUMN
    candidate_edge_count: 130
  - edge_type: USES_DEPENDENT_METRIC
    candidate_edge_count: 5
  - edge_type: USES_FORMULA_TEMPLATE
    candidate_edge_count: 14
  - edge_type: USES_MATCHING_LOGIC
    candidate_edge_count: 4
  - edge_type: USES_OUTPUT_CONTRACT
    candidate_edge_count: 6
  - edge_type: USES_RECONCILIATION_PROFILE
    candidate_edge_count: 4
  - edge_type: USES_RELATIONSHIP
    candidate_edge_count: 3
  - edge_type: USES_SOURCE_COLUMN
    candidate_edge_count: 6
  - edge_type: USES_TABLE
    candidate_edge_count: 51
  - edge_type: USES_TARGET_COLUMN
    candidate_edge_count: 6
```

### 6.4 Candidate Edge Registry

```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.expected_vs_actual_fee_validation.BELONGS_TO_DOMAIN.domain.marketplace.amazon.reconciliation
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: business_process.amazon.expected_vs_actual_fee_validation
  source_type: business_process
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.expected_vs_actual_fee_validation.HAS_WORKFLOW_STEP.workflow_step.amazon.expected_vs_actual_fee_validation.actual_fee_aggregated
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.expected_vs_actual_fee_validation
  source_type: business_process
  target_id: workflow_step.amazon.expected_vs_actual_fee_validation.actual_fee_aggregated
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.business_process.amazon.expected_vs_actual_fee_validation.has_step.actual_fee_aggregated
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.expected_vs_actual_fee_validation.HAS_WORKFLOW_STEP.workflow_step.amazon.expected_vs_actual_fee_validation.expected_fee_loaded
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.expected_vs_actual_fee_validation
  source_type: business_process
  target_id: workflow_step.amazon.expected_vs_actual_fee_validation.expected_fee_loaded
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.business_process.amazon.expected_vs_actual_fee_validation.has_step.expected_fee_loaded
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.expected_vs_actual_fee_validation.HAS_WORKFLOW_STEP.workflow_step.amazon.expected_vs_actual_fee_validation.root_cause_reviewed
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.expected_vs_actual_fee_validation
  source_type: business_process
  target_id: workflow_step.amazon.expected_vs_actual_fee_validation.root_cause_reviewed
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.business_process.amazon.expected_vs_actual_fee_validation.has_step.root_cause_reviewed
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.expected_vs_actual_fee_validation.HAS_WORKFLOW_STEP.workflow_step.amazon.expected_vs_actual_fee_validation.variance_computed
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.expected_vs_actual_fee_validation
  source_type: business_process
  target_id: workflow_step.amazon.expected_vs_actual_fee_validation.variance_computed
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.business_process.amazon.expected_vs_actual_fee_validation.has_step.variance_computed
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.BELONGS_TO_DOMAIN.domain.marketplace.amazon.reconciliation
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_PROCESS_VARIANT.process_variant.amazon.fba_fulfilment_variant
  edge_type: HAS_PROCESS_VARIANT
  canonical_edge_type: HAS_PROCESS_VARIANT
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: process_variant.amazon.fba_fulfilment_variant
  target_type: process_variant
  legacy_edge_aliases: []
  inverse_edge_type: EXTENDS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_PROCESS_VARIANT.process_variant.amazon.mfn_easyship_variant
  edge_type: HAS_PROCESS_VARIANT
  canonical_edge_type: HAS_PROCESS_VARIANT
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: process_variant.amazon.mfn_easyship_variant
  target_type: process_variant
  legacy_edge_aliases: []
  inverse_edge_type: EXTENDS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_STATE_TRANSITION.state_transition.amazon.disbursment_order_fee_to_refund_fee
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: state_transition.amazon.disbursment_order_fee_to_refund_fee
  target_type: state_transition
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_STATE_TRANSITION.state_transition.amazon.fee_charge_to_fulfillment_fee_refund
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: state_transition.amazon.fee_charge_to_fulfillment_fee_refund
  target_type: state_transition
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_STATE_TRANSITION.state_transition.amazon.oms_forward_to_reverse
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: state_transition.amazon.oms_forward_to_reverse
  target_type: state_transition
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_STATE_TRANSITION.state_transition.amazon.settlement_order_to_refund
  edge_type: HAS_STATE_TRANSITION
  canonical_edge_type: HAS_STATE_TRANSITION
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: state_transition.amazon.settlement_order_to_refund
  target_type: state_transition
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.order_to_settlement.marketplace_deductions_applied
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.order_to_settlement.marketplace_deductions_applied
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.business_process.amazon.order_to_settlement.has_step.marketplace_deductions_applied
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.order_to_settlement.net_settlement_posted
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.order_to_settlement.net_settlement_posted
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.business_process.amazon.order_to_settlement.has_step.net_settlement_posted
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.order_to_settlement.order_recorded
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.order_to_settlement.order_recorded
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.business_process.amazon.order_to_settlement.has_step.order_recorded
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.order_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.order_to_settlement.settlement_period_netted
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.order_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.order_to_settlement.settlement_period_netted
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.business_process.amazon.order_to_settlement.has_step.settlement_period_netted
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.BELONGS_TO_DOMAIN.domain.marketplace.amazon.reconciliation
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.HAS_PROCESS_VARIANT.process_variant.amazon.india_vs_international_returns_variant
  edge_type: HAS_PROCESS_VARIANT
  canonical_edge_type: HAS_PROCESS_VARIANT
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: process_variant.amazon.india_vs_international_returns_variant
  target_type: process_variant
  legacy_edge_aliases: []
  inverse_edge_type: EXTENDS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.return_to_settlement.fee_recovery_assessed
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.return_to_settlement.fee_recovery_assessed
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.business_process.amazon.return_to_settlement.has_step.fee_recovery_assessed
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.return_to_settlement.non_recovered_fees_recorded
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.return_to_settlement.non_recovered_fees_recorded
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.business_process.amazon.return_to_settlement.has_step.non_recovered_fees_recorded
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.return_to_settlement.refund_debited
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.return_to_settlement.refund_debited
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.business_process.amazon.return_to_settlement.has_step.refund_debited
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.return_to_settlement.HAS_WORKFLOW_STEP.workflow_step.amazon.return_to_settlement.return_recorded
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.return_to_settlement
  source_type: business_process
  target_id: workflow_step.amazon.return_to_settlement.return_recorded
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.business_process.amazon.return_to_settlement.has_step.return_recorded
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.safe_t_reimbursement.BELONGS_TO_DOMAIN.domain.marketplace.amazon.returns
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: business_process.amazon.safe_t_reimbursement
  source_type: business_process
  target_id: domain.marketplace.amazon.returns
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_BUSINESS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.safe_t_reimbursement.HAS_WORKFLOW_STEP.workflow_step.amazon.safe_t_reimbursement.claim_or_reimbursement_detected
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.safe_t_reimbursement
  source_type: business_process
  target_id: workflow_step.amazon.safe_t_reimbursement.claim_or_reimbursement_detected
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
  source_old_edge_id: edge.business_process.amazon.safe_t_reimbursement.has_step.claim_or_reimbursement_detected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.safe_t_reimbursement.HAS_WORKFLOW_STEP.workflow_step.amazon.safe_t_reimbursement.eligible_return_identified
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.safe_t_reimbursement
  source_type: business_process
  target_id: workflow_step.amazon.safe_t_reimbursement.eligible_return_identified
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
  source_old_edge_id: edge.business_process.amazon.safe_t_reimbursement.has_step.eligible_return_identified
```
```yaml
candidate_edge:
  edge_id: edge.amazon.business_process.amazon.safe_t_reimbursement.HAS_WORKFLOW_STEP.workflow_step.amazon.safe_t_reimbursement.recovery_amount_recorded
  edge_type: HAS_WORKFLOW_STEP
  canonical_edge_type: HAS_WORKFLOW_STEP
  source_id: business_process.amazon.safe_t_reimbursement
  source_type: business_process
  target_id: workflow_step.amazon.safe_t_reimbursement.recovery_amount_recorded
  target_type: workflow_step
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
  source_old_edge_id: edge.business_process.amazon.safe_t_reimbursement.has_step.recovery_amount_recorded
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.charged_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.charged_amount
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.charged_amount_type.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.charged_amount_type
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.charged_amount_type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_disbursment.charged_amount_type
  source_type: column
  target_id: value_profile.zs_observe.amazon_disbursment.charged_amount_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.currency_type.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.currency_type
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.group_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.group_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.group_level_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.group_level_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.is_active.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.is_active
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.item_fee_type.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.item_fee_type
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.item_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.item_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.mp_fee_type.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.mp_fee_type
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.mp_fee_type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_disbursment.mp_fee_type
  source_type: column
  target_id: value_profile.zs_observe.amazon_disbursment.mp_fee_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.order_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.order_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.order_level_total.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.order_level_total
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.posted_date.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.posted_date
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.promotion_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.promotion_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.settlement_date.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.settlement_date
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.settlement_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.settlement_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.sku.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.sku
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.sku_id.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.sku_id
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.transaction_type.BELONGS_TO_TABLE.table.zs_observe.amazon_disbursment
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_disbursment.transaction_type
  source_type: column
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_disbursment.transaction_type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.transaction_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_disbursment.transaction_type
  source_type: column
  target_id: value_profile.zs_observe.amazon_disbursment.transaction_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.amazon_store.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.amazon_store
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.amazon_store.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_fee_preview.amazon_store
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_fee_preview.amazon_store
  source_type: column
  target_id: value_profile.zs_observe.amazon_fee_preview.amazon_store
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.asin.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.asin
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.brand.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.brand
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.charged_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.charged_amount
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.description.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.description
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.estimated_fee_total.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.estimated_fee_total
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.final_weight.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.final_weight
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.fixed_fee.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.fixed_fee
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.fnsku.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.fnsku
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.fulfilled_by.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.fulfilled_by
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.gross_commission.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.gross_commission
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.gross_weight.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.gross_weight
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.hsn.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.hsn
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.is_active.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.is_active
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.is_duplicated.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.is_duplicated
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.longest_side.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.longest_side
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.median_side.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.median_side
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.pick_and_pack_fee.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.pick_and_pack_fee
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.product_group.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.product_group
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.product_name.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.product_name
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.referal_fee.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.referal_fee
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.referral_fee.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.referral_fee
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.shipping_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.shipping_amount
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.shortest_side.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.shortest_side
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.sku.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.sku
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.volumetric_weight.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.volumetric_weight
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_fee_preview.zen_status.BELONGS_TO_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_fee_preview.zen_status
  source_type: column
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.asin.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.asin
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.charged_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.charged_amount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.charged_amount_excluding_tax.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.charged_amount_excluding_tax
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.created_date.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.created_date
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.currency_type.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.currency_type
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.destination_gst_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.destination_gst_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.destination_state.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.destination_state
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.fulfilment_channel.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.fulfilment_channel
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.fulfilment_channel.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.fulfilment_channel
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_oms.fulfilment_channel
  source_type: column
  target_id: value_profile.zs_observe.amazon_oms.fulfilment_channel
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.fulfilment_type.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.fulfilment_type
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.fulfilment_type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_oms.fulfilment_type
  source_type: column
  target_id: value_profile.zs_observe.amazon_oms.fulfilment_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.gross_commission.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.gross_commission
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.group_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.group_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.group_level_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.group_level_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.invoice_date.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.invoice_date
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.invoice_number.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.invoice_number
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.is_active.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.is_active
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.is_duplicated.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.is_duplicated
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.item_amount_excluding_tax.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.item_amount_excluding_tax
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.item_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.item_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.item_promo_discount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.item_promo_discount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.metadata.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.metadata
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.metadata.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.metadata
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_oms.metadata
  source_type: column
  target_id: value_profile.zs_observe.amazon_oms.metadata
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.mrp.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.mrp
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.order_date.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.order_date
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.order_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.order_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.order_shipped_date.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.order_shipped_date
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.principal_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.principal_amount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.settled_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.settled_amount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.settlement_date.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.settlement_date
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.shipping_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.shipping_amount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.shipping_promo_discount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.shipping_promo_discount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.sku_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.sku_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.source_gst_id.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.source_gst_id
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.source_state.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.source_state
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.tax_cgst_rate.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.tax_cgst_rate
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.tax_igst_rate.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.tax_igst_rate
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.tax_ugst_rate.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.tax_ugst_rate
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.total_tax.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.total_tax
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.total_tcs_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.total_tcs_amount
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.total_tds.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.total_tds
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.transaction_type.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.transaction_type
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.transaction_type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.transaction_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_oms.transaction_type
  source_type: column
  target_id: value_profile.zs_observe.amazon_oms.transaction_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.zen_status.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.zen_status
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.zone.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.zone
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.zone.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.zone
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_oms.zone
  source_type: column
  target_id: value_profile.zs_observe.amazon_oms.zone
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_oms.zone_new.BELONGS_TO_TABLE.table.zs_observe.amazon_oms
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_oms.zone_new
  source_type: column
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.brand.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.brand
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.charged_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.charged_amount
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.charged_amount_excluding_tax.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.charged_amount_excluding_tax
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.created_date.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.created_date
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.currency_type.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.currency_type
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.customer_comments.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.customer_comments
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.fulfilment_channel.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.fulfilment_channel
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.group_level_id.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.group_level_id
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.internal_transaction_type.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.internal_transaction_type
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.is_active.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.is_active
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.is_duplicated.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.is_duplicated
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.order_id.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.order_id
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.quantity.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.quantity
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.return_date_str.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.return_date_str
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.return_reason.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.return_reason
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.return_reason.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_returns.return_reason
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_returns.return_reason
  source_type: column
  target_id: value_profile.zs_observe.amazon_returns.return_reason
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.shipping_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.shipping_amount
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.sku_id.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.sku_id
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.transaction_type.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.transaction_type
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_returns.zen_status.BELONGS_TO_TABLE.table.zs_observe.amazon_returns
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_returns.zen_status
  source_type: column
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.account_type.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.account_type
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.created_date.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.created_date
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.date_time.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.date_time
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.description.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.description
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.destination_state.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.destination_state
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.fba_fees.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.fba_fees
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.fulfillment.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.fulfillment
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.gift_wrap_credits.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.gift_wrap_credits
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.gross_commission.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.gross_commission
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.group_level_id.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.group_level_id
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.is_active.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.is_active
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.is_duplicated.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.is_duplicated
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.marketplace.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.marketplace
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.marketplace_withheld_tax.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.marketplace_withheld_tax
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.mp_fees.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.mp_fees
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.order_id.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.order_id
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.other.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.other
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.other_transaction_fees.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.other_transaction_fees
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.product_sales.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.product_sales
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.promotional_rebates.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.promotional_rebates
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.selling_fees.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.selling_fees
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.settled_amount.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.settled_amount
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.settlement_date.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.settlement_date
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.settlement_id.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.settlement_id
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.shipping_credits.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.shipping_credits
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.sku.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.sku
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.sku_id.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.sku_id
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.tcs_cgst.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.tcs_cgst
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.tcs_igst.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.tcs_igst
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.tcs_sgst.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.tcs_sgst
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.tds.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.tds
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.total.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.total
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.type.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.type
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.type.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_settlement.type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: column.zs_observe.amazon_settlement.type
  source_type: column
  target_id: value_profile.zs_observe.amazon_settlement.type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.column.zs_observe.amazon_settlement.zen_status.BELONGS_TO_TABLE.table.zs_observe.amazon_settlement
  edge_type: BELONGS_TO_TABLE
  canonical_edge_type: BELONGS_TO_TABLE
  source_id: column.zs_observe.amazon_settlement.zen_status
  source_type: column
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - column_belongs_to_table
  inverse_edge_type: HAS_COLUMN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.advertising_fees.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.advertising_fees
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.advertising_fees.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.advertising_fees
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.disbursement.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.disbursement
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.disbursement.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.disbursement
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fee_preview.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.fee_preview
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fee_preview.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.fee_preview
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fees.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.fees
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.fee_taxonomy.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fees.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.fees
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.fee_taxonomy.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fulfilment_shipping.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.fulfilment_shipping
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.fulfilment_shipping.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.fulfilment_shipping
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.orders.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.orders
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.orders.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.orders
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.recon.settlement_disbursement.001
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.recon.settlement_disbursement.001
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_BUSINESS_PROCESS.business_process.amazon.expected_vs_actual_fee_validation
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: business_process.amazon.expected_vs_actual_fee_validation
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_BUSINESS_PROCESS.business_process.amazon.order_to_settlement
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_BUSINESS_PROCESS.business_process.amazon.return_to_settlement
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement
  edge_type: HAS_RECONCILIATION_PROFILE
  canonical_edge_type: HAS_RECONCILIATION_PROFILE
  source_id: domain.marketplace.amazon.reconciliation
  source_type: domain
  target_id: reconciliation_profile.amazon.settlement_to_disbursement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: SUPPORTS_PROCESS
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reimbursements_claims.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.reimbursements_claims
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.reimbursements_claims.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.reimbursements_claims
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.returns.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.returns
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.returns.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.returns
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.returns.HAS_BUSINESS_PROCESS.business_process.amazon.safe_t_reimbursement
  edge_type: HAS_BUSINESS_PROCESS
  canonical_edge_type: HAS_BUSINESS_PROCESS
  source_id: domain.marketplace.amazon.returns
  source_type: domain
  target_id: business_process.amazon.safe_t_reimbursement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_DOMAIN
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.settlement.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.settlement
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.settlement.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.settlement
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.tax_deductions.APPLIES_TO_PLATFORM.platform.amazon
  edge_type: APPLIES_TO_PLATFORM
  canonical_edge_type: APPLIES_TO_PLATFORM
  source_id: domain.marketplace.amazon.tax_deductions
  source_type: domain
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon.fee_taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.domain.marketplace.amazon.tax_deductions.APPLIES_TO_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: APPLIES_TO_PLATFORM_CONTEXT
  canonical_edge_type: APPLIES_TO_PLATFORM_CONTEXT
  source_id: domain.marketplace.amazon.tax_deductions
  source_type: domain
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_APPLICABLE_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon.fee_taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.returns_reason_volume
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.returns_reason_volume
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_RULE.rule.amazon.amazon_fee_preview_filters
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_fee_preview_filters
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_RULE.rule.amazon.amazon_settlement_null_type
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_settlement_null_type
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_VALIDATION_TEST.validation_test.amazon.fee_preview_coverage
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: validation_test.amazon.fee_preview_coverage
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.active_records.INCLUDES_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.active_records
  source_type: execution_constraint_set
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.aggregate_before_join.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.fee_overcharge
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.aggregate_before_join
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.fee_overcharge
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.aggregate_before_join.INCLUDES_RULE.rule.amazon.amazon_disbursment_spelling
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.aggregate_before_join
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_disbursment_spelling
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.aggregate_before_join.INCLUDES_VALIDATION_TEST.validation_test.amazon.returns_source_active
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.aggregate_before_join
  source_type: execution_constraint_set
  target_id: validation_test.amazon.returns_source_active
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.fee_sign_semantics.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.fee_chargebacks
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.fee_sign_semantics
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.fee_chargebacks
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.fee_sign_semantics.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.return_margin_impact
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.fee_sign_semantics
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.return_margin_impact
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.fee_sign_semantics.INCLUDES_RULE.rule.amazon.amazon_disbursment_fee_context
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.fee_sign_semantics
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_disbursment_fee_context
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.fee_sign_semantics.INCLUDES_RULE.rule.amazon.amazon_refund_commission_positive
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.fee_sign_semantics
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_refund_commission_positive
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.advertising_spend
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.advertising_spend
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.b2b_b2c_split
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.b2b_b2c_split
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.fee_chargebacks
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.fee_chargebacks
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.fee_overcharge
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.fee_overcharge
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.gst_breakdown
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.gst_breakdown
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.realization_rate_month
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.realization_rate_month
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.return_margin_impact
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.return_margin_impact
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.returns_reason_volume
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.returns_reason_volume
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.revenue_by_state
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.revenue_by_state
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.settlement_cash_position
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.settlement_cash_position
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.tds_tcs_month
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.tds_tcs_month
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.volumetric_gap
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.volumetric_gap
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.worst_return_rate_skus
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.worst_return_rate_skus
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.no_hardcoded_scope.INCLUDES_RULE.rule.amazon.amazon_no_hardcoded_group_level
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.no_hardcoded_scope
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_no_hardcoded_group_level
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.returns_availability.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.returns_reason_volume
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.returns_availability
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.returns_reason_volume
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.returns_availability.INCLUDES_VALIDATION_TEST.validation_test.amazon.returns_source_active
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.returns_availability
  source_type: execution_constraint_set
  target_id: validation_test.amazon.returns_source_active
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.returns_availability.USES_OUTPUT_CONTRACT.output_contract.amazon.returns_reason
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: execution_constraint_set.amazon.returns_availability
  source_type: execution_constraint_set
  target_id: output_contract.amazon.returns_reason
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.revenue_vs_cashflow.APPLIES_TO_QUERY_PATTERN.query_pattern.amazon.return_margin_impact
  edge_type: APPLIES_TO_QUERY_PATTERN
  canonical_edge_type: APPLIES_TO_QUERY_PATTERN
  source_id: execution_constraint_set.amazon.revenue_vs_cashflow
  source_type: execution_constraint_set
  target_id: query_pattern.amazon.return_margin_impact
  target_type: query_pattern
  legacy_edge_aliases: []
  inverse_edge_type: HAS_EXECUTION_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.revenue_vs_cashflow.INCLUDES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: INCLUDES_RULE
  canonical_edge_type: INCLUDES_RULE
  source_id: execution_constraint_set.amazon.revenue_vs_cashflow
  source_type: execution_constraint_set
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases:
  - rule_enforced_by_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.execution_constraint_set.amazon.revenue_vs_cashflow.INCLUDES_VALIDATION_TEST.validation_test.amazon.oms_settlement_order_count
  edge_type: INCLUDES_VALIDATION_TEST
  canonical_edge_type: INCLUDES_VALIDATION_TEST
  source_id: execution_constraint_set.amazon.revenue_vs_cashflow
  source_type: execution_constraint_set
  target_id: validation_test.amazon.oms_settlement_order_count
  target_type: validation_test
  legacy_edge_aliases:
  - validation_enforces_constraint
  inverse_edge_type: INCLUDED_IN_CONSTRAINT_SET
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.matching_logic.amazon.fee_preview_to_actual_fee.primary.SUPPORTS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_id: matching_logic.amazon.fee_preview_to_actual_fee.primary
  source_type: matching_logic
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.matching_logic.amazon.oms_to_settlement.primary.SUPPORTS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_id: matching_logic.amazon.oms_to_settlement.primary
  source_type: matching_logic
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.matching_logic.amazon.returns_to_settlement.primary.SUPPORTS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_id: matching_logic.amazon.returns_to_settlement.primary
  source_type: matching_logic
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.matching_logic.amazon.settlement_to_disbursement.primary.SUPPORTS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement
  edge_type: SUPPORTS_RECONCILIATION_PROFILE
  canonical_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  source_id: matching_logic.amazon.settlement_to_disbursement.primary
  source_type: matching_logic
  target_id: reconciliation_profile.amazon.settlement_to_disbursement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USES_MATCHING_LOGIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.actual_fee_variance.DEPENDS_ON_METRIC.metric.marketplace.effective_fee_rate
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_id: metric.marketplace.actual_fee_variance
  source_type: metric
  target_id: metric.marketplace.effective_fee_rate
  target_type: metric
  legacy_edge_aliases:
  - metric_depends_on_metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  notes: Both compare actual fee behavior; variance uses fee preview expected values.
  source_old_edge_id: edge.metric_dependency.actual_fee_variance_depends_on_effective_fee_rate
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.actual_fee_variance.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.actual_fee_variance
  source_type: metric
  target_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.advertising_spend.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.advertising_spend
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.advertising_spend
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.average_order_value.DEPENDS_ON_METRIC.metric.marketplace.gross_revenue
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_id: metric.marketplace.average_order_value
  source_type: metric
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases:
  - metric_depends_on_metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  notes: AOV numerator is forward gross revenue.
  source_old_edge_id: edge.metric_dependency.aov_depends_on_gross_revenue
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.average_order_value.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.average_order_value
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.average_order_value
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.average_order_value
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.cancellation_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.cancellation_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.cancellation_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.discount_depth.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.discount_depth
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.discount_depth
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.discount_depth
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.effective_commission_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.effective_commission_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.effective_fee_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.effective_fee_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.effective_tax_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.effective_tax_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.effective_tax_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.fee_burden.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_fee_preview.fee_burden
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.fee_burden
  source_type: metric
  target_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.fee_recovery_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.fee_recovery_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_disbursment.transaction_types.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.forward_fee.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.forward_fee
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.forward_fee
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.gross_revenue.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.gross_revenue
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.gross_revenue
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.gross_revenue
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.marketplace_shipping_cost_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.marketplace_shipping_cost_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.net_revenue.DEPENDS_ON_METRIC.metric.marketplace.gross_revenue
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_id: metric.marketplace.net_revenue
  source_type: metric
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases:
  - metric_depends_on_metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  notes: Net revenue is forward/reverse netting of gross revenue semantics.
  source_old_edge_id: edge.metric_dependency.net_revenue_depends_on_gross_revenue
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.net_revenue.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.net_revenue
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.net_revenue
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.net_revenue
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.net_revenue_per_forward_order.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.net_revenue_per_forward_order
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.net_settlement_per_order.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.net_settlement_per_order
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.principal_revenue.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.principal_revenue
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.principal_revenue
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.return_loss.DEPENDS_ON_METRIC.metric.marketplace.return_rate
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_id: metric.marketplace.return_loss
  source_type: metric
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases:
  - metric_depends_on_metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  notes: Return loss analysis depends on identifying returned orders and fee recovery.
  source_old_edge_id: edge.metric_dependency.return_loss_depends_on_return_rate
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.return_loss.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_disbursment.return_loss
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.return_loss
  source_type: metric
  target_id: metric_implementation.amazon.amazon_disbursment.return_loss
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.return_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.return_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.return_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.return_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.return_value_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.return_value_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.return_value_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.return_value_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.revenue_per_unit.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.revenue_per_unit
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.revenue_per_unit
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.safe_t_recovery_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.safe_t_recovery_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.seller_realization_rate.DEPENDS_ON_METRIC.metric.marketplace.settlement_cash_position
  edge_type: DEPENDS_ON_METRIC
  canonical_edge_type: DEPENDS_ON_METRIC
  source_id: metric.marketplace.seller_realization_rate
  source_type: metric
  target_id: metric.marketplace.settlement_cash_position
  target_type: metric
  legacy_edge_aliases:
  - metric_depends_on_metric
  inverse_edge_type: DEPENDENCY_OF_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  notes: Both use settlement total but realization divides by product_sales orders.
  source_old_edge_id: edge.metric_dependency.seller_realization_depends_on_settlement_cash_position
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.seller_realization_rate.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.seller_realization_rate
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.seller_realization_rate
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.settlement_cash_position.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.settlement_cash_position
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.settlement_cash_position
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.taxable_revenue.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_oms.taxable_revenue
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.taxable_revenue
  source_type: metric
  target_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.tds_tcs_deductions.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.tds_tcs_deductions
  source_type: metric
  target_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric.marketplace.volumetric_excess_percent.HAS_IMPLEMENTATION.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  edge_type: HAS_IMPLEMENTATION
  canonical_edge_type: HAS_IMPLEMENTATION
  source_id: metric.marketplace.volumetric_excess_percent
  source_type: metric
  target_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  target_type: metric_implementation
  legacy_edge_aliases: []
  inverse_edge_type: IMPLEMENTS_METRIC
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.actual_fee_variance_depends_on_effective_fee_rate.PARENT_METRIC.metric.marketplace.actual_fee_variance
  edge_type: PARENT_METRIC
  canonical_edge_type: PARENT_METRIC
  source_id: metric_dependency.amazon.actual_fee_variance_depends_on_effective_fee_rate
  source_type: metric_dependency
  target_id: metric.marketplace.actual_fee_variance
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.actual_fee_variance_depends_on_effective_fee_rate.USES_DEPENDENT_METRIC.metric.marketplace.effective_fee_rate
  edge_type: USES_DEPENDENT_METRIC
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_id: metric_dependency.amazon.actual_fee_variance_depends_on_effective_fee_rate
  source_type: metric_dependency
  target_id: metric.marketplace.effective_fee_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.aov_depends_on_gross_revenue.PARENT_METRIC.metric.marketplace.average_order_value
  edge_type: PARENT_METRIC
  canonical_edge_type: PARENT_METRIC
  source_id: metric_dependency.amazon.aov_depends_on_gross_revenue
  source_type: metric_dependency
  target_id: metric.marketplace.average_order_value
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.aov_depends_on_gross_revenue.USES_DEPENDENT_METRIC.metric.marketplace.gross_revenue
  edge_type: USES_DEPENDENT_METRIC
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_id: metric_dependency.amazon.aov_depends_on_gross_revenue
  source_type: metric_dependency
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.net_revenue_depends_on_gross_revenue.PARENT_METRIC.metric.marketplace.net_revenue
  edge_type: PARENT_METRIC
  canonical_edge_type: PARENT_METRIC
  source_id: metric_dependency.amazon.net_revenue_depends_on_gross_revenue
  source_type: metric_dependency
  target_id: metric.marketplace.net_revenue
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.net_revenue_depends_on_gross_revenue.USES_DEPENDENT_METRIC.metric.marketplace.gross_revenue
  edge_type: USES_DEPENDENT_METRIC
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_id: metric_dependency.amazon.net_revenue_depends_on_gross_revenue
  source_type: metric_dependency
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.return_loss_depends_on_return_rate.PARENT_METRIC.metric.marketplace.return_loss
  edge_type: PARENT_METRIC
  canonical_edge_type: PARENT_METRIC
  source_id: metric_dependency.amazon.return_loss_depends_on_return_rate
  source_type: metric_dependency
  target_id: metric.marketplace.return_loss
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.return_loss_depends_on_return_rate.USES_DEPENDENT_METRIC.metric.marketplace.return_rate
  edge_type: USES_DEPENDENT_METRIC
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_id: metric_dependency.amazon.return_loss_depends_on_return_rate
  source_type: metric_dependency
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.seller_realization_depends_on_settlement_cash_position.PARENT_METRIC.metric.marketplace.seller_realization_rate
  edge_type: PARENT_METRIC
  canonical_edge_type: PARENT_METRIC
  source_id: metric_dependency.amazon.seller_realization_depends_on_settlement_cash_position
  source_type: metric_dependency
  target_id: metric.marketplace.seller_realization_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC_DEPENDENCY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_dependency.amazon.seller_realization_depends_on_settlement_cash_position.USES_DEPENDENT_METRIC.metric.marketplace.settlement_cash_position
  edge_type: USES_DEPENDENT_METRIC
  canonical_edge_type: USES_DEPENDENT_METRIC
  source_id: metric_dependency.amazon.seller_realization_depends_on_settlement_cash_position
  source_type: metric_dependency
  target_id: metric.marketplace.settlement_cash_position
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: DEPENDENCY_USED_BY
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.IMPLEMENTS_METRIC.metric.marketplace.effective_commission_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: metric.marketplace.effective_commission_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.effective_commission_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  - ev.amazon_disbursment.queries.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.effective_commission_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.IMPLEMENTS_METRIC.metric.marketplace.effective_fee_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: metric.marketplace.effective_fee_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.effective_fee_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.effective_fee_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.IMPLEMENTS_METRIC.metric.marketplace.fee_recovery_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  source_type: metric_implementation
  target_id: metric.marketplace.fee_recovery_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_disbursment.transaction_types.001
  - ev.amazon_disbursment.queries.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_disbursment.transaction_types.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_disbursment.transaction_types.001
  - ev.amazon_disbursment.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.fee_recovery_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_disbursment.transaction_types.001
  - ev.amazon_disbursment.queries.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.fee_recovery_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.IMPLEMENTS_METRIC.metric.marketplace.forward_fee
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: metric.marketplace.forward_fee
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.forward_fee.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.USES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.forward_fee.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.forward_fee
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.forward_fee.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.IMPLEMENTS_METRIC.metric.marketplace.marketplace_shipping_cost_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: metric.marketplace.marketplace_shipping_cost_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.marketplace_shipping_cost_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.IMPLEMENTS_METRIC.metric.marketplace.principal_revenue
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: metric.marketplace.principal_revenue
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.principal_revenue.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.USES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.principal_revenue.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.principal_revenue
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.principal_revenue.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.return_loss.IMPLEMENTS_METRIC.metric.marketplace.return_loss
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_disbursment.return_loss
  source_type: metric_implementation
  target_id: metric.marketplace.return_loss
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.return_loss.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.return_loss.USES_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.return_loss
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.return_loss.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_disbursment.return_loss
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.return_loss.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_return_loss
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_disbursment.return_loss
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_return_loss
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_disbursment.return_loss.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_disbursment.return_loss
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_disbursment.return_loss.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.IMPLEMENTS_METRIC.metric.marketplace.actual_fee_variance
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: metric.marketplace.actual_fee_variance
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_COLUMN.column.zs_observe.amazon_fee_preview.gross_commission
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.gross_commission
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_COLUMN.column.zs_observe.amazon_fee_preview.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_COLUMN.column.zs_observe.amazon_fee_preview.zen_status
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.zen_status
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_fee_preview_total_fee
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_fee_preview_total_fee
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_fee_variance
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_fee_variance
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_fee_preview.actual_fee_variance
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.actual_fee_variance.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.IMPLEMENTS_METRIC.metric.marketplace.fee_burden
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: metric.marketplace.fee_burden
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.fee_burden.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_COLUMN.column.zs_observe.amazon_fee_preview.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_COLUMN.column.zs_observe.amazon_fee_preview.gross_commission
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.gross_commission
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_COLUMN.column.zs_observe.amazon_fee_preview.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_COLUMN.column.zs_observe.amazon_fee_preview.sku
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.sku
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_COLUMN.column.zs_observe.amazon_fee_preview.zen_status
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.zen_status
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_fee_preview_total_fee
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_fee_preview_total_fee
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.fee_burden.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_fee_preview.fee_burden
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.fee_cost.001
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.fee_burden.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.IMPLEMENTS_METRIC.metric.marketplace.volumetric_excess_percent
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: metric.marketplace.volumetric_excess_percent
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_COLUMN.column.zs_observe.amazon_fee_preview.gross_weight
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.gross_weight
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_COLUMN.column.zs_observe.amazon_fee_preview.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_COLUMN.column.zs_observe.amazon_fee_preview.volumetric_weight
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.volumetric_weight
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_COLUMN.column.zs_observe.amazon_fee_preview.zen_status
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_fee_preview.zen_status
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_volumetric_weight
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_volumetric_weight
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_fee_preview.volumetric_excess_percent.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.IMPLEMENTS_METRIC.metric.marketplace.average_order_value
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: metric.marketplace.average_order_value
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.average_order_value.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.USES_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.average_order_value.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.average_order_value
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.average_order_value.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.IMPLEMENTS_METRIC.metric.marketplace.cancellation_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: metric.marketplace.cancellation_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.cancellation_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.USES_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_cancellation_rate
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_cancellation_rate
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.cancellation_rate.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.cancellation_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.cancellation_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.IMPLEMENTS_METRIC.metric.marketplace.discount_depth
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: metric.marketplace.discount_depth
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.discount_depth.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.USES_COLUMN.column.zs_observe.amazon_oms.item_amount_excluding_tax
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.item_amount_excluding_tax
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.USES_COLUMN.column.zs_observe.amazon_oms.item_promo_discount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.item_promo_discount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.discount_depth.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.discount_depth
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.discount_depth.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.IMPLEMENTS_METRIC.metric.marketplace.effective_tax_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: metric.marketplace.effective_tax_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.effective_tax_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount_excluding_tax
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount_excluding_tax
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_COLUMN.column.zs_observe.amazon_oms.total_tax
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.total_tax
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_effective_tax_rate
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_effective_tax_rate
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.effective_tax_rate.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.effective_tax_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.effective_tax_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.IMPLEMENTS_METRIC.metric.marketplace.gross_revenue
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.gross_revenue.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_oms_revenue_formula
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_oms_revenue_formula
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.gross_revenue.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.gross_revenue
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.gross_revenue.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.IMPLEMENTS_METRIC.metric.marketplace.net_revenue
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: metric.marketplace.net_revenue
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.net_revenue.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_oms_revenue_formula
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_oms_revenue_formula
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.net_revenue
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.net_revenue.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.IMPLEMENTS_METRIC.metric.marketplace.net_revenue_per_forward_order
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: metric.marketplace.net_revenue_per_forward_order
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.USES_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.net_revenue_per_forward_order.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.IMPLEMENTS_METRIC.metric.marketplace.return_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.return_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.USES_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_return_rate
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_return_rate
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_rate.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.return_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  - ev.amazon_oms.transaction_types.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.return_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_value_rate.IMPLEMENTS_METRIC.metric.marketplace.return_value_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.return_value_rate
  source_type: metric_implementation
  target_id: metric.marketplace.return_value_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.return_value_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_value_rate.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_value_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_value_rate.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_value_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_value_rate.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.return_value_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.return_value_rate.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.return_value_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.return_cancel.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.return_value_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.revenue_per_unit.IMPLEMENTS_METRIC.metric.marketplace.revenue_per_unit
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  source_type: metric_implementation
  target_id: metric.marketplace.revenue_per_unit
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.revenue_per_unit.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.revenue_per_unit.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.revenue_per_unit.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.revenue_per_unit.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.revenue_per_unit.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.revenue_per_unit.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.IMPLEMENTS_METRIC.metric.marketplace.taxable_revenue
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: metric.marketplace.taxable_revenue
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.taxable_revenue.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount_excluding_tax
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.charged_amount_excluding_tax
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.USES_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_oms_revenue_formula
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_oms_revenue_formula
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_oms.taxable_revenue.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_oms.taxable_revenue
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_oms.taxable_revenue.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.IMPLEMENTS_METRIC.metric.marketplace.advertising_spend
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: metric.marketplace.advertising_spend
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.advertising_spend.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_COLUMN.column.zs_observe.amazon_settlement.description
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.description
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_COLUMN.column.zs_observe.amazon_settlement.marketplace
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.marketplace
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_COLUMN.column.zs_observe.amazon_settlement.total
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.advertising_spend.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.advertising_spend
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.advertising_spend.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.IMPLEMENTS_METRIC.metric.marketplace.net_settlement_per_order
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  source_type: metric_implementation
  target_id: metric.marketplace.net_settlement_per_order
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.USES_COLUMN.column.zs_observe.amazon_settlement.order_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.USES_COLUMN.column.zs_observe.amazon_settlement.settled_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.settled_amount
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.net_settlement_per_order
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.net_settlement_per_order.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.IMPLEMENTS_METRIC.metric.marketplace.safe_t_recovery_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  source_type: metric_implementation
  target_id: metric.marketplace.safe_t_recovery_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.USES_COLUMN.column.zs_observe.amazon_settlement.total
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.USES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.safe_t_recovery_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.IMPLEMENTS_METRIC.metric.marketplace.seller_realization_rate
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: metric.marketplace.seller_realization_rate
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.seller_realization_rate.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_COLUMN.column.zs_observe.amazon_settlement.group_level_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.group_level_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_COLUMN.column.zs_observe.amazon_settlement.product_sales
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.product_sales
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_COLUMN.column.zs_observe.amazon_settlement.total
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_seller_realization_rate
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_seller_realization_rate
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_settlement_total
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_settlement_total
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.seller_realization_rate.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.seller_realization_rate
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.settlement.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.seller_realization_rate.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.IMPLEMENTS_METRIC.metric.marketplace.settlement_cash_position
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: metric.marketplace.settlement_cash_position
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.settlement_cash_position.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_COLUMN.column.zs_observe.amazon_settlement.settlement_id
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.settlement_id
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_COLUMN.column.zs_observe.amazon_settlement.total
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_FORMULA_TEMPLATE.formula_template.amazon.amazon_settlement_total
  edge_type: USES_FORMULA_TEMPLATE
  canonical_edge_type: USES_FORMULA_TEMPLATE
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: formula_template.amazon.amazon_settlement_total
  target_type: formula_template
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.settlement_cash_position.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.settlement_cash_position
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon.settlement_cycle.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.settlement_cash_position.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.IMPLEMENTS_METRIC.metric.marketplace.tds_tcs_deductions
  edge_type: IMPLEMENTS_METRIC
  canonical_edge_type: IMPLEMENTS_METRIC
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: metric.marketplace.tds_tcs_deductions
  target_type: metric
  legacy_edge_aliases:
  - implements_metric
  inverse_edge_type: HAS_IMPLEMENTATION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.implements
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.marketplace
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.marketplace
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.tcs_cgst
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.tcs_cgst
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.tcs_igst
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.tcs_igst
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.tcs_sgst
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.tcs_sgst
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_COLUMN.column.zs_observe.amazon_settlement.tds
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: column.zs_observe.amazon_settlement.tds
  target_type: column
  legacy_edge_aliases:
  - implementation_uses_column
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: metric_implementation.amazon.amazon_settlement.tds_tcs_deductions
  source_type: metric_implementation
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - implementation_uses_table
  inverse_edge_type: USED_BY_IMPLEMENTATION
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.metric_implementation.amazon.amazon_settlement.tds_tcs_deductions.uses_table
```
```yaml
candidate_edge:
  edge_id: edge.amazon.output_contract.amazon.fee_variance.TARGETS_CARD.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: output_contract.amazon.fee_variance
  source_type: output_contract
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.output_contract.amazon.oms_settlement_recon.TARGETS_CARD.reconciliation_profile.amazon.oms_to_settlement
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: output_contract.amazon.oms_settlement_recon
  source_type: output_contract
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.output_contract.amazon.return_rate.TARGETS_CARD.metric.marketplace.return_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: output_contract.amazon.return_rate
  source_type: output_contract
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.output_contract.amazon.returns_reason.TARGETS_CARD.table.zs_observe.amazon_returns
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: output_contract.amazon.returns_reason
  source_type: output_contract
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.output_contract.amazon.settlement_waterfall.TARGETS_CARD.metric.marketplace.seller_realization_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: output_contract.amazon.settlement_waterfall
  source_type: output_contract
  target_id: metric.marketplace.seller_realization_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.platform.amazon.HAS_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: HAS_PLATFORM_CONTEXT
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_id: platform.amazon
  source_type: platform
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_oms.purpose.001
  - ev.amazon_settlement.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.platform.amazon.HAS_PLATFORM_CONTEXT.platform_context.amazon.international
  edge_type: HAS_PLATFORM_CONTEXT
  canonical_edge_type: HAS_PLATFORM_CONTEXT
  source_id: platform.amazon
  source_type: platform
  target_id: platform_context.amazon.international
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_PLATFORM
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.platform_context.amazon.in.BELONGS_TO_PLATFORM.platform.amazon
  edge_type: BELONGS_TO_PLATFORM
  canonical_edge_type: BELONGS_TO_PLATFORM
  source_id: platform_context.amazon.in
  source_type: platform_context
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_oms.purpose.001
  - ev.amazon_settlement.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.platform_context.amazon.international.BELONGS_TO_PLATFORM.platform.amazon
  edge_type: BELONGS_TO_PLATFORM
  canonical_edge_type: BELONGS_TO_PLATFORM
  source_id: platform_context.amazon.international
  source_type: platform_context
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_PLATFORM_CONTEXT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.process_variant.amazon.fba_fulfilment_variant.EXTENDS_PROCESS.business_process.amazon.order_to_settlement
  edge_type: EXTENDS_PROCESS
  canonical_edge_type: EXTENDS_PROCESS
  source_id: process_variant.amazon.fba_fulfilment_variant
  source_type: process_variant
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: HAS_PROCESS_VARIANT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.process_variant.amazon.india_vs_international_returns_variant.EXTENDS_PROCESS.business_process.amazon.return_to_settlement
  edge_type: EXTENDS_PROCESS
  canonical_edge_type: EXTENDS_PROCESS
  source_id: process_variant.amazon.india_vs_international_returns_variant
  source_type: process_variant
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: HAS_PROCESS_VARIANT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.process_variant.amazon.mfn_easyship_variant.EXTENDS_PROCESS.business_process.amazon.order_to_settlement
  edge_type: EXTENDS_PROCESS
  canonical_edge_type: EXTENDS_PROCESS
  source_id: process_variant.amazon.mfn_easyship_variant
  source_type: process_variant
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases: []
  inverse_edge_type: HAS_PROCESS_VARIANT
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.advertising_spend.HAS_VALIDATION_TEST.validation_test.amazon.settlement_total_formula
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.advertising_spend
  source_type: query_pattern
  target_id: validation_test.amazon.settlement_total_formula
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.advertising_spend.PRODUCES_METRIC.metric.marketplace.advertising_spend
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.advertising_spend
  source_type: query_pattern
  target_id: metric.marketplace.advertising_spend
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.advertising_spend.TARGETS_CARD.metric.marketplace.advertising_spend
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.advertising_spend
  source_type: query_pattern
  target_id: metric.marketplace.advertising_spend
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.advertising_spend.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.advertising_spend
  source_type: query_pattern
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.PRODUCES_METRIC.metric.marketplace.gross_revenue
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.TARGETS_CARD.metric.marketplace.gross_revenue
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.b2b_b2c_split.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.b2b_b2c_split
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.PRODUCES_METRIC.metric.marketplace.marketplace_shipping_cost_rate
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: metric.marketplace.marketplace_shipping_cost_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.REQUIRES_RULE.rule.amazon.amazon_disbursment_fee_context
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_fee_context
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.REQUIRES_RULE.rule.amazon.amazon_disbursment_spelling
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_spelling
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.TARGETS_CARD.metric.marketplace.marketplace_shipping_cost_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: metric.marketplace.marketplace_shipping_cost_rate
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.USES_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_chargebacks.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.fee_chargebacks
  source_type: query_pattern
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.HAS_VALIDATION_TEST.validation_test.amazon.fee_preview_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: validation_test.amazon.fee_preview_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.PRODUCES_METRIC.metric.marketplace.actual_fee_variance
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: metric.marketplace.actual_fee_variance
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.REQUIRES_RULE.rule.amazon.amazon_disbursment_fee_context
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_fee_context
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.REQUIRES_RULE.rule.amazon.amazon_disbursment_spelling
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_spelling
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.REQUIRES_RULE.rule.amazon.amazon_fee_preview_filters
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: rule.amazon.amazon_fee_preview_filters
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.TARGETS_CARD.metric.marketplace.actual_fee_variance
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: metric.marketplace.actual_fee_variance
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.USES_OUTPUT_CONTRACT.output_contract.amazon.fee_variance
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: output_contract.amazon.fee_variance
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.USES_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.USES_RELATIONSHIP.relationship.amazon.fee_preview_to_disbursment.sku
  edge_type: USES_RELATIONSHIP
  canonical_edge_type: USES_RELATIONSHIP
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: relationship.amazon.fee_preview_to_disbursment.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.fee_overcharge.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.fee_overcharge
  source_type: query_pattern
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.HAS_VALIDATION_TEST.validation_test.amazon.effective_tax_denominator
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: validation_test.amazon.effective_tax_denominator
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.PRODUCES_METRIC.metric.marketplace.effective_tax_rate
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: metric.marketplace.effective_tax_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.REQUIRES_RULE.rule.amazon.amazon_tax_denominator
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: rule.amazon.amazon_tax_denominator
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.TARGETS_CARD.metric.marketplace.effective_tax_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: metric.marketplace.effective_tax_rate
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.gst_breakdown.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.gst_breakdown
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.kpis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.HAS_VALIDATION_TEST.validation_test.amazon.settlement_total_formula
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: validation_test.amazon.settlement_total_formula
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.PRODUCES_METRIC.metric.marketplace.seller_realization_rate
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: metric.marketplace.seller_realization_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.TARGETS_CARD.metric.marketplace.seller_realization_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: metric.marketplace.seller_realization_rate
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.USES_OUTPUT_CONTRACT.output_contract.amazon.oms_settlement_recon
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: output_contract.amazon.oms_settlement_recon
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.USES_OUTPUT_CONTRACT.output_contract.amazon.settlement_waterfall
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: output_contract.amazon.settlement_waterfall
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.realization_rate_month.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.realization_rate_month
  source_type: query_pattern
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.PRODUCES_METRIC.metric.marketplace.return_loss
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: metric.marketplace.return_loss
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.REQUIRES_RULE.rule.amazon.amazon_disbursment_fee_context
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_fee_context
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.REQUIRES_RULE.rule.amazon.amazon_disbursment_spelling
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: rule.amazon.amazon_disbursment_spelling
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.TARGETS_CARD.metric.marketplace.return_loss
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: metric.marketplace.return_loss
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.USES_RELATIONSHIP.relationship.amazon.oms_to_disbursment.order_id
  edge_type: USES_RELATIONSHIP
  canonical_edge_type: USES_RELATIONSHIP
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: relationship.amazon.oms_to_disbursment.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.return_margin_impact.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.return_margin_impact
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.HAS_VALIDATION_TEST.validation_test.amazon.returns_source_active
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: validation_test.amazon.returns_source_active
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.PRODUCES_METRIC.metric.marketplace.return_rate
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.TARGETS_CARD.metric.marketplace.return_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.USES_OUTPUT_CONTRACT.output_contract.amazon.return_rate
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: output_contract.amazon.return_rate
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.USES_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.returns_reason_volume.USES_TABLE.table.zs_observe.amazon_returns
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.returns_reason_volume
  source_type: query_pattern
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.queries.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.PRODUCES_METRIC.metric.marketplace.gross_revenue
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.TARGETS_CARD.metric.marketplace.gross_revenue
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: metric.marketplace.gross_revenue
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.revenue_by_state.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.revenue_by_state
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.settlement_cash_position.HAS_VALIDATION_TEST.validation_test.amazon.settlement_total_formula
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.settlement_cash_position
  source_type: query_pattern
  target_id: validation_test.amazon.settlement_total_formula
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.settlement_cash_position.PRODUCES_METRIC.metric.marketplace.settlement_cash_position
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.settlement_cash_position
  source_type: query_pattern
  target_id: metric.marketplace.settlement_cash_position
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.settlement_cash_position.TARGETS_CARD.metric.marketplace.settlement_cash_position
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.settlement_cash_position
  source_type: query_pattern
  target_id: metric.marketplace.settlement_cash_position
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.settlement_cash_position.USES_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement
  edge_type: USES_RECONCILIATION_PROFILE
  canonical_edge_type: USES_RECONCILIATION_PROFILE
  source_id: query_pattern.amazon.settlement_cash_position
  source_type: query_pattern
  target_id: reconciliation_profile.amazon.settlement_to_disbursement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.settlement_cash_position.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.settlement_cash_position
  source_type: query_pattern
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.HAS_VALIDATION_TEST.validation_test.amazon.settlement_total_formula
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: validation_test.amazon.settlement_total_formula
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.PRODUCES_METRIC.metric.marketplace.tds_tcs_deductions
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: metric.marketplace.tds_tcs_deductions
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.TARGETS_CARD.metric.marketplace.tds_tcs_deductions
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: metric.marketplace.tds_tcs_deductions
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.USES_RELATIONSHIP.relationship.amazon.oms_to_settlement.order_id
  edge_type: USES_RELATIONSHIP
  canonical_edge_type: USES_RELATIONSHIP
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: relationship.amazon.oms_to_settlement.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.tds_tcs_month.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.tds_tcs_month
  source_type: query_pattern
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.volumetric_gap.HAS_VALIDATION_TEST.validation_test.amazon.fee_preview_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.volumetric_gap
  source_type: query_pattern
  target_id: validation_test.amazon.fee_preview_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.volumetric_gap.PRODUCES_METRIC.metric.marketplace.volumetric_excess_percent
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.volumetric_gap
  source_type: query_pattern
  target_id: metric.marketplace.volumetric_excess_percent
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.volumetric_gap.REQUIRES_RULE.rule.amazon.amazon_fee_preview_filters
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.volumetric_gap
  source_type: query_pattern
  target_id: rule.amazon.amazon_fee_preview_filters
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.volumetric_gap.TARGETS_CARD.metric.marketplace.volumetric_excess_percent
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.volumetric_gap
  source_type: query_pattern
  target_id: metric.marketplace.volumetric_excess_percent
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.volumetric_gap.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.volumetric_gap
  source_type: query_pattern
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.packaging_weight.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: VALIDATES_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.PRODUCES_METRIC.metric.marketplace.return_rate
  edge_type: PRODUCES_METRIC
  canonical_edge_type: PRODUCES_METRIC
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: PRODUCED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.REQUIRES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.REQUIRES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.REQUIRES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: REQUIRES_RULE
  canonical_edge_type: REQUIRES_RULE
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: REQUIRED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.TARGETS_CARD.metric.marketplace.return_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: metric.marketplace.return_rate
  target_type: metric
  legacy_edge_aliases:
  - query_targets_card
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.USES_OUTPUT_CONTRACT.output_contract.amazon.return_rate
  edge_type: USES_OUTPUT_CONTRACT
  canonical_edge_type: USES_OUTPUT_CONTRACT
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: output_contract.amazon.return_rate
  target_type: output_contract
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.query_pattern.amazon.worst_return_rate_skus.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: query_pattern.amazon.worst_return_rate_skus
  source_type: query_pattern
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - query_requires_table
  inverse_edge_type: USED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.analytical_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.fee_preview_to_actual_fee.category_reclassification
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.fee_preview_to_actual_fee.category_reclassification
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_mismatch.category_reclassification
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.fee_preview_to_actual_fee.fee_tier_change
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.fee_preview_to_actual_fee.fee_tier_change
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_mismatch.fee_tier_change
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.fee_preview_to_actual_fee.overcharge_variance
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.fee_preview_to_actual_fee.overcharge_variance
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_mismatch.overcharge_variance
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.fee_preview_to_actual_fee.price_difference
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.fee_preview_to_actual_fee.price_difference
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_mismatch.price_difference
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.fee_preview_to_actual_fee.weight_dimension_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.fee_preview_to_actual_fee.weight_dimension_mismatch
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_mismatch.weight_dimension_mismatch
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_PRIMARY_UNIT.reconciliation_unit.amazon.fee_preview_to_actual_fee.sku
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: reconciliation_unit.amazon.fee_preview_to_actual_fee.sku
  target_type: reconciliation_unit
  legacy_edge_aliases:
  - profile_uses_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_unit
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.fee_preview_to_actual_fee.actual.side_role_actual
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_actual_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    side_role: actual
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_side.actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.side_role_expected
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_expected_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    side_role: expected
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_side.expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.SUPPORTS_PROCESS.domain.marketplace.amazon.reconciliation
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  notes: Materialized inverse of edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  materialized_inverse_of: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.fee_preview_to_actual_fee.USES_MATCHING_LOGIC.matching_logic.amazon.fee_preview_to_actual_fee.primary
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  source_type: reconciliation_profile
  target_id: matching_logic.amazon.fee_preview_to_actual_fee.primary
  target_type: matching_logic
  legacy_edge_aliases:
  - profile_uses_matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.oms_to_settlement.order_count_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.oms_to_settlement.order_count_mismatch
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_mismatch.order_count_mismatch
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.oms_to_settlement.revenue_mismatch
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.oms_to_settlement.revenue_mismatch
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_mismatch.revenue_mismatch
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.oms_to_settlement.yet_to_be_settled
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.oms_to_settlement.yet_to_be_settled
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_mismatch.yet_to_be_settled
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_PRIMARY_UNIT.reconciliation_unit.amazon.oms_to_settlement.order
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_unit.amazon.oms_to_settlement.order
  target_type: reconciliation_unit
  legacy_edge_aliases:
  - profile_uses_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_unit
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.oms_to_settlement.actual.side_role_actual
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.oms_to_settlement.actual
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_actual_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    side_role: actual
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_side.actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.oms_to_settlement.expected.side_role_expected
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.oms_to_settlement.expected
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_expected_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    side_role: expected
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_side.expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.SUPPORTS_PROCESS.domain.marketplace.amazon.reconciliation
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  notes: Materialized inverse of edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement
  materialized_inverse_of: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.oms_to_settlement.USES_MATCHING_LOGIC.matching_logic.amazon.oms_to_settlement.primary
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_id: reconciliation_profile.amazon.oms_to_settlement
  source_type: reconciliation_profile
  target_id: matching_logic.amazon.oms_to_settlement.primary
  target_type: matching_logic
  legacy_edge_aliases:
  - profile_uses_matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.returns_to_settlement.fee_recovery_gap
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.returns_to_settlement.fee_recovery_gap
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_mismatch.fee_recovery_gap
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.returns_to_settlement.inactive_return_source
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.returns_to_settlement.inactive_return_source
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_mismatch.inactive_return_source
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.returns_to_settlement.missing_refund_settlement
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.returns_to_settlement.missing_refund_settlement
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_mismatch.missing_refund_settlement
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_PRIMARY_UNIT.reconciliation_unit.amazon.returns_to_settlement.return_order
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_unit.amazon.returns_to_settlement.return_order
  target_type: reconciliation_unit
  legacy_edge_aliases:
  - profile_uses_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_unit
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.returns_to_settlement.actual.side_role_actual
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.returns_to_settlement.actual
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_actual_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    side_role: actual
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_side.actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.returns_to_settlement.expected.side_role_expected
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.returns_to_settlement.expected
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_expected_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    side_role: expected
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_side.expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.SUPPORTS_PROCESS.domain.marketplace.amazon.reconciliation
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  notes: Materialized inverse of edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
  materialized_inverse_of: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.returns_to_settlement.USES_MATCHING_LOGIC.matching_logic.amazon.returns_to_settlement.primary
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_id: reconciliation_profile.amazon.returns_to_settlement
  source_type: reconciliation_profile
  target_id: matching_logic.amazon.returns_to_settlement.primary
  target_type: matching_logic
  legacy_edge_aliases:
  - profile_uses_matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.settlement_to_disbursement.different_settlement_id_mapping
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.settlement_to_disbursement.different_settlement_id_mapping
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_mismatch.different_settlement_id_mapping
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.settlement_to_disbursement.missing_disbursement_rows
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.settlement_to_disbursement.missing_disbursement_rows
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_mismatch.missing_disbursement_rows
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_MISMATCH_CATEGORY.mismatch_category.amazon.settlement_to_disbursement.timing_difference
  edge_type: HAS_MISMATCH_CATEGORY
  canonical_edge_type: HAS_MISMATCH_CATEGORY
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: mismatch_category.amazon.settlement_to_disbursement.timing_difference
  target_type: mismatch_category
  legacy_edge_aliases:
  - profile_has_mismatch_category
  inverse_edge_type: MISMATCH_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_mismatch.timing_difference
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_PRIMARY_UNIT.reconciliation_unit.amazon.settlement_to_disbursement.order_settlement
  edge_type: HAS_PRIMARY_UNIT
  canonical_edge_type: HAS_PRIMARY_UNIT
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: reconciliation_unit.amazon.settlement_to_disbursement.order_settlement
  target_type: reconciliation_unit
  legacy_edge_aliases:
  - profile_uses_unit
  inverse_edge_type: PRIMARY_UNIT_OF_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_unit
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.settlement_to_disbursement.actual.side_role_actual
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_actual_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    side_role: actual
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_side.actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.HAS_RECONCILIATION_SIDE.reconciliation_side.amazon.settlement_to_disbursement.expected.side_role_expected
  edge_type: HAS_RECONCILIATION_SIDE
  canonical_edge_type: HAS_RECONCILIATION_SIDE
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  target_type: reconciliation_side
  legacy_edge_aliases:
  - profile_expected_side
  inverse_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    side_role: expected
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.has_side.expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.SUPPORTS_PROCESS.domain.marketplace.amazon.reconciliation
  edge_type: SUPPORTS_PROCESS
  canonical_edge_type: SUPPORTS_PROCESS
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: domain.marketplace.amazon.reconciliation
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  notes: Materialized inverse of edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement
  materialized_inverse_of: edge.amazon.domain.marketplace.amazon.reconciliation.HAS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_profile.amazon.settlement_to_disbursement.USES_MATCHING_LOGIC.matching_logic.amazon.settlement_to_disbursement.primary
  edge_type: USES_MATCHING_LOGIC
  canonical_edge_type: USES_MATCHING_LOGIC
  source_id: reconciliation_profile.amazon.settlement_to_disbursement
  source_type: reconciliation_profile
  target_id: matching_logic.amazon.settlement_to_disbursement.primary
  target_type: matching_logic
  legacy_edge_aliases:
  - profile_uses_matching_logic
  inverse_edge_type: SUPPORTS_RECONCILIATION_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.reconciliation_profile.amazon.settlement_to_disbursement.uses_matching_logic
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.actual.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee.side_role_actual
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    side_role: actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.actual.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.actual.USES_COLUMN.column.zs_observe.amazon_disbursment.sku.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_disbursment.sku
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.actual.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.actual
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee.side_role_expected
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    side_role: expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_COLUMN.column.zs_observe.amazon_fee_preview.charged_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_fee_preview.charged_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_COLUMN.column.zs_observe.amazon_fee_preview.fixed_fee.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_fee_preview.fixed_fee
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_COLUMN.column.zs_observe.amazon_fee_preview.gross_commission.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_fee_preview.gross_commission
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_COLUMN.column.zs_observe.amazon_fee_preview.referral_fee.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_fee_preview.referral_fee
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_COLUMN.column.zs_observe.amazon_fee_preview.sku.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_fee_preview.sku
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.fee_preview_to_actual_fee.expected.USES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.fee_preview_to_actual_fee.expected
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement.side_role_actual
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    side_role: actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.product_sales.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.product_sales
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.settled_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.settled_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.total.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.actual.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.oms_to_settlement.actual
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.expected.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement.side_role_expected
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.oms_to_settlement.expected
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    side_role: expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.expected.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.expected.USES_COLUMN.column.zs_observe.amazon_oms.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.expected.USES_COLUMN.column.zs_observe.amazon_oms.settled_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.oms_to_settlement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_oms.settled_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.oms_to_settlement.expected.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.oms_to_settlement.expected
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.actual.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement.side_role_actual
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.returns_to_settlement.actual
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    side_role: actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.returns_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.product_sales.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.returns_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.product_sales
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.actual.USES_COLUMN.column.zs_observe.amazon_settlement.total.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.returns_to_settlement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.actual.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.returns_to_settlement.actual
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.expected.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement.side_role_expected
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.returns_to_settlement.expected
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    side_role: expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.expected.USES_COLUMN.column.zs_observe.amazon_oms.charged_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.returns_to_settlement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.expected.USES_COLUMN.column.zs_observe.amazon_oms.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.returns_to_settlement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.returns_to_settlement.expected.USES_TABLE.table.zs_observe.amazon_oms
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.returns_to_settlement.expected
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.actual.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement.side_role_actual
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.settlement_to_disbursement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    side_role: actual
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.actual.USES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.actual.USES_COLUMN.column.zs_observe.amazon_disbursment.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_disbursment.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.actual.USES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.settlement_to_disbursement.actual
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.expected.BELONGS_TO_RECONCILIATION_PROFILE.reconciliation_profile.amazon.settlement_to_disbursement.side_role_expected
  edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  canonical_edge_type: BELONGS_TO_RECONCILIATION_PROFILE
  source_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  source_type: reconciliation_side
  target_id: reconciliation_profile.amazon.settlement_to_disbursement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_SIDE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    side_role: expected
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.expected.USES_COLUMN.column.zs_observe.amazon_settlement.order_id.column_role_key
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases:
  - side_uses_key_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    column_role: key
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.expected.USES_COLUMN.column.zs_observe.amazon_settlement.total.column_role_amount
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  source_type: reconciliation_side
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases:
  - side_uses_amount_column
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  edge_properties:
    column_role: amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_side.amazon.settlement_to_disbursement.expected.USES_TABLE.table.zs_observe.amazon_settlement
  edge_type: USES_TABLE
  canonical_edge_type: USES_TABLE
  source_id: reconciliation_side.amazon.settlement_to_disbursement.expected
  source_type: reconciliation_side
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases:
  - side_uses_table
  inverse_edge_type: USED_BY_RECONCILIATION_SIDE
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_variant.amazon.fee_preview_to_actual_fee.component_level.EXTENDS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.fee_preview_to_actual_fee
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
  source_id: reconciliation_variant.amazon.fee_preview_to_actual_fee.component_level
  source_type: reconciliation_variant
  target_id: reconciliation_profile.amazon.fee_preview_to_actual_fee
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_VARIANT
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.reconciliation_profile.amazon.fee_preview_to_actual_fee.has_variant.component_level
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_variant.amazon.oms_to_settlement.india_vs_international.EXTENDS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.oms_to_settlement
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
  source_id: reconciliation_variant.amazon.oms_to_settlement.india_vs_international
  source_type: reconciliation_variant
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_VARIANT
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.oms_settlement.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.oms_to_settlement.has_variant.india_vs_international
```
```yaml
candidate_edge:
  edge_id: edge.amazon.reconciliation_variant.amazon.returns_to_settlement.india_oms_reverse_vs_international_returns.EXTENDS_RECONCILIATION_PROFILE.reconciliation_profile.amazon.returns_to_settlement
  edge_type: EXTENDS_RECONCILIATION_PROFILE
  canonical_edge_type: EXTENDS_RECONCILIATION_PROFILE
  source_id: reconciliation_variant.amazon.returns_to_settlement.india_oms_reverse_vs_international_returns
  source_type: reconciliation_variant
  target_id: reconciliation_profile.amazon.returns_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: HAS_RECONCILIATION_VARIANT
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon_returns.purpose.001
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.reconciliation_profile.amazon.returns_to_settlement.has_variant.india_oms_reverse_vs_international_returns
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_disbursment.sku.SOURCE_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.fee_preview_to_disbursment.sku
  source_type: relationship
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.fee_preview_to_disbursment.sku.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_disbursment.sku.TARGET_TABLE.table.zs_observe.amazon_disbursment
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.fee_preview_to_disbursment.sku
  source_type: relationship
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.fee_preview_to_disbursment.sku.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_disbursment.sku.USES_SOURCE_COLUMN.column.zs_observe.amazon_fee_preview.sku
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.fee_preview_to_disbursment.sku
  source_type: relationship
  target_id: column.zs_observe.amazon_fee_preview.sku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_disbursment.sku.USES_TARGET_COLUMN.column.zs_observe.amazon_disbursment.sku_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.fee_preview_to_disbursment.sku
  source_type: relationship
  target_id: column.zs_observe.amazon_disbursment.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_oms.sku.SOURCE_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.fee_preview_to_oms.sku
  source_type: relationship
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.fee_preview_to_oms.sku.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_oms.sku.TARGET_TABLE.table.zs_observe.amazon_oms
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.fee_preview_to_oms.sku
  source_type: relationship
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.fee_preview_to_oms.sku.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_oms.sku.USES_SOURCE_COLUMN.column.zs_observe.amazon_fee_preview.sku
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.fee_preview_to_oms.sku
  source_type: relationship
  target_id: column.zs_observe.amazon_fee_preview.sku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.fee_preview_to_oms.sku.USES_TARGET_COLUMN.column.zs_observe.amazon_oms.sku_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.fee_preview_to_oms.sku
  source_type: relationship
  target_id: column.zs_observe.amazon_oms.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_disbursment.order_id.SOURCE_TABLE.table.zs_observe.amazon_oms
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.oms_to_disbursment.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
  source_old_edge_id: edge.oms_to_disbursment.order_id.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_disbursment.order_id.TARGET_TABLE.table.zs_observe.amazon_disbursment
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.oms_to_disbursment.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
  source_old_edge_id: edge.oms_to_disbursment.order_id.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_disbursment.order_id.USES_SOURCE_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.oms_to_disbursment.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_disbursment.order_id.USES_TARGET_COLUMN.column.zs_observe.amazon_disbursment.order_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.oms_to_disbursment.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_disbursment.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_settlement.order_id.SOURCE_TABLE.table.zs_observe.amazon_oms
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.oms_to_settlement.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.oms_to_settlement.order_id.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_settlement.order_id.TARGET_TABLE.table.zs_observe.amazon_settlement
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.oms_to_settlement.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
  source_old_edge_id: edge.oms_to_settlement.order_id.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_settlement.order_id.USES_SOURCE_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.oms_to_settlement.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.oms_to_settlement.order_id.USES_TARGET_COLUMN.column.zs_observe.amazon_settlement.order_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.oms_to_settlement.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_oms.order_id.SOURCE_TABLE.table.zs_observe.amazon_returns
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.returns_to_oms.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.returns_to_oms.order_id.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_oms.order_id.TARGET_TABLE.table.zs_observe.amazon_oms
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.returns_to_oms.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.returns_to_oms.order_id.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_oms.order_id.USES_SOURCE_COLUMN.column.zs_observe.amazon_returns.order_id
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.returns_to_oms.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_returns.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_oms.order_id.USES_TARGET_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.returns_to_oms.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_settlement.order_id.SOURCE_TABLE.table.zs_observe.amazon_returns
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.returns_to_settlement.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.returns_to_settlement.order_id.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_settlement.order_id.TARGET_TABLE.table.zs_observe.amazon_settlement
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.returns_to_settlement.order_id
  source_type: relationship
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.returns_to_settlement.order_id.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_settlement.order_id.USES_SOURCE_COLUMN.column.zs_observe.amazon_returns.order_id
  edge_type: USES_SOURCE_COLUMN
  canonical_edge_type: USES_SOURCE_COLUMN
  source_id: relationship.amazon.returns_to_settlement.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_returns.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.returns_to_settlement.order_id.USES_TARGET_COLUMN.column.zs_observe.amazon_settlement.order_id
  edge_type: USES_TARGET_COLUMN
  canonical_edge_type: USES_TARGET_COLUMN
  source_id: relationship.amazon.returns_to_settlement.order_id
  source_type: relationship
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_COLUMN_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.settlement_to_disbursment.order_id_settlement_id.SOURCE_TABLE.table.zs_observe.amazon_settlement
  edge_type: SOURCE_TABLE
  canonical_edge_type: SOURCE_TABLE
  source_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  source_type: relationship
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: SOURCE_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.settlement_to_disbursment.order_id_settlement_id.from
```
```yaml
candidate_edge:
  edge_id: edge.amazon.relationship.amazon.settlement_to_disbursment.order_id_settlement_id.TARGET_TABLE.table.zs_observe.amazon_disbursment
  edge_type: TARGET_TABLE
  canonical_edge_type: TARGET_TABLE
  source_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  source_type: relationship
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGET_OF_RELATIONSHIP
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.settlement_to_disbursment.order_id_settlement_id.to
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_aggregate_before_fee_preview_join.TARGETS_CARD.relationship.amazon.fee_preview_to_disbursment.sku
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_aggregate_before_fee_preview_join
  source_type: rule
  target_id: relationship.amazon.fee_preview_to_disbursment.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_disbursment_fee_context.TARGETS_CARD.table.zs_observe.amazon_disbursment
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_disbursment_fee_context
  source_type: rule
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_disbursment_spelling.TARGETS_CARD.table.zs_observe.amazon_disbursment
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_disbursment_spelling
  source_type: rule
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_fee_preview_filters.HAS_VALIDATION_TEST.validation_test.amazon.fee_preview_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_fee_preview_filters
  source_type: rule
  target_id: validation_test.amazon.fee_preview_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_fee_preview_filters.TARGETS_CARD.table.zs_observe.amazon_fee_preview
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_fee_preview_filters
  source_type: rule
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_forward_revenue_filter.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_forward_revenue_filter
  source_type: rule
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_forward_revenue_filter.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_forward_revenue_filter
  source_type: rule
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_forward_revenue_filter.TARGETS_CARD.table.zs_observe.amazon_oms
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_forward_revenue_filter
  source_type: rule
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_net_revenue_netting.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_net_revenue_netting
  source_type: rule
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_net_revenue_netting.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_net_revenue_netting
  source_type: rule
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_net_revenue_netting.TARGETS_CARD.table.zs_observe.amazon_oms
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_net_revenue_netting
  source_type: rule
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.kpi.revenue.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_no_hardcoded_group_level.TARGETS_CARD.column.zs_observe.amazon_settlement.group_level_id
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_no_hardcoded_group_level
  source_type: rule
  target_id: column.zs_observe.amazon_settlement.group_level_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_oms_active_filter.HAS_VALIDATION_TEST.validation_test.amazon.oms_active_record_rate
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_oms_active_filter
  source_type: rule
  target_id: validation_test.amazon.oms_active_record_rate
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_oms_active_filter.HAS_VALIDATION_TEST.validation_test.amazon.oms_date_coverage
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_oms_active_filter
  source_type: rule
  target_id: validation_test.amazon.oms_date_coverage
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_oms_active_filter.TARGETS_CARD.table.zs_observe.amazon_oms
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_oms_active_filter
  source_type: rule
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_refund_commission_positive.TARGETS_CARD.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_refund_commission_positive
  source_type: rule
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_settlement_null_type.TARGETS_CARD.column.zs_observe.amazon_settlement.type
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_settlement_null_type
  source_type: rule
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_tax_denominator.HAS_VALIDATION_TEST.validation_test.amazon.effective_tax_denominator
  edge_type: HAS_VALIDATION_TEST
  canonical_edge_type: HAS_VALIDATION_TEST
  source_id: rule.amazon.amazon_tax_denominator
  source_type: rule
  target_id: validation_test.amazon.effective_tax_denominator
  target_type: validation_test
  legacy_edge_aliases: []
  inverse_edge_type: ENFORCES_RULE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_tax_denominator.TARGETS_CARD.metric.marketplace.effective_tax_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_tax_denominator
  source_type: rule
  target_id: metric.marketplace.effective_tax_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.rule.amazon.amazon_tax_filing_out_of_scope.TARGETS_CARD.domain.marketplace.amazon.tax_deductions
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: rule.amazon.amazon_tax_filing_out_of_scope
  source_type: rule
  target_id: domain.marketplace.amazon.tax_deductions
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.disbursment_order_fee_to_refund_fee.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: state_transition.amazon.disbursment_order_fee_to_refund_fee
  source_type: state_transition
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - transition_in_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.disbursment_order_fee_to_refund_fee.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: state_transition.amazon.disbursment_order_fee_to_refund_fee
  source_type: state_transition
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.fee_charge_to_fulfillment_fee_refund.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: state_transition.amazon.fee_charge_to_fulfillment_fee_refund
  source_type: state_transition
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - transition_in_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.fee_charge_to_fulfillment_fee_refund.USES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: state_transition.amazon.fee_charge_to_fulfillment_fee_refund
  source_type: state_transition
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.oms_forward_to_reverse.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: state_transition.amazon.oms_forward_to_reverse
  source_type: state_transition
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - transition_in_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.oms_forward_to_reverse.USES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: state_transition.amazon.oms_forward_to_reverse
  source_type: state_transition
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.settlement_order_to_refund.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: state_transition.amazon.settlement_order_to_refund
  source_type: state_transition
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - transition_in_process
  inverse_edge_type: HAS_STATE_TRANSITION
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.state_transition.amazon.settlement_order_to_refund.USES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: USES_COLUMN
  canonical_edge_type: USES_COLUMN
  source_id: state_transition.amazon.settlement_order_to_refund
  source_type: state_transition
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: USED_BY_CARD
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.BELONGS_TO_DOMAIN.domain.marketplace.amazon.disbursement
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: domain.marketplace.amazon.disbursement
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.charged_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.charged_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.amazon_disbursment.has_column.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.amazon_disbursment.has_column.charged_amount_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.currency_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.currency_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.currency_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.group_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.group_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no group card.
  source_old_edge_id: edge.amazon_disbursment.has_column.group_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.group_level_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.group_level_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no account-binding card.
  source_old_edge_id: edge.amazon_disbursment.has_column.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.is_active
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.is_active
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.quality.001
  notes: Mandatory filter.
  source_old_edge_id: edge.amazon_disbursment.has_column.is_active
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.item_fee_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.item_fee_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.item_fee_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.item_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.item_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.item_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.amazon_disbursment.has_column.mp_fee_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.order_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.order_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.order_level_total
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.order_level_total
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.order_level_total
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.posted_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.posted_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.posted_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.promotion_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.promotion_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.promotion_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.settlement_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.settlement_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.settlement_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.settlement_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.settlement_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  - ev.amazon.recon.settlement_disbursement.001
  source_old_edge_id: edge.amazon_disbursment.has_column.settlement_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.sku
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.sku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.sku
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.sku_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.amazon_disbursment.has_column.sku_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
  notes: Always specify in fee computations.
  source_old_edge_id: edge.amazon_disbursment.has_column.transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_RELATIONSHIP.relationship.amazon.fee_preview_to_disbursment.sku
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: relationship.amazon.fee_preview_to_disbursment.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_RELATIONSHIP.relationship.amazon.oms_to_disbursment.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: relationship.amazon.oms_to_disbursment.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_RELATIONSHIP.relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: value_profile.zs_observe.amazon_disbursment.charged_amount_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: value_profile.zs_observe.amazon_disbursment.mp_fee_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_disbursment.transaction_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: value_profile.zs_observe.amazon_disbursment.transaction_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.SOURCED_FROM_PLATFORM.platform.amazon
  edge_type: SOURCED_FROM_PLATFORM
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_disbursment.SOURCED_FROM_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_id: table.zs_observe.amazon_disbursment
  source_type: table
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.purpose.001
  - ev.amazon_disbursment.quality.001
  - ev.amazon_disbursment.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.BELONGS_TO_DOMAIN.domain.marketplace.amazon.fee_preview
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: domain.marketplace.amazon.fee_preview
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.amazon_store
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.amazon_store
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.amazon_store
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.asin
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.asin
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.asin
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.brand
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.brand
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.brand
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.charged_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.charged_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.description
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.description
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.description
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.estimated_fee_total
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.estimated_fee_total
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon_fee_preview.quality.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.estimated_fee_total
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.final_weight
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.final_weight
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.final_weight
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.fixed_fee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.fixed_fee
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.fixed_fee
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.fnsku
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.fnsku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.fnsku
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.fulfilled_by
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.fulfilled_by
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.fulfilled_by
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.gross_commission
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.gross_commission
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.gross_commission
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.gross_weight
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.gross_weight
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.gross_weight
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.hsn
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.hsn
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  notes: Column only; no statutory tax card.
  source_old_edge_id: edge.amazon_fee_preview.has_column.hsn
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.is_active
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.is_active
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
  notes: Mandatory filter.
  source_old_edge_id: edge.amazon_fee_preview.has_column.is_active
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.is_duplicated
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.is_duplicated
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.is_duplicated
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.longest_side
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.longest_side
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.longest_side
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.median_side
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.median_side
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.median_side
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.pick_and_pack_fee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.pick_and_pack_fee
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.pick_and_pack_fee
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.product_group
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.product_group
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.product_group
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.product_name
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.product_name
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.product_name
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.referal_fee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.referal_fee
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon_fee_preview.quality.001
  notes: DOCX warns this is a percentage (0.19 = 19%), not rupee amount.
  source_old_edge_id: edge.amazon_fee_preview.has_column.referal_fee
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.referral_fee
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.referral_fee
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon_fee_preview.quality.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.referral_fee
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.shipping_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.shipping_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.packaging_weight.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.shipping_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.shortest_side
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.shortest_side
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.shortest_side
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.sku
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.sku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon_fee_preview.recon.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.sku
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.volumetric_weight
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.volumetric_weight
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.weights.001
  source_old_edge_id: edge.amazon_fee_preview.has_column.volumetric_weight
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_COLUMN.column.zs_observe.amazon_fee_preview.zen_status
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: column.zs_observe.amazon_fee_preview.zen_status
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
  notes: Mandatory/recommended filter per DOCX.
  source_old_edge_id: edge.amazon_fee_preview.has_column.zen_status
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_RELATIONSHIP.relationship.amazon.fee_preview_to_disbursment.sku
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: relationship.amazon.fee_preview_to_disbursment.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_RELATIONSHIP.relationship.amazon.fee_preview_to_oms.sku
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: relationship.amazon.fee_preview_to_oms.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_fee_preview.amazon_store
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: value_profile.zs_observe.amazon_fee_preview.amazon_store
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.SOURCED_FROM_PLATFORM.platform.amazon
  edge_type: SOURCED_FROM_PLATFORM
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_fee_preview.SOURCED_FROM_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_id: table.zs_observe.amazon_fee_preview
  source_type: table
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.purpose.001
  - ev.amazon_fee_preview.quality.001
  - ev.amazon_fee_preview.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.BELONGS_TO_DOMAIN.domain.marketplace.amazon.orders
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: domain.marketplace.amazon.orders
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.asin
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.asin
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.asin
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.charged_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.charged_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.amazon_oms.has_column.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.charged_amount_excluding_tax
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.charged_amount_excluding_tax
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.amazon_oms.has_column.charged_amount_excluding_tax
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.created_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.created_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.created_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.currency_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.currency_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.currency_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.destination_gst_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.destination_gst_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_oms.columns.001
  notes: Column only; not tenant/customer card.
  source_old_edge_id: edge.amazon_oms.has_column.destination_gst_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.destination_state
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.destination_state
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon.analytical_patterns.001
  source_old_edge_id: edge.amazon_oms.has_column.destination_state
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.fulfilment_channel
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.fulfilment_channel
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.fulfilment_channel
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.fulfilment_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.fulfilment_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.amazon_oms.has_column.fulfilment_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.gross_commission
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.gross_commission
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon_oms.pitfalls.001
  notes: Estimate, not exact actual fee.
  source_old_edge_id: edge.amazon_oms.has_column.gross_commission
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.group_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.group_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no group card.
  source_old_edge_id: edge.amazon_oms.has_column.group_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.group_level_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.group_level_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no account-binding card.
  source_old_edge_id: edge.amazon_oms.has_column.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.invoice_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.invoice_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.invoice_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.invoice_number
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.invoice_number
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.invoice_number
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.is_active
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.is_active
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
  notes: Mandatory filter.
  source_old_edge_id: edge.amazon_oms.has_column.is_active
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.is_duplicated
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.is_duplicated
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
  notes: Recommended optional exclusion.
  source_old_edge_id: edge.amazon_oms.has_column.is_duplicated
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.item_amount_excluding_tax
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.item_amount_excluding_tax
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.item_amount_excluding_tax
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.item_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.item_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.item_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.item_promo_discount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.item_promo_discount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon_oms.kpis.001
  source_old_edge_id: edge.amazon_oms.has_column.item_promo_discount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.metadata
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.metadata
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  - ev.amazon_oms.transaction_types.001
  source_old_edge_id: edge.amazon_oms.has_column.metadata
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.mrp
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.mrp
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.mrp
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.order_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.order_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.order_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.order_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.amazon_oms.has_column.order_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.order_shipped_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.order_shipped_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.order_shipped_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.principal_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.principal_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.principal_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.settled_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.settled_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.settled_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.settlement_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.settlement_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.settlement_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.shipping_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.shipping_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.shipping_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.shipping_promo_discount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.shipping_promo_discount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.shipping_promo_discount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.sku_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.amazon_oms.has_column.sku_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.source_gst_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.source_gst_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  notes: Column only; not tax compliance card.
  source_old_edge_id: edge.amazon_oms.has_column.source_gst_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.source_state
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.source_state
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  - ev.amazon_oms.columns.001
  source_old_edge_id: edge.amazon_oms.has_column.source_state
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.tax_cgst_rate
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.tax_cgst_rate
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  source_old_edge_id: edge.amazon_oms.has_column.tax_cgst_rate
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.tax_igst_rate
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.tax_igst_rate
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  source_old_edge_id: edge.amazon_oms.has_column.tax_igst_rate
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.tax_ugst_rate
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.tax_ugst_rate
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
  source_old_edge_id: edge.amazon_oms.has_column.tax_ugst_rate
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.total_tax
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.total_tax
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.gst.001
  source_old_edge_id: edge.amazon_oms.has_column.total_tax
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.total_tcs_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.total_tcs_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column; not statutory filing card.
  source_old_edge_id: edge.amazon_oms.has_column.total_tcs_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.total_tds
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.total_tds
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column; not statutory filing card.
  source_old_edge_id: edge.amazon_oms.has_column.total_tds
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
  notes: Always filter explicitly.
  source_old_edge_id: edge.amazon_oms.has_column.transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.zen_status
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.zen_status
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.quality.001
  notes: Recommended optional filter.
  source_old_edge_id: edge.amazon_oms.has_column.zen_status
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.zone
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.zone
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.amazon_oms.has_column.zone
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_COLUMN.column.zs_observe.amazon_oms.zone_new
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: column.zs_observe.amazon_oms.zone_new
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.amazon_oms.has_column.zone_new
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_RELATIONSHIP.relationship.amazon.fee_preview_to_oms.sku
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: relationship.amazon.fee_preview_to_oms.sku
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.columns.001
  - ev.amazon.join_patterns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_RELATIONSHIP.relationship.amazon.oms_to_disbursment.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: relationship.amazon.oms_to_disbursment.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon_disbursment.purpose.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_RELATIONSHIP.relationship.amazon.oms_to_settlement.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: relationship.amazon.oms_to_settlement.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_RELATIONSHIP.relationship.amazon.returns_to_oms.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: relationship.amazon.returns_to_oms.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.fulfilment_channel
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: value_profile.zs_observe.amazon_oms.fulfilment_channel
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.fulfilment_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: value_profile.zs_observe.amazon_oms.fulfilment_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.metadata
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: value_profile.zs_observe.amazon_oms.metadata
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.transaction_type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: value_profile.zs_observe.amazon_oms.transaction_type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_oms.zone
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: value_profile.zs_observe.amazon_oms.zone
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.SOURCED_FROM_PLATFORM.platform.amazon
  edge_type: SOURCED_FROM_PLATFORM
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_oms.SOURCED_FROM_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_id: table.zs_observe.amazon_oms
  source_type: table
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.purpose.001
  - ev.amazon_oms.quality.001
  - ev.amazon_oms.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.BELONGS_TO_DOMAIN.domain.marketplace.amazon.returns
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: domain.marketplace.amazon.returns
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.brand
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.brand
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.brand
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.charged_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.charged_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.charged_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.charged_amount_excluding_tax
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.charged_amount_excluding_tax
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.charged_amount_excluding_tax
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.created_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.created_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.created_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.currency_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.currency_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.currency_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.customer_comments
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.customer_comments
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.customer_comments
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.fulfilment_channel
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.fulfilment_channel
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.fulfilment_channel
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.group_level_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.group_level_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no account-binding card.
  source_old_edge_id: edge.amazon_returns.has_column.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.internal_transaction_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.internal_transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.internal_transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.is_active
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.is_active
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
  notes: No active records until re-ingested.
  source_old_edge_id: edge.amazon_returns.has_column.is_active
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.is_duplicated
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.is_duplicated
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
  source_old_edge_id: edge.amazon_returns.has_column.is_duplicated
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.order_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.order_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.quantity
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.quantity
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.quantity
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.return_date_str
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.return_date_str
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.return_date_str
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.return_reason
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.return_reason
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.taxonomy.001
  source_old_edge_id: edge.amazon_returns.has_column.return_reason
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.shipping_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.shipping_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.shipping_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.sku_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.sku_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.transaction_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.transaction_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.columns.001
  source_old_edge_id: edge.amazon_returns.has_column.transaction_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_COLUMN.column.zs_observe.amazon_returns.zen_status
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: column.zs_observe.amazon_returns.zen_status
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
  source_old_edge_id: edge.amazon_returns.has_column.zen_status
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_RELATIONSHIP.relationship.amazon.returns_to_oms.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: relationship.amazon.returns_to_oms.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_RELATIONSHIP.relationship.amazon.returns_to_settlement.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: relationship.amazon.returns_to_settlement.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_returns.return_reason
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: value_profile.zs_observe.amazon_returns.return_reason
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.SOURCED_FROM_PLATFORM.platform.amazon
  edge_type: SOURCED_FROM_PLATFORM
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_returns.SOURCED_FROM_PLATFORM_CONTEXT.platform_context.amazon.international
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_id: table.zs_observe.amazon_returns
  source_type: table
  target_id: platform_context.amazon.international
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.quality.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.BELONGS_TO_DOMAIN.domain.marketplace.amazon.settlement
  edge_type: BELONGS_TO_DOMAIN
  canonical_edge_type: BELONGS_TO_DOMAIN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: domain.marketplace.amazon.settlement
  target_type: domain
  legacy_edge_aliases: []
  inverse_edge_type: HAS_METRIC
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.account_type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.account_type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  notes: Column only; no platform_account card.
  source_old_edge_id: edge.amazon_settlement.has_column.account_type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.created_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.created_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.amazon_settlement.has_column.created_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.date_time
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.date_time
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon_settlement.pitfalls.001
  notes: Do not filter on date_time.
  source_old_edge_id: edge.amazon_settlement.has_column.date_time
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.description
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.description
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.kpis.001
  - ev.amazon.analytical_patterns.001
  source_old_edge_id: edge.amazon_settlement.has_column.description
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.destination_state
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.destination_state
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.destination_state
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.fba_fees
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.fba_fees
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.fba_fees
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.fulfillment
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.fulfillment
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.fulfillment
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.gift_wrap_credits
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.gift_wrap_credits
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.gift_wrap_credits
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.gross_commission
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.gross_commission
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.gross_commission
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.group_level_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.group_level_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.quality.001
  - ev.amazon.tenant_scope_mention.001
  notes: Column/caveat only; no account-binding card.
  source_old_edge_id: edge.amazon_settlement.has_column.group_level_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.is_active
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.is_active
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.quality.001
  notes: Mandatory filter.
  source_old_edge_id: edge.amazon_settlement.has_column.is_active
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.is_duplicated
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.is_duplicated
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.quality.001
  source_old_edge_id: edge.amazon_settlement.has_column.is_duplicated
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.marketplace
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.marketplace
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.marketplace
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.marketplace_withheld_tax
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.marketplace_withheld_tax
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  notes: Marketplace column only.
  source_old_edge_id: edge.amazon_settlement.has_column.marketplace_withheld_tax
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.mp_fees
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.mp_fees
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.mp_fees
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.order_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.order_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.join_patterns.001
  source_old_edge_id: edge.amazon_settlement.has_column.order_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.other
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.other
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.other
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.other_transaction_fees
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.other_transaction_fees
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.other_transaction_fees
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.product_sales
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.product_sales
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.product_sales
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.promotional_rebates
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.promotional_rebates
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.promotional_rebates
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.selling_fees
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.selling_fees
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.selling_fees
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.settled_amount
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.settled_amount
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.settled_amount
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.settlement_date
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.settlement_date
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.settlement_date
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.settlement_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.settlement_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.settlement_cycle.001
  source_old_edge_id: edge.amazon_settlement.has_column.settlement_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.shipping_credits
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.shipping_credits
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.shipping_credits
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.sku
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.sku
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.sku
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.sku_id
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.sku_id
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.amazon_settlement.has_column.sku_id
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.tcs_cgst
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.tcs_cgst
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column only.
  source_old_edge_id: edge.amazon_settlement.has_column.tcs_cgst
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.tcs_igst
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.tcs_igst
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column only.
  source_old_edge_id: edge.amazon_settlement.has_column.tcs_igst
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.tcs_sgst
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.tcs_sgst
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column only.
  source_old_edge_id: edge.amazon_settlement.has_column.tcs_sgst
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.tds
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.tds
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon.gst.001
  notes: Marketplace deduction column only.
  source_old_edge_id: edge.amazon_settlement.has_column.tds
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.total
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.total
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon_settlement.kpis.001
  source_old_edge_id: edge.amazon_settlement.has_column.total
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  - ev.amazon_settlement.quality.001
  notes: NULL values carry financial data.
  source_old_edge_id: edge.amazon_settlement.has_column.type
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_COLUMN.column.zs_observe.amazon_settlement.zen_status
  edge_type: HAS_COLUMN
  canonical_edge_type: HAS_COLUMN
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: column.zs_observe.amazon_settlement.zen_status
  target_type: column
  legacy_edge_aliases: []
  inverse_edge_type: BELONGS_TO_TABLE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.quality.001
  notes: Recommended optional filter.
  source_old_edge_id: edge.amazon_settlement.has_column.zen_status
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_RELATIONSHIP.relationship.amazon.oms_to_settlement.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: relationship.amazon.oms_to_settlement.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.join_patterns.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_RELATIONSHIP.relationship.amazon.returns_to_settlement.order_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: relationship.amazon.returns_to_settlement.order_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.purpose.001
  - ev.amazon_returns.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_RELATIONSHIP.relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  edge_type: HAS_RELATIONSHIP
  canonical_edge_type: HAS_RELATIONSHIP
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: relationship.amazon.settlement_to_disbursment.order_id_settlement_id
  target_type: relationship
  legacy_edge_aliases: []
  inverse_edge_type: RELATIONSHIP_OF_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.settlement_disbursement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.HAS_VALUE_PROFILE.value_profile.zs_observe.amazon_settlement.type
  edge_type: HAS_VALUE_PROFILE
  canonical_edge_type: HAS_VALUE_PROFILE
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: value_profile.zs_observe.amazon_settlement.type
  target_type: value_profile
  legacy_edge_aliases: []
  inverse_edge_type: PROFILES_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.SOURCED_FROM_PLATFORM.platform.amazon
  edge_type: SOURCED_FROM_PLATFORM
  canonical_edge_type: SOURCED_FROM_PLATFORM
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: platform.amazon
  target_type: platform
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.table.zs_observe.amazon_settlement.SOURCED_FROM_PLATFORM_CONTEXT.platform_context.amazon.in
  edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  canonical_edge_type: SOURCED_FROM_PLATFORM_CONTEXT
  source_id: table.zs_observe.amazon_settlement
  source_type: table
  target_id: platform_context.amazon.in
  target_type: platform_context
  legacy_edge_aliases: []
  inverse_edge_type: HAS_SOURCE_TABLE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.purpose.001
  - ev.amazon_settlement.quality.001
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.effective_tax_denominator.ENFORCES_RULE.rule.amazon.amazon_tax_denominator
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.effective_tax_denominator
  source_type: validation_test
  target_id: rule.amazon.amazon_tax_denominator
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.effective_tax_denominator.TARGETS_CARD.metric.marketplace.effective_tax_rate
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.effective_tax_denominator
  source_type: validation_test
  target_id: metric.marketplace.effective_tax_rate
  target_type: metric
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.gst.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.fee_preview_coverage.ENFORCES_RULE.rule.amazon.amazon_fee_preview_filters
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.fee_preview_coverage
  source_type: validation_test
  target_id: rule.amazon.amazon_fee_preview_filters
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.fee_preview_coverage.TARGETS_CARD.table.zs_observe.amazon_fee_preview
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.fee_preview_coverage
  source_type: validation_test
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_active_record_rate.ENFORCES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_active_record_rate
  source_type: validation_test
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_active_record_rate.ENFORCES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_active_record_rate
  source_type: validation_test
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_active_record_rate.ENFORCES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_active_record_rate
  source_type: validation_test
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_active_record_rate.TARGETS_CARD.table.zs_observe.amazon_oms
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.oms_active_record_rate
  source_type: validation_test
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_date_coverage.ENFORCES_RULE.rule.amazon.amazon_forward_revenue_filter
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_date_coverage
  source_type: validation_test
  target_id: rule.amazon.amazon_forward_revenue_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_date_coverage.ENFORCES_RULE.rule.amazon.amazon_net_revenue_netting
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_date_coverage
  source_type: validation_test
  target_id: rule.amazon.amazon_net_revenue_netting
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_date_coverage.ENFORCES_RULE.rule.amazon.amazon_oms_active_filter
  edge_type: ENFORCES_RULE
  canonical_edge_type: ENFORCES_RULE
  source_id: validation_test.amazon.oms_date_coverage
  source_type: validation_test
  target_id: rule.amazon.amazon_oms_active_filter
  target_type: rule
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALIDATION_TEST
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_date_coverage.TARGETS_CARD.table.zs_observe.amazon_oms
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.oms_date_coverage
  source_type: validation_test
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.oms_settlement_order_count.TARGETS_CARD.reconciliation_profile.amazon.oms_to_settlement
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.oms_settlement_order_count
  source_type: validation_test
  target_id: reconciliation_profile.amazon.oms_to_settlement
  target_type: reconciliation_profile
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon.data_integrity.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.returns_source_active.TARGETS_CARD.table.zs_observe.amazon_returns
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.returns_source_active
  source_type: validation_test
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_returns.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.validation_test.amazon.settlement_total_formula.TARGETS_CARD.table.zs_observe.amazon_settlement
  edge_type: TARGETS_CARD
  canonical_edge_type: TARGETS_CARD
  source_id: validation_test.amazon.settlement_total_formula
  source_type: validation_test
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: TARGETED_BY_QUERY_PATTERN
  materialize_inverse: false
  edge_class: parser_helper
  canonical_cognee_edge: false
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.charged_amount_type.PROFILES_COLUMN.column.zs_observe.amazon_disbursment.charged_amount_type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_disbursment.charged_amount_type
  source_type: value_profile
  target_id: column.zs_observe.amazon_disbursment.charged_amount_type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_disbursment.charged_amount_type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.charged_amount_type.PROFILES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_disbursment.charged_amount_type
  source_type: value_profile
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.mp_fee_type.PROFILES_COLUMN.column.zs_observe.amazon_disbursment.mp_fee_type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_disbursment.mp_fee_type
  source_type: value_profile
  target_id: column.zs_observe.amazon_disbursment.mp_fee_type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_disbursment.mp_fee_type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.mp_fee_type.PROFILES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_disbursment.mp_fee_type
  source_type: value_profile
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.transaction_type.PROFILES_COLUMN.column.zs_observe.amazon_disbursment.transaction_type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_disbursment.transaction_type
  source_type: value_profile
  target_id: column.zs_observe.amazon_disbursment.transaction_type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_disbursment.transaction_type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_disbursment.transaction_type.PROFILES_TABLE.table.zs_observe.amazon_disbursment
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_disbursment.transaction_type
  source_type: value_profile
  target_id: table.zs_observe.amazon_disbursment
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_fee_preview.amazon_store.PROFILES_COLUMN.column.zs_observe.amazon_fee_preview.amazon_store
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_fee_preview.amazon_store
  source_type: value_profile
  target_id: column.zs_observe.amazon_fee_preview.amazon_store
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_fee_preview.amazon_store.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_fee_preview.amazon_store.PROFILES_TABLE.table.zs_observe.amazon_fee_preview
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_fee_preview.amazon_store
  source_type: value_profile
  target_id: table.zs_observe.amazon_fee_preview
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_fee_preview.quality.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.fulfilment_channel.PROFILES_COLUMN.column.zs_observe.amazon_oms.fulfilment_channel
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_oms.fulfilment_channel
  source_type: value_profile
  target_id: column.zs_observe.amazon_oms.fulfilment_channel
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_oms.fulfilment_channel.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.fulfilment_channel.PROFILES_TABLE.table.zs_observe.amazon_oms
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_oms.fulfilment_channel
  source_type: value_profile
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.fulfilment_type.PROFILES_COLUMN.column.zs_observe.amazon_oms.fulfilment_type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_oms.fulfilment_type
  source_type: value_profile
  target_id: column.zs_observe.amazon_oms.fulfilment_type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_oms.fulfilment_type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.fulfilment_type.PROFILES_TABLE.table.zs_observe.amazon_oms
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_oms.fulfilment_type
  source_type: value_profile
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.metadata.PROFILES_COLUMN.column.zs_observe.amazon_oms.metadata
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_oms.metadata
  source_type: value_profile
  target_id: column.zs_observe.amazon_oms.metadata
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_oms.metadata.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.metadata.PROFILES_TABLE.table.zs_observe.amazon_oms
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_oms.metadata
  source_type: value_profile
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.transaction_type.PROFILES_COLUMN.column.zs_observe.amazon_oms.transaction_type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_oms.transaction_type
  source_type: value_profile
  target_id: column.zs_observe.amazon_oms.transaction_type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_oms.transaction_type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.transaction_type.PROFILES_TABLE.table.zs_observe.amazon_oms
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_oms.transaction_type
  source_type: value_profile
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_oms.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.zone.PROFILES_COLUMN.column.zs_observe.amazon_oms.zone
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_oms.zone
  source_type: value_profile
  target_id: column.zs_observe.amazon_oms.zone
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_oms.zone.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_oms.zone.PROFILES_TABLE.table.zs_observe.amazon_oms
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_oms.zone
  source_type: value_profile
  target_id: table.zs_observe.amazon_oms
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.segmentation.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_returns.return_reason.PROFILES_COLUMN.column.zs_observe.amazon_returns.return_reason
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_returns.return_reason
  source_type: value_profile
  target_id: column.zs_observe.amazon_returns.return_reason
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.taxonomy.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_returns.return_reason.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_returns.return_reason.PROFILES_TABLE.table.zs_observe.amazon_returns
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_returns.return_reason
  source_type: value_profile
  target_id: table.zs_observe.amazon_returns
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_returns.taxonomy.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_settlement.type.PROFILES_COLUMN.column.zs_observe.amazon_settlement.type
  edge_type: PROFILES_COLUMN
  canonical_edge_type: PROFILES_COLUMN
  source_id: value_profile.zs_observe.amazon_settlement.type
  source_type: value_profile
  target_id: column.zs_observe.amazon_settlement.type
  target_type: column
  legacy_edge_aliases:
  - value_profile_describes_column
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
  source_old_edge_id: edge.value_profile.zs_observe.amazon_settlement.type.profiles_column
```
```yaml
candidate_edge:
  edge_id: edge.amazon.value_profile.zs_observe.amazon_settlement.type.PROFILES_TABLE.table.zs_observe.amazon_settlement
  edge_type: PROFILES_TABLE
  canonical_edge_type: PROFILES_TABLE
  source_id: value_profile.zs_observe.amazon_settlement.type
  source_type: value_profile
  target_id: table.zs_observe.amazon_settlement
  target_type: table
  legacy_edge_aliases: []
  inverse_edge_type: HAS_VALUE_PROFILE
  materialize_inverse: false
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon_settlement.columns.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.expected_vs_actual_fee_validation.actual_fee_aggregated.BELONGS_TO_PROCESS.business_process.amazon.expected_vs_actual_fee_validation
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.expected_vs_actual_fee_validation.actual_fee_aggregated
  source_type: workflow_step
  target_id: business_process.amazon.expected_vs_actual_fee_validation
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.expected_vs_actual_fee_validation.expected_fee_loaded.BELONGS_TO_PROCESS.business_process.amazon.expected_vs_actual_fee_validation
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.expected_vs_actual_fee_validation.expected_fee_loaded
  source_type: workflow_step
  target_id: business_process.amazon.expected_vs_actual_fee_validation
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.expected_vs_actual_fee_validation.root_cause_reviewed.BELONGS_TO_PROCESS.business_process.amazon.expected_vs_actual_fee_validation
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.expected_vs_actual_fee_validation.root_cause_reviewed
  source_type: workflow_step
  target_id: business_process.amazon.expected_vs_actual_fee_validation
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.expected_vs_actual_fee_validation.variance_computed.BELONGS_TO_PROCESS.business_process.amazon.expected_vs_actual_fee_validation
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.expected_vs_actual_fee_validation.variance_computed
  source_type: workflow_step
  target_id: business_process.amazon.expected_vs_actual_fee_validation
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.recon.fee_preview_actual.001
  - ev.amazon_fee_preview.recon.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.order_to_settlement.marketplace_deductions_applied.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.order_to_settlement.marketplace_deductions_applied
  source_type: workflow_step
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.order_to_settlement.net_settlement_posted.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.order_to_settlement.net_settlement_posted
  source_type: workflow_step
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.order_to_settlement.order_recorded.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.order_to_settlement.order_recorded
  source_type: workflow_step
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.order_to_settlement.settlement_period_netted.BELONGS_TO_PROCESS.business_process.amazon.order_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.order_to_settlement.settlement_period_netted
  source_type: workflow_step
  target_id: business_process.amazon.order_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.financial_stack.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon.recon.oms_settlement.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.return_to_settlement.fee_recovery_assessed.BELONGS_TO_PROCESS.business_process.amazon.return_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.return_to_settlement.fee_recovery_assessed
  source_type: workflow_step
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.return_to_settlement.non_recovered_fees_recorded.BELONGS_TO_PROCESS.business_process.amazon.return_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.return_to_settlement.non_recovered_fees_recorded
  source_type: workflow_step
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.return_to_settlement.refund_debited.BELONGS_TO_PROCESS.business_process.amazon.return_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.return_to_settlement.refund_debited
  source_type: workflow_step
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.return_to_settlement.return_recorded.BELONGS_TO_PROCESS.business_process.amazon.return_to_settlement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.return_to_settlement.return_recorded
  source_type: workflow_step
  target_id: business_process.amazon.return_to_settlement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.return_analysis.001
  - ev.amazon.settlement_cycle.001
  - ev.amazon_disbursment.transaction_types.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.safe_t_reimbursement.claim_or_reimbursement_detected.BELONGS_TO_PROCESS.business_process.amazon.safe_t_reimbursement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.safe_t_reimbursement.claim_or_reimbursement_detected
  source_type: workflow_step
  target_id: business_process.amazon.safe_t_reimbursement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.safe_t_reimbursement.eligible_return_identified.BELONGS_TO_PROCESS.business_process.amazon.safe_t_reimbursement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.safe_t_reimbursement.eligible_return_identified
  source_type: workflow_step
  target_id: business_process.amazon.safe_t_reimbursement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
```
```yaml
candidate_edge:
  edge_id: edge.amazon.workflow_step.amazon.safe_t_reimbursement.recovery_amount_recorded.BELONGS_TO_PROCESS.business_process.amazon.safe_t_reimbursement
  edge_type: BELONGS_TO_PROCESS
  canonical_edge_type: BELONGS_TO_PROCESS
  source_id: workflow_step.amazon.safe_t_reimbursement.recovery_amount_recorded
  source_type: workflow_step
  target_id: business_process.amazon.safe_t_reimbursement
  target_type: business_process
  legacy_edge_aliases:
  - step_in_process
  inverse_edge_type: HAS_WORKFLOW_STEP
  materialize_inverse: true
  edge_class: canonical
  canonical_cognee_edge: true
  confidence: high
  evidence_refs:
  - ev.amazon.safet.001
  - ev.amazon.return_analysis.001
```

## 7. SQL Pattern Registry

```yaml
sql_pattern:
  sql_ref: sql.amazon.oms.gross_revenue
  description: Gross revenue
  sql_template: SELECT SUM(charged_amount) FROM zs_observe.amazon_oms WHERE is_active = true AND transaction_type = 'forward';
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.oms.net_revenue
  description: Net revenue
  sql_template: SELECT SUM(charged_amount) FROM zs_observe.amazon_oms WHERE is_active = true AND transaction_type IN ('forward', 'reverse');
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.oms.return_rate_by_sku
  description: Return rate by SKU
  sql_template: SELECT sku_id, COUNT(DISTINCT CASE WHEN transaction_type='forward' THEN order_id END) AS forward_orders, COUNT(DISTINCT CASE WHEN transaction_type='reverse' THEN order_id
    END) AS returns FROM zs_observe.amazon_oms WHERE is_active = true GROUP BY sku_id;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.oms.gst_breakdown
  description: GST breakdown
  sql_template: SELECT CASE WHEN tax_igst_rate > 0 THEN 'Inter-State (IGST)' WHEN tax_cgst_rate > 0 THEN 'Intra-State (CGST+SGST)' WHEN tax_ugst_rate > 0 THEN 'Union Territory' ELSE
    'No Tax / Other' END AS gst_type, SUM(total_tax), SUM(charged_amount_excluding_tax) FROM zs_observe.amazon_oms WHERE is_active = true AND transaction_type = 'forward' GROUP BY 1;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.settlement.realization_rate
  description: Seller realization rate
  sql_template: SELECT settlement_id, SUM(CASE WHEN type = 'Order' THEN product_sales ELSE 0 END) AS gross_sales, SUM(total) AS net_settled, SUM(total) / NULLIF(SUM(CASE WHEN type =
    'Order' THEN product_sales ELSE 0 END), 0) AS realization_rate FROM zs_observe.amazon_settlement WHERE is_active = true GROUP BY settlement_id;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.settlement.advertising_spend
  description: Advertising spend
  sql_template: SELECT DATE_TRUNC('month', created_date) AS month, SUM(total) AS advertising_spend FROM zs_observe.amazon_settlement WHERE is_active = true AND type = 'Service Fee' AND
    description LIKE '%Advertising%' GROUP BY 1;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.settlement.cash_position
  description: Settlement cash position
  sql_template: SELECT settlement_id, SUM(total) AS net_cash_position FROM zs_observe.amazon_settlement WHERE is_active = true GROUP BY settlement_id;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.settlement.tds_tcs_deductions
  description: TDS/TCS deductions
  sql_template: SELECT DATE_TRUNC('month', created_date) AS month, SUM(tds) AS tds_total, SUM(tcs_igst + tcs_cgst + tcs_sgst) AS tcs_total FROM zs_observe.amazon_settlement WHERE is_active
    = true GROUP BY 1;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.disbursement.fee_breakdown_summary
  description: Disbursement fee breakdown
  sql_template: SELECT charged_amount_type, SUM(charged_amount) AS amount FROM zs_observe.amazon_disbursment WHERE is_active = true AND mp_fee_type = 'ItemFees' GROUP BY charged_amount_type;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.disbursement.effective_commission_by_sku
  description: Effective commission by SKU
  sql_template: SELECT sku_id, ABS(SUM(CASE WHEN mp_fee_type='ItemFees' AND charged_amount_type='commission' THEN charged_amount ELSE 0 END)) / NULLIF(SUM(CASE WHEN mp_fee_type='ItemPrice'
    AND charged_amount_type='principal' THEN charged_amount ELSE 0 END),0) AS effective_commission_rate FROM zs_observe.amazon_disbursment WHERE is_active = true GROUP BY sku_id;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.fee_preview.expected_vs_actual
  description: Expected vs actual fee
  sql_template: WITH actual_fees AS (SELECT sku_id, SUM(CASE WHEN mp_fee_type='ItemFees' AND transaction_type='Order' THEN charged_amount ELSE 0 END) AS actual_fee FROM zs_observe.amazon_disbursment
    WHERE is_active = true GROUP BY sku_id) SELECT fp.sku, fp.gross_commission AS expected_fee, a.actual_fee, fp.gross_commission + a.actual_fee AS variance FROM zs_observe.amazon_fee_preview
    fp JOIN actual_fees a ON fp.sku = a.sku_id WHERE fp.is_active = true AND fp.zen_status = true;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.fee_preview.volumetric_gap
  description: Volumetric weight gap
  sql_template: SELECT sku, gross_weight, volumetric_weight, final_weight FROM zs_observe.amazon_fee_preview WHERE is_active = true AND zen_status = true AND volumetric_weight > gross_weight
    * 1.5;
```
```yaml
sql_pattern:
  sql_ref: sql.amazon.returns.volume_by_reason
  description: Return volume by reason
  sql_template: SELECT return_reason, COUNT(*) AS return_count, SUM(charged_amount) AS total_refund FROM zs_observe.amazon_returns WHERE is_active = true GROUP BY return_reason ORDER
    BY return_count DESC;
```

## 8. Review Item Registry

```yaml
review_item:
  review_id: review.amazon.supporting_sku_master.001
  review_type: missing_source_table_detail
  related_card_type: table
  related_canonical_id: table.zs_observe.amazon_sku_master
  issue: DOCX references amazon_sku_master as related table but does not provide a full marketplace table section.
  required_resolution: Do not create table card unless a source DOCX section gives schema, purpose, filters, and columns.
  severity: medium
  evidence_refs: ev.amazon_oms.purpose.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.supporting_shipping_invoice.001
  review_type: missing_source_table_detail
  related_card_type: table
  related_canonical_id: table.zs_observe.amazon_shipping_invoice
  issue: DOCX references amazon_shipping_invoice as related table but does not provide full schema/details.
  required_resolution: Do not create external logistics or shipping-invoice table card from this markdown; add only if marketplace-owned detail is documented separately.
  severity: medium
  evidence_refs: ev.amazon_oms.purpose.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.recon_report.001
  review_type: missing_source_table_detail
  related_card_type: table
  related_canonical_id: table.zs_observe.amazon_recon_report
  issue: DOCX references amazon_recon_report as waterfall/recon report but does not provide full schema.
  required_resolution: Treat as evidence mention only; create table card only with full source details.
  severity: medium
  evidence_refs: ev.amazon.settlement_cycle.001; ev.amazon_settlement.purpose.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.returns.inactive.001
  review_type: inactive_source
  related_card_type: table
  related_canonical_id: table.zs_observe.amazon_returns
  issue: All amazon_returns records are currently inactive due to FILE_DELETED.
  required_resolution: Keep table/column semantics but mark query patterns as prepared for re-ingest; active analytics should use OMS reverse rows for India.
  severity: high
  evidence_refs: ev.amazon_returns.quality.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.recon.tolerance.001
  review_type: missing_tolerance
  related_card_type: matching_logic
  related_canonical_id: matching_logic.amazon.oms_to_settlement.primary
  issue: DOCX does not specify numeric tolerance for amount variance checks.
  required_resolution: Add tolerance policy in a separate reconciliation/rule standard before auto-classifying mismatches by amount.
  severity: medium
  evidence_refs: ev.amazon.recon.oms_settlement.001; ev.amazon.recon.settlement_disbursement.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.scope.group_level.001
  review_type: scope_layer_required
  related_card_type: column
  related_canonical_id: column.zs_observe.amazon_settlement.group_level_id
  issue: DOCX provides group_level_id examples, but marketplace-only standard must not create account-binding cards.
  required_resolution: Provide runtime scope externally through separate tenant/group/account-binding standard.
  severity: high
  evidence_refs: ev.amazon.tenant_scope_mention.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.metric.revenue_per_unit.001
  review_type: missing_column_confirmation
  related_card_type: metric_implementation
  related_canonical_id: metric_implementation.amazon.amazon_oms.revenue_per_unit
  issue: Revenue per Unit formula references quantity, but compact OMS column evidence in available text does not clearly list quantity.
  required_resolution: Confirm quantity column from actual schema before using this implementation operationally.
  severity: medium
  evidence_refs: ev.amazon.kpi.revenue.001
  status: open
```
```yaml
review_item:
  review_id: review.amazon.benchmarks.001
  review_type: benchmark_context
  related_card_type: metric
  related_canonical_id: metric.marketplace.seller_realization_rate
  issue: Benchmarks are documented but context-specific and not universal thresholds.
  required_resolution: Use benchmark values as guidance only; do not encode as hard validation failure without platform/account context.
  severity: low
  evidence_refs: ev.amazon.kpi.settlement.001; ev.amazon.return_analysis.001
  status: open
```

## 9. Quality Gates for Deterministic Parser Output

```yaml
quality_gates:
  no_prohibited_card_types:
    status: pass
    notes: No tenant, group, platform_account, account_data_binding, business_scope_set, or business_flow_binding cards were created.
  marketplace_only_boundary:
    status: pass
    notes: No prohibited tenant/group/account/business-flow/bank/logistics/payment/ERP/statutory cards were generated.
  evidence_refs_present:
    status: pass
    notes: All candidate cards include source evidence references.
  field_required_flags_present:
    status: pass
    notes: Every candidate field is marked yes, recommended, or conditional.
  metric_colloquial_names_present:
    status: pass
    notes: Metric cards include colloquial names such as gross sales, topline, AOV, return rate, realization rate, and fee burden.
  metric_implementation_patterns_present:
    status: pass
    notes: Amazon implementation cards include formulas, filters, grain, SQL refs, and metric patterns.
  reconciliation_scope:
    status: pass
    notes: Reconciliation profiles are marketplace-internal only.
  open_reviews:
    status: review_required
    notes: 8 review items remain for missing/inactive source details, tolerance policy, runtime scope layer, and benchmark context.
  unified_edge_taxonomy_present:
    status: pass
    notes: Every candidate edge includes canonical_edge_type, inverse_edge_type, source/target types, materialize_inverse, canonical flag, and legacy aliases where applicable.
  missing_edge_references:
    status: pass
    notes: 0 missing source/target references.
```

## 10. Candidate Coverage Summary

```yaml
candidate_coverage_summary:
  candidate_cards: 352
  candidate_cards_by_type:
  - card_type: business_process
    candidate_count: 4
  - card_type: column
    candidate_count: 140
  - card_type: domain
    candidate_count: 11
  - card_type: execution_constraint_set
    candidate_count: 6
  - card_type: formula_template
    candidate_count: 10
  - card_type: matching_logic
    candidate_count: 4
  - card_type: metric
    candidate_count: 27
  - card_type: metric_dependency
    candidate_count: 5
  - card_type: metric_implementation
    candidate_count: 27
  - card_type: mismatch_category
    candidate_count: 14
  - card_type: output_contract
    candidate_count: 5
  - card_type: platform
    candidate_count: 1
  - card_type: platform_context
    candidate_count: 2
  - card_type: process_variant
    candidate_count: 3
  - card_type: query_pattern
    candidate_count: 13
  - card_type: reconciliation_profile
    candidate_count: 4
  - card_type: reconciliation_side
    candidate_count: 8
  - card_type: reconciliation_unit
    candidate_count: 4
  - card_type: reconciliation_variant
    candidate_count: 3
  - card_type: relationship
    candidate_count: 7
  - card_type: rule
    candidate_count: 12
  - card_type: state_transition
    candidate_count: 4
  - card_type: table
    candidate_count: 5
  - card_type: validation_test
    candidate_count: 7
  - card_type: value_profile
    candidate_count: 11
  - card_type: workflow_step
    candidate_count: 15
  candidate_edges: 933
  canonical_cognee_edges: 865
  parser_helper_edges: 68
  edges_with_legacy_aliases: 436
  materialized_inverse_edges: 4
  review_items: 8
  source_tables: 5
  missing_edge_references: 0
  isolated_cards: 0
```
