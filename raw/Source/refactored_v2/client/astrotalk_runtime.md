# AstroTalk — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `astrotalk_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Snapmint
  config: snapmint_settlement
  reason: No Snapmint canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
- label: Shipway
  config: Invoice + Settlement report
  reason: No Shipway canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: Kwikship
  config: Invoice + Settlement
  reason: No Kwikship canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: Yolojet
  config: Invoice + Manual entry
  reason: No Yolojet canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: Criticalog
  config: Invoice only
  reason: No Criticalog canonical logistics platform/table cards in uploaded logistics_integrated.md
  source_family: logistics
- label: Petpooja
  config: restaurant/F&B POS
  reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
  source_family: oms
- label: Posist
  config: restaurant/F&B POS
  reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
  source_family: oms
- label: GoKwik
  config: gokwik_settlement
  reason: No GoKwik canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 8
  account_data_binding: 23
  business_scope_set: 5
  business_flow_binding: 5
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 39
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 23
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 23
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 5
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 23
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 8
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 5
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 5
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 23
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 7
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 8
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 8
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 5
  GROUP_HAS_BUSINESS_SCOPE_SET: 5
  GROUP_HAS_PLATFORM_ACCOUNT: 8
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 8
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 23
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
- wms
- payment_gateway
wms_integration:
  source_packs:
  - increff_wms.md
  - unicommerce_wms.md
  added_runtime_cards: 5
  added_runtime_edges: 25
  supported_wms_accounts: 1
  supported_wms_bindings: 2
  resolved_deferred_mentions: 1
bank_payment_integration:
  source_packs:
  - payment_gateway.md
  - bank_statement.md
  added_runtime_cards: 4
  added_runtime_edges: 18
  supported_payment_bindings: 1
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 1
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.astrotalk

```yaml
canonical_card:
  canonical_id: tenant.astrotalk
  card_type: tenant
  canonical_name: AstroTalk
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk
    - AstroTalk runtime tenant
    colloquial_phrases:
    - AstroTalk client runtime
    - AstroTalk source configuration
    - AstroTalk scoped reconciliation setup
    business_meaning: Runtime tenant identity for AstroTalk. It anchors the client's marketplace, logistics, OMS,
      WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to AstroTalk?
    - Which group and account bindings should constrain AstroTalk's SQL handoff?
    - After AstroTalk's runtime scope is resolved, which domain layer should receive the query next?
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
    - tenant_id:tenant.astrotalk
    embedding_text: AstroTalk is the runtime tenant root for the client's marketplace, logistics, OMS, WMS, payment-gateway,
      and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding nodes
      before invoking reusable canonical packs.
    search_keywords:
    - AstroTalk
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.astrotalk
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
  fields:
    tenant_slug: astrotalk
    tenant_name: AstroTalk
    legal_name: AstroTalk
    active: true
```

### 2.2 Group Cards

#### group.astrotalk.g60.gl221

```yaml
canonical_card:
  canonical_id: group.astrotalk.g60.gl221
  card_type: group
  canonical_name: AstroTalk group 60/221
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk
    - AstroTalk group 60/221
    - group_id 60
    - group_level_id 221
    colloquial_phrases:
    - AstroTalk group scope
    - AstroTalk runtime scope
    - group 60 level 221 query boundary
    business_meaning: 'Runtime group scope for AstroTalk: group_id=60 and group_level_id=221. It is the client-specific
      filter boundary that must be applied before resolving account bindings for IN in INR.'
    business_questions:
    - Which bindings use group_id=60 and group_level_id=221?
    - Which source families are active under AstroTalk?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=60
    - group_level_id=221
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - group_id_value:60
    - group_level_id_value:221
    embedding_text: AstroTalk is the runtime group node for AstroTalk. Apply group_id=60 and group_level_id=221
      when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - AstroTalk
    - group_id 60
    - group_level_id 221
    - runtime group scope
    exact_match_keys:
    - group.astrotalk.g60.gl221
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    group_level_id: '221'
  fields:
    tenant_id: tenant.astrotalk
    group_id_value: '60'
    group_level_id_value: '221'
    group_name: AstroTalk
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.astrotalk.amazon.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.amazon.marketplace
  card_type: platform_account
  canonical_name: AstroTalk — Amazon
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon
    - AstroTalk Amazon
    - Amazon marketplace account
    colloquial_phrases:
    - AstroTalk Amazon source account
    - Amazon marketplace runtime account
    - Amazon configured source family
    business_meaning: Runtime platform account for AstroTalk's Amazon marketplace sources. It points traversal to
      platform.amazon and platform_context.amazon.international and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Amazon table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Amazon questions traverse through?
    - Which source roles under Amazon are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: SKU master (product/ASIN–SKU reference lookup)'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    embedding_text: AstroTalk's Amazon platform account routes marketplace questions to platform.amazon / platform_context.amazon.international.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.astrotalk.amazon.marketplace
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.astrotalk.amazon.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon
    account_type: marketplace_seller_account
    source_account_identifier: Amazon
    active: true
    configured_source_description: SKU master (product/ASIN–SKU reference lookup)
```

#### platform_account.astrotalk.amazon_india.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.amazon_india.marketplace
  card_type: platform_account
  canonical_name: AstroTalk — Amazon India
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon India
    - AstroTalk Amazon India
    - Amazon
    - Amazon India marketplace account
    colloquial_phrases:
    - AstroTalk Amazon India source account
    - Amazon India marketplace runtime account
    - Amazon India configured source family
    business_meaning: Runtime platform account for AstroTalk's Amazon India marketplace sources. It points traversal
      to platform.amazon and platform_context.amazon.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Amazon India table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Amazon India questions traverse through?
    - Which source roles under Amazon India are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)'
    - platform.amazon
    - platform_context.amazon.in
    - Amazon India
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - platform_account_id:platform_account.astrotalk.amazon_india.marketplace
    embedding_text: AstroTalk's Amazon India platform account routes marketplace questions to platform.amazon /
      platform_context.amazon.in. Use it to collect the client's table bindings; do not use this account card as
      a table or metric definition.
    search_keywords:
    - AstroTalk
    - Amazon India
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.in
    exact_match_keys:
    - platform_account.astrotalk.amazon_india.marketplace
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_name: Amazon India
    account_type: marketplace_seller_account
    source_account_identifier: Amazon India
    active: true
    configured_source_description: OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
```

#### platform_account.astrotalk.flipkart.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.flipkart.marketplace
  card_type: platform_account
  canonical_name: AstroTalk — Flipkart
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart
    - AstroTalk Flipkart
    - Flipkart marketplace account
    colloquial_phrases:
    - AstroTalk Flipkart source account
    - Flipkart marketplace runtime account
    - Flipkart configured source family
    business_meaning: Runtime platform account for AstroTalk's Flipkart marketplace sources. It points traversal
      to platform.flipkart and platform_context.flipkart.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Flipkart table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Flipkart questions traverse through?
    - Which source roles under Flipkart are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)'
    - platform.flipkart
    - platform_context.flipkart.in
    - Flipkart
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - platform_account_id:platform_account.astrotalk.flipkart.marketplace
    embedding_text: AstroTalk's Flipkart platform account routes marketplace questions to platform.flipkart / platform_context.flipkart.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - Flipkart
    - marketplace
    - platform.flipkart
    - platform_context.flipkart.in
    exact_match_keys:
    - platform_account.astrotalk.flipkart.marketplace
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_name: Flipkart
    account_type: marketplace_seller_account
    source_account_identifier: Flipkart
    active: true
    configured_source_description: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### platform_account.astrotalk.myntra.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.myntra.marketplace
  card_type: platform_account
  canonical_name: AstroTalk — Myntra
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra
    - AstroTalk Myntra
    - Myntra marketplace account
    colloquial_phrases:
    - AstroTalk Myntra source account
    - Myntra marketplace runtime account
    - Myntra configured source family
    business_meaning: Runtime platform account for AstroTalk's Myntra marketplace sources. It points traversal to
      platform.myntra and platform_context.myntra.in and groups the client's table-level account-data bindings for
      this source.
    business_questions:
    - Which Myntra table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Myntra questions traverse through?
    - Which source roles under Myntra are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses'
    - platform.myntra
    - platform_context.myntra.in
    - Myntra
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - platform_account_id:platform_account.astrotalk.myntra.marketplace
    embedding_text: AstroTalk's Myntra platform account routes marketplace questions to platform.myntra / platform_context.myntra.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - Myntra
    - marketplace
    - platform.myntra
    - platform_context.myntra.in
    exact_match_keys:
    - platform_account.astrotalk.myntra.marketplace
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    platform_account_id: platform_account.astrotalk.myntra.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_name: Myntra
    account_type: marketplace_seller_account
    source_account_identifier: Myntra
    active: true
    configured_source_description: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP),
      Non-order settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS
      expenses
```

