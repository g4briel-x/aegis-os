## FILE: `templates/operations/incident-report-template/examples/examples.md`

# Incident Report Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Project Submission API Degradation

## Incident Name

```text
Project Submission API Degradation
```

## Status

```text
identified
```

## Severity

```text
SEV2
```

## Current Status

```text
As of 15:20 UTC, the project submission API is degraded for some workspaces. The team has identified increased database lock waits during submission validation. A mitigation is being prepared.
```

## Customer Impact

```text
Some creators cannot submit completed project packages for readiness review. Draft editing, login and document upload remain available.
```

## Timeline

```text
15:02 | API error rate alert fired | monitoring
15:05 | Incident declared as SEV2 | operations
15:11 | Database lock waits identified | technical lead
15:20 | Mitigation plan prepared | engineering
```

## Next Steps

```text
Apply mitigation query timeout adjustment | Technical Lead | 15:30 UTC | in_progress
Validate submission success rate | Operations | 15:40 UTC | pending
Prepare customer update if degradation continues | Support | 15:45 UTC | pending
```

---

# 2. Example — Security Incident Report Note

```text
If cross-tenant access is suspected, classify severity conservatively, preserve audit logs, avoid deleting evidence and involve Security immediately.
```

---

# 3. Example — Resolution Section

```text
Resolved at: 16:05 UTC
Resolution summary: Database lock contention was mitigated by disabling the risky validation path behind a feature flag.
Validation performed: Submission success rate returned to normal and no new errors were observed for 20 minutes.
Postmortem required: Yes
```

---

# 4. Final Principle

> Examples show that incident reports should be short, factual and operationally useful.