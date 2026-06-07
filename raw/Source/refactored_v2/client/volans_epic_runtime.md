# Volans Epic LLC — Client Runtime Cards v1 (Marketplace + Logistics + OMS + WMS + Payment + Bank Slice) — Runtime Semantics Rewritten + Rendered by Card Type

Runtime markdown filename: `volans_epic_runtime.md`
This file contains client-runtime cards only. It references reusable semantic cards by canonical ID and does not copy platform, domain, table, column, metric, process, reconciliation, payment, or bank cards into the client layer. Logistics runtime bindings reference `logistics_integrated.md`; OMS runtime bindings reference `oms_business_kb.md` and/or `shopify_d2c_oms.md`; WMS runtime bindings reference `increff_wms.md` and/or `unicommerce_wms.md`; payment-gateway runtime bindings reference `payment_gateway.md`; bank-statement runtime bindings reference `bank_statement.md`.

## 0. Deferred / unresolved client source mentions

```yaml
deferred_sources:
- label: Native marketplace OMS feeds
  config: Amazon/Walmart native OMS
  reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS Business
    KB binding emitted in this pass.
  source_family: oms
```

## 1. Runtime Pack Manifest

```yaml
card_counts:
  tenant: 1
  group: 1
  platform_account: 9
  account_data_binding: 19
  business_scope_set: 2
  business_flow_binding: 2
edge_counts:
  ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN: 38
  ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT: 19
  ACCOUNT_DATA_BINDING_BINDS_TO_TABLE: 19
  BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP: 2
  BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING: 19
  BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT: 9
  BUSINESS_FLOW_BINDING_USES_SCOPE_SET: 2
  BUSINESS_SCOPE_SET_BELONGS_TO_GROUP: 2
  BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING: 19
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM: 4
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT: 9
  BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT: 4
  GROUP_BELONGS_TO_TENANT: 1
  GROUP_HAS_BUSINESS_FLOW_BINDING: 2
  GROUP_HAS_BUSINESS_SCOPE_SET: 2
  GROUP_HAS_PLATFORM_ACCOUNT: 9
  PLATFORM_ACCOUNT_BELONGS_TO_GROUP: 9
  PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING: 19
  PLATFORM_ACCOUNT_USES_PLATFORM: 9
  PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT: 9
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
  deferred_financial_sources_added_or_updated: 0
```

## 2. Canonical Runtime Cards

### 2.1 Tenant Cards

#### tenant.volans_epic_llc

```yaml
canonical_card:
  canonical_id: tenant.volans_epic_llc
  card_type: tenant
  canonical_name: Volans Epic LLC
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC
    - volans_epic_llc
    - Volans Epic LLC runtime tenant
    colloquial_phrases:
    - Volans Epic LLC client runtime
    - Volans Epic LLC source configuration
    - Volans Epic LLC scoped reconciliation setup
    business_meaning: Runtime tenant identity for Volans Epic LLC. It anchors the client's marketplace, logistics,
      OMS, WMS, payment-gateway, and bank-statement bindings while keeping client scope separate from reusable domain
      semantics.
    business_questions:
    - Which source families and configured accounts belong to Volans Epic LLC?
    - Which group and account bindings should constrain Volans Epic LLC's SQL handoff?
    - After Volans Epic LLC's runtime scope is resolved, which domain layer should receive the query next?
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
    - tenant_id:tenant.volans_epic_llc
    embedding_text: Volans Epic LLC is the runtime tenant root for the client's marketplace, logistics, OMS, WMS,
      payment-gateway, and bank-statement configuration. Use it to reach group, platform-account, and account-data-binding
      nodes before invoking reusable canonical packs.
    search_keywords:
    - Volans Epic LLC
    - volans_epic_llc
    - client runtime
    - runtime tenant
    - source bindings
    exact_match_keys:
    - tenant.volans_epic_llc
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
  fields:
    tenant_slug: volans_epic_llc
    tenant_name: Volans Epic LLC
    legal_name: Volans Epic LLC
    active: true
```

### 2.2 Group Cards

#### group.volans_epic_llc.g9.gl134

```yaml
canonical_card:
  canonical_id: group.volans_epic_llc.g9.gl134
  card_type: group
  canonical_name: Volans Epic LLC group 9/134
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Mensa Brands
    - Volans Epic LLC group 9/134
    - group_id 9
    - group_level_id 134
    colloquial_phrases:
    - Volans Epic LLC group scope
    - Mensa Brands runtime scope
    - group 9 level 134 query boundary
    business_meaning: 'Runtime group scope for Volans Epic LLC: group_id=9 and group_level_id=134. It is the client-specific
      filter boundary that must be applied before resolving account bindings for US in USD.'
    business_questions:
    - Which bindings use group_id=9 and group_level_id=134?
    - Which source families are active under Mensa Brands?
    - Where should runtime scope be injected before querying reusable tables?
    semantic_tags:
    - client_runtime
    - group_scope
    - query_filter_boundary
    - runtime_group
    included_concepts:
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - group_id_value:9
    - group_level_id_value:134
    embedding_text: Mensa Brands is the runtime group node for Volans Epic LLC. Apply group_id=9 and group_level_id=134
      when traversing from the client to platform accounts, source bindings, and flow bindings.
    search_keywords:
    - Volans Epic LLC
    - Mensa Brands
    - group_id 9
    - group_level_id 134
    - runtime group scope
    exact_match_keys:
    - group.volans_epic_llc.g9.gl134
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    group_level_id: '134'
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id_value: '9'
    group_level_id_value: '134'
    group_name: Mensa Brands
    default_currency: USD
    country: US
```

### 2.3 Platform Account Cards

#### platform_account.volans_epic_llc.amazon_brazil_br.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Amazon Brazil (BR)
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
    - Amazon Brazil (BR)
    - Volans Epic LLC Amazon Brazil (BR)
    - Amazon
    - Amazon Brazil (BR) marketplace account
    colloquial_phrases:
    - Volans Epic LLC Amazon Brazil (BR) source account
    - Amazon Brazil (BR) marketplace runtime account
    - Amazon Brazil (BR) configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Amazon Brazil (BR) marketplace sources. It
      points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon Brazil (BR) table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Amazon Brazil (BR) questions traverse through?
    - Which source roles under Amazon Brazil (BR) are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Brazil (BR)
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.volans_epic_llc.amazon_brazil_br.marketplace
    embedding_text: Volans Epic LLC's Amazon Brazil (BR) platform account routes marketplace questions to platform.amazon
      / platform_context.amazon.international. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Amazon Brazil (BR)
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Brazil (BR)
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Brazil (BR)
    active: true
    configured_source_description: Settlement
```

#### platform_account.volans_epic_llc.amazon_canada_ca.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Amazon Canada (CA)
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
    - Amazon Canada (CA)
    - Volans Epic LLC Amazon Canada (CA)
    - Amazon
    - Amazon Canada (CA) marketplace account
    colloquial_phrases:
    - Volans Epic LLC Amazon Canada (CA) source account
    - Amazon Canada (CA) marketplace runtime account
    - Amazon Canada (CA) configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Amazon Canada (CA) marketplace sources. It
      points traversal to platform.amazon and platform_context.amazon.international and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Amazon Canada (CA) table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Amazon Canada (CA) questions traverse through?
    - Which source roles under Amazon Canada (CA) are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Settlement'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon Canada (CA)
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.volans_epic_llc.amazon_canada_ca.marketplace
    embedding_text: Volans Epic LLC's Amazon Canada (CA) platform account routes marketplace questions to platform.amazon
      / platform_context.amazon.international. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Amazon Canada (CA)
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon Canada (CA)
    account_type: marketplace_seller_account
    source_account_identifier: Amazon Canada (CA)
    active: true
    configured_source_description: Settlement
```

#### platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Amazon fee preview amazon_fee_preview
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
    - Amazon fee preview amazon_fee_preview
    - Volans Epic LLC Amazon fee preview amazon_fee_preview
    - Amazon
    - Amazon fee preview amazon_fee_preview marketplace account
    colloquial_phrases:
    - Volans Epic LLC Amazon fee preview amazon_fee_preview source account
    - Amazon fee preview amazon_fee_preview marketplace runtime account
    - Amazon fee preview amazon_fee_preview configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Amazon fee preview amazon_fee_preview marketplace
      sources. It points traversal to platform.amazon and platform_context.amazon.international and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Amazon fee preview amazon_fee_preview table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Amazon fee preview amazon_fee_preview questions
      traverse through?
    - Which source roles under Amazon fee preview amazon_fee_preview are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Projected fee estimates ahead of settlement close'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon fee preview amazon_fee_preview
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    embedding_text: Volans Epic LLC's Amazon fee preview amazon_fee_preview platform account routes marketplace
      questions to platform.amazon / platform_context.amazon.international. Use it to collect the client's table
      bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Amazon fee preview amazon_fee_preview
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon fee preview amazon_fee_preview
    account_type: marketplace_seller_account
    source_account_identifier: Amazon fee preview amazon_fee_preview
    active: true
    configured_source_description: Projected fee estimates ahead of settlement close
```

#### platform_account.volans_epic_llc.amazon_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.amazon_us.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Amazon US
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
    - Amazon US
    - Volans Epic LLC Amazon US
    - Amazon
    - Amazon US marketplace account
    colloquial_phrases:
    - Volans Epic LLC Amazon US source account
    - Amazon US marketplace runtime account
    - Amazon US configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Amazon US marketplace sources. It points traversal
      to platform.amazon and platform_context.amazon.international and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Amazon US table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Amazon US questions traverse through?
    - Which source roles under Amazon US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, Returns, Fee preview'
    - platform.amazon
    - platform_context.amazon.international
    - Amazon US
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - platform_account_id:platform_account.volans_epic_llc.amazon_us.marketplace
    embedding_text: Volans Epic LLC's Amazon US platform account routes marketplace questions to platform.amazon
      / platform_context.amazon.international. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Amazon US
    - Amazon
    - marketplace
    - platform.amazon
    - platform_context.amazon.international
    exact_match_keys:
    - platform_account.volans_epic_llc.amazon_us.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_name: Amazon US
    account_type: marketplace_seller_account
    source_account_identifier: Amazon US
    active: true
    configured_source_description: OMS, Settlement, Returns, Fee preview
```

#### platform_account.volans_epic_llc.shopify_d2c.oms

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.shopify_d2c.oms
  card_type: platform_account
  canonical_name: Volans Epic LLC Shopify D2C OMS account
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC Shopify D2C OMS account
    - Volans Epic LLC Volans Epic LLC Shopify D2C OMS account
    - Shopify
    - Volans Epic LLC Shopify D2C OMS account OMS account
    colloquial_phrases:
    - Volans Epic LLC Volans Epic LLC Shopify D2C OMS account source account
    - Volans Epic LLC Shopify D2C OMS account OMS runtime account
    - Volans Epic LLC Shopify D2C OMS account configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Volans Epic LLC Shopify D2C OMS account OMS
      sources. It points traversal to platform.shopify and platform_context.shopify.in.d2c_oms and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Volans Epic LLC Shopify D2C OMS account table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Volans Epic LLC Shopify D2C OMS account questions
      traverse through?
    - Which source roles under Volans Epic LLC Shopify D2C OMS account are active or review-required for this client?
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - runtime_source_family:oms
    embedding_text: Volans Epic LLC's Volans Epic LLC Shopify D2C OMS account platform account routes OMS questions
      to platform.shopify / platform_context.shopify.in.d2c_oms. Use it to collect the client's table bindings;
      do not use this account card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Volans Epic LLC Shopify D2C OMS account
    - Shopify
    - OMS
    - platform.shopify
    - platform_context.shopify.in.d2c_oms
    exact_match_keys:
    - platform_account.volans_epic_llc.shopify_d2c.oms
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    - shopify_d2c_oms.md
    source_path: Volans Epic LLC.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    runtime_source_family: oms
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_name: Volans Epic LLC Shopify D2C OMS account
    account_type: d2c_oms_account
    source_account_identifier: null
    source_account_identifier_status: not_provided_in_client_docx_not_a_runtime_blocker_when_scope_keys_exist
    active: true
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
    configured_source_description: Shopify D2C OMS and returns/refund events
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    group_scope_values:
      group_id: '9'
      group_level_id: '134'
```

#### platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Target TCIN mapping target_tcin_mapping
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target TCIN mapping target_tcin_mapping
    - Volans Epic LLC Target TCIN mapping target_tcin_mapping
    - Target Plus
    - Target TCIN mapping target_tcin_mapping marketplace account
    colloquial_phrases:
    - Volans Epic LLC Target TCIN mapping target_tcin_mapping source account
    - Target TCIN mapping target_tcin_mapping marketplace runtime account
    - Target TCIN mapping target_tcin_mapping configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Target TCIN mapping target_tcin_mapping marketplace
      sources. It points traversal to platform.target_plus and platform_context.target_plus.us and groups the client's
      table-level account-data bindings for this source.
    business_questions:
    - Which Target TCIN mapping target_tcin_mapping table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Target TCIN mapping target_tcin_mapping questions
      traverse through?
    - Which source roles under Target TCIN mapping target_tcin_mapping are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Maps Target internal item numbers (TCIN) to brand SKUs'
    - platform.target_plus
    - platform_context.target_plus.us
    - Target TCIN mapping target_tcin_mapping
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - platform_account_id:platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
    embedding_text: Volans Epic LLC's Target TCIN mapping target_tcin_mapping platform account routes marketplace
      questions to platform.target_plus / platform_context.target_plus.us. Use it to collect the client's table
      bindings; do not use this account card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Target TCIN mapping target_tcin_mapping
    - Target Plus
    - marketplace
    - platform.target_plus
    - platform_context.target_plus.us
    exact_match_keys:
    - platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    platform_account_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_name: Target TCIN mapping target_tcin_mapping
    account_type: marketplace_seller_account
    source_account_identifier: Target TCIN mapping target_tcin_mapping
    active: true
    configured_source_description: Maps Target internal item numbers (TCIN) to brand SKUs
```

#### platform_account.volans_epic_llc.target_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.target_us.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Target US
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target US
    - Volans Epic LLC Target US
    - Target Plus
    - Target US marketplace account
    colloquial_phrases:
    - Volans Epic LLC Target US source account
    - Target US marketplace runtime account
    - Target US configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Target US marketplace sources. It points traversal
      to platform.target_plus and platform_context.target_plus.us and groups the client's table-level account-data
      bindings for this source.
    business_questions:
    - Which Target US table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Target US questions traverse through?
    - Which source roles under Target US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Sales, Settlement, Returns, TCIN mapping'
    - platform.target_plus
    - platform_context.target_plus.us
    - Target US
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - platform_account_id:platform_account.volans_epic_llc.target_us.marketplace
    embedding_text: Volans Epic LLC's Target US platform account routes marketplace questions to platform.target_plus
      / platform_context.target_plus.us. Use it to collect the client's table bindings; do not use this account
      card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Target US
    - Target Plus
    - marketplace
    - platform.target_plus
    - platform_context.target_plus.us
    exact_match_keys:
    - platform_account.volans_epic_llc.target_us.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_name: Target US
    account_type: marketplace_seller_account
    source_account_identifier: Target US
    active: true
    configured_source_description: Sales, Settlement, Returns, TCIN mapping
```

#### platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Walmart ASIN–SKU walmart_lookup
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart ASIN–SKU walmart_lookup
    - Volans Epic LLC Walmart ASIN–SKU walmart_lookup
    - Walmart
    - Walmart ASIN–SKU walmart_lookup marketplace account
    colloquial_phrases:
    - Volans Epic LLC Walmart ASIN–SKU walmart_lookup source account
    - Walmart ASIN–SKU walmart_lookup marketplace runtime account
    - Walmart ASIN–SKU walmart_lookup configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Walmart ASIN–SKU walmart_lookup marketplace
      sources. It points traversal to platform.walmart and platform_context.walmart.us and groups the client's table-level
      account-data bindings for this source.
    business_questions:
    - Which Walmart ASIN–SKU walmart_lookup table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Walmart ASIN–SKU walmart_lookup questions traverse
      through?
    - Which source roles under Walmart ASIN–SKU walmart_lookup are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: Maps Walmart item IDs to brand SKUs'
    - platform.walmart
    - platform_context.walmart.us
    - Walmart ASIN–SKU walmart_lookup
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - platform_account_id:platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
    embedding_text: Volans Epic LLC's Walmart ASIN–SKU walmart_lookup platform account routes marketplace questions
      to platform.walmart / platform_context.walmart.us. Use it to collect the client's table bindings; do not use
      this account card as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Walmart ASIN–SKU walmart_lookup
    - Walmart
    - marketplace
    - platform.walmart
    - platform_context.walmart.us
    exact_match_keys:
    - platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    platform_account_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_name: Walmart ASIN–SKU walmart_lookup
    account_type: marketplace_seller_account
    source_account_identifier: Walmart ASIN–SKU walmart_lookup
    active: true
    configured_source_description: Maps Walmart item IDs to brand SKUs
```

