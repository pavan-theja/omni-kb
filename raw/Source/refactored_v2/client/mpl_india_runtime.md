# Mpl India — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `mpl_india_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Yes Bank pay-in
  config: yesbank_oms_payin
  reason: No yesbank_oms_payin canonical table in uploaded payment_gateway.md or bank_statement.md; only yesbank_oms_payout
    is present in bank_statement.md
  source_family: payment_gateway
- label: Yes Biz
  config: yes_biz_payin
  reason: No Yes Biz canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 8
  account_data_binding: 12
  business_scope_set: 3
  business_flow_binding: 3
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 4
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 12
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 12
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 3
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 12
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 8
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 3
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 3
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 12
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 8
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 8
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 8
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 3
  GROUP_HAS_BUSINESS_SCOPE_SET: 3
  GROUP_HAS_PLATFORM_ACCOUNT: 8
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 8
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 12
  PLATFORM_ACCOUNT_USES_PLATFORM: 8
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 8
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
- payment_gateway
- bank_statement
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
  added_runtime_cards: 21
  added_runtime_edges: 116
  supported_payment_bindings: 8
  supported_bank_bindings: 2
  deferred_financial_sources_added_or_updated: 2
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.mpl_india

```yaml
canonical_card:
  canonical_id: tenant.mpl_india
  card_type: tenant
  canonical_name: Mpl India
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
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India
    - mpl_india
    - Mpl India runtime tenant
    colloquial_phrases:
    - Mpl India client runtime
    - Mpl India source configuration
    - Mpl India scoped reconciliation setup
    business_meaning: Runtime tenant identity for Mpl India. It anchors the client's marketplace, logistics, OMS,
      WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to Mpl India?
    - Which group and account bindings should constrain Mpl India's SQL handoff?
    - After Mpl India's runtime scope is resolved, which domain layer should receive the query next?
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
    - tenant_id:tenant.mpl_india
    embedding_text: Mpl India is the runtime tenant root for the client's marketplace, logistics, OMS, WMS, payment-gateway,
      and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding nodes
      before invoking reusable canonical packs.
    search_keywords:
    - Mpl India
    - mpl_india
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.mpl_india
  evidence:
    source_documents:
    - MPL India.docx
    source_path: MPL India.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
  fields:
    tenant_slug: mpl_india
    tenant_name: Mpl India
    legal_name: Mpl India
    active: true
```

### 2.2 Group Cards

#### group.mpl_india.g2.gl2

```yaml
canonical_card:
  canonical_id: group.mpl_india.g2.gl2
  card_type: group
  canonical_name: Mpl India group 2/2
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
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - MPL
    - Mpl India group 2/2
    - group_id 2
    - group_level_id 2
    colloquial_phrases:
    - Mpl India group scope
    - MPL runtime scope
    - group 2 level 2 query boundary
    business_meaning: 'Runtime group scope for Mpl India: group_id=2 and group_level_id=2. It is the client-specific
      filter boundary that must be applied before resolving account bindings for IN in INR.'
    business_questions:
    - Which bindings use group_id=2 and group_level_id=2?
    - Which source families are active under MPL?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=2
    - group_level_id=2
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - group_id_value:2
    - group_level_id_value:2
    embedding_text: MPL is the runtime group node for Mpl India. Apply group_id=2 and group_level_id=2 when traversing
      from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Mpl India
    - MPL
    - group_id 2
    - group_level_id 2
    - runtime group scope
    exact_match_keys:
    - group.mpl_india.g2.gl2
  evidence:
    source_documents:
    - MPL India.docx
    source_path: MPL India.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    group_level_id: '2'
  fields:
    tenant_id: tenant.mpl_india
    group_id_value: '2'
    group_level_id_value: '2'
    group_name: MPL
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.mpl_india.mpl_wallet_oms.oms

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.mpl_wallet_oms.oms
  card_type: platform_account
  canonical_name: Mpl India MPL Wallet OMS account
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
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India MPL Wallet OMS account
    - Mpl India Mpl India MPL Wallet OMS account
    - Zenstatement Oms Business Kb
    - Mpl India MPL Wallet OMS account OMS account
    colloquial_phrases:
    - Mpl India Mpl India MPL Wallet OMS account source account
    - Mpl India MPL Wallet OMS account OMS runtime account
    - Mpl India MPL Wallet OMS account configured source family
    business_meaning: Runtime platform account for Mpl India's Mpl India MPL Wallet OMS account OMS sources. It
      points traversal to platform.zenstatement_oms_business_kb and platform_context.zenstatement.oms_business_kb
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Mpl India MPL Wallet OMS account table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's Mpl India MPL Wallet OMS account questions traverse through?
    - Which source roles under Mpl India MPL Wallet OMS account are active or review-required for this client?
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Mpl India's Mpl India MPL Wallet OMS account platform account routes OMS questions to platform.zenstatement_oms_business_kb
      / platform_context.zenstatement.oms_business_kb. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Mpl India
    - Mpl India MPL Wallet OMS account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.mpl_india.mpl_wallet_oms.oms
  evidence:
    source_documents:
    - MPL India.docx
    - oms_business_kb.md
    source_path: MPL India.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Mpl India MPL Wallet OMS account
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
      group_level_id: '2'
```

