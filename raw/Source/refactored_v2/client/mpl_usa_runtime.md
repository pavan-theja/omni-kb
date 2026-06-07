# MPL USA — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `mpl_usa_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Braintree
  config: braintree pay-in deposits
  reason: No Braintree canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
- label: Skrill
  config: international gaming payment gateway
  reason: No Skrill canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
- label: Hyperwallet
  config: hyperwallet payout withdrawals
  reason: No Hyperwallet canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 1
  account_data_binding: 2
  business_scope_set: 1
  business_flow_binding: 1
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 4
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 2
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 2
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 1
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 2
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 1
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 1
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 1
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 2
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 1
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 1
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 1
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 1
  GROUP_HAS_BUSINESS_SCOPE_SET: 1
  GROUP_HAS_PLATFORM_ACCOUNT: 1
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 1
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 2
  PLATFORM_ACCOUNT_USES_PLATFORM: 1
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 1
  TENANT_HAS_GROUP: 1
allowed_card_types:
- tenant
- group
- platform_account
- account_data_binding
- business_scope_set
- business_flow_binding
render_order:
- tenant
- group
- platform_account
- account_data_binding
- business_scope_set
- business_flow_binding
boundary_policy: client runtime only; no reusable semantic card bodies are emitted in this file
integration_layers:
- marketplace
- logistics
- oms
wms_integration:
  source_packs:
  - increff_wms.md
  - unicommerce_wms.md
  added_runtime_cards: 0
  added_runtime_edges: 0
  supported_wms_accounts: 0
  supported_wms_bindings: 0
  resolved_deferred_mentions: 0
bank_payment_integration:
  source_packs:
  - payment_gateway.md
  - bank_statement.md
  added_runtime_cards: 0
  added_runtime_edges: 0
  supported_payment_bindings: 0
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 3
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.mpl_usa

```yaml
canonical_card:
  canonical_id: tenant.mpl_usa
  card_type: tenant
  canonical_name: MPL USA
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL USA
    - mpl_usa
    - MPL USA runtime tenant
    colloquial_phrases:
    - MPL USA client runtime
    - MPL USA source configuration
    - MPL USA scoped reconciliation setup
    business_meaning: Runtime tenant identity for MPL USA. It anchors the client's marketplace, logistics, OMS,
      WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to MPL USA?
    - Which group and account bindings should constrain MPL USA's SQL handoff?
    - After MPL USA's runtime scope is resolved, which domain layer should receive the query next?
    semantic_tags:
    - client_runtime
    - tenant_identity
    - source_scope_root
    - runtime_boundary
    included_concepts:
    - client legal identity
    - runtime source routing
    - group/account traversal root
    excluded_concepts:
    - reusable platform semantics
    - physical table definitions
    - metric formulas
    caveats:
    - Do not infer platform coverage from this tenant card alone; use the linked platform-account and account-data-binding
      cards.
    examples: []
  retrieval:
    node_sets:
    - card_type:tenant
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    embedding_text: MPL USA is the runtime tenant root for the client's marketplace, logistics, OMS, WMS, payment-gateway,
      and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding nodes
      before invoking reusable canonical packs.
    search_keywords:
    - MPL USA
    - mpl_usa
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.mpl_usa
  evidence:
    source_documents:
    - MPL USA.docx
    source_path: MPL USA.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
  fields:
    tenant_slug: mpl_usa
    tenant_name: MPL USA
    legal_name: MPL USA
    active: true
```

### 2.2 Group Cards

#### group.mpl_usa.g2.gl3

```yaml
canonical_card:
  canonical_id: group.mpl_usa.g2.gl3
  card_type: group
  canonical_name: MPL USA group 2/3
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL
    - MPL USA group 2/3
    - group_id 2
    - group_level_id 3
    colloquial_phrases:
    - MPL USA group scope
    - MPL runtime scope
    - group 2 level 3 query boundary
    business_meaning: 'Runtime group scope for MPL USA: group_id=2 and group_level_id=3. It is the client-specific
      filter boundary that must be applied before resolving account bindings for US in USD.'
    business_questions:
    - Which bindings use group_id=2 and group_level_id=3?
    - Which source families are active under MPL?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=2
    - group_level_id=3
    - client group runtime scope
    excluded_concepts:
    - domain metric logic
    - platform table schemas
    - bank or gateway account ownership by itself
    caveats:
    - Treat this as runtime scope only; do not create reusable tenant or platform semantics from group IDs.
    examples: []
  retrieval:
    node_sets:
    - card_type:group
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - group_id_value:2
    - group_level_id_value:3
    embedding_text: MPL is the runtime group node for MPL USA. Apply group_id=2 and group_level_id=3 when traversing
      from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - MPL USA
    - MPL
    - group_id 2
    - group_level_id 3
    - runtime group scope
    exact_match_keys:
    - group.mpl_usa.g2.gl3
  evidence:
    source_documents:
    - MPL USA.docx
    source_path: MPL USA.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    group_level_id: '3'
  fields:
    tenant_id: tenant.mpl_usa
    group_id_value: '2'
    group_level_id_value: '3'
    group_name: MPL
    default_currency: USD
    country: US
```

