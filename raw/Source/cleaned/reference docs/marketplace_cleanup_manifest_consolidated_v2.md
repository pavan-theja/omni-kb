# Marketplace Cleanup Manifest — Consolidated V2

This consolidated markdown combines the reusable marketplace cleanup manifest pack with the V2 benchmark and scope-identifier addendum. It is intended to be reused across marketplace canonical markdown reviews, including Amazon, Flipkart, Myntra, Nykaa, Shopify, and similar marketplace sources.

---

## 1. Evidence Anchoring Manifest

**Purpose:** Every card must be traceable to an explicit source section, not inferred from generic marketplace intuition.

**Use it to catch:**

- Lazy workflows like “order recorded → deductions applied → settlement posted”
- Metric formulas not actually supported by table columns
- Process variants invented from mere segments
- Reviews opened even though the source already answers the issue

**Manifest fields:**

```yaml
evidence_anchor_manifest:
  source_evidence_id: ev.<marketplace>.<topic>.<seq>
  source_section: exact document section/table/query block
  evidence_type: prose | table | metric_definition | reconciliation_playbook | schema_reference | caveat | query_example
  supported_semantics:
    - what this evidence explicitly supports
  unsupported_semantics:
    - what must not be inferred from this evidence
  allowed_card_types:
    - metric
    - rule
    - reconciliation_profile
  forbidden_card_types:
    - process_variant
    - execution_constraint_set
  confidence_policy:
    explicit_table_or_formula: high
    inferred_from_prose: medium
    absent_or_ambiguous: review_required
```

**Amazon example:** The OMS ↔ Settlement framework explicitly defines OMS Revenue, Settlement `product_sales`, and Gap / Yet to be Settled; therefore `order_to_settlement` must be a reconciliation framework, not a generic lifecycle.

---

## 2. Card-Type Fit Manifest

**Purpose:** Make sure each semantic object is the right kind of card.

This would have caught `execution_constraint_set.amazon.revenue_vs_cashflow`: the idea was valid, but the card type was wrong. It should be a rule about reporting scope, not an execution constraint.

```yaml
card_type_fit_manifest:
  candidate_card_id: <card_id>
  proposed_card_type: <card_type>
  semantic_question: What is this thing?
  card_type_decision_rules:
    rule:
      use_when: source states a business/query rule or interpretation rule
    execution_constraint_set:
      use_when: cross-cutting runtime behavior must be enforced across many query patterns
    process_variant:
      use_when: a materially different process sequence exists
    value_profile:
      use_when: source only defines column values/segments
    reconciliation_variant:
      use_when: same reconciliation has different matching/source behavior by context
    review_item:
      use_when: source lacks evidence needed to safely create or finalize a card
  remediation:
    - keep_as_is
    - recast_card_type
    - remove_card
    - downgrade_to_note
    - convert_to_review
```

**Common repeatable rule:** Segments are usually value profiles, not process variants. FBA/MFN, B2B/B2C, India/International, COD/Prepaid should not become process variants unless the document describes a different workflow or matching logic.

---

## 3. Lazy-Load Detection Manifest

**Purpose:** Block generic, low-material cards before they enter the graph.

Run this against `business_process`, `workflow_step`, `state_transition`, `process_variant`, `metric_implementation`, `query_pattern`, and `execution_constraint_set`.

```yaml
lazy_load_detection_manifest:
  fail_if:
    step_description_too_short:
      max_words_without_specific_column_or_metric: 5
      examples:
        - order recorded
        - refund debited
        - variance computed
    candidate_notes_repeat_name: true
    no_source_specific_column_or_value: true
    formula_contains_placeholders:
      - eligible return refund value
      - reversed fees
      - non_recovered_fees
      - actual ItemFees from disbursement
    process_description_is_generic_lifecycle: true
    evidence_refs_are_broad_but_card_is_specific: true
  remediation:
    - replace_with_source_specific_definition
    - convert_to_rule_or_reconciliation_step
    - delete_if_no_material_semantic_content
    - open_review_only_if_source_gap_is_real
```

**Practical standard:** A workflow step should mention at least one of:

- source table
- source column
- source transaction type
- reconciliation side
- amount field
- known timing behavior
- documented business meaning

If it says only “order recorded” or “refund debited,” it fails.

---

## 4. Process Versus Reconciliation Manifest

**Purpose:** Separate business lifecycle from reconciliation framework.

Amazon’s big issue was exactly this: `order_to_settlement` was treated as a lifecycle when the source defined it as a reconciliation: OMS forward revenue versus settlement product sales, with the gap as yet-to-be-settled.