#### platform_account.mpl_india.razorpay.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.razorpay.payment_gateway
  card_type: platform_account
  canonical_name: Mpl India — Razorpay payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay
    - Mpl India Razorpay
    - Razorpay payment gateway account
    colloquial_phrases:
    - Mpl India Razorpay source account
    - Razorpay payment gateway runtime account
    - Razorpay configured source family
    business_meaning: Runtime platform account for Mpl India's Razorpay payment gateway sources. It points traversal
      to platform.razorpay and platform_context.razorpay.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Razorpay table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's Razorpay questions traverse through?
    - Which source roles under Razorpay are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Razorpay'
    - platform.razorpay
    - platform_context.razorpay.in
    - Razorpay
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - platform_account_id:platform_account.mpl_india.razorpay.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India's Razorpay platform account routes payment gateway questions to platform.razorpay
      / platform_context.razorpay.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Mpl India
    - Razorpay
    - payment gateway
    - platform.razorpay
    - platform_context.razorpay.in
    exact_match_keys:
    - platform_account.mpl_india.razorpay.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    account_name: Razorpay
    account_type: payment_gateway_account
    source_account_identifier: Razorpay
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.cashfree.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.cashfree.payment_gateway
  card_type: platform_account
  canonical_name: Mpl India — Cashfree payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree
    - Mpl India Cashfree
    - Cashfree payment gateway account
    colloquial_phrases:
    - Mpl India Cashfree source account
    - Cashfree payment gateway runtime account
    - Cashfree configured source family
    business_meaning: Runtime platform account for Mpl India's Cashfree payment gateway sources. It points traversal
      to platform.cashfree and platform_context.cashfree.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Cashfree table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's Cashfree questions traverse through?
    - Which source roles under Cashfree are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Cashfree'
    - platform.cashfree
    - platform_context.cashfree.in
    - Cashfree
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - platform_account_id:platform_account.mpl_india.cashfree.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India's Cashfree platform account routes payment gateway questions to platform.cashfree
      / platform_context.cashfree.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Mpl India
    - Cashfree
    - payment gateway
    - platform.cashfree
    - platform_context.cashfree.in
    exact_match_keys:
    - platform_account.mpl_india.cashfree.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    account_name: Cashfree
    account_type: payment_gateway_account
    source_account_identifier: Cashfree
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.paytm.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.paytm.payment_gateway
  card_type: platform_account
  canonical_name: Mpl India — Paytm payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Paytm
    - Mpl India Paytm
    - Paytm payment gateway account
    colloquial_phrases:
    - Mpl India Paytm source account
    - Paytm payment gateway runtime account
    - Paytm configured source family
    business_meaning: Runtime platform account for Mpl India's Paytm payment gateway sources. It points traversal
      to platform.paytm and platform_context.paytm.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Paytm table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's Paytm questions traverse through?
    - Which source roles under Paytm are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: Paytm'
    - platform.paytm
    - platform_context.paytm.in
    - Paytm
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.paytm
    - platform_context_id:platform_context.paytm.in
    - platform_account_id:platform_account.mpl_india.paytm.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India's Paytm platform account routes payment gateway questions to platform.paytm / platform_context.paytm.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Mpl India
    - Paytm
    - payment gateway
    - platform.paytm
    - platform_context.paytm.in
    exact_match_keys:
    - platform_account.mpl_india.paytm.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    platform_account_id: platform_account.mpl_india.paytm.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    account_name: Paytm
    account_type: payment_gateway_account
    source_account_identifier: Paytm
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.phonepe.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.phonepe.payment_gateway
  card_type: platform_account
  canonical_name: Mpl India — PhonePe payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - PhonePe
    - Mpl India PhonePe
    - PhonePe payment gateway account
    colloquial_phrases:
    - Mpl India PhonePe source account
    - PhonePe payment gateway runtime account
    - PhonePe configured source family
    business_meaning: Runtime platform account for Mpl India's PhonePe payment gateway sources. It points traversal
      to platform.phonepe and platform_context.phonepe.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which PhonePe table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's PhonePe questions traverse through?
    - Which source roles under PhonePe are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: PhonePe'
    - platform.phonepe
    - platform_context.phonepe.in
    - PhonePe
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.phonepe
    - platform_context_id:platform_context.phonepe.in
    - platform_account_id:platform_account.mpl_india.phonepe.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India's PhonePe platform account routes payment gateway questions to platform.phonepe /
      platform_context.phonepe.in. Use it to collect the client's table bindings; do not use this account card as
      a table or metric definition.
    search_keywords:
    - Mpl India
    - PhonePe
    - payment gateway
    - platform.phonepe
    - platform_context.phonepe.in
    exact_match_keys:
    - platform_account.mpl_india.phonepe.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    platform_account_id: platform_account.mpl_india.phonepe.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    account_name: PhonePe
    account_type: payment_gateway_account
    source_account_identifier: PhonePe
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.rbl_bank_oms.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  card_type: platform_account
  canonical_name: Mpl India — RBL Bank OMS payment gateway
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - RBL Bank OMS
    - Mpl India RBL Bank OMS
    - RBL Bank
    - RBL Bank OMS payment gateway account
    colloquial_phrases:
    - Mpl India RBL Bank OMS source account
    - RBL Bank OMS payment gateway runtime account
    - RBL Bank OMS configured source family
    business_meaning: Runtime platform account for Mpl India's RBL Bank OMS payment gateway sources. It points traversal
      to platform.rbl_bank and platform_context.rbl_bank.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which RBL Bank OMS table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's RBL Bank OMS questions traverse through?
    - Which source roles under RBL Bank OMS are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: RBL Bank OMS'
    - platform.rbl_bank
    - platform_context.rbl_bank.in
    - RBL Bank OMS
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.rbl_bank
    - platform_context_id:platform_context.rbl_bank.in
    - platform_account_id:platform_account.mpl_india.rbl_bank_oms.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India's RBL Bank OMS platform account routes payment gateway questions to platform.rbl_bank
      / platform_context.rbl_bank.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Mpl India
    - RBL Bank OMS
    - RBL Bank
    - payment gateway
    - platform.rbl_bank
    - platform_context.rbl_bank.in
    exact_match_keys:
    - platform_account.mpl_india.rbl_bank_oms.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.rbl_bank
    platform_context_id: platform_context.rbl_bank.in
    platform_account_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.rbl_bank
    platform_context_id: platform_context.rbl_bank.in
    account_name: RBL Bank OMS
    account_type: direct_bank_payin_account
    source_account_identifier: RBL Bank OMS
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.idfc_bank.bank_statement

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.idfc_bank.bank_statement
  card_type: platform_account
  canonical_name: Mpl India — IDFC First Bank bank statement
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - IDFC First Bank
    - Mpl India IDFC First Bank
    - IDFC First Bank bank statement account
    colloquial_phrases:
    - Mpl India IDFC First Bank source account
    - IDFC First Bank bank statement runtime account
    - IDFC First Bank configured source family
    business_meaning: Runtime platform account for Mpl India's IDFC First Bank bank statement sources. It points
      traversal to platform.idfc_first_bank and platform_context.idfc_first_bank.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which IDFC First Bank table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's IDFC First Bank questions traverse through?
    - Which source roles under IDFC First Bank are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - bank_statement
    - source_router
    included_concepts:
    - 'client configuration: IDFC First Bank'
    - platform.idfc_first_bank
    - platform_context.idfc_first_bank.in
    - IDFC First Bank
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.idfc_first_bank
    - platform_context_id:platform_context.idfc_first_bank.in
    - platform_account_id:platform_account.mpl_india.idfc_bank.bank_statement
    - runtime_source_family:bank_statement
    embedding_text: Mpl India's IDFC First Bank platform account routes bank statement questions to platform.idfc_first_bank
      / platform_context.idfc_first_bank.in. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Mpl India
    - IDFC First Bank
    - bank statement
    - platform.idfc_first_bank
    - platform_context.idfc_first_bank.in
    exact_match_keys:
    - platform_account.mpl_india.idfc_bank.bank_statement
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: MPL India.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.idfc_first_bank
    platform_context_id: platform_context.idfc_first_bank.in
    platform_account_id: platform_account.mpl_india.idfc_bank.bank_statement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.idfc_first_bank
    platform_context_id: platform_context.idfc_first_bank.in
    account_name: IDFC First Bank
    account_type: bank_statement_account
    source_account_identifier: IDFC First Bank
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: bank_statement
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: bank_statement.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```

#### platform_account.mpl_india.yes_bank.bank_statement

```yaml
canonical_card:
  canonical_id: platform_account.mpl_india.yes_bank.bank_statement
  card_type: platform_account
  canonical_name: Mpl India — Yes Bank bank statement
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Yes Bank
    - Mpl India Yes Bank
    - Yes Bank bank statement account
    colloquial_phrases:
    - Mpl India Yes Bank source account
    - Yes Bank bank statement runtime account
    - Yes Bank configured source family
    business_meaning: Runtime platform account for Mpl India's Yes Bank bank statement sources. It points traversal
      to platform.yes_bank and platform_context.yes_bank.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Yes Bank table bindings are available for Mpl India?
    - Which canonical platform/context should Mpl India's Yes Bank questions traverse through?
    - Which source roles under Yes Bank are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - bank_statement
    - source_router
    included_concepts:
    - 'client configuration: Yes Bank'
    - platform.yes_bank
    - platform_context.yes_bank.in
    - Yes Bank
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_id:platform.yes_bank
    - platform_context_id:platform_context.yes_bank.in
    - platform_account_id:platform_account.mpl_india.yes_bank.bank_statement
    - runtime_source_family:bank_statement
    embedding_text: Mpl India's Yes Bank platform account routes bank statement questions to platform.yes_bank /
      platform_context.yes_bank.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Mpl India
    - Yes Bank
    - bank statement
    - platform.yes_bank
    - platform_context.yes_bank.in
    exact_match_keys:
    - platform_account.mpl_india.yes_bank.bank_statement
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: MPL India.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.yes_bank
    platform_context_id: platform_context.yes_bank.in
    platform_account_id: platform_account.mpl_india.yes_bank.bank_statement
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_id: platform.yes_bank
    platform_context_id: platform_context.yes_bank.in
    account_name: Yes Bank
    account_type: bank_statement_account
    source_account_identifier: Yes Bank
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: bank_statement
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: bank_statement.md
    group_scope_values:
      group_id: '2'
      group_level_id: '2'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  card_type: account_data_binding
  canonical_name: Mpl India MPL Wallet OMS wallet_deposit_oms binding
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
    vendor_or_system: Mpl India
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
    - Mpl India MPL Wallet OMS wallet deposit OMS
    colloquial_phrases:
    - Mpl India MPL Wallet OMS wallet deposit OMS source
    - MPL Wallet OMS wallet deposit OMS runtime binding
    - mpl_oms_deposit for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's MPL Wallet OMS wallet deposit
      OMS evidence should use zs_observe.mpl_oms_deposit. Apply group_id=2, group_level_id=2 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which MPL Wallet OMS OMS rows should answer Mpl India's wallet deposit OMS question?
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
    - group_level_id=2
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:wallet_deposit_oms
    - table_id:table.zs_observe.mpl_oms_deposit
    - runtime_source_family:oms
    embedding_text: 'For Mpl India, the MPL Wallet OMS wallet deposit OMS binding selects zs_observe.mpl_oms_deposit
      as OMS evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from oms_business_kb.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - MPL Wallet OMS
    - wallet deposit OMS
    - OMS
    - zs_observe.mpl_oms_deposit
    - mpl_oms_deposit
    - wallet_deposit_oms
    - oms_business_kb.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  evidence:
    source_documents:
    - MPL India.docx
    - oms_business_kb.md
    source_path: MPL India.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_deposit
    source_role: wallet_deposit_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
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

