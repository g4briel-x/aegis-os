## FILE: `playbooks/engineering/create-api-contract/decision-points.md`

# Create API Contract — Decision Points

Version: 0.1.0  
Status: Premium Draft

---

# 1. Decision Point — Is This a New Resource or an Action?

```yaml
decision_point:
  question: Should the API model this as a resource endpoint or a custom action?
  options:
    - resource
    - action
    - unclear
  criteria:
    - persistent business object
    - lifecycle state
    - CRUD behavior
    - domain action
    - clarity for client
  recommended_action:
    resource: use RESTful resource naming.
    action: use explicit action when it represents domain behavior.
    unclear: review data model and workflow.
  fallback: choose the structure that best communicates domain intent.
```

---

# 2. Decision Point — Should the Endpoint Be Public?

```yaml
decision_point:
  question: Should this endpoint be accessible without authenticated user context?
  options:
    - yes
    - no
    - limited
  criteria:
    - public content
    - anonymous workflow
    - security risk
    - abuse risk
    - sensitive data
  recommended_action:
    yes: add rate limiting and restrict returned fields.
    no: require authentication.
    limited: define exact public fields and protections.
  fallback: default to authenticated access.
```

---

# 3. Decision Point — Is Authorization Object-Level?

```yaml
decision_point:
  question: Does access depend on ownership, tenant, workspace or resource membership?
  options:
    - yes
    - no
    - unclear
  criteria:
    - user-owned resources
    - organization-scoped data
    - workspace membership
    - tenant isolation
    - role-specific access
  recommended_action:
    yes: document object-level authorization rule.
    no: document global or role-level rule.
    unclear: involve Security Engineer Skill.
  fallback: assume object-level authorization for customer data.
```

---

# 4. Decision Point — Is This a Breaking Change?

```yaml
decision_point:
  question: Could this change break existing clients?
  options:
    - yes
    - no
    - unclear
  criteria:
    - removed field
    - renamed field
    - changed type
    - changed required field
    - changed status code
    - changed error behavior
  recommended_action:
    yes: version or migrate safely.
    no: document compatibility.
    unclear: review existing client usage.
  fallback: avoid breaking changes without explicit migration plan.
```

---

# 5. Decision Point — Is Pagination Required?

```yaml
decision_point:
  question: Can this endpoint return an unbounded or large result set?
  options:
    - yes
    - no
    - likely
  criteria:
    - list endpoint
    - growing records
    - dashboard query
    - search result
    - external integration
  recommended_action:
    yes: require pagination.
    no: document bounded response.
    likely: add pagination from the beginning.
  fallback: paginate all collection endpoints unless clearly bounded.
```

---

# 6. Final Principle

> API contract decisions should favor explicit behavior, safe defaults and client stability.