```yaml
process_reconciliation_manifest:
  source_pattern:
    reconciliation_if_source_contains:
      - expected side
      - actual side
      - gap
      - match count
      - amount comparison
      - timing difference
      - mismatch category
    process_if_source_contains:
      - ordered business events
      - operational lifecycle
      - state progression
      - action sequence
  required_resolution:
    if_reconciliation:
      create:
        - reconciliation_profile
        - reconciliation_side
        - reconciliation_unit
        - matching_logic
        - mismatch_category
      avoid:
        - generic workflow_step lifecycle unless source gives process sequence
    if_process:
      create:
        - business_process
        - workflow_step
        - state_transition
      avoid:
        - reconciliation sides unless comparison logic exists
```

Use this especially for phrases like:

- “A reconciles to B”
- “expected vs actual”
- “gap”
- “variance”
- “matching”
- “settlement vs disbursement”
- “source of truth”

Those should usually produce reconciliation cards first, not process cards.

---

## 5. State-Transition Binding Manifest

**Purpose:** Prevent transitions from being mapped to the wrong process.

A state transition must belong to the process where its state change actually makes business sense. For example, Order → Refund belongs to return/refund settlement behavior, not the forward OMS-to-settlement revenue reconciliation.

```yaml
state_transition_binding_manifest:
  transition_card_id: <state_transition_id>
  state_column: <column_id>
  from_state: <documented_value>
  to_state: <documented_value>
  value_profile_exists: true
  source_values_exist_in_value_profile: true
  valid_process_binding_tests:
    - process_mentions_same_state_column_or_table
    - process_description_mentions_transition_business_meaning
    - workflow_steps_include_before_after_context
  fail_if:
    - transition_is_attached_to_unrelated_process
    - from_or_to_state_not_in_value_profile
    - transition_meaning_is_generic
    - edge_links_transition_to_process_only_because_same_document_section
  remediation:
    - remap_to_correct_process
    - remove_process_edge
    - create_dedicated_process_if_source_supports_it
    - convert_to_value_profile_note
```

**Repeatable rule:** A transition edge is not valid just because both cards share evidence refs. It needs semantic fit.

---

## 6. Process-Variant Discipline Manifest

**Purpose:** Stop turning every segment into a process variant.

```yaml
process_variant_manifest:
  create_process_variant_only_if:
    - source documents a different sequence of steps
    - source documents different state transitions
    - source documents different required matching logic
    - source documents different required filters that change process behavior
  do_not_create_for:
    - fulfilment labels alone
    - geography labels alone
    - account/group labels alone
    - benchmark differences alone
    - table availability differences alone
  alternative_card_type:
    fulfilment_label: value_profile
    geography_scope: platform_context | value_profile
    source_availability_difference: rule | caveat | reconciliation_variant
    matching_difference: reconciliation_variant
```

**Amazon examples:**

- FBA/MFN should be value profiles or fee-segmentation semantics.
- India returns vs international returns should be a reconciliation/source-availability variant, not a generic process variant.

---

## 7. Metric Implementation Executability Manifest

**Purpose:** A metric definition may be valid, but a platform-specific implementation must be executable against documented columns.

This would have caught:

- `SUM(quantity)` without a documented `amazon_oms.quantity`
- `SUM(reversed fees + fulfillment fee refunds)` as a non-executable placeholder
- `eligible return refund value` as an undefined denominator

```yaml
metric_implementation_manifest:
  metric_id: <metric>
  implementation_id: <metric_implementation>
  source_tables:
    - <table_id>
  formula_must:
    - reference existing column cards
    - include required filters
    - respect transaction/value sign semantics
    - be executable SQL-like logic
    - align with source metric definition
  fail_if_formula_contains:
    - natural_language_placeholder
    - undefined_component
    - missing_denominator_definition
    - column_not_declared
    - wrong_grain
  remediation:
    metric_valid_but_implementation_invalid:
      - keep metric card
      - delete or review implementation
    formula_partially_defined:
      - convert missing pieces into review_item
      - avoid accepted implementation
    formula_fully_supported:
      - create sql_pattern
      - link_sql_ref
```

**Repeatable rule:** A generic metric can exist from a source KPI table; a marketplace implementation needs documented columns and filters.

---

## 8. Formula and Sign-Semantics Manifest

**Purpose:** Prevent sign errors and fee/refund mixing.

Marketplace financial docs often have negative fee rows, positive refund credits, and mixed settlement types. Amazon has exactly this issue: settlement revenue reporting uses Order/Refund, while cash-flow uses all settlement types; disbursement ItemFees need transaction context.

