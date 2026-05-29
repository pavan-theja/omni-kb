# Mensa Business Hierarchy + Runtime Binding Cards v0.1

Cards: 117  
Edges: 408  
Status: draft_for_review

## Identity cards

### tenant.mensa_brand_technologies
```json
{
  "card_type": "tenant",
  "canonical_id": "tenant.mensa_brand_technologies",
  "tenant_name": "Mensa Brand Technologies Private Limited",
  "tenant_code": "MENSA",
  "description": "Large-scale multi-channel marketplace seller using ZenStatement for marketplace, D2C, OMS/WMS, logistics, payment-gateway, settlement, reconciliation, diagnostics, and money-flow reasoning.",
  "active": true,
  "status": "active",
  "source_documents": [
    "Mensa Brand Technologies Private Limited.docx"
  ]
}
```

### group.mensa_brands
```json
{
  "card_type": "group",
  "canonical_id": "group.mensa_brands",
  "tenant_id": "tenant.mensa_brand_technologies",
  "group_name": "Mensa Brands",
  "group_code": "MENSA_BRANDS",
  "group_type": "operational_unit",
  "business_meaning": "Mensa Brands operating group for the Mensa Brand Technologies Private Limited multi-channel commerce business. Source client scope uses GROUP ID 8 and GROUP LEVEL ID 22; table filtering is represented through Account Data Binding cards, not as a universal Group property.",
  "country_or_region": "India primary; international sales contexts include US, CA, UK, and MX where separately bound.",
  "default_currency": "INR",
  "active": true,
  "status": "active",
  "source_documents": [
    "Mensa Brand Technologies Private Limited.docx",
    "Cognee KB Design v4.md"
  ]
}
```

## Semantic mapping note — Myntra

```json
{
  "platform_account_id": "platform_account.mensa.myntra_in.primary",
  "client_config_text": "OMS (JIT + PPMP), Fwd/Rev Settlement, Returns (JIT + PPMP), Non-order Settlement, GSTR, VHS/VFS expenses, Seller reports, Transactions",
  "canonical_mapped_now": [
    "table.zs_observe.myntra_oms",
    "table.zs_observe.myntra_settlement",
    "table.zs_observe.myntra_reverse",
    "table.zs_observe.myntra_non_order_settlement",
    "table.zs_observe.myntra_oms_settlement"
  ],
  "future_platform_context_gaps": [
    "Myntra GSTR",
    "Myntra VHS/VFS expenses",
    "Myntra seller reports",
    "Myntra transactions"
  ],
  "mapping_rule": "Map client-described artifacts to existing canonical semantic coverage only. Do not invent table cards for missing client artifacts; add them later to platform context and bind then."
}
```

## Review items

- **low** — `tenant.mensa_brand_technologies`: Confirm preferred tenant_code; MENSA is inferred from company name.

- **low** — `group.mensa_brands`: Confirm whether group_type should remain operational_unit or be recast as business_unit/legal_entity. Do not move group_level_id=22 onto Group card.

- **medium** — `platform_account.*`: Exact seller IDs, merchant IDs, store IDs, and account identifiers are not in the client reference. Platform accounts are present but most account identifiers are null.

- **high** — `bank platform account`: No Mensa bank account or bank-statement table binding was provided. Marketplace-to-bank, PG-to-bank, and logistics-COD-to-bank BFBs remain draft.

- **medium** — `myntra gaps`: GSTR, VHS/VFS expenses, seller reports, and transactions mentioned in the client reference are intentionally not mapped until canonical platform-context/table cards exist.

- **medium** — `shadowfax/smartr/shipturtle/easebuzz`: Configured in Mensa client reference, but native canonical table/context coverage was not found in the current package; bindings are pending.

- **medium** — `some prior uploads expired`: The file tool reported that some earlier uploaded files had expired. Re-upload any missing source docs before final end-to-end validator lock.


Full cards and edges are in the JSON artifact.