### 2.3 Platform Account Cards

#### platform_account.mpl_usa.mpl_wallet_oms.oms

```yaml
canonical_card:
  canonical_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  card_type: platform_account
  canonical_name: MPL USA MPL Wallet OMS account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL USA MPL Wallet OMS account
    - MPL USA MPL USA MPL Wallet OMS account
    - Zenstatement Oms Business Kb
    - MPL USA MPL Wallet OMS account OMS account
    colloquial_phrases:
    - MPL USA MPL USA MPL Wallet OMS account source account
    - MPL USA MPL Wallet OMS account OMS runtime account
    - MPL USA MPL Wallet OMS account configured source family
    business_meaning: Runtime platform account for MPL USA's MPL USA MPL Wallet OMS account OMS sources. It points
      traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb and groups
      the client's table-level account-data bindings for this source.
    business_questions:
    - Which MPL USA MPL Wallet OMS account table bindings are available for MPL USA?
    - Which canonical platform/context should MPL USA's MPL USA MPL Wallet OMS account questions traverse through?
    - Which source roles under MPL USA MPL Wallet OMS account are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: MPL proprietary deposit and withdrawal ledgers'
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    excluded_concepts:
    - reusable table schemas
    - metric formulas
    - cross-source reconciliation logic by itself
    caveats:
    - Use account-data-binding cards for exact physical table selection and runtime scope filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:platform_account
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - platform_account_id:platform_account.mpl_usa.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: MPL USA's MPL USA MPL Wallet OMS account platform account routes OMS questions to platform.zenstatement_oms_business_kb
      / platform_context.zenstatement.oms_business_kb. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - MPL USA
    - MPL USA MPL Wallet OMS account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.mpl_usa.mpl_wallet_oms.oms
  evidence:
    source_documents:
    - MPL USA.docx
    - oms_business_kb.md
    source_path: MPL USA.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: MPL USA MPL Wallet OMS account
    account_type: wallet_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: MPL proprietary deposit and withdrawal ledgers
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '2'
      group_level_id: '3'
```

### 2.4 Account Data Binding Cards

