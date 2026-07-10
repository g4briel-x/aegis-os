## FILE: `playbooks/security/design-auth-rbac/PLAYBOOK.md`

# Design Auth RBAC — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for designing authentication and role-based access control for SaaS systems.

---

# 2. Trigger

A SaaS application, feature, API or workflow requires defined user identity, roles, permissions or tenant boundaries.

---

# 3. Inputs

Useful inputs include:

- product requirements;
- user roles;
- user journeys;
- data model;
- tenant model;
- API contract;
- sensitive data list;
- admin workflows;
- compliance requirements;
- audit requirements;
- existing auth provider;
- security constraints.

---

# 4. Outputs

Expected outputs include:

- authentication model;
- role catalog;
- permission matrix;
- resource ownership model;
- tenant isolation rules;
- API authorization rules;
- audit event list;
- permission test matrix;
- security review notes;
- open security questions.

---

# 5. Execution Summary

```text
1. Define identity and authentication model
2. Identify protected resources
3. Define roles and role hierarchy
4. Define permissions and actions
5. Map roles to permissions
6. Define ownership and tenant boundaries
7. Define API authorization rules
8. Define audit and logging needs
9. Define permission tests
10. Produce security handoff
```

---

# 6. Completion Criteria

The Playbook is complete when:

- user identity model is clear;
- protected resources are listed;
- roles are defined;
- permissions are explicit;
- tenant boundaries are documented;
- object-level authorization rules are defined;
- API enforcement points are known;
- audit and permission tests are documented.

---

# 7. Escalation or Fallback

Escalate when:

- permissions affect sensitive data;
- tenant isolation is unclear;
- admin privileges are broad;
- external users or partners need access;
- public endpoints expose data;
- compliance or contractual requirements apply;
- authorization cannot be tested clearly.

---

# 8. Final Principle

> RBAC design should prevent accidental access by making allowed behavior explicit and denied behavior testable.
