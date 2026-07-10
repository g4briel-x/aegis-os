## FILE: `playbooks/engineering/create-api-contract/steps.md`

# Create API Contract — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define API Purpose and Consumers

Clarify why the API exists and who will use it.

Capture:

- product workflow;
- frontend consumer;
- external integration consumer;
- user role;
- expected action;
- success outcome;
- non-goals.

Output:

```text
API purpose and consumer summary
```

---

# 2. Step 2 — Identify Resources and Actions

Define the business resources exposed by the API.

Examples:

- users;
- organizations;
- workspaces;
- projects;
- documents;
- reviews;
- comments;
- notifications;
- invoices;
- audit events.

For each resource, define actions:

```text
create
read
list
update
delete
submit
approve
reject
archive
```

Output:

```text
Resource and action map
```

---

# 3. Step 3 — Design Endpoints and Methods

Define endpoint paths and HTTP methods.

Review:

- resource naming;
- route hierarchy;
- path parameters;
- query parameters;
- collection endpoints;
- resource endpoints;
- action endpoints;
- HTTP method semantics.

Output:

```text
Endpoint list
```

---

# 4. Step 4 — Define Request Schemas

Define what clients must send.

For each request, specify:

- required fields;
- optional fields;
- data types;
- validation rules;
- default values;
- file or multipart behavior;
- idempotency key if needed.

Output:

```text
Request schema definitions
```

---

# 5. Step 5 — Define Response Schemas

Define what the API returns.

For each response, specify:

- status code;
- response body;
- resource fields;
- nested objects;
- timestamps;
- pagination metadata;
- links or references;
- omitted sensitive fields.

Output:

```text
Response schema definitions
```

---

# 6. Step 6 — Define Error Model

Standardize failure responses.

Define errors for:

- validation failure;
- authentication failure;
- authorization failure;
- not found;
- conflict;
- rate limit;
- server error;
- dependency failure.

Output:

```text
Error model
```

---

# 7. Step 7 — Define Authentication and Authorization

Clarify access rules.

Review:

- authentication requirement;
- role requirement;
- object ownership;
- tenant boundary;
- admin-only actions;
- public endpoint rules;
- sensitive fields;
- audit requirements.

Output:

```text
Authentication and authorization notes
```

---

# 8. Step 8 — Define Pagination, Filtering and Sorting

For list endpoints, define access patterns.

Capture:

- pagination style;
- default limit;
- max limit;
- supported filters;
- sort fields;
- search behavior;
- stable ordering rule.

Output:

```text
Pagination, filtering and sorting rules
```

---

# 9. Step 9 — Review Versioning and Compatibility

Protect existing clients.

Review:

- breaking changes;
- optional versus required fields;
- deprecated fields;
- API versioning;
- backward-compatible additions;
- migration window;
- client communication.

Output:

```text
Versioning and compatibility notes
```

---

# 10. Step 10 — Produce Implementation Handoff

Assemble final API contract.

Include:

- endpoints;
- schemas;
- errors;
- permissions;
- examples;
- test expectations;
- open questions.

Output:

```text
Implementation-ready API contract
```

---

# 11. Final Principle

> API contract steps should turn product behavior into predictable technical exchange.