#### platform_account.volans_epic_llc.walmart_us.marketplace

```yaml
canonical_card:
  canonical_id: platform_account.volans_epic_llc.walmart_us.marketplace
  card_type: platform_account
  canonical_name: Volans Epic LLC — Walmart US
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart US
    - Volans Epic LLC Walmart US
    - Walmart
    - Walmart US marketplace account
    colloquial_phrases:
    - Volans Epic LLC Walmart US source account
    - Walmart US marketplace runtime account
    - Walmart US configured source family
    business_meaning: Runtime platform account for Volans Epic LLC's Walmart US marketplace sources. It points traversal
      to platform.walmart and platform_context.walmart.us and groups the client's table-level account-data bindings
      for this source.
    business_questions:
    - Which Walmart US table bindings are available for Volans Epic LLC?
    - Which canonical platform/context should Volans Epic LLC's Walmart US questions traverse through?
    - Which source roles under Walmart US are active or review-required for this client?
    semantic_tags:
    - client_runtime
    - platform_account
    - marketplace
    - source_router
    included_concepts:
    - 'client configuration: OMS, Settlement, ASIN–SKU lookup'
    - platform.walmart
    - platform_context.walmart.us
    - Walmart US
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - platform_account_id:platform_account.volans_epic_llc.walmart_us.marketplace
    embedding_text: Volans Epic LLC's Walmart US platform account routes marketplace questions to platform.walmart
      / platform_context.walmart.us. Use it to collect the client's table bindings; do not use this account card
      as a table or metric definition.
    search_keywords:
    - Volans Epic LLC
    - Walmart US
    - Walmart
    - marketplace
    - platform.walmart
    - platform_context.walmart.us
    exact_match_keys:
    - platform_account.volans_epic_llc.walmart_us.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_name: Walmart US
    account_type: marketplace_seller_account
    source_account_identifier: Walmart US
    active: true
    configured_source_description: OMS, Settlement, ASIN–SKU lookup
```

### 2.4 Account Data Binding Cards

#### account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon Brazil (BR) — settlement
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
    - Settlement
    - Volans Epic LLC Amazon settlement
    colloquial_phrases:
    - Volans Epic LLC Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon settlement evidence
      should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_settlement limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_brazil_br.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Volans Epic LLC, the Amazon settlement binding selects zs_observe.amazon_settlement as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon Canada (CA) — settlement
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
    - Settlement
    - Volans Epic LLC Amazon settlement
    colloquial_phrases:
    - Volans Epic LLC Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon settlement evidence
      should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_settlement limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_canada_ca.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Volans Epic LLC, the Amazon settlement binding selects zs_observe.amazon_settlement as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Settlement
```

#### account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon fee preview amazon_fee_preview — fee_preview
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
    - Projected fee estimates ahead of settlement close
    - Volans Epic LLC Amazon fee preview
    colloquial_phrases:
    - Volans Epic LLC Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon fee preview evidence
      should use zs_observe.amazon_fee_preview. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_fee_preview limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For Volans Epic LLC, the Amazon fee preview binding selects zs_observe.amazon_fee_preview as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: Projected fee estimates ahead of settlement close
```

#### account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon fee preview amazon_fee_preview — settlement
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
    - Projected fee estimates ahead of settlement close
    - Volans Epic LLC Amazon settlement
    colloquial_phrases:
    - Volans Epic LLC Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon settlement evidence
      should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_settlement limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Volans Epic LLC, the Amazon settlement binding selects zs_observe.amazon_settlement as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Projected fee estimates ahead of settlement close
```

#### account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon US — fee_preview
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
    - OMS, Settlement, Returns, Fee preview
    - Volans Epic LLC Amazon fee preview
    colloquial_phrases:
    - Volans Epic LLC Amazon fee preview source
    - Amazon fee preview runtime binding
    - amazon_fee_preview for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon fee preview evidence
      should use zs_observe.amazon_fee_preview. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon fee preview file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_fee_preview limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:fee_preview
    - table_id:table.zs_observe.amazon_fee_preview
    embedding_text: 'For Volans Epic LLC, the Amazon fee preview binding selects zs_observe.amazon_fee_preview as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - fee preview
    - marketplace
    - zs_observe.amazon_fee_preview
    - amazon_fee_preview
    - fee_preview
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    table_id: table.zs_observe.amazon_fee_preview
    source_role: fee_preview
    source_entity: Amazon
    scope_keys:
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon US — oms_sales
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
    - OMS, Settlement, Returns, Fee preview
    - Volans Epic LLC Amazon OMS sales
    colloquial_phrases:
    - Volans Epic LLC Amazon OMS sales source
    - Amazon OMS sales runtime binding
    - amazon_oms for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon OMS sales evidence
      should use zs_observe.amazon_oms. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Amazon OMS sales file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_oms limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:oms_sales
    - table_id:table.zs_observe.amazon_oms
    embedding_text: 'For Volans Epic LLC, the Amazon OMS sales binding selects zs_observe.amazon_oms as marketplace
      evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - OMS sales
    - marketplace
    - zs_observe.amazon_oms
    - amazon_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
    table_id: table.zs_observe.amazon_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
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
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_oms.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon US — returns
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
    - OMS, Settlement, Returns, Fee preview
    - Volans Epic LLC Amazon returns
    colloquial_phrases:
    - Volans Epic LLC Amazon returns source
    - Amazon returns runtime binding
    - amazon_returns for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon returns evidence
      should use zs_observe.amazon_returns. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Amazon returns file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_returns limited to Volans Epic LLC?
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
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:returns
    - table_id:table.zs_observe.amazon_returns
    embedding_text: 'For Volans Epic LLC, the Amazon returns binding selects zs_observe.amazon_returns as marketplace
      evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - returns
    - marketplace
    - zs_observe.amazon_returns
    - amazon_returns
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
    table_id: table.zs_observe.amazon_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    table_id: table.zs_observe.amazon_returns
    source_role: returns
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_returns.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Amazon US — settlement
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
    - OMS, Settlement, Returns, Fee preview
    - Volans Epic LLC Amazon settlement
    colloquial_phrases:
    - Volans Epic LLC Amazon settlement source
    - Amazon settlement runtime binding
    - amazon_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Amazon settlement evidence
      should use zs_observe.amazon_settlement. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Amazon settlement file/table is active for Volans Epic LLC?
    - Which group filters keep amazon_settlement limited to Volans Epic LLC?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.amazon_us.marketplace
    - platform_id:platform.amazon
    - platform_context_id:platform_context.amazon.international
    - source_role:settlement
    - table_id:table.zs_observe.amazon_settlement
    embedding_text: 'For Volans Epic LLC, the Amazon settlement binding selects zs_observe.amazon_settlement as
      marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Amazon
    - settlement
    - marketplace
    - zs_observe.amazon_settlement
    - amazon_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    platform_id: platform.amazon
    platform_context_id: platform_context.amazon.international
    account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
    table_id: table.zs_observe.amazon_settlement
    source_role: settlement
    source_entity: Amazon
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.amazon_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, Returns, Fee preview
```

