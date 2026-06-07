# Aza Fashions Private Limited — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `aza_fashions_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Bluedart
  config: Settlement + Invoice
  reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: iThink
  config: Settlement + Invoice
  reason: No iThink canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: PayU
  config: payu_settlement
  reason: No PayU canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
- label: PayGlocal
  config: payglocal_settlement
  reason: No PayGlocal canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 7
  account_data_binding: 12
  business_scope_set: 3
  business_flow_binding: 3
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 11
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 12
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 12
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 3
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 12
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 7
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 3
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 3
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 12
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 7
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 7
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 7
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 3
  GROUP_HAS_BUSINESS_SCOPE_SET: 3
  GROUP_HAS_PLATFORM_ACCOUNT: 7
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 7
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 12
  PLATFORM_ACCOUNT_USES_PLATFORM: 7
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 7
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
  added_runtime_cards: 6
  added_runtime_edges: 31
  supported_payment_bindings: 2
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 2
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.aza_fashions_private_limited

```yaml
canonical_card:
  canonical_id: tenant.aza_fashions_private_limited
  card_type: tenant
  canonical_name: Aza Fashions Private Limited
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited
    - aza_fashions_private_limited
    - Aza Fashions Private Limited runtime tenant
    colloquial_phrases:
    - Aza Fashions Private Limited client runtime
    - Aza Fashions Private Limited source configuration
    - Aza Fashions Private Limited scoped reconciliation setup
    business_meaning: Runtime tenant identity for Aza Fashions Private Limited. It anchors the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from
      reusable domain semantics.
    business_questions:
    - Which source families and configured accounts belong to Aza Fashions Private Limited?
    - Which group and account bindings should constrain Aza Fashions Private Limited's SQL handoff?
    - After Aza Fashions Private Limited's runtime scope is resolved, which domain layer should receive the query
      next?
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
    - tenant_id:tenant.aza_fashions_private_limited
    embedding_text: Aza Fashions Private Limited is the runtime tenant root for the client's marketplace, logistics,
      OMS, WMS, payment-gateway, and bank-statement configuration. Use it to reach group, platform-account, and
      account-data-binding nodes before invoking reusable canonical packs.
    search_keywords:
    - Aza Fashions Private Limited
    - aza_fashions_private_limited
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.aza_fashions_private_limited
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    source_path: Aza Fashions Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
  fields:
    tenant_slug: aza_fashions_private_limited
    tenant_name: Aza Fashions Private Limited
    legal_name: Aza Fashions Private Limited
    active: true
```

### 2.2 Group Cards

#### group.aza_fashions_private_limited.g56.gl203

```yaml
canonical_card:
  canonical_id: group.aza_fashions_private_limited.g56.gl203
  card_type: group
  canonical_name: Aza Fashions Private Limited group 56/203
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashion
    - Aza Fashions Private Limited group 56/203
    - group_id 56
    - group_level_id 203
    colloquial_phrases:
    - Aza Fashions Private Limited group scope
    - Aza Fashion runtime scope
    - group 56 level 203 query boundary
    business_meaning: 'Runtime group scope for Aza Fashions Private Limited: group_id=56 and group_level_id=203.
      It is the client-specific filter boundary that must be applied before resolving account bindings for US in
      USD.'
    business_questions:
    - Which bindings use group_id=56 and group_level_id=203?
    - Which source families are active under Aza Fashion?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - group_id_value:56
    - group_level_id_value:203
    embedding_text: Aza Fashion is the runtime group node for Aza Fashions Private Limited. Apply group_id=56 and
      group_level_id=203 when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashion
    - group_id 56
    - group_level_id 203
    - runtime group scope
    exact_match_keys:
    - group.aza_fashions_private_limited.g56.gl203
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    source_path: Aza Fashions Private Limited.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    group_level_id: '203'
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id_value: '56'
    group_level_id_value: '203'
    group_name: Aza Fashion
    default_currency: USD
    country: US
```

### 2.3 Platform Account Cards

#### platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited AZA Proprietary D2C OMS account
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited AZA Proprietary D2C OMS account
    - Aza Fashions Private Limited Aza Fashions Private Limited AZA Proprietary D2C OMS account
    - Zenstatement Oms Business Kb
    - Aza Fashions Private Limited AZA Proprietary D2C OMS account OMS account
    colloquial_phrases:
    - Aza Fashions Private Limited Aza Fashions Private Limited AZA Proprietary D2C OMS account source account
    - Aza Fashions Private Limited AZA Proprietary D2C OMS account OMS runtime account
    - Aza Fashions Private Limited AZA Proprietary D2C OMS account configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Aza Fashions Private Limited AZA
      Proprietary D2C OMS account OMS sources. It points traversal to platform.zenstatement_oms_business_kb and
      platform_context.zenstatement.oms_business_kb and groups the client's table-level account-data bindings for
      this source.
    business_questions:
    - Which Aza Fashions Private Limited AZA Proprietary D2C OMS account table bindings are available for Aza Fashions
      Private Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Aza Fashions Private Limited AZA Proprietary
      D2C OMS account questions traverse through?
    - Which source roles under Aza Fashions Private Limited AZA Proprietary D2C OMS account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: AZA sales dump, return dump, and wallet ledger flat-file sources'
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - runtime_source_family:oms
    embedding_text: Aza Fashions Private Limited's Aza Fashions Private Limited AZA Proprietary D2C OMS account
      platform account routes OMS questions to platform.zenstatement_oms_business_kb / platform_context.zenstatement.oms_business_kb.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited AZA Proprietary D2C OMS account
    - Zenstatement Oms Business Kb
    - OMS
    - platform.zenstatement_oms_business_kb
    - platform_context.zenstatement.oms_business_kb
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - oms_business_kb.md
    source_path: Aza Fashions Private Limited.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    runtime_source_family: oms
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_name: Aza Fashions Private Limited AZA Proprietary D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: AZA sales dump, return dump, and wallet ledger flat-file sources
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.delhivery.logistics

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited Delhivery Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited Delhivery Logistics account
    - Aza Fashions Private Limited Aza Fashions Private Limited Delhivery Logistics account
    - Delhivery
    - Aza Fashions Private Limited Delhivery Logistics account logistics / courier account
    colloquial_phrases:
    - Aza Fashions Private Limited Aza Fashions Private Limited Delhivery Logistics account source account
    - Aza Fashions Private Limited Delhivery Logistics account logistics / courier runtime account
    - Aza Fashions Private Limited Delhivery Logistics account configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Aza Fashions Private Limited Delhivery
      Logistics account logistics / courier sources. It points traversal to platform.delhivery and platform_context.delhivery.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Aza Fashions Private Limited Delhivery Logistics account table bindings are available for Aza Fashions
      Private Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Aza Fashions Private Limited Delhivery
      Logistics account questions traverse through?
    - Which source roles under Aza Fashions Private Limited Delhivery Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.delhivery
    - platform_context.delhivery.in
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited's Aza Fashions Private Limited Delhivery Logistics account platform
      account routes logistics / courier questions to platform.delhivery / platform_context.delhivery.in. Use it
      to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited Delhivery Logistics account
    - Delhivery
    - logistics / courier
    - platform.delhivery
    - platform_context.delhivery.in
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.delhivery.logistics
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_name: Aza Fashions Private Limited Delhivery Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.dtdc.logistics

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited DTDC Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited DTDC Logistics account
    - Aza Fashions Private Limited Aza Fashions Private Limited DTDC Logistics account
    - DTDC
    - Aza Fashions Private Limited DTDC Logistics account logistics / courier account
    colloquial_phrases:
    - Aza Fashions Private Limited Aza Fashions Private Limited DTDC Logistics account source account
    - Aza Fashions Private Limited DTDC Logistics account logistics / courier runtime account
    - Aza Fashions Private Limited DTDC Logistics account configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Aza Fashions Private Limited DTDC
      Logistics account logistics / courier sources. It points traversal to platform.dtdc and platform_context.dtdc.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Aza Fashions Private Limited DTDC Logistics account table bindings are available for Aza Fashions Private
      Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Aza Fashions Private Limited DTDC Logistics
      account questions traverse through?
    - Which source roles under Aza Fashions Private Limited DTDC Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.dtdc
    - platform_context.dtdc.in
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.dtdc.logistics
    - platform_id:platform.dtdc
    - platform_context_id:platform_context.dtdc.in
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited's Aza Fashions Private Limited DTDC Logistics account platform
      account routes logistics / courier questions to platform.dtdc / platform_context.dtdc.in. Use it to collect
      the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited DTDC Logistics account
    - DTDC
    - logistics / courier
    - platform.dtdc
    - platform_context.dtdc.in
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.dtdc.logistics
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    account_name: Aza Fashions Private Limited DTDC Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.ekart.logistics

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.ekart.logistics
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited Ekart Logistics account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited Ekart Logistics account
    - Aza Fashions Private Limited Aza Fashions Private Limited Ekart Logistics account
    - Ekart
    - Aza Fashions Private Limited Ekart Logistics account logistics / courier account
    colloquial_phrases:
    - Aza Fashions Private Limited Aza Fashions Private Limited Ekart Logistics account source account
    - Aza Fashions Private Limited Ekart Logistics account logistics / courier runtime account
    - Aza Fashions Private Limited Ekart Logistics account configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Aza Fashions Private Limited Ekart
      Logistics account logistics / courier sources. It points traversal to platform.ekart and platform_context.ekart.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Aza Fashions Private Limited Ekart Logistics account table bindings are available for Aza Fashions Private
      Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Aza Fashions Private Limited Ekart
      Logistics account questions traverse through?
    - Which source roles under Aza Fashions Private Limited Ekart Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.ekart
    - platform_context.ekart.in
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.ekart.logistics
    - platform_id:platform.ekart
    - platform_context_id:platform_context.ekart.in
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited's Aza Fashions Private Limited Ekart Logistics account platform
      account routes logistics / courier questions to platform.ekart / platform_context.ekart.in. Use it to collect
      the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited Ekart Logistics account
    - Ekart
    - logistics / courier
    - platform.ekart
    - platform_context.ekart.in
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.ekart.logistics
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.ekart.logistics
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    account_name: Aza Fashions Private Limited Ekart Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.shiprocket.logistics

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited Shiprocket Logistics Aggregator account
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator account
    - Aza Fashions Private Limited Aza Fashions Private Limited Shiprocket Logistics Aggregator account
    - Shiprocket
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator account logistics / courier account
    colloquial_phrases:
    - Aza Fashions Private Limited Aza Fashions Private Limited Shiprocket Logistics Aggregator account source account
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator account logistics / courier runtime account
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator account configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Aza Fashions Private Limited Shiprocket
      Logistics Aggregator account logistics / courier sources. It points traversal to platform.shiprocket and platform_context.shiprocket.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Aza Fashions Private Limited Shiprocket Logistics Aggregator account table bindings are available for
      Aza Fashions Private Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Aza Fashions Private Limited Shiprocket
      Logistics Aggregator account questions traverse through?
    - Which source roles under Aza Fashions Private Limited Shiprocket Logistics Aggregator account are active or
      review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.shiprocket
    - platform_context.shiprocket.in
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited's Aza Fashions Private Limited Shiprocket Logistics Aggregator
      account platform account routes logistics / courier questions to platform.shiprocket / platform_context.shiprocket.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator account
    - Shiprocket
    - logistics / courier
    - platform.shiprocket
    - platform_context.shiprocket.in
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.shiprocket.logistics
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_name: Aza Fashions Private Limited Shiprocket Logistics Aggregator account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.razorpay.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited — Razorpay payment gateway
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay
    - Aza Fashions Private Limited Razorpay
    - Razorpay payment gateway account
    colloquial_phrases:
    - Aza Fashions Private Limited Razorpay source account
    - Razorpay payment gateway runtime account
    - Razorpay configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's Razorpay payment gateway sources.
      It points traversal to platform.razorpay and platform_context.razorpay.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Razorpay table bindings are available for Aza Fashions Private Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's Razorpay questions traverse through?
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - platform_account_id:platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Aza Fashions Private Limited's Razorpay platform account routes payment gateway questions to
      platform.razorpay / platform_context.razorpay.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - Razorpay
    - payment gateway
    - platform.razorpay
    - platform_context.razorpay.in
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: Aza Fashions Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    platform_account_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
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
      group_id: '56'
      group_level_id: '203'