#### account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  card_type: account_data_binding
  canonical_name: MPL USA MPL Wallet OMS wallet_deposit_oms binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL Wallet OMS wallet deposit OMS
    - mpl_oms_deposit
    - zs_observe.mpl_oms_deposit
    - MPL proprietary deposit and withdrawal ledgers
    - MPL USA MPL Wallet OMS wallet deposit OMS
    colloquial_phrases:
    - MPL USA MPL Wallet OMS wallet deposit OMS source
    - MPL Wallet OMS wallet deposit OMS runtime binding
    - mpl_oms_deposit for MPL USA
    business_meaning: This account-data binding tells the resolver that MPL USA's MPL Wallet OMS wallet deposit
      OMS evidence should use zs_observe.mpl_oms_deposit. Apply group_id=2, group_level_id=3 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which MPL Wallet OMS OMS rows should answer MPL USA's wallet deposit OMS question?
    - Which runtime scope must be injected before using mpl_oms_deposit?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - wallet_deposit_oms
    included_concepts:
    - zs_observe.mpl_oms_deposit
    - wallet deposit OMS
    - MPL Wallet OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=2
    - group_level_id=3
    - oms_business_kb.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - OMS rows define order or expected-side evidence; actual payment, bank, shipment, or warehouse proof must come
      from linked packs.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - platform_account_id:platform_account.mpl_usa.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:wallet_deposit_oms
    - table_id:table.zs_observe.mpl_oms_deposit
    - runtime_source_family:oms
    embedding_text: 'For MPL USA, the MPL Wallet OMS wallet deposit OMS binding selects zs_observe.mpl_oms_deposit
      as OMS evidence. Scope: group_id=2, group_level_id=3. Reusable semantics come from oms_business_kb.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - MPL USA
    - MPL Wallet OMS
    - wallet deposit OMS
    - OMS
    - zs_observe.mpl_oms_deposit
    - mpl_oms_deposit
    - wallet_deposit_oms
    - oms_business_kb.md
    - group_id=2
    - group_level_id=3
    exact_match_keys:
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  evidence:
    source_documents:
    - MPL USA.docx
    - oms_business_kb.md
    source_path: MPL USA.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_deposit
    source_role: wallet_deposit_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_deposit
    source_role: wallet_deposit_oms
    source_entity: MPL Wallet OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: MPL proprietary deposit and withdrawal ledgers
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  card_type: account_data_binding
  canonical_name: MPL USA MPL Wallet OMS wallet_withdrawal_oms binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL Wallet OMS wallet withdrawal OMS
    - mpl_oms_withdrawal
    - zs_observe.mpl_oms_withdrawal
    - MPL proprietary deposit and withdrawal ledgers
    - MPL USA MPL Wallet OMS wallet withdrawal OMS
    colloquial_phrases:
    - MPL USA MPL Wallet OMS wallet withdrawal OMS source
    - MPL Wallet OMS wallet withdrawal OMS runtime binding
    - mpl_oms_withdrawal for MPL USA
    business_meaning: This account-data binding tells the resolver that MPL USA's MPL Wallet OMS wallet withdrawal
      OMS evidence should use zs_observe.mpl_oms_withdrawal. Apply group_id=2, group_level_id=3 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which MPL Wallet OMS OMS rows should answer MPL USA's wallet withdrawal OMS question?
    - Which runtime scope must be injected before using mpl_oms_withdrawal?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - wallet_withdrawal_oms
    included_concepts:
    - zs_observe.mpl_oms_withdrawal
    - wallet withdrawal OMS
    - MPL Wallet OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=2
    - group_level_id=3
    - oms_business_kb.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - OMS rows define order or expected-side evidence; actual payment, bank, shipment, or warehouse proof must come
      from linked packs.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - platform_account_id:platform_account.mpl_usa.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:wallet_withdrawal_oms
    - table_id:table.zs_observe.mpl_oms_withdrawal
    - runtime_source_family:oms
    embedding_text: 'For MPL USA, the MPL Wallet OMS wallet withdrawal OMS binding selects zs_observe.mpl_oms_withdrawal
      as OMS evidence. Scope: group_id=2, group_level_id=3. Reusable semantics come from oms_business_kb.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - MPL USA
    - MPL Wallet OMS
    - wallet withdrawal OMS
    - OMS
    - zs_observe.mpl_oms_withdrawal
    - mpl_oms_withdrawal
    - wallet_withdrawal_oms
    - oms_business_kb.md
    - group_id=2
    - group_level_id=3
    exact_match_keys:
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  evidence:
    source_documents:
    - MPL USA.docx
    - oms_business_kb.md
    source_path: MPL USA.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_withdrawal
    source_role: wallet_withdrawal_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_withdrawal
    source_role: wallet_withdrawal_oms
    source_entity: MPL Wallet OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: MPL proprietary deposit and withdrawal ledgers
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.5 Business Scope Set Cards

#### business_scope_set.mpl_usa.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.mpl_usa.oms
  card_type: business_scope_set
  canonical_name: MPL USA OMS runtime scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL USA OMS runtime scope
    - MPL USA OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - MPL USA OMS scope
    - OMS accounts and bindings
    - MPL USA OMS resolver input
    business_meaning: Business scope set for MPL USA's OMS runtime resolution. It groups 1 platform accounts and
      2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for MPL USA?
    - Which runtime table bindings should be considered together under MPL USA OMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 0 deferred sources
    excluded_concepts:
    - table schema definitions
    - metric implementations
    - unbound client sources
    caveats:
    - A scope set is a resolver grouping; individual account-data-binding cards still control exact table selection
      and filters.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_scope_set
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - runtime_source_family:oms
    embedding_text: MPL USA OMS runtime scope groups MPL USA's OMS runtime accounts and table bindings. Use it to
      restrict traversal to the client's configured sources; unresolved sources remain deferred until supported
      canonical packs exist.
    search_keywords:
    - MPL USA
    - MPL USA OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.mpl_usa.oms
  evidence:
    source_documents:
    - client DOCX files
    - oms_business_kb.md
    - shopify_d2c_oms.md
    source_path: client DOCX files plus uploaded OMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.mpl_usa.oms
  fields:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    binding_name: MPL USA OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.mpl_usa.oms
    account_data_binding_ids:
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    participating_accounts:
    - platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
      account_name: MPL USA MPL Wallet OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
      source_role: wallet_deposit_oms
      table_id: table.zs_observe.mpl_oms_deposit
      domain_id: domain.oms_business.mpl_wallet
    - account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
      source_role: wallet_withdrawal_oms
      table_id: table.zs_observe.mpl_oms_withdrawal
      domain_id: domain.oms_business.mpl_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.6 Business Flow Binding Cards