#### platform_account.astrotalk.shiprocket.logistics

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.shiprocket.logistics
  card_type: platform_account
  canonical_name: AstroTalk Shiprocket Logistics Aggregator account
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk Shiprocket Logistics Aggregator account
    - AstroTalk AstroTalk Shiprocket Logistics Aggregator account
    - Shiprocket
    - AstroTalk Shiprocket Logistics Aggregator account logistics / courier account
    colloquial_phrases:
    - AstroTalk AstroTalk Shiprocket Logistics Aggregator account source account
    - AstroTalk Shiprocket Logistics Aggregator account logistics / courier runtime account
    - AstroTalk Shiprocket Logistics Aggregator account configured source family
    business_meaning: Runtime platform account for AstroTalk's AstroTalk Shiprocket Logistics Aggregator account
      logistics / courier sources. It points traversal to platform.shiprocket and platform_context.shiprocket.in
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which AstroTalk Shiprocket Logistics Aggregator account table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's AstroTalk Shiprocket Logistics Aggregator account questions
      traverse through?
    - Which source roles under AstroTalk Shiprocket Logistics Aggregator account are active or review-required for
      this client?
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - runtime_source_family:logistics
    embedding_text: AstroTalk's AstroTalk Shiprocket Logistics Aggregator account platform account routes logistics
      / courier questions to platform.shiprocket / platform_context.shiprocket.in. Use it to collect the client's
      table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - AstroTalk Shiprocket Logistics Aggregator account
    - Shiprocket
    - logistics / courier
    - platform.shiprocket
    - platform_context.shiprocket.in
    exact_match_keys:
    - platform_account.astrotalk.shiprocket.logistics
  evidence:
    source_documents:
    - AstroTalk.docx
    - logistics_integrated.md
    source_path: AstroTalk.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_name: AstroTalk Shiprocket Logistics Aggregator account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '60'
      group_level_id: '221'
```

#### platform_account.astrotalk.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.shopify_d2c.oms
  card_type: platform_account
  canonical_name: AstroTalk Shopify D2C OMS account
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk Shopify D2C OMS account
    - AstroTalk AstroTalk Shopify D2C OMS account
    - Shopify
    - AstroTalk Shopify D2C OMS account OMS account
    colloquial_phrases:
    - AstroTalk AstroTalk Shopify D2C OMS account source account
    - AstroTalk Shopify D2C OMS account OMS runtime account
    - AstroTalk Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for AstroTalk's AstroTalk Shopify D2C OMS account OMS sources. It
      points traversal to platform.shopify and platform_context.shopify.in.d2c_oms and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which AstroTalk Shopify D2C OMS account table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's AstroTalk Shopify D2C OMS account questions traverse through?
    - Which source roles under AstroTalk Shopify D2C OMS account are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - OMS
    - source_router
    included_concepts:
    - 'client configuration: Shopify D2C OMS and returns/refund events'
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: AstroTalk's AstroTalk Shopify D2C OMS account platform account routes OMS questions to platform.shopify
      / platform_context.shopify.in.d2c_oms. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - AstroTalk Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.astrotalk.shopify_d2c.oms
  evidence:
    source_documents:
    - AstroTalk.docx
    - shopify_d2c_oms.md
    source_path: AstroTalk.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: AstroTalk Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    group_scope_values:
      group_id: '60'
      group_level_id: '221'
```

#### platform_account.astrotalk.unicommerce_wms.wms

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.unicommerce_wms.wms
  card_type: platform_account
  canonical_name: AstroTalk — Unicommerce WMS
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS
    - AstroTalk Unicommerce WMS
    - Unicommerce
    - Unicommerce WMS WMS account
    colloquial_phrases:
    - AstroTalk Unicommerce WMS source account
    - Unicommerce WMS WMS runtime account
    - Unicommerce WMS configured source family
    business_meaning: Runtime platform account for AstroTalk's Unicommerce WMS WMS sources. It points traversal
      to platform.unicommerce and platform_context.unicommerce.in_wms and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Unicommerce WMS table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Unicommerce WMS questions traverse through?
    - Which source roles under Unicommerce WMS are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - WMS
    - source_router
    included_concepts:
    - 'client configuration: order management / marketplace sync / WMS fulfilment'
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    - Unicommerce WMS
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - platform_account_id:platform_account.astrotalk.unicommerce_wms.wms
    - runtime_source_family:wms
    embedding_text: AstroTalk's Unicommerce WMS platform account routes WMS questions to platform.unicommerce /
      platform_context.unicommerce.in_wms. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - AstroTalk
    - Unicommerce WMS
    - Unicommerce
    - WMS
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    exact_match_keys:
    - platform_account.astrotalk.unicommerce_wms.wms
  evidence:
    source_documents:
    - AstroTalk.docx
    - unicommerce_wms.md
    source_path: AstroTalk.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
    runtime_source_family: wms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    account_name: Unicommerce WMS
    account_type: wms_operator_account
    source_account_identifier: Unicommerce WMS
    source_account_identifier_status: client_docx_names_wms_system_without_separate_account_number
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    group_scope_values:
      group_id: '60'
      group_level_id: '221'
```

#### platform_account.astrotalk.razorpay.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.astrotalk.razorpay.payment_gateway
  card_type: platform_account
  canonical_name: AstroTalk — Razorpay payment gateway
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Razorpay
    - AstroTalk Razorpay
    - Razorpay payment gateway account
    colloquial_phrases:
    - AstroTalk Razorpay source account
    - Razorpay payment gateway runtime account
    - Razorpay configured source family
    business_meaning: Runtime platform account for AstroTalk's Razorpay payment gateway sources. It points traversal
      to platform.razorpay and platform_context.razorpay.in and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Razorpay table bindings are available for AstroTalk?
    - Which canonical platform/context should AstroTalk's Razorpay questions traverse through?
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - platform_account_id:platform_account.astrotalk.razorpay.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: AstroTalk's Razorpay platform account routes payment gateway questions to platform.razorpay
      / platform_context.razorpay.in. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - AstroTalk
    - Razorpay
    - payment gateway
    - platform.razorpay
    - platform_context.razorpay.in
    exact_match_keys:
    - platform_account.astrotalk.razorpay.payment_gateway
  evidence:
    source_documents:
    - AstroTalk.docx
    - payment_gateway.md
    source_path: AstroTalk.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    platform_account_id: platform_account.astrotalk.razorpay.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
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
      group_id: '60'
      group_level_id: '221'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon — disbursement
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon disbursement
    - amazon_disbursment
    - zs_observe.amazon_disbursment
    - SKU master (product/ASIN–SKU reference lookup)
    - AstroTalk Amazon disbursement
    colloquial_phrases:
    - AstroTalk Amazon disbursement source
    - Amazon disbursement runtime binding
    - amazon_disbursment for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon disbursement evidence
      should use zs_observe.amazon_disbursment. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon disbursement file/table is active for AstroTalk?
    - Which group filters keep amazon_disbursment limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - disbursement
    included_concepts:
    - zs_observe.amazon_disbursment
    - disbursement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:disbursement
    - table_id:table.zs_observe.amazon_disbursment
    embedding_text: 'For AstroTalk, the Amazon disbursement binding selects zs_observe.amazon_disbursment as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - disbursement
    - marketplace
    - zs_observe.amazon_disbursment
    - amazon_disbursment
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
  fields:
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: SKU master (product/ASIN–SKU reference lookup)
```

#### account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon — fee_preview
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon fee preview
    - amazon_fee_preview
    - zs_observe.amazon_fee_preview
    - SKU master (product/ASIN–SKU reference lookup)
    - AstroTalk Amazon fee preview
    colloquial_phrases:
    - AstroTalk Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon fee preview evidence
      should use zs_observe.amazon_fee_preview. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for AstroTalk?
    - Which group filters keep amazon_fee_preview limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - fee_preview
    included_concepts:
    - zs_observe.amazon_fee_preview
    - fee preview
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For AstroTalk, the Amazon fee preview binding selects zs_observe.amazon_fee_preview as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: SKU master (product/ASIN–SKU reference lookup)
```

#### account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon — oms_sales
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon OMS sales
    - amazon_oms
    - zs_observe.amazon_oms
    - SKU master (product/ASIN–SKU reference lookup)
    - AstroTalk Amazon OMS sales
    colloquial_phrases:
    - AstroTalk Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon OMS sales evidence should
      use zs_observe.amazon_oms. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for AstroTalk?
    - Which group filters keep amazon_oms limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.amazon_oms
    - OMS sales
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For AstroTalk, the Amazon OMS sales binding selects zs_observe.amazon_oms as marketplace evidence.
      Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical pack.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_oms.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: SKU master (product/ASIN–SKU reference lookup)
```

