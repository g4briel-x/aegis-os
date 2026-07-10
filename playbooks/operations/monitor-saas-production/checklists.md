## FILE: `playbooks/operations/monitor-saas-production/checklists.md`

# Monitor SaaS Production — Checklists

Version: 0.1.0  
Status: Premium Draft

---

# 1. Monitoring Scope Checklist

```text
[ ] Environment defined
[ ] Services listed
[ ] Critical workflows listed
[ ] Monitoring window defined
[ ] Owner assigned
[ ] Escalation contact identified
[ ] Recent deployment reviewed
```

---

# 2. Application Health Checklist

```text
[ ] Uptime checked
[ ] Health checks reviewed
[ ] Error rate reviewed
[ ] Crash indicators reviewed
[ ] Recent restarts reviewed
[ ] Failed requests reviewed
[ ] User reports checked
```

---

# 3. Performance Checklist

```text
[ ] API latency reviewed
[ ] Page load time reviewed if available
[ ] Timeout errors reviewed
[ ] Slow endpoints identified
[ ] Queue processing time reviewed if relevant
[ ] Resource saturation checked
```

---

# 4. Database Checklist

```text
[ ] Database connectivity checked
[ ] Slow queries reviewed
[ ] Lock or timeout errors reviewed
[ ] Storage usage checked
[ ] Backup status checked
[ ] Migration status checked if recent release occurred
```

---

# 5. Security Signal Checklist

```text
[ ] Login failure spikes reviewed
[ ] Authorization failures reviewed
[ ] Rate limit events reviewed
[ ] Suspicious traffic reviewed
[ ] Admin action anomalies reviewed
[ ] Sensitive data access anomalies reviewed
```

---

# 6. Follow-Up Checklist

```text
[ ] Anomalies classified
[ ] Escalation decision recorded
[ ] Tickets created if needed
[ ] Owners assigned
[ ] Monitoring gaps documented
[ ] Alert improvements identified
```

---

# 7. Final Principle

> Monitoring checklists keep operations from missing weak signals before they become strong failures.
