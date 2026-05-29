# Grounded Intent Skill

Refine raw intent using retrieved evidence. Do not choose final SQL tables and do not produce SQL.

Question:
{{query}}

{{scope}}

Raw Intent JSON:
{{raw_intent_json}}

Retrieved context:
{{context}}

Resolve:
- final question family: metric, report_generation, business_process, workflow, source_mapping, metadata_inventory, reconciliation, logistics, or mixed
- answer mode: physical_sql, metadata_inventory, mixed, or partial
- requested grain
- metric/status logic
- dimensions
- filters
- tenant/account/platform scope
- whether this is single-source or multi-source
- whether candidate source enumeration is mandatory
- maximum useful physical table count, normally 1-3

Rules:
- Preserve raw intent unless retrieved evidence clearly contradicts it.
- Set `answer_mode=metadata_inventory` when the question is about source topology, platform/account bindings, OMS-marketplace mappings, supported marketplaces, workflow dependencies, or other catalog facts.
- Set `answer_mode=physical_sql` when the question needs runtime metrics, dimensions, filters, joins, statuses, or report tables.
- Set `answer_mode=mixed` when metadata is required to identify the right physical SQL path.
- Set `answer_mode=partial` when retrieved context lacks the required physical table, column, join key, filter, or metadata evidence.
- Set `must_enumerate_sources=true` for channel, marketplace, settlement, reconciliation, risk, bottleneck, dependency, concentration, courier mapping, OMS dependency, or marketplace-wide questions.
- Do not select final source tables in this stage; source selection belongs to the source resolver.

Return a top-level JSON object with exactly one key named `content`.
The `content` value must be a string containing a JSON-serialized object with keys:
`question_family`, `answer_mode`, `grain`, `metric_or_status_logic`, `dimensions`, `filters`, `scope`, `source_mode`, `must_enumerate_sources`, `table_limit`, `reason`.

Example wrapper:
{"content":"{\"question_family\":\"metric\",\"answer_mode\":\"physical_sql\",\"grain\":\"channel\",\"metric_or_status_logic\":\"count orders\",\"dimensions\":[\"sales_channel\"],\"filters\":[],\"scope\":{},\"source_mode\":\"single_source\",\"must_enumerate_sources\":false,\"table_limit\":1,\"reason\":\"...\"}"}
