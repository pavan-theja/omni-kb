# **11. Resolution Examples**

**Status:** Draft — V4.0
**Phase:** 1 — KB Schema & Card Design
**Scope:** End-to-end examples using Business Flow Binding, Account Data Binding, and reusable card families

---

## **Purpose of this section**

Resolution Examples show how the KB works end-to-end across analytics, reconciliation, diagnostics, and money-flow tracing.

This section answers:

* How do the card families work together?
* How does scope resolution differ from metric applicability?
* How do Account Data Bindings become SQL filters?
* When is Business Flow Binding needed?
* How do marketplace, logistics, payment gateway, and banking domains connect?
* How do process and reconciliation cards support reasoning?
* How do execution guidance cards constrain downstream execution?

These examples are not retrieval architecture and not execution plans. They are conceptual walkthroughs showing which knowledge should be available.

---

## **11.0 Key Rule for Examples**

Use this rule consistently:

```text
If the question involves one platform/account family, Account Data Binding may be enough.

If the question crosses platform families, such as marketplace → logistics, payment gateway → bank, marketplace → bank, or logistics COD → bank, Business Flow Binding should be resolved.
```

Examples:

```text
Amazon seller realization
→ Metric + Account Data Binding
→ Business Flow Binding usually not required

Razorpay payout vs HDFC credit
→ Business Flow Binding required

Shopify order to Shiprocket COD remittance
→ Business Flow Binding required

Amazon settlement to bank credit
→ Business Flow Binding required
```

---

## **11.1 Example 1 — Analytical Query Without Cross-Platform Flow**

### User question

```text
Show seller realization rate for Acme India Amazon last month.
```

---

### Step 1 — Business Hierarchy

Resolve:

```text
Tenant: Acme Retail
Group: Acme India
Platform: Amazon
Platform Context: Amazon India
Runtime Scope: Acme India Amazon accounts
```

Relevant cards:

```text
tenant.acme_retail
group.acme_india
platform.amazon
platform_context.amazon.in
platform_account.acme.amazon_in.primary
platform_account.acme.amazon_in.secondary
business_scope_set.acme_india.amazon_all
```

Account Data Bindings:

```text
platform_account.acme.amazon_in.primary → amazon_settlement → group_level_id = 22
platform_account.acme.amazon_in.secondary → amazon_settlement → group_level_id = 26
```

Runtime filter:

```sql
group_level_id IN (22, 26)
```

Business Flow Binding:

```text
Not required by default.
```

Reason:

```text
This question calculates a marketplace metric inside Amazon settlement data.
It does not cross into bank, logistics, payment gateway, or accounting evidence.
```

---

### Step 2 — Data Understanding

Relevant cards:

```text
table.zs_observe.amazon_settlement
column.zs_observe.amazon_settlement.total
column.zs_observe.amazon_settlement.product_sales
column.zs_observe.amazon_settlement.type
column.zs_observe.amazon_settlement.created_date
value_profile.amazon_settlement.type
```

Data knowledge:

```text
Table grain: one row per settlement transaction line
Safe dates: created_date, settlement_date
Unsafe date: date_time if varchar
Value profile: type = Order, Refund, Service Fee, etc.
```

---

### Step 3 — Metric Understanding

Relevant cards:

```text
metric.seller_realization_rate
metric_impl.amazon_settlement.seller_realization_rate
formula_template.ratio_percentage
metric_dependency.seller_realization_rate
```

Metric meaning:

```text
Percentage of gross product sales that reaches the seller after deductions.
```

Formula concept:

```text
Net settled amount / gross product sales
```

Important:

```text
Metric implementation is valid for Amazon settlement data.
Selected accounts are resolved separately through Runtime Scope and Account Data Binding.
```

---

### Step 4 — Execution Guidance

Relevant cards:

```text
query_pattern.amazon_settlement.monthly_performance
rule.required_scope_filters
rule.use_safe_date_columns
rule.denominator_protection
validation_test.required_scope_filter_present
validation_test.no_forbidden_date_column
validation_test.denominator_not_zero
```

Required safeguards:

```text
Apply account scope filters.
Use safe date column.
Avoid unsafe varchar date fields.
Protect denominator from divide-by-zero.
```

