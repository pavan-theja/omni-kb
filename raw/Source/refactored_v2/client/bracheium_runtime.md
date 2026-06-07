# Bracheium Brand Technologies Pvt Ltd — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `bracheium_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Cred
  config: Sales, Settlement, Returns, Transactions
  reason: Cred marketplace pack not uploaded
- label: FirstCry
  config: OMS — WB, Settlement — WB, Returns — WB, RTO — WB
  reason: FirstCry marketplace pack not uploaded
- label: Klip · Blitz
  config: Settlement only
  reason: Klip/Blitz settlement pack not uploaded
- label: XpressBees invoice
  config: invoice
  reason: No native XpressBees invoice table card in uploaded logistics_integrated.md
  source_family: logistics
- label: Shiprocket order source
  config: order source table
  reason: Shiprocket OMS table is already bound in the logistics runtime slice for this client; no duplicate OMS
    binding emitted.
  source_family: oms
- label: Easebuzz
  config: payment gateway files configured
  reason: No Easebuzz canonical platform/table cards in uploaded payment_gateway.md
  source_family: payment_gateway
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 14
  account_data_binding: 41
  business_scope_set: 5
  business_flow_binding: 5
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 72
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 41
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 41
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 5
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 41
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 14
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 5
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 5
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 41
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 14
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 14
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 14
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 5
  GROUP_HAS_BUSINESS_SCOPE_SET: 5
  GROUP_HAS_PLATFORM_ACCOUNT: 14
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 14
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 41
  PLATFORM_ACCOUNT_USES_PLATFORM: 14
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 14
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
  added_runtime_cards: 8
  added_runtime_edges: 45
  supported_wms_accounts: 2
  supported_wms_bindings: 4
  resolved_deferred_mentions: 2
bank_payment_integration:
  source_packs:
  - payment_gateway.md
  - bank_statement.md
  added_runtime_cards: 6
  added_runtime_edges: 31
  supported_payment_bindings: 2
  supported_bank_bindings: 0
  deferred_financial_sources_added_or_updated: 1
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.bracheium_brand_technologies_pvt_ltd

```yaml
canonical_card:
  canonical_id: tenant.bracheium_brand_technologies_pvt_ltd
  card_type: tenant
  canonical_name: Bracheium Brand Technologies Pvt Ltd
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd
    - bracheium_brand_technologies_pvt_ltd
    - Bracheium Brand Technologies Pvt Ltd runtime tenant
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd client runtime
    - Bracheium Brand Technologies Pvt Ltd source configuration
    - Bracheium Brand Technologies Pvt Ltd scoped reconciliation setup
    business_meaning: Runtime tenant identity for Bracheium Brand Technologies Pvt Ltd. It anchors the client's
      marketplace, logistics, OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope
      separate from reusable domain semantics.
    business_questions:
    - Which source families and configured accounts belong to Bracheium Brand Technologies Pvt Ltd?
    - Which group and account bindings should constrain Bracheium Brand Technologies Pvt Ltd's SQL handoff?
    - After Bracheium Brand Technologies Pvt Ltd's runtime scope is resolved, which domain layer should receive
      the query next?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    embedding_text: Bracheium Brand Technologies Pvt Ltd is the runtime tenant root for the client's marketplace,
      logistics, OMS, WMS, payment-gateway, and bank-statement configuration. Use it to reach group, platform-account,
      and account-data-binding nodes before invoking reusable canonical packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - bracheium_brand_technologies_pvt_ltd
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.bracheium_brand_technologies_pvt_ltd
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
  fields:
    tenant_slug: bracheium_brand_technologies_pvt_ltd
    tenant_name: Bracheium Brand Technologies Pvt Ltd
    legal_name: Bracheium Brand Technologies Pvt Ltd
    active: true
```

### 2.2 Group Cards

#### group.bracheium_brand_technologies_pvt_ltd.g9.gl29

```yaml
canonical_card:
  canonical_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  card_type: group
  canonical_name: Bracheium Brand Technologies Pvt Ltd group 9/29
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mensa Brands
    - Bracheium Brand Technologies Pvt Ltd group 9/29
    - group_id 9
    - group_level_id 29
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd group scope
    - Mensa Brands runtime scope
    - group 9 level 29 query boundary
    business_meaning: 'Runtime group scope for Bracheium Brand Technologies Pvt Ltd: group_id=9 and group_level_id=29.
      It is the client-specific filter boundary that must be applied before resolving account bindings for IN in
      INR.'
    business_questions:
    - Which bindings use group_id=9 and group_level_id=29?
    - Which source families are active under Mensa Brands?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - group_id_value:9
    - group_level_id_value:29
    embedding_text: Mensa Brands is the runtime group node for Bracheium Brand Technologies Pvt Ltd. Apply group_id=9
      and group_level_id=29 when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Mensa Brands
    - group_id 9
    - group_level_id 29
    - runtime group scope
    exact_match_keys:
    - group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    group_level_id: '29'
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id_value: '9'
    group_level_id_value: '29'
    group_name: Mensa Brands
    default_currency: INR
    country: IN
```

### 2.3 Platform Account Cards

#### platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Amazon India
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
    - Bracheium Brand Technologies Pvt Ltd Amazon India
    - Amazon
    - Amazon India marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Amazon India source account
    - Amazon India marketplace runtime account
    - Amazon India configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Amazon India marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon India table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Amazon India questions traverse
      through?
    - Which source roles under Amazon India are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions'
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Amazon India platform account routes marketplace questions
      to platform.amazon / platform_context.amazon.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Amazon India
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_name: Amazon India
    account_type: marketplace_seller_account
    source_account_identifier: Amazon India
    active: true
    configured_source_description: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Flipkart
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
    - Bracheium Brand Technologies Pvt Ltd Flipkart
    - Flipkart marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Flipkart source account
    - Flipkart marketplace runtime account
    - Flipkart configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Flipkart marketplace sources.
      It points traversal to platform.flipkart and platform_context.flipkart.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Flipkart table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Flipkart questions traverse
      through?
    - Which source roles under Flipkart are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions'
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Flipkart platform account routes marketplace questions
      to platform.flipkart / platform_context.flipkart.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Flipkart
    - marketplace
    - platform.flipkart
    - platform_context.flipkart.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_name: Flipkart
    account_type: marketplace_seller_account
    source_account_identifier: Flipkart
    active: true
    configured_source_description: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads),
      Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Increff WMS
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Increff WMS
    - Bracheium Brand Technologies Pvt Ltd Increff WMS
    - Increff
    - Increff WMS WMS account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Increff WMS source account
    - Increff WMS WMS runtime account
    - Increff WMS configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Increff WMS WMS sources.
      It points traversal to platform.increff and platform_context.increff.in_wms and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Increff WMS table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Increff WMS questions traverse
      through?
    - Which source roles under Increff WMS are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - WMS
    - source_router
    included_concepts:
    - 'client configuration: fulfilment/WMS'
    - platform.increff
    - platform_context.increff.in_wms
    - Increff WMS
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.increff
    - platform_context_id:platform_context.increff.in_wms
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    - runtime_source_family:wms
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Increff WMS platform account routes WMS questions to
      platform.increff / platform_context.increff.in_wms. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Increff WMS
    - Increff
    - WMS
    - platform.increff
    - platform_context.increff.in_wms
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - increff_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded increff_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    account_name: Increff WMS
    account_type: wms_operator_account
    source_account_identifier: Increff WMS
    source_account_identifier_status: client_docx_names_wms_system_without_separate_account_number
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: fulfilment/WMS
    canonical_source_pack: increff_wms.md
    group_scope_values:
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — JioMart
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
    vendor_or_system: JioMart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - JioMart
    - Bracheium Brand Technologies Pvt Ltd JioMart
    - JioMart marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd JioMart source account
    - JioMart marketplace runtime account
    - JioMart configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's JioMart marketplace sources.
      It points traversal to platform.jiomart and platform_context.jiomart.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which JioMart table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's JioMart questions traverse
      through?
    - Which source roles under JioMart are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Returns, Transactions'
    - platform.jiomart
    - platform_context.jiomart.in
    - JioMart
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.jiomart
    - platform_context_id:platform_context.jiomart.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's JioMart platform account routes marketplace questions
      to platform.jiomart / platform_context.jiomart.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - JioMart
    - marketplace
    - platform.jiomart
    - platform_context.jiomart.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.jiomart
    platform_context_id: platform_context.jiomart.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.jiomart
    platform_context_id: platform_context.jiomart.in
    account_name: JioMart
    account_type: marketplace_seller_account
    source_account_identifier: JioMart
    active: true
    configured_source_description: OMS, Settlement, Returns, Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho
    - Bracheium Brand Technologies Pvt Ltd Meesho
    - Meesho marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho source account
    - Meesho marketplace runtime account
    - Meesho configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Meesho marketplace sources.
      It points traversal to platform.meesho and platform_context.meesho.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Meesho table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Meesho questions traverse through?
    - Which source roles under Meesho are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions'
    - platform.meesho
    - platform_context.meesho.in
    - Meesho
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Meesho platform account routes marketplace questions
      to platform.meesho / platform_context.meesho.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - marketplace
    - platform.meesho
    - platform_context.meesho.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_name: Meesho
    account_type: marketplace_seller_account
    source_account_identifier: Meesho
    active: true
    configured_source_description: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Myntra
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
    - Bracheium Brand Technologies Pvt Ltd Myntra
    - Myntra marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Myntra source account
    - Myntra marketplace runtime account
    - Myntra configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Myntra marketplace sources.
      It points traversal to platform.myntra and platform_context.myntra.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Myntra table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Myntra questions traverse through?
    - Which source roles under Myntra are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses,
      Transactions'
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Myntra platform account routes marketplace questions
      to platform.myntra / platform_context.myntra.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Myntra
    - marketplace
    - platform.myntra
    - platform_context.myntra.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_name: Myntra
    account_type: marketplace_seller_account
    source_account_identifier: Myntra
    active: true
    configured_source_description: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP),
      Non-order settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS
      expenses, Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator
      account
    - Shiprocket
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account logistics / courier account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator
      account source account
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account logistics / courier runtime account
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd Shiprocket Logistics Aggregator account logistics / courier sources. It points traversal to platform.shiprocket
      and platform_context.shiprocket.in and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account table bindings are available
      for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd Shiprocket Logistics Aggregator account questions traverse through?
    - Which source roles under Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account are
      active or review-required for this client?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - runtime_source_family:logistics
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics
      Aggregator account platform account routes logistics / courier questions to platform.shiprocket / platform_context.shiprocket.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account
    - Shiprocket
    - logistics / courier
    - platform.shiprocket
    - platform_context.shiprocket.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_name: Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    - Shopify
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account OMS account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account source account
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account OMS runtime account
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd Shopify D2C OMS account OMS sources. It points traversal to platform.shopify and platform_context.shopify.in.d2c_oms
      and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account table bindings are available for Bracheium
      Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd Shopify D2C OMS account questions traverse through?
    - Which source roles under Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account are active or review-required
      for this client?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS
      account platform account routes OMS questions to platform.shopify / platform_context.shopify.in.d2c_oms. Use
      it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - shopify_d2c_oms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    group_scope_values:
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal
    - Bracheium Brand Technologies Pvt Ltd Snapdeal
    - Snapdeal marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal source account
    - Snapdeal marketplace runtime account
    - Snapdeal configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Snapdeal marketplace sources.
      It points traversal to platform.snapdeal and platform_context.snapdeal.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Snapdeal table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Snapdeal questions traverse
      through?
    - Which source roles under Snapdeal are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Commission file (5-sheet), Transactions'
    - platform.snapdeal
    - platform_context.snapdeal.in
    - Snapdeal
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Snapdeal platform account routes marketplace questions
      to platform.snapdeal / platform_context.snapdeal.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - marketplace
    - platform.snapdeal
    - platform_context.snapdeal.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_name: Snapdeal
    account_type: marketplace_seller_account
    source_account_identifier: Snapdeal
    active: true
    configured_source_description: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Tata Cliq
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Tata Cliq
    - Bracheium Brand Technologies Pvt Ltd Tata Cliq
    - TataCliq
    - Tata Cliq marketplace account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Tata Cliq source account
    - Tata Cliq marketplace runtime account
    - Tata Cliq configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Tata Cliq marketplace
      sources. It points traversal to platform.tatacliq and platform_context.tatacliq.in and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Tata Cliq table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Tata Cliq questions traverse
      through?
    - Which source roles under Tata Cliq are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Transactions'
    - platform.tatacliq
    - platform_context.tatacliq.in
    - Tata Cliq
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Tata Cliq platform account routes marketplace questions
      to platform.tatacliq / platform_context.tatacliq.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Tata Cliq
    - TataCliq
    - marketplace
    - platform.tatacliq
    - platform_context.tatacliq.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_name: Tata Cliq
    account_type: marketplace_seller_account
    source_account_identifier: Tata Cliq
    active: true
    configured_source_description: OMS, Settlement, Transactions
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Unicommerce WMS
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Unicommerce WMS
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS
    - Unicommerce
    - Unicommerce WMS WMS account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS source account
    - Unicommerce WMS WMS runtime account
    - Unicommerce WMS configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Unicommerce WMS WMS sources.
      It points traversal to platform.unicommerce and platform_context.unicommerce.in_wms and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Unicommerce WMS table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Unicommerce WMS questions traverse
      through?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    - runtime_source_family:wms
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Unicommerce WMS platform account routes WMS questions
      to platform.unicommerce / platform_context.unicommerce.in_wms. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Unicommerce WMS
    - Unicommerce
    - WMS
    - platform.unicommerce
    - platform_context.unicommerce.in_wms
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - unicommerce_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
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
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
    - XpressBees
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account logistics / courier account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account source
      account
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account logistics / courier runtime account
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd XpressBees Logistics account logistics / courier sources. It points traversal to platform.xpressbees
      and platform_context.xpressbees.in and groups the client's table-level account-data bindings for this source.
    business_questions:
    - Which Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account table bindings are available for Bracheium
      Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies
      Pvt Ltd XpressBees Logistics account questions traverse through?
    - Which source roles under Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account are active or review-required
      for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - logistics_courier
    - source_router
    included_concepts:
    - platform.xpressbees
    - platform_context.xpressbees.in
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    - platform_id:platform.xpressbees
    - platform_context_id:platform_context.xpressbees.in
    - runtime_source_family:logistics
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Bracheium Brand Technologies Pvt Ltd XpressBees Logistics
      account platform account routes logistics / courier questions to platform.xpressbees / platform_context.xpressbees.in.
      Use it to collect the client's table bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
    - XpressBees
    - logistics / courier
    - platform.xpressbees
    - platform_context.xpressbees.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    runtime_source_family: logistics
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    account_name: Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
    account_type: logistics_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    group_scope_values:
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Cashfree payment gateway
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Cashfree
    - Bracheium Brand Technologies Pvt Ltd Cashfree
    - Cashfree payment gateway account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Cashfree source account
    - Cashfree payment gateway runtime account
    - Cashfree configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's Cashfree payment gateway
      sources. It points traversal to platform.cashfree and platform_context.cashfree.in and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Cashfree table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's Cashfree questions traverse
      through?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Bracheium Brand Technologies Pvt Ltd's Cashfree platform account routes payment gateway questions
      to platform.cashfree / platform_context.cashfree.in. Use it to collect the client's table bindings; do not
      use this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Cashfree
    - payment gateway
    - platform.cashfree
    - platform_context.cashfree.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
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
      group_id: '9'
      group_level_id: '29'
