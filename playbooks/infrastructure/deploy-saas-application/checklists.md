## FILE: `playbooks/infrastructure/deploy-saas-application/checklists.md`

# Deploy SaaS Application — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Deployment Readiness Checklist

```text
[ ] Release scope confirmed
[ ] Target environment confirmed
[ ] Deployment owner assigned
[ ] Required approvals collected
[ ] CI checks passed
[ ] Build artifact available
[ ] Deployment window confirmed
```

---

# 2. Environment Checklist

```text
[ ] Runtime version confirmed
[ ] Environment variables confirmed
[ ] Service URLs confirmed
[ ] Domain settings confirmed
[ ] Feature flags confirmed
[ ] Database connection confirmed
[ ] Storage configuration confirmed
```

---

# 3. Secrets and Permissions Checklist

```text
[ ] Required secrets listed
[ ] Secrets available in target environment
[ ] Secret values not exposed
[ ] Deployment permissions confirmed
[ ] Service account permissions reviewed
[ ] Database permissions reviewed
[ ] Access is least privilege where possible
```

---

# 4. Migration Checklist

```text
[ ] Migration required or not confirmed
[ ] Migration reviewed
[ ] Backup required or not confirmed
[ ] Rollback limits documented
[ ] Destructive operations reviewed
[ ] Compatibility reviewed
[ ] Validation queries defined if needed
```

---

# 5. Smoke Test Checklist

```text
[ ] Application loads
[ ] Login works
[ ] Critical API responds
[ ] Core workflow works
[ ] Affected feature works
[ ] Error logs checked
[ ] Monitoring dashboard checked
```

---

# 6. Rollback Checklist

```text
[ ] Rollback trigger defined
[ ] Rollback owner assigned
[ ] Previous version identified
[ ] Rollback steps documented
[ ] Data constraints documented
[ ] Verification after rollback defined
```

---

# 7. Final Principle

> Deployment checklists reduce failure by forcing operational readiness before production risk is taken.