---

### Conceptual result

```text
Metric: Seller Realization Rate
Scope: Acme India Amazon all accounts
Filter: group_level_id IN (22, 26)
Date: last month using safe Amazon settlement date column
Formula: Amazon settlement seller realization implementation
Business Flow Binding: not needed
```

---

## **11.2 Example 2 — Payment Gateway to Bank Reconciliation**

### User question

```text
Why does Razorpay payout not match my HDFC bank credit for Acme India last month?
```

---

### Step 1 — Business Hierarchy and Flow Binding

Resolve:

```text
Tenant: Acme Retail
Group: Acme India
Payment Gateway: Razorpay
Banking Platform: HDFC Bank
Runtime Scope: Acme India Razorpay → HDFC reconciliation
Money Flow Path: payment_gateway_to_bank
```

Relevant identity cards:

```text
tenant.acme_retail
group.acme_india
platform.razorpay
platform.hdfc_bank
platform_context.razorpay.in
platform_context.hdfc.india
platform_account.acme.razorpay.primary
platform_account.acme.hdfc.current
business_scope_set.acme_india.razorpay_to_hdfc
```

Required Business Flow Binding:

```text
business_flow_binding.acme_india.razorpay_to_hdfc
```

Business Flow Binding participants:

```text
Razorpay account = payout_source
HDFC account = bank_destination
```

Business Flow Binding evidence path:

```text
razorpay_payouts
→ bank_statement
```

Account Data Bindings:

```text
Razorpay account → razorpay_payouts → merchant_id = 'rzp_live_xxx'
HDFC account → bank_statement → bank_account_id = 'hdfc_current_xxx'
```

---

### Step 2 — Process Understanding

Relevant cards:

```text
domain.payment_reconciliation
business_process.payment_gateway_to_bank_reconciliation
workflow_step.payment_captured
workflow_step.payout_created
workflow_step.payout_processed
workflow_step.bank_credit_received
state_transition.payout_processed_to_bank_credit_received
```

Expected process:

```text
Payment captured
→ Payout created
→ Payout processed
→ Bank credit received
```

Expected lag:

```text
Bank credit should usually appear within the configured gateway/bank settlement window.
```

---

### Step 3 — Reconciliation Understanding

Relevant cards:

```text
reconciliation_profile.payment_gateway_payout_to_bank_credit
reconciliation_side.payment_gateway_payout
reconciliation_side.bank_credit
reconciliation_unit.payout_reference
reconciliation_unit.utr
reconciliation_unit.amount_date_bank_account
matching_logic.payment_gateway_payout_to_bank_credit
mismatch_category.delayed_credit
mismatch_category.amount_mismatch
mismatch_category.unidentified_bank_credit
mismatch_category.bank_credit_missing
```

Matching model:

```text
Expected side: payment gateway payout
Actual side: bank credit
Primary match: UTR / bank reference
Fallback match: amount + bank account + date window
Expected alignment: one payout → one bank credit, unless known split/merged credit behavior exists
```

---

### Step 4 — Data Understanding

Relevant cards:

```text
table.zs_observe.razorpay_payouts
table.zs_observe.razorpay_payments
table.zs_observe.bank_statement
relationship.razorpay_payouts.bank_statement_by_utr
```

Data requirements:

```text
Razorpay payout amount
Razorpay payout date
UTR / bank reference
Bank credit amount
Bank transaction date
Bank account identifier
Bank narration, if reference is embedded in text
```

---

### Step 5 — Metric Understanding

Relevant cards:

```text
metric.payout_amount
metric.bank_credit_amount
metric.reconciliation_gap_amount
formula_template.gap_amount
```

Gap concept:

```text
Expected payout amount - actual bank credit amount
```

---

### Step 6 — Execution Guidance

Relevant cards:

```text
query_pattern.payment_gateway_to_bank_recon.summary
rule.required_scope_and_flow_context
rule.prevent_recon_double_counting
rule.apply_reconciliation_window
validation_test.required_scope_filter_present
validation_test.business_flow_binding_present
validation_test.recon_grain_alignment
output_contract.reconciliation_summary
execution_constraint_set.payment_gateway_to_bank_recon
```