#### account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon — returns
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon returns
    - amazon_returns
    - zs_observe.amazon_returns
    - SKU master (product/ASIN–SKU reference lookup)
    - AstroTalk Amazon returns
    colloquial_phrases:
    - AstroTalk Amazon returns source
    - Amazon returns runtime binding
    - amazon_returns for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon returns evidence should
      use zs_observe.amazon_returns. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Amazon returns file/table is active for AstroTalk?
    - Which group filters keep amazon_returns limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.amazon_returns
    - returns
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:returns
    - table_id:table.zs_observe.amazon_returns
    embedding_text: 'For AstroTalk, the Amazon returns binding selects zs_observe.amazon_returns as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - returns
    - marketplace
    - zs_observe.amazon_returns
    - amazon_returns
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
    table_id: table.zs_observe.amazon_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    table_id: table.zs_observe.amazon_returns
    source_role: returns
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_returns.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: SKU master (product/ASIN–SKU reference lookup)
```

#### account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon — settlement
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon settlement
    - amazon_settlement
    - zs_observe.amazon_settlement
    - SKU master (product/ASIN–SKU reference lookup)
    - AstroTalk Amazon settlement
    colloquial_phrases:
    - AstroTalk Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon settlement evidence should
      use zs_observe.amazon_settlement. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for AstroTalk?
    - Which group filters keep amazon_settlement limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.amazon_settlement
    - settlement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For AstroTalk, the Amazon settlement binding selects zs_observe.amazon_settlement as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.astrotalk.amazon.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: SKU master (product/ASIN–SKU reference lookup)
```

#### account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon India — disbursement
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon disbursement
    - amazon_disbursment
    - zs_observe.amazon_disbursment
    - OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
    - AstroTalk Amazon disbursement
    colloquial_phrases:
    - AstroTalk Amazon disbursement source
    - Amazon disbursement runtime binding
    - amazon_disbursment for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon disbursement evidence
      should use zs_observe.amazon_disbursment. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon disbursement file/table is active for AstroTalk?
    - Which group filters keep amazon_disbursment limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - disbursement
    included_concepts:
    - zs_observe.amazon_disbursment
    - disbursement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:disbursement
    - table_id:table.zs_observe.amazon_disbursment
    embedding_text: 'For AstroTalk, the Amazon disbursement binding selects zs_observe.amazon_disbursment as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - disbursement
    - marketplace
    - zs_observe.amazon_disbursment
    - amazon_disbursment
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
  fields:
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
```

#### account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon India — oms_sales
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon OMS sales
    - amazon_oms
    - zs_observe.amazon_oms
    - OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
    - AstroTalk Amazon OMS sales
    colloquial_phrases:
    - AstroTalk Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon OMS sales evidence should
      use zs_observe.amazon_oms. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for AstroTalk?
    - Which group filters keep amazon_oms limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.amazon_oms
    - OMS sales
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For AstroTalk, the Amazon OMS sales binding selects zs_observe.amazon_oms as marketplace evidence.
      Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical pack.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_oms.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
```

#### account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: AstroTalk — Amazon India — settlement
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
    vendor_or_system: Amazon
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Amazon settlement
    - amazon_settlement
    - zs_observe.amazon_settlement
    - OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
    - AstroTalk Amazon settlement
    colloquial_phrases:
    - AstroTalk Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Amazon settlement evidence should
      use zs_observe.amazon_settlement. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for AstroTalk?
    - Which group filters keep amazon_settlement limited to AstroTalk?
    - What Amazon canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.amazon_settlement
    - settlement
    - Amazon
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For AstroTalk, the Amazon settlement binding selects zs_observe.amazon_settlement as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.astrotalk.amazon_india.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, SKU master (lookup)
```

#### account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  card_type: account_data_binding
  canonical_name: AstroTalk — Flipkart — cashback_credit_debit_note
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart cashback / credit-debit note
    - flipkart_cashback
    - zs_observe.flipkart_cashback
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - AstroTalk Flipkart cashback / credit-debit note
    colloquial_phrases:
    - AstroTalk Flipkart cashback / credit-debit note source
    - Flipkart cashback / credit-debit note runtime binding
    - flipkart_cashback for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Flipkart cashback / credit-debit
      note evidence should use zs_observe.flipkart_cashback. Apply group_id=60, group_level_id=221 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart cashback / credit-debit note file/table is active for AstroTalk?
    - Which group filters keep flipkart_cashback limited to AstroTalk?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - cashback_credit_debit_note
    included_concepts:
    - zs_observe.flipkart_cashback
    - cashback / credit-debit note
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:cashback_credit_debit_note
    - table_id:table.zs_observe.flipkart_cashback
    embedding_text: 'For AstroTalk, the Flipkart cashback / credit-debit note binding selects zs_observe.flipkart_cashback
      as marketplace evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Flipkart
    - cashback / credit-debit note
    - marketplace
    - zs_observe.flipkart_cashback
    - flipkart_cashback
    - cashback_credit_debit_note
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
  fields:
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  card_type: account_data_binding
  canonical_name: AstroTalk — Flipkart — commission_fee_invoice
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart commission invoice
    - flipkart_commission
    - zs_observe.flipkart_commission
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - AstroTalk Flipkart commission invoice
    colloquial_phrases:
    - AstroTalk Flipkart commission invoice source
    - Flipkart commission invoice runtime binding
    - flipkart_commission for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Flipkart commission invoice
      evidence should use zs_observe.flipkart_commission. Apply group_id=60, group_level_id=221 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart commission invoice file/table is active for AstroTalk?
    - Which group filters keep flipkart_commission limited to AstroTalk?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - commission_fee_invoice
    included_concepts:
    - zs_observe.flipkart_commission
    - commission invoice
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:commission_fee_invoice
    - table_id:table.zs_observe.flipkart_commission
    embedding_text: 'For AstroTalk, the Flipkart commission invoice binding selects zs_observe.flipkart_commission
      as marketplace evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Flipkart
    - commission invoice
    - marketplace
    - zs_observe.flipkart_commission
    - flipkart_commission
    - commission_fee_invoice
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
  fields:
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_commission.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_commission.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  card_type: account_data_binding
  canonical_name: AstroTalk — Flipkart — oms_sales
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart OMS sales
    - flipkart_oms
    - zs_recon_processor.flipkart_oms
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - AstroTalk Flipkart OMS sales
    colloquial_phrases:
    - AstroTalk Flipkart OMS sales source
    - Flipkart OMS sales runtime binding
    - flipkart_oms for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Flipkart OMS sales evidence
      should use zs_recon_processor.flipkart_oms. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart OMS sales file/table is active for AstroTalk?
    - Which group filters keep flipkart_oms limited to AstroTalk?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_recon_processor.flipkart_oms
    - OMS sales
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:oms_sales
    - table_id:table.zs_recon_processor.flipkart_oms
    embedding_text: 'For AstroTalk, the Flipkart OMS sales binding selects zs_recon_processor.flipkart_oms as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Flipkart
    - OMS sales
    - marketplace
    - zs_recon_processor.flipkart_oms
    - flipkart_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
    source_entity: Flipkart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_recon_processor.flipkart_oms.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  card_type: account_data_binding
  canonical_name: AstroTalk — Flipkart — settlement
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
    vendor_or_system: Flipkart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Flipkart settlement
    - flipkart_settlement
    - zs_observe.flipkart_settlement
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
    - AstroTalk Flipkart settlement
    colloquial_phrases:
    - AstroTalk Flipkart settlement source
    - Flipkart settlement runtime binding
    - flipkart_settlement for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Flipkart settlement evidence
      should use zs_observe.flipkart_settlement. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart settlement file/table is active for AstroTalk?
    - Which group filters keep flipkart_settlement limited to AstroTalk?
    - What Flipkart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.flipkart_settlement
    - settlement
    - Flipkart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:settlement
    - table_id:table.zs_observe.flipkart_settlement
    embedding_text: 'For AstroTalk, the Flipkart settlement binding selects zs_observe.flipkart_settlement as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Flipkart
    - settlement
    - marketplace
    - zs_observe.flipkart_settlement
    - flipkart_settlement
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.astrotalk.flipkart.marketplace
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads)
```

