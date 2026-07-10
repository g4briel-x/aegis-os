## FILE: `skills/engineering/database-engineer/examples/examples.md`

# Database Engineer — Examples

Version: 0.2.0  
Status: Premium Draft

---

# 1. Example — SaaS User and Subscription Schema

## User Request

Design a PostgreSQL schema for a SaaS with users, organizations, roles and subscriptions.

## Expected Skill Behavior

The Skill should:

- identify tenant model;
- define organizations and users;
- define membership table;
- define roles;
- define subscriptions;
- use constraints;
- propose indexes;
- mention security and audit fields.

## Expected Output Structure

```text
Assumptions
Data model
SQL schema
Indexes
Integrity notes
Security notes
Validation notes
```

---

# 2. Example — SQL Report Query

## User Request

Write a SQL query to show monthly revenue by customer for the last 12 months.

## Expected Skill Behavior

The Skill should:

- state assumptions about tables;
- use grouping by month and customer;
- filter the date range;
- consider indexes on date and customer fields.

---

# 3. Example — Slow Query Optimization

## User Request

This query is slow: SELECT * FROM orders WHERE customer_id = 42 ORDER BY created_at DESC;

## Expected Skill Behavior

The Skill should:

- recommend selecting needed columns;
- suggest a composite index on customer_id and created_at;
- explain why the index helps;
- mention verifying with query plan tools.

---

# 4. Example — Safe Migration

## User Request

Add a NOT NULL email column to an existing users table.

## Expected Skill Behavior

The Skill should:

- warn that adding NOT NULL directly may fail on existing rows;
- propose staged migration;
- backfill values;
- add constraint after validation;
- provide rollback notes.

---

# 5. Example — Airtable Data Model

## User Request

Create an Airtable structure for tracking clients, projects, invoices and payments.

## Expected Skill Behavior

The Skill should:

- define tables;
- define relationships;
- explain linked records;
- warn about Airtable limitations;
- keep the structure simple.

---

# 6. Final Principle

> Examples prove that the Skill can protect data quality across design, queries and operations.
