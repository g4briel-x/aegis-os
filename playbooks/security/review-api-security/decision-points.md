## FILE: `playbooks/security/review-api-security/decision-points.md`

# Review API Security — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is Authentication Required?

```yaml
decision_point:
  question: Should this endpoint require authenticated identity?
  options:
    - yes
    - no
    - unclear
  criteria:
    - accesses user data
    - modifies state
    - performs sensitive operation
    - exposes internal information
  recommended_action:
    yes: enforce authentication server-side.
    no: document why public access is safe.
    unclear: treat as authenticated until reviewed.
  fallback: restrict access until authentication requirements are confirmed.
```

---

# 2. Decision Point — Is Object-Level Authorization Needed?

```yaml
decision_point:
  question: Does the endpoint access a specific user, tenant, project, invoice, file or record?
  options:
    - yes
    - no
    - unknown
  criteria:
    - resource identifier in path
    - resource identifier in body
    - tenant-specific data
    - role-specific access
  recommended_action:
    yes: enforce object-level authorization.
    no: verify endpoint does not expose scoped resources.
    unknown: inspect data model and route behavior.
  fallback: block access to scoped resources until ownership checks are defined.
```

---

# 3. Decision Point — Could the Response Expose Sensitive Data?

```yaml
decision_point:
  question: Could the response include sensitive, internal or cross-tenant data?
  options:
    - yes
    - no
    - unknown
  criteria:
    - personal data
    - financial data
    - internal IDs
    - tokens or secrets
    - tenant-specific records
  recommended_action:
    yes: minimize response and remove sensitive fields.
    no: document reviewed fields.
    unknown: inspect response schema and real examples.
  fallback: reduce output to only required fields.
```

---

# 4. Decision Point — Is Abuse Protection Required?

```yaml
decision_point:
  question: Could the endpoint be abused through high volume, brute force or expensive requests?
  options:
    - yes
    - no
    - unknown
  criteria:
    - login or verification endpoint
    - search endpoint
    - file upload endpoint
    - expensive database query
    - public exposure
  recommended_action:
    yes: add rate limits, size limits or abuse controls.
    no: document why abuse risk is low.
    unknown: add conservative limits until usage is known.
  fallback: monitor usage and alert on abnormal patterns.
```

---

# 5. Final Principle

> API security decisions must be conservative when identity, data or abuse risk is unclear.