#### account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  card_type: account_data_binding
  canonical_name: AstroTalk — Myntra — non_order_settlement
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra non-order settlement
    - myntra_non_order_settlement
    - zs_observe.myntra_non_order_settlement
    - OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order settlement (JIT +
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
    - AstroTalk Myntra non-order settlement
    colloquial_phrases:
    - AstroTalk Myntra non-order settlement source
    - Myntra non-order settlement runtime binding
    - myntra_non_order_settlement for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Myntra non-order settlement
      evidence should use zs_observe.myntra_non_order_settlement. Apply group_id=60, group_level_id=221 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra non-order settlement file/table is active for AstroTalk?
    - Which group filters keep myntra_non_order_settlement limited to AstroTalk?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - non_order_settlement
    included_concepts:
    - zs_observe.myntra_non_order_settlement
    - non-order settlement
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:non_order_settlement
    - table_id:table.zs_observe.myntra_non_order_settlement
    embedding_text: 'For AstroTalk, the Myntra non-order settlement binding selects zs_observe.myntra_non_order_settlement
      as marketplace evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Myntra
    - non-order settlement
    - marketplace
    - zs_observe.myntra_non_order_settlement
    - myntra_non_order_settlement
    - non_order_settlement
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
  fields:
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
```

#### account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  card_type: account_data_binding
  canonical_name: AstroTalk — Myntra — oms_sales
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra OMS sales
    - myntra_oms
    - zs_observe.myntra_oms
    - OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order settlement (JIT +
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
    - AstroTalk Myntra OMS sales
    colloquial_phrases:
    - AstroTalk Myntra OMS sales source
    - Myntra OMS sales runtime binding
    - myntra_oms for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Myntra OMS sales evidence should
      use zs_observe.myntra_oms. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Myntra OMS sales file/table is active for AstroTalk?
    - Which group filters keep myntra_oms limited to AstroTalk?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.myntra_oms
    - OMS sales
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:oms_sales
    - table_id:table.zs_observe.myntra_oms
    embedding_text: 'For AstroTalk, the Myntra OMS sales binding selects zs_observe.myntra_oms as marketplace evidence.
      Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical pack.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Myntra
    - OMS sales
    - marketplace
    - zs_observe.myntra_oms
    - myntra_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_oms.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_oms.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
```

#### account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  card_type: account_data_binding
  canonical_name: AstroTalk — Myntra — returns
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra returns
    - myntra_reverse
    - zs_observe.myntra_reverse
    - OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order settlement (JIT +
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
    - AstroTalk Myntra returns
    colloquial_phrases:
    - AstroTalk Myntra returns source
    - Myntra returns runtime binding
    - myntra_reverse for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Myntra returns evidence should
      use zs_observe.myntra_reverse. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field, metric,
      and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Myntra returns file/table is active for AstroTalk?
    - Which group filters keep myntra_reverse limited to AstroTalk?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.myntra_reverse
    - returns
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:returns
    - table_id:table.zs_observe.myntra_reverse
    embedding_text: 'For AstroTalk, the Myntra returns binding selects zs_observe.myntra_reverse as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Myntra
    - returns
    - marketplace
    - zs_observe.myntra_reverse
    - myntra_reverse
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
  fields:
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_reverse.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_reverse.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
```

#### account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  card_type: account_data_binding
  canonical_name: AstroTalk — Myntra — settlement
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
    vendor_or_system: Myntra
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Myntra settlement
    - myntra_settlement
    - zs_observe.myntra_settlement
    - OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order settlement (JIT +
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
    - AstroTalk Myntra settlement
    colloquial_phrases:
    - AstroTalk Myntra settlement source
    - Myntra settlement runtime binding
    - myntra_settlement for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Myntra settlement evidence should
      use zs_observe.myntra_settlement. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Myntra settlement file/table is active for AstroTalk?
    - Which group filters keep myntra_settlement limited to AstroTalk?
    - What Myntra canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.myntra_settlement
    - settlement
    - Myntra
    - marketplace source role
    - client-scoped marketplace table
    - group_id=60
    - group_level_id=221
    - uploaded marketplace canonical pack
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - Marketplace runtime bindings select client-specific files; reusable marketplace semantics and sign rules remain
      in the vendor pack.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:settlement
    - table_id:table.zs_observe.myntra_settlement
    embedding_text: 'For AstroTalk, the Myntra settlement binding selects zs_observe.myntra_settlement as marketplace
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Myntra
    - settlement
    - marketplace
    - zs_observe.myntra_settlement
    - myntra_settlement
    - uploaded marketplace canonical pack
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.astrotalk.myntra.marketplace
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_settlement.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_settlement.group_level_id
      runtime_value: '221'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses
```

#### account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  card_type: account_data_binding
  canonical_name: AstroTalk Shiprocket Logistics Aggregator logistics_cod_settlement_report_schema_only binding
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shiprocket Logistics Aggregator logistics cod settlement report schema only
    - shiprocket_settlement_report
    - zs_observe.shiprocket_settlement_report
    - table.zs_observe.shiprocket_invoice, table.zs_observe.shiprocket_settlement_report
    - AstroTalk Shiprocket Logistics Aggregator logistics cod settlement report schema only
    colloquial_phrases:
    - AstroTalk Shiprocket Logistics Aggregator logistics cod settlement report schema only source
    - Shiprocket Logistics Aggregator logistics cod settlement report schema only runtime binding
    - shiprocket_settlement_report for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Shiprocket Logistics Aggregator
      logistics cod settlement report schema only evidence should use zs_observe.shiprocket_settlement_report. Apply
      client runtime scope before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Shiprocket Logistics Aggregator logistics rows should answer AstroTalk's logistics cod settlement report
      schema only question?
    - Which courier/account scope must be applied before using shiprocket_settlement_report?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - logistics_cod_settlement_report_schema_only
    included_concepts:
    - zs_observe.shiprocket_settlement_report
    - logistics cod settlement report schema only
    - Shiprocket Logistics Aggregator
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - source_role:logistics_cod_settlement_report_schema_only
    - table_id:table.zs_observe.shiprocket_settlement_report
    - runtime_source_family:logistics
    embedding_text: 'For AstroTalk, the Shiprocket Logistics Aggregator logistics cod settlement report schema only
      binding selects zs_observe.shiprocket_settlement_report as logistics / courier evidence. Runtime scope must
      be supplied before SQL. Reusable semantics come from logistics_integrated.md. Coverage status: review_required.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Shiprocket Logistics Aggregator
    - logistics cod settlement report schema only
    - logistics / courier
    - zs_observe.shiprocket_settlement_report
    - shiprocket_settlement_report
    - logistics_cod_settlement_report_schema_only
    - logistics_integrated.md
    exact_match_keys:
    - account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  evidence:
    source_documents:
    - AstroTalk.docx
    - logistics_integrated.md
    source_path: AstroTalk.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_data_binding_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
    table_id: table.zs_observe.shiprocket_settlement_report
    source_role: logistics_cod_settlement_report_schema_only
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.astrotalk.shiprocket.logistics
    table_id: table.zs_observe.shiprocket_settlement_report
    source_role: logistics_cod_settlement_report_schema_only
    source_entity: Shiprocket Logistics Aggregator
    scope_keys: []
    scope_key_status: no_documented_group_level_scope_column_in_reusable_logistics_table_card
    active: false
    source_configuration_text: table.zs_observe.shiprocket_invoice, table.zs_observe.shiprocket_settlement_report
    canonical_table_coverage_status: review_required
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  card_type: account_data_binding
  canonical_name: AstroTalk Shiprocket Logistics Aggregator logistics_freight_invoice binding
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
    vendor_or_system: AstroTalk
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
    - table.zs_observe.shiprocket_invoice, table.zs_observe.shiprocket_settlement_report
    - AstroTalk Shiprocket Logistics Aggregator freight invoice
    colloquial_phrases:
    - AstroTalk Shiprocket Logistics Aggregator freight invoice source
    - Shiprocket Logistics Aggregator freight invoice runtime binding
    - shiprocket_invoice for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Shiprocket Logistics Aggregator
      freight invoice evidence should use zs_observe.shiprocket_invoice. Apply group_level_id=221 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Shiprocket Logistics Aggregator logistics rows should answer AstroTalk's freight invoice question?
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
    - group_level_id=221
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - source_role:logistics_freight_invoice
    - table_id:table.zs_observe.shiprocket_invoice
    - runtime_source_family:logistics
    embedding_text: 'For AstroTalk, the Shiprocket Logistics Aggregator freight invoice binding selects zs_observe.shiprocket_invoice
      as logistics / courier evidence. Scope: group_level_id=221. Reusable semantics come from logistics_integrated.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Shiprocket Logistics Aggregator
    - freight invoice
    - logistics / courier
    - zs_observe.shiprocket_invoice
    - shiprocket_invoice
    - logistics_freight_invoice
    - logistics_integrated.md
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  evidence:
    source_documents:
    - AstroTalk.docx
    - logistics_integrated.md
    source_path: AstroTalk.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_data_binding_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    table_id: table.zs_observe.shiprocket_invoice
    source_role: logistics_freight_invoice
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.astrotalk.shiprocket.logistics
    table_id: table.zs_observe.shiprocket_invoice
    source_role: logistics_freight_invoice
    source_entity: Shiprocket Logistics Aggregator
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shiprocket_invoice.group_level_id
      runtime_value: '221'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.shiprocket_invoice, table.zs_observe.shiprocket_settlement_report
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: AstroTalk Shopify D2C OMS oms_sales binding
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shopify D2C OMS OMS sales
    - shopify_oms
    - zs_observe.shopify_oms
    - Shopify D2C OMS and returns/refund events
    - AstroTalk Shopify D2C OMS OMS sales
    colloquial_phrases:
    - AstroTalk Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Shopify D2C OMS OMS sales evidence
      should use zs_observe.shopify_oms. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer AstroTalk's OMS sales question?
    - Which runtime scope must be injected before using shopify_oms?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - oms_sales
    included_concepts:
    - zs_observe.shopify_oms
    - OMS sales
    - Shopify D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=60
    - group_level_id=221
    - shopify_d2c_oms.md
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For AstroTalk, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms as OMS
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - AstroTalk.docx
    - shopify_d2c_oms.md
    source_path: AstroTalk.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.astrotalk.shopify_d2c.oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    source_entity: Shopify D2C OMS
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '60'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.shopify_oms.group_id
      runtime_value: '60'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '221'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: AstroTalk Shopify D2C OMS returns binding
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shopify D2C OMS returns
    - shopify_returns
    - zs_observe.shopify_returns
    - Shopify D2C OMS and returns/refund events
    - AstroTalk Shopify D2C OMS returns
    colloquial_phrases:
    - AstroTalk Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Shopify D2C OMS returns evidence
      should use zs_observe.shopify_returns. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer AstroTalk's returns question?
    - Which runtime scope must be injected before using shopify_returns?
    - Which payment, bank, WMS, or logistics actual source is needed for reconciliation beyond OMS expectation?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - OMS
    - returns
    included_concepts:
    - zs_observe.shopify_returns
    - returns
    - Shopify D2C OMS
    - order-side evidence
    - invoice/order lifecycle
    - group_id=60
    - group_level_id=221
    - shopify_d2c_oms.md
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For AstroTalk, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns as OMS
      evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - AstroTalk.docx
    - shopify_d2c_oms.md
    source_path: AstroTalk.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.astrotalk.shopify_d2c.oms
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    source_entity: Shopify D2C OMS
    scope_keys:
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  card_type: account_data_binding
  canonical_name: AstroTalk Unicommerce WMS invoice transaction ledger binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS WMS invoice transaction ledger
    - unicommerce
    - zs_observe.unicommerce
    - order management / marketplace sync / WMS fulfilment
    - AstroTalk Unicommerce WMS WMS invoice transaction ledger
    colloquial_phrases:
    - AstroTalk Unicommerce WMS WMS invoice transaction ledger source
    - Unicommerce WMS WMS invoice transaction ledger runtime binding
    - unicommerce for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Unicommerce WMS WMS invoice
      transaction ledger evidence should use zs_observe.unicommerce. Apply group_level_id=221 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer AstroTalk's WMS invoice transaction ledger question?
    - Which group scope and active-row filters apply before querying unicommerce?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_invoice_transaction_ledger
    included_concepts:
    - zs_observe.unicommerce
    - WMS invoice transaction ledger
    - Unicommerce WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=221
    - unicommerce_wms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - WMS evidence is operational fulfilment or return evidence; do not treat it as payout, bank, or marketplace
      settlement proof.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce
    - source_role:wms_invoice_transaction_ledger
    - runtime_source_family:wms
    embedding_text: 'For AstroTalk, the Unicommerce WMS WMS invoice transaction ledger binding selects zs_observe.unicommerce
      as WMS evidence. Scope: group_level_id=221. Reusable semantics come from unicommerce_wms.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Unicommerce WMS
    - WMS invoice transaction ledger
    - WMS
    - zs_observe.unicommerce
    - unicommerce
    - wms_invoice_transaction_ledger
    - unicommerce_wms.md
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  evidence:
    source_documents:
    - AstroTalk.docx
    - unicommerce_wms.md
    source_path: AstroTalk.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    runtime_source_family: wms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    canonical_table_id: table.zs_observe.unicommerce
    physical_table_reference: zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    source_role_label: invoice transaction ledger
    source_family: wms
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce.group_level_id
      runtime_value: '221'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter
    - metadata filter when separating sales, returns, or cancellations
    grain_from_reusable_pack: order or SKU invoice transaction row carrying sales, reverse return, or cancellation
      classification
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  card_type: account_data_binding
  canonical_name: AstroTalk Unicommerce WMS order sales report shipment tracking binding
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS WMS shipment tracking
    - unicommerce_order_sales_report
    - zs_observe.unicommerce_order_sales_report
    - order management / marketplace sync / WMS fulfilment
    - AstroTalk Unicommerce WMS WMS shipment tracking
    colloquial_phrases:
    - AstroTalk Unicommerce WMS WMS shipment tracking source
    - Unicommerce WMS WMS shipment tracking runtime binding
    - unicommerce_order_sales_report for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Unicommerce WMS WMS shipment
      tracking evidence should use zs_observe.unicommerce_order_sales_report. Apply group_level_id=221 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer AstroTalk's WMS shipment tracking question?
    - Which group scope and active-row filters apply before querying unicommerce_order_sales_report?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_shipment_tracking
    included_concepts:
    - zs_observe.unicommerce_order_sales_report
    - WMS shipment tracking
    - Unicommerce WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=221
    - unicommerce_wms.md
    excluded_concepts:
    - reusable table schema
    - metric formulas
    - tenant-independent domain semantics
    caveats:
    - Do not copy reusable platform, table, column, metric, or reconciliation semantics into this runtime binding.
    - WMS evidence is operational fulfilment or return evidence; do not treat it as payout, bank, or marketplace
      settlement proof.
    examples: []
  retrieval:
    node_sets:
    - card_type:account_data_binding
    - domain_family:client_runtime
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce_order_sales_report
    - source_role:wms_shipment_tracking
    - runtime_source_family:wms
    embedding_text: 'For AstroTalk, the Unicommerce WMS WMS shipment tracking binding selects zs_observe.unicommerce_order_sales_report
      as WMS evidence. Scope: group_level_id=221. Reusable semantics come from unicommerce_wms.md. Coverage status:
      active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Unicommerce WMS
    - WMS shipment tracking
    - WMS
    - zs_observe.unicommerce_order_sales_report
    - unicommerce_order_sales_report
    - wms_shipment_tracking
    - unicommerce_wms.md
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  evidence:
    source_documents:
    - AstroTalk.docx
    - unicommerce_wms.md
    source_path: AstroTalk.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    runtime_source_family: wms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    canonical_table_id: table.zs_observe.unicommerce_order_sales_report
    physical_table_reference: zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    source_role_label: order sales report shipment tracking
    source_family: wms
    configured_source_description: order management / marketplace sync / WMS fulfilment
    canonical_source_pack: unicommerce_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '221'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
      runtime_value: '221'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter when available
    grain_from_reusable_pack: shipment or order-SKU operational row carrying delivery status, AWB, courier method,
      MRP and package dimensions
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  card_type: account_data_binding
  canonical_name: AstroTalk Razorpay payment gateway reconciliation binding
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
    vendor_or_system: AstroTalk
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
    - AstroTalk Razorpay settlement
    colloquial_phrases:
    - AstroTalk Razorpay settlement source
    - Razorpay settlement runtime binding
    - razorpay_payin for AstroTalk
    business_meaning: This account-data binding tells the resolver that AstroTalk's Razorpay settlement evidence
      should use zs_observe.razorpay_payin. Apply group_id=60, group_level_id=221 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing bridge, not a reusable
      domain card.
    business_questions:
    - Which Razorpay settlement rows represent expected gateway evidence for AstroTalk?
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
    - group_id=60
    - group_level_id=221
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - platform_account_id:platform_account.astrotalk.razorpay.payment_gateway
    - platform_id:platform.razorpay
    - platform_context_id:platform_context.razorpay.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.razorpay_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For AstroTalk, the Razorpay settlement binding selects zs_observe.razorpay_payin as payment
      gateway evidence. Scope: group_id=60, group_level_id=221. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - AstroTalk
    - Razorpay
    - settlement
    - payment gateway
    - zs_observe.razorpay_payin
    - razorpay_payin
    - payment_gateway.md
    - group_id=60
    - group_level_id=221
    exact_match_keys:
    - account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  evidence:
    source_documents:
    - AstroTalk.docx
    - payment_gateway.md
    source_path: AstroTalk.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    platform_account_id: platform_account.astrotalk.razorpay.payment_gateway
    platform_id: platform.razorpay
    platform_context_id: platform_context.razorpay.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.razorpay_payin
    canonical_table_id: table.zs_observe.razorpay_payin
    physical_table_reference: zs_observe.razorpay_payin
    configured_pipeline_target: razorpay_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Razorpay payment gateway reconciliation
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '60'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '60'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '221'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '221'
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


### 2.5 Business Scope Set Cards

#### business_scope_set.astrotalk.logistics

```yaml
canonical_card:
  canonical_id: business_scope_set.astrotalk.logistics
  card_type: business_scope_set
  canonical_name: AstroTalk logistics scope
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - AstroTalk.docx
    - logistics_integrated.md
    source_path: AstroTalk.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_scope_set_id: business_scope_set.astrotalk.logistics
    runtime_source_family: logistics
  semantic:
    aliases:
    - AstroTalk logistics scope
    - AstroTalk logistics / courier scope
    - logistics / courier runtime scope set
    colloquial_phrases:
    - AstroTalk logistics / courier scope
    - logistics / courier accounts and bindings
    - AstroTalk logistics / courier resolver input
    business_meaning: Business scope set for AstroTalk's logistics / courier runtime resolution. It groups 1 platform
      accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which logistics / courier accounts and bindings are active for AstroTalk?
    - Which runtime table bindings should be considered together under AstroTalk logistics scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - logistics_courier
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 4 deferred sources
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - business_scope_set_id:business_scope_set.astrotalk.logistics
    - runtime_source_family:logistics
    embedding_text: AstroTalk logistics scope groups AstroTalk's logistics / courier runtime accounts and table
      bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain deferred
      until supported canonical packs exist.
    search_keywords:
    - AstroTalk
    - AstroTalk logistics scope
    - logistics / courier
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.astrotalk.logistics
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    scope_name: AstroTalk logistics scope
    scope_type: logistics_courier_reconciliation
    platform_account_ids:
    - platform_account.astrotalk.shiprocket.logistics
    platform_ids:
    - platform.shiprocket
    platform_context_ids:
    - platform_context.shiprocket.in
    account_data_binding_ids:
    - account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
    - account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    group_scope_values:
      group_id: '60'
      group_level_id: '221'
    deferred_sources:
    - label: Shipway
      config: Invoice + Settlement report
      reason: No Shipway canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Kwikship
      config: Invoice + Settlement
      reason: No Kwikship canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Yolojet
      config: Invoice + Manual entry
      reason: No Yolojet canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Criticalog
      config: Invoice only
      reason: No Criticalog canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.astrotalk.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.astrotalk.marketplace
  card_type: business_scope_set
  canonical_name: AstroTalk marketplace scope
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - AstroTalk marketplace scope
    - marketplace accounts and bindings
    - AstroTalk marketplace resolver input
    business_meaning: Business scope set for AstroTalk's marketplace runtime resolution. It groups 4 platform accounts
      and 16 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which marketplace accounts and bindings are active for AstroTalk?
    - Which runtime table bindings should be considered together under AstroTalk marketplace scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 4 platform accounts
    - 16 account-data bindings
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - business_scope_set_id:business_scope_set.astrotalk.marketplace
    embedding_text: AstroTalk marketplace scope groups AstroTalk's marketplace runtime accounts and table bindings.
      Use it to restrict traversal to the client's configured sources; unresolved sources remain deferred until
      supported canonical packs exist.
    search_keywords:
    - AstroTalk
    - AstroTalk marketplace scope
    - marketplace
    - business scope set
    - 4 accounts
    - 16 bindings
    exact_match_keys:
    - business_scope_set.astrotalk.marketplace
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_scope_set_id: business_scope_set.astrotalk.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    scope_name: AstroTalk marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.astrotalk.amazon_india.marketplace
    - platform_account.astrotalk.flipkart.marketplace
    - platform_account.astrotalk.myntra.marketplace
    - platform_account.astrotalk.amazon.marketplace
    platform_ids:
    - platform.amazon
    - platform.flipkart
    - platform.myntra
    platform_context_ids:
    - platform_context.amazon.in
    - platform_context.amazon.international
    - platform_context.flipkart.in
    - platform_context.myntra.in
    account_data_binding_ids:
    - account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
    - account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
    - account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
```

#### business_scope_set.astrotalk.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.astrotalk.oms
  card_type: business_scope_set
  canonical_name: AstroTalk OMS runtime scope
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk OMS runtime scope
    - AstroTalk OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - AstroTalk OMS scope
    - OMS accounts and bindings
    - AstroTalk OMS resolver input
    business_meaning: Business scope set for AstroTalk's OMS runtime resolution. It groups 1 platform accounts and
      2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for AstroTalk?
    - Which runtime table bindings should be considered together under AstroTalk OMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:oms
    embedding_text: AstroTalk OMS runtime scope groups AstroTalk's OMS runtime accounts and table bindings. Use
      it to restrict traversal to the client's configured sources; unresolved sources remain deferred until supported
      canonical packs exist.
    search_keywords:
    - AstroTalk
    - AstroTalk OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.astrotalk.oms
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
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.astrotalk.oms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.oms
    account_data_binding_ids:
    - account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.astrotalk.shopify_d2c.oms
      account_name: AstroTalk Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Petpooja
      config: restaurant/F&B POS
      reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
      source_family: oms
    - label: Posist
      config: restaurant/F&B POS
      reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.astrotalk.wms

```yaml
canonical_card:
  canonical_id: business_scope_set.astrotalk.wms
  card_type: business_scope_set
  canonical_name: AstroTalk WMS runtime scope
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk WMS runtime scope
    - AstroTalk WMS scope
    - WMS runtime scope set
    colloquial_phrases:
    - AstroTalk WMS scope
    - WMS accounts and bindings
    - AstroTalk WMS resolver input
    business_meaning: Business scope set for AstroTalk's WMS runtime resolution. It groups 1 platform accounts and
      2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which WMS accounts and bindings are active for AstroTalk?
    - Which runtime table bindings should be considered together under AstroTalk WMS runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - WMS
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:wms
    embedding_text: AstroTalk WMS runtime scope groups AstroTalk's WMS runtime accounts and table bindings. Use
      it to restrict traversal to the client's configured sources; unresolved sources remain deferred until supported
      canonical packs exist.
    search_keywords:
    - AstroTalk
    - AstroTalk WMS runtime scope
    - WMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.astrotalk.wms
  evidence:
    source_documents:
    - AstroTalk.docx
    - increff_wms.md
    - unicommerce_wms.md
    source_path: client DOCX plus uploaded WMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: wms
    business_scope_set_id: business_scope_set.astrotalk.wms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk WMS runtime scope
    binding_type: wms_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.wms
    platform_account_ids:
    - platform_account.astrotalk.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    included_platform_ids:
    - platform.unicommerce
    included_platform_context_ids:
    - platform_context.unicommerce.in_wms
    source_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.astrotalk.payment_gateway

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
  canonical_id: business_scope_set.astrotalk.payment_gateway
  card_type: business_scope_set
  canonical_name: AstroTalk payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk payment gateway runtime scope
    - AstroTalk payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - AstroTalk payment gateway scope
    - payment gateway accounts and bindings
    - AstroTalk payment gateway resolver input
    business_meaning: Business scope set for AstroTalk's payment gateway runtime resolution. It groups 1 platform
      accounts and 1 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for AstroTalk?
    - Which runtime table bindings should be considered together under AstroTalk payment gateway runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - payment_gateway
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:payment_gateway
    embedding_text: AstroTalk payment gateway runtime scope groups AstroTalk's payment gateway runtime accounts
      and table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - AstroTalk
    - AstroTalk payment gateway runtime scope
    - payment gateway
    - business scope set
    - 1 accounts
    - 1 bindings
    exact_match_keys:
    - business_scope_set.astrotalk.payment_gateway
  evidence:
    source_documents:
    - AstroTalk.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.astrotalk.payment_gateway
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.payment_gateway
    platform_account_ids:
    - platform_account.astrotalk.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
    included_platform_ids:
    - platform.razorpay
    included_platform_context_ids:
    - platform_context.razorpay.in
    source_flow_paths:
    - platform_account_id: platform_account.astrotalk.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.astrotalk.logistics_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  card_type: business_flow_binding
  canonical_name: AstroTalk logistics runtime resolution
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - AstroTalk.docx
    - logistics_integrated.md
    source_path: AstroTalk.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_flow_binding_id: business_flow_binding.astrotalk.logistics_runtime_resolution
    runtime_source_family: logistics
    business_scope_set_id: business_scope_set.astrotalk.logistics
  semantic:
    aliases:
    - AstroTalk logistics runtime resolution
    - AstroTalk logistics / courier flow
    - logistics / courier runtime resolution flow
    colloquial_phrases:
    - AstroTalk logistics / courier resolution flow
    - logistics / courier source routing
    - AstroTalk runtime traversal plan
    business_meaning: Business flow binding for AstroTalk's logistics / courier source resolution. It connects the
      scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which logistics / courier bindings should be traversed for AstroTalk's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - logistics_courier
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - business_flow_binding_id:business_flow_binding.astrotalk.logistics_runtime_resolution
    - runtime_source_family:logistics
    embedding_text: AstroTalk logistics runtime resolution is AstroTalk's logistics / courier runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - AstroTalk
    - AstroTalk logistics runtime resolution
    - logistics / courier
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.astrotalk.logistics_runtime_resolution
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk logistics runtime resolution
    binding_type: logistics_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.logistics
    account_data_binding_ids:
    - account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
    - account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
    participating_accounts:
    - platform_account_id: platform_account.astrotalk.shiprocket.logistics
      account_name: AstroTalk Shiprocket Logistics Aggregator account
    money_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
      source_role: logistics_cod_settlement_report_schema_only
      table_id: table.zs_observe.shiprocket_settlement_report
    - account_data_binding_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
      source_role: logistics_freight_invoice
      table_id: table.zs_observe.shiprocket_invoice
    deferred_sources:
    - label: Shipway
      config: Invoice + Settlement report
      reason: No Shipway canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Kwikship
      config: Invoice + Settlement
      reason: No Kwikship canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Yolojet
      config: Invoice + Manual entry
      reason: No Yolojet canonical logistics platform/table cards in uploaded logistics_integrated.md
    - label: Criticalog
      config: Invoice only
      reason: No Criticalog canonical logistics platform/table cards in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.astrotalk.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: AstroTalk marketplace runtime resolution
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk marketplace runtime resolution
    - AstroTalk marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - AstroTalk marketplace resolution flow
    - marketplace source routing
    - AstroTalk runtime traversal plan
    business_meaning: Business flow binding for AstroTalk's marketplace source resolution. It connects the scope
      set to 4 platform accounts and 16 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for AstroTalk's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 4 platform accounts
    - 16 account-data bindings
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - business_flow_binding_id:business_flow_binding.astrotalk.marketplace_runtime_resolution
    embedding_text: AstroTalk marketplace runtime resolution is AstroTalk's marketplace runtime traversal binding.
      It connects the business scope set to account and table bindings so retrieval selects client evidence first
      and then delegates semantics to external canonical packs.
    search_keywords:
    - AstroTalk
    - AstroTalk marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.astrotalk.marketplace_runtime_resolution
  evidence:
    source_documents:
    - AstroTalk.docx
    source_path: AstroTalk.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_flow_binding_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.astrotalk.marketplace
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.marketplace
    account_data_binding_ids:
    - account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
    - account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
    - account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
    participating_accounts:
    - platform_account_id: platform_account.astrotalk.amazon_india.marketplace
      account_name: Amazon India
    - platform_account_id: platform_account.astrotalk.flipkart.marketplace
      account_name: Flipkart
    - platform_account_id: platform_account.astrotalk.myntra.marketplace
      account_name: Myntra
    - platform_account_id: platform_account.astrotalk.amazon.marketplace
      account_name: Amazon
    money_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
      source_role: disbursement
      table_id: table.zs_observe.amazon_disbursment
    - account_data_binding_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
      source_role: oms_sales
      table_id: table.zs_recon_processor.flipkart_oms
    - account_data_binding_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
      source_role: settlement
      table_id: table.zs_observe.flipkart_settlement
    - account_data_binding_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
      source_role: commission_fee_invoice
      table_id: table.zs_observe.flipkart_commission
    - account_data_binding_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
      source_role: cashback_credit_debit_note
      table_id: table.zs_observe.flipkart_cashback
    - account_data_binding_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
      source_role: oms_sales
      table_id: table.zs_observe.myntra_oms
    - account_data_binding_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
      source_role: settlement
      table_id: table.zs_observe.myntra_settlement
    - account_data_binding_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
      source_role: non_order_settlement
      table_id: table.zs_observe.myntra_non_order_settlement
    - account_data_binding_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
      source_role: returns
      table_id: table.zs_observe.myntra_reverse
    - account_data_binding_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
      source_role: disbursement
      table_id: table.zs_observe.amazon_disbursment
    - account_data_binding_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
    - account_data_binding_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
      source_role: returns
      table_id: table.zs_observe.amazon_returns
    deferred_sources:
    - label: Snapmint
      config: snapmint_settlement
      reason: Snapmint is payment/BNPL settlement; PG pack expected later
```

#### business_flow_binding.astrotalk.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.astrotalk.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: AstroTalk OMS runtime resolution flow
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
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk OMS runtime resolution flow
    - AstroTalk OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - AstroTalk OMS resolution flow
    - OMS source routing
    - AstroTalk runtime traversal plan
    business_meaning: Business flow binding for AstroTalk's OMS source resolution. It connects the scope set to
      1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence before
      reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for AstroTalk's runtime question?
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:oms
    embedding_text: AstroTalk OMS runtime resolution flow is AstroTalk's OMS runtime traversal binding. It connects
      the business scope set to account and table bindings so retrieval selects client evidence first and then delegates
      semantics to external canonical packs.
    search_keywords:
    - AstroTalk
    - AstroTalk OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.astrotalk.oms_runtime_resolution
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
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.astrotalk.oms_runtime_resolution
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    binding_name: AstroTalk OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.astrotalk.oms
    account_data_binding_ids:
    - account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.astrotalk.shopify_d2c.oms
      account_name: AstroTalk Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Petpooja
      config: restaurant/F&B POS
      reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
      source_family: oms
    - label: Posist
      config: restaurant/F&B POS
      reason: No Petpooja/Posist restaurant POS canonical cards in the uploaded OMS packs.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.astrotalk.wms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.astrotalk.wms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: AstroTalk WMS runtime resolution
  status: active
  review_status: accepted
  confidence: high
  version: client_marketplace_logistics_oms_wms_runtime_v1
  created_at: '2026-06-04'
  updated_at: '2026-06-04'
  created_by: openai_runtime_curation
  updated_by: openai_runtime_semantic_rewrite
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk WMS runtime resolution
    - AstroTalk WMS flow
    - WMS runtime resolution flow
    colloquial_phrases:
    - AstroTalk WMS resolution flow
    - WMS source routing
    - AstroTalk runtime traversal plan
    business_meaning: Business flow binding for AstroTalk's WMS source resolution. It connects the scope set to
      1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence before
      reusable semantics run.
    business_questions:
    - Which WMS bindings should be traversed for AstroTalk's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - WMS
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:wms
    embedding_text: AstroTalk WMS runtime resolution is AstroTalk's WMS runtime traversal binding. It connects the
      business scope set to account and table bindings so retrieval selects client evidence first and then delegates
      semantics to external canonical packs.
    search_keywords:
    - AstroTalk
    - AstroTalk WMS runtime resolution
    - WMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.astrotalk.wms_runtime_resolution
  evidence:
    source_documents:
    - AstroTalk.docx
    - increff_wms.md
    - unicommerce_wms.md
    source_path: client DOCX plus uploaded WMS canonical packs
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_flow
    evidence_ids:
    - client_runtime.wms_flow
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: wms
    business_flow_binding_id: business_flow_binding.astrotalk.wms_runtime_resolution
    business_scope_set_id: business_scope_set.astrotalk.wms
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_flow_binding_id: business_flow_binding.astrotalk.wms_runtime_resolution
    business_scope_set_id: business_scope_set.astrotalk.wms
    flow_name: AstroTalk WMS runtime resolution
    flow_type: wms_source_resolution
    platform_account_ids:
    - platform_account.astrotalk.unicommerce_wms.wms
    account_data_binding_ids:
    - account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    source_flow_paths:
    - account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.astrotalk.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.astrotalk.payment_gateway_runtime_resolution

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
  canonical_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: AstroTalk payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: AstroTalk
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - AstroTalk payment gateway runtime resolution
    - AstroTalk payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - AstroTalk payment gateway resolution flow
    - payment gateway source routing
    - AstroTalk runtime traversal plan
    business_meaning: Business flow binding for AstroTalk's payment gateway source resolution. It connects the scope
      set to 1 platform accounts and 1 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for AstroTalk's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - payment_gateway
    - runtime_traversal
    included_concepts:
    - 1 platform accounts
    - 1 account-data bindings
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
    - tenant_id:tenant.astrotalk
    - group_id:group.astrotalk.g60.gl221
    - runtime_source_family:payment_gateway
    embedding_text: AstroTalk payment gateway runtime resolution is AstroTalk's payment gateway runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - AstroTalk
    - AstroTalk payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - AstroTalk.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.astrotalk.payment_gateway
  fields:
    tenant_id: tenant.astrotalk
    group_id: group.astrotalk.g60.gl221
    business_flow_binding_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.astrotalk.payment_gateway
    flow_name: AstroTalk payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.astrotalk.razorpay.payment_gateway
    account_data_binding_ids:
    - account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
    source_flow_paths:
    - platform_account_id: platform_account.astrotalk.razorpay.payment_gateway
      account_data_binding_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
      platform_id: platform.razorpay
      platform_context_id: platform_context.razorpay.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.razorpay_payin
      source_role: settlement
      configured_pipeline_target: razorpay_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_invoice_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_invoice_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: column.zs_observe.shiprocket_invoice.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: column.zs_observe.unicommerce.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '221'
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '221'
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shiprocket_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  target_card_id: platform_account.astrotalk.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shiprocket_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: platform_account.astrotalk.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.astrotalk.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.astrotalk.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: platform_account.astrotalk.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: platform_account.astrotalk.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  target_card_id: table.zs_observe.amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  target_card_id: table.zs_observe.amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: table.zs_observe.amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: table.zs_observe.flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: table.zs_observe.flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: table.zs_recon_processor.flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: table.zs_observe.flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: table.zs_observe.myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: table.zs_observe.myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  target_card_id: table.zs_observe.myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: table.zs_observe.myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report.account_data_binding_binds_to_table.table_zs_observe_shiprocket_settlement_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report.account_data_binding_binds_to_table.table_zs_observe_shiprocket_settlement_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  target_card_id: table.zs_observe.shiprocket_settlement_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_binds_to_table.table_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice.account_data_binding_binds_to_table.table_zs_observe_shiprocket_invoice
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  target_card_id: table.zs_observe.shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: table.zs_observe.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: table.zs_observe.unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  target_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  target_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_shiprocket_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  target_card_id: platform_account.astrotalk.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  target_card_id: platform_account.astrotalk.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_unicommerce_wms_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  target_card_id: platform_account.astrotalk.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  target_card_id: business_scope_set.astrotalk.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  target_card_id: business_scope_set.astrotalk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  target_card_id: business_scope_set.astrotalk.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  target_card_id: business_scope_set.astrotalk.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform.platform_shiprocket
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_flipkart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform.platform_myntra
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform.platform_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform_account.platform_account_astrotalk_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform_account.platform_account_astrotalk_shiprocket_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: platform_account.astrotalk.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform_account.platform_account_astrotalk_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform_account.platform_account_astrotalk_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: platform_account.astrotalk.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform_account.platform_account_astrotalk_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform_account.platform_account_astrotalk_unicommerce_wms_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: platform_account.astrotalk.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_astrotalk_g60_gl221.group_belongs_to_tenant.tenant_astrotalk

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_belongs_to_tenant.tenant_astrotalk
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: tenant.astrotalk
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_logistics_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_logistics_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_flow_binding.astrotalk.logistics_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_flow_binding.astrotalk.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_flow_binding.astrotalk.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_wms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_wms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_flow_binding.astrotalk.wms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_logistics

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_logistics
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_scope_set.astrotalk.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_scope_set.astrotalk.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_oms

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_scope_set.astrotalk.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_wms

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_wms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_scope_set.astrotalk.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_amazon_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_amazon_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.amazon.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_amazon_india_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_flipkart_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_myntra_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_shiprocket_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_unicommerce_wms_wms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_shiprocket_logistics.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shiprocket_logistics.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.shiprocket.logistics
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.shopify_d2c.oms
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.unicommerce_wms.wms
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_disbursement_zs_observe_amazon_disbursment
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_returns_zs_observe_amazon_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: account_data_binding.astrotalk.amazon.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: account_data_binding.astrotalk.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: account_data_binding.astrotalk.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_returns_zs_observe_myntra_reverse
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_astrotalk_myntra_settlement_zs_observe_myntra_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: account_data_binding.astrotalk.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_cod_settlement_report_schema_only_zs_observe_shiprocket_settlement_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.shiprocket.logistics
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_cod_settlement_report_schema_only.zs_observe_shiprocket_settlement_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_astrotalk_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_astrotalk_shiprocket_logistics_freight_invoice_zs_observe_shiprocket_invoice
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.shiprocket.logistics
  target_card_id: account_data_binding.astrotalk.shiprocket.logistics_freight_invoice.zs_observe_shiprocket_invoice
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_astrotalk_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.shopify_d2c.oms
  target_card_id: account_data_binding.astrotalk.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_astrotalk_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.shopify_d2c.oms
  target_card_id: account_data_binding.astrotalk.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.unicommerce_wms.wms
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_astrotalk_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.unicommerce_wms.wms
  target_card_id: account_data_binding.astrotalk.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_uses_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_uses_platform.platform_flipkart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_uses_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_uses_platform.platform_myntra
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.shiprocket.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.unicommerce_wms.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_astrotalk_amazon_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.amazon.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.amazon_india.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.flipkart.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.myntra.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_astrotalk_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.shiprocket.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.unicommerce_wms.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### TENANT_HAS_GROUP

#### edge.tenant_astrotalk.tenant_has_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.tenant_astrotalk.tenant_has_group.group_astrotalk_g60_gl221
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.astrotalk
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_belongs_to_platform_account.platform_account_astrotalk_razorpay_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: platform_account.astrotalk.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin.account_data_binding_binds_to_table.table_zs_observe_razorpay_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  target_card_id: table.zs_observe.razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_astrotalk_razorpay_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  target_card_id: platform_account.astrotalk.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_astrotalk_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_astrotalk_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.astrotalk.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.astrotalk.payment_gateway
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.astrotalk.payment_gateway
  target_card_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform.platform_razorpay
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.astrotalk.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform_account.platform_account_astrotalk_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform_account.platform_account_astrotalk_razorpay_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.astrotalk.payment_gateway
  target_card_id: platform_account.astrotalk.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_astrotalk_payment_gateway.business_scope_set_includes_platform_context.platform_context_razorpay_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.astrotalk.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_flow_binding.business_flow_binding_astrotalk_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_flow_binding.astrotalk.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_business_scope_set.business_scope_set_astrotalk_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: business_scope_set.astrotalk.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_razorpay_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_astrotalk_g60_gl221.group_has_platform_account.platform_account_astrotalk_razorpay_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.astrotalk.g60.gl221
  target_card_id: platform_account.astrotalk.razorpay.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_belongs_to_group.group_astrotalk_g60_gl221

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_belongs_to_group.group_astrotalk_g60_gl221
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.astrotalk.razorpay.payment_gateway
  target_card_id: group.astrotalk.g60.gl221
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_has_account_data_binding.account_data_binding_astrotalk_razorpay_settlement_zs_observe_razorpay_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.astrotalk.razorpay.payment_gateway
  target_card_id: account_data_binding.astrotalk.razorpay.settlement.zs_observe_razorpay_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_uses_platform.platform_razorpay
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.astrotalk.razorpay.payment_gateway
  target_card_id: platform.razorpay
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_astrotalk_razorpay_payment_gateway.platform_account_uses_platform_context.platform_context_razorpay_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.astrotalk.razorpay.payment_gateway
  target_card_id: platform_context.razorpay.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