#### account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  card_type: account_data_binding
  canonical_name: Volans Epic LLC Shopify D2C OMS oms_sales binding
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
    vendor_or_system: Volans Epic LLC
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
    - Volans Epic LLC Shopify D2C OMS OMS sales
    colloquial_phrases:
    - Volans Epic LLC Shopify D2C OMS OMS sales source
    - Shopify D2C OMS OMS sales runtime binding
    - shopify_oms for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Shopify D2C OMS OMS sales
      evidence should use zs_observe.shopify_oms. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Volans Epic LLC's OMS sales question?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:oms_sales
    - table_id:table.zs_observe.shopify_oms
    - runtime_source_family:oms
    embedding_text: 'For Volans Epic LLC, the Shopify D2C OMS OMS sales binding selects zs_observe.shopify_oms as
      OMS evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Shopify D2C OMS
    - OMS sales
    - OMS
    - zs_observe.shopify_oms
    - shopify_oms
    - oms_sales
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    - shopify_d2c_oms.md
    source_path: Volans Epic LLC.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
    domain_id: domain.shopify.d2c_order_capture
    table_id: table.zs_observe.shopify_oms
    source_role: oms_sales
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
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
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.shopify_oms.group_level_id
      runtime_value: '134'
    scope_key_status: runtime_group_and_group_level_scope_available
    active: true
    source_configuration_text: Shopify D2C OMS and returns/refund events
    canonical_table_coverage_status: active
    canonical_source_pack: shopify_d2c_oms.md
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  card_type: account_data_binding
  canonical_name: Volans Epic LLC Shopify D2C OMS returns binding
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
    vendor_or_system: Volans Epic LLC
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
    - Volans Epic LLC Shopify D2C OMS returns
    colloquial_phrases:
    - Volans Epic LLC Shopify D2C OMS returns source
    - Shopify D2C OMS returns runtime binding
    - shopify_returns for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Shopify D2C OMS returns
      evidence should use zs_observe.shopify_returns. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in shopify_d2c_oms.md. It is a runtime routing bridge,
      not a reusable domain card.
    business_questions:
    - Which Shopify D2C OMS OMS rows should answer Volans Epic LLC's returns question?
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
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.shopify_d2c.oms
    - platform_id:platform.shopify
    - platform_context_id:platform_context.shopify.in.d2c_oms
    - source_role:returns
    - table_id:table.zs_observe.shopify_returns
    - runtime_source_family:oms
    embedding_text: 'For Volans Epic LLC, the Shopify D2C OMS returns binding selects zs_observe.shopify_returns
      as OMS evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from shopify_d2c_oms.md. Coverage
      status: active. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Shopify D2C OMS
    - returns
    - OMS
    - zs_observe.shopify_returns
    - shopify_returns
    - shopify_d2c_oms.md
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    - shopify_d2c_oms.md
    source_path: Volans Epic LLC.docx and shopify_d2c_oms.md
    source_format: client_docx_runtime_overlay_plus_reusable_oms_canonical_pack
    evidence_refs:
    - client_runtime.oms_scope
    evidence_ids:
    - client_runtime.oms_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
    platform_id: platform.shopify
    platform_context_id: platform_context.shopify.in.d2c_oms
    account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
    domain_id: domain.shopify.refunds_returns
    table_id: table.zs_observe.shopify_returns
    source_role: returns
    runtime_source_family: oms
  fields:
    platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
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
    context_fit_status: shopify_pack_exposes_in_context_non_in_client_review_currency_and_country_before_production
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

#### account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Target TCIN mapping target_tcin_mapping — orders
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus orders
    - target_tcin_mapping
    - zs_observe.target_tcin_mapping
    - Maps Target internal item numbers (TCIN) to brand SKUs
    - Volans Epic LLC Target Plus orders
    colloquial_phrases:
    - Volans Epic LLC Target Plus orders source
    - Target Plus orders runtime binding
    - target_tcin_mapping for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Target Plus orders evidence
      should use zs_observe.target_tcin_mapping. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus orders file/table is active for Volans Epic LLC?
    - Which group filters keep target_tcin_mapping limited to Volans Epic LLC?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - orders
    included_concepts:
    - zs_observe.target_tcin_mapping
    - orders
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:orders
    - table_id:table.zs_observe.target_tcin_mapping
    embedding_text: 'For Volans Epic LLC, the Target Plus orders binding selects zs_observe.target_tcin_mapping
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Target Plus
    - orders
    - marketplace
    - zs_observe.target_tcin_mapping
    - target_tcin_mapping
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
    table_id: table.zs_observe.target_tcin_mapping
    source_role: orders
  fields:
    platform_account_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
    table_id: table.zs_observe.target_tcin_mapping
    source_role: orders
    source_entity: Target Plus
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.target_tcin_mapping.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_tcin_mapping.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Maps Target internal item numbers (TCIN) to brand SKUs
```

#### account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Target US — oms_sales
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus OMS sales
    - target_sales
    - zs_observe.target_sales
    - Sales, Settlement, Returns, TCIN mapping
    - Volans Epic LLC Target Plus OMS sales
    colloquial_phrases:
    - Volans Epic LLC Target Plus OMS sales source
    - Target Plus OMS sales runtime binding
    - target_sales for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Target Plus OMS sales
      evidence should use zs_observe.target_sales. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus OMS sales file/table is active for Volans Epic LLC?
    - Which group filters keep target_sales limited to Volans Epic LLC?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.target_sales
    - OMS sales
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.target_us.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:oms_sales
    - table_id:table.zs_observe.target_sales
    embedding_text: 'For Volans Epic LLC, the Target Plus OMS sales binding selects zs_observe.target_sales as marketplace
      evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Target Plus
    - OMS sales
    - marketplace
    - zs_observe.target_sales
    - target_sales
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
    table_id: table.zs_observe.target_sales
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    table_id: table.zs_observe.target_sales
    source_role: oms_sales
    source_entity: Target Plus
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.target_sales.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_sales.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Sales, Settlement, Returns, TCIN mapping
```

#### account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Target US — orders
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus orders
    - target_tcin_mapping
    - zs_observe.target_tcin_mapping
    - Sales, Settlement, Returns, TCIN mapping
    - Volans Epic LLC Target Plus orders
    colloquial_phrases:
    - Volans Epic LLC Target Plus orders source
    - Target Plus orders runtime binding
    - target_tcin_mapping for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Target Plus orders evidence
      should use zs_observe.target_tcin_mapping. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable
      field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime
      routing bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus orders file/table is active for Volans Epic LLC?
    - Which group filters keep target_tcin_mapping limited to Volans Epic LLC?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - orders
    included_concepts:
    - zs_observe.target_tcin_mapping
    - orders
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.target_us.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:orders
    - table_id:table.zs_observe.target_tcin_mapping
    embedding_text: 'For Volans Epic LLC, the Target Plus orders binding selects zs_observe.target_tcin_mapping
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Target Plus
    - orders
    - marketplace
    - zs_observe.target_tcin_mapping
    - target_tcin_mapping
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
    table_id: table.zs_observe.target_tcin_mapping
    source_role: orders
  fields:
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    table_id: table.zs_observe.target_tcin_mapping
    source_role: orders
    source_entity: Target Plus
    scope_keys:
    - business_key: group_id
      column: group_id
      operator: '='
      value: '9'
      data_type: string
      scope_name: group_id
      scope_column_id: column.zs_observe.target_tcin_mapping.group_id
      runtime_value: '9'
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_tcin_mapping.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Sales, Settlement, Returns, TCIN mapping
```

#### account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Target US — returns
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus returns
    - target_returns
    - zs_observe.target_returns
    - Sales, Settlement, Returns, TCIN mapping
    - Volans Epic LLC Target Plus returns
    colloquial_phrases:
    - Volans Epic LLC Target Plus returns source
    - Target Plus returns runtime binding
    - target_returns for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Target Plus returns evidence
      should use zs_observe.target_returns. Apply group_id=9, group_level_id=134 before SQL handoff. Reusable field,
      metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is a runtime routing
      bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus returns file/table is active for Volans Epic LLC?
    - Which group filters keep target_returns limited to Volans Epic LLC?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - returns
    included_concepts:
    - zs_observe.target_returns
    - returns
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.target_us.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:returns
    - table_id:table.zs_observe.target_returns
    embedding_text: 'For Volans Epic LLC, the Target Plus returns binding selects zs_observe.target_returns as marketplace
      evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace canonical
      pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Target Plus
    - returns
    - marketplace
    - zs_observe.target_returns
    - target_returns
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
    table_id: table.zs_observe.target_returns
    source_role: returns
  fields:
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    table_id: table.zs_observe.target_returns
    source_role: returns
    source_entity: Target Plus
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_returns.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Sales, Settlement, Returns, TCIN mapping
```