Execution safeguards:

```text
Use the selected Razorpay → HDFC Business Flow Binding.
Apply Account Data Bindings for both Razorpay and HDFC tables.
Aggregate to payout/reference grain before matching.
Apply the configured reconciliation window.
Classify delayed separately from missing.
Return reconciliation summary output contract.
```

---

### Conceptual result

```text
Expected: Razorpay payout amount
Actual: HDFC bank credit amount
Gap: Expected - Actual
Classifications: matched, delayed, missing, mismatched, unidentified
Business Flow Binding: required
```

---

## **11.3 Example 3 — Marketplace Settlement to Bank Reconciliation**

### User question

```text
Why does Amazon settlement not match the HDFC bank credit?
```

---

### Step 1 — Business Hierarchy and Flow Binding

Resolve:

```text
Tenant: Acme Retail
Group: Acme India
Marketplace Platform: Amazon
Banking Platform: HDFC Bank
Money Flow Path: marketplace_to_bank
```

Relevant cards:

```text
tenant.acme_retail
group.acme_india
platform.amazon
platform_context.amazon.in
platform_account.acme.amazon_in.primary
platform_account.acme.amazon_in.secondary
platform.hdfc_bank
platform_context.hdfc.india
platform_account.acme.hdfc.current
business_scope_set.acme_india.amazon_to_hdfc
business_flow_binding.acme_india.amazon_to_hdfc
```

Business Flow Binding participants:

```text
Amazon seller account(s) = settlement_source
HDFC bank account = bank_destination
```

Business Flow Binding evidence path:

```text
amazon_settlement
→ bank_statement
```

Account Data Bindings:

```text
Amazon settlement table → group_level_id / seller account scope key
Bank statement table → bank_account_id / account reference scope key
```

---

### Step 2 — Process Understanding

Relevant process:

```text
Marketplace order / settlement cycle
→ marketplace payout / settlement generated
→ bank credit received
```

Relevant cards:

```text
domain.marketplace_finance
domain.bank_reconciliation
business_process.marketplace_settlement_to_bank_reconciliation
workflow_step.marketplace_settlement_generated
workflow_step.marketplace_payout_processed
workflow_step.bank_credit_received
```

---

### Step 3 — Reconciliation Understanding

Relevant cards:

```text
reconciliation_profile.marketplace_settlement_to_bank_credit
reconciliation_side.marketplace_settlement
reconciliation_side.bank_credit
reconciliation_unit.settlement_reference
reconciliation_unit.utr
reconciliation_unit.amount_date_bank_account
matching_logic.marketplace_settlement_to_bank_credit
```

Matching model:

```text
Expected side: marketplace settlement / payout
Actual side: bank credit
Primary match: settlement reference / UTR / bank reference if available
Fallback match: amount + account + settlement date / bank credit date window
```

---

### Step 4 — Data Understanding

Relevant cards:

```text
table.zs_observe.amazon_settlement
table.zs_observe.bank_statement
relationship.amazon_settlement.bank_statement_by_reference_or_amount_window
```

Data requirements:

```text
Settlement amount
Settlement ID / payout reference
Settlement date
Bank credit amount
Bank transaction date
Bank narration / UTR / reference
```

---

### Step 5 — Execution Guidance

Required safeguards:

```text
Use the selected Amazon → HDFC Business Flow Binding.
Do not compare transaction-line grain directly to bank credit grain.
Aggregate marketplace settlement to settlement/payout reference before matching.
Apply account filters from both Amazon and HDFC Account Data Bindings.
Separate delayed bank credits from true missing credits.
```

---

### Conceptual result

```text
Expected: Amazon settlement amount
Actual: HDFC bank credit amount
Gap: Expected - Actual
Possible causes: delayed credit, reference missing, amount mismatch, settlement not yet paid, bank credit unidentified
Business Flow Binding: required
```

---

## **11.4 Example 4 — Marketplace to Logistics Flow**

### User question

```text
Which Shopify COD orders were delivered but not remitted by courier?
```

---

### Step 1 — Business Hierarchy and Flow Binding

Resolve:

