## FILE: `playbooks/operations/monitor-saas-production/steps.md`

# Monitor SaaS Production — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define Monitoring Scope

Clarify what is being monitored.

Capture:

- environment;
- services;
- release version;
- critical workflows;
- monitoring window;
- responsible owner;
- escalation contact.

Output:

```text
Monitoring scope summary
```

---

# 2. Step 2 — Review Application Health

Check whether the application is generally available.

Review:

- uptime;
- health checks;
- service status;
- deployment status;
- recent restarts;
- crash indicators;
- availability by region if relevant.

Output:

```text
Application health summary
```

---

# 3. Step 3 — Review Error Rate and Logs

Inspect application errors.

Review:

- error rate;
- exception types;
- repeated stack traces;
- failed requests;
- warning spikes;
- correlation IDs;
- affected endpoints.

Output:

```text
Error and log review
```

---

# 4. Step 4 — Review Latency and Performance

Check performance signals.

Review:

- request latency;
- page load time;
- API response time;
- slow endpoints;
- timeout errors;
- queue processing time;
- user workflow duration.

Output:

```text
Latency and performance summary
```

---

# 5. Step 5 — Review Infrastructure Health

Check runtime resources.

Review:

- CPU;
- memory;
- disk;
- network;
- container or function failures;
- scaling events;
- region or provider status;
- deployment platform errors.

Output:

```text
Infrastructure health summary
```

---

# 6. Step 6 — Review Database Health

Check persistence layer health.

Review:

- connection errors;
- slow queries;
- lock contention;
- replication lag;
- storage usage;
- failed migrations;
- backup status;
- query volume.

Output:

```text
Database health summary
```

---

# 7. Step 7 — Review Critical User Flows

Verify the product workflows that matter most.

Examples:

- signup;
- login;
- dashboard load;
- project creation;
- payment;
- file upload;
- search;
- notification delivery.

Output:

```text
Critical flow review
```

---

# 8. Step 8 — Review Security and Abuse Signals

Check for suspicious behavior.

Review:

- login failures;
- unusual traffic spikes;
- authorization failures;
- rate limit events;
- suspicious IPs;
- file access anomalies;
- admin action anomalies.

Output:

```text
Security signal review
```

---

# 9. Step 9 — Classify Anomalies

Classify issues by severity.

Suggested levels:

```text
normal
watch
degraded
incident
security_review_needed
```

Output:

```text
Anomaly classification
```

---

# 10. Step 10 — Escalate or Assign Follow-Up

Decide what happens next.

Possible actions:

- continue monitoring;
- create bug ticket;
- escalate to incident playbook;
- escalate to security incident playbook;
- rollback recent release;
- improve alerting;
- add missing instrumentation.

Output:

```text
Operational decision and follow-up actions
```

---

# 11. Final Principle

> Monitoring steps should turn signals into decisions, not dashboards into decoration.