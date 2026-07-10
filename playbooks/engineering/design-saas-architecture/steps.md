## FILE: `playbooks/engineering/design-saas-architecture/steps.md`

# Design SaaS Architecture — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Clarify Product and Technical Context

Summarize the SaaS product and the architecture problem.

Capture:

- product purpose;
- target users;
- MVP scope;
- business constraints;
- delivery timeline;
- team capacity;
- technical assumptions.

Output:

```text
Architecture context summary
```

---

# 2. Step 2 — Define Architecture Goals

Define what the architecture must optimize for.

Possible goals:

- speed of MVP delivery;
- maintainability;
- scalability;
- security;
- low cost;
- extensibility;
- integration readiness;
- operational simplicity.

Output:

```text
Architecture goal list
```

---

# 3. Step 3 — Identify Users, Roles and Boundaries

Define who uses the system and what boundaries exist.

Review:

- user roles;
- admin roles;
- tenant boundaries;
- internal operators;
- public users;
- external partners;
- service accounts.

Output:

```text
Role and boundary model
```

---

# 4. Step 4 — Define System Components

Break the system into major components.

Typical components:

- frontend application;
- backend API;
- database;
- authentication service;
- file storage;
- notification service;
- billing service;
- admin panel;
- background jobs;
- analytics or reporting.

Output:

```text
Component map
```

---

# 5. Step 5 — Define Data Model Outline

Identify core entities and relationships.

Capture:

- main entities;
- ownership model;
- relationships;
- tenant scoping;
- sensitive fields;
- audit needs;
- lifecycle states.

Output:

```text
Data model outline
```

---

# 6. Step 6 — Define API Model

Define how the frontend, backend and integrations communicate.

Capture:

- API style;
- key endpoints;
- request and response expectations;
- authorization requirements;
- validation needs;
- error handling approach;
- versioning needs.

Output:

```text
API model summary
```

---

# 7. Step 7 — Define Authentication and Authorization

Define identity and access control.

Capture:

- authentication method;
- user session or token model;
- roles;
- permissions;
- tenant access;
- admin controls;
- audit requirements.

Output:

```text
Auth model
```

---

# 8. Step 8 — Define Infrastructure and Deployment Model

Define where and how the system runs.

Capture:

- hosting platform;
- environments;
- deployment pipeline;
- configuration management;
- secret management;
- storage;
- backups;
- monitoring.

Output:

```text
Infrastructure plan
```

---

# 9. Step 9 — Review Security, Observability and Scalability

Validate architecture quality.

Review:

- OWASP risks;
- data protection;
- secrets;
- logging;
- metrics;
- tracing;
- alerting;
- rate limiting;
- scaling bottlenecks;
- failure modes.

Output:

```text
Architecture quality review
```

---

# 10. Step 10 — Produce Implementation Sequence

Turn architecture into execution order.

Recommended phases:

```text
Phase 1 — Foundation
Phase 2 — Core domain and data model
Phase 3 — Core API and auth
Phase 4 — UI integration
Phase 5 — security, observability and release readiness
```

Output:

```text
Implementation sequence
```

---

# 11. Final Principle

> Architecture steps should convert product ambiguity into technical structure and execution order.