```

#### platform_account.aza_fashions_private_limited.paypal.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  card_type: platform_account
  canonical_name: Aza Fashions Private Limited — PayPal payment gateway
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - PayPal
    - Aza Fashions Private Limited PayPal
    - PayPal payment gateway account
    colloquial_phrases:
    - Aza Fashions Private Limited PayPal source account
    - PayPal payment gateway runtime account
    - PayPal configured source family
    business_meaning: Runtime platform account for Aza Fashions Private Limited's PayPal payment gateway sources.
      It points traversal to platform.paypal and platform_context.paypal.global and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which PayPal table bindings are available for Aza Fashions Private Limited?
    - Which canonical platform/context should Aza Fashions Private Limited's PayPal questions traverse through?
    - Which source roles under PayPal are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - payment_gateway
    - source_router
    included_concepts:
    - 'client configuration: PayPal'
    - platform.paypal
    - platform_context.paypal.global
    - PayPal
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_id:platform.paypal
    - platform_context_id:platform_context.paypal.global
    - platform_account_id:platform_account.aza_fashions_private_limited.paypal.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Aza Fashions Private Limited's PayPal platform account routes payment gateway questions to platform.paypal
      / platform_context.paypal.global. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Aza Fashions Private Limited
    - PayPal
    - payment gateway
    - platform.paypal
    - platform_context.paypal.global
    exact_match_keys:
    - platform_account.aza_fashions_private_limited.paypal.payment_gateway
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: Aza Fashions Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.paypal
    platform_context_id: platform_context.paypal.global
    platform_account_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_id: platform.paypal
    platform_context_id: platform_context.paypal.global
    account_name: PayPal
    account_type: payment_gateway_account
    source_account_identifier: PayPal
    source_account_identifier_status: client_docx_names_source_without_specific_merchant_or_bank_account_number
    active: true
    source_family: payment_gateway
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
    canonical_source_pack: payment_gateway.md
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited AZA Proprietary D2C OMS d2c_sales_orders binding
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AZA Proprietary D2C OMS d2c sales orders
    - aza_sales_dump
    - zs_observe.aza_sales_dump
    - AZA sales dump, return dump, and wallet ledger flat-file sources
    - Aza Fashions Private Limited AZA Proprietary D2C OMS d2c sales orders
    colloquial_phrases:
    - Aza Fashions Private Limited AZA Proprietary D2C OMS d2c sales orders source
    - AZA Proprietary D2C OMS d2c sales orders runtime binding
    - aza_sales_dump for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's AZA Proprietary
      D2C OMS d2c sales orders evidence should use zs_observe.aza_sales_dump. Apply group_id=56, group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AZA Proprietary D2C OMS OMS rows should answer Aza Fashions Private Limited's d2c sales orders question?
    - Which runtime scope must be injected before using aza_sales_dump?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - d2c_sales_orders
    included_concepts:
    - zs_observe.aza_sales_dump
    - d2c sales orders
    - AZA Proprietary D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:d2c_sales_orders
    - table_id:table.zs_observe.aza_sales_dump
    - runtime_source_family:oms
    embedding_text: 'For Aza Fashions Private Limited, the AZA Proprietary D2C OMS d2c sales orders binding selects
      zs_observe.aza_sales_dump as OMS evidence. Scope: group_id=56, group_level_id=203. Reusable semantics come
      from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - AZA Proprietary D2C OMS
    - d2c sales orders
    - OMS
    - zs_observe.aza_sales_dump
    - aza_sales_dump
    - d2c_sales_orders
    - oms_business_kb.md
    - group_id=56
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - oms_business_kb.md
    source_path: Aza Fashions Private Limited.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_sales_dump
    source_role: d2c_sales_orders
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_sales_dump
    source_role: d2c_sales_orders
    source_entity: AZA Proprietary D2C OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: AZA sales dump, return dump, and wallet ledger flat-file sources
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited AZA Proprietary D2C OMS return_orders binding
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AZA Proprietary D2C OMS return orders
    - aza_return_dump
    - zs_observe.aza_return_dump
    - AZA sales dump, return dump, and wallet ledger flat-file sources
    - Aza Fashions Private Limited AZA Proprietary D2C OMS return orders
    colloquial_phrases:
    - Aza Fashions Private Limited AZA Proprietary D2C OMS return orders source
    - AZA Proprietary D2C OMS return orders runtime binding
    - aza_return_dump for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's AZA Proprietary
      D2C OMS return orders evidence should use zs_observe.aza_return_dump. Apply group_id=56, group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AZA Proprietary D2C OMS OMS rows should answer Aza Fashions Private Limited's return orders question?
    - Which runtime scope must be injected before using aza_return_dump?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - return_orders
    included_concepts:
    - zs_observe.aza_return_dump
    - return orders
    - AZA Proprietary D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:return_orders
    - table_id:table.zs_observe.aza_return_dump
    - runtime_source_family:oms
    embedding_text: 'For Aza Fashions Private Limited, the AZA Proprietary D2C OMS return orders binding selects
      zs_observe.aza_return_dump as OMS evidence. Scope: group_id=56, group_level_id=203. Reusable semantics come
      from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - AZA Proprietary D2C OMS
    - return orders
    - OMS
    - zs_observe.aza_return_dump
    - aza_return_dump
    - return_orders
    - oms_business_kb.md
    - group_id=56
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - oms_business_kb.md
    source_path: Aza Fashions Private Limited.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_return_dump
    source_role: return_orders
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_return_dump
    source_role: return_orders
    source_entity: AZA Proprietary D2C OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: AZA sales dump, return dump, and wallet ledger flat-file sources
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited AZA Proprietary D2C OMS wallet_ledger binding
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AZA Proprietary D2C OMS wallet ledger
    - aza_wallet_ledger
    - zs_observe.aza_wallet_ledger
    - AZA sales dump, return dump, and wallet ledger flat-file sources
    - Aza Fashions Private Limited AZA Proprietary D2C OMS wallet ledger
    colloquial_phrases:
    - Aza Fashions Private Limited AZA Proprietary D2C OMS wallet ledger source
    - AZA Proprietary D2C OMS wallet ledger runtime binding
    - aza_wallet_ledger for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's AZA Proprietary
      D2C OMS wallet ledger evidence should use zs_observe.aza_wallet_ledger. Apply group_id=56, group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in oms_business_kb.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which AZA Proprietary D2C OMS OMS rows should answer Aza Fashions Private Limited's wallet ledger question?
    - Which runtime scope must be injected before using aza_wallet_ledger?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - wallet_ledger
    included_concepts:
    - zs_observe.aza_wallet_ledger
    - wallet ledger
    - AZA Proprietary D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    - platform_id:platform.zenstatement_oms_business_kb
    - platform_context_id:platform_context.zenstatement.oms_business_kb
    - source_role:wallet_ledger
    - table_id:table.zs_observe.aza_wallet_ledger
    - runtime_source_family:oms
    embedding_text: 'For Aza Fashions Private Limited, the AZA Proprietary D2C OMS wallet ledger binding selects
      zs_observe.aza_wallet_ledger as OMS evidence. Scope: group_id=56, group_level_id=203. Reusable semantics come
      from oms_business_kb.md. Coverage status: active. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - AZA Proprietary D2C OMS
    - wallet ledger
    - OMS
    - zs_observe.aza_wallet_ledger
    - aza_wallet_ledger
    - wallet_ledger
    - oms_business_kb.md
    - group_id=56
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - oms_business_kb.md
    source_path: Aza Fashions Private Limited.docx and oms_business_kb.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    platform_id: platform.zenstatement_oms_business_kb
    platform_context_id: platform_context.zenstatement.oms_business_kb
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_wallet_ledger
    source_role: wallet_ledger
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
    domain_id: domain.oms_business.aza_orders_returns_wallet
    table_id: table.zs_observe.aza_wallet_ledger
    source_role: wallet_ledger
    source_entity: AZA Proprietary D2C OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: AZA sales dump, return dump, and wallet ledger flat-file sources
    canonical_table_coverage_status: active
    canonical_source_pack: oms_business_kb.md
    context_fit_status: direct_match_to_uploaded_oms_business_pack
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Delhivery Logistics direct_courier_cod_settlement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Delhivery Logistics direct courier COD settlement
    - delhivery_settlement
    - zs_observe.delhivery_settlement
    - table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    - Aza Fashions Private Limited Delhivery Logistics direct courier COD settlement
    colloquial_phrases:
    - Aza Fashions Private Limited Delhivery Logistics direct courier COD settlement source
    - Delhivery Logistics direct courier COD settlement runtime binding
    - delhivery_settlement for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Delhivery
      Logistics direct courier COD settlement evidence should use zs_observe.delhivery_settlement. Apply group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Delhivery Logistics logistics rows should answer Aza Fashions Private Limited's direct courier COD settlement
      question?
    - Which courier/account scope must be applied before using delhivery_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - direct_courier_cod_settlement
    included_concepts:
    - zs_observe.delhivery_settlement
    - direct courier COD settlement
    - Delhivery Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=203
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - source_role:direct_courier_cod_settlement
    - table_id:table.zs_observe.delhivery_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the Delhivery Logistics direct courier COD settlement binding
      selects zs_observe.delhivery_settlement as logistics / courier evidence. Scope: group_level_id=203. Reusable
      semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Delhivery Logistics
    - direct courier COD settlement
    - logistics / courier
    - zs_observe.delhivery_settlement
    - delhivery_settlement
    - direct_courier_cod_settlement
    - logistics_integrated.md
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    table_id: table.zs_observe.delhivery_settlement
    source_role: direct_courier_cod_settlement
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
    table_id: table.zs_observe.delhivery_settlement
    source_role: direct_courier_cod_settlement
    source_entity: Delhivery Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '203'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.delhivery_settlement.group_level_id
      runtime_value: '203'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Delhivery Logistics direct_courier_freight_invoice binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Delhivery Logistics direct courier freight invoice
    - delhivery_invoice
    - zs_observe.delhivery_invoice
    - table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    - Aza Fashions Private Limited Delhivery Logistics direct courier freight invoice
    colloquial_phrases:
    - Aza Fashions Private Limited Delhivery Logistics direct courier freight invoice source
    - Delhivery Logistics direct courier freight invoice runtime binding
    - delhivery_invoice for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Delhivery
      Logistics direct courier freight invoice evidence should use zs_observe.delhivery_invoice. Apply group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Delhivery Logistics logistics rows should answer Aza Fashions Private Limited's direct courier freight
      invoice question?
    - Which courier/account scope must be applied before using delhivery_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - direct_courier_freight_invoice
    included_concepts:
    - zs_observe.delhivery_invoice
    - direct courier freight invoice
    - Delhivery Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=203
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.delhivery.logistics
    - platform_id:platform.delhivery
    - platform_context_id:platform_context.delhivery.in
    - source_role:direct_courier_freight_invoice
    - table_id:table.zs_observe.delhivery_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the Delhivery Logistics direct courier freight invoice binding
      selects zs_observe.delhivery_invoice as logistics / courier evidence. Scope: group_level_id=203. Reusable
      semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Delhivery Logistics
    - direct courier freight invoice
    - logistics / courier
    - zs_observe.delhivery_invoice
    - delhivery_invoice
    - direct_courier_freight_invoice
    - logistics_integrated.md
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
    platform_id: platform.delhivery
    platform_context_id: platform_context.delhivery.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    table_id: table.zs_observe.delhivery_invoice
    source_role: direct_courier_freight_invoice
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
    table_id: table.zs_observe.delhivery_invoice
    source_role: direct_courier_freight_invoice
    source_entity: Delhivery Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '203'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.delhivery_invoice.group_level_id
      runtime_value: '203'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.delhivery_settlement, table.zs_observe.delhivery_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited DTDC Logistics courier_cod_settlement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - DTDC Logistics courier COD settlement
    - dtdc_settlement
    - zs_observe.dtdc_settlement
    - table.zs_observe.dtdc_settlement, table.zs_observe.dtdc_invoice
    - Aza Fashions Private Limited DTDC Logistics courier COD settlement
    colloquial_phrases:
    - Aza Fashions Private Limited DTDC Logistics courier COD settlement source
    - DTDC Logistics courier COD settlement runtime binding
    - dtdc_settlement for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's DTDC Logistics
      courier COD settlement evidence should use zs_observe.dtdc_settlement. Apply group_level_id=203 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which DTDC Logistics logistics rows should answer Aza Fashions Private Limited's courier COD settlement question?
    - Which courier/account scope must be applied before using dtdc_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - courier_cod_settlement
    included_concepts:
    - zs_observe.dtdc_settlement
    - courier COD settlement
    - DTDC Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=203
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.dtdc.logistics
    - platform_id:platform.dtdc
    - platform_context_id:platform_context.dtdc.in
    - source_role:courier_cod_settlement
    - table_id:table.zs_observe.dtdc_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the DTDC Logistics courier COD settlement binding selects
      zs_observe.dtdc_settlement as logistics / courier evidence. Scope: group_level_id=203. Reusable semantics
      come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - DTDC Logistics
    - courier COD settlement
    - logistics / courier
    - zs_observe.dtdc_settlement
    - dtdc_settlement
    - courier_cod_settlement
    - logistics_integrated.md
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
    table_id: table.zs_observe.dtdc_settlement
    source_role: courier_cod_settlement
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
    table_id: table.zs_observe.dtdc_settlement
    source_role: courier_cod_settlement
    source_entity: DTDC Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '203'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.dtdc_settlement.group_level_id
      runtime_value: '203'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.dtdc_settlement, table.zs_observe.dtdc_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited DTDC Logistics empty_courier_invoice_guardrail binding
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - DTDC Logistics empty courier invoice guardrail
    - dtdc_invoice
    - zs_observe.dtdc_invoice
    - table.zs_observe.dtdc_settlement, table.zs_observe.dtdc_invoice
    - Aza Fashions Private Limited DTDC Logistics empty courier invoice guardrail
    colloquial_phrases:
    - Aza Fashions Private Limited DTDC Logistics empty courier invoice guardrail source
    - DTDC Logistics empty courier invoice guardrail runtime binding
    - dtdc_invoice for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's DTDC Logistics
      empty courier invoice guardrail evidence should use zs_observe.dtdc_invoice. Apply client runtime scope before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which DTDC Logistics logistics rows should answer Aza Fashions Private Limited's empty courier invoice guardrail
      question?
    - Which courier/account scope must be applied before using dtdc_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - empty_courier_invoice_guardrail
    included_concepts:
    - zs_observe.dtdc_invoice
    - empty courier invoice guardrail
    - DTDC Logistics
    - courier settlement or invoice evidence
    - shipment references
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.dtdc.logistics
    - platform_id:platform.dtdc
    - platform_context_id:platform_context.dtdc.in
    - source_role:empty_courier_invoice_guardrail
    - table_id:table.zs_observe.dtdc_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the DTDC Logistics empty courier invoice guardrail binding
      selects zs_observe.dtdc_invoice as logistics / courier evidence. Runtime scope must be supplied before SQL.
      Reusable semantics come from logistics_integrated.md. Coverage status: review_required. Use this card for
      runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - DTDC Logistics
    - empty courier invoice guardrail
    - logistics / courier
    - zs_observe.dtdc_invoice
    - dtdc_invoice
    - empty_courier_invoice_guardrail
    - logistics_integrated.md
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
    platform_id: platform.dtdc
    platform_context_id: platform_context.dtdc.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    table_id: table.zs_observe.dtdc_invoice
    source_role: empty_courier_invoice_guardrail
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
    table_id: table.zs_observe.dtdc_invoice
    source_role: empty_courier_invoice_guardrail
    source_entity: DTDC Logistics
    scope_keys: []
    scope_key_status: no_documented_group_level_scope_column_in_reusable_logistics_table_card
    active: false
    source_configuration_text: table.zs_observe.dtdc_settlement, table.zs_observe.dtdc_invoice
    canonical_table_coverage_status: review_required
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Ekart Logistics logistics_invoice_empty binding
  status: review_required
  review_status: review_required
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Ekart Logistics empty logistics invoice guardrail
    - ekart_invoice
    - zs_observe.ekart_invoice
    - table.zs_observe.ekart_invoice
    - Aza Fashions Private Limited Ekart Logistics empty logistics invoice guardrail
    colloquial_phrases:
    - Aza Fashions Private Limited Ekart Logistics empty logistics invoice guardrail source
    - Ekart Logistics empty logistics invoice guardrail runtime binding
    - ekart_invoice for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Ekart Logistics
      empty logistics invoice guardrail evidence should use zs_observe.ekart_invoice. Apply client runtime scope
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Ekart Logistics logistics rows should answer Aza Fashions Private Limited's empty logistics invoice
      guardrail question?
    - Which courier/account scope must be applied before using ekart_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_invoice_empty
    included_concepts:
    - zs_observe.ekart_invoice
    - empty logistics invoice guardrail
    - Ekart Logistics
    - courier settlement or invoice evidence
    - shipment references
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.ekart.logistics
    - platform_id:platform.ekart
    - platform_context_id:platform_context.ekart.in
    - source_role:logistics_invoice_empty
    - table_id:table.zs_observe.ekart_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the Ekart Logistics empty logistics invoice guardrail binding
      selects zs_observe.ekart_invoice as logistics / courier evidence. Runtime scope must be supplied before SQL.
      Reusable semantics come from logistics_integrated.md. Coverage status: review_required. Use this card for
      runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Ekart Logistics
    - empty logistics invoice guardrail
    - logistics / courier
    - zs_observe.ekart_invoice
    - ekart_invoice
    - logistics_invoice_empty
    - logistics_integrated.md
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.ekart.logistics
    platform_id: platform.ekart
    platform_context_id: platform_context.ekart.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    table_id: table.zs_observe.ekart_invoice
    source_role: logistics_invoice_empty
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.ekart.logistics
    table_id: table.zs_observe.ekart_invoice
    source_role: logistics_invoice_empty
    source_entity: Ekart Logistics
    scope_keys: []
    scope_key_status: no_documented_group_level_scope_column_in_reusable_logistics_table_card
    active: false
    source_configuration_text: table.zs_observe.ekart_invoice
    canonical_table_coverage_status: review_required
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Shiprocket Logistics Aggregator logistics_cod_settlement binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shiprocket Logistics Aggregator logistics cod settlement
    - shiprocket_settlement
    - zs_observe.shiprocket_settlement
    - table.zs_observe.shiprocket_settlement, table.zs_observe.shiprocket_invoice
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator logistics cod settlement
    colloquial_phrases:
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator logistics cod settlement source
    - Shiprocket Logistics Aggregator logistics cod settlement runtime binding
    - shiprocket_settlement for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Shiprocket
      Logistics Aggregator logistics cod settlement evidence should use zs_observe.shiprocket_settlement. Apply
      group_level_id=203 before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Shiprocket Logistics Aggregator logistics rows should answer Aza Fashions Private Limited's logistics
      cod settlement question?
    - Which courier/account scope must be applied before using shiprocket_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_cod_settlement
    included_concepts:
    - zs_observe.shiprocket_settlement
    - logistics cod settlement
    - Shiprocket Logistics Aggregator
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=203
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - source_role:logistics_cod_settlement
    - table_id:table.zs_observe.shiprocket_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the Shiprocket Logistics Aggregator logistics cod settlement
      binding selects zs_observe.shiprocket_settlement as logistics / courier evidence. Scope: group_level_id=203.
      Reusable semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source
      resolution, not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Shiprocket Logistics Aggregator
    - logistics cod settlement
    - logistics / courier
    - zs_observe.shiprocket_settlement
    - shiprocket_settlement
    - logistics_cod_settlement
    - logistics_integrated.md
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
    table_id: table.zs_observe.shiprocket_settlement
    source_role: logistics_cod_settlement
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
    table_id: table.zs_observe.shiprocket_settlement
    source_role: logistics_cod_settlement
    source_entity: Shiprocket Logistics Aggregator
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '203'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shiprocket_settlement.group_level_id
      runtime_value: '203'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.shiprocket_settlement, table.zs_observe.shiprocket_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Shiprocket Logistics Aggregator logistics_freight_invoice binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shiprocket Logistics Aggregator freight invoice
    - shiprocket_invoice
    - zs_observe.shiprocket_invoice
    - table.zs_observe.shiprocket_settlement, table.zs_observe.shiprocket_invoice
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator freight invoice
    colloquial_phrases:
    - Aza Fashions Private Limited Shiprocket Logistics Aggregator freight invoice source
    - Shiprocket Logistics Aggregator freight invoice runtime binding
    - shiprocket_invoice for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Shiprocket
      Logistics Aggregator freight invoice evidence should use zs_observe.shiprocket_invoice. Apply group_level_id=203
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Shiprocket Logistics Aggregator logistics rows should answer Aza Fashions Private Limited's freight
      invoice question?
    - Which courier/account scope must be applied before using shiprocket_invoice?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_freight_invoice
    included_concepts:
    - zs_observe.shiprocket_invoice
    - freight invoice
    - Shiprocket Logistics Aggregator
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=203
    - logistics_integrated.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Courier evidence should not be treated as marketplace settlement or bank cash unless a reconciliation profile
      links the sides.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - source_role:logistics_freight_invoice
    - table_id:table.zs_observe.shiprocket_invoice
    - runtime_source_family:logistics
    embedding_text: 'For Aza Fashions Private Limited, the Shiprocket Logistics Aggregator freight invoice binding
      selects zs_observe.shiprocket_invoice as logistics / courier evidence. Scope: group_level_id=203. Reusable
      semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source resolution,
      not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Shiprocket Logistics Aggregator
    - freight invoice
    - logistics / courier
    - zs_observe.shiprocket_invoice
    - shiprocket_invoice
    - logistics_freight_invoice
    - logistics_integrated.md
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    table_id: table.zs_observe.shiprocket_invoice
    source_role: logistics_freight_invoice
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
    table_id: table.zs_observe.shiprocket_invoice
    source_role: logistics_freight_invoice
    source_entity: Shiprocket Logistics Aggregator
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '203'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shiprocket_invoice.group_level_id
      runtime_value: '203'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.shiprocket_settlement, table.zs_observe.shiprocket_invoice
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited Razorpay Domestic D2C Razorpay pay-in binding
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
    vendor_or_system: Aza Fashions Private Limited
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
    - Aza Fashions Private Limited Razorpay settlement
    colloquial_phrases:
    - Aza Fashions Private Limited Razorpay settlement source
    - Razorpay settlement runtime binding
    - razorpay_payin for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's Razorpay
      settlement evidence should use zs_observe.razorpay_payin. Apply group_id=56, group_level_id=203 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Razorpay settlement rows represent expected gateway evidence for Aza Fashions Private Limited?
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
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.razorpay_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Aza Fashions Private Limited, the Razorpay settlement binding selects zs_observe.razorpay_payin
      as payment gateway evidence. Scope: group_id=56, group_level_id=203. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - Razorpay
    - settlement
    - payment gateway
    - zs_observe.razorpay_payin
    - razorpay_payin
    - payment_gateway.md
    - group_id=56
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: Aza Fashions Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    canonical_table_id: table.zs_observe.razorpay_payin
    physical_table_reference: zs_observe.razorpay_payin
    configured_pipeline_target: razorpay_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Domestic D2C Razorpay pay-in
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '56'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '56'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '203'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '203'
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

#### account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  card_type: account_data_binding
  canonical_name: Aza Fashions Private Limited PayPal settlement variant requires ops confirmation binding
  status: review_required
  review_status: review_required
  confidence: medium
  version: client_marketplace_logistics_oms_wms_payment_bank_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - PayPal settlement
    - paypal_settlement
    - zs_observe.paypal_settlement
    - paypal_in_settlement + paypal_us_settlement
    - Aza Fashions Private Limited PayPal settlement
    colloquial_phrases:
    - Aza Fashions Private Limited PayPal settlement source
    - PayPal settlement runtime binding
    - paypal_settlement for Aza Fashions Private Limited
    business_meaning: This account-data binding tells the resolver that Aza Fashions Private Limited's PayPal settlement
      evidence should use zs_observe.paypal_settlement. Apply group_id=56, group_level_id=203 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which PayPal settlement rows represent expected gateway evidence for Aza Fashions Private Limited?
    - Which merchant/account filters are still needed before querying paypal_settlement?
    - Which bank-statement binding should confirm actual cash for this gateway evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - payment_gateway
    - settlement
    included_concepts:
    - zs_observe.paypal_settlement
    - settlement
    - PayPal
    - payin / payout / settlement evidence
    - gateway references and UTRs
    - group_id=56
    - group_level_id=203
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - platform_account_id:platform_account.aza_fashions_private_limited.paypal.payment_gateway
    - platform_id:platform.paypal
    - platform_context_id:platform_context.paypal.global
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.paypal_settlement
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Aza Fashions Private Limited, the PayPal settlement binding selects zs_observe.paypal_settlement
      as payment gateway evidence. Scope: group_id=56, group_level_id=203. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Aza Fashions Private Limited
    - PayPal
    - settlement
    - payment gateway
    - zs_observe.paypal_settlement
    - paypal_settlement
    - paypal_in_settlement + paypal_us_settlement
    - payment_gateway.md
    - group_id=56
    - group_level_id=203
    exact_match_keys:
    - account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: Aza Fashions Private Limited.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
    platform_id: platform.paypal
    platform_context_id: platform_context.paypal.global
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paypal_settlement
    source_role: settlement
    account_data_binding_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    platform_account_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
    platform_id: platform.paypal
    platform_context_id: platform_context.paypal.global
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.paypal_settlement
    canonical_table_id: table.zs_observe.paypal_settlement
    physical_table_reference: zs_observe.paypal_settlement
    configured_pipeline_target: paypal_in_settlement + paypal_us_settlement
    mapping_status: provider_supported_but_client_pipeline_variant_not_exact
    source_role: settlement
    source_role_label: PayPal settlement variant requires ops confirmation
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '56'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '56'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '203'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '203'
      scope_application: runtime_or_ingestion_metadata
    candidate_account_scope_columns_from_reusable_pack: []
    mandatory_filters_from_reusable_pack:
    - is_active = true when present
    recommended_date_columns_from_reusable_pack:
    - created_date
    business_keys_from_reusable_pack:
    - transaction_id
    - reference_txn_id
    - bank_arn
    amount_columns_from_reusable_pack:
    - gross
    - fee
    - net
    - balance
    - balance_impact
    - vat
    - charged_amount
    - mp_fee
    - settled_amount
    grain_from_reusable_pack: one row per settlement/balance event or settlement line
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.5 Business Scope Set Cards

#### business_scope_set.aza_fashions_private_limited.logistics

```yaml
canonical_card:
  canonical_id: business_scope_set.aza_fashions_private_limited.logistics
  card_type: business_scope_set
  canonical_name: Aza Fashions Private Limited logistics scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.logistics
    runtime_source_family: logistics
  semantic:
    aliases:
    - Aza Fashions Private Limited logistics scope
    - Aza Fashions Private Limited logistics / courier scope
    - logistics / courier runtime scope set
    colloquial_phrases:
    - Aza Fashions Private Limited logistics / courier scope
    - logistics / courier accounts and bindings
    - Aza Fashions Private Limited logistics / courier resolver input
    business_meaning: Business scope set for Aza Fashions Private Limited's logistics / courier runtime resolution.
      It groups 4 platform accounts and 7 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which logistics / courier accounts and bindings are active for Aza Fashions Private Limited?
    - Which runtime table bindings should be considered together under Aza Fashions Private Limited logistics scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - logistics_courier
    - resolver_scope
    included_concepts:
    - 4 platform accounts
    - 7 account-data bindings
    - 2 deferred sources
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - business_scope_set_id:business_scope_set.aza_fashions_private_limited.logistics
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited logistics scope groups Aza Fashions Private Limited's logistics
      / courier runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited logistics scope
    - logistics / courier
    - business scope set
    - 4 accounts
    - 7 bindings
    exact_match_keys:
    - business_scope_set.aza_fashions_private_limited.logistics
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    scope_name: Aza Fashions Private Limited logistics scope
    scope_type: logistics_courier_reconciliation
    platform_account_ids:
    - platform_account.aza_fashions_private_limited.delhivery.logistics
    - platform_account.aza_fashions_private_limited.dtdc.logistics
    - platform_account.aza_fashions_private_limited.ekart.logistics
    - platform_account.aza_fashions_private_limited.shiprocket.logistics
    platform_ids:
    - platform.delhivery
    - platform.dtdc
    - platform.ekart
    - platform.shiprocket
    platform_context_ids:
    - platform_context.delhivery.in
    - platform_context.dtdc.in
    - platform_context.ekart.in
    - platform_context.shiprocket.in
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    - account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
    - account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    - account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    group_scope_values:
      group_id: '56'
      group_level_id: '203'
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: iThink
      config: Settlement + Invoice
      reason: No iThink canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.aza_fashions_private_limited.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.aza_fashions_private_limited.oms
  card_type: business_scope_set
  canonical_name: Aza Fashions Private Limited OMS runtime scope
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited OMS runtime scope
    - Aza Fashions Private Limited OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Aza Fashions Private Limited OMS scope
    - OMS accounts and bindings
    - Aza Fashions Private Limited OMS resolver input
    business_meaning: Business scope set for Aza Fashions Private Limited's OMS runtime resolution. It groups 1
      platform accounts and 3 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which OMS accounts and bindings are active for Aza Fashions Private Limited?
    - Which runtime table bindings should be considered together under Aza Fashions Private Limited OMS runtime
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 3 account-data bindings
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - runtime_source_family:oms
    embedding_text: Aza Fashions Private Limited OMS runtime scope groups Aza Fashions Private Limited's OMS runtime
      accounts and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources
      remain deferred until supported canonical packs exist.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 3 bindings
    exact_match_keys:
    - business_scope_set.aza_fashions_private_limited.oms
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
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.oms
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    binding_name: Aza Fashions Private Limited OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.oms
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
    participating_accounts:
    - platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
      account_name: Aza Fashions Private Limited AZA Proprietary D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
      source_role: d2c_sales_orders
      table_id: table.zs_observe.aza_sales_dump
      domain_id: domain.oms_business.aza_orders_returns_wallet
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
      source_role: return_orders
      table_id: table.zs_observe.aza_return_dump
      domain_id: domain.oms_business.aza_orders_returns_wallet
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
      source_role: wallet_ledger
      table_id: table.zs_observe.aza_wallet_ledger
      domain_id: domain.oms_business.aza_orders_returns_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.aza_fashions_private_limited.payment_gateway

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
  canonical_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  card_type: business_scope_set
  canonical_name: Aza Fashions Private Limited payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited payment gateway runtime scope
    - Aza Fashions Private Limited payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - Aza Fashions Private Limited payment gateway scope
    - payment gateway accounts and bindings
    - Aza Fashions Private Limited payment gateway resolver input
    business_meaning: Business scope set for Aza Fashions Private Limited's payment gateway runtime resolution.
      It groups 2 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for Aza Fashions Private Limited?
    - Which runtime table bindings should be considered together under Aza Fashions Private Limited payment gateway
      runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - payment_gateway
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - runtime_source_family:payment_gateway
    embedding_text: Aza Fashions Private Limited payment gateway runtime scope groups Aza Fashions Private Limited's
      payment gateway runtime accounts and table bindings. Use it to restrict traversal to the client's configured
      sources; unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited payment gateway runtime scope
    - payment gateway
    - business scope set
    - 2 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.aza_fashions_private_limited.payment_gateway
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    binding_name: Aza Fashions Private Limited payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.payment_gateway
    platform_account_ids:
    - platform_account.aza_fashions_private_limited.paypal.payment_gateway
    - platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
    - account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    included_platform_ids:
    - platform.paypal
    - platform.razorpay
    included_platform_context_ids:
    - platform_context.paypal.global
    - platform_context.razorpay.in
    source_flow_paths:
    - platform_account_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
      account_data_binding_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
      platform_id: platform.paypal
      platform_context_id: platform_context.paypal.global
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paypal_settlement
      source_role: settlement
      configured_pipeline_target: paypal_in_settlement + paypal_us_settlement
      mapping_status: provider_supported_but_client_pipeline_variant_not_exact
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Aza Fashions Private Limited logistics runtime resolution
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - logistics_integrated.md
    source_path: Aza Fashions Private Limited.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    business_flow_binding_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
    runtime_source_family: logistics
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.logistics
  semantic:
    aliases:
    - Aza Fashions Private Limited logistics runtime resolution
    - Aza Fashions Private Limited logistics / courier flow
    - logistics / courier runtime resolution flow
    colloquial_phrases:
    - Aza Fashions Private Limited logistics / courier resolution flow
    - logistics / courier source routing
    - Aza Fashions Private Limited runtime traversal plan
    business_meaning: Business flow binding for Aza Fashions Private Limited's logistics / courier source resolution.
      It connects the scope set to 4 platform accounts and 7 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which logistics / courier bindings should be traversed for Aza Fashions Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - logistics_courier
    - runtime_traversal
    included_concepts:
    - 4 platform accounts
    - 7 account-data bindings
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - business_flow_binding_id:business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
    - runtime_source_family:logistics
    embedding_text: Aza Fashions Private Limited logistics runtime resolution is Aza Fashions Private Limited's
      logistics / courier runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited logistics runtime resolution
    - logistics / courier
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    binding_name: Aza Fashions Private Limited logistics runtime resolution
    binding_type: logistics_source_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.logistics
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
    - account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
    - account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
    - account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
    - account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
    - account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    participating_accounts:
    - platform_account_id: platform_account.aza_fashions_private_limited.delhivery.logistics
      account_name: Aza Fashions Private Limited Delhivery Logistics account
    - platform_account_id: platform_account.aza_fashions_private_limited.dtdc.logistics
      account_name: Aza Fashions Private Limited DTDC Logistics account
    - platform_account_id: platform_account.aza_fashions_private_limited.ekart.logistics
      account_name: Aza Fashions Private Limited Ekart Logistics account
    - platform_account_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
      account_name: Aza Fashions Private Limited Shiprocket Logistics Aggregator account
    money_flow_paths:
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
      source_role: direct_courier_cod_settlement
      table_id: table.zs_observe.delhivery_settlement
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
      source_role: direct_courier_freight_invoice
      table_id: table.zs_observe.delhivery_invoice
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
      source_role: courier_cod_settlement
      table_id: table.zs_observe.dtdc_settlement
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
      source_role: empty_courier_invoice_guardrail
      table_id: table.zs_observe.dtdc_invoice
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
      source_role: logistics_invoice_empty
      table_id: table.zs_observe.ekart_invoice
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
      source_role: logistics_cod_settlement
      table_id: table.zs_observe.shiprocket_settlement
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
      source_role: logistics_freight_invoice
      table_id: table.zs_observe.shiprocket_invoice
    deferred_sources:
    - label: Bluedart
      config: Settlement + Invoice
      reason: No Bluedart canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: iThink
      config: Settlement + Invoice
      reason: No iThink canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Aza Fashions Private Limited OMS runtime resolution flow
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
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited OMS runtime resolution flow
    - Aza Fashions Private Limited OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Aza Fashions Private Limited OMS resolution flow
    - OMS source routing
    - Aza Fashions Private Limited runtime traversal plan
    business_meaning: Business flow binding for Aza Fashions Private Limited's OMS source resolution. It connects
      the scope set to 1 platform accounts and 3 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Aza Fashions Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - OMS
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 3 account-data bindings
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - runtime_source_family:oms
    embedding_text: Aza Fashions Private Limited OMS runtime resolution flow is Aza Fashions Private Limited's OMS
      runtime traversal binding. It connects the business scope set to account and table bindings so retrieval selects
      client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
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
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    binding_name: Aza Fashions Private Limited OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.oms
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
    - account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
    participating_accounts:
    - platform_account_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
      account_name: Aza Fashions Private Limited AZA Proprietary D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
      source_role: d2c_sales_orders
      table_id: table.zs_observe.aza_sales_dump
      domain_id: domain.oms_business.aza_orders_returns_wallet
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
      source_role: return_orders
      table_id: table.zs_observe.aza_return_dump
      domain_id: domain.oms_business.aza_orders_returns_wallet
    - account_data_binding_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
      source_role: wallet_ledger
      table_id: table.zs_observe.aza_wallet_ledger
      domain_id: domain.oms_business.aza_orders_returns_wallet
    deferred_sources: []
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution

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
  canonical_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Aza Fashions Private Limited payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Aza Fashions Private Limited
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Aza Fashions Private Limited payment gateway runtime resolution
    - Aza Fashions Private Limited payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - Aza Fashions Private Limited payment gateway resolution flow
    - payment gateway source routing
    - Aza Fashions Private Limited runtime traversal plan
    business_meaning: Business flow binding for Aza Fashions Private Limited's payment gateway source resolution.
      It connects the scope set to 2 platform accounts and 2 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for Aza Fashions Private Limited's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - payment_gateway
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
    - tenant_id:tenant.aza_fashions_private_limited
    - group_id:group.aza_fashions_private_limited.g56.gl203
    - runtime_source_family:payment_gateway
    embedding_text: Aza Fashions Private Limited payment gateway runtime resolution is Aza Fashions Private Limited's
      payment gateway runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Aza Fashions Private Limited
    - Aza Fashions Private Limited payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - Aza Fashions Private Limited.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  fields:
    tenant_id: tenant.aza_fashions_private_limited
    group_id: group.aza_fashions_private_limited.g56.gl203
    business_flow_binding_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.aza_fashions_private_limited.payment_gateway
    flow_name: Aza Fashions Private Limited payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.aza_fashions_private_limited.paypal.payment_gateway
    - platform_account.aza_fashions_private_limited.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
    - account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
    source_flow_paths:
    - platform_account_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
      account_data_binding_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
      platform_id: platform.paypal
      platform_context_id: platform_context.paypal.global
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.paypal_settlement
      source_role: settlement
      configured_pipeline_target: paypal_in_settlement + paypal_us_settlement
      mapping_status: provider_supported_but_client_pipeline_variant_not_exact
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_sales_dump_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_sales_dump_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  target_card_id: column.zs_observe.aza_sales_dump.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_sales_dump_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_sales_dump_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  target_card_id: column.zs_observe.aza_sales_dump.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_return_dump_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_return_dump_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  target_card_id: column.zs_observe.aza_return_dump.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_return_dump_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_applies_scope_column.column_zs_observe_aza_return_dump_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  target_card_id: column.zs_observe.aza_return_dump.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_applies_scope_column.column_zs_observe_aza_wallet_ledger_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_applies_scope_column.column_zs_observe_aza_wallet_ledger_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  target_card_id: column.zs_observe.aza_wallet_ledger.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_applies_scope_column.column_zs_observe_aza_wallet_ledger_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_applies_scope_column.column_zs_observe_aza_wallet_ledger_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  target_card_id: column.zs_observe.aza_wallet_ledger.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_applies_scope_column.column_zs_observe_delhivery_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_applies_scope_column.column_zs_observe_delhivery_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: column.zs_observe.delhivery_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_applies_scope_column.column_zs_observe_delhivery_invoice_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_applies_scope_column.column_zs_observe_delhivery_invoice_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: column.zs_observe.delhivery_invoice.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_applies_scope_column.column_zs_observe_dtdc_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_applies_scope_column.column_zs_observe_dtdc_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  target_card_id: column.zs_observe.dtdc_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  target_card_id: column.zs_observe.shiprocket_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_invoice_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_invoice_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: column.zs_observe.shiprocket_invoice.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  target_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  target_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  target_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  target_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_binds_to_table.table_zs_observe_aza_sales_dump

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump.account_data_binding_binds_to_table.table_zs_observe_aza_sales_dump
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  target_card_id: table.zs_observe.aza_sales_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_binds_to_table.table_zs_observe_aza_return_dump

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump.account_data_binding_binds_to_table.table_zs_observe_aza_return_dump
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  target_card_id: table.zs_observe.aza_return_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_binds_to_table.table_zs_observe_aza_wallet_ledger

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger.account_data_binding_binds_to_table.table_zs_observe_aza_wallet_ledger
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  target_card_id: table.zs_observe.aza_wallet_ledger
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_binds_to_table.table_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement.account_data_binding_binds_to_table.table_zs_observe_delhivery_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  target_card_id: table.zs_observe.delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_binds_to_table.table_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice.account_data_binding_binds_to_table.table_zs_observe_delhivery_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  target_card_id: table.zs_observe.delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_binds_to_table.table_zs_observe_dtdc_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement.account_data_binding_binds_to_table.table_zs_observe_dtdc_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  target_card_id: table.zs_observe.dtdc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_binds_to_table.table_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice.account_data_binding_binds_to_table.table_zs_observe_dtdc_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  target_card_id: table.zs_observe.dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_binds_to_table.table_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice.account_data_binding_binds_to_table.table_zs_observe_ekart_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  target_card_id: table.zs_observe.ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_binds_to_table.table_zs_observe_shiprocket_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement.account_data_binding_binds_to_table.table_zs_observe_shiprocket_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  target_card_id: table.zs_observe.shiprocket_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_binds_to_table.table_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_binds_to_table.table_zs_observe_shiprocket_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: table.zs_observe.shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  target_card_id: business_scope_set.aza_fashions_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  target_card_id: business_scope_set.aza_fashions_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_delhivery

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_delhivery
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform.delhivery
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_dtdc

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_dtdc
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform.dtdc
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_ekart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_ekart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform.ekart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform.platform_shiprocket
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform.platform_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_delhivery_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_delhivery_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_context.delhivery.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_dtdc_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_dtdc_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_context.dtdc.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_ekart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_ekart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_context.ekart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_oms.business_scope_set_includes_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_aza_fashions_private_limited_g56_gl203.group_belongs_to_tenant.tenant_aza_fashions_private_limited

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_belongs_to_tenant.tenant_aza_fashions_private_limited
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: tenant.aza_fashions_private_limited
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_logistics_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_flow_binding.aza_fashions_private_limited.logistics_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_flow_binding.aza_fashions_private_limited.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_logistics

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_logistics
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_scope_set.aza_fashions_private_limited.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_oms

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_scope_set.aza_fashions_private_limited.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_delhivery_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_dtdc_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_ekart_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_shiprocket_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_d2c_sales_orders_zs_observe_aza_sales_dump
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.d2c_sales_orders.zs_observe_aza_sales_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_return_orders_zs_observe_aza_return_dump
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.return_orders.zs_observe_aza_return_dump
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_aza_proprietary_oms_wallet_ledger_zs_observe_aza_wallet_ledger
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: account_data_binding.aza_fashions_private_limited.aza_proprietary_oms.wallet_ledger.zs_observe_aza_wallet_ledger
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_cod_settlement_zs_observe_delhivery_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_cod_settlement.zs_observe_delhivery_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_delhivery_direct_courier_freight_invoice_zs_observe_delhivery_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.delhivery.direct_courier_freight_invoice.zs_observe_delhivery_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_courier_cod_settlement_zs_observe_dtdc_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.courier_cod_settlement.zs_observe_dtdc_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_dtdc_empty_courier_invoice_guardrail_zs_observe_dtdc_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.dtdc.empty_courier_invoice_guardrail.zs_observe_dtdc_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_ekart_logistics_invoice_empty_zs_observe_ekart_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.ekart.logistics_invoice_empty.zs_observe_ekart_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_cod_settlement_zs_observe_shiprocket_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_cod_settlement.zs_observe_shiprocket_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  target_card_id: account_data_binding.aza_fashions_private_limited.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_uses_platform.platform_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: platform.zenstatement_oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_uses_platform.platform_delhivery

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_uses_platform.platform_delhivery
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  target_card_id: platform.delhivery
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_uses_platform.platform_dtdc

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_uses_platform.platform_dtdc
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  target_card_id: platform.dtdc
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_uses_platform.platform_ekart

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_uses_platform.platform_ekart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  target_card_id: platform.ekart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_aza_proprietary_oms_oms.platform_account_uses_platform_context.platform_context_zenstatement_oms_business_kb
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.aza_proprietary_oms.oms
  target_card_id: platform_context.zenstatement.oms_business_kb
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_uses_platform_context.platform_context_delhivery_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_delhivery_logistics.platform_account_uses_platform_context.platform_context_delhivery_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.delhivery.logistics
  target_card_id: platform_context.delhivery.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_uses_platform_context.platform_context_dtdc_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_dtdc_logistics.platform_account_uses_platform_context.platform_context_dtdc_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.dtdc.logistics
  target_card_id: platform_context.dtdc.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_uses_platform_context.platform_context_ekart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_ekart_logistics.platform_account_uses_platform_context.platform_context_ekart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.ekart.logistics
  target_card_id: platform_context.ekart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.shiprocket.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### TENANT_HAS_GROUP

