## FILE: `playbooks/security/design-auth-rbac/decision-points.md`

# Design Auth RBAC — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is Role-Based Access Enough?

```yaml
decision_point:
  question: Can access be controlled by roles alone?
  options:
    - yes
    - no
    - partially
  criteria:
    - simple role model
    - no object ownership complexity
    - no tenant-specific exceptions
    - no per-resource sharing
  recommended_action:
    yes: use RBAC.
    no: add object-level or attribute-based checks.
    partially: combine roles with ownership and tenant checks.
  fallback: use least privilege and explicit resource checks.
```

---

# 2. Decision Point — Is Tenant Isolation Required?

```yaml
decision_point:
  question: Must data be isolated by tenant, organization or workspace?
  options:
    - yes
    - no
    - unclear
  criteria:
    - B2B SaaS
    - organization accounts
    - customer-owned records
    - workspace membership
    - sensitive business data
  recommended_action:
    yes: enforce tenant boundary on every protected resource.
    no: document global resource behavior.
    unclear: treat data as tenant-scoped until confirmed.
  fallback: involve Security Engineer and Software Architect Skills.
```

---

# 3. Decision Point — Should This Role Be Admin?

```yaml
decision_point:
  question: Does this role require administrative privilege?
  options:
    - yes
    - no
    - limited_admin
  criteria:
    - manages users
    - manages billing
    - manages settings
    - can access sensitive data
    - can delete records
  recommended_action:
    yes: restrict assignment and audit all critical actions.
    no: keep role least-privilege.
    limited_admin: define exact admin capabilities.
  fallback: avoid broad admin roles without explicit need.
```

---

# 4. Decision Point — Is Support Access Needed?

```yaml
decision_point:
  question: Should internal support or operations users access customer data?
  options:
    - yes
    - no
    - exceptional
  criteria:
    - support workflow
    - privacy risk
    - audit requirement
    - customer trust
    - compliance constraint
  recommended_action:
    yes: require scoped, audited and time-bound access.
    no: block support access to customer data.
    exceptional: require approval and audit trail.
  fallback: deny by default.
```

---

# 5. Decision Point — Are Permission Tests Sufficient?

```yaml
decision_point:
  question: Do tests prove allowed and denied access paths?
  options:
    - yes
    - no
    - partially
  criteria:
    - each role tested
    - denied access tested
    - cross-tenant tests included
    - unauthenticated access tested
    - admin-only paths tested
  recommended_action:
    yes: approve RBAC validation.
    no: add missing permission tests.
    partially: block high-risk permissions until tested.
  fallback: do not ship sensitive permissions without tests.
```

---

# 6. Final Principle

> Authorization decisions should default to least privilege, explicit ownership and testable denial.