```yaml
formula_sign_manifest:
  amount_column: <column_id>
  sign_context_columns:
    - transaction_type
    - type
    - mp_fee_type
    - charged_amount_type
  sign_rules:
    positive_means: credit | revenue | refund_credit | varies
    negative_means: deduction | refund | fee | varies
  required_filters_by_use_case:
    revenue_reporting:
      - sales/refund transaction types only
    cashflow_reporting:
      - all payout-impacting settlement types
    fee_reporting:
      - transaction_type context required
  fail_if:
    - sums_amount_without_required_type_context
    - treats_all_fee_rows_as_negative
    - mixes_order_and_refund_without_netting_intent
```

---

## 9. Schema/Type Fidelity Manifest

**Purpose:** Ensure canonical column cards match the source table docs.

This catches:

- string date fields misrepresented as dates
- boolean flags treated as strings
- dimensions stored as varchar but used as decimals without cast
- mandatory filters missing or downgraded to optional

```yaml
schema_type_manifest:
  table_id: <table_id>
  column_id: <column_id>
  source_declared_type: <type_from_doc>
  canonical_data_type: <type_in_md>
  type_match: true | false
  cast_required: true | false
  mandatory_filters:
    - is_active = true
  optional_filters:
    - zen_status = true
  fail_if:
    - source_string_marked_as_date
    - boolean_filter_written_as_string
    - mandatory_filter_missing
    - table_scope_ignored
  remediation:
    - correct_data_type
    - add_cast_note
    - add_rule_card
    - update_sql_patterns
```

This is especially important because table docs often contain “pitfall” sections that are as important as the column list itself.

---

## 10. SQL Reference Integrity Manifest

**Purpose:** Every `sql_ref` must resolve.

The canonical markdown can look clean but still contain dangling SQL refs. That is a lazy-load smell.

```yaml
sql_ref_integrity_manifest:
  sql_ref_registry:
    required_for_card_types:
      - metric_implementation
      - query_pattern
      - validation_test
  checks:
    - every_sql_ref_has_sql_pattern_block
    - every_sql_pattern_uses_existing_tables
    - every_sql_pattern_uses_existing_columns
    - sql_filters_match_required_filters
    - sql_formula_matches_metric_formula
  fail_if:
    - dangling_sql_ref
    - sql_uses_deleted_card
    - sql_uses_undefined_column
    - formula_and_sql_disagree
  remediation:
    - add_sql_pattern
    - remove_sql_ref
    - downgrade_to_review
    - fix formula and SQL together
```

---

## 11. Edge Referential-Integrity Manifest

**Purpose:** Prevent graph corruption after cards are removed or remapped.

This would catch deleted process variants still referenced by edges, transitions mapped to wrong processes, and stale ids in notes.

```yaml
edge_integrity_manifest:
  checks:
    - every_edge_source_id_exists
    - every_edge_target_id_exists
    - source_type_matches_card_type
    - target_type_matches_card_type
    - edge_type_allowed_for_source_target_pair
    - inverse_policy_valid
    - no_edges_to_deleted_cards
    - no_notes_reference_deleted_card_ids
  semantic_checks:
    - transition_edges_bind_to_correct_process
    - process_variant_edges_only_if_variant_valid
    - reconciliation_side_edges_match_profile
    - query_pattern_edges_match_primary_metric
  remediation:
    - delete_edge
    - remap_edge
    - recreate_missing_card_only_if_source_supports_it
```

The V8 canonical file already has a unified edge taxonomy and allowed/forbidden card-type framework, so this integrity manifest should be mandatory for every later marketplace doc.

---

## 12. Review-State Discipline Manifest — V2

**Purpose:** Stop creating `review_required` items for things the source already states, and stop accepting things that are not actually supported.

Amazon benchmark review was the example: benchmarks were documented, but they should be encoded as guidance, not hard validation thresholds.

```yaml
review_state_manifest:
  review_item_id: <review_id>
  issue_type:
    - missing_evidence
    - ambiguous_threshold
    - unsupported_column
    - context_specific_guidance
    - external_runtime_scope
  close_review_if:
    - source explicitly defines the value
    - source explicitly defines caveat/context
    - source supports guidance but not hard validation
    - benchmark is explicitly documented but context-specific
    - benchmark can be encoded as guidance rather than validation
    - group_level_id values are source-documented and only used as scope specs or benchmark qualifiers
  keep_open_if:
    - tolerance not documented
    - numeric reconciliation tolerance is not documented
    - runtime account/scope binding external
    - runtime user/account scope selection is not documented
    - denominator undefined
    - required column absent
  status_resolution:
    resolved_as_guidance:
      use_when: source gives benchmark but says/context implies non-universal
    resolved_as_rule:
      use_when: source gives deterministic rule
    remains_open:
      use_when: source lacks operational value needed by parser/runtime
```

