# Cognee KB Design

**Status:** Draft - V3.0
**Phase:** 1 — KB Schema & Card Design   
**Scope:** Tenant-aware knowledge base for GraphRAG-driven SQL generation

## **1\. Overview**

This document specifies the Phase 1 design of a structured knowledge base (KB) intended for ingestion into Cognee. The KB underpins a GraphRAG pipeline that converts natural-language business questions into safe, deterministic SQL against ZenStatement's warehouse.

A critical structural discovery drives this design: **each tenant can have multiple groups, and each group can have multiple marketplace accounts.** Marketplace accounts map to data through scoping fields such as `group_level_id`. For example, on Amazon:

* `group_level_id = 22` → one Amazon India seller account  
* `group_level_id = 26` → another Amazon India seller account  
* `group_level_id = 123` → US / France / Spain context

`group_level_id` is stored as an **integer** and must not be compared as a string. The KB must encode this and similar constraints so that downstream SQL generation respects them.

---

## **2\. Goals**

The KB must support:

1. Tenant-aware context retrieval  
2. Platform, marketplace, and account resolution  
3. Table and column understanding  
4. Metric and formula retrieval  
5. SQL generation  
6. SQL validation  
7. Deterministic and compositional retrieval (i.e., composing new metrics from primitives when a pre-defined metric does not exist)

---

## **3\. Design Principles**

* **Business hierarchy tells us *whose* data to query.**  
* **Data cards tell us *where* the data lives.**  
* **Metric cards tell us *what* to calculate.**  
* **Rule and validation cards tell us *how* to avoid bad SQL.**  
* **Every card must have a stable `canonical_id`.** Names can change; IDs must not.

---

## **4\. Hierarchy**

Tenant  
└── Group  
    └── Platform  
        └── Marketplace  
            └── Marketplace Account  
                ├── Table  
                │   ├── Column  
                │   ├── Value Profile  
                │   ├── Relationship  
                │   ├── Rule  
                │   └── Query Pattern  
                │  
                ├── Metric  
                │   └── Metric Implementation  
                │  
                ├── Domain  
                ├── Business Process  
                ├── Formula Template  
                └── Validation Test

---

## **5\. Card Type Catalog**

The KB uses **17 card types**, grouped into four families.

| \# | Card Type | Family |
| ----- | ----- | ----- |
| 1 | Tenant | Business Hierarchy |
| 2 | Group | Business Hierarchy |
| 3 | Platform | Business Hierarchy |
| 4 | Marketplace | Business Hierarchy |
| 5 | Marketplace Account | Business Hierarchy |
| 6 | Table | Data Structure |
| 7 | Column | Data Structure |
| 8 | Relationship | Data Structure |
| 9 | Value Profile | Data Structure |
| 10 | Metric | Analytics & SQL |
| 11 | Metric Implementation | Analytics & SQL |
| 12 | Rule | Analytics & SQL |
| 13 | Query Pattern | Analytics & SQL |
| 14 | Domain | Semantic Reasoning |
| 15 | Business Process | Semantic Reasoning |
| 16 | Formula Template | Semantic Reasoning |
| 17 | Validation Test | Semantic Reasoning |

---