```

#### platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway

```yaml
canonical_card:
  canonical_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  card_type: platform_account
  canonical_name: Bracheium Brand Technologies Pvt Ltd — PhonePe payment gateway
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - PhonePe
    - Bracheium Brand Technologies Pvt Ltd PhonePe
    - PhonePe payment gateway account
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd PhonePe source account
    - PhonePe payment gateway runtime account
    - PhonePe configured source family
    business_meaning: Runtime platform account for Bracheium Brand Technologies Pvt Ltd's PhonePe payment gateway
      sources. It points traversal to platform.phonepe and platform_context.phonepe.in and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which PhonePe table bindings are available for Bracheium Brand Technologies Pvt Ltd?
    - Which canonical platform/context should Bracheium Brand Technologies Pvt Ltd's PhonePe questions traverse
      through?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_id:platform.phonepe
    - platform_context_id:platform_context.phonepe.in
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    - runtime_source_family:payment_gateway
    embedding_text: Bracheium Brand Technologies Pvt Ltd's PhonePe platform account routes payment gateway questions
      to platform.phonepe / platform_context.phonepe.in. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - PhonePe
    - payment gateway
    - platform.phonepe
    - platform_context.phonepe.in
    exact_match_keys:
    - platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
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
      group_id: '9'
      group_level_id: '29'
