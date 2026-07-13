## FILE: `templates/security/security-review-template/examples/examples.md`

# Security Review Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Project Submission Security Review

## Review Name

```text
Project Submission Security Review
```

## Scope

```text
Review the project submission API, project status update, required document validation, audit event and reviewer assignment job.
```

## Risk Level

```text
medium
```

## Authorization Rule

```text
User must have project.submit permission in the same workspace as the project.
```

## Tenant Boundary

```text
The project.workspace_id must match the authenticated user's active workspace_id.
```

## Audit Event

```text
project.submitted
```

Required fields:

```text
actor_id
workspace_id
project_id
result
timestamp
request_id
```

## Security Test Case

```text
Given a user from workspace A
When the user attempts to submit a project from workspace B
Then the API returns permission_denied and no workspace B project details are exposed.
```

## Decision

```text
approved_with_conditions
```

## Required Fix

```text
Add explicit tenant isolation test before release.
```

---

# 2. Example — File Upload Review

## Risk

```text
Unsafe file upload could allow malicious files, oversized payloads or unauthorized document access.
```

## Mitigation

```text
Restrict file types, enforce size limits, store files privately, use signed URLs and validate workspace ownership before access.
```

---

# 3. Example — Billing Admin Review

## Permission Rule

```text
Only workspace_owner and billing_admin can access invoices or change subscription state.
```

## Audit Events

```text
billing.subscription_changed
billing.payment_method_updated
billing.invoice_viewed
```

---

# 4. Final Principle

> Examples show that security reviews should turn abstract risk into concrete checks and release decisions.
