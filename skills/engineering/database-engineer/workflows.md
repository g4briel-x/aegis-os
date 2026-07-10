## FILE: `skills/engineering/database-engineer/workflows.md`

# Database Engineer — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. Schema Design Workflow

Use this workflow when designing a new database structure.

```text
1. Understand the business domain
2. Identify entities
3. Identify relationships
4. Define primary keys
5. Define foreign keys
6. Define constraints
7. Define indexes based on query patterns
8. Validate integrity and migration readiness
```

---

# 2. SQL Query Workflow

Use this workflow when writing a query.

```text
1. Understand the expected result
2. Identify required tables
3. Define joins and filters
4. Write the query
5. Review syntax for target engine
6. Review correctness
7. Consider performance
8. Provide usage notes
```

---

# 3. Query Optimization Workflow

Use this workflow when improving slow SQL.

```text
1. Understand the slow query
2. Identify database engine
3. Identify table sizes and indexes if available
4. Analyze filtering, joins and aggregations
5. Recommend query changes
6. Recommend indexes where justified
7. Explain trade-offs
8. Provide verification steps
```

---

# 4. Migration Workflow

Use this workflow for schema changes.

```text
1. Understand the change
2. Identify affected tables and data
3. Assess backward compatibility
4. Define migration SQL
5. Define backup requirement
6. Define rollback plan
7. Define validation queries
8. Document deployment risk
```

---

# 5. Data Integrity Review Workflow

Use this workflow when reviewing a schema.

```text
1. Review entities and relationships
2. Review primary keys
3. Review foreign keys
4. Review uniqueness constraints
5. Review nullability
6. Review cascade behavior
7. Review audit fields
8. Identify integrity risks
```

---

# 6. 4-Pass Database Validation Workflow

Every database output must be reviewed using this workflow:

```text
Pass 1 — Syntax and compatibility review
Pass 2 — Data model and integrity review
Pass 3 — Performance, indexing and scalability review
Pass 4 — Safety, migration and operational readiness review
```

---

# 7. Final Principle

> Database work is complete only when correctness, performance and safety have all been reviewed.