```


### 2.4 Account Data Binding Cards

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Amazon India — disbursement
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
    - OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
    - Bracheium Brand Technologies Pvt Ltd Amazon disbursement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Amazon disbursement source
    - Amazon disbursement runtime binding
    - amazon_disbursment for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Amazon
      disbursement evidence should use zs_observe.amazon_disbursment. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon disbursement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep amazon_disbursment limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:disbursement
    - table_id:table.zs_observe.amazon_disbursment
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Amazon disbursement binding selects zs_observe.amazon_disbursment
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Amazon
    - disbursement
    - marketplace
    - zs_observe.amazon_disbursment
    - amazon_disbursment
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    table_id: table.zs_observe.amazon_disbursment
    source_role: disbursement
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_disbursment.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Amazon India — fee_preview
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
    - OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
    - Bracheium Brand Technologies Pvt Ltd Amazon fee preview
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Amazon
      fee preview evidence should use zs_observe.amazon_fee_preview. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep amazon_fee_preview limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Amazon fee preview binding selects zs_observe.amazon_fee_preview
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Amazon India — oms_sales
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
    - OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
    - Bracheium Brand Technologies Pvt Ltd Amazon OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Amazon
      OMS sales evidence should use zs_observe.amazon_oms. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep amazon_oms limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Amazon OMS sales binding selects zs_observe.amazon_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
    source_entity: Amazon
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.amazon_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Amazon India — settlement
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
    - OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
    - Bracheium Brand Technologies Pvt Ltd Amazon settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Amazon
      settlement evidence should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep amazon_settlement limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.in
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Amazon settlement binding selects zs_observe.amazon_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (B2C + B2B), Settlement, Disbursement, Fee preview, MTR report, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Flipkart — cashback_credit_debit_note
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
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
    - Bracheium Brand Technologies Pvt Ltd Flipkart cashback / credit-debit note
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Flipkart cashback / credit-debit note source
    - Flipkart cashback / credit-debit note runtime binding
    - flipkart_cashback for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Flipkart
      cashback / credit-debit note evidence should use zs_observe.flipkart_cashback. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart cashback / credit-debit note file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep flipkart_cashback limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:cashback_credit_debit_note
    - table_id:table.zs_observe.flipkart_cashback
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Flipkart cashback / credit-debit note binding
      selects zs_observe.flipkart_cashback as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable
      semantics come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Flipkart
    - cashback / credit-debit note
    - marketplace
    - zs_observe.flipkart_cashback
    - flipkart_cashback
    - cashback_credit_debit_note
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    table_id: table.zs_observe.flipkart_cashback
    source_role: cashback_credit_debit_note
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_cashback.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Flipkart — commission_fee_invoice
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
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
    - Bracheium Brand Technologies Pvt Ltd Flipkart commission invoice
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Flipkart commission invoice source
    - Flipkart commission invoice runtime binding
    - flipkart_commission for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Flipkart
      commission invoice evidence should use zs_observe.flipkart_commission. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart commission invoice file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep flipkart_commission limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:commission_fee_invoice
    - table_id:table.zs_observe.flipkart_commission
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Flipkart commission invoice binding selects zs_observe.flipkart_commission
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Flipkart
    - commission invoice
    - marketplace
    - zs_observe.flipkart_commission
    - flipkart_commission
    - commission_fee_invoice
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    table_id: table.zs_observe.flipkart_commission
    source_role: commission_fee_invoice
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_commission.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_commission.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Flipkart — oms_sales
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
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
    - Bracheium Brand Technologies Pvt Ltd Flipkart OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Flipkart OMS sales source
    - Flipkart OMS sales runtime binding
    - flipkart_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Flipkart
      OMS sales evidence should use zs_recon_processor.flipkart_oms. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep flipkart_oms limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:oms_sales
    - table_id:table.zs_recon_processor.flipkart_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Flipkart OMS sales binding selects zs_recon_processor.flipkart_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Flipkart
    - OMS sales
    - marketplace
    - zs_recon_processor.flipkart_oms
    - flipkart_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    table_id: table.zs_recon_processor.flipkart_oms
    source_role: oms_sales
    source_entity: Flipkart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_recon_processor.flipkart_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Flipkart — settlement
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
    - OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
    - Bracheium Brand Technologies Pvt Ltd Flipkart settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Flipkart settlement source
    - Flipkart settlement runtime binding
    - flipkart_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Flipkart
      settlement evidence should use zs_observe.flipkart_settlement. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Flipkart settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep flipkart_settlement limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    - platform_id:platform.flipkart
    - platform_context_id:platform_context.flipkart.in
    - source_role:settlement
    - table_id:table.zs_observe.flipkart_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Flipkart settlement binding selects zs_observe.flipkart_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Flipkart
    - settlement
    - marketplace
    - zs_observe.flipkart_settlement
    - flipkart_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    platform_id: platform.flipkart
    platform_context_id: platform_context.flipkart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    table_id: table.zs_observe.flipkart_settlement
    source_role: settlement
    source_entity: Flipkart
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.flipkart_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS + Cashback, Settlement, Commission, Adhoc (Ads/TDS/Rebates/VAS/Google Ads), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Increff WMS WMS returns, RTO and QC binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Increff WMS WMS returns
    - increff_returns
    - zs_observe.increff_returns
    - fulfilment/WMS
    - Bracheium Brand Technologies Pvt Ltd Increff WMS WMS returns
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Increff WMS WMS returns source
    - Increff WMS WMS returns runtime binding
    - increff_returns for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Increff
      WMS WMS returns evidence should use zs_observe.increff_returns. Apply group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in increff_wms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Increff WMS WMS rows should answer Bracheium Brand Technologies Pvt Ltd's WMS returns question?
    - Which group scope and active-row filters apply before querying increff_returns?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_returns
    included_concepts:
    - zs_observe.increff_returns
    - WMS returns
    - Increff WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=29
    - increff_wms.md
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    - platform_id:platform.increff
    - platform_context_id:platform_context.increff.in_wms
    - domain_id:domain.wms.increff.returns_rto_qc
    - table_id:table.zs_observe.increff_returns
    - source_role:wms_returns
    - runtime_source_family:wms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Increff WMS WMS returns binding selects zs_observe.increff_returns
      as WMS evidence. Scope: group_level_id=29. Reusable semantics come from increff_wms.md. Coverage status: active.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Increff WMS
    - WMS returns
    - WMS
    - zs_observe.increff_returns
    - increff_returns
    - wms_returns
    - increff_wms.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - increff_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded increff_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    domain_id: domain.wms.increff.returns_rto_qc
    table_id: table.zs_observe.increff_returns
    source_role: wms_returns
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    domain_id: domain.wms.increff.returns_rto_qc
    table_id: table.zs_observe.increff_returns
    canonical_table_id: table.zs_observe.increff_returns
    physical_table_reference: zs_observe.increff_returns
    source_role: wms_returns
    source_role_label: WMS returns, RTO and QC
    source_family: wms
    configured_source_description: fulfilment/WMS
    canonical_source_pack: increff_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.increff_returns.group_level_id
      runtime_value: '29'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - brand filter for Mensa-specific returns where applicable
    - runtime group_level_id filter
    grain_from_reusable_pack: one WMS return event or return item row
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Increff WMS WMS sales and dispatch binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Increff WMS WMS sales
    - increff_sales
    - zs_observe.increff_sales
    - fulfilment/WMS
    - Bracheium Brand Technologies Pvt Ltd Increff WMS WMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Increff WMS WMS sales source
    - Increff WMS WMS sales runtime binding
    - increff_sales for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Increff
      WMS WMS sales evidence should use zs_observe.increff_sales. Apply group_level_id=29 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in increff_wms.md. It is a runtime routing bridge, not
      a reusable domain card.
    business_questions:
    - Which Increff WMS WMS rows should answer Bracheium Brand Technologies Pvt Ltd's WMS sales question?
    - Which group scope and active-row filters apply before querying increff_sales?
    - Which marketplace, logistics, or OMS binding should be joined only through a documented cross-domain profile?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - WMS
    - wms_sales
    included_concepts:
    - zs_observe.increff_sales
    - WMS sales
    - Increff WMS
    - warehouse operations
    - fulfilment/return traceability
    - group_level_id=29
    - increff_wms.md
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    - platform_id:platform.increff
    - platform_context_id:platform_context.increff.in_wms
    - domain_id:domain.wms.increff.forward_fulfilment
    - table_id:table.zs_observe.increff_sales
    - source_role:wms_sales
    - runtime_source_family:wms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Increff WMS WMS sales binding selects zs_observe.increff_sales
      as WMS evidence. Scope: group_level_id=29. Reusable semantics come from increff_wms.md. Coverage status: active.
      Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Increff WMS
    - WMS sales
    - WMS
    - zs_observe.increff_sales
    - increff_sales
    - wms_sales
    - increff_wms.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - increff_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded increff_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    domain_id: domain.wms.increff.forward_fulfilment
    table_id: table.zs_observe.increff_sales
    source_role: wms_sales
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    platform_id: platform.increff
    platform_context_id: platform_context.increff.in_wms
    domain_id: domain.wms.increff.forward_fulfilment
    table_id: table.zs_observe.increff_sales
    canonical_table_id: table.zs_observe.increff_sales
    physical_table_reference: zs_observe.increff_sales
    source_role: wms_sales
    source_role_label: WMS sales and dispatch
    source_family: wms
    configured_source_description: fulfilment/WMS
    canonical_source_pack: increff_wms.md
    coverage_status: active
    active: true
    runtime_scope_status: runtime_group_level_scope_available
    runtime_scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.increff_sales.group_level_id
      runtime_value: '29'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - order_status = COMPLETED for completed dispatch analysis
    - transaction_type = SALES for revenue analysis
    - runtime group_level_id filter
    grain_from_reusable_pack: one WMS order or order-line fulfilment row
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — JioMart — oms_sales
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
    vendor_or_system: JioMart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - JioMart OMS sales
    - jiomart_oms
    - zs_observe.jiomart_oms
    - OMS, Settlement, Returns, Transactions
    - Bracheium Brand Technologies Pvt Ltd JioMart OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd JioMart OMS sales source
    - JioMart OMS sales runtime binding
    - jiomart_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's JioMart
      OMS sales evidence should use zs_observe.jiomart_oms. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which JioMart OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep jiomart_oms limited to Bracheium Brand Technologies Pvt Ltd?
    - What JioMart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.jiomart_oms
    - OMS sales
    - JioMart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    - platform_id:platform.jiomart
    - platform_context_id:platform_context.jiomart.in
    - source_role:oms_sales
    - table_id:table.zs_observe.jiomart_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the JioMart OMS sales binding selects zs_observe.jiomart_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - JioMart
    - OMS sales
    - marketplace
    - zs_observe.jiomart_oms
    - jiomart_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    platform_id: platform.jiomart
    platform_context_id: platform_context.jiomart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
    table_id: table.zs_observe.jiomart_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    table_id: table.zs_observe.jiomart_oms
    source_role: oms_sales
    source_entity: JioMart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.jiomart_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — JioMart — returns
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
    vendor_or_system: JioMart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - JioMart returns
    - jiomart_returns
    - zs_observe.jiomart_returns
    - OMS, Settlement, Returns, Transactions
    - Bracheium Brand Technologies Pvt Ltd JioMart returns
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd JioMart returns source
    - JioMart returns runtime binding
    - jiomart_returns for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's JioMart
      returns evidence should use zs_observe.jiomart_returns. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which JioMart returns file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep jiomart_returns limited to Bracheium Brand Technologies Pvt Ltd?
    - What JioMart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.jiomart_returns
    - returns
    - JioMart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    - platform_id:platform.jiomart
    - platform_context_id:platform_context.jiomart.in
    - source_role:returns
    - table_id:table.zs_observe.jiomart_returns
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the JioMart returns binding selects zs_observe.jiomart_returns
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - JioMart
    - returns
    - marketplace
    - zs_observe.jiomart_returns
    - jiomart_returns
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    platform_id: platform.jiomart
    platform_context_id: platform_context.jiomart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
    table_id: table.zs_observe.jiomart_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    table_id: table.zs_observe.jiomart_returns
    source_role: returns
    source_entity: JioMart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.jiomart_returns.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — JioMart — settlement
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
    vendor_or_system: JioMart
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - JioMart settlement
    - jiomart_settlement
    - zs_observe.jiomart_settlement
    - OMS, Settlement, Returns, Transactions
    - Bracheium Brand Technologies Pvt Ltd JioMart settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd JioMart settlement source
    - JioMart settlement runtime binding
    - jiomart_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's JioMart
      settlement evidence should use zs_observe.jiomart_settlement. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which JioMart settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep jiomart_settlement limited to Bracheium Brand Technologies Pvt Ltd?
    - What JioMart canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.jiomart_settlement
    - settlement
    - JioMart
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    - platform_id:platform.jiomart
    - platform_context_id:platform_context.jiomart.in
    - source_role:settlement
    - table_id:table.zs_observe.jiomart_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the JioMart settlement binding selects zs_observe.jiomart_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - JioMart
    - settlement
    - marketplace
    - zs_observe.jiomart_settlement
    - jiomart_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    platform_id: platform.jiomart
    platform_context_id: platform_context.jiomart.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
    table_id: table.zs_observe.jiomart_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    table_id: table.zs_observe.jiomart_settlement
    source_role: settlement
    source_entity: JioMart
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.jiomart_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — brand_sku_mapping
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho brand/SKU mapping
    - meesho_brand_mapping
    - zs_observe.meesho_brand_mapping
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho brand/SKU mapping
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho brand/SKU mapping source
    - Meesho brand/SKU mapping runtime binding
    - meesho_brand_mapping for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      brand/SKU mapping evidence should use zs_observe.meesho_brand_mapping. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho brand/SKU mapping file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_brand_mapping limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - brand_sku_mapping
    included_concepts:
    - zs_observe.meesho_brand_mapping
    - brand/SKU mapping
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:brand_sku_mapping
    - table_id:table.zs_observe.meesho_brand_mapping
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho brand/SKU mapping binding selects zs_observe.meesho_brand_mapping
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - brand/SKU mapping
    - marketplace
    - zs_observe.meesho_brand_mapping
    - meesho_brand_mapping
    - brand_sku_mapping
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
    table_id: table.zs_observe.meesho_brand_mapping
    source_role: brand_sku_mapping
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_brand_mapping
    source_role: brand_sku_mapping
    source_entity: Meesho
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_brand_mapping.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — forward_expense_invoice
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho forward expense invoice
    - meesho_forward_expenses
    - zs_observe.meesho_forward_expenses
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho forward expense invoice
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho forward expense invoice source
    - Meesho forward expense invoice runtime binding
    - meesho_forward_expenses for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      forward expense invoice evidence should use zs_observe.meesho_forward_expenses. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho forward expense invoice file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_forward_expenses limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - forward_expense_invoice
    included_concepts:
    - zs_observe.meesho_forward_expenses
    - forward expense invoice
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:forward_expense_invoice
    - table_id:table.zs_observe.meesho_forward_expenses
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho forward expense invoice binding selects
      zs_observe.meesho_forward_expenses as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable
      semantics come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - forward expense invoice
    - marketplace
    - zs_observe.meesho_forward_expenses
    - meesho_forward_expenses
    - forward_expense_invoice
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
    table_id: table.zs_observe.meesho_forward_expenses
    source_role: forward_expense_invoice
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_forward_expenses
    source_role: forward_expense_invoice
    source_entity: Meesho
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_forward_expenses.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — oms_sales
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho OMS sales
    - meesho_sales
    - zs_observe.meesho_sales
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho OMS sales source
    - Meesho OMS sales runtime binding
    - meesho_sales for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      OMS sales evidence should use zs_observe.meesho_sales. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_sales limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.meesho_sales
    - OMS sales
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:oms_sales
    - table_id:table.zs_observe.meesho_sales
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho OMS sales binding selects zs_observe.meesho_sales
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - OMS sales
    - marketplace
    - zs_observe.meesho_sales
    - meesho_sales
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
    table_id: table.zs_observe.meesho_sales
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_sales
    source_role: oms_sales
    source_entity: Meesho
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.meesho_sales.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_sales.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — other_charges_expense
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho other charges expense
    - meesho_other_charges_expenses
    - zs_observe.meesho_other_charges_expenses
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho other charges expense
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho other charges expense source
    - Meesho other charges expense runtime binding
    - meesho_other_charges_expenses for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      other charges expense evidence should use zs_observe.meesho_other_charges_expenses. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho other charges expense file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_other_charges_expenses limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - other_charges_expense
    included_concepts:
    - zs_observe.meesho_other_charges_expenses
    - other charges expense
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:other_charges_expense
    - table_id:table.zs_observe.meesho_other_charges_expenses
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho other charges expense binding selects
      zs_observe.meesho_other_charges_expenses as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable
      semantics come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - other charges expense
    - marketplace
    - zs_observe.meesho_other_charges_expenses
    - meesho_other_charges_expenses
    - other_charges_expense
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
    table_id: table.zs_observe.meesho_other_charges_expenses
    source_role: other_charges_expense
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_other_charges_expenses
    source_role: other_charges_expense
    source_entity: Meesho
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_other_charges_expenses.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — return_tracking
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho return tracking
    - meesho_returns
    - zs_observe.meesho_returns
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho return tracking
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho return tracking source
    - Meesho return tracking runtime binding
    - meesho_returns for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      return tracking evidence should use zs_observe.meesho_returns. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho return tracking file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_returns limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - return_tracking
    included_concepts:
    - zs_observe.meesho_returns
    - return tracking
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:return_tracking
    - table_id:table.zs_observe.meesho_returns
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho return tracking binding selects zs_observe.meesho_returns
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - return tracking
    - marketplace
    - zs_observe.meesho_returns
    - meesho_returns
    - return_tracking
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
    table_id: table.zs_observe.meesho_returns
    source_role: return_tracking
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_returns
    source_role: return_tracking
    source_entity: Meesho
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.meesho_returns.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_returns.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — reverse_expense_invoice
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho reverse expense invoice
    - meesho_reverse_expenses
    - zs_observe.meesho_reverse_expenses
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho reverse expense invoice
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho reverse expense invoice source
    - Meesho reverse expense invoice runtime binding
    - meesho_reverse_expenses for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      reverse expense invoice evidence should use zs_observe.meesho_reverse_expenses. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho reverse expense invoice file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_reverse_expenses limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - reverse_expense_invoice
    included_concepts:
    - zs_observe.meesho_reverse_expenses
    - reverse expense invoice
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:reverse_expense_invoice
    - table_id:table.zs_observe.meesho_reverse_expenses
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho reverse expense invoice binding selects
      zs_observe.meesho_reverse_expenses as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable
      semantics come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not
      for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - reverse expense invoice
    - marketplace
    - zs_observe.meesho_reverse_expenses
    - meesho_reverse_expenses
    - reverse_expense_invoice
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
    table_id: table.zs_observe.meesho_reverse_expenses
    source_role: reverse_expense_invoice
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_reverse_expenses
    source_role: reverse_expense_invoice
    source_entity: Meesho
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_reverse_expenses.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — reverse_oms
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho reverse OMS
    - meesho_reverse
    - zs_observe.meesho_reverse
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho reverse OMS
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho reverse OMS source
    - Meesho reverse OMS runtime binding
    - meesho_reverse for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      reverse OMS evidence should use zs_observe.meesho_reverse. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho reverse OMS file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_reverse limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - reverse_oms
    included_concepts:
    - zs_observe.meesho_reverse
    - reverse OMS
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:reverse_oms
    - table_id:table.zs_observe.meesho_reverse
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho reverse OMS binding selects zs_observe.meesho_reverse
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - reverse OMS
    - marketplace
    - zs_observe.meesho_reverse
    - meesho_reverse
    - reverse_oms
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
    table_id: table.zs_observe.meesho_reverse
    source_role: reverse_oms
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_reverse
    source_role: reverse_oms
    source_entity: Meesho
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.meesho_reverse.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_reverse.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Meesho — settlement
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
    vendor_or_system: Meesho
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Meesho settlement
    - meesho_settlement
    - zs_observe.meesho_settlement
    - Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment, Brand mapping, Transactions
    - Bracheium Brand Technologies Pvt Ltd Meesho settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Meesho settlement source
    - Meesho settlement runtime binding
    - meesho_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Meesho
      settlement evidence should use zs_observe.meesho_settlement. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Meesho settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep meesho_settlement limited to Bracheium Brand Technologies Pvt Ltd?
    - What Meesho canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.meesho_settlement
    - settlement
    - Meesho
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_id:platform.meesho
    - platform_context_id:platform_context.meesho.in
    - source_role:settlement
    - table_id:table.zs_observe.meesho_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Meesho settlement binding selects zs_observe.meesho_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Meesho
    - settlement
    - marketplace
    - zs_observe.meesho_settlement
    - meesho_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    platform_id: platform.meesho
    platform_context_id: platform_context.meesho.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
    table_id: table.zs_observe.meesho_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    table_id: table.zs_observe.meesho_settlement
    source_role: settlement
    source_entity: Meesho
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.meesho_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: Sales/OMS, Settlement, Returns/Reverse, Fwd/Rev expenses, Other charges, Adjustment,
      Brand mapping, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Myntra — non_order_settlement
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
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses, Transactions
    - Bracheium Brand Technologies Pvt Ltd Myntra non-order settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Myntra non-order settlement source
    - Myntra non-order settlement runtime binding
    - myntra_non_order_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Myntra
      non-order settlement evidence should use zs_observe.myntra_non_order_settlement. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra non-order settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep myntra_non_order_settlement limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:non_order_settlement
    - table_id:table.zs_observe.myntra_non_order_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Myntra non-order settlement binding selects zs_observe.myntra_non_order_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Myntra
    - non-order settlement
    - marketplace
    - zs_observe.myntra_non_order_settlement
    - myntra_non_order_settlement
    - non_order_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    table_id: table.zs_observe.myntra_non_order_settlement
    source_role: non_order_settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_non_order_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses,
      Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Myntra — oms_sales
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
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses, Transactions
    - Bracheium Brand Technologies Pvt Ltd Myntra OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Myntra OMS sales source
    - Myntra OMS sales runtime binding
    - myntra_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Myntra
      OMS sales evidence should use zs_observe.myntra_oms. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep myntra_oms limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:oms_sales
    - table_id:table.zs_observe.myntra_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Myntra OMS sales binding selects zs_observe.myntra_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Myntra
    - OMS sales
    - marketplace
    - zs_observe.myntra_oms
    - myntra_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    table_id: table.zs_observe.myntra_oms
    source_role: oms_sales
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses,
      Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Myntra — returns
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
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses, Transactions
    - Bracheium Brand Technologies Pvt Ltd Myntra returns
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Myntra returns source
    - Myntra returns runtime binding
    - myntra_reverse for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Myntra
      returns evidence should use zs_observe.myntra_reverse. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra returns file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep myntra_reverse limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:returns
    - table_id:table.zs_observe.myntra_reverse
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Myntra returns binding selects zs_observe.myntra_reverse
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Myntra
    - returns
    - marketplace
    - zs_observe.myntra_reverse
    - myntra_reverse
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    table_id: table.zs_observe.myntra_reverse
    source_role: returns
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_reverse.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_reverse.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses,
      Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Myntra — settlement
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
      PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses, Transactions
    - Bracheium Brand Technologies Pvt Ltd Myntra settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Myntra settlement source
    - Myntra settlement runtime binding
    - myntra_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Myntra
      settlement evidence should use zs_observe.myntra_settlement. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Myntra settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep myntra_settlement limited to Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    - platform_id:platform.myntra
    - platform_context_id:platform_context.myntra.in
    - source_role:settlement
    - table_id:table.zs_observe.myntra_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Myntra settlement binding selects zs_observe.myntra_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Myntra
    - settlement
    - marketplace
    - zs_observe.myntra_settlement
    - myntra_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    platform_id: platform.myntra
    platform_context_id: platform_context.myntra.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    table_id: table.zs_observe.myntra_settlement
    source_role: settlement
    source_entity: Myntra
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.myntra_settlement.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.myntra_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS (JIT + PPMP), Seller reports (Fwd + Rev), Fwd/Rev settlement (JIT + PPMP), Non-order
      settlement (JIT + PPMP), Non-order expenses, Returns/RTO (JIT + PPMP), JIT GSTR return, VHS + VFS expenses,
      Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator primary_operational_source
    binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Shiprocket Logistics Aggregator primary operational source
    - shiprocket_oms
    - zs_observe.shiprocket_oms
    - table.zs_observe.shiprocket_oms
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator primary operational source
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator primary operational source source
    - Shiprocket Logistics Aggregator primary operational source runtime binding
    - shiprocket_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Shiprocket
      Logistics Aggregator primary operational source evidence should use zs_observe.shiprocket_oms. Apply group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Shiprocket Logistics Aggregator logistics rows should answer Bracheium Brand Technologies Pvt Ltd's
      primary operational source question?
    - Which courier/account scope must be applied before using shiprocket_oms?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - primary_operational_source
    included_concepts:
    - zs_observe.shiprocket_oms
    - primary operational source
    - Shiprocket Logistics Aggregator
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    - platform_id:platform.shiprocket
    - platform_context_id:platform_context.shiprocket.in
    - source_role:primary_operational_source
    - table_id:table.zs_observe.shiprocket_oms
    - runtime_source_family:logistics
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Shiprocket Logistics Aggregator primary operational
      source binding selects zs_observe.shiprocket_oms as logistics / courier evidence. Scope: group_level_id=29.
      Reusable semantics come from logistics_integrated.md. Coverage status: active. Use this card for runtime source
      resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Shiprocket Logistics Aggregator
    - primary operational source
    - logistics / courier
    - zs_observe.shiprocket_oms
    - shiprocket_oms
    - primary_operational_source
    - logistics_integrated.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    platform_id: platform.shiprocket
    platform_context_id: platform_context.shiprocket.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
    table_id: table.zs_observe.shiprocket_oms
    source_role: primary_operational_source
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    table_id: table.zs_observe.shiprocket_oms
    source_role: primary_operational_source
    source_entity: Shiprocket Logistics Aggregator
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shiprocket_oms.group_level_id
      runtime_value: '29'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.shiprocket_oms
    canonical_table_coverage_status: active
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS oms_sales binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Shopify
      D2C OMS OMS sales evidence should use zs_observe.shopify_oms. Apply group_id=9, group_level_id=29 before SQL
      handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Bracheium Brand Technologies Pvt Ltd's OMS sales question?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms
      as OMS evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - shopify_d2c_oms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    source_entity: Shopify D2C OMS
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.shopify_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '29'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: available_shopify_pack_context
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS returns binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS returns
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Shopify
      D2C OMS returns evidence should use zs_observe.shopify_returns. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Bracheium Brand Technologies Pvt Ltd's returns question?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns
      as OMS evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - shopify_d2c_oms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
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

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — commission_invoice
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal commission invoice
    - snapdeal_commission
    - zs_observe.snapdeal_commission
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal commission invoice
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal commission invoice source
    - Snapdeal commission invoice runtime binding
    - snapdeal_commission for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      commission invoice evidence should use zs_observe.snapdeal_commission. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal commission invoice file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_commission limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - commission_invoice
    included_concepts:
    - zs_observe.snapdeal_commission
    - commission invoice
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:commission_invoice
    - table_id:table.zs_observe.snapdeal_commission
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal commission invoice binding selects zs_observe.snapdeal_commission
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - commission invoice
    - marketplace
    - zs_observe.snapdeal_commission
    - snapdeal_commission
    - commission_invoice
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
    table_id: table.zs_observe.snapdeal_commission
    source_role: commission_invoice
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_commission
    source_role: commission_invoice
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_commission.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_commission.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — marketplace_payment
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal marketplace payment
    - snapdeal_payments
    - zs_observe.snapdeal_payments
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal marketplace payment
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal marketplace payment source
    - Snapdeal marketplace payment runtime binding
    - snapdeal_payments for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      marketplace payment evidence should use zs_observe.snapdeal_payments. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal marketplace payment file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_payments limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - marketplace_payment
    included_concepts:
    - zs_observe.snapdeal_payments
    - marketplace payment
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:marketplace_payment
    - table_id:table.zs_observe.snapdeal_payments
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal marketplace payment binding selects
      zs_observe.snapdeal_payments as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics
      come from uploaded marketplace canonical pack. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - marketplace payment
    - marketplace
    - zs_observe.snapdeal_payments
    - snapdeal_payments
    - marketplace_payment
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
    table_id: table.zs_observe.snapdeal_payments
    source_role: marketplace_payment
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_payments
    source_role: marketplace_payment
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_payments.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_payments.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — non_order_tds
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal non-order TDS
    - snapdeal_non_order
    - zs_observe.snapdeal_non_order
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal non-order TDS
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal non-order TDS source
    - Snapdeal non-order TDS runtime binding
    - snapdeal_non_order for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      non-order TDS evidence should use zs_observe.snapdeal_non_order. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal non-order TDS file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_non_order limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - non_order_tds
    included_concepts:
    - zs_observe.snapdeal_non_order
    - non-order TDS
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:non_order_tds
    - table_id:table.zs_observe.snapdeal_non_order
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal non-order TDS binding selects zs_observe.snapdeal_non_order
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - non-order TDS
    - marketplace
    - zs_observe.snapdeal_non_order
    - snapdeal_non_order
    - non_order_tds
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
    table_id: table.zs_observe.snapdeal_non_order
    source_role: non_order_tds
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_non_order
    source_role: non_order_tds
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_non_order.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_non_order.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — oms_sales
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal OMS sales
    - snapdeal_oms
    - zs_observe.snapdeal_oms
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal OMS sales
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal OMS sales source
    - Snapdeal OMS sales runtime binding
    - snapdeal_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      OMS sales evidence should use zs_observe.snapdeal_oms. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal OMS sales file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_oms limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.snapdeal_oms
    - OMS sales
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:oms_sales
    - table_id:table.zs_observe.snapdeal_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal OMS sales binding selects zs_observe.snapdeal_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - OMS sales
    - marketplace
    - zs_observe.snapdeal_oms
    - snapdeal_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
    table_id: table.zs_observe.snapdeal_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_oms
    source_role: oms_sales
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — sales_return
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal sales return
    - snapdeal_sales_return
    - zs_observe.snapdeal_sales_return
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal sales return
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal sales return source
    - Snapdeal sales return runtime binding
    - snapdeal_sales_return for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      sales return evidence should use zs_observe.snapdeal_sales_return. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal sales return file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_sales_return limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - sales_return
    included_concepts:
    - zs_observe.snapdeal_sales_return
    - sales return
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:sales_return
    - table_id:table.zs_observe.snapdeal_sales_return
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal sales return binding selects zs_observe.snapdeal_sales_return
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - sales return
    - marketplace
    - zs_observe.snapdeal_sales_return
    - snapdeal_sales_return
    - sales_return
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
    table_id: table.zs_observe.snapdeal_sales_return
    source_role: sales_return
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_sales_return
    source_role: sales_return
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_sales_return.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_sales_return.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Snapdeal — settlement
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
    vendor_or_system: Snapdeal
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Snapdeal settlement
    - snapdeal_settlement
    - zs_observe.snapdeal_settlement
    - OMS, Settlement, Commission file (5-sheet), Transactions
    - Bracheium Brand Technologies Pvt Ltd Snapdeal settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Snapdeal settlement source
    - Snapdeal settlement runtime binding
    - snapdeal_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Snapdeal
      settlement evidence should use zs_observe.snapdeal_settlement. Apply group_id=9, group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Snapdeal settlement file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep snapdeal_settlement limited to Bracheium Brand Technologies Pvt Ltd?
    - What Snapdeal canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.snapdeal_settlement
    - settlement
    - Snapdeal
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_id:platform.snapdeal
    - platform_context_id:platform_context.snapdeal.in
    - source_role:settlement
    - table_id:table.zs_observe.snapdeal_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Snapdeal settlement binding selects zs_observe.snapdeal_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Snapdeal
    - settlement
    - marketplace
    - zs_observe.snapdeal_settlement
    - snapdeal_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    platform_id: platform.snapdeal
    platform_context_id: platform_context.snapdeal.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
    table_id: table.zs_observe.snapdeal_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    table_id: table.zs_observe.snapdeal_settlement
    source_role: settlement
    source_entity: Snapdeal
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.snapdeal_settlement.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.snapdeal_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Commission file (5-sheet), Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Tata Cliq — oms_invoice
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - TataCliq OMS invoice
    - tatacliq_oms
    - zs_observe.tatacliq_oms
    - OMS, Settlement, Transactions
    - Bracheium Brand Technologies Pvt Ltd TataCliq OMS invoice
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd TataCliq OMS invoice source
    - TataCliq OMS invoice runtime binding
    - tatacliq_oms for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's TataCliq
      OMS invoice evidence should use zs_observe.tatacliq_oms. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which TataCliq OMS invoice file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep tatacliq_oms limited to Bracheium Brand Technologies Pvt Ltd?
    - What TataCliq canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_invoice
    included_concepts:
    - zs_observe.tatacliq_oms
    - OMS invoice
    - TataCliq
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - source_role:oms_invoice
    - table_id:table.zs_observe.tatacliq_oms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the TataCliq OMS invoice binding selects zs_observe.tatacliq_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - TataCliq
    - OMS invoice
    - marketplace
    - zs_observe.tatacliq_oms
    - tatacliq_oms
    - oms_invoice
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    table_id: table.zs_observe.tatacliq_oms
    source_role: oms_invoice
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    table_id: table.zs_observe.tatacliq_oms
    source_role: oms_invoice
    source_entity: TataCliq
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.tatacliq_oms.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.tatacliq_oms.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd — Tata Cliq — settlement_payout
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
    vendor_or_system: TataCliq
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - TataCliq settlement payout
    - tatacliq_settlement
    - zs_observe.tatacliq_settlement
    - OMS, Settlement, Transactions
    - Bracheium Brand Technologies Pvt Ltd TataCliq settlement payout
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd TataCliq settlement payout source
    - TataCliq settlement payout runtime binding
    - tatacliq_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's TataCliq
      settlement payout evidence should use zs_observe.tatacliq_settlement. Apply group_id=9, group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which TataCliq settlement payout file/table is active for Bracheium Brand Technologies Pvt Ltd?
    - Which group filters keep tatacliq_settlement limited to Bracheium Brand Technologies Pvt Ltd?
    - What TataCliq canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement_payout
    included_concepts:
    - zs_observe.tatacliq_settlement
    - settlement payout
    - TataCliq
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    - platform_id:platform.tatacliq
    - platform_context_id:platform_context.tatacliq.in
    - source_role:settlement_payout
    - table_id:table.zs_observe.tatacliq_settlement
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the TataCliq settlement payout binding selects zs_observe.tatacliq_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - TataCliq
    - settlement payout
    - marketplace
    - zs_observe.tatacliq_settlement
    - tatacliq_settlement
    - settlement_payout
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    platform_id: platform.tatacliq
    platform_context_id: platform_context.tatacliq.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
    table_id: table.zs_observe.tatacliq_settlement
    source_role: settlement_payout
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    table_id: table.zs_observe.tatacliq_settlement
    source_role: settlement_payout
    source_entity: TataCliq
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.tatacliq_settlement.group_level_id
      runtime_value: '29'
    active: true
    source_configuration_text: OMS, Settlement, Transactions
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Unicommerce WMS invoice transaction ledger binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS WMS invoice transaction ledger
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS WMS invoice transaction ledger source
    - Unicommerce WMS WMS invoice transaction ledger runtime binding
    - unicommerce for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Unicommerce
      WMS WMS invoice transaction ledger evidence should use zs_observe.unicommerce. Apply group_level_id=29 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Bracheium Brand Technologies Pvt Ltd's WMS invoice transaction
      ledger question?
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
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce
    - source_role:wms_invoice_transaction_ledger
    - runtime_source_family:wms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Unicommerce WMS WMS invoice transaction ledger
      binding selects zs_observe.unicommerce as WMS evidence. Scope: group_level_id=29. Reusable semantics come
      from unicommerce_wms.md. Coverage status: active. Use this card for runtime source resolution, not for defining
      table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Unicommerce WMS
    - WMS invoice transaction ledger
    - WMS
    - zs_observe.unicommerce
    - unicommerce
    - wms_invoice_transaction_ledger
    - unicommerce_wms.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - unicommerce_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce
    source_role: wms_invoice_transaction_ledger
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
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
      value: '29'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce.group_level_id
      runtime_value: '29'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter
    - metadata filter when separating sales, returns, or cancellations
    grain_from_reusable_pack: order or SKU invoice transaction row carrying sales, reverse return, or cancellation
      classification
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Unicommerce WMS order sales report shipment tracking binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS WMS shipment tracking
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Unicommerce WMS WMS shipment tracking source
    - Unicommerce WMS WMS shipment tracking runtime binding
    - unicommerce_order_sales_report for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Unicommerce
      WMS WMS shipment tracking evidence should use zs_observe.unicommerce_order_sales_report. Apply group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in unicommerce_wms.md. It
      is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Unicommerce WMS WMS rows should answer Bracheium Brand Technologies Pvt Ltd's WMS shipment tracking
      question?
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
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    - platform_id:platform.unicommerce
    - platform_context_id:platform_context.unicommerce.in_wms
    - domain_id:domain.wms.unicommerce.fulfilment_operations
    - table_id:table.zs_observe.unicommerce_order_sales_report
    - source_role:wms_shipment_tracking
    - runtime_source_family:wms
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Unicommerce WMS WMS shipment tracking binding
      selects zs_observe.unicommerce_order_sales_report as WMS evidence. Scope: group_level_id=29. Reusable semantics
      come from unicommerce_wms.md. Coverage status: active. Use this card for runtime source resolution, not for
      defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Unicommerce WMS
    - WMS shipment tracking
    - WMS
    - zs_observe.unicommerce_order_sales_report
    - unicommerce_order_sales_report
    - wms_shipment_tracking
    - unicommerce_wms.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - unicommerce_wms.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded unicommerce_wms.md
    source_format: client_docx_runtime_overlay_plus_reusable_wms_canonical_pack
    evidence_refs:
    - client_runtime.wms_scope
    evidence_ids:
    - client_runtime.wms_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    platform_id: platform.unicommerce
    platform_context_id: platform_context.unicommerce.in_wms
    domain_id: domain.wms.unicommerce.fulfilment_operations
    table_id: table.zs_observe.unicommerce_order_sales_report
    source_role: wms_shipment_tracking
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    runtime_source_family: wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
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
      value: '29'
      data_type: integer
      scope_name: group_level_id
      scope_column_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
      runtime_value: '29'
    mandatory_filters_from_reusable_pack:
    - is_active = true
    - runtime group_level_id filter when available
    grain_from_reusable_pack: shipment or order-SKU operational row carrying delivery status, AWB, courier method,
      MRP and package dimensions
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd XpressBees Logistics native_courier_cod_settlement_sparse
    binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - XpressBees Logistics native courier COD settlement
    - xpressbees_settlement
    - zs_observe.xpressbees_settlement
    - table.zs_observe.xpressbees_settlement
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics native courier COD settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd XpressBees Logistics native courier COD settlement source
    - XpressBees Logistics native courier COD settlement runtime binding
    - xpressbees_settlement for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's XpressBees
      Logistics native courier COD settlement evidence should use zs_observe.xpressbees_settlement. Apply group_level_id=29
      before SQL handoff. Reusable field, metric, and reconciliation semantics remain in logistics_integrated.md.
      It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which XpressBees Logistics logistics rows should answer Bracheium Brand Technologies Pvt Ltd's native courier
      COD settlement question?
    - Which courier/account scope must be applied before using xpressbees_settlement?
    - Which OMS or marketplace binding provides the expected order side for this courier evidence?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - logistics_courier
    - native_courier_cod_settlement_sparse
    included_concepts:
    - zs_observe.xpressbees_settlement
    - native courier COD settlement
    - XpressBees Logistics
    - courier settlement or invoice evidence
    - shipment references
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    - platform_id:platform.xpressbees
    - platform_context_id:platform_context.xpressbees.in
    - source_role:native_courier_cod_settlement_sparse
    - table_id:table.zs_observe.xpressbees_settlement
    - runtime_source_family:logistics
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the XpressBees Logistics native courier COD settlement
      binding selects zs_observe.xpressbees_settlement as logistics / courier evidence. Scope: group_level_id=29.
      Reusable semantics come from logistics_integrated.md. Coverage status: schema_partial. Use this card for runtime
      source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - XpressBees Logistics
    - native courier COD settlement
    - logistics / courier
    - zs_observe.xpressbees_settlement
    - xpressbees_settlement
    - native_courier_cod_settlement_sparse
    - logistics_integrated.md
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    platform_id: platform.xpressbees
    platform_context_id: platform_context.xpressbees.in
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    table_id: table.zs_observe.xpressbees_settlement
    source_role: native_courier_cod_settlement_sparse
    runtime_source_family: logistics
  fields:
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    table_id: table.zs_observe.xpressbees_settlement
    source_role: native_courier_cod_settlement_sparse
    source_entity: XpressBees Logistics
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '29'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.xpressbees_settlement.group_level_id
      runtime_value: '29'
    scope_key_status: runtime_group_level_id_scope_available
    active: true
    source_configuration_text: table.zs_observe.xpressbees_settlement
    canonical_table_coverage_status: schema_partial
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd Cashfree Settlement Txns sheet binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd Cashfree settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd Cashfree settlement source
    - Cashfree settlement runtime binding
    - cashfree_payin for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's Cashfree
      settlement evidence should use zs_observe.cashfree_payin. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Cashfree settlement rows represent expected gateway evidence for Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    - platform_id:platform.cashfree
    - platform_context_id:platform_context.cashfree.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.cashfree_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the Cashfree settlement binding selects zs_observe.cashfree_payin
      as payment gateway evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Cashfree
    - settlement
    - payment gateway
    - zs_observe.cashfree_payin
    - cashfree_payin
    - payment_gateway.md
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    platform_id: platform.cashfree
    platform_context_id: platform_context.cashfree.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.cashfree_payin
    canonical_table_id: table.zs_observe.cashfree_payin
    physical_table_reference: zs_observe.cashfree_payin
    configured_pipeline_target: cashfree_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: Cashfree Settlement Txns sheet
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '9'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '9'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '29'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '29'
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

#### account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin

```yaml
canonical_card:
  canonical_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  card_type: account_data_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd PhonePe pay-in reconciliation binding
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
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
    - Bracheium Brand Technologies Pvt Ltd PhonePe settlement
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd PhonePe settlement source
    - PhonePe settlement runtime binding
    - phonepe_payin for Bracheium Brand Technologies Pvt Ltd
    business_meaning: This account-data binding tells the resolver that Bracheium Brand Technologies Pvt Ltd's PhonePe
      settlement evidence should use zs_observe.phonepe_payin. Apply group_id=9, group_level_id=29 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in payment_gateway.md. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which PhonePe settlement rows represent expected gateway evidence for Bracheium Brand Technologies Pvt Ltd?
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
    - group_id=9
    - group_level_id=29
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - platform_account_id:platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    - platform_id:platform.phonepe
    - platform_context_id:platform_context.phonepe.in
    - domain_id:domain.payment_gateway.settlement
    - table_id:table.zs_observe.phonepe_payin
    - source_role:settlement
    - runtime_source_family:payment_gateway
    embedding_text: 'For Bracheium Brand Technologies Pvt Ltd, the PhonePe settlement binding selects zs_observe.phonepe_payin
      as payment gateway evidence. Scope: group_id=9, group_level_id=29. Reusable semantics come from payment_gateway.md.
      Coverage status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - PhonePe
    - settlement
    - payment gateway
    - zs_observe.phonepe_payin
    - phonepe_payin
    - payment_gateway.md
    - group_id=9
    - group_level_id=29
    exact_match_keys:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.phonepe_payin
    source_role: settlement
    account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
    runtime_source_family: payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    platform_id: platform.phonepe
    platform_context_id: platform_context.phonepe.in
    domain_id: domain.payment_gateway.settlement
    table_id: table.zs_observe.phonepe_payin
    canonical_table_id: table.zs_observe.phonepe_payin
    physical_table_reference: zs_observe.phonepe_payin
    configured_pipeline_target: phonepe_payin
    mapping_status: canonical_table_exact_or_directly_supported
    source_role: settlement
    source_role_label: PhonePe pay-in reconciliation
    source_family: payment_gateway
    canonical_source_pack: payment_gateway.md
    coverage_status: active
    active: true
    runtime_scope_status: gateway_source_bound_but_merchant_identifier_not_present_in_client_docx
    runtime_scope_keys:
    - business_key: group_id
      column: null
      operator: '='
      value: '9'
      data_type: integer
      scope_name: runtime_group_id
      scope_column_id: null
      runtime_value: '9'
      scope_application: runtime_or_ingestion_metadata
    - business_key: group_level_id
      column: null
      operator: '='
      value: '29'
      data_type: integer
      scope_name: runtime_group_level_id
      scope_column_id: null
      runtime_value: '29'
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