#### account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  card_type: account_data_binding
  canonical_name: Mpl India MPL Wallet OMS wallet_withdrawal_oms binding
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
    vendor_or_system: Mpl India
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
    - Mpl India MPL Wallet OMS wallet withdrawal OMS
    colloquial_phrases:
    - Mpl India MPL Wallet OMS wallet withdrawal OMS source
    - MPL Wallet OMS wallet withdrawal OMS runtime binding
    - mpl_oms_withdrawal for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's MPL Wallet OMS wallet withdrawal
      OMS evidence should use zs_observe.mpl_oms_withdrawal. Apply group_id=2, group_level_id=2 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which MPL Wallet OMS OMS rows should answer Mpl India's wallet withdrawal OMS question?
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
    - group_level_id=2
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.mpl_wallet_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:wallet_withdrawal_oms
    - table_id:table.zs_observe.mpl_oms_withdrawal
    - runtime_source_family:oms
    embedding_text: 'For Mpl India, the MPL Wallet OMS wallet withdrawal OMS binding selects zs_observe.mpl_oms_withdrawal
      as OMS evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from oms_business_kb.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - MPL Wallet OMS
    - wallet withdrawal OMS
    - OMS
    - zs_observe.mpl_oms_withdrawal
    - mpl_oms_withdrawal
    - wallet_withdrawal_oms
    - oms_business_kb.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  evidence:
    source_documents:
    - MPL India.docx
    - oms_business_kb.md
    source_path: MPL India.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    domain_id: domain.oms_business.mpl_wallet
    table_id: table.zs_observe.mpl_oms_withdrawal
    source_role: wallet_withdrawal_oms
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
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

