## FILE: `templates/operations/postmortem-template/examples/examples.md`

# Postmortem Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Project Submission Outage

## Incident Name

```text
Project Submission Outage
```

## Severity

```text
SEV2
```

## Executive Summary

```text
On 2026-07-13, the project submission workflow failed for creators attempting to submit completed audiovisual project packages. The incident lasted 42 minutes and affected all users using the submission endpoint. The issue was caused by a required database field being introduced before existing project records were fully backfilled.
```

## Customer Impact

```text
Creators could not submit projects for readiness review. Draft editing remained available.
```

## Root Cause

```text
The release process did not require pre-deployment validation for existing records before adding a required schema constraint.
```

## Corrective Action

```text
Action: Add database migration safety checklist to release preparation.
Owner: Engineering Lead
Due Date: 2026-07-20
Priority: High
```

---

# 2. Example — Delayed Review Jobs

## Impact

```text
Reviewer assignment jobs were delayed for 90 minutes. Customers saw submitted projects remain in pending state.
```

## Detection Gap

```text
Queue depth alert existed, but job age alert did not exist.
```

## Corrective Action

```text
Add job age alert for project review jobs older than 15 minutes.
```

---

# 3. Example — Cross-Tenant Access Attempt

## Severity

```text
SEV1
```

## Required Notes

```text
Preserve audit logs.
Document exact exposure scope.
Include security review.
Include customer notification decision.
Track remediation separately.
```

---

# 4. Final Principle

> Examples show that postmortems should produce concrete reliability improvements, not only incident summaries.