### 2.5 Business Scope Set Cards

#### business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics

```yaml
canonical_card:
  canonical_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  card_type: business_scope_set
  canonical_name: Bracheium Brand Technologies Pvt Ltd logistics scope
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
    runtime_source_family: logistics
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd logistics scope
    - Bracheium Brand Technologies Pvt Ltd logistics / courier scope
    - logistics / courier runtime scope set
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd logistics / courier scope
    - logistics / courier accounts and bindings
    - Bracheium Brand Technologies Pvt Ltd logistics / courier resolver input
    business_meaning: Business scope set for Bracheium Brand Technologies Pvt Ltd's logistics / courier runtime
      resolution. It groups 2 platform accounts and 2 account-data bindings so the resolver can choose client-scoped
      sources before entering reusable canonical packs.
    business_questions:
    - Which logistics / courier accounts and bindings are active for Bracheium Brand Technologies Pvt Ltd?
    - Which runtime table bindings should be considered together under Bracheium Brand Technologies Pvt Ltd logistics
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - logistics_courier
    - resolver_scope
    included_concepts:
    - 2 platform accounts
    - 2 account-data bindings
    - 1 deferred sources
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - business_scope_set_id:business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
    - runtime_source_family:logistics
    embedding_text: Bracheium Brand Technologies Pvt Ltd logistics scope groups Bracheium Brand Technologies Pvt
      Ltd's logistics / courier runtime accounts and table bindings. Use it to restrict traversal to the client's
      configured sources; unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd logistics scope
    - logistics / courier
    - business scope set
    - 2 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    scope_name: Bracheium Brand Technologies Pvt Ltd logistics scope
    scope_type: logistics_courier_reconciliation
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
    - platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
    platform_ids:
    - platform.shiprocket
    - platform.xpressbees
    platform_context_ids:
    - platform_context.shiprocket.in
    - platform_context.xpressbees.in
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    group_scope_values:
      group_id: '9'
      group_level_id: '29'
    deferred_sources:
    - label: XpressBees invoice
      config: invoice
      reason: No native XpressBees invoice table card in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  card_type: business_scope_set
  canonical_name: Bracheium Brand Technologies Pvt Ltd marketplace scope
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd marketplace scope
    - marketplace accounts and bindings
    - Bracheium Brand Technologies Pvt Ltd marketplace resolver input
    business_meaning: Business scope set for Bracheium Brand Technologies Pvt Ltd's marketplace runtime resolution.
      It groups 7 platform accounts and 31 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Bracheium Brand Technologies Pvt Ltd?
    - Which runtime table bindings should be considered together under Bracheium Brand Technologies Pvt Ltd marketplace
      scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 7 platform accounts
    - 31 account-data bindings
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - business_scope_set_id:business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
    embedding_text: Bracheium Brand Technologies Pvt Ltd marketplace scope groups Bracheium Brand Technologies Pvt
      Ltd's marketplace runtime accounts and table bindings. Use it to restrict traversal to the client's configured
      sources; unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd marketplace scope
    - marketplace
    - business scope set
    - 7 accounts
    - 31 bindings
    exact_match_keys:
    - business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    scope_name: Bracheium Brand Technologies Pvt Ltd marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
    - platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
    platform_ids:
    - platform.amazon
    - platform.flipkart
    - platform.jiomart
    - platform.meesho
    - platform.myntra
    - platform.snapdeal
    - platform.tatacliq
    platform_context_ids:
    - platform_context.amazon.in
    - platform_context.flipkart.in
    - platform_context.jiomart.in
    - platform_context.meesho.in
    - platform_context.myntra.in
    - platform_context.snapdeal.in
    - platform_context.tatacliq.in
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
```

