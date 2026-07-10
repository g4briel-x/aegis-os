## FILE: `playbooks/engineering/design-saas-architecture/PLAYBOOK.md`

# Design SaaS Architecture — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured process for designing a SaaS technical architecture from product requirements.

---

# 2. Trigger

A SaaS product, MVP, platform or feature needs an implementation-ready technical architecture.

---

# 3. Inputs

Useful inputs include:

- product concept;
- PRD;
- MVP scope;
- user roles;
- UX flow;
- functional requirements;
- non-functional requirements;
- data requirements;
- security constraints;
- integration needs;
- expected scale;
- budget and team constraints.

---

# 4. Outputs

Expected outputs include:

- architecture summary;
- system context;
- component map;
- data model outline;
- API model;
- authentication and authorization model;
- infrastructure plan;
- security notes;
- observability plan;
- architectural risks;
- implementation sequence.

---

# 5. Execution Summary

```text
1. Clarify product and technical context
2. Define architecture goals and constraints
3. Identify users, roles and access boundaries
4. Define system components
5. Define data model and storage needs
6. Define API and integration model
7. Define authentication and authorization model
8. Define infrastructure and deployment model
9. Review security, observability and scalability
10. Produce implementation-ready architecture plan
```

---

# 6. Completion Criteria

The Playbook is complete when:

- architecture scope is clear;
- major components are identified;
- data and API models are outlined;
- access control is defined;
- infrastructure direction is documented;
- major risks are visible;
- implementation sequence is clear;
- open technical questions are recorded.

---

# 7. Escalation or Fallback

Escalate when:

- requirements are unstable;
- data model is unclear;
- security or compliance risk is high;
- infrastructure cost is uncertain;
- expected scale is unknown;
- critical integrations are not validated;
- architecture trade-offs require leadership decision.

---

# 8. Final Principle

> Architecture should make technical decisions explicit before hidden assumptions become expensive rewrites.