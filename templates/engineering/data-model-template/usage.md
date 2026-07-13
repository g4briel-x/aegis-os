## FILE: `templates/engineering/data-model-template/usage.md`

# Data Model Template — Usage Guide

Version: 0.1.0  
Status: Draft

---

# 1. Usage Process

Use this sequence:

```text
1. Define model name and business context
2. Identify main entities
3. Define fields and types
4. Define relationships
5. Define tenant and ownership rules
6. Define constraints and indexes
7. Define lifecycle states
8. Define permissions and audit events
9. Define retention and deletion rules
10. Review migration and implementation risks
```

---

# 2. Recommended Review Flow

Review in this order:

```text
Product review
Architecture review
Database review
Security review
Engineering review
QA review if test cases depend on data behavior
```

---

# 3. Writing Rules

A Data Model should:

- use clear entity names;
- define ownership;
- define tenant scope;
- include constraints;
- include indexes when query patterns are known;
- include lifecycle states;
- include audit events for sensitive actions;
- identify migration risks.

---

# 4. Modeling Rule

Weak:

```text
Project has data.
```

Better:

```text
Project belongs to one workspace, has one creator, contains financing readiness fields and can move from draft to submitted to reviewed.
```

---

# 5. Final Principle

> Use the Data Model Template before migrations, APIs and screens depend on unclear structures.