#### business_scope_set.bracheium_brand_technologies_pvt_ltd.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  card_type: business_scope_set
  canonical_name: Bracheium Brand Technologies Pvt Ltd OMS runtime scope
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd OMS runtime scope
    - Bracheium Brand Technologies Pvt Ltd OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd OMS scope
    - OMS accounts and bindings
    - Bracheium Brand Technologies Pvt Ltd OMS resolver input
    business_meaning: Business scope set for Bracheium Brand Technologies Pvt Ltd's OMS runtime resolution. It groups
      1 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which OMS accounts and bindings are active for Bracheium Brand Technologies Pvt Ltd?
    - Which runtime table bindings should be considered together under Bracheium Brand Technologies Pvt Ltd OMS
      runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - OMS
    - resolver_scope
    included_concepts:
    - 1 platform accounts
    - 2 account-data bindings
    - 1 deferred sources
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:oms
    embedding_text: Bracheium Brand Technologies Pvt Ltd OMS runtime scope groups Bracheium Brand Technologies Pvt
      Ltd's OMS runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
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
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
      account_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Shiprocket order source
      config: order source table
      reason: Shiprocket OMS table is already bound in the logistics runtime slice for this client; no duplicate
        OMS binding emitted.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.bracheium_brand_technologies_pvt_ltd.wms