**Repeatable rule:** Context-specific benchmark ≠ open review. It means: encode benchmark as guidance, and block hard-failure validation unless context is supplied.

---

## 13. Rule Versus Execution-Constraint Manifest

**Purpose:** Avoid vague execution constraints.

```yaml
rule_constraint_split_manifest:
  rule_card_when:
    - explains business interpretation
    - tells how to filter for a metric
    - prevents a semantic mistake
    - applies to a table, metric, relationship, or reconciliation
  execution_constraint_set_when:
    - global runtime behavior applies across many cards
    - query generation must always enforce it
    - it is not merely business prose
  fail_if_execution_constraint:
    - has only one narrow related concept
    - reads like a business rule
    - user cannot tell what execution behavior it changes
    - overlaps existing rule card
  remediation:
    - convert_to_rule
    - attach_to_query_patterns
    - remove_if_duplicate
```

**Example:**

- “Use Order/Refund for revenue; use all settlement types for cash-flow” → rule
- “Always apply active-row filters across all Amazon core tables” → execution constraint

---

## 14. Scope and Out-of-Scope Manifest

**Purpose:** Keep marketplace docs from spawning tenant/account/bank/tax-filing/logistics cards.

```yaml
scope_guardrail_manifest:
  allowed_scope:
    - marketplace_semantics
    - marketplace tables
    - marketplace columns
    - marketplace metrics
    - marketplace reconciliation
    - marketplace payout/cash-flow semantics
  forbidden_scope:
    - tenant
    - group
    - platform_account
    - bank_account
    - statutory_tax_filing
    - ERP/accounting posting
    - external logistics operations
  allowed_as_column_or_caveat:
    - group_id
    - group_level_id
    - GSTIN-like fields
    - payout references
    - fulfilment labels
  fail_if:
    - scope column becomes account card
    - tax deduction becomes filing compliance
    - settlement payout becomes bank reconciliation
```

This should be copied almost unchanged across marketplace docs. For documented scope identifiers that should remain in canonical marketplace cards without becoming runtime scope bindings, use the dedicated Scope Identifier Manifest in section 18.

---

## 15. Output Contract and Query-Pattern Manifest

**Purpose:** Ensure query patterns produce sane, source-backed outputs.

```yaml
query_output_manifest:
  query_pattern_id: <query_pattern>
  natural_language_patterns:
    - <question>
  primary_metric: <metric_id>
  source_tables:
    - <table_id>
  required_rules:
    - active_filter
    - transaction_type_filter
    - aggregate_before_join
  output_contract:
    output_columns:
      - column_or_alias
    must_include:
      - grain_identifier
      - metric_value
      - variance_or_status_when_recon
  fail_if:
    - primary_metric_missing
    - source_tables_do_not_support_metric
    - output_contract_has_undefined_columns
    - query_logic_mentions_uncreated_card
```

---

## 16. Parser QA Summary Manifest — V2

**Purpose:** Every cleaned markdown version should end with machine-checkable QA counts.

```yaml
parser_quality_manifest:
  candidate_cards: <count>
  candidate_edges: <count>
  source_evidence_count: <count>
  sql_patterns: <count>
  missing_edge_references: 0
  dangling_sql_refs: 0
  deleted_card_references: 0
  open_reviews: <count>
  lazy_workflow_steps: 0
  placeholder_metric_formulas: 0
  unsupported_metric_implementations: 0
  process_variants_review_required: 0
  unresolved_benchmark_reviews_without_reason: 0
  hard_threshold_benchmarks_without_rule: 0
  forbidden_scope_cards_from_scope_ids: 0
```

This gives you an objective release gate instead of relying on eyeballing.

---

## 17. Benchmark Card Manifest

**Purpose:** Allow explicitly documented benchmark values to live on canonical metric cards as guidance, not as hard validation thresholds.

