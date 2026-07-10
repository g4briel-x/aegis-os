## FILE: `playbooks/security/design-auth-rbac/outputs.md`

# Design Auth RBAC — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Authentication Model

Purpose:

Define how users authenticate.

Required sections:

```text
Login method:
Identity provider:
Session model:
Token model:
User lifecycle:
Recovery:
MFA:
```

---

# 2. Role Catalog

Purpose:

Define system roles.

Required sections:

```text
Role:
Purpose:
Scope:
Assignable by:
Default permissions:
Risk:
```

---

# 3. Permission Matrix

Purpose:

Map roles to actions.

Required sections:

```text
Role:
Resource:
Action:
Allowed:
Condition:
Notes:
```

---

# 4. Resource Ownership Model

Purpose:

Define who owns each protected record.

Required sections:

```text
Resource:
Owner:
Tenant boundary:
Shared access:
Admin access:
Restriction:
```

---

# 5. API Authorization Rules

Purpose:

Define endpoint-level access control.

Required sections:

```text
Endpoint:
Method:
Authentication:
Role:
Permission:
Ownership check:
Tenant check:
Audit:
```

---

# 6. Audit Event List

Purpose:

Define security events to log.

Required sections:

```text
Event:
Actor:
Resource:
Trigger:
Fields:
Retention:
```

---

# 7. Permission Test Matrix

Purpose:

Validate access behavior.

Required sections:

```text
Role:
Resource:
Action:
Expected result:
Test type:
Priority:
```

---

# 8. Final Principle

> RBAC outputs must be detailed enough to implement guards, write tests and review security posture.