#### account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Target US — settlement
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
    vendor_or_system: Target Plus
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Target Plus settlement
    - target_settlement
    - zs_observe.target_settlement
    - Sales, Settlement, Returns, TCIN mapping
    - Volans Epic LLC Target Plus settlement
    colloquial_phrases:
    - Volans Epic LLC Target Plus settlement source
    - Target Plus settlement runtime binding
    - target_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Target Plus settlement
      evidence should use zs_observe.target_settlement. Apply group_id=9, group_level_id=134 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Target Plus settlement file/table is active for Volans Epic LLC?
    - Which group filters keep target_settlement limited to Volans Epic LLC?
    - What Target Plus canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - settlement
    included_concepts:
    - zs_observe.target_settlement
    - settlement
    - Target Plus
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.target_us.marketplace
    - platform_id:platform.target_plus
    - platform_context_id:platform_context.target_plus.us
    - source_role:settlement
    - table_id:table.zs_observe.target_settlement
    embedding_text: 'For Volans Epic LLC, the Target Plus settlement binding selects zs_observe.target_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Target Plus
    - settlement
    - marketplace
    - zs_observe.target_settlement
    - target_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    platform_id: platform.target_plus
    platform_context_id: platform_context.target_plus.us
    account_data_binding_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
    table_id: table.zs_observe.target_settlement
    source_role: settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
    table_id: table.zs_observe.target_settlement
    source_role: settlement
    source_entity: Target Plus
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.target_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Sales, Settlement, Returns, TCIN mapping
```

#### account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Walmart ASIN–SKU walmart_lookup — catalogue_lookup
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace catalogue lookup
    - walmart_lookup
    - zs_observe.walmart_lookup
    - Maps Walmart item IDs to brand SKUs
    - Volans Epic LLC Walmart Marketplace catalogue lookup
    colloquial_phrases:
    - Volans Epic LLC Walmart Marketplace catalogue lookup source
    - Walmart Marketplace catalogue lookup runtime binding
    - walmart_lookup for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Walmart Marketplace catalogue
      lookup evidence should use zs_observe.walmart_lookup. Apply group_id=9, group_level_id=134 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace catalogue lookup file/table is active for Volans Epic LLC?
    - Which group filters keep walmart_lookup limited to Volans Epic LLC?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - catalogue_lookup
    included_concepts:
    - zs_observe.walmart_lookup
    - catalogue lookup
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:catalogue_lookup
    - table_id:table.zs_observe.walmart_lookup
    embedding_text: 'For Volans Epic LLC, the Walmart Marketplace catalogue lookup binding selects zs_observe.walmart_lookup
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Walmart Marketplace
    - catalogue lookup
    - marketplace
    - zs_observe.walmart_lookup
    - walmart_lookup
    - catalogue_lookup
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
    table_id: table.zs_observe.walmart_lookup
    source_role: catalogue_lookup
  fields:
    platform_account_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
    table_id: table.zs_observe.walmart_lookup
    source_role: catalogue_lookup
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_lookup.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: Maps Walmart item IDs to brand SKUs
```

#### account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Walmart US — catalogue_lookup
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace catalogue lookup
    - walmart_lookup
    - zs_observe.walmart_lookup
    - OMS, Settlement, ASIN–SKU lookup
    - Volans Epic LLC Walmart Marketplace catalogue lookup
    colloquial_phrases:
    - Volans Epic LLC Walmart Marketplace catalogue lookup source
    - Walmart Marketplace catalogue lookup runtime binding
    - walmart_lookup for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Walmart Marketplace catalogue
      lookup evidence should use zs_observe.walmart_lookup. Apply group_id=9, group_level_id=134 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace catalogue lookup file/table is active for Volans Epic LLC?
    - Which group filters keep walmart_lookup limited to Volans Epic LLC?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - catalogue_lookup
    included_concepts:
    - zs_observe.walmart_lookup
    - catalogue lookup
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.walmart_us.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:catalogue_lookup
    - table_id:table.zs_observe.walmart_lookup
    embedding_text: 'For Volans Epic LLC, the Walmart Marketplace catalogue lookup binding selects zs_observe.walmart_lookup
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Walmart Marketplace
    - catalogue lookup
    - marketplace
    - zs_observe.walmart_lookup
    - walmart_lookup
    - catalogue_lookup
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
    table_id: table.zs_observe.walmart_lookup
    source_role: catalogue_lookup
  fields:
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    table_id: table.zs_observe.walmart_lookup
    source_role: catalogue_lookup
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_lookup.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, ASIN–SKU lookup
```

#### account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Walmart US — marketplace_settlement
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace marketplace settlement
    - walmart_settlement
    - zs_observe.walmart_settlement
    - OMS, Settlement, ASIN–SKU lookup
    - Volans Epic LLC Walmart Marketplace marketplace settlement
    colloquial_phrases:
    - Volans Epic LLC Walmart Marketplace marketplace settlement source
    - Walmart Marketplace marketplace settlement runtime binding
    - walmart_settlement for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Walmart Marketplace marketplace
      settlement evidence should use zs_observe.walmart_settlement. Apply group_id=9, group_level_id=134 before
      SQL handoff. Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical
      pack. It is a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace marketplace settlement file/table is active for Volans Epic LLC?
    - Which group filters keep walmart_settlement limited to Volans Epic LLC?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - marketplace_settlement
    included_concepts:
    - zs_observe.walmart_settlement
    - marketplace settlement
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.walmart_us.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:marketplace_settlement
    - table_id:table.zs_observe.walmart_settlement
    embedding_text: 'For Volans Epic LLC, the Walmart Marketplace marketplace settlement binding selects zs_observe.walmart_settlement
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Walmart Marketplace
    - marketplace settlement
    - marketplace
    - zs_observe.walmart_settlement
    - walmart_settlement
    - marketplace_settlement
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
  fields:
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    table_id: table.zs_observe.walmart_settlement
    source_role: marketplace_settlement
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_settlement.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, ASIN–SKU lookup
```

#### account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms

```yaml
canonical_card:
  canonical_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  card_type: account_data_binding
  canonical_name: Volans Epic LLC — Walmart US — oms_sales
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
    vendor_or_system: Walmart Marketplace
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Walmart Marketplace OMS sales
    - walmart_oms
    - zs_observe.walmart_oms
    - OMS, Settlement, ASIN–SKU lookup
    - Volans Epic LLC Walmart Marketplace OMS sales
    colloquial_phrases:
    - Volans Epic LLC Walmart Marketplace OMS sales source
    - Walmart Marketplace OMS sales runtime binding
    - walmart_oms for Volans Epic LLC
    business_meaning: This account-data binding tells the resolver that Volans Epic LLC's Walmart Marketplace OMS
      sales evidence should use zs_observe.walmart_oms. Apply group_id=9, group_level_id=134 before SQL handoff.
      Reusable field, metric, and reconciliation semantics remain in uploaded marketplace canonical pack. It is
      a runtime routing bridge, not a reusable domain card.
    business_questions:
    - Which Walmart Marketplace OMS sales file/table is active for Volans Epic LLC?
    - Which group filters keep walmart_oms limited to Volans Epic LLC?
    - What Walmart Marketplace canonical rules should be applied after this runtime binding selects the source?
    semantic_tags:
    - client_runtime
    - account_data_binding
    - marketplace
    - oms_sales
    included_concepts:
    - zs_observe.walmart_oms
    - OMS sales
    - Walmart Marketplace
    - marketplace source role
    - client-scoped marketplace table
    - group_id=9
    - group_level_id=134
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - platform_account_id:platform_account.volans_epic_llc.walmart_us.marketplace
    - platform_id:platform.walmart
    - platform_context_id:platform_context.walmart.us
    - source_role:oms_sales
    - table_id:table.zs_observe.walmart_oms
    embedding_text: 'For Volans Epic LLC, the Walmart Marketplace OMS sales binding selects zs_observe.walmart_oms
      as marketplace evidence. Scope: group_id=9, group_level_id=134. Reusable semantics come from uploaded marketplace
      canonical pack. Use this card for runtime source resolution, not for defining table columns or metrics.'
    search_keywords:
    - Volans Epic LLC
    - Walmart Marketplace
    - OMS sales
    - marketplace
    - zs_observe.walmart_oms
    - walmart_oms
    - oms_sales
    - uploaded marketplace canonical pack
    - group_id=9
    - group_level_id=134
    exact_match_keys:
    - account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    platform_id: platform.walmart
    platform_context_id: platform_context.walmart.us
    account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
    table_id: table.zs_observe.walmart_oms
    source_role: oms_sales
  fields:
    platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
    table_id: table.zs_observe.walmart_oms
    source_role: oms_sales
    source_entity: Walmart Marketplace
    scope_keys:
    - business_key: group_level_id
      column: group_level_id
      operator: '='
      value: '134'
      data_type: string
      scope_name: group_level_id
      scope_column_id: column.zs_observe.walmart_oms.group_level_id
      runtime_value: '134'
    active: true
    source_configuration_text: OMS, Settlement, ASIN–SKU lookup
```

