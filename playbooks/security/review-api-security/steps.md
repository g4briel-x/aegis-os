## FILE: `playbooks/security/review-api-security/steps.md`

# Review API Security — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define API Review Scope

Identify what is being reviewed.

Capture:

- endpoint path;
- HTTP method;
- purpose;
- consuming clients;
- environment;
- exposure level;
- owner.

Output:

```text
API review scope
```

---

# 2. Step 2 — Identify Protected Assets

Identify what the API can access, modify or expose.

Review:

- user data;
- account data;
- tenant data;
- payment data;
- files;
- credentials;
- internal records;
- administrative actions.

Output:

```text
Protected asset list
```

---

# 3. Step 3 — Review Authentication

Verify how the API confirms identity.

Check:

- authentication requirement;
- token or session handling;
- credential storage;
- token expiry;
- refresh behavior;
- anonymous access;
- service-to-service authentication.

Output:

```text
Authentication review findings
```

---

# 4. Step 4 — Review Authorization

Verify what authenticated users are allowed to do.

Check:

- role checks;
- resource ownership;
- tenant isolation;
- object-level authorization;
- admin-only actions;
- privilege escalation paths.

Output:

```text
Authorization review findings
```

---

# 5. Step 5 — Review Input Validation

Check that the API validates all input.

Review:

- required fields;
- field types;
- length limits;
- allowed values;
- file uploads;
- nested objects;
- injection risks;
- malformed requests.

Output:

```text
Input validation findings
```

---

# 6. Step 6 — Review Output and Data Exposure

Check what the API returns.

Review:

- sensitive fields;
- internal IDs;
- debug data;
- tokens or secrets;
- unnecessary nested data;
- cross-tenant leakage;
- excessive response detail.

Output:

```text
Data exposure findings
```

---

# 7. Step 7 — Review Abuse Controls

Check whether the API can be abused.

Review:

- rate limits;
- brute force protection;
- pagination limits;
- request size limits;
- expensive query protection;
- replay protection where relevant;
- automation abuse.

Output:

```text
Abuse control findings
```

---

# 8. Step 8 — Review Error Handling

Check that errors are safe and useful.

Review:

- status codes;
- error messages;
- stack traces;
- validation errors;
- authentication errors;
- authorization errors;
- information leakage.

Output:

```text
Error handling findings
```

---

# 9. Step 9 — Review Logging and Audit

Check whether security-relevant activity is visible.

Review:

- login or token events;
- privileged actions;
- failed authorization;
- sensitive data access;
- admin changes;
- suspicious behavior;
- correlation IDs.

Output:

```text
Logging and audit findings
```

---

# 10. Step 10 — Prioritize Risks and Mitigations

Rank findings by severity and define corrections.

For each risk, capture:

- issue;
- impact;
- likelihood;
- affected endpoint;
- mitigation;
- owner;
- verification method.

Output:

```text
Prioritized mitigation plan
```

---

# 11. Final Principle

> API security review must follow the data and the permission boundary, not only the route name.