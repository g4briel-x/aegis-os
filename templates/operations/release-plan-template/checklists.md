## FILE: `templates/operations/release-plan-template/checklists.md`

# Release Plan Template — Checklists

Version: 0.1.0  
Status: Draft

---

# 1. Completeness Checklist

```text
[ ] Release name is defined
[ ] Release owner is assigned
[ ] Scope is listed
[ ] Excluded changes are listed
[ ] Target release date is defined
[ ] Risk level is assigned
[ ] Dependencies are listed
[ ] Test readiness is documented
[ ] Deployment steps are written
[ ] Rollback plan exists
```

---

# 2. Risk Checklist

```text
[ ] Customer impact reviewed
[ ] Database migration reviewed
[ ] Security impact reviewed
[ ] Tenant isolation reviewed if relevant
[ ] Performance impact reviewed
[ ] Third-party dependency risk reviewed
[ ] Support impact reviewed
```

---

# 3. Deployment Checklist

```text
[ ] Deployment owner assigned
[ ] Release window confirmed
[ ] Feature flags configured if needed
[ ] Migration plan reviewed if needed
[ ] Monitoring dashboard ready
[ ] Communication channel ready
[ ] Stop conditions defined
```

---

# 4. Validation Checklist

```text
[ ] Health checks pass
[ ] Core workflows tested
[ ] Error rate reviewed
[ ] Logs reviewed
[ ] Background jobs reviewed
[ ] Metrics reviewed
[ ] Customer-facing behavior verified
```

---

# 5. Approval Checklist

```text
[ ] Product approved
[ ] Engineering approved
[ ] QA approved
[ ] Security approved if required
[ ] Operations approved
[ ] Support approved if customer-facing
```

---

# 6. Final Principle

> Release checklists should make production readiness measurable.