```yaml
benchmark_card_manifest:
  purpose: Allow explicitly documented benchmark values to live on canonical metric cards as guidance, not as hard validation thresholds.
  include_benchmarks_when:
    - source document gives a benchmark table, benchmark range, or explicit benchmark sentence
    - benchmark is tied to a metric definition, table-specific KPI section, or marketplace context
    - benchmark can be represented without creating tenant/group/account-binding cards
  benchmark_field_policy:
    field_name: benchmarks
    allowed_on_card_types:
      - metric
    allowed_value_shapes:
      - scalar_guidance_string
      - named_context_map
      - group_level_qualified_context_map
    required_subfields_when_available:
      - interpretation
      - source
  validation_policy:
    default_behavior: guidance_only
    hard_failure_allowed_only_if: separate validation_test or rule documents account/category/period-specific thresholds
  fail_if:
    - benchmark is opened as review only because it is context-specific despite being explicitly documented
    - benchmark is encoded as hard pass/fail validation without context
    - benchmark creates tenant, group, platform_account, or account_data_binding cards
```

### Canonical example

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.safe_t_recovery_rate
  fields:
    benchmarks:
      eligible_returns_healthy: '15-30 percent'
      below_15_percent: investigate claim process gaps or systematic Amazon rejection patterns
      above_30_percent: verify eligibility filtering is correct; may indicate over-claiming
      source: docx section 9 (SAFE-T Reimbursement Program)
```

---

## 18. Scope Identifier Manifest

**Purpose:** Permit documented marketplace scope identifiers in canonical cards while preserving the marketplace-only boundary.

```yaml
scope_identifier_manifest:
  purpose: Permit documented marketplace scope identifiers in canonical cards while preserving the marketplace-only boundary.
  allowed_scope_identifier_fields:
    - documented_scope_values
    - scope_filter_columns
    - benchmark qualifiers containing group_level_id values
  allowed_on_card_types:
    - column
    - metric
    - platform_context
  allowed_examples:
    - column.zs_observe.amazon_settlement.group_level_id.documented_scope_values
    - metric.marketplace.seller_realization_rate.benchmarks.india_amazon_in
  forbidden_derivations:
    - tenant
    - group
    - platform_account
    - account_data_binding
    - business_scope_set
  runtime_scope_policy: Canonical cards may document source-provided ids and benchmark qualifiers; actual user/account selection remains a runtime or external scope-layer responsibility.
```

### Canonical example

```yaml
candidate_card:
  card_type: metric
  card_id: metric.marketplace.seller_realization_rate
  fields:
    benchmarks:
      india_amazon_in: '70-78 percent (group_level_id 22, 26)'
      us_amazon_com: '50-55 percent (group_level_id 123)'
      interpretation: Outside range warrants investigation into return volume, ad spend, or inventory write-offs.
      source: docx section 2 (Settlement & Realization Metrics) and table-specific seller realization section
```

---

## 19. Recommended Repeatable Cleanup Sequence

Use this order for any future marketplace doc:

1. **Build evidence registry first.** No cards before source evidence ids are clear.
2. **Apply card-type fit.** Recast rules, variants, processes, constraints, and reconciliation cards before fixing edges.
3. **Run lazy-load detection.** Remove generic workflow steps, placeholder formulas, and note-only cards.
4. **Resolve process/reconciliation conflicts.** Anything with expected/actual/gap/variance becomes reconciliation-first.
5. **Validate metric implementations.** Keep generic metric definitions, but delete or review implementations that lack columns or executable formulas.
6. **Validate schema and filters.** Fix data types, mandatory filters, boolean/string traps, and date-string traps.
7. **Apply benchmark-card policy.** Document explicit benchmarks on metric cards as guidance; do not convert them into hard validation unless a separate rule or validation test documents the required account/category/period-specific threshold.
8. **Apply scope-identifier policy.** Keep documented scope ids as values, qualifiers, or filter columns; do not derive tenant, group, platform account, account binding, or business scope cards from them.
9. **Regenerate or repair edges.** Do this after card deletion/remapping, not before.
10. **Resolve reviews.** Explicit documented guidance should not remain open; missing tolerances and external runtime scope can remain open.
11. **Check SQL refs and SQL patterns.** No dangling `sql_ref`.
12. **Emit parser QA summary.** Ship only if hard integrity counts are clean.

---

## 20. The Core Rule

For every conflict, ask:

> Is this source-backed, correctly typed, executable, and connected to the right semantic neighborhood?

If any answer is “no,” the fix is one of five actions:

```yaml
conflict_resolution_actions:
  - delete_card
  - recast_card_type
  - remap_edges
  - downgrade_to_rule_or_note
  - keep_review_open_with_specific_missing_evidence
```

That is the reusable manifest system to apply to Flipkart, Myntra, Nykaa, Shopify, Amazon, or any other marketplace canonical markdown.
