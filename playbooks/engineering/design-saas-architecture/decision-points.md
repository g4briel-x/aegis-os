## FILE: `playbooks/engineering/design-saas-architecture/decision-points.md`

# Design SaaS Architecture — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Monolith or Distributed Services?

```yaml
decision_point:
  question: Should the SaaS begin as a modular monolith or distributed services?
  options:
    - modular_monolith
    - distributed_services
    - hybrid
  criteria:
    - team size
    - product maturity
    - deployment complexity
    - domain boundaries
    - scalability needs
  recommended_action:
    modular_monolith: use for most MVPs and early SaaS products.
    distributed_services: use only when boundaries and scaling needs are strong.
    hybrid: isolate only the components that clearly require separation.
  fallback: start modular and define extraction boundaries.
```

---

# 2. Decision Point — Is Multi-Tenancy Required?

```yaml
decision_point:
  question: Does the product need multi-tenant data isolation?
  options:
    - yes
    - no
    - later
  criteria:
    - multiple customer workspaces
    - organization accounts
    - role-based workspace access
    - customer data isolation
  recommended_action:
    yes: define tenant model from the start.
    no: keep model simple.
    later: avoid choices that block tenant scoping later.
  fallback: add tenant_id or workspace boundary early if B2B SaaS is likely.
```

---

# 3. Decision Point — Is External Integration Critical?

```yaml
decision_point:
  question: Is a third-party integration required for the MVP to deliver value?
  options:
    - critical
    - useful_later
    - not_required
  criteria:
    - core workflow dependency
    - payment dependency
    - data import dependency
    - user adoption dependency
  recommended_action:
    critical: design integration boundary and failure handling.
    useful_later: defer to post-MVP.
    not_required: exclude from architecture scope.
  fallback: use manual or mock workflow for MVP validation.
```

---

# 4. Decision Point — Is Security Review Required?

```yaml
decision_point:
  question: Does the architecture handle sensitive data, identity, payments, files or permissions?
  options:
    - yes
    - no
    - unclear
  criteria:
    - personal data
    - payment data
    - file uploads
    - role permissions
    - public API
    - audit requirements
  recommended_action:
    yes: require security architecture review.
    no: document low security sensitivity.
    unclear: treat as security-sensitive until reviewed.
  fallback: involve Security Engineer Skill.
```

---

# 5. Decision Point — Is the Architecture MVP-Appropriate?

```yaml
decision_point:
  question: Is the architecture simple enough for MVP delivery but safe enough for real use?
  options:
    - yes
    - over_engineered
    - under_engineered
  criteria:
    - build time
    - team capacity
    - operational complexity
    - risk exposure
    - future adaptability
  recommended_action:
    yes: proceed to implementation planning.
    over_engineered: reduce components and defer complexity.
    under_engineered: strengthen security, data and operational foundations.
  fallback: review architecture goals and constraints.
```

---

# 6. Final Principle

> Architecture decision points protect the team from both premature complexity and unsafe shortcuts.