#### account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  card_type: account_data_binding
  canonical_name: Mpl India Razorpay wallet deposit pay-in binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay settlement
    - razorpay_payin
    - zs_observe.razorpay_payin
    - Mpl India Razorpay settlement
    colloquial_phrases:
    - Mpl India Razorpay settlement source
    - Razorpay settlement runtime binding
    - razorpay_payin for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Razorpay settlement evidence
      should use zs_observe.razorpay_payin. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Razorpay settlement rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying razorpay_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.razorpay_payin
    - settlement
    - Razorpay
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.razorpay.payment_gateway
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.razorpay_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Razorpay settlement binding selects zs_observe.razorpay_payin as payment
      gateway evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Razorpay
    - settlement
    - payment gateway
    - zs_observe.razorpay_payin
    - razorpay_payin
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    canonical_table_id: table.zs_observe.razorpay_payin
    physical_table_reference: zs_observe.razorpay_payin
    configured_pipeline_target: razorpay_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: wallet deposit pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - settlement_id
    - arn
    - settlement_utr
    - utr
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - fee
    - tax
    - settled_amount
    - sale_type
    - cards_network
    - settlement_utr
    - settled_at
    - settled_by
    - debit
    - credit
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  card_type: account_data_binding
  canonical_name: Mpl India Razorpay winnings withdrawal payout binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay payout
    - razorpay_payout
    - zs_observe.razorpay_payout
    - Mpl India Razorpay payout
    colloquial_phrases:
    - Mpl India Razorpay payout source
    - Razorpay payout runtime binding
    - razorpay_payout for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Razorpay payout evidence should
      use zs_observe.razorpay_payout. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Razorpay payout rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying razorpay_payout?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - payout
    included_concepts:
    - zs_observe.razorpay_payout
    - payout
    - Razorpay
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.razorpay.payment_gateway
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - domain_id:domain.payment_gateway.payout
    - table_id:table.zs_observe.razorpay_payout
    - source_role:payout
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Razorpay payout binding selects zs_observe.razorpay_payout as payment gateway
      evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Razorpay
    - payout
    - payment gateway
    - zs_observe.razorpay_payout
    - razorpay_payout
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.razorpay_payout
    source_role: payout
    account_data_binding_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.razorpay_payout
    canonical_table_id: table.zs_observe.razorpay_payout
    physical_table_reference: zs_observe.razorpay_payout
    configured_pipeline_target: razorpay_payout
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: payout
    source_role_label: winnings withdrawal payout
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - payout_id
    - utr
    - reference_id
    amount_columns_from_reusable_pack:
    - amount
    - fees
    - tax
    - settled_amount
    grain_from_reusable_pack: one row per payout/transfer event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  card_type: account_data_binding
  canonical_name: Mpl India Cashfree wallet deposit pay-in binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree settlement
    - cashfree_payin
    - zs_observe.cashfree_payin
    - Mpl India Cashfree settlement
    colloquial_phrases:
    - Mpl India Cashfree settlement source
    - Cashfree settlement runtime binding
    - cashfree_payin for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Cashfree settlement evidence
      should use zs_observe.cashfree_payin. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Cashfree settlement rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying cashfree_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.cashfree_payin
    - settlement
    - Cashfree
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.cashfree.payment_gateway
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.cashfree_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Cashfree settlement binding selects zs_observe.cashfree_payin as payment
      gateway evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Cashfree
    - settlement
    - payment gateway
    - zs_observe.cashfree_payin
    - cashfree_payin
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    canonical_table_id: table.zs_observe.cashfree_payin
    physical_table_reference: zs_observe.cashfree_payin
    configured_pipeline_target: cashfree_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: wallet deposit pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - cashfree_reference_id
    - merchant_reference_id
    - customer_reference_id
    - settlement_id
    - refund_arn
    - utr
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - event_amount
    - transaction_amount
    - transaction_service_charge
    - fee
    - tax
    - txn_st_gst
    - net_settlement_amount
    - event_settlement_amount
    - settled_amount
    - refund_arn
    - refund_type
    - credit_ref_no
    - redemption_amount
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  card_type: account_data_binding
  canonical_name: Mpl India Cashfree payout and fee/charge tracking binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree payout
    - cashfree_expense_report
    - zs_observe.cashfree_expense_report
    - cashfree_payout / cashfree fee report
    - Mpl India Cashfree payout
    colloquial_phrases:
    - Mpl India Cashfree payout source
    - Cashfree payout runtime binding
    - cashfree_expense_report for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Cashfree payout evidence should
      use zs_observe.cashfree_expense_report. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Cashfree payout rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying cashfree_expense_report?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - payout
    included_concepts:
    - zs_observe.cashfree_expense_report
    - payout
    - Cashfree
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.cashfree.payment_gateway
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - domain_id:domain.payment_gateway.payout
    - table_id:table.zs_observe.cashfree_expense_report
    - source_role:payout
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Cashfree payout binding selects zs_observe.cashfree_expense_report as payment
      gateway evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Cashfree
    - payout
    - payment gateway
    - zs_observe.cashfree_expense_report
    - cashfree_expense_report
    - cashfree_payout / cashfree fee report
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.cashfree_expense_report
    source_role: payout
    account_data_binding_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.cashfree_expense_report
    canonical_table_id: table.zs_observe.cashfree_expense_report
    physical_table_reference: zs_observe.cashfree_expense_report
    configured_pipeline_target: cashfree_payout / cashfree fee report
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: payout
    source_role_label: Cashfree payout and fee/charge tracking
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - added_on
    - added_on_1
    business_keys_from_reusable_pack:
    - reference_id
    - bank_ref_no
    - extended_utr
    amount_columns_from_reusable_pack:
    - amount
    - service_charge
    - service_tax
    - pg_fee
    - pg_tax
    - charge_amount
    grain_from_reusable_pack: one row per payout/transfer event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  card_type: account_data_binding
  canonical_name: Mpl India Paytm wallet deposit pay-in binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Paytm settlement
    - paytm_payin
    - zs_observe.paytm_payin
    - Mpl India Paytm settlement
    colloquial_phrases:
    - Mpl India Paytm settlement source
    - Paytm settlement runtime binding
    - paytm_payin for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Paytm settlement evidence should
      use zs_observe.paytm_payin. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Paytm settlement rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying paytm_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.paytm_payin
    - settlement
    - Paytm
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.paytm.payment_gateway
    - platform_id:platform.paytm
    - platform_context_id:platform_context.paytm.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.paytm_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Paytm settlement binding selects zs_observe.paytm_payin as payment gateway
      evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Paytm
    - settlement
    - payment gateway
    - zs_observe.paytm_payin
    - paytm_payin
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paytm_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paytm_payin
    canonical_table_id: table.zs_observe.paytm_payin
    physical_table_reference: zs_observe.paytm_payin
    configured_pipeline_target: paytm_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: wallet deposit pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    - transaction_date
    - payout_date
    business_keys_from_reusable_pack:
    - transaction_id
    - payout_id
    - settlement_id
    - bank_transaction_id
    - utr_no
    - rrn
    - reference_no
    - reference_transaction_id
    - split_transaction_id
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - fee
    - tax
    - gst
    - commission
    - settled_amount
    - txn_amount
    - bill_amount
    - card_network
    - settlement_type
    - discount_amount
    - subvention_amount
    - loan_amount
    - bank_offer_cashback
    - protection_plan_amount
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  card_type: account_data_binding
  canonical_name: Mpl India Paytm winnings withdrawal payout binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Paytm payout
    - paytm_payout
    - zs_observe.paytm_payout
    - Mpl India Paytm payout
    colloquial_phrases:
    - Mpl India Paytm payout source
    - Paytm payout runtime binding
    - paytm_payout for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Paytm payout evidence should
      use zs_observe.paytm_payout. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Paytm payout rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying paytm_payout?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - payout
    included_concepts:
    - zs_observe.paytm_payout
    - payout
    - Paytm
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.paytm.payment_gateway
    - platform_id:platform.paytm
    - platform_context_id:platform_context.paytm.in
    - domain_id:domain.payment_gateway.payout
    - table_id:table.zs_observe.paytm_payout
    - source_role:payout
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the Paytm payout binding selects zs_observe.paytm_payout as payment gateway
      evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Paytm
    - payout
    - payment gateway
    - zs_observe.paytm_payout
    - paytm_payout
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.paytm_payout
    source_role: payout
    account_data_binding_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.paytm.payment_gateway
    platform_id: platform.paytm
    platform_context_id: platform_context.paytm.in
    domain_id: domain.payment_gateway.payout
    table_id: table.zs_observe.paytm_payout
    canonical_table_id: table.zs_observe.paytm_payout
    physical_table_reference: zs_observe.paytm_payout
    configured_pipeline_target: paytm_payout
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: payout
    source_role_label: winnings withdrawal payout
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - utr
    amount_columns_from_reusable_pack:
    - amount
    - txn_amount
    - commission_amount
    - fee
    - tax
    - settled_amount
    - credit_debit
    - closing_balance
    grain_from_reusable_pack: one row per payout/transfer event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  card_type: account_data_binding
  canonical_name: Mpl India PhonePe wallet deposit pay-in binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - PhonePe settlement
    - phonepe_payin
    - zs_observe.phonepe_payin
    - Mpl India PhonePe settlement
    colloquial_phrases:
    - Mpl India PhonePe settlement source
    - PhonePe settlement runtime binding
    - phonepe_payin for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's PhonePe settlement evidence
      should use zs_observe.phonepe_payin. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which PhonePe settlement rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying phonepe_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.phonepe_payin
    - settlement
    - PhonePe
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.phonepe.payment_gateway
    - platform_id:platform.phonepe
    - platform_context_id:platform_context.phonepe.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.phonepe_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the PhonePe settlement binding selects zs_observe.phonepe_payin as payment gateway
      evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - PhonePe
    - settlement
    - payment gateway
    - zs_observe.phonepe_payin
    - phonepe_payin
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.phonepe.payment_gateway
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.phonepe_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.phonepe.payment_gateway
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.phonepe_payin
    canonical_table_id: table.zs_observe.phonepe_payin
    physical_table_reference: zs_observe.phonepe_payin
    configured_pipeline_target: phonepe_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: wallet deposit pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - txn_date
    - settlement_date
    business_keys_from_reusable_pack:
    - transaction_id
    - phonepereferenceid
    - merchantreferenceid
    - settlement_id
    - bankreferenceno
    - transactionutr
    - originalmerchantreferenceid
    - a_provider_reference
    - a_payment_resp_reference
    - a_operator_reference
    - a_refund_req_reference
    - a_reference_id
    amount_columns_from_reusable_pack:
    - settlement_id
    - amount
    - fee
    - tax
    - cgst
    - sgst
    - igst
    - settled_amount
    - sale_type
    - credit
    - a_baseamount
    - a_refund_req_reference
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  card_type: account_data_binding
  canonical_name: Mpl India RBL Bank OMS direct bank OMS-labelled pay-in binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - RBL Bank OMS bank statement
    - rbl_oms_payin
    - zs_observe.rbl_oms_payin
    - Mpl India RBL Bank OMS bank statement
    colloquial_phrases:
    - Mpl India RBL Bank OMS bank statement source
    - RBL Bank OMS bank statement runtime binding
    - rbl_oms_payin for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's RBL Bank OMS bank statement
      evidence should use zs_observe.rbl_oms_payin. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which RBL Bank OMS bank statement rows represent expected gateway evidence for Mpl India?
    - Which merchant/account filters are still needed before querying rbl_oms_payin?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - bank_statement
    included_concepts:
    - zs_observe.rbl_oms_payin
    - bank statement
    - RBL Bank OMS
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=2
    - group_level_id=2
    - payment_gateway.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Gateway rows are expected payment or settlement evidence; actual cash must be confirmed through a bank-statement
      binding.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.rbl_bank_oms.payment_gateway
    - platform_id:platform.rbl_bank
    - platform_context_id:platform_context.rbl_bank.in
    - domain_id:domain.payment_gateway.bank_side_evidence
    - table_id:table.zs_observe.rbl_oms_payin
    - source_role:bank_statement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Mpl India, the RBL Bank OMS bank statement binding selects zs_observe.rbl_oms_payin as
      payment gateway evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - RBL Bank OMS
    - bank statement
    - payment gateway
    - zs_observe.rbl_oms_payin
    - rbl_oms_payin
    - bank_statement
    - payment_gateway.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: MPL India.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
    platform_id: platform.rbl_bank
    platform_context_id: platform_context.rbl_bank.in
    domain_id: domain.payment_gateway.bank_side_evidence
    table_id: table.zs_observe.rbl_oms_payin
    source_role: bank_statement
    account_data_binding_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
    platform_id: platform.rbl_bank
    platform_context_id: platform_context.rbl_bank.in
    domain_id: domain.payment_gateway.bank_side_evidence
    table_id: table.zs_observe.rbl_oms_payin
    canonical_table_id: table.zs_observe.rbl_oms_payin
    physical_table_reference: zs_observe.rbl_oms_payin
    configured_pipeline_target: rbl_oms_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: bank_statement
    source_role_label: direct bank OMS-labelled pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - posted_date
    - transaction_date
    business_keys_from_reusable_pack:
    - transaction_id
    amount_columns_from_reusable_pack:
    - credit_debit
    - transaction_amount
    - balance
    grain_from_reusable_pack: one row per payin/payment/refund/adjustment gateway event
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  card_type: account_data_binding
  canonical_name: Mpl India IDFC First Bank direct bank statement reconciliation binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - IDFC First Bank bank current account
    - idfc_bank
    - zs_ingest.idfc_bank
    - Mpl India IDFC First Bank bank current account
    colloquial_phrases:
    - Mpl India IDFC First Bank bank current account source
    - IDFC First Bank bank current account runtime binding
    - idfc_bank for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's IDFC First Bank bank current
      account evidence should use zs_ingest.idfc_bank. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in bank_statement.md. It is a runtime routing bridge, not
      a reusable domain card.
    business_questions:
    - Which IDFC First Bank bank rows provide actual cash evidence for Mpl India?
    - Which account or group scope must be applied before reading idfc_bank?
    - Which gateway, marketplace, or payout binding should be matched against this bank feed?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - bank_statement
    - bank_current_account_source
    included_concepts:
    - zs_ingest.idfc_bank
    - bank current account
    - IDFC First Bank
    - actual credits/debits
    - bank references
    - cash confirmation
    - group_id=2
    - group_level_id=2
    - bank_statement.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Bank statement rows are actual cash evidence, but this binding still needs client account scope before production
      SQL.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.idfc_bank.bank_statement
    - platform_id:platform.idfc_first_bank
    - platform_context_id:platform_context.idfc_first_bank.in
    - domain_id:domain.bank_statement.core
    - table_id:table.zs_ingest.idfc_bank
    - source_role:bank_current_account_source
    - runtime_source_family:bank_statement
    embedding_text: 'For Mpl India, the IDFC First Bank bank current account binding selects zs_ingest.idfc_bank
      as bank statement evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from bank_statement.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - IDFC First Bank
    - bank current account
    - bank statement
    - zs_ingest.idfc_bank
    - idfc_bank
    - bank_current_account_source
    - bank_statement.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: MPL India.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.idfc_bank.bank_statement
    platform_id: platform.idfc_first_bank
    platform_context_id: platform_context.idfc_first_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.idfc_bank
    source_role: bank_current_account_source
    account_data_binding_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.idfc_bank.bank_statement
    platform_id: platform.idfc_first_bank
    platform_context_id: platform_context.idfc_first_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.idfc_bank
    canonical_table_id: table.zs_ingest.idfc_bank
    physical_table_reference: zs_ingest.idfc_bank
    configured_pipeline_target: idfc_bank
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: bank_current_account_source
    source_role_label: direct bank statement reconciliation
    source_family: bank_statement
    canonical_source_pack: bank_statement.md
    coverage_status: active
    active: true
    runtime_scope_status: bank_source_bound_but_account_number_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack:
    - account
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - (is_duplicated = false OR is_duplicated IS NULL)
    recommended_date_columns_from_reusable_pack:
    - date
    - postdate
    - trandate
    business_keys_from_reusable_pack:
    - transaction_id
    - description
    - user_narration
    - journal
    - teller
    - branch
    - from_to
    - transfer_acct
    - account
    amount_columns_from_reusable_pack:
    - transaction_amount
    - trnamount
    - balance
    grain_from_reusable_pack: one raw bank statement transaction row or bank-provided account movement row
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout

```yaml
canonical_card:
  canonical_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  card_type: account_data_binding
  canonical_name: Mpl India Yes Bank direct bank payout statement reconciliation binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Yes Bank bank payout statement
    - yesbank_oms_payout
    - zs_ingest.yesbank_oms_payout
    - Mpl India Yes Bank bank payout statement
    colloquial_phrases:
    - Mpl India Yes Bank bank payout statement source
    - Yes Bank bank payout statement runtime binding
    - yesbank_oms_payout for Mpl India
    business_meaning: This account-data binding tells the resolver that Mpl India's Yes Bank bank payout statement
      evidence should use zs_ingest.yesbank_oms_payout. Apply group_id=2, group_level_id=2 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in bank_statement.md. It is a runtime routing bridge, not
      a reusable domain card.
    business_questions:
    - Which Yes Bank bank rows provide actual cash evidence for Mpl India?
    - Which account or group scope must be applied before reading yesbank_oms_payout?
    - Which gateway, marketplace, or payout binding should be matched against this bank feed?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - bank_statement
    - bank_payout_source
    included_concepts:
    - zs_ingest.yesbank_oms_payout
    - bank payout statement
    - Yes Bank
    - actual credits/debits
    - bank references
    - cash confirmation
    - group_id=2
    - group_level_id=2
    - bank_statement.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Bank statement rows are actual cash evidence, but this binding still needs client account scope before production
      SQL.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - platform_account_id:platform_account.mpl_india.yes_bank.bank_statement
    - platform_id:platform.yes_bank
    - platform_context_id:platform_context.yes_bank.in
    - domain_id:domain.bank_statement.core
    - table_id:table.zs_ingest.yesbank_oms_payout
    - source_role:bank_payout_source
    - runtime_source_family:bank_statement
    embedding_text: 'For Mpl India, the Yes Bank bank payout statement binding selects zs_ingest.yesbank_oms_payout
      as bank statement evidence. Scope: group_id=2, group_level_id=2. Reusable semantics come from bank_statement.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Mpl India
    - Yes Bank
    - bank payout statement
    - bank statement
    - zs_ingest.yesbank_oms_payout
    - yesbank_oms_payout
    - bank_payout_source
    - bank_statement.md
    - group_id=2
    - group_level_id=2
    exact_match_keys:
    - account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: MPL India.docx plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.yes_bank.bank_statement
    platform_id: platform.yes_bank
    platform_context_id: platform_context.yes_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.yesbank_oms_payout
    source_role: bank_payout_source
    account_data_binding_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
    runtime_source_family: bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    platform_account_id: platform_account.mpl_india.yes_bank.bank_statement
    platform_id: platform.yes_bank
    platform_context_id: platform_context.yes_bank.in
    domain_id: domain.bank_statement.core
    table_id: table.zs_ingest.yesbank_oms_payout
    canonical_table_id: table.zs_ingest.yesbank_oms_payout
    physical_table_reference: zs_ingest.yesbank_oms_payout
    configured_pipeline_target: yesbank_oms_payout
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: bank_payout_source
    source_role_label: direct bank payout statement reconciliation
    source_family: bank_statement
    canonical_source_pack: bank_statement.md
    coverage_status: active
    active: true
    runtime_scope_status: bank_source_bound_but_account_number_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '2'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '2'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - (is_duplicated = false OR is_duplicated IS NULL)
    recommended_date_columns_from_reusable_pack:
    - date
    - posted_date
    - txn_date
    business_keys_from_reusable_pack:
    - transaction_id
    - description
    - narration
    - cod_acct_no
    - urn
    - bankreferencenumber
    - cheque_no
    amount_columns_from_reusable_pack:
    - transaction_amount
    - amount
    - running_balance
    grain_from_reusable_pack: one raw bank statement transaction row or bank-provided account movement row
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.5 Business Scope Set Cards

#### business_scope_set.mpl_india.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.mpl_india.oms
  card_type: business_scope_set
  canonical_name: Mpl India OMS runtime scope
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
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India OMS runtime scope
    - Mpl India OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Mpl India OMS scope
    - OMS accounts and bindings
    - Mpl India OMS resolver input
    business_meaning: Business scope set for Mpl India's OMS runtime resolution. It groups 1 platform accounts and
      2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for Mpl India?
    - Which runtime table bindings should be considered together under Mpl India OMS runtime scope?
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:oms
    embedding_text: Mpl India OMS runtime scope groups Mpl India's OMS runtime accounts and table bindings. Use
      it to restrict traversal to the client's configured sources; unresolved sources remain deferred until supported
      canonical packs exist.
    search_keywords:
    - Mpl India
    - Mpl India OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.mpl_india.oms
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
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.mpl_india.oms
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    binding_name: Mpl India OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.mpl_india.oms
    account_data_binding_ids:
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    participating_accounts:
    - platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
      account_name: Mpl India MPL Wallet OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
      source_role: wallet_deposit_oms
      table_id: table.zs_observe.mpl_oms_deposit
      domain_id: domain.oms_business.mpl_wallet
    - account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
      source_role: wallet_withdrawal_oms
      table_id: table.zs_observe.mpl_oms_withdrawal
      domain_id: domain.oms_business.mpl_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.mpl_india.payment_gateway

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_scope_set.mpl_india.payment_gateway
  card_type: business_scope_set
  canonical_name: Mpl India payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India payment gateway runtime scope
    - Mpl India payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - Mpl India payment gateway scope
    - payment gateway accounts and bindings
    - Mpl India payment gateway resolver input
    business_meaning: Business scope set for Mpl India's payment gateway runtime resolution. It groups 5 platform
      accounts and 8 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for Mpl India?
    - Which runtime table bindings should be considered together under Mpl India payment gateway runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - payment_gateway
    - resolver_scope
    included_concepts:
    - 5 platform accounts
    - 8 account-data bindings
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India payment gateway runtime scope groups Mpl India's payment gateway runtime accounts
      and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Mpl India
    - Mpl India payment gateway runtime scope
    - payment gateway
    - business scope set
    - 5 accounts
    - 8 bindings
    exact_match_keys:
    - business_scope_set.mpl_india.payment_gateway
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.mpl_india.payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    binding_name: Mpl India payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.mpl_india.payment_gateway
    platform_account_ids:
    - platform_account.mpl_india.cashfree.payment_gateway
    - platform_account.mpl_india.paytm.payment_gateway
    - platform_account.mpl_india.phonepe.payment_gateway
    - platform_account.mpl_india.razorpay.payment_gateway
    - platform_account.mpl_india.rbl_bank_oms.payment_gateway
    account_data_binding_ids:
    - account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
    - account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
    - account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
    - account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
    - account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
    - account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
    - account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
    included_platform_ids:
    - platform.cashfree
    - platform.paytm
    - platform.phonepe
    - platform.razorpay
    - platform.rbl_bank
    included_platform_context_ids:
    - platform_context.cashfree.in
    - platform_context.paytm.in
    - platform_context.phonepe.in
    - platform_context.razorpay.in
    - platform_context.rbl_bank.in
    source_flow_paths:
    - platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.razorpay_payout
      source_role: payout
      configured_pipeline_target: razorpay_payout
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.cashfree_expense_report
      source_role: payout
      configured_pipeline_target: cashfree_payout / cashfree fee report
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.paytm.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paytm_payin
      source_role: settlement
      configured_pipeline_target: paytm_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.paytm.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.paytm_payout
      source_role: payout
      configured_pipeline_target: paytm_payout
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.phonepe.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
      platform_id: platform.phonepe
      platform_context_id: platform_context.phonepe.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.phonepe_payin
      source_role: settlement
      configured_pipeline_target: phonepe_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
      platform_id: platform.rbl_bank
      platform_context_id: platform_context.rbl_bank.in
      domain_id: domain.payment_gateway.bank_side_evidence
      table_id: table.zs_observe.rbl_oms_payin
      source_role: bank_statement
      configured_pipeline_target: rbl_oms_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### business_scope_set.mpl_india.bank_statement

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_scope_set.mpl_india.bank_statement
  card_type: business_scope_set
  canonical_name: Mpl India bank statement runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India bank statement runtime scope
    - Mpl India bank statement scope
    - bank statement runtime scope set
    colloquial_phrases:
    - Mpl India bank statement scope
    - bank statement accounts and bindings
    - Mpl India bank statement resolver input
    business_meaning: Business scope set for Mpl India's bank statement runtime resolution. It groups 2 platform
      accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which bank statement accounts and bindings are active for Mpl India?
    - Which runtime table bindings should be considered together under Mpl India bank statement runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - bank_statement
    - resolver_scope
    included_concepts:
    - 2 platform accounts
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:bank_statement
    embedding_text: Mpl India bank statement runtime scope groups Mpl India's bank statement runtime accounts and
      table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Mpl India
    - Mpl India bank statement runtime scope
    - bank statement
    - business scope set
    - 2 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.mpl_india.bank_statement
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: client DOCX plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_scope
    evidence_ids:
    - client_runtime.bank_statement_scope
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: bank_statement
    business_scope_set_id: business_scope_set.mpl_india.bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    binding_name: Mpl India bank statement runtime scope
    binding_type: bank_statement_source_resolution
    business_scope_set_id: business_scope_set.mpl_india.bank_statement
    platform_account_ids:
    - platform_account.mpl_india.idfc_bank.bank_statement
    - platform_account.mpl_india.yes_bank.bank_statement
    account_data_binding_ids:
    - account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
    - account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
    included_platform_ids:
    - platform.idfc_first_bank
    - platform.yes_bank
    included_platform_context_ids:
    - platform_context.idfc_first_bank.in
    - platform_context.yes_bank.in
    source_flow_paths:
    - platform_account_id: platform_account.mpl_india.idfc_bank.bank_statement
      account_data_binding_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
      platform_id: platform.idfc_first_bank
      platform_context_id: platform_context.idfc_first_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.idfc_bank
      source_role: bank_current_account_source
      configured_pipeline_target: idfc_bank
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.yes_bank.bank_statement
      account_data_binding_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
      platform_id: platform.yes_bank
      platform_context_id: platform_context.yes_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.yesbank_oms_payout
      source_role: bank_payout_source
      configured_pipeline_target: yesbank_oms_payout
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.mpl_india.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.mpl_india.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Mpl India OMS runtime resolution flow
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
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India OMS runtime resolution flow
    - Mpl India OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Mpl India OMS resolution flow
    - OMS source routing
    - Mpl India runtime traversal plan
    business_meaning: Business flow binding for Mpl India's OMS source resolution. It connects the scope set to
      1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence before
      reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Mpl India's runtime question?
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:oms
    embedding_text: Mpl India OMS runtime resolution flow is Mpl India's OMS runtime traversal binding. It connects
      the business scope set to account and table bindings so retrieval selects client evidence first and then delegates
      semantics to external canonical packs.
    search_keywords:
    - Mpl India
    - Mpl India OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.mpl_india.oms_runtime_resolution
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
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.mpl_india.oms_runtime_resolution
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    binding_name: Mpl India OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.mpl_india.oms
    account_data_binding_ids:
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
    - account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
    participating_accounts:
    - platform_account_id: platform_account.mpl_india.mpl_wallet_oms.oms
      account_name: Mpl India MPL Wallet OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
      source_role: wallet_deposit_oms
      table_id: table.zs_observe.mpl_oms_deposit
      domain_id: domain.oms_business.mpl_wallet
    - account_data_binding_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
      source_role: wallet_withdrawal_oms
      table_id: table.zs_observe.mpl_oms_withdrawal
      domain_id: domain.oms_business.mpl_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.mpl_india.payment_gateway_runtime_resolution

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Mpl India payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India payment gateway runtime resolution
    - Mpl India payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - Mpl India payment gateway resolution flow
    - payment gateway source routing
    - Mpl India runtime traversal plan
    business_meaning: Business flow binding for Mpl India's payment gateway source resolution. It connects the scope
      set to 5 platform accounts and 8 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for Mpl India's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - payment_gateway
    - runtime_traversal
    included_concepts:
    - 5 platform accounts
    - 8 account-data bindings
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:payment_gateway
    embedding_text: Mpl India payment gateway runtime resolution is Mpl India's payment gateway runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - Mpl India
    - Mpl India payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - MPL India.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.mpl_india.payment_gateway
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    business_flow_binding_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.mpl_india.payment_gateway
    flow_name: Mpl India payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.mpl_india.cashfree.payment_gateway
    - platform_account.mpl_india.paytm.payment_gateway
    - platform_account.mpl_india.phonepe.payment_gateway
    - platform_account.mpl_india.razorpay.payment_gateway
    - platform_account.mpl_india.rbl_bank_oms.payment_gateway
    account_data_binding_ids:
    - account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
    - account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
    - account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
    - account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
    - account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
    - account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
    - account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
    source_flow_paths:
    - platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.razorpay_payout
      source_role: payout
      configured_pipeline_target: razorpay_payout
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.cashfree_expense_report
      source_role: payout
      configured_pipeline_target: cashfree_payout / cashfree fee report
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.paytm.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paytm_payin
      source_role: settlement
      configured_pipeline_target: paytm_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.paytm.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
      platform_id: platform.paytm
      platform_context_id: platform_context.paytm.in
      domain_id: domain.payment_gateway.payout
      table_id: table.zs_observe.paytm_payout
      source_role: payout
      configured_pipeline_target: paytm_payout
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.phonepe.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
      platform_id: platform.phonepe
      platform_context_id: platform_context.phonepe.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.phonepe_payin
      source_role: settlement
      configured_pipeline_target: phonepe_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
      account_data_binding_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
      platform_id: platform.rbl_bank
      platform_context_id: platform_context.rbl_bank.in
      domain_id: domain.payment_gateway.bank_side_evidence
      table_id: table.zs_observe.rbl_oms_payin
      source_role: bank_statement
      configured_pipeline_target: rbl_oms_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```

