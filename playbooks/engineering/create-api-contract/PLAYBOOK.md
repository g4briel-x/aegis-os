# FILE: `playbooks/engineering/create-api-contract/PLAYBOOK.md`

# Create API Contract — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for designing and documenting an API contract before implementation.

---

# 2. Trigger

A SaaS feature, integration, workflow or frontend screen requires defined API behavior.

---

# 3. Inputs

Useful inputs include:

- PRD;
- UX flow;
- user story;
- data model;
- permission model;
- frontend requirements;
- integration requirements;
- existing API standards;
- authentication model;
- error model;
- performance constraints.

---

# 4. Outputs

Expected outputs include:

- API contract;
- endpoint list;
- request schema;
- response schema;
- error schema;
- authentication and authorization notes;
- pagination and filtering rules;
- versioning notes;
- compatibility notes;
- implementation handoff.

---

# 5. Execution Summary

```text
1. Define API purpose and consumers
2. Identify resources and actions
3. Design endpoints and methods
4. Define request schemas
5. Define response schemas
6. Define error model
7. Define authentication and authorization
8. Define pagination, filtering and sorting
9. Review versioning and compatibility
10. Produce implementation-ready contract
```

---

# 6. Completion Criteria

The Playbook is complete when:

- endpoint behavior is clear;
- request and response schemas are documented;
- error cases are defined;
- permissions are explicit;
- pagination and filtering are defined if needed;
- backward compatibility is reviewed;
- implementation handoff is ready.

---

# 7. Escalation or Fallback

Escalate when:

- resource ownership is unclear;
- permissions are ambiguous;
- sensitive data is exposed;
- API changes may break clients;
- data model is not ready;
- performance requirements are high;
- public integration contract requires external review.

---

# 8. Final Principle

> API contract design should remove ambiguity before implementation creates inconsistent behavior.

---