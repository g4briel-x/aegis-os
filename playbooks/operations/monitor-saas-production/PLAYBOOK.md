## FILE: `playbooks/operations/monitor-saas-production/PLAYBOOK.md`

# Monitor SaaS Production — Playbook Definition

Version: 0.1.0  
Status: Premium Draft

---

# 1. Purpose

Guide a structured monitoring process for SaaS production health.

---

# 2. Trigger

A SaaS application is live and requires operational monitoring, especially after deployment or during business-critical periods.

---

# 3. Inputs

Useful inputs include:

- production environment;
- monitoring dashboard;
- logs;
- metrics;
- traces;
- deployment history;
- alert rules;
- critical user flows;
- infrastructure status;
- database status;
- support reports;
- business metrics.

---

# 4. Outputs

Expected outputs include:

- production health summary;
- signal review;
- alert review;
- anomaly findings;
- risk notes;
- escalation decision;
- follow-up actions;
- monitoring improvement recommendations.

---

# 5. Execution Summary

```text
1. Define monitoring scope
2. Review application health
3. Review error rate and logs
4. Review latency and performance
5. Review infrastructure health
6. Review database health
7. Review critical user flows
8. Review security and abuse signals
9. Classify anomalies
10. Escalate or record follow-up actions
```

---

# 6. Completion Criteria

The Playbook is complete when:

- production signals are reviewed;
- anomalies are classified;
- critical risks are escalated;
- follow-up actions are assigned;
- monitoring gaps are documented;
- current production health is summarized.

---

# 7. Escalation or Fallback

Escalate when:

- user impact is confirmed;
- error rate is above threshold;
- latency affects critical workflows;
- database or infrastructure is unstable;
- security compromise is suspected;
- alerts are firing repeatedly;
- monitoring data is missing for critical services.

---

# 8. Final Principle

> Monitoring is not watching dashboards. Monitoring is making production risk visible and actionable.