```yaml
canonical_card:
  canonical_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  card_type: business_scope_set
  canonical_name: Bracheium Brand Technologies Pvt Ltd WMS runtime scope
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd WMS runtime scope
    - Bracheium Brand Technologies Pvt Ltd WMS scope
    - WMS runtime scope set
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd WMS scope
    - WMS accounts and bindings
    - Bracheium Brand Technologies Pvt Ltd WMS resolver input
    business_meaning: Business scope set for Bracheium Brand Technologies Pvt Ltd's WMS runtime resolution. It groups
      2 platform accounts and 4 account-data bindings so the resolver can choose client-scoped sources before entering
      reusable canonical packs.
    business_questions:
    - Which WMS accounts and bindings are active for Bracheium Brand Technologies Pvt Ltd?
    - Which runtime table bindings should be considered together under Bracheium Brand Technologies Pvt Ltd WMS
      runtime scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - WMS
    - resolver_scope
    included_concepts:
    - 2 platform accounts
    - 4 account-data bindings
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:wms
    embedding_text: Bracheium Brand Technologies Pvt Ltd WMS runtime scope groups Bracheium Brand Technologies Pvt
      Ltd's WMS runtime accounts and table bindings. Use it to restrict traversal to the client's configured sources;
      unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd WMS runtime scope
    - WMS
    - business scope set
    - 2 accounts
    - 4 bindings
    exact_match_keys:
    - business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
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
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: wms
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd WMS runtime scope
    binding_type: wms_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    - platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
    included_platform_ids:
    - platform.increff
    - platform.unicommerce
    included_platform_context_ids:
    - platform_context.increff.in_wms
    - platform_context.unicommerce.in_wms
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
      source_role: wms_sales
      table_id: table.zs_observe.increff_sales
      domain_id: domain.wms.increff.forward_fulfilment
      canonical_source_pack: increff_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
      source_role: wms_returns
      table_id: table.zs_observe.increff_returns
      domain_id: domain.wms.increff.returns_rto_qc
      canonical_source_pack: increff_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway

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
  canonical_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  card_type: business_scope_set
  canonical_name: Bracheium Brand Technologies Pvt Ltd payment gateway runtime scope
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd payment gateway runtime scope
    - Bracheium Brand Technologies Pvt Ltd payment gateway scope
    - payment gateway runtime scope set
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd payment gateway scope
    - payment gateway accounts and bindings
    - Bracheium Brand Technologies Pvt Ltd payment gateway resolver input
    business_meaning: Business scope set for Bracheium Brand Technologies Pvt Ltd's payment gateway runtime resolution.
      It groups 2 platform accounts and 2 account-data bindings so the resolver can choose client-scoped sources
      before entering reusable canonical packs.
    business_questions:
    - Which payment gateway accounts and bindings are active for Bracheium Brand Technologies Pvt Ltd?
    - Which runtime table bindings should be considered together under Bracheium Brand Technologies Pvt Ltd payment
      gateway runtime scope?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:payment_gateway
    embedding_text: Bracheium Brand Technologies Pvt Ltd payment gateway runtime scope groups Bracheium Brand Technologies
      Pvt Ltd's payment gateway runtime accounts and table bindings. Use it to restrict traversal to the client's
      configured sources; unresolved sources remain deferred until supported canonical packs exist.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd payment gateway runtime scope
    - payment gateway
    - business scope set
    - 2 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_scope
    evidence_ids:
    - client_runtime.payment_gateway_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: payment_gateway
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd payment gateway runtime scope
    binding_type: payment_gateway_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    - platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
    included_platform_ids:
    - platform.cashfree
    - platform.phonepe
    included_platform_context_ids:
    - platform_context.cashfree.in
    - platform_context.phonepe.in
    source_flow_paths:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
      account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
      platform_id: platform.phonepe
      platform_context_id: platform_context.phonepe.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.phonepe_payin
      source_role: settlement
      configured_pipeline_target: phonepe_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


### 2.6 Business Flow Binding Cards

#### business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd logistics runtime resolution
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - logistics_integrated.md
    source_path: Bracheium Brand Technologies Pvt Ltd.docx and logistics_integrated.md
    source_format: client_docx_runtime_overlay_plus_reusable_logistics_canonical_pack
    evidence_refs:
    - client_runtime.logistics_scope
    evidence_ids:
    - client_runtime.logistics_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
    runtime_source_family: logistics
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd logistics runtime resolution
    - Bracheium Brand Technologies Pvt Ltd logistics / courier flow
    - logistics / courier runtime resolution flow
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd logistics / courier resolution flow
    - logistics / courier source routing
    - Bracheium Brand Technologies Pvt Ltd runtime traversal plan
    business_meaning: Business flow binding for Bracheium Brand Technologies Pvt Ltd's logistics / courier source
      resolution. It connects the scope set to 2 platform accounts and 2 account-data bindings so questions enter
      the right client-scoped evidence before reusable semantics run.
    business_questions:
    - Which logistics / courier bindings should be traversed for Bracheium Brand Technologies Pvt Ltd's runtime
      question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - logistics_courier
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - business_flow_binding_id:business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
    - runtime_source_family:logistics
    embedding_text: Bracheium Brand Technologies Pvt Ltd logistics runtime resolution is Bracheium Brand Technologies
      Pvt Ltd's logistics / courier runtime traversal binding. It connects the business scope set to account and
      table bindings so retrieval selects client evidence first and then delegates semantics to external canonical
      packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd logistics runtime resolution
    - logistics / courier
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd logistics runtime resolution
    binding_type: logistics_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
    participating_accounts:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
      account_name: Bracheium Brand Technologies Pvt Ltd Shiprocket Logistics Aggregator account
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
      account_name: Bracheium Brand Technologies Pvt Ltd XpressBees Logistics account
    money_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
      source_role: primary_operational_source
      table_id: table.zs_observe.shiprocket_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
      source_role: native_courier_cod_settlement_sparse
      table_id: table.zs_observe.xpressbees_settlement
    deferred_sources:
    - label: XpressBees invoice
      config: invoice
      reason: No native XpressBees invoice table card in uploaded logistics_integrated.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd marketplace runtime resolution
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd marketplace runtime resolution
    - Bracheium Brand Technologies Pvt Ltd marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd marketplace resolution flow
    - marketplace source routing
    - Bracheium Brand Technologies Pvt Ltd runtime traversal plan
    business_meaning: Business flow binding for Bracheium Brand Technologies Pvt Ltd's marketplace source resolution.
      It connects the scope set to 7 platform accounts and 31 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Bracheium Brand Technologies Pvt Ltd's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 7 platform accounts
    - 31 account-data bindings
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - business_flow_binding_id:business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
    embedding_text: Bracheium Brand Technologies Pvt Ltd marketplace runtime resolution is Bracheium Brand Technologies
      Pvt Ltd's marketplace runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    source_path: Bracheium Brand Technologies Pvt Ltd.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
    participating_accounts:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
      account_name: Amazon India
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
      account_name: Flipkart
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
      account_name: Myntra
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
      account_name: Meesho
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
      account_name: JioMart
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
      account_name: Snapdeal
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
      account_name: Tata Cliq
    money_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
      source_role: disbursement
      table_id: table.zs_observe.amazon_disbursment
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
      source_role: oms_sales
      table_id: table.zs_recon_processor.flipkart_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
      source_role: settlement
      table_id: table.zs_observe.flipkart_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
      source_role: commission_fee_invoice
      table_id: table.zs_observe.flipkart_commission
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
      source_role: cashback_credit_debit_note
      table_id: table.zs_observe.flipkart_cashback
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
      source_role: oms_sales
      table_id: table.zs_observe.myntra_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
      source_role: settlement
      table_id: table.zs_observe.myntra_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
      source_role: non_order_settlement
      table_id: table.zs_observe.myntra_non_order_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
      source_role: returns
      table_id: table.zs_observe.myntra_reverse
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
      source_role: oms_sales
      table_id: table.zs_observe.meesho_sales
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
      source_role: settlement
      table_id: table.zs_observe.meesho_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
      source_role: return_tracking
      table_id: table.zs_observe.meesho_returns
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
      source_role: reverse_oms
      table_id: table.zs_observe.meesho_reverse
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
      source_role: forward_expense_invoice
      table_id: table.zs_observe.meesho_forward_expenses
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
      source_role: reverse_expense_invoice
      table_id: table.zs_observe.meesho_reverse_expenses
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
      source_role: other_charges_expense
      table_id: table.zs_observe.meesho_other_charges_expenses
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
      source_role: brand_sku_mapping
      table_id: table.zs_observe.meesho_brand_mapping
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
      source_role: oms_sales
      table_id: table.zs_observe.jiomart_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
      source_role: returns
      table_id: table.zs_observe.jiomart_returns
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
      source_role: settlement
      table_id: table.zs_observe.jiomart_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
      source_role: oms_sales
      table_id: table.zs_observe.snapdeal_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
      source_role: settlement
      table_id: table.zs_observe.snapdeal_settlement
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
      source_role: marketplace_payment
      table_id: table.zs_observe.snapdeal_payments
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
      source_role: commission_invoice
      table_id: table.zs_observe.snapdeal_commission
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
      source_role: sales_return
      table_id: table.zs_observe.snapdeal_sales_return
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
      source_role: non_order_tds
      table_id: table.zs_observe.snapdeal_non_order
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
      source_role: oms_invoice
      table_id: table.zs_observe.tatacliq_oms
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
      source_role: settlement_payout
      table_id: table.zs_observe.tatacliq_settlement
    deferred_sources:
    - label: Cred
      config: Sales, Settlement, Returns, Transactions
      reason: Cred marketplace pack not uploaded
    - label: FirstCry
      config: OMS — WB, Settlement — WB, Returns — WB, RTO — WB
      reason: FirstCry marketplace pack not uploaded
    - label: Klip · Blitz
      config: Settlement only
      reason: Klip/Blitz settlement pack not uploaded
```