### 2.5 Business Scope Set Cards

#### business_scope_set.volans_epic_llc.marketplace

```yaml
canonical_card:
  canonical_id: business_scope_set.volans_epic_llc.marketplace
  card_type: business_scope_set
  canonical_name: Volans Epic LLC marketplace scope
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC marketplace scope
    - marketplace runtime scope set
    colloquial_phrases:
    - Volans Epic LLC marketplace scope
    - marketplace accounts and bindings
    - Volans Epic LLC marketplace resolver input
    business_meaning: Business scope set for Volans Epic LLC's marketplace runtime resolution. It groups 8 platform
      accounts and 17 account-data bindings so the resolver can choose client-scoped sources before entering reusable
      canonical packs.
    business_questions:
    - Which marketplace accounts and bindings are active for Volans Epic LLC?
    - Which runtime table bindings should be considered together under Volans Epic LLC marketplace scope?
    - Which deferred sources, if any, must stay unresolved until a canonical pack is supplied?
    semantic_tags:
    - client_runtime
    - business_scope_set
    - marketplace
    - resolver_scope
    included_concepts:
    - 8 platform accounts
    - 17 account-data bindings
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - business_scope_set_id:business_scope_set.volans_epic_llc.marketplace
    embedding_text: Volans Epic LLC marketplace scope groups Volans Epic LLC's marketplace runtime accounts and
      table bindings. Use it to restrict traversal to the client's configured sources; unresolved sources remain
      deferred until supported canonical packs exist.
    search_keywords:
    - Volans Epic LLC
    - Volans Epic LLC marketplace scope
    - marketplace
    - business scope set
    - 8 accounts
    - 17 bindings
    exact_match_keys:
    - business_scope_set.volans_epic_llc.marketplace
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    business_scope_set_id: business_scope_set.volans_epic_llc.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    scope_name: Volans Epic LLC marketplace scope
    scope_type: marketplace_only
    platform_account_ids:
    - platform_account.volans_epic_llc.amazon_us.marketplace
    - platform_account.volans_epic_llc.amazon_canada_ca.marketplace
    - platform_account.volans_epic_llc.amazon_brazil_br.marketplace
    - platform_account.volans_epic_llc.walmart_us.marketplace
    - platform_account.volans_epic_llc.target_us.marketplace
    - platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
    - platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
    - platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
    platform_ids:
    - platform.amazon
    - platform.target_plus
    - platform.walmart
    platform_context_ids:
    - platform_context.amazon.international
    - platform_context.target_plus.us
    - platform_context.walmart.us
    account_data_binding_ids:
    - account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
    - account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
    - account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
    - account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    - account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
    - account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
    - account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
    - account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
    - account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
    - account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
    - account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
```

#### business_scope_set.volans_epic_llc.oms

```yaml
canonical_card:
  canonical_id: business_scope_set.volans_epic_llc.oms
  card_type: business_scope_set
  canonical_name: Volans Epic LLC OMS runtime scope
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC OMS runtime scope
    - Volans Epic LLC OMS scope
    - OMS runtime scope set
    colloquial_phrases:
    - Volans Epic LLC OMS scope
    - OMS accounts and bindings
    - Volans Epic LLC OMS resolver input
    business_meaning: Business scope set for Volans Epic LLC's OMS runtime resolution. It groups 1 platform accounts
      and 2 account-data bindings so the resolver can choose client-scoped sources before entering reusable canonical
      packs.
    business_questions:
    - Which OMS accounts and bindings are active for Volans Epic LLC?
    - Which runtime table bindings should be considered together under Volans Epic LLC OMS runtime scope?
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - runtime_source_family:oms
    embedding_text: Volans Epic LLC OMS runtime scope groups Volans Epic LLC's OMS runtime accounts and table bindings.
      Use it to restrict traversal to the client's configured sources; unresolved sources remain deferred until
      supported canonical packs exist.
    search_keywords:
    - Volans Epic LLC
    - Volans Epic LLC OMS runtime scope
    - OMS
    - business scope set
    - 1 accounts
    - 2 bindings
    exact_match_keys:
    - business_scope_set.volans_epic_llc.oms
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
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    runtime_source_family: oms
    business_scope_set_id: business_scope_set.volans_epic_llc.oms
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    binding_name: Volans Epic LLC OMS runtime scope
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.volans_epic_llc.oms
    account_data_binding_ids:
    - account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
      account_name: Volans Epic LLC Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Native marketplace OMS feeds
      config: Amazon/Walmart native OMS
      reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS
        Business KB binding emitted in this pass.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

### 2.6 Business Flow Binding Cards

#### business_flow_binding.volans_epic_llc.marketplace_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Volans Epic LLC marketplace runtime resolution
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC marketplace runtime resolution
    - Volans Epic LLC marketplace flow
    - marketplace runtime resolution flow
    colloquial_phrases:
    - Volans Epic LLC marketplace resolution flow
    - marketplace source routing
    - Volans Epic LLC runtime traversal plan
    business_meaning: Business flow binding for Volans Epic LLC's marketplace source resolution. It connects the
      scope set to 8 platform accounts and 17 account-data bindings so questions enter the right client-scoped evidence
      before reusable semantics run.
    business_questions:
    - Which marketplace bindings should be traversed for Volans Epic LLC's runtime question?
    - Which scope set constrains this flow before SQL handoff?
    - Which unsupported sources must remain deferred instead of being guessed?
    semantic_tags:
    - client_runtime
    - business_flow_binding
    - marketplace
    - runtime_traversal
    included_concepts:
    - 8 platform accounts
    - 17 account-data bindings
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - business_flow_binding_id:business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
    embedding_text: Volans Epic LLC marketplace runtime resolution is Volans Epic LLC's marketplace runtime traversal
      binding. It connects the business scope set to account and table bindings so retrieval selects client evidence
      first and then delegates semantics to external canonical packs.
    search_keywords:
    - Volans Epic LLC
    - Volans Epic LLC marketplace runtime resolution
    - marketplace
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  evidence:
    source_documents:
    - Volans Epic LLC.docx
    source_path: Volans Epic LLC.docx
    source_format: client_docx_runtime_overlay
    evidence_refs:
    - client_runtime.marketplace_scope
    evidence_ids:
    - client_runtime.marketplace_scope
    source_line: null
  traversal:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    business_flow_binding_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
    business_scope_set_id: business_scope_set.volans_epic_llc.marketplace
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    binding_name: Volans Epic LLC marketplace runtime resolution
    binding_type: marketplace_source_resolution
    business_scope_set_id: business_scope_set.volans_epic_llc.marketplace
    account_data_binding_ids:
    - account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
    - account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
    - account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
    - account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
    - account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
    - account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
    - account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
    - account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
    - account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
    - account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
    - account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
    - account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
    - account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
    participating_accounts:
    - platform_account_id: platform_account.volans_epic_llc.amazon_us.marketplace
      account_name: Amazon US
    - platform_account_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
      account_name: Amazon Canada (CA)
    - platform_account_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
      account_name: Amazon Brazil (BR)
    - platform_account_id: platform_account.volans_epic_llc.walmart_us.marketplace
      account_name: Walmart US
    - platform_account_id: platform_account.volans_epic_llc.target_us.marketplace
      account_name: Target US
    - platform_account_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
      account_name: Walmart ASIN–SKU walmart_lookup
    - platform_account_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
      account_name: Target TCIN mapping target_tcin_mapping
    - platform_account_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
      account_name: Amazon fee preview amazon_fee_preview
    money_flow_paths:
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
      source_role: oms_sales
      table_id: table.zs_observe.amazon_oms
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
      source_role: returns
      table_id: table.zs_observe.amazon_returns
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
      source_role: oms_sales
      table_id: table.zs_observe.walmart_oms
    - account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
      source_role: marketplace_settlement
      table_id: table.zs_observe.walmart_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
      source_role: catalogue_lookup
      table_id: table.zs_observe.walmart_lookup
    - account_data_binding_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
      source_role: oms_sales
      table_id: table.zs_observe.target_sales
    - account_data_binding_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
      source_role: settlement
      table_id: table.zs_observe.target_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
      source_role: returns
      table_id: table.zs_observe.target_returns
    - account_data_binding_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
      source_role: orders
      table_id: table.zs_observe.target_tcin_mapping
    - account_data_binding_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
      source_role: catalogue_lookup
      table_id: table.zs_observe.walmart_lookup
    - account_data_binding_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
      source_role: orders
      table_id: table.zs_observe.target_tcin_mapping
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
      source_role: settlement
      table_id: table.zs_observe.amazon_settlement
    - account_data_binding_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
      source_role: fee_preview
      table_id: table.zs_observe.amazon_fee_preview
```