#### edge.tenant_aza_fashions_private_limited.tenant_has_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.tenant_aza_fashions_private_limited.tenant_has_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.aza_fashions_private_limited
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  target_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement.account_data_binding_binds_to_table.table_zs_observe_paypal_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement.account_data_binding_binds_to_table.table_zs_observe_paypal_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  target_card_id: table.zs_observe.paypal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: table.zs_observe.razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_aza_fashions_private_limited_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform.platform_paypal

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform.platform_paypal
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform.paypal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform.platform_razorpay
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_paypal_global

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_paypal_global
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform_context.paypal.global
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_aza_fashions_private_limited_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_flow_binding.business_flow_binding_aza_fashions_private_limited_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_flow_binding.aza_fashions_private_limited.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_business_scope_set.business_scope_set_aza_fashions_private_limited_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: business_scope_set.aza_fashions_private_limited.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_paypal_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_aza_fashions_private_limited_g56_gl203.group_has_platform_account.platform_account_aza_fashions_private_limited_razorpay_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.aza_fashions_private_limited.g56.gl203
  target_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_belongs_to_group.group_aza_fashions_private_limited_g56_gl203
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  target_card_id: group.aza_fashions_private_limited.g56.gl203
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_paypal_settlement_zs_observe_paypal_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  target_card_id: account_data_binding.aza_fashions_private_limited.paypal.settlement.zs_observe_paypal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_aza_fashions_private_limited_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  target_card_id: account_data_binding.aza_fashions_private_limited.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_uses_platform.platform_paypal

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_uses_platform.platform_paypal
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  target_card_id: platform.paypal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_uses_platform_context.platform_context_paypal_global

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_paypal_payment_gateway.platform_account_uses_platform_context.platform_context_paypal_global
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.paypal.payment_gateway
  target_card_id: platform_context.paypal.global
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_aza_fashions_private_limited_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.aza_fashions_private_limited.razorpay.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