#### business_flow_binding.mpl_usa.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: MPL USA OMS runtime resolution flow
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: MPL USA
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL USA OMS runtime resolution flow
    - MPL USA OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - MPL USA OMS resolution flow
    - OMS source routing
    - MPL USA runtime traversal plan
    business_meaning: Business flow binding for MPL USA's OMS source resolution. It connects the scope set to 1
      platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence before reusable
      semantics run.
    business_questions:
    - Which OMS bindings should be traversed for MPL USA's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - OMS
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - documented source flow paths
    excluded_concepts:
    - SQL formulas
    - domain metrics
    - unconfigured source inference
    caveats:
    - Use this flow after resolving tenant and group scope; unsupported sources must stay deferred until their canonical
      packs are available.
    examples: []
  retrieval:
    node_sets:
    - card_type:business_flow_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_usa
    - group_id:group.mpl_usa.g2.gl3
    - runtime_source_family:oms
    embedding_text: MPL USA OMS runtime resolution flow is MPL USA's OMS runtime traversal binding. It connects
      the business scope set to account and table bindings so retrieval selects client evidence first and then delegates
      semantics to external canonical packs.
    search_keywords:
    - MPL USA
    - MPL USA OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.mpl_usa.oms_runtime_resolution
  evidence:
    source_documents:
    - client DOCX files
    - oms_business_kb.md
    - shopify_d2c_oms.md
    source_path: client DOCX files plus uploaded OMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  fields:
    tenant_id: tenant.mpl_usa
    group_id: group.mpl_usa.g2.gl3
    binding_name: MPL USA OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.mpl_usa.oms
    account_data_binding_ids:
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    - account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    participating_accounts:
    - platform_account_id: platform_account.mpl_usa.mpl_wallet_oms.oms
      account_name: MPL USA MPL Wallet OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
      source_role: wallet_deposit_oms
      table_id: table.zs_observe.mpl_oms_deposit
      domain_id: domain.oms_business.mpl_wallet
    - account_data_binding_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
      source_role: wallet_withdrawal_oms
      table_id: table.zs_observe.mpl_oms_withdrawal
      domain_id: domain.oms_business.mpl_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: column.zs_observe.mpl_oms_deposit.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: column.zs_observe.mpl_oms_deposit.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: column.zs_observe.mpl_oms_withdrawal.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: column.zs_observe.mpl_oms_withdrawal.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_belongs_to_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_belongs_to_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_belongs_to_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_belongs_to_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_deposit
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: table.zs_observe.mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_withdrawal
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: table.zs_observe.mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_usa_g2_gl3

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_usa_g2_gl3
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  target_card_id: group.mpl_usa.g2.gl3
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  target_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_usa_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_usa_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_usa_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  target_card_id: business_scope_set.mpl_usa.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_belongs_to_group.group_mpl_usa_g2_gl3

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_belongs_to_group.group_mpl_usa_g2_gl3
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: group.mpl_usa.g2.gl3
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_usa_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_usa.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_mpl_usa_g2_gl3.group_belongs_to_tenant.tenant_mpl_usa

```yaml
canonical_edge:
  edge_id: edge.group_mpl_usa_g2_gl3.group_belongs_to_tenant.tenant_mpl_usa
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.mpl_usa.g2.gl3
  target_card_id: tenant.mpl_usa
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_mpl_usa_g2_gl3.group_has_business_flow_binding.business_flow_binding_mpl_usa_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_mpl_usa_g2_gl3.group_has_business_flow_binding.business_flow_binding_mpl_usa_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.mpl_usa.g2.gl3
  target_card_id: business_flow_binding.mpl_usa.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_mpl_usa_g2_gl3.group_has_business_scope_set.business_scope_set_mpl_usa_oms

```yaml
canonical_edge:
  edge_id: edge.group_mpl_usa_g2_gl3.group_has_business_scope_set.business_scope_set_mpl_usa_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.mpl_usa.g2.gl3
  target_card_id: business_scope_set.mpl_usa.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_mpl_usa_g2_gl3.group_has_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.group_mpl_usa_g2_gl3.group_has_platform_account.platform_account_mpl_usa_mpl_wallet_oms_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_usa.g2.gl3
  target_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_belongs_to_group.group_mpl_usa_g2_gl3

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_belongs_to_group.group_mpl_usa_g2_gl3
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  target_card_id: group.mpl_usa.g2.gl3
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_usa_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  target_card_id: account_data_binding.mpl_usa.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_usa_mpl_wallet_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_usa.mpl_wallet_oms.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### TENANT_HAS_GROUP

#### edge.tenant_mpl_usa.tenant_has_group.group_mpl_usa_g2_gl3

```yaml
canonical_edge:
  edge_id: edge.tenant_mpl_usa.tenant_has_group.group_mpl_usa_g2_gl3
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.mpl_usa
  target_card_id: group.mpl_usa.g2.gl3
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```
