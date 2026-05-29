# Canonical Edge Taxonomy Registry — Logistics v6 Role-Split Manifest-Aligned

This compact registry is derived from the scoped canonical edge list and is used by every v5 logistics markdown. It intentionally reuses the same cross-domain edge names for logistics, payment gateway, banking, ERP/accounting, marketplace, and custom-source docs.

## Canonical edge rules

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
    - HAS_IMPLEMENTATION <-> IMPLEMENTS_METRIC
    - HAS_WORKFLOW_STEP <-> BELONGS_TO_PROCESS
    - HAS_STATE_TRANSITION <-> BELONGS_TO_PROCESS
    - HAS_PROCESS_VARIANT <-> EXTENDS_PROCESS
    - HAS_RECONCILIATION_PROFILE <-> SUPPORTS_PROCESS
    - HAS_RECONCILIATION_SIDE <-> BELONGS_TO_RECONCILIATION_PROFILE
    - USES_MATCHING_LOGIC <-> SUPPORTS_RECONCILIATION_PROFILE
    index_reverse_lookup_only:
    - SOURCED_FROM_PLATFORM
    - SOURCED_FROM_PLATFORM_CONTEXT
    - USES_TABLE
    - USES_COLUMN
    - PRODUCES_METRIC
    - USES_RECONCILIATION_PROFILE
    - REQUIRES_RULE
    - USES_OUTPUT_CONTRACT
    - INCLUDES_RULE
    - INCLUDES_VALIDATION_TEST
    - APPLIES_TO_QUERY_PATTERN
  generic_logistics_boundary: Generic vendor/domain docs must not emit tenant, group, platform account, account data binding,
    business scope set, or business flow binding cards.
```


## V5 Manifest Alignment Addendum

```yaml
edge_integrity_manifest:
  source_manifest: marketplace_cleanup_manifest_consolidated_v2.md / Edge Referential-Integrity Manifest
  required_edge_fields:
  - edge_id
  - edge_type
  - source
  - target
  - inverse_edge_type
  - materialize_inverse
  - edge_family
  - edge_class
  checks:
  - every_edge_source_id_exists_or_is_allowed_external_reference
  - every_edge_target_id_exists_or_is_allowed_external_reference
  - edge_type_allowed_for_source_target_pair
  - inverse_policy_valid
  - no_edges_to_deleted_cards
  - no_notes_reference_deleted_card_ids
  semantic_checks:
  - transition_edges_bind_to_correct_process
  - process_variant_edges_only_if_variant_valid
  - reconciliation_side_edges_match_profile
  - query_pattern_edges_match_primary_metric
  deterministic_action_on_failure:
  - delete_edge
  - remap_edge
  - recreate_missing_card_only_if_source_supports_it
  - convert_to_review_item
```

```yaml
canonical_edge_manifest_policy:
  domain_specific_route_edges_forbidden:
  - LOGISTICS_ROUTE_BINDING
  - COURIER_BANK_ROUTE_BINDING
  - MARKETPLACE_LOGISTICS_ROUTE
  - PAYMENT_ROUTE_BINDING
  replacement: Use business_flow_binding cards and canonical Business Flow Binding edges in tenant/group applicability docs.
  generic_logistics_boundary: Generic vendor/domain docs must not emit tenant, group, platform account, account data binding, business scope set, or business flow binding cards.