#### business_flow_binding.volans_epic_llc.oms_runtime_resolution

```yaml
canonical_card:
  canonical_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  card_type: business_flow_binding
  canonical_name: Volans Epic LLC OMS runtime resolution flow
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
    vendor_or_system: Volans Epic LLC
    tenant_slug: null
    marketplace_only: false
    logistics_only: false
    banking_only: false
    payment_gateway_only: false
    client_runtime_layer: true
  semantic:
    aliases:
    - Volans Epic LLC OMS runtime resolution flow
    - Volans Epic LLC OMS flow
    - OMS runtime resolution flow
    colloquial_phrases:
    - Volans Epic LLC OMS resolution flow
    - OMS source routing
    - Volans Epic LLC runtime traversal plan
    business_meaning: Business flow binding for Volans Epic LLC's OMS source resolution. It connects the scope set
      to 1 platform accounts and 2 account-data bindings so questions enter the right client-scoped evidence before
      reusable semantics run.
    business_questions:
    - Which OMS bindings should be traversed for Volans Epic LLC's runtime question?
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
    - tenant_id:tenant.volans_epic_llc
    - group_id:group.volans_epic_llc.g9.gl134
    - runtime_source_family:oms
    embedding_text: Volans Epic LLC OMS runtime resolution flow is Volans Epic LLC's OMS runtime traversal binding.
      It connects the business scope set to account and table bindings so retrieval selects client evidence first
      and then delegates semantics to external canonical packs.
    search_keywords:
    - Volans Epic LLC
    - Volans Epic LLC OMS runtime resolution flow
    - OMS
    - business flow binding
    - runtime traversal
    - source resolution
    exact_match_keys:
    - business_flow_binding.volans_epic_llc.oms_runtime_resolution
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
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    runtime_source_family: oms
    business_flow_binding_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  fields:
    tenant_id: tenant.volans_epic_llc
    group_id: group.volans_epic_llc.g9.gl134
    binding_name: Volans Epic LLC OMS runtime resolution flow
    binding_type: oms_source_resolution
    business_scope_set_id: business_scope_set.volans_epic_llc.oms
    account_data_binding_ids:
    - account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
    - account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
    participating_accounts:
    - platform_account_id: platform_account.volans_epic_llc.shopify_d2c.oms
      account_name: Volans Epic LLC Shopify D2C OMS account
    source_flow_paths:
    - account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
      source_role: oms_sales
      table_id: table.zs_observe.shopify_oms
      domain_id: domain.shopify.d2c_order_capture
    - account_data_binding_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
      source_role: returns
      table_id: table.zs_observe.shopify_returns
      domain_id: domain.shopify.refunds_returns
    deferred_sources:
    - label: Native marketplace OMS feeds
      config: Amazon/Walmart native OMS
      reason: Native marketplace OMS is already represented through marketplace runtime bindings; no separate OMS
        Business KB binding emitted in this pass.
      source_family: oms
    runtime_layer_policy: client_scope_and_account_binding_only_no_canonical_semantics_created_here
```

## 3. Canonical Runtime Edges

### ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN

#### edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_applies_scope_column.column_zs_observe_amazon_fee_preview_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: column.zs_observe.amazon_fee_preview.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_applies_scope_column.column_zs_observe_amazon_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: column.zs_observe.amazon_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_applies_scope_column.column_zs_observe_amazon_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: column.zs_observe.amazon_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_applies_scope_column.column_zs_observe_amazon_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: column.zs_observe.amazon_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_applies_scope_column.column_zs_observe_shopify_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: column.zs_observe.shopify_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_applies_scope_column.column_zs_observe_shopify_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: column.zs_observe.shopify_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_applies_scope_column.column_zs_observe_target_sales_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_applies_scope_column.column_zs_observe_target_sales_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  target_card_id: column.zs_observe.target_sales.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_applies_scope_column.column_zs_observe_target_sales_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_applies_scope_column.column_zs_observe_target_sales_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  target_card_id: column.zs_observe.target_sales.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_applies_scope_column.column_zs_observe_target_tcin_mapping_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  target_card_id: column.zs_observe.target_tcin_mapping.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  target_card_id: column.zs_observe.target_returns.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_applies_scope_column.column_zs_observe_target_returns_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  target_card_id: column.zs_observe.target_returns.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  target_card_id: column.zs_observe.target_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_applies_scope_column.column_zs_observe_target_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  target_card_id: column.zs_observe.target_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: column.zs_observe.walmart_lookup.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: column.zs_observe.walmart_lookup.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: column.zs_observe.walmart_lookup.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_applies_scope_column.column_zs_observe_walmart_lookup_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: column.zs_observe.walmart_lookup.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_applies_scope_column.column_zs_observe_walmart_settlement_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: column.zs_observe.walmart_settlement.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_applies_scope_column.column_zs_observe_walmart_oms_group_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_applies_scope_column.column_zs_observe_walmart_oms_group_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  target_card_id: column.zs_observe.walmart_oms.group_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_applies_scope_column.column_zs_observe_walmart_oms_group_level_id

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_applies_scope_column.column_zs_observe_walmart_oms_group_level_id
  edge_type: ACCOUNT_DATA_BINDING_APPLIES_SCOPE_COLUMN
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  target_card_id: column.zs_observe.walmart_oms.group_level_id
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT

#### edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  target_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_belongs_to_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: ACCOUNT_DATA_BINDING_BELONGS_TO_PLATFORM_ACCOUNT
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### ACCOUNT_DATA_BINDING_BINDS_TO_TABLE

#### edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview.account_data_binding_binds_to_table.table_zs_observe_amazon_fee_preview
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  target_card_id: table.zs_observe.amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms.account_data_binding_binds_to_table.table_zs_observe_amazon_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  target_card_id: table.zs_observe.amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns.account_data_binding_binds_to_table.table_zs_observe_amazon_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  target_card_id: table.zs_observe.amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement.account_data_binding_binds_to_table.table_zs_observe_amazon_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  target_card_id: table.zs_observe.amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms.account_data_binding_binds_to_table.table_zs_observe_shopify_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  target_card_id: table.zs_observe.shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns.account_data_binding_binds_to_table.table_zs_observe_shopify_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  target_card_id: table.zs_observe.shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_binds_to_table.table_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping.account_data_binding_binds_to_table.table_zs_observe_target_tcin_mapping
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  target_card_id: table.zs_observe.target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_binds_to_table.table_zs_observe_target_sales

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales.account_data_binding_binds_to_table.table_zs_observe_target_sales
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  target_card_id: table.zs_observe.target_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_binds_to_table.table_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping.account_data_binding_binds_to_table.table_zs_observe_target_tcin_mapping
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  target_card_id: table.zs_observe.target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_binds_to_table.table_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns.account_data_binding_binds_to_table.table_zs_observe_target_returns
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  target_card_id: table.zs_observe.target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_binds_to_table.table_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement.account_data_binding_binds_to_table.table_zs_observe_target_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  target_card_id: table.zs_observe.target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_binds_to_table.table_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_binds_to_table.table_zs_observe_walmart_lookup
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: table.zs_observe.walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_binds_to_table.table_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup.account_data_binding_binds_to_table.table_zs_observe_walmart_lookup
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  target_card_id: table.zs_observe.walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement.account_data_binding_binds_to_table.table_zs_observe_walmart_settlement
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  target_card_id: table.zs_observe.walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_binds_to_table.table_zs_observe_walmart_oms

