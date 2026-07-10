## FILE: `playbooks/operations/prepare-release/checklists.md`

# Prepare Release — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Scope Checklist

```text
[ ] Release objective defined
[ ] Included changes listed
[ ] Excluded changes listed
[ ] Affected services identified
[ ] Owners identified
[ ] Stakeholders informed
[ ] Target environment confirmed
```

---

# 2. Quality Checklist

```text
[ ] Code reviews complete
[ ] Unit tests passed
[ ] Integration tests passed where relevant
[ ] End-to-end tests passed where relevant
[ ] Acceptance criteria met
[ ] Known defects documented
[ ] Documentation updated if needed
```

---

# 3. Data and Compatibility Checklist

```text
[ ] Database migrations reviewed
[ ] Backward compatibility reviewed
[ ] API compatibility reviewed
[ ] Data transformation risk reviewed
[ ] Backup need identified
[ ] Migration validation defined
[ ] Data rollback limits documented
```

---

# 4. Security Checklist

```text
[ ] Authentication changes reviewed
[ ] Authorization changes reviewed
[ ] Secrets not exposed
[ ] Sensitive data exposure reviewed
[ ] Public API changes reviewed
[ ] Dependency risk reviewed
[ ] Audit logging considered
```

---

# 5. Deployment Checklist

```text
[ ] Deployment owner assigned
[ ] Deployment steps documented
[ ] Required approvals collected
[ ] Environment variables validated
[ ] Feature flags configured if needed
[ ] Smoke tests defined
[ ] Deployment window confirmed
```

---

# 6. Rollback Checklist

```text
[ ] Rollback trigger defined
[ ] Rollback steps documented
[ ] Rollback owner assigned
[ ] Data rollback constraints reviewed
[ ] Feature disablement option defined
[ ] Recovery verification defined
```

---

# 7. Monitoring Checklist

```text
[ ] Error rate monitored
[ ] Latency monitored
[ ] Logs monitored
[ ] Critical user flows monitored
[ ] Support channel monitored
[ ] Business metric monitored if relevant
[ ] Monitoring window defined
```

---

# 8. Final Principle

> Release checklists reduce avoidable production failure by forcing readiness before action.
