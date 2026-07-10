## FILE: `playbooks/engineering/create-api-contract/outputs.md`

# Create API Contract — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. API Contract

Purpose:

Provide the complete endpoint behavior definition.

Required sections:

```text
Endpoint:
Method:
Purpose:
Auth:
Request:
Response:
Errors:
Permissions:
Examples:
```

---

# 2. Endpoint List

Purpose:

Summarize all API endpoints in scope.

Required sections:

```text
Method:
Path:
Resource:
Action:
Consumer:
Status:
```

---

# 3. Request Schema

Purpose:

Define what clients send.

Required sections:

```text
Field:
Type:
Required:
Validation:
Default:
Notes:
```

---

# 4. Response Schema

Purpose:

Define what clients receive.

Required sections:

```text
Field:
Type:
Nullable:
Description:
Sensitive:
Notes:
```

---

# 5. Error Schema

Purpose:

Standardize error responses.

Required sections:

```text
Status:
Code:
Message:
Details:
When:
```

---

# 6. Authorization Rule

Purpose:

Clarify access control.

Required sections:

```text
Endpoint:
Role:
Resource owner:
Tenant rule:
Allowed:
Denied:
Audit:
```

---

# 7. Compatibility Notes

Purpose:

Protect existing clients.

Required sections:

```text
Change:
Breaking:
Affected clients:
Migration:
Versioning:
Decision:
```

---

# 8. Final Principle

> API contract outputs must be precise enough to generate implementation, tests and documentation.
