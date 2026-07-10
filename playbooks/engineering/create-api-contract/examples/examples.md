## FILE: `playbooks/engineering/create-api-contract/examples/examples.md`

# Create API Contract — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Project Submission API

## Trigger

A SaaS platform needs an API for creators to submit audiovisual projects for financing review.

## Expected Execution

The Playbook should guide the team to:

- define project resource endpoints;
- define create, update, submit and list behavior;
- define draft and submitted response states;
- define creator ownership rules;
- define validation errors;
- define reviewer list access.

## Expected Output

```text
API contract
Endpoint list
Request schemas
Response schemas
Error schema
Authorization rules
Compatibility notes
```

---

# 2. Example — File Upload API

## Trigger

A feature requires uploading pitch decks and project documents.

## Expected Execution

The Playbook should guide the team to:

- define upload request model;
- define file metadata response;
- define file type and size validation;
- define access rules;
- define error responses for invalid files.

---

# 3. Example — Dashboard Metrics API

## Trigger

The frontend needs a dashboard metrics endpoint.

## Expected Execution

The Playbook should guide the team to:

- define aggregate response schema;
- define date range filters;
- define pagination if needed;
- define cache behavior if applicable;
- define permission boundary.

---

# 4. Example — External Investor Integration API

## Trigger

An external partner needs controlled access to selected project data.

## Expected Execution

The Playbook should guide the team to:

- define authentication model;
- restrict returned fields;
- add rate limits;
- document versioning;
- define audit events.

---

# 5. Final Principle

> Examples show that API contracts align product workflow, data structure, permissions and client expectations.