```text
Tenant: Acme Retail
Group: Acme India
Channel Platform: Shopify
Logistics Platform: Shiprocket
Money Flow Path: cod_delivery_to_courier_remittance
Fulfilment Model: aggregator_routed
```

Relevant cards:

```text
tenant.acme_retail
group.acme_india
platform.shopify
platform_context.shopify.in
platform_account.acme.shopify.primary
platform.shiprocket
platform_context.shiprocket.in
platform_account.acme.shiprocket.primary
business_flow_binding.acme_india.shopify_to_shiprocket
```

Business Flow Binding participants:

```text
Shopify account = order_source
Shiprocket account = logistics_source / courier aggregator
```

Business Flow Binding evidence path:

```text
shopify_oms
→ shiprocket_oms
→ shiprocket_settlement
```

Account Data Bindings:

```text
Shopify account → shopify_oms → account/group/store scope key
Shiprocket account → shiprocket_oms → account/group scope key
Shiprocket account → shiprocket_settlement → account/group scope key
```

---

### Step 2 — Process Understanding

Relevant cards:

```text
domain.logistics_reconciliation
business_process.order_to_shipment_flow
business_process.logistics_cod_remittance_reconciliation
workflow_step.order_created
workflow_step.shipment_created
workflow_step.delivery_completed
workflow_step.cod_collected_by_courier
workflow_step.cod_remittance_created
```

Expected process:

```text
Shopify order created
→ Shiprocket shipment created
→ AWB assigned
→ Shipment delivered
→ COD collected
→ COD remitted
```

---

### Step 3 — Reconciliation Understanding

Relevant cards:

```text
reconciliation_profile.order_to_shipment_reconciliation
reconciliation_profile.cod_delivery_to_courier_remittance
reconciliation_side.channel_order
reconciliation_side.logistics_shipment
reconciliation_side.logistics_cod_remittance
reconciliation_unit.order_id
reconciliation_unit.awb
matching_logic.order_to_shiprocket_shipment
matching_logic.shiprocket_cod_delivery_to_remittance
mismatch_category.delivered_cod_not_remitted
mismatch_category.shipment_missing_settlement
```

Matching model:

```text
Order source: Shopify OMS
Shipment evidence: Shiprocket OMS
COD remittance evidence: Shiprocket settlement
Primary path: Shopify order ID → Shiprocket order ID → AWB → COD settlement
```

---

### Step 4 — Data Understanding

Relevant cards:

```text
table.zs_observe.shopify_oms
table.zs_observe.shiprocket_oms
table.zs_observe.shiprocket_settlement
relationship.shopify_oms.shiprocket_oms.order_id
relationship.shiprocket_oms.shiprocket_settlement.awb
value_profile.shiprocket_oms.status
value_profile.shiprocket_oms.payment_method
```

Data requirements:

```text
Shopify order ID
Shiprocket composite order ID
AWB code
Payment method = COD
Delivery status / delivered date
COD payable amount
COD remitted / settlement amount
Settlement date
```

---

### Step 5 — Execution Guidance

Required safeguards:

```text
Use the selected Shopify → Shiprocket Business Flow Binding.
Apply Account Data Bindings for Shopify and Shiprocket tables.
Parse or normalize order identifiers where Shiprocket uses composite order IDs.
Use AWB as the primary shipment/remittance bridge.
Do not assume delivered COD means remitted COD.
Classify delivered-but-not-remitted separately from delayed remittance.
```

---

### Conceptual result

```text
Expected: delivered COD shipments from Shopify/Shiprocket flow
Actual: Shiprocket COD settlement/remittance records
Gap: Delivered COD orders without corresponding remittance
Business Flow Binding: required
```

---

## **11.5 Example 5 — Logistics COD to Bank Reconciliation**

### User question

```text
COD was delivered, but why has the cash not reached the bank?
```

---

### Step 1 — Business Hierarchy and Flow Binding

Resolve:

```text
Tenant
Group
Logistics platform account
Bank platform account
Money Flow Path: logistics_cod_to_bank
```

Possible Business Flow Bindings:

```text
business_flow_binding.acme_india.shiprocket_cod_to_hdfc
business_flow_binding.acme_india.ekart_cod_to_icici
business_flow_binding.acme_india.delhivery_cod_to_hdfc
```

