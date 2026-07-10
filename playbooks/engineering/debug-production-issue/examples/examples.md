## FILE: `playbooks/engineering/debug-production-issue/examples/examples.md`

# Debug Production Issue — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — API 500 Errors After Deployment

## Trigger

Monitoring shows a spike in HTTP 500 errors after a backend deployment.

## Expected Execution

The Playbook should guide the user to:

- confirm production impact;
- inspect recent deployment;
- review logs;
- identify failing endpoint;
- decide rollback versus hotfix;
- verify recovery;
- document prevention.

## Expected Output

```text
Impact summary
Recent changes
Evidence
Likely root cause
Mitigation decision
Verification
Prevention actions
```

---

# 2. Example — Login Failure

## Trigger

Users report that they cannot log in after a configuration change.

## Expected Execution

The Playbook should guide the user to:

- check authentication logs;
- inspect environment variables;
- review session or token configuration;
- assess whether rollback is safe;
- verify login flow after correction.

---

# 3. Example — Slow Database Queries

## Trigger

Application latency increases and database CPU is high.

## Expected Execution

The Playbook should guide the user to:

- identify slow endpoints;
- inspect query logs;
- review recent migrations;
- check indexes;
- mitigate with safe operational action;
- plan permanent query or indexing fix.

---

# 4. Example — Third-Party API Outage

## Trigger

A payment or email provider becomes unavailable.

## Expected Execution

The Playbook should guide the user to:

- confirm provider status;
- isolate affected workflows;
- activate fallback or queueing if available;
- communicate impact;
- verify recovery when provider returns.

---

# 5. Example — Suspected Data Integrity Issue

## Trigger

Users report missing or duplicated records after a deployment.

## Expected Execution

The Playbook should guide the user to:

- pause risky writes if needed;
- preserve evidence;
- review migrations and write paths;
- involve database and security reviewers if needed;
- define repair and validation plan.

---

# 6. Final Principle

> Examples show how the Playbook behaves under real production pressure.
