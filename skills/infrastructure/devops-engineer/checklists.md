## FILE: `skills/infrastructure/devops-engineer/checklists.md`

# DevOps Engineer — Checklists

Version: 0.2.0  
Status: Premium Draft

---

# 1. CI/CD Checklist

```text
[ ] Repository context identified
[ ] Build step defined
[ ] Test step defined
[ ] Deployment step defined
[ ] Environment variables documented
[ ] Secrets handled safely
[ ] Failure notifications considered
[ ] Rollback or recovery path defined
```

---

# 2. Deployment Checklist

```text
[ ] Target environment confirmed
[ ] Configuration validated
[ ] Secrets available and not exposed
[ ] Artifact or image verified
[ ] Database migration risk reviewed
[ ] Smoke tests defined
[ ] Monitoring active
[ ] Rollback plan ready
```

---

# 3. Docker Checklist

```text
[ ] Base image appropriate
[ ] Dependencies installed intentionally
[ ] Build cache considered
[ ] Secrets not baked into image
[ ] Runtime command clear
[ ] Ports documented
[ ] Image size reviewed
[ ] Security reviewed
```

---

# 4. Observability Checklist

```text
[ ] Health check defined
[ ] Logs available
[ ] Metrics defined
[ ] Alerts defined
[ ] Dashboard considered
[ ] Error rate monitored
[ ] Latency monitored where relevant
[ ] Incident evidence accessible
```

---

# 5. Security Checklist

```text
[ ] Secrets not committed
[ ] Least privilege considered
[ ] Production access controlled
[ ] Audit trail considered
[ ] Dependency risk considered
[ ] Deployment permissions reviewed
[ ] Sensitive logs avoided
```

---

# 6. 4-Pass Validation Checklist

```text
[ ] Pass 1 completed — requirements and environment
[ ] Pass 2 completed — automation and deployment safety
[ ] Pass 3 completed — security and access control
[ ] Pass 4 completed — observability and rollback
[ ] Weaknesses corrected or documented
```

---

# 7. Final Principle

> DevOps checklists protect production from invisible operational assumptions.