#### business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd OMS runtime resolution flow
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd OMS runtime resolution flow
    - Bracheium Brand Technologies Pvt Ltd OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd OMS resolution flow
    - OMS source routing
    - Bracheium Brand Technologies Pvt Ltd runtime traversal plan
    business_meaning: Business flow binding for Bracheium Brand Technologies Pvt Ltd's OMS source resolution. It
      connects the scope set to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Bracheium Brand Technologies Pvt Ltd's runtime question?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:oms
    embedding_text: Bracheium Brand Technologies Pvt Ltd OMS runtime resolution flow is Bracheium Brand Technologies
      Pvt Ltd's OMS runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
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
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    binding_name: Bracheium Brand Technologies Pvt Ltd OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
      account_name: Bracheium Brand Technologies Pvt Ltd Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Shiprocket order source
      config: order source table
      reason: Shiprocket OMS table is already bound in the logistics runtime slice for this client; no duplicate
        OMS binding emitted.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd WMS runtime resolution
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
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd WMS runtime resolution
    - Bracheium Brand Technologies Pvt Ltd WMS flow
    - WMS runtime resolution flow
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd WMS resolution flow
    - WMS source routing
    - Bracheium Brand Technologies Pvt Ltd runtime traversal plan
    business_meaning: Business flow binding for Bracheium Brand Technologies Pvt Ltd's WMS source resolution. It
      connects the scope set to 2 platform accounts and 4 account-data bindings so questions enter the right client-scoped
      evidence before reusable semantics run.
    business_questions:
    - Which WMS bindings should be traversed for Bracheium Brand Technologies Pvt Ltd's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - WMS
    - runtime_traversal
    included_concepts:
    - 2 platform accounts
    - 4 account-data bindings
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:wms
    embedding_text: Bracheium Brand Technologies Pvt Ltd WMS runtime resolution is Bracheium Brand Technologies
      Pvt Ltd's WMS runtime traversal binding. It connects the business scope set to account and table bindings
      so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd WMS runtime resolution
    - WMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
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
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: wms
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
    flow_name: Bracheium Brand Technologies Pvt Ltd WMS runtime resolution
    flow_type: wms_source_resolution
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
    - platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
    source_flow_paths:
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
      source_role: wms_invoice_transaction_ledger
      table_id: table.zs_observe.unicommerce
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
      source_role: wms_shipment_tracking
      table_id: table.zs_observe.unicommerce_order_sales_report
      domain_id: domain.wms.unicommerce.fulfilment_operations
      canonical_source_pack: unicommerce_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
      source_role: wms_sales
      table_id: table.zs_observe.increff_sales
      domain_id: domain.wms.increff.forward_fulfilment
      canonical_source_pack: increff_wms.md
    - account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
      platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
      source_role: wms_returns
      table_id: table.zs_observe.increff_returns
      domain_id: domain.wms.increff.returns_rto_qc
      canonical_source_pack: increff_wms.md
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution

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
  canonical_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Bracheium Brand Technologies Pvt Ltd payment gateway runtime resolution
  ownership:
    layer: runtime
    domain_family: client_runtime
    vendor_or_system: Bracheium Brand Technologies Pvt Ltd
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: true
    client_runtime_layer: true
  semantic:
    aliases:
    - Bracheium Brand Technologies Pvt Ltd payment gateway runtime resolution
    - Bracheium Brand Technologies Pvt Ltd payment gateway flow
    - payment gateway runtime resolution flow
    colloquial_phrases:
    - Bracheium Brand Technologies Pvt Ltd payment gateway resolution flow
    - payment gateway source routing
    - Bracheium Brand Technologies Pvt Ltd runtime traversal plan
    business_meaning: Business flow binding for Bracheium Brand Technologies Pvt Ltd's payment gateway source resolution.
      It connects the scope set to 2 platform accounts and 2 account-data bindings so questions enter the right
      client-scoped evidence before reusable semantics run.
    business_questions:
    - Which payment gateway bindings should be traversed for Bracheium Brand Technologies Pvt Ltd's runtime question?
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
    - tenant_id:tenant.bracheium_brand_technologies_pvt_ltd
    - group_id:group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    - runtime_source_family:payment_gateway
    embedding_text: Bracheium Brand Technologies Pvt Ltd payment gateway runtime resolution is Bracheium Brand Technologies
      Pvt Ltd's payment gateway runtime traversal binding. It connects the business scope set to account and table
      bindings so retrieval selects client evidence first and then delegates semantics to external canonical packs.
    search_keywords:
    - Bracheium Brand Technologies Pvt Ltd
    - Bracheium Brand Technologies Pvt Ltd payment gateway runtime resolution
    - payment gateway
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  evidence:
    source_documents:
    - Bracheium Brand Technologies Pvt Ltd.docx
    - payment_gateway.md
    source_path: client DOCX plus uploaded payment_gateway.md
    source_format: client_docx_runtime_overlay_plus_reusable_payment_gateway_canonical_pack
    evidence_refs:
    - client_runtime.payment_gateway_flow
    evidence_ids:
    - client_runtime.payment_gateway_flow
    source_line: null
  traversal:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    runtime_source_family: payment_gateway
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  fields:
    tenant_id: tenant.bracheium_brand_technologies_pvt_ltd
    group_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
    business_flow_binding_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
    business_scope_set_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
    flow_name: Bracheium Brand Technologies Pvt Ltd payment gateway runtime resolution
    flow_type: payment_gateway_source_resolution
    platform_account_ids:
    - platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
    - platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
    account_data_binding_ids:
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
    - account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
    source_flow_paths:
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
      account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
      platform_id: platform.cashfree
      platform_context_id: platform_context.cashfree.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.cashfree_payin
      source_role: settlement
      configured_pipeline_target: cashfree_payin
      mapping_status: canonical_table_exact_or_directly_supported
    - platform_account_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
      account_data_binding_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
      platform_id: platform.phonepe
      platform_context_id: platform_context.phonepe.in
      domain_id: domain.payment_gateway.settlement
      table_id: table.zs_observe.phonepe_payin
      source_role: settlement
      configured_pipeline_target: phonepe_payin
      mapping_status: canonical_table_exact_or_directly_supported
    runtime_layer_policy: client_scope_and_account_binding_only_no_reusable_semantic_cards_created_here
