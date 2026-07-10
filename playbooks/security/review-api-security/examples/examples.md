## FILE: `playbooks/security/review-api-security/examples/examples.md`

# Review API Security — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Billing Endpoint

## Trigger

A new endpoint allows users to update billing information.

## Expected Execution

The Playbook should guide the reviewer to:

- require authentication;
- verify the user can only update their own account or tenant;
- validate request fields;
- avoid returning payment-sensitive data;
- log security-relevant changes;
- define verification tests.

## Expected Output

```text
API scope
Protected assets
Authorization findings
Validation findings
Data exposure findings
Mitigation plan
Verification checklist
```

---

# 2. Example — Admin User Management API

## Trigger

An admin endpoint allows creating, disabling and changing user roles.

## Expected Execution

The Playbook should guide the reviewer to:

- check admin-only access;
- verify least privilege;
- require audit logs;
- prevent privilege escalation;
- review error responses;
- define approval or monitoring requirements.

---

# 3. Example — Public Search API

## Trigger

A public search endpoint returns project records.

## Expected Execution

The Playbook should guide the reviewer to:

- check public data boundaries;
- prevent private fields from being returned;
- add pagination limits;
- add rate limits;
- avoid expensive unbounded queries.

---

# 4. Example — File Upload API

## Trigger

An API allows users to upload documents.

## Expected Execution

The Playbook should guide the reviewer to:

- validate file type and size;
- authenticate upload action;
- enforce ownership;
- avoid public file exposure;
- scan or quarantine risky files where relevant;
- define storage access rules.

---

# 5. Final Principle

> Examples show how the Playbook protects APIs from access, validation, exposure and abuse failures.
