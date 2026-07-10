## FILE: `patterns/security/rbac-permission-model/context.md`

# RBAC Permission Model — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products where users have different responsibilities and data access boundaries.

Examples:

```text
B2B SaaS
client portals
collaboration tools
project management platforms
marketplaces
document platforms
financing platforms
enterprise dashboards
```

---

# 2. Product Context

Use this Pattern when the product has:

- owners;
- admins;
- members;
- viewers;
- reviewers;
- customers;
- external partners;
- support users;
- billing administrators.

---

# 3. Data Context

Use this Pattern when data is scoped by:

```text
organization
workspace
tenant
project
owner
assigned reviewer
public visibility
```

---

# 4. Technical Context

The Pattern works with:

- REST APIs;
- GraphQL APIs;
- server-rendered apps;
- background jobs;
- file storage;
- multi-tenant databases;
- admin dashboards.

---

# 5. Warning Signs

Permission design is weak when:

- role names are clear but allowed actions are not;
- admin can do too much;
- API authorization differs from UI authorization;
- tenant filters are repeated manually everywhere;
- tests do not cover denied access;
- file download permissions are not checked;
- support access is not audited.

---

# 6. Final Principle

> RBAC context should always include the customer boundary, not only the role name.