#### business_flow_binding.mpl_india.bank_statement_runtime_resolution

```yaml
canonical_card:
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  canonical_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Mpl India bank statement runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Mpl India
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: true
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mpl India bank statement runtime resolution
    - Mpl India bank statement flow
    - bank statement runtime resolution flow
    colloquial_phrases:
    - Mpl India bank statement resolution flow
    - bank statement source routing
    - Mpl India runtime traversal plan
    business_meaning: Business flow binding for Mpl India's bank statement source resolution. It connects the scope
      set to 2 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which bank statement bindings should be traversed for Mpl India's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - bank_statement
    - runtime_traversal
    included_concepts:
    - 2 platform accounts
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
    - tenant_id:tenant.mpl_india
    - group_id:group.mpl_india.g2.gl2
    - runtime_source_family:bank_statement
    embedding_text: Mpl India bank statement runtime resolution is Mpl India's bank statement runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - Mpl India
    - Mpl India bank statement runtime resolution
    - bank statement
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.mpl_india.bank_statement_runtime_resolution
  evidence:
    source_documents:
    - MPL India.docx
    - bank_statement.md
    source_path: client DOCX plus uploaded bank_statement.md
    source_format: client_docx_runtime_overlay_plus_reusable_bank_statement_canonical_pack
    evidence_refs:
    - client_runtime.bank_statement_flow
    evidence_ids:
    - client_runtime.bank_statement_flow
    source_line: null
  traversal:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    runtime_source_family: bank_statement
    business_flow_binding_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
    business_scope_set_id: business_scope_set.mpl_india.bank_statement
  fields:
    tenant_id: tenant.mpl_india
    group_id: group.mpl_india.g2.gl2
    business_flow_binding_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
    business_scope_set_id: business_scope_set.mpl_india.bank_statement
    flow_name: Mpl India bank statement runtime resolution
    flow_type: bank_statement_source_resolution
    platform_account_ids:
    - platform_account.mpl_india.idfc_bank.bank_statement
    - platform_account.mpl_india.yes_bank.bank_statement
    account_data_binding_ids:
    - account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
    - account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
    source_flow_paths:
    - platform_account_id: platform_account.mpl_india.idfc_bank.bank_statement
      account_data_binding_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
      platform_id: platform.idfc_first_bank
      platform_context_id: platform_context.idfc_first_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.idfc_bank
      source_role: bank_current_account_source
      configured_pipeline_target: idfc_bank
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.mpl_india.yes_bank.bank_statement
      account_data_binding_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
      platform_id: platform.yes_bank
      platform_context_id: platform_context.yes_bank.in
      domain_id: domain.bank_statement.core
      table_id: table.zs_ingest.yesbank_oms_payout
      source_role: bank_payout_source
      configured_pipeline_target: yesbank_oms_payout
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: column.zs_observe.mpl_oms_deposit.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_deposit_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: column.zs_observe.mpl_oms_deposit.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: column.zs_observe.mpl_oms_withdrawal.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_applies_scope_column.column_zs_observe_mpl_oms_withdrawal_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: column.zs_observe.mpl_oms_withdrawal.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_deposit
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  target_card_id: table.zs_observe.mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal.account_data_binding_binds_to_table.table_zs_observe_mpl_oms_withdrawal
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  target_card_id: table.zs_observe.mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  target_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  target_card_id: business_scope_set.mpl_india.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_mpl_india_oms.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_mpl_india_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_mpl_india_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_mpl_india_g2_gl2.group_belongs_to_tenant.tenant_mpl_india

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_belongs_to_tenant.tenant_mpl_india
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: tenant.mpl_india
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_flow_binding.mpl_india.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_oms

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_scope_set.mpl_india.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_mpl_wallet_oms_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_deposit_oms_zs_observe_mpl_oms_deposit
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_deposit_oms.zs_observe_mpl_oms_deposit
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_has_account_data_binding.account_data_binding_mpl_india_mpl_wallet_oms_wallet_withdrawal_oms_zs_observe_mpl_oms_withdrawal
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  target_card_id: account_data_binding.mpl_india.mpl_wallet_oms.wallet_withdrawal_oms.zs_observe_mpl_oms_withdrawal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_mpl_wallet_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.mpl_wallet_oms.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### TENANT_HAS_GROUP

#### edge.tenant_mpl_india.tenant_has_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.tenant_mpl_india.tenant_has_group.group_mpl_india_g2_gl2
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.mpl_india
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_cashfree_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  target_card_id: platform_account.mpl_india.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_cashfree_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: platform_account.mpl_india.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_idfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_idfc_bank_bank_statement
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  target_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_paytm_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  target_card_id: platform_account.mpl_india.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_paytm_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  target_card_id: platform_account.mpl_india.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_phonepe_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  target_card_id: platform_account.mpl_india.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_razorpay_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  target_card_id: platform_account.mpl_india.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_razorpay_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: platform_account.mpl_india.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  target_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_yes_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout.account_data_binding_belongs_to_platform_account.platform_account_mpl_india_yes_bank_bank_statement
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  target_card_id: platform_account.mpl_india.yes_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report.account_data_binding_binds_to_table.table_zs_observe_cashfree_expense_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report.account_data_binding_binds_to_table.table_zs_observe_cashfree_expense_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  target_card_id: table.zs_observe.cashfree_expense_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: table.zs_observe.cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank.account_data_binding_binds_to_table.table_zs_ingest_idfc_bank

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank.account_data_binding_binds_to_table.table_zs_ingest_idfc_bank
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  target_card_id: table.zs_ingest.idfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout.account_data_binding_binds_to_table.table_zs_observe_paytm_payout

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout.account_data_binding_binds_to_table.table_zs_observe_paytm_payout
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  target_card_id: table.zs_observe.paytm_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin.account_data_binding_binds_to_table.table_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin.account_data_binding_binds_to_table.table_zs_observe_paytm_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  target_card_id: table.zs_observe.paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_binds_to_table.table_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_binds_to_table.table_zs_observe_phonepe_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  target_card_id: table.zs_observe.phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout.account_data_binding_binds_to_table.table_zs_observe_razorpay_payout

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout.account_data_binding_binds_to_table.table_zs_observe_razorpay_payout
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  target_card_id: table.zs_observe.razorpay_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: table.zs_observe.razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin.account_data_binding_binds_to_table.table_zs_observe_rbl_oms_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin.account_data_binding_binds_to_table.table_zs_observe_rbl_oms_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  target_card_id: table.zs_observe.rbl_oms_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout.account_data_binding_binds_to_table.table_zs_ingest_yesbank_oms_payout

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout.account_data_binding_binds_to_table.table_zs_ingest_yesbank_oms_payout
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  target_card_id: table.zs_ingest.yesbank_oms_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_idfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_idfc_bank_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_yes_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_yes_bank_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: platform_account.mpl_india.yes_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_cashfree_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: platform_account.mpl_india.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_paytm_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: platform_account.mpl_india.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_phonepe_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: platform_account.mpl_india.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_razorpay_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: platform_account.mpl_india.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_bank_statement_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_bank_statement
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  target_card_id: business_scope_set.mpl_india.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_mpl_india_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_mpl_india_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.mpl_india.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform.platform_idfc_first_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform.platform_idfc_first_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform.idfc_first_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform.platform_yes_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform.platform_yes_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform.yes_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_cashfree
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_paytm

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_paytm
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform.paytm
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_phonepe

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_phonepe
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform.phonepe
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_razorpay
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_rbl_bank

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform.platform_rbl_bank
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform.rbl_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_account.platform_account_mpl_india_idfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_account.platform_account_mpl_india_idfc_bank_bank_statement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_account.platform_account_mpl_india_yes_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_account.platform_account_mpl_india_yes_bank_bank_statement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform_account.mpl_india.yes_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_cashfree_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_account.mpl_india.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_paytm_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_account.mpl_india.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_phonepe_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_account.mpl_india.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_razorpay_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_account.mpl_india.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_context.platform_context_idfc_first_bank_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_context.platform_context_idfc_first_bank_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform_context.idfc_first_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_context.platform_context_yes_bank_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_bank_statement.business_scope_set_includes_platform_context.platform_context_yes_bank_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.bank_statement
  target_card_id: platform_context.yes_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_paytm_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_paytm_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_context.paytm.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_phonepe_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_phonepe_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_context.phonepe.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_rbl_bank_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_mpl_india_payment_gateway.business_scope_set_includes_platform_context.platform_context_rbl_bank_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.mpl_india.payment_gateway
  target_card_id: platform_context.rbl_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_bank_statement_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_bank_statement_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_flow_binding.mpl_india.bank_statement_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_flow_binding.business_flow_binding_mpl_india_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_flow_binding.mpl_india.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_bank_statement
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_scope_set.mpl_india.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_business_scope_set.business_scope_set_mpl_india_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: business_scope_set.mpl_india.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_cashfree_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_idfc_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_idfc_bank_bank_statement
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_paytm_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_paytm_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.paytm.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_phonepe_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_razorpay_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_rbl_bank_oms_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_yes_bank_bank_statement

```yaml
canonical_edge:
  edge_id: edge.group_mpl_india_g2_gl2.group_has_platform_account.platform_account_mpl_india_yes_bank_bank_statement
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.mpl_india.g2.gl2
  target_card_id: platform_account.mpl_india.yes_bank.bank_statement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.cashfree.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.paytm.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.phonepe.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.razorpay.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_belongs_to_group.group_mpl_india_g2_gl2

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_belongs_to_group.group_mpl_india_g2_gl2
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.mpl_india.yes_bank.bank_statement
  target_card_id: group.mpl_india.g2.gl2
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_cashfree_payout_zs_observe_cashfree_expense_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.cashfree.payment_gateway
  target_card_id: account_data_binding.mpl_india.cashfree.payout.zs_observe_cashfree_expense_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.cashfree.payment_gateway
  target_card_id: account_data_binding.mpl_india.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_mpl_india_idfc_bank_bank_current_account_source_zs_ingest_idfc_bank
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  target_card_id: account_data_binding.mpl_india.idfc_bank.bank_current_account_source.zs_ingest_idfc_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_paytm_payout_zs_observe_paytm_payout
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.paytm.payment_gateway
  target_card_id: account_data_binding.mpl_india.paytm.payout.zs_observe_paytm_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_paytm_settlement_zs_observe_paytm_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.paytm.payment_gateway
  target_card_id: account_data_binding.mpl_india.paytm.settlement.zs_observe_paytm_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.phonepe.payment_gateway
  target_card_id: account_data_binding.mpl_india.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_razorpay_payout_zs_observe_razorpay_payout
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.razorpay.payment_gateway
  target_card_id: account_data_binding.mpl_india.razorpay.payout.zs_observe_razorpay_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.razorpay.payment_gateway
  target_card_id: account_data_binding.mpl_india.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_has_account_data_binding.account_data_binding_mpl_india_rbl_bank_oms_bank_statement_zs_observe_rbl_oms_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  target_card_id: account_data_binding.mpl_india.rbl_bank_oms.bank_statement.zs_observe_rbl_oms_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_has_account_data_binding.account_data_binding_mpl_india_yes_bank_bank_payout_source_zs_ingest_yesbank_oms_payout
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.mpl_india.yes_bank.bank_statement
  target_card_id: account_data_binding.mpl_india.yes_bank.bank_payout_source.zs_ingest_yesbank_oms_payout
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.cashfree.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_uses_platform.platform_idfc_first_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_uses_platform.platform_idfc_first_bank
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  target_card_id: platform.idfc_first_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_uses_platform.platform_paytm

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_uses_platform.platform_paytm
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.paytm.payment_gateway
  target_card_id: platform.paytm
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_uses_platform.platform_phonepe

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_uses_platform.platform_phonepe
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.phonepe.payment_gateway
  target_card_id: platform.phonepe
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.razorpay.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_uses_platform.platform_rbl_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_uses_platform.platform_rbl_bank
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  target_card_id: platform.rbl_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_uses_platform.platform_yes_bank

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_uses_platform.platform_yes_bank
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.mpl_india.yes_bank.bank_statement
  target_card_id: platform.yes_bank
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.cashfree.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_uses_platform_context.platform_context_idfc_first_bank_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_idfc_bank_bank_statement.platform_account_uses_platform_context.platform_context_idfc_first_bank_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.idfc_bank.bank_statement
  target_card_id: platform_context.idfc_first_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_uses_platform_context.platform_context_paytm_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_paytm_payment_gateway.platform_account_uses_platform_context.platform_context_paytm_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.paytm.payment_gateway
  target_card_id: platform_context.paytm.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_uses_platform_context.platform_context_phonepe_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_phonepe_payment_gateway.platform_account_uses_platform_context.platform_context_phonepe_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.phonepe.payment_gateway
  target_card_id: platform_context.phonepe.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.razorpay.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_uses_platform_context.platform_context_rbl_bank_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_rbl_bank_oms_payment_gateway.platform_account_uses_platform_context.platform_context_rbl_bank_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.rbl_bank_oms.payment_gateway
  target_card_id: platform_context.rbl_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_uses_platform_context.platform_context_yes_bank_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_mpl_india_yes_bank_bank_statement.platform_account_uses_platform_context.platform_context_yes_bank_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.mpl_india.yes_bank.bank_statement
  target_card_id: platform_context.yes_bank.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
