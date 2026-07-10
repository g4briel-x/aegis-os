## FILE: `playbooks/engineering/create-api-contract/README.md`

# Create API Contract Playbook

Version: 0.1.0  
Status: Premium Draft  
Domain: Engineering  
Category: API Design

---

# 1. Purpose

The Create API Contract Playbook provides a structured procedure for defining clear, stable and implementation-ready API contracts for SaaS applications.

It helps teams specify endpoints, methods, request bodies, response schemas, errors, authentication, authorization, pagination, filtering, versioning and backward compatibility before implementation.

---

# 2. Trigger

Use this Playbook when:

- a feature requires a new API endpoint;
- frontend and backend teams need a shared contract;
- a PRD or UX flow must be translated into API behavior;
- an existing API needs cleanup or documentation;
- an integration requires predictable data exchange;
- permissions and error responses must be standardized;
- API behavior must be reviewed before implementation.

---

# 3. Scope

This Playbook covers:

- API purpose definition;
- endpoint design;
- request schema;
- response schema;
- error model;
- authentication and authorization;
- pagination and filtering;
- idempotency;
- versioning;
- backward compatibility;
- documentation and handoff.

This Playbook does not replace backend implementation, but it creates the contract that implementation must follow.

---

# 4. Related Skills

```text
engineering.software-architect
engineering.senior-developer
engineering.database-engineer
security.security-engineer
product.business-analyst
design.ux-ui-designer-saas
```

---

# 5. Final Principle

> An API contract is good when product, frontend, backend and security can all predict the same behavior from the same document.