Relevant logistics platforms may include:

```text
Shiprocket
Delhivery
DTDC
Ekart
XpressBees
Shadowfax
Ecom Express
```

Business Flow Binding participants:

```text
logistics account = cod_remittance_source
bank account = bank_destination
```

Business Flow Binding evidence path:

```text
shipment / AWB
→ courier settlement / COD remittance
→ UTR / bank reference
→ bank statement credit
```

---

### Step 2 — Process Understanding

Relevant cards:

```text
domain.logistics_reconciliation
domain.bank_reconciliation
business_process.logistics_cod_to_bank_reconciliation
workflow_step.order_shipped
workflow_step.delivery_completed
workflow_step.cod_collected_by_courier
workflow_step.cod_remittance_batch_created
workflow_step.bank_credit_received
```

Expected process:

```text
Order delivered
→ COD collected by courier
→ COD remittance created
→ Bank credit received
```

---

### Step 3 — Reconciliation Understanding

Relevant cards:

```text
reconciliation_profile.logistics_cod_remittance_to_bank_credit
reconciliation_side.logistics_cod_remittance
reconciliation_side.bank_credit
reconciliation_unit.awb
reconciliation_unit.cod_remittance_batch
reconciliation_unit.utr
matching_logic.cod_remittance_to_bank_credit
mismatch_category.delivered_but_cod_not_remitted
mismatch_category.cod_remitted_but_bank_credit_missing
mismatch_category.partial_cod_remittance
mismatch_category.unidentified_bank_credit
```

Matching model:

```text
Expected side: courier COD remittance or remittance batch
Actual side: bank credit
Primary unit: UTR / remittance batch where available
Supporting unit: AWB / shipment ID / courier reference
Fallback: amount + courier + bank account + date window
```

---

### Step 4 — Data Understanding

Relevant tables may include:

```text
table.zs_observe.shiprocket_oms
table.zs_observe.shiprocket_settlement
table.zs_observe.delhivery_settlement
table.zs_observe.dtdc_settlement
table.zs_observe.ekart_settlement
table.zs_observe.xpressbees_settlement
table.zs_observe.bank_statement
```

Important relationships:

```text
Order → shipment / AWB
AWB → courier settlement
Courier remittance → UTR / bank reference
UTR / bank reference → bank statement credit
```

---

### Step 5 — Execution Guidance

Required safeguards:

```text
Use the selected logistics COD → bank Business Flow Binding.
Do not assume every delivered COD order has immediate bank credit.
Respect courier-specific remittance windows.
Aggregate AWB-level COD to remittance batch before comparing to bank credit when settlement is batch-level.
Treat partial remittance separately from missing remittance.
Use courier-specific data quality caveats.
Use bank statement semantics from Banking KB, not logistics docs alone.
```

---

### Conceptual result

```text
Expected: courier COD remittance or remittance batch
Actual: bank credit
Gap: expected COD remittance - actual bank credit
Possible causes: delivery not remitted, remittance delayed, partial remittance, missing UTR, bank credit unidentified
Business Flow Binding: required
```

---

## **11.6 Example 6 — Diagnostic Query Across Marketplace, Logistics, Payment, and Bank**

### User question

```text
Why did my marketplace realization drop this month?
```

---

### Step 1 — Business Hierarchy

Resolve:

```text
Tenant
Group
Marketplace platform accounts
Relevant marketplace contexts
Runtime reporting scope
```

If the marketplace is unspecified, retrieval should return a bundle with unresolved or partial scope rather than hallucinating defaults.

Business Flow Binding is not immediately required for the first pass if the question can be answered from marketplace settlement drivers.

But Business Flow Binding becomes required if the diagnostic branches into:

```text
marketplace → logistics
marketplace → bank
payment gateway → bank
logistics COD → bank
```

---

### Step 2 — Domain and Process Understanding

Relevant domains:

```text
domain.marketplace_finance
domain.logistics_reconciliation
domain.payment_reconciliation
domain.bank_reconciliation
```

Potential processes:

