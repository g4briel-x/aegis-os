## FILE: `playbooks/operations/monitor-saas-production/examples/examples.md`

# Monitor SaaS Production — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Post-Deployment Monitoring

## Trigger

A new SaaS release has just been deployed to production.

## Expected Execution

The Playbook should guide the team to:

- review application health;
- check error rate;
- monitor affected endpoints;
- test critical user flows;
- watch logs;
- classify anomalies;
- confirm success or escalate.

## Expected Output

```text
Production health summary
Signal review
Alert review
Anomaly findings
Escalation decision
Follow-up actions
```

---

# 2. Example — Login Error Spike

## Trigger

Monitoring shows an increase in login failures.

## Expected Execution

The Playbook should guide the team to:

- check authentication logs;
- compare baseline;
- inspect recent deployments;
- review suspicious activity;
- decide between debugging and security review.

---

# 3. Example — Database Latency Increase

## Trigger

Database query latency increases after a release.

## Expected Execution

The Playbook should guide the team to:

- review slow queries;
- inspect recent migrations;
- check indexes;
- monitor user workflow impact;
- escalate if critical workflows degrade.

---

# 4. Example — Suspicious Traffic Spike

## Trigger

Traffic increases suddenly from unusual IP ranges.

## Expected Execution

The Playbook should guide the team to:

- review rate limits;
- inspect authentication failures;
- check security logs;
- involve Security Engineer Skill if suspicious behavior persists.

---

# 5. Final Principle

> Examples show that production monitoring connects technical signals to operational decisions.