```


## Emitted edge type registry

| edge_type | inverse_edge_type | materialize_inverse_default | edge_family |
|---|---|---:|---|
| `APPLIES_TO_PLATFORM` | `HAS_APPLICABLE_CARD` | false | `applicability` |
| `APPLIES_TO_PLATFORM_CONTEXT` | `HAS_APPLICABLE_CARD` | false | `applicability` |
| `APPLIES_TO_QUERY_PATTERN` | `HAS_EXECUTION_CONSTRAINT_SET` | false | `execution_guidance` |
| `BELONGS_TO_DOMAIN` | `HAS_METRIC_OR_HAS_BUSINESS_PROCESS` | false | `metric_understanding` |
| `BELONGS_TO_PLATFORM` | `HAS_PLATFORM_CONTEXT` | true | `platform_context` |
| `BELONGS_TO_PROCESS` | `HAS_WORKFLOW_STEP_OR_HAS_STATE_TRANSITION` | true | `process_understanding` |
| `BELONGS_TO_RECONCILIATION_PROFILE` | `HAS_RECONCILIATION_SIDE` | true | `reconciliation_understanding` |
| `BELONGS_TO_TABLE` | `HAS_COLUMN` | true | `data_understanding` |
| `DEPENDS_ON_METRIC` | `DEPENDENCY_OF_METRIC` | false | `metric_understanding` |
| `ENFORCES_RULE` | `HAS_VALIDATION_TEST` | true | `execution_guidance` |
| `EXTENDS_PROCESS` | `HAS_PROCESS_VARIANT` | true | `process_understanding` |
| `EXTENDS_RECONCILIATION_PROFILE` | `HAS_RECONCILIATION_VARIANT` | false | `reconciliation_understanding` |
| `HAS_BUSINESS_PROCESS` | `BELONGS_TO_DOMAIN` | true | `process_understanding` |
| `HAS_COLUMN` | `BELONGS_TO_TABLE` | true | `data_understanding` |
| `HAS_IMPLEMENTATION` | `IMPLEMENTS_METRIC` | true | `metric_understanding` |
| `HAS_MISMATCH_CATEGORY` | `MISMATCH_OF_PROFILE` | false | `reconciliation_understanding` |
| `HAS_PLATFORM_CONTEXT` | `BELONGS_TO_PLATFORM` | true | `platform_context` |
| `HAS_PRIMARY_UNIT` | `PRIMARY_UNIT_OF_PROFILE` | false | `reconciliation_understanding` |
| `HAS_PROCESS_VARIANT` | `EXTENDS_PROCESS` | true | `process_understanding` |
| `HAS_RECONCILIATION_PROFILE` | `SUPPORTS_PROCESS` | true | `reconciliation_understanding` |
| `HAS_RECONCILIATION_SIDE` | `BELONGS_TO_RECONCILIATION_PROFILE` | true | `reconciliation_understanding` |
| `HAS_RELATIONSHIP` | `RELATIONSHIP_OF_TABLE` | false | `data_understanding` |
| `HAS_SECONDARY_UNIT` | `SECONDARY_UNIT_OF_PROFILE` | false | `reconciliation_understanding` |
| `HAS_STATE_TRANSITION` | `BELONGS_TO_PROCESS` | true | `process_understanding` |
| `HAS_VALIDATION_TEST` | `VALIDATES_QUERY_PATTERN_OR_ENFORCES_RULE` | false | `execution_guidance` |
| `HAS_VALUE_PROFILE` | `PROFILES_COLUMN_OR_PROFILES_TABLE` | true | `data_understanding` |
| `HAS_WORKFLOW_STEP` | `BELONGS_TO_PROCESS` | true | `process_understanding` |
| `IMPLEMENTS_METRIC` | `HAS_IMPLEMENTATION` | true | `metric_understanding` |
| `INCLUDES_RULE` | `INCLUDED_IN_CONSTRAINT_SET` | false | `execution_guidance` |
| `INCLUDES_VALIDATION_TEST` | `INCLUDED_IN_CONSTRAINT_SET` | false | `execution_guidance` |
| `OVERRIDES_MATCHING_LOGIC` | `OVERRIDDEN_BY_VARIANT` | false | `reconciliation_understanding` |
| `PARENT_METRIC` | `HAS_METRIC_DEPENDENCY` | false | `metric_understanding` |
| `PRODUCES_METRIC` | `PRODUCED_BY_QUERY_PATTERN` | false | `execution_guidance` |
| `PROFILES_COLUMN` | `HAS_VALUE_PROFILE` | true | `data_understanding` |
| `PROFILES_TABLE` | `HAS_VALUE_PROFILE` | true | `data_understanding` |
| `REQUIRES_RULE` | `REQUIRED_BY_QUERY_PATTERN` | false | `execution_guidance` |
| `SOURCED_FROM_PLATFORM` | `HAS_SOURCE_TABLE` | false | `platform_context` |
| `SOURCED_FROM_PLATFORM_CONTEXT` | `HAS_SOURCE_TABLE` | false | `platform_context` |
| `SOURCE_TABLE` | `SOURCE_OF_RELATIONSHIP` | false | `data_understanding` |
| `SUPPORTS_PROCESS` | `HAS_RECONCILIATION_PROFILE` | true | `reconciliation_understanding` |
| `SUPPORTS_RECONCILIATION_PROFILE` | `USES_MATCHING_LOGIC` | true | `reconciliation_understanding` |
| `TARGETS_CARD` | `TARGETED_BY_QUERY_PATTERN` | false | `execution_guidance` |
| `TARGET_TABLE` | `TARGET_OF_RELATIONSHIP` | false | `data_understanding` |
| `TRIGGERED_BY_STEP` | `TRIGGERS_TRANSITION` | false | `process_understanding` |
| `USED_IN_PROCESS` | `USES_METRIC` | false | `metric_understanding` |
| `USES_COLUMN` | `USED_BY_CONTEXT` | false | `metric_understanding` |
| `USES_DEPENDENT_METRIC` | `DEPENDENCY_USED_BY` | false | `metric_understanding` |
| `USES_FORMULA_TEMPLATE` | `USED_BY_IMPLEMENTATION` | false | `metric_understanding` |
| `USES_MATCHING_LOGIC` | `SUPPORTS_RECONCILIATION_PROFILE` | true | `reconciliation_understanding` |
| `USES_METRIC` | `USED_IN_PROCESS` | false | `metric_understanding` |
| `USES_OUTPUT_CONTRACT` | `USED_BY_CONTEXT` | false | `execution_guidance` |
| `USES_RECONCILIATION_PROFILE` | `USED_BY_QUERY_PATTERN` | false | `execution_guidance` |
| `USES_RELATIONSHIP` | `USED_BY_CONTEXT` | false | `execution_guidance` |
| `USES_SOURCE_COLUMN` | `SOURCE_COLUMN_OF_RELATIONSHIP` | false | `data_understanding` |
| `USES_TABLE` | `USED_BY_CONTEXT` | false | `metric_understanding` |
| `USES_TARGET_COLUMN` | `TARGET_COLUMN_OF_RELATIONSHIP` | false | `data_understanding` |

## Legacy alias normalization

| legacy_alias | canonical_edge_type |
|---|---|
| `column_belongs_to_table` | `BELONGS_TO_TABLE` |
| `value_profile_describes_column` | `PROFILES_COLUMN` |
| `implementation_uses_table` | `USES_TABLE` |
| `implementation_uses_column` | `USES_COLUMN` |
| `implements_metric` | `IMPLEMENTS_METRIC` |
| `metric_depends_on_metric` | `DEPENDS_ON_METRIC` |
| `query_requires_table` | `USES_TABLE` |
| `query_targets_card` | `TARGETS_CARD (prefer PRODUCES_METRIC, USES_RECONCILIATION_PROFILE, REQUIRES_RULE, USES_OUTPUT_CONTRACT, or USES_RELATIONSHIP when target type is known)` |
| `process_uses_table` | `USES_TABLE` |
| `step_in_process` | `BELONGS_TO_PROCESS` |
| `transition_in_process` | `BELONGS_TO_PROCESS` |
| `profile_expected_side` | `HAS_RECONCILIATION_SIDE with side_role=expected` |
| `profile_actual_side` | `HAS_RECONCILIATION_SIDE with side_role=actual` |
| `profile_uses_unit` | `HAS_PRIMARY_UNIT` |
| `profile_uses_matching_logic` | `USES_MATCHING_LOGIC` |
| `profile_has_mismatch_category` | `HAS_MISMATCH_CATEGORY` |
| `side_uses_table` | `USES_TABLE` |
| `side_uses_key_column` | `USES_COLUMN with column_role=key` |
| `side_uses_amount_column` | `USES_COLUMN with column_role=amount` |
| `validation_enforces_constraint` | `INCLUDES_VALIDATION_TEST (reverse old direction)` |
| `rule_enforced_by_constraint` | `INCLUDES_RULE (reverse old direction)` |

## Do not create domain-specific route edges

Do not create `LOGISTICS_ROUTE_BINDING`, `COURIER_BANK_ROUTE_BINDING`, `MARKETPLACE_LOGISTICS_ROUTE`, or similar domain-specific edge names. Use `business_flow_binding` cards and canonical Business Flow Binding edges in tenant/group applicability docs.