```text
business_process.seller_payout_analysis
business_process.marketplace_settlement_reconciliation
business_process.logistics_freight_reconciliation
business_process.logistics_cod_to_bank_reconciliation
business_process.marketplace_settlement_to_bank_reconciliation
business_process.payment_gateway_to_bank_reconciliation
```

Expected reasoning:

```text
Seller realization can drop due to lower gross sales, higher refunds, higher marketplace fees, shipping deductions, reverse logistics/RTO costs, missing reimbursements, delayed settlements, gateway deductions, or bank credits not received.
```

---

### Step 3 — Metric Understanding

Relevant metrics:

```text
metric.seller_realization_rate
metric.gross_product_sales
metric.net_settled_amount
metric.refund_amount
metric.marketplace_fee_amount
metric.shipping_fee_amount
metric.reverse_shipping_fee_amount
metric.logistics_freight_amount
metric.cod_remitted_amount
metric.payment_gateway_fee_amount
metric.bank_credit_amount
metric.reconciliation_gap_amount
```

---

### Step 4 — Data Understanding

Relevant data sources depend on detected driver path:

```text
Marketplace settlement table
Marketplace order/refund/fee table
Logistics shipment and courier settlement tables
Payment gateway payout/payment tables
Bank statement table
```

---

### Step 5 — Business Flow Binding Branching

If driver path is marketplace-only:

```text
No Business Flow Binding required.
Use marketplace tables + Account Data Binding.
```

If driver path is marketplace to logistics:

```text
Resolve relevant Business Flow Binding, e.g.
business_flow_binding.acme_india.flipkart_to_ekart
business_flow_binding.acme_india.shopify_to_shiprocket
```

If driver path is marketplace/payment to bank:

```text
Resolve relevant Business Flow Binding, e.g.
business_flow_binding.acme_india.amazon_to_hdfc
business_flow_binding.acme_india.razorpay_to_hdfc
```

If driver path is logistics COD to bank:

```text
Resolve relevant Business Flow Binding, e.g.
business_flow_binding.acme_india.shiprocket_cod_to_hdfc
```

---

### Step 6 — Diagnostic Reasoning

Possible drivers:

```text
Refund spike
Marketplace fee increase
Shipping fee increase
RTO / reverse logistics cost increase
Delayed marketplace settlement
COD delivered but not remitted
Payment gateway payout delayed
Bank credit missing or unidentified
Missing reimbursement
Mix shift toward lower-realization categories
```

---

### Step 7 — Execution Guidance

Relevant cards:

```text
query_pattern.seller_realization_driver_breakdown
query_pattern.month_over_month_metric_driver_analysis
query_pattern.marketplace_to_bank_recon.summary
query_pattern.logistics_cod_to_bank_recon.summary
query_pattern.payment_gateway_to_bank_recon.summary
rule.required_scope_filters
rule.required_scope_and_flow_context
rule.use_safe_date_columns
rule.prevent_double_counting
output_contract.diagnostic_summary
```

Expected structured output:

```text
Summary
Metric movement
Top drivers
Supporting breakdown
Related reconciliation gaps
Resolved Business Flow Bindings, if used
Confidence
Next actions
```

---

## **11.7 What These Examples Prove**

The same KB model supports:

```text
Analytical question:
What is the metric?

Single-platform metric question:
Which account/table filters apply?

Cross-platform reconciliation question:
Which platform accounts participate together?

Diagnostic question:
Why did something change?

Money-flow question:
Where did the money get stuck?
```

The system remains clean because:

```text
Business Hierarchy resolves identity and ownership.
Account Data Binding resolves account-to-table filters.
Business Scope Set resolves durable named account groups.
Business Flow Binding resolves cross-platform flow participation.
Data Understanding resolves evidence.
Metric Understanding resolves computation.
Process Understanding resolves expected flow.
Reconciliation Understanding resolves matching semantics.
Execution Guidance resolves guardrails and output contracts.
```

---

## **11.8 Final Principle**

```text
The KB does not execute the answer.
The KB supplies the structured knowledge needed to execute the answer correctly.

Account Data Binding tells the system how to filter tables.
Business Flow Binding tells the system which platform accounts participate together in a reusable flow.
```
---