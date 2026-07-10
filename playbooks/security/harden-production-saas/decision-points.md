## FILE: `playbooks/security/harden-production-saas/decision-points.md`

# Harden Production SaaS — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is the System Production-Ready?

```yaml
decision_point:
  question: Are critical security controls verified enough for production use?
  options:
    - yes
    - no
    - ready_with_risks
  criteria:
    - access controls verified
    - tenant isolation verified
    - secrets protected
    - monitoring available
    - rollback available
    - blockers resolved
  recommended_action:
    yes: approve readiness with monitoring.
    no: block launch or release.
    ready_with_risks: document accepted risks and owners.
  fallback: block production launch for unresolved critical risks.
```

---

# 2. Decision Point — Is Tenant Isolation Verified?

```yaml
decision_point:
  question: Has cross-tenant access been tested and prevented?
  options:
    - yes
    - no
    - partially
  criteria:
    - tenant-scoped queries
    - object-level tests
    - API authorization
    - file access control
    - admin support access
  recommended_action:
    yes: record evidence.
    no: mark as launch blocker.
    partially: require targeted tests before launch.
  fallback: treat unverified tenant isolation as high severity.
```

---

# 3. Decision Point — Are Secrets Properly Protected?

```yaml
decision_point:
  question: Are production secrets stored, scoped and rotated safely?
  options:
    - yes
    - no
    - unclear
  criteria:
    - not committed to repository
    - not exposed in logs
    - scoped to environment
    - least privilege
    - rotation plan
  recommended_action:
    yes: continue.
    no: remediate before launch.
    unclear: perform secret inventory review.
  fallback: rotate any secret suspected of exposure.
```

---

# 4. Decision Point — Is Monitoring Actionable?

```yaml
decision_point:
  question: Will the team know quickly if production security or reliability degrades?
  options:
    - yes
    - no
    - partially
  criteria:
    - critical alerts
    - owner routing
    - audit logs
    - error monitoring
    - suspicious activity detection
  recommended_action:
    yes: record monitoring readiness.
    no: add monitoring before launch.
    partially: add alerts for critical gaps.
  fallback: do not launch critical workflows without basic monitoring.
```

---

# 5. Decision Point — Is Recovery Possible?

```yaml
decision_point:
  question: Can the team recover from a failed release, data issue or security event?
  options:
    - yes
    - no
    - unclear
  criteria:
    - backups exist
    - restore process known
    - rollback available
    - incident owner defined
    - runbooks available
  recommended_action:
    yes: record recovery readiness.
    no: block production readiness.
    unclear: test or document recovery before launch.
  fallback: require recovery plan for customer-facing production systems.
```

---

# 6. Final Principle

> Hardening decisions should be conservative when customer data, tenant isolation or recovery readiness is unclear.
