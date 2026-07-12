## FILE: `patterns/engineering/database-migration-safety/context.md`

# Database Migration Safety — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS applications where production data matters.

Typical contexts:

```text
first production release
customer data migration
tenant schema evolution
billing model change
permission model change
large table indexing
data correction
release hardening
```

---

# 2. Product Context

Use this Pattern when database changes affect:

- signup;
- login;
- billing;
- project creation;
- document upload;
- submission;
- review;
- permissions;
- reporting;
- customer exports.

---

# 3. Technical Context

The Pattern applies to:

```text
PostgreSQL
MySQL
SQL Server
managed relational databases
ORM migration systems
manual SQL migrations
background backfill jobs
multi-tenant schemas
```

---

# 4. Operational Context

Operators need to know:

- how long migration should take;
- whether it locks tables;
- how to verify success;
- how to stop or recover;
- whether customer workflows are affected;
- whether backup is required.

---

# 5. Security Context

Migration safety must protect:

```text
tenant boundaries
permission records
audit logs
private files metadata
billing records
personal information
```

Any migration touching these areas needs extra review.

---

# 6. Warning Signs

A migration is unsafe when:

- it drops data immediately;
- it assumes rollback is simple;
- it has no validation queries;
- it updates all rows at once on a large table;
- it changes tenant data without tenant filters;
- it adds constraints before cleaning data;
- it is not compatible with current application code;
- it has no owner during deployment.

---

# 7. Final Principle

> Migration context should include data value, system uptime, customer impact and recovery options.