```yaml
canonical_edge:
  edge_id: edge.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms.account_data_binding_binds_to_table.table_zs_observe_walmart_oms
  edge_type: ACCOUNT_DATA_BINDING_BINDS_TO_TABLE
  source_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  target_card_id: table.zs_observe.walmart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: BUSINESS_FLOW_BINDING_BELONGS_TO_GROUP
  source_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_FLOW_BINDING_USES_ACCOUNT_DATA_BINDING
  source_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_PLATFORM_ACCOUNT
  source_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  target_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_FLOW_BINDING_USES_SCOPE_SET

#### edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_volans_epic_llc_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_volans_epic_llc_marketplace
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  target_card_id: business_scope_set.volans_epic_llc.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_volans_epic_llc_oms

```yaml
canonical_edge:
  edge_id: edge.business_flow_binding_volans_epic_llc_oms_runtime_resolution.business_flow_binding_uses_scope_set.business_scope_set_volans_epic_llc_oms
  edge_type: BUSINESS_FLOW_BINDING_USES_SCOPE_SET
  source_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  target_card_id: business_scope_set.volans_epic_llc.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_BELONGS_TO_GROUP

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: BUSINESS_SCOPE_SET_BELONGS_TO_GROUP
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_ACCOUNT_DATA_BINDING
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_amazon
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_target_plus
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform.platform_walmart
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform.platform_shopify
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_ACCOUNT
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_amazon_international
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_target_plus_us
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_marketplace.business_scope_set_includes_platform_context.platform_context_walmart_us
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.volans_epic_llc.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.business_scope_set_volans_epic_llc_oms.business_scope_set_includes_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: BUSINESS_SCOPE_SET_INCLUDES_PLATFORM_CONTEXT
  source_card_id: business_scope_set.volans_epic_llc.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_BELONGS_TO_TENANT

#### edge.group_volans_epic_llc_g9_gl134.group_belongs_to_tenant.tenant_volans_epic_llc

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_belongs_to_tenant.tenant_volans_epic_llc
  edge_type: GROUP_BELONGS_TO_TENANT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: tenant.volans_epic_llc
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### GROUP_HAS_BUSINESS_FLOW_BINDING

#### edge.group_volans_epic_llc_g9_gl134.group_has_business_flow_binding.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_business_flow_binding.business_flow_binding_volans_epic_llc_marketplace_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: business_flow_binding.volans_epic_llc.marketplace_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_business_flow_binding.business_flow_binding_volans_epic_llc_oms_runtime_resolution

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_business_flow_binding.business_flow_binding_volans_epic_llc_oms_runtime_resolution
  edge_type: GROUP_HAS_BUSINESS_FLOW_BINDING
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: business_flow_binding.volans_epic_llc.oms_runtime_resolution
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_BUSINESS_SCOPE_SET

#### edge.group_volans_epic_llc_g9_gl134.group_has_business_scope_set.business_scope_set_volans_epic_llc_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_business_scope_set.business_scope_set_volans_epic_llc_marketplace
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: business_scope_set.volans_epic_llc.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_business_scope_set.business_scope_set_volans_epic_llc_oms

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_business_scope_set.business_scope_set_volans_epic_llc_oms
  edge_type: GROUP_HAS_BUSINESS_SCOPE_SET
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: business_scope_set.volans_epic_llc.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

### GROUP_HAS_PLATFORM_ACCOUNT

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_brazil_br_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_canada_ca_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_amazon_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_shopify_d2c_oms
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_target_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_target_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.target_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace

```yaml
canonical_edge:
  edge_id: edge.group_volans_epic_llc_g9_gl134.group_has_platform_account.platform_account_volans_epic_llc_walmart_us_marketplace
  edge_type: GROUP_HAS_PLATFORM_ACCOUNT
  source_card_id: group.volans_epic_llc.g9.gl134
  target_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_BELONGS_TO_GROUP

#### edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_belongs_to_group.group_volans_epic_llc_g9_gl134
  edge_type: PLATFORM_ACCOUNT_BELONGS_TO_GROUP
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING

#### edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_brazil_br_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_brazil_br.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_canada_ca_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_canada_ca.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_fee_preview_zs_observe_amazon_fee_preview
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.fee_preview.zs_observe_amazon_fee_preview
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_oms_sales_zs_observe_amazon_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.oms_sales.zs_observe_amazon_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_returns_zs_observe_amazon_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.returns.zs_observe_amazon_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_amazon_us_settlement_zs_observe_amazon_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.amazon_us.settlement.zs_observe_amazon_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_oms_sales_zs_observe_shopify_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.oms_sales.zs_observe_shopify_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_shopify_d2c_returns_zs_observe_shopify_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  target_card_id: account_data_binding.volans_epic_llc.shopify_d2c.returns.zs_observe_shopify_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_orders_zs_observe_target_tcin_mapping
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_oms_sales_zs_observe_target_sales
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.oms_sales.zs_observe_target_sales
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_orders_zs_observe_target_tcin_mapping
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.orders.zs_observe_target_tcin_mapping
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_returns_zs_observe_target_returns
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.returns.zs_observe_target_returns
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_target_us_settlement_zs_observe_target_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.target_us.settlement.zs_observe_target_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_asin_sku_walmart_lookup_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_asin_sku_walmart_lookup.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_catalogue_lookup_zs_observe_walmart_lookup
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.catalogue_lookup.zs_observe_walmart_lookup
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_marketplace_settlement_zs_observe_walmart_settlement
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.marketplace_settlement.zs_observe_walmart_settlement
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_has_account_data_binding.account_data_binding_volans_epic_llc_walmart_us_oms_sales_zs_observe_walmart_oms
  edge_type: PLATFORM_ACCOUNT_HAS_ACCOUNT_DATA_BINDING
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: account_data_binding.volans_epic_llc.walmart_us.oms_sales.zs_observe_walmart_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_USES_PLATFORM

#### edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_uses_platform.platform_amazon

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_uses_platform.platform_amazon
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: platform.amazon
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_uses_platform.platform_shopify

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_uses_platform.platform_shopify
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  target_card_id: platform.shopify
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_uses_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_uses_platform.platform_target_plus
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_uses_platform.platform_target_plus

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_uses_platform.platform_target_plus
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: platform.target_plus
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_uses_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_uses_platform.platform_walmart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_uses_platform.platform_walmart

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_uses_platform.platform_walmart
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: platform.walmart
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT

#### edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_brazil_br_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.amazon_brazil_br.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_canada_ca_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.amazon_canada_ca.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_fee_preview_amazon_fee_preview_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.amazon_fee_preview_amazon_fee_preview.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_uses_platform_context.platform_context_amazon_international

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_amazon_us_marketplace.platform_account_uses_platform_context.platform_context_amazon_international
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.amazon_us.marketplace
  target_card_id: platform_context.amazon.international
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_shopify_d2c_oms.platform_account_uses_platform_context.platform_context_shopify_in_d2c_oms
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.shopify_d2c.oms
  target_card_id: platform_context.shopify.in.d2c_oms
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_logistics_oms
```

#### edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_tcin_mapping_target_tcin_mapping_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.target_tcin_mapping_target_tcin_mapping.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_target_us_marketplace.platform_account_uses_platform_context.platform_context_target_plus_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.target_us.marketplace
  target_card_id: platform_context.target_plus.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_uses_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_asin_sku_walmart_lookup_marketplace.platform_account_uses_platform_context.platform_context_walmart_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.walmart_asin_sku_walmart_lookup.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

#### edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_uses_platform_context.platform_context_walmart_us

```yaml
canonical_edge:
  edge_id: edge.platform_account_volans_epic_llc_walmart_us_marketplace.platform_account_uses_platform_context.platform_context_walmart_us
  edge_type: PLATFORM_ACCOUNT_USES_PLATFORM_CONTEXT
  source_card_id: platform_account.volans_epic_llc.walmart_us.marketplace
  target_card_id: platform_context.walmart.us
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```

### TENANT_HAS_GROUP

#### edge.tenant_volans_epic_llc.tenant_has_group.group_volans_epic_llc_g9_gl134

```yaml
canonical_edge:
  edge_id: edge.tenant_volans_epic_llc.tenant_has_group.group_volans_epic_llc_g9_gl134
  edge_type: TENANT_HAS_GROUP
  source_card_id: tenant.volans_epic_llc
  target_card_id: group.volans_epic_llc.g9.gl134
  confidence: high
  review_status: accepted
  properties:
    runtime_resolution: marketplace_only
```
