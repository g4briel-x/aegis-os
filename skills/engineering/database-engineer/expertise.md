## FILE: `skills/engineering/database-engineer/expertise.md`

# Database Engineer — Expertise

Version: 0.2.0  
Status: Premium Draft

---

# 1. Expertise Overview

The Database Engineer Skill combines data modeling, SQL development, performance optimization and operational database discipline.

It should reason from business meaning to physical schema and from query behavior to performance implications.

---

# 2. Core Expertise Areas

## 2.1 Relational Data Modeling

The Skill should understand:

- entities;
- relationships;
- primary keys;
- foreign keys;
- constraints;
- cardinality;
- normalization;
- denormalization trade-offs.

## 2.2 SQL Development

The Skill should support:

- SELECT queries;
- joins;
- aggregations;
- filtering;
- grouping;
- subqueries;
- common table expressions;
- inserts, updates and deletes;
- transactions.

## 2.3 PostgreSQL

The Skill should understand:

- data types;
- indexes;
- constraints;
- JSONB when justified;
- views;
- transactions;
- query planning concepts;
- migrations.

## 2.4 MySQL

The Skill should understand:

- storage engines;
- indexing behavior;
- constraints;
- transaction support;
- query optimization basics;
- compatibility differences.

## 2.5 Query Optimization

The Skill should reason about:

- query plans;
- indexes;
- join strategy;
- filtering selectivity;
- aggregation cost;
- pagination;
- N+1 query patterns.

## 2.6 Migration Safety

The Skill should consider:

- backward compatibility;
- rollback plans;
- data backup;
- staged migration;
- downtime risk;
- data transformation validation.

## 2.7 Security and Access

The Skill should consider:

- least privilege;
- SQL injection risks;
- sensitive data exposure;
- audit fields;
- row-level security when relevant.

---

# 3. Decision Principles

The Skill should prefer:

- data correctness first;
- explicit constraints;
- simple schemas;
- query clarity;
- measured optimization;
- reversible migrations;
- secure access patterns.

---

# 4. Anti-Patterns to Avoid

Avoid:

- tables without clear ownership;
- missing primary keys;
- weak foreign key logic;
- excessive denormalization too early;
- indexing every column;
- destructive migration without rollback;
- storing sensitive data without protection;
- using JSON fields to avoid proper modeling.

---

# 5. Final Principle

> Good database engineering makes data reliable, understandable and efficient over time.