```


## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_applies_scope_column.column_zs_observe_amazon_disbursment_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: column.zs_observe.amazon_disbursment.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_applies_scope_column.column_zs_observe_flipkart_cashback_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: column.zs_observe.flipkart_cashback.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_applies_scope_column.column_zs_observe_flipkart_commission_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: column.zs_observe.flipkart_commission.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_applies_scope_column.column_zs_recon_processor_flipkart_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: column.zs_recon_processor.flipkart_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_applies_scope_column.column_zs_observe_flipkart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: column.zs_observe.flipkart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_applies_scope_column.column_zs_observe_increff_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_applies_scope_column.column_zs_observe_increff_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  target_card_id: column.zs_observe.increff_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '29'
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_applies_scope_column.column_zs_observe_increff_sales_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_applies_scope_column.column_zs_observe_increff_sales_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  target_card_id: column.zs_observe.increff_sales.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '29'
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_applies_scope_column.column_zs_observe_jiomart_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_applies_scope_column.column_zs_observe_jiomart_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_applies_scope_column.column_zs_observe_jiomart_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_applies_scope_column.column_zs_observe_jiomart_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  target_card_id: column.zs_observe.jiomart_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_applies_scope_column.column_zs_observe_jiomart_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_applies_scope_column.column_zs_observe_jiomart_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_applies_scope_column.column_zs_observe_jiomart_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_applies_scope_column.column_zs_observe_jiomart_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  target_card_id: column.zs_observe.jiomart_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_applies_scope_column.column_zs_observe_jiomart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_applies_scope_column.column_zs_observe_jiomart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_applies_scope_column.column_zs_observe_jiomart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_applies_scope_column.column_zs_observe_jiomart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  target_card_id: column.zs_observe.jiomart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_applies_scope_column.column_zs_observe_meesho_brand_mapping_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_applies_scope_column.column_zs_observe_meesho_brand_mapping_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  target_card_id: column.zs_observe.meesho_brand_mapping.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_applies_scope_column.column_zs_observe_meesho_brand_mapping_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_applies_scope_column.column_zs_observe_meesho_brand_mapping_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  target_card_id: column.zs_observe.meesho_brand_mapping.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_forward_expenses_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_forward_expenses_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  target_card_id: column.zs_observe.meesho_forward_expenses.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_forward_expenses_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_forward_expenses_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  target_card_id: column.zs_observe.meesho_forward_expenses.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_applies_scope_column.column_zs_observe_meesho_sales_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_applies_scope_column.column_zs_observe_meesho_sales_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  target_card_id: column.zs_observe.meesho_sales.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_applies_scope_column.column_zs_observe_meesho_sales_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_applies_scope_column.column_zs_observe_meesho_sales_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  target_card_id: column.zs_observe.meesho_sales.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_other_charges_expenses_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_other_charges_expenses_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  target_card_id: column.zs_observe.meesho_other_charges_expenses.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_other_charges_expenses_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_other_charges_expenses_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  target_card_id: column.zs_observe.meesho_other_charges_expenses.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_applies_scope_column.column_zs_observe_meesho_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_applies_scope_column.column_zs_observe_meesho_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  target_card_id: column.zs_observe.meesho_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_applies_scope_column.column_zs_observe_meesho_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_applies_scope_column.column_zs_observe_meesho_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  target_card_id: column.zs_observe.meesho_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_expenses_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_expenses_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  target_card_id: column.zs_observe.meesho_reverse_expenses.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_expenses_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_expenses_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  target_card_id: column.zs_observe.meesho_reverse_expenses.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  target_card_id: column.zs_observe.meesho_reverse.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_applies_scope_column.column_zs_observe_meesho_reverse_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  target_card_id: column.zs_observe.meesho_reverse.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_applies_scope_column.column_zs_observe_meesho_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_applies_scope_column.column_zs_observe_meesho_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  target_card_id: column.zs_observe.meesho_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_applies_scope_column.column_zs_observe_meesho_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_applies_scope_column.column_zs_observe_meesho_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  target_card_id: column.zs_observe.meesho_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_non_order_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: column.zs_observe.myntra_non_order_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_applies_scope_column.column_zs_observe_myntra_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: column.zs_observe.myntra_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_applies_scope_column.column_zs_observe_myntra_reverse_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  target_card_id: column.zs_observe.myntra_reverse.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_applies_scope_column.column_zs_observe_myntra_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: column.zs_observe.myntra_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_applies_scope_column.column_zs_observe_shiprocket_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  target_card_id: column.zs_observe.shiprocket_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_commission_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_commission_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  target_card_id: column.zs_observe.snapdeal_commission.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_commission_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_commission_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  target_card_id: column.zs_observe.snapdeal_commission.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_payments_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_payments_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  target_card_id: column.zs_observe.snapdeal_payments.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_payments_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_payments_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  target_card_id: column.zs_observe.snapdeal_payments.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_non_order_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_non_order_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  target_card_id: column.zs_observe.snapdeal_non_order.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_non_order_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_non_order_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  target_card_id: column.zs_observe.snapdeal_non_order.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  target_card_id: column.zs_observe.snapdeal_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  target_card_id: column.zs_observe.snapdeal_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_sales_return_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_sales_return_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  target_card_id: column.zs_observe.snapdeal_sales_return.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_sales_return_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_sales_return_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  target_card_id: column.zs_observe.snapdeal_sales_return.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  target_card_id: column.zs_observe.snapdeal_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_applies_scope_column.column_zs_observe_snapdeal_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  target_card_id: column.zs_observe.snapdeal_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: column.zs_observe.tatacliq_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_applies_scope_column.column_zs_observe_tatacliq_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: column.zs_observe.tatacliq_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: column.zs_observe.unicommerce.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '29'
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_applies_scope_column.column_zs_observe_unicommerce_order_sales_report_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: column.zs_observe.unicommerce_order_sales_report.group_level_id
  confidence: high
  review_status: accepted
  properties:
    scope_column: group_level_id
    runtime_value: '29'
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_applies_scope_column.column_zs_observe_xpressbees_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_applies_scope_column.column_zs_observe_xpressbees_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: column.zs_observe.xpressbees_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment.account_data_binding_binds_to_table.table_zs_observe_amazon_disbursment
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  target_card_id: table.zs_observe.amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback.account_data_binding_binds_to_table.table_zs_observe_flipkart_cashback
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  target_card_id: table.zs_observe.flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission.account_data_binding_binds_to_table.table_zs_observe_flipkart_commission
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  target_card_id: table.zs_observe.flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms.account_data_binding_binds_to_table.table_zs_recon_processor_flipkart_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  target_card_id: table.zs_recon_processor.flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement.account_data_binding_binds_to_table.table_zs_observe_flipkart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  target_card_id: table.zs_observe.flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_binds_to_table.table_zs_observe_increff_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns.account_data_binding_binds_to_table.table_zs_observe_increff_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  target_card_id: table.zs_observe.increff_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_binds_to_table.table_zs_observe_increff_sales

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales.account_data_binding_binds_to_table.table_zs_observe_increff_sales
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  target_card_id: table.zs_observe.increff_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_binds_to_table.table_zs_observe_jiomart_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms.account_data_binding_binds_to_table.table_zs_observe_jiomart_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  target_card_id: table.zs_observe.jiomart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_binds_to_table.table_zs_observe_jiomart_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns.account_data_binding_binds_to_table.table_zs_observe_jiomart_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  target_card_id: table.zs_observe.jiomart_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_binds_to_table.table_zs_observe_jiomart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement.account_data_binding_binds_to_table.table_zs_observe_jiomart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  target_card_id: table.zs_observe.jiomart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_binds_to_table.table_zs_observe_meesho_brand_mapping

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping.account_data_binding_binds_to_table.table_zs_observe_meesho_brand_mapping
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  target_card_id: table.zs_observe.meesho_brand_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_forward_expenses

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_forward_expenses
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  target_card_id: table.zs_observe.meesho_forward_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_binds_to_table.table_zs_observe_meesho_sales

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales.account_data_binding_binds_to_table.table_zs_observe_meesho_sales
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  target_card_id: table.zs_observe.meesho_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_other_charges_expenses

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_other_charges_expenses
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  target_card_id: table.zs_observe.meesho_other_charges_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_binds_to_table.table_zs_observe_meesho_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns.account_data_binding_binds_to_table.table_zs_observe_meesho_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  target_card_id: table.zs_observe.meesho_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_reverse_expenses

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses.account_data_binding_binds_to_table.table_zs_observe_meesho_reverse_expenses
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  target_card_id: table.zs_observe.meesho_reverse_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_binds_to_table.table_zs_observe_meesho_reverse

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse.account_data_binding_binds_to_table.table_zs_observe_meesho_reverse
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  target_card_id: table.zs_observe.meesho_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_binds_to_table.table_zs_observe_meesho_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement.account_data_binding_binds_to_table.table_zs_observe_meesho_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  target_card_id: table.zs_observe.meesho_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_non_order_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  target_card_id: table.zs_observe.myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms.account_data_binding_binds_to_table.table_zs_observe_myntra_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  target_card_id: table.zs_observe.myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse.account_data_binding_binds_to_table.table_zs_observe_myntra_reverse
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  target_card_id: table.zs_observe.myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement.account_data_binding_binds_to_table.table_zs_observe_myntra_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  target_card_id: table.zs_observe.myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_binds_to_table.table_zs_observe_shiprocket_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms.account_data_binding_binds_to_table.table_zs_observe_shiprocket_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  target_card_id: table.zs_observe.shiprocket_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_binds_to_table.table_zs_observe_snapdeal_commission

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission.account_data_binding_binds_to_table.table_zs_observe_snapdeal_commission
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  target_card_id: table.zs_observe.snapdeal_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_binds_to_table.table_zs_observe_snapdeal_payments

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments.account_data_binding_binds_to_table.table_zs_observe_snapdeal_payments
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  target_card_id: table.zs_observe.snapdeal_payments
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_binds_to_table.table_zs_observe_snapdeal_non_order

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order.account_data_binding_binds_to_table.table_zs_observe_snapdeal_non_order
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  target_card_id: table.zs_observe.snapdeal_non_order
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_binds_to_table.table_zs_observe_snapdeal_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms.account_data_binding_binds_to_table.table_zs_observe_snapdeal_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  target_card_id: table.zs_observe.snapdeal_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_binds_to_table.table_zs_observe_snapdeal_sales_return

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return.account_data_binding_binds_to_table.table_zs_observe_snapdeal_sales_return
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  target_card_id: table.zs_observe.snapdeal_sales_return
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_binds_to_table.table_zs_observe_snapdeal_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement.account_data_binding_binds_to_table.table_zs_observe_snapdeal_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  target_card_id: table.zs_observe.snapdeal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_binds_to_table.table_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms.account_data_binding_binds_to_table.table_zs_observe_tatacliq_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  target_card_id: table.zs_observe.tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_binds_to_table.table_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement.account_data_binding_binds_to_table.table_zs_observe_tatacliq_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  target_card_id: table.zs_observe.tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce.account_data_binding_binds_to_table.table_zs_observe_unicommerce
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  target_card_id: table.zs_observe.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report.account_data_binding_binds_to_table.table_zs_observe_unicommerce_order_sales_report
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  target_card_id: table.zs_observe.unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_binds_to_table.table_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement.account_data_binding_binds_to_table.table_zs_observe_xpressbees_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  target_card_id: table.zs_observe.xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform.platform_shiprocket
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform.platform_xpressbees

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform.platform_xpressbees
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform.xpressbees
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_flipkart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_jiomart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_jiomart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.jiomart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_meesho

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_meesho
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.meesho
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_myntra
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_snapdeal

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_snapdeal
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.snapdeal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_tatacliq

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform.platform_tatacliq
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform.tatacliq
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform.platform_increff

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform.platform_increff
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform.increff
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform.platform_unicommerce
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_context.platform_context_shiprocket_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_context.platform_context_xpressbees_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics.business_scope_set_includes_platform_context.platform_context_xpressbees_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  target_card_id: platform_context.xpressbees.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_flipkart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_jiomart_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_jiomart_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.jiomart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_meesho_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_meesho_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.meesho.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_myntra_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_snapdeal_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_snapdeal_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.snapdeal.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_tatacliq_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace.business_scope_set_includes_platform_context.platform_context_tatacliq_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  target_card_id: platform_context.tatacliq.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_context.platform_context_increff_in_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_context.platform_context_increff_in_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform_context.increff.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms.business_scope_set_includes_platform_context.platform_context_unicommerce_in_wms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_belongs_to_tenant.tenant_bracheium_brand_technologies_pvt_ltd

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_belongs_to_tenant.tenant_bracheium_brand_technologies_pvt_ltd
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: tenant.bracheium_brand_technologies_pvt_ltd
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_logistics_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.logistics_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_wms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.wms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_logistics
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_wms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_disbursement_zs_observe_amazon_disbursment
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.disbursement.zs_observe_amazon_disbursment
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_amazon_india_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.amazon_india.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_cashback_credit_debit_note_zs_observe_flipkart_cashback
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.cashback_credit_debit_note.zs_observe_flipkart_cashback
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_commission_fee_invoice_zs_observe_flipkart_commission
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.commission_fee_invoice.zs_observe_flipkart_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_oms_sales_zs_recon_processor_flipkart_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.oms_sales.zs_recon_processor_flipkart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_flipkart_settlement_zs_observe_flipkart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.flipkart.settlement.zs_observe_flipkart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_returns_zs_observe_increff_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_returns.zs_observe_increff_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_increff_wms_wms_sales_zs_observe_increff_sales
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.increff_wms.wms_sales.zs_observe_increff_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_oms_sales_zs_observe_jiomart_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.oms_sales.zs_observe_jiomart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_returns_zs_observe_jiomart_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.returns.zs_observe_jiomart_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_jiomart_settlement_zs_observe_jiomart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.jiomart.settlement.zs_observe_jiomart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_brand_sku_mapping_zs_observe_meesho_brand_mapping
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.brand_sku_mapping.zs_observe_meesho_brand_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_forward_expense_invoice_zs_observe_meesho_forward_expenses
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.forward_expense_invoice.zs_observe_meesho_forward_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_oms_sales_zs_observe_meesho_sales
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.oms_sales.zs_observe_meesho_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_other_charges_expense_zs_observe_meesho_other_charges_expenses
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.other_charges_expense.zs_observe_meesho_other_charges_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_return_tracking_zs_observe_meesho_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.return_tracking.zs_observe_meesho_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_expense_invoice_zs_observe_meesho_reverse_expenses
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_expense_invoice.zs_observe_meesho_reverse_expenses
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_reverse_oms_zs_observe_meesho_reverse
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.reverse_oms.zs_observe_meesho_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_meesho_settlement_zs_observe_meesho_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.meesho.settlement.zs_observe_meesho_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_non_order_settlement_zs_observe_myntra_non_order_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.non_order_settlement.zs_observe_myntra_non_order_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_oms_sales_zs_observe_myntra_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.oms_sales.zs_observe_myntra_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_returns_zs_observe_myntra_reverse
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.returns.zs_observe_myntra_reverse
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_myntra_settlement_zs_observe_myntra_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.myntra.settlement.zs_observe_myntra_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shiprocket_primary_operational_source_zs_observe_shiprocket_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shiprocket.primary_operational_source.zs_observe_shiprocket_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_commission_invoice_zs_observe_snapdeal_commission
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.commission_invoice.zs_observe_snapdeal_commission
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace_payment_zs_observe_snapdeal_payments
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace_payment.zs_observe_snapdeal_payments
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_non_order_tds_zs_observe_snapdeal_non_order
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.non_order_tds.zs_observe_snapdeal_non_order
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_oms_sales_zs_observe_snapdeal_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.oms_sales.zs_observe_snapdeal_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_sales_return_zs_observe_snapdeal_sales_return
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.sales_return.zs_observe_snapdeal_sales_return
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_snapdeal_settlement_zs_observe_snapdeal_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.snapdeal.settlement.zs_observe_snapdeal_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_oms_invoice_zs_observe_tatacliq_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.oms_invoice.zs_observe_tatacliq_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_tata_cliq_settlement_payout_zs_observe_tatacliq_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.tata_cliq.settlement_payout.zs_observe_tatacliq_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_invoice_transaction_ledger_zs_observe_unicommerce
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_invoice_transaction_ledger.zs_observe_unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms_shipment_tracking_zs_observe_unicommerce_order_sales_report
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms_shipment_tracking.zs_observe_unicommerce_order_sales_report
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_xpressbees_native_courier_cod_settlement_sparse_zs_observe_xpressbees_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.xpressbees.native_courier_cod_settlement_sparse.zs_observe_xpressbees_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_uses_platform.platform_flipkart

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_uses_platform.platform_flipkart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: platform.flipkart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_uses_platform.platform_increff

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_uses_platform.platform_increff
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  target_card_id: platform.increff
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_uses_platform.platform_jiomart

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_uses_platform.platform_jiomart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: platform.jiomart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_uses_platform.platform_meesho

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_uses_platform.platform_meesho
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: platform.meesho
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_uses_platform.platform_myntra

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_uses_platform.platform_myntra
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: platform.myntra
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_uses_platform.platform_shiprocket
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  target_card_id: platform.shiprocket
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_uses_platform.platform_snapdeal

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_uses_platform.platform_snapdeal
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: platform.snapdeal
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_uses_platform.platform_tatacliq

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_uses_platform.platform_tatacliq
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  target_card_id: platform.tatacliq
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_uses_platform.platform_unicommerce
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  target_card_id: platform.unicommerce
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_uses_platform.platform_xpressbees

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_uses_platform.platform_xpressbees
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  target_card_id: platform.xpressbees
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_amazon_india_marketplace.platform_account_uses_platform_context.platform_context_amazon_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.amazon_india.marketplace
  target_card_id: platform_context.amazon.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_flipkart_marketplace.platform_account_uses_platform_context.platform_context_flipkart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.flipkart.marketplace
  target_card_id: platform_context.flipkart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_uses_platform_context.platform_context_increff_in_wms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_increff_wms_wms.platform_account_uses_platform_context.platform_context_increff_in_wms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.increff_wms.wms
  target_card_id: platform_context.increff.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_uses_platform_context.platform_context_jiomart_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_jiomart_marketplace.platform_account_uses_platform_context.platform_context_jiomart_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.jiomart.marketplace
  target_card_id: platform_context.jiomart.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_uses_platform_context.platform_context_meesho_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_meesho_marketplace.platform_account_uses_platform_context.platform_context_meesho_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.meesho.marketplace
  target_card_id: platform_context.meesho.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_myntra_marketplace.platform_account_uses_platform_context.platform_context_myntra_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.myntra.marketplace
  target_card_id: platform_context.myntra.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shiprocket_logistics.platform_account_uses_platform_context.platform_context_shiprocket_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shiprocket.logistics
  target_card_id: platform_context.shiprocket.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_uses_platform_context.platform_context_snapdeal_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_snapdeal_marketplace.platform_account_uses_platform_context.platform_context_snapdeal_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.snapdeal.marketplace
  target_card_id: platform_context.snapdeal.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_uses_platform_context.platform_context_tatacliq_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_tata_cliq_marketplace.platform_account_uses_platform_context.platform_context_tatacliq_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.tata_cliq.marketplace
  target_card_id: platform_context.tatacliq.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_unicommerce_wms_wms.platform_account_uses_platform_context.platform_context_unicommerce_in_wms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.unicommerce_wms.wms
  target_card_id: platform_context.unicommerce.in_wms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_uses_platform_context.platform_context_xpressbees_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_xpressbees_logistics.platform_account_uses_platform_context.platform_context_xpressbees_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.xpressbees.logistics
  target_card_id: platform_context.xpressbees.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics
```

### TENANT_HAS_GROUP

#### edge.tenant_bracheium_brand_technologies_pvt_ltd.tenant_has_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.tenant_bracheium_brand_technologies_pvt_ltd.tenant_has_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.bracheium_brand_technologies_pvt_ltd
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```


<!-- Added bank/payment runtime edges -->

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_belongs_to_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin.account_data_binding_binds_to_table.table_zs_observe_cashfree_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  target_card_id: table.zs_observe.cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_binds_to_table.table_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin.account_data_binding_binds_to_table.table_zs_observe_phonepe_payin
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  target_card_id: table.zs_observe.phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform.platform_cashfree
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform.platform_phonepe

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform.platform_phonepe
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform.phonepe
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_context.platform_context_cashfree_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_context.platform_context_phonepe_in

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway.business_scope_set_includes_platform_context.platform_context_phonepe_in
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  target_card_id: platform_context.phonepe.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_flow_binding.business_flow_binding_bracheium_brand_technologies_pvt_ltd_payment_gateway_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_flow_binding.bracheium_brand_technologies_pvt_ltd.payment_gateway_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_business_scope_set.business_scope_set_bracheium_brand_technologies_pvt_ltd_payment_gateway
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: business_scope_set.bracheium_brand_technologies_pvt_ltd.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway

```yaml
canonical_edge:
  edge_id: edge.group_bracheium_brand_technologies_pvt_ltd_g9_gl29.group_has_platform_account.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  target_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_belongs_to_group.group_bracheium_brand_technologies_pvt_ltd_g9_gl29
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  target_card_id: group.bracheium_brand_technologies_pvt_ltd.g9.gl29
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_cashfree_settlement_zs_observe_cashfree_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.cashfree.settlement.zs_observe_cashfree_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_has_account_data_binding.account_data_binding_bracheium_brand_technologies_pvt_ltd_phonepe_settlement_zs_observe_phonepe_payin
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  target_card_id: account_data_binding.bracheium_brand_technologies_pvt_ltd.phonepe.settlement.zs_observe_phonepe_payin
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_uses_platform.platform_cashfree
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  target_card_id: platform.cashfree
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_uses_platform.platform_phonepe

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_uses_platform.platform_phonepe
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  target_card_id: platform.phonepe
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_cashfree_payment_gateway.platform_account_uses_platform_context.platform_context_cashfree_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.cashfree.payment_gateway
  target_card_id: platform_context.cashfree.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```

#### edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_uses_platform_context.platform_context_phonepe_in

```yaml
canonical_edge:
  edge_id: edge.platform_account_bracheium_brand_technologies_pvt_ltd_phonepe_payment_gateway.platform_account_uses_platform_context.platform_context_phonepe_in
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.bracheium_brand_technologies_pvt_ltd.phonepe.payment_gateway
  target_card_id: platform_context.phonepe.in
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms_wms_payment_bank
```
