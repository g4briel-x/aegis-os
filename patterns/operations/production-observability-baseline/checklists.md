## FILE: `patterns/operations/production-observability-baseline/checklists.md`

# Production Observability Baseline — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Context Fit Checklist

```text
[ ] Production users exist or are planned
[ ] API endpoints exist
[ ] Critical workflows exist
[ ] Background jobs exist or are planned
[ ] Support needs request correlation
[ ] Incidents must be diagnosed quickly
```

---

# 2. Logging Checklist

```text
[ ] Structured logs are used
[ ] Request id is included
[ ] Environment is included
[ ] Service name is included
[ ] Error code is included where relevant
[ ] Tenant id is included when safe
[ ] Sensitive data is redacted
```

---

# 3. Metrics Checklist

```text
[ ] API request count tracked
[ ] Error rate tracked
[ ] Latency tracked
[ ] Database health tracked
[ ] Background job health tracked
[ ] Dependency failures tracked
[ ] Critical workflow metrics tracked
```

---

# 4. Dashboard Checklist

```text
[ ] Production overview dashboard exists
[ ] API health dashboard exists
[ ] Database dashboard exists
[ ] Background jobs dashboard exists
[ ] Critical workflow dashboard exists
[ ] Release impact dashboard exists
[ ] Dashboard owner assigned
```

---

# 5. Alert Checklist

```text
[ ] Critical alerts defined
[ ] Alert thresholds are actionable
[ ] Alert owner assigned
[ ] Notification channel defined
[ ] Runbook linked
[ ] Severity defined
[ ] Noisy alerts reviewed
```

---

# 6. Incident Evidence Checklist

```text
[ ] Request id available
[ ] Release marker available
[ ] Affected tenants can be identified
[ ] Error traces are available
[ ] Logs can be searched
[ ] Recovery metric is defined
```

---

# 7. Final Principle

> Observability checklists should prove that production can be seen, understood and recovered.
