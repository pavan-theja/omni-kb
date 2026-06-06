# Query 001

Query: `Compare Amazon sales and returns`

## Outcome

- status: `best_effort`
- completion_policy: `best_effort`
- handoff_status: `present`
- total_latency_seconds: `285.741`
- global_step_count: `14`
- usable_branch_count: `1`
- incomplete_branch_count: `5`

## Evidence

- runtime_bindings: `account_data_binding.mensa_brand_technologies_private_limited.amazon_india.oms_sales.zs_observe_amazon_oms`
- tables: `table.zs_observe.amazon_oms`
- query_patterns: `query_pattern.amazon.gst_breakdown, query_pattern.amazon.return_margin_impact, query_pattern.amazon.worst_return_rate_skus`
- metric_implementations: `none`

## Health

- llm_call_count: `16`
- cognee_recall_count: `16`
- contract_repair_count: `1`
- contract_rejection_count: `6`
- invalid_contract_executed_count: `0`
- acceptance_failures: `none`

## Blocked Reasons

- `runtime_contract_missing_domain_family`
- `runtime_contract_missing_tenant_id`
- `runtime_contract_missing_group_id`
- `contract_missing_template_required_nodeset_key:domain_family`
- `contract_missing_template_required_nodeset_key:tenant_id`
- `contract_missing_template_required_nodeset_key:group_id`
- `contract_missing_template_required_nodeset_key:platform_account_id`
- `contract_card_type_does_not_match_template:metric_implementation`

## Warnings

```json
[
  {
    "warning": "branch_incomplete",
    "branch_id": "branch.1d553221027e",
    "status": "partial",
    "scope": {
      "tenant_id": "tenant.mensa_brand_technologies_private_limited",
      "group_id": "group.mensa_brand_technologies_private_limited.g8.gl22",
      "platform_id": "platform.amazon",
      "platform_context_id": "platform_context.amazon.in",
      "platform_account_id": "platform_account.mensa_brand_technologies_private_limited.amazon_india.marketplace"
    },
    "missing_evidence": [
      "runtime_binding",
      "table_frame",
      "query_pattern_or_metric_implementation"
    ],
    "branch_warnings": [],
    "blocked_reasons": [
      "runtime_contract_missing_domain_family",
      "runtime_contract_missing_tenant_id",
      "runtime_contract_missing_group_id",
      "contract_missing_template_required_nodeset_key:domain_family",
      "contract_missing_template_required_nodeset_key:tenant_id",
      "contract_missing_template_required_nodeset_key:group_id",
      "contract_missing_template_required_nodeset_key:platform_account_id"
    ]
  },
  {
    "warning": "branch_incomplete",
    "branch_id": "branch.a8f02f4f4fda",
    "status": "partial",
    "scope": {
      "tenant_id": "tenant.mensa_brand_technologies_private_limited",
      "group_id": "group.mensa_brand_technologies_private_limited.g8.gl22",
      "platform_id": "platform.amazon",
      "platform_context_id": "platform_context.amazon.international",
      "platform_account_id": "platform_account.mensa_brand_technologies_private_limited.amazon_us_ca_uk_mx.marketplace"
    },
    "missing_evidence": [
      "runtime_binding",
      "table_frame",
      "query_pattern_or_metric_implementation"
    ],
    "branch_warnings": [
      "contract_returned_no_cards"
    ],
    "blocked_reasons": []
  },
  {
    "warning": "branch_incomplete",
    "branch_id": "branch.47e71e0d891b",
    "status": "partial",
    "scope": {
      "tenant_id": "tenant.mensa_brand_technologies_private_limited",
      "group_id": "group.mensa_brand_technologies_private_limited.g8.gl22",
      "platform_id": "platform.amazon",
      "platform_account_id": "platform_account.mensa_brand_technologies_private_limited.amazon_india.marketplace",
      "platform_context_id": "platform_context.amazon.in",
      "account_data_binding_id": "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.disbursement.zs_observe_amazon_disbursment",
      "source_role": "disbursement",
      "table_id": "table.zs_observe.amazon_disbursment"
    },
    "missing_evidence": [
      "table_frame",
      "query_pattern_or_metric_implementation"
    ],
    "branch_warnings": [],
    "blocked_reasons": []
  },
  {
    "warning": "branch_incomplete",
    "branch_id": "branch.dff5a0379e2a",
    "status": "partial",
    "scope": {
      "tenant_id": "tenant.mensa_brand_technologies_private_limited",
      "group_id": "group.mensa_brand_technologies_private_limited.g8.gl22",
      "platform_id": "platform.amazon",
      "platform_account_id": "platform_account.mensa_brand_technologies_private_limited.amazon_india.marketplace",
      "platform_context_id": "platform_context.amazon.in",
      "account_data_binding_id": "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.returns.zs_observe_amazon_returns",
      "source_role": "returns",
      "table_id": "table.zs_observe.amazon_returns"
    },
    "missing_evidence": [
      "query_pattern_or_metric_implementation"
    ],
    "branch_warnings": [
      "contract_returned_no_cards"
    ],
    "blocked_reasons": []
  },
  {
    "warning": "branch_incomplete",
    "branch_id": "branch.7cf4fd2afe1b",
    "status": "partial",
    "scope": {
      "tenant_id": "tenant.mensa_brand_technologies_private_limited",
      "group_id": "group.mensa_brand_technologies_private_limited.g8.gl22",
      "platform_id": "platform.amazon",
      "platform_account_id": "platform_account.mensa_brand_technologies_private_limited.amazon_india.marketplace",
      "platform_context_id": "platform_context.amazon.in",
      "account_data_binding_id": "account_data_binding.mensa_brand_technologies_private_limited.amazon_india.settlement.zs_observe_amazon_settlement",
      "source_role": "settlement",
      "table_id": "table.zs_observe.amazon_settlement"
    },
    "missing_evidence": [
      "table_frame",
      "query_pattern_or_metric_implementation"
    ],
    "branch_warnings": [],
    "blocked_reasons": []
  }
]
```
