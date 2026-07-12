## FILE: `patterns/security/tenant-data-isolation/context.md`

# Tenant Data Isolation — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products where multiple customers share the same application.

Typical examples:

```text
B2B SaaS
workspace SaaS
client portal
document platform
financing platform
collaboration platform
enterprise dashboard
```

---

# 2. Product Context

Use this Pattern when:

- customers have private records;
- users belong to organizations;
- workspaces contain shared resources;
- projects, files or invoices must stay private;
- admins or support users may access customer data.

---

# 3. Technical Context

The Pattern works with:

- shared database;
- shared application runtime;
- REST API;
- GraphQL API;
- object storage;
- background workers;
- search indexes;
- analytics pipelines.

---

# 4. Security Context

Tenant isolation is critical when data includes:

```text
personal information
business records
financial records
private documents
project files
contracts
messages
admin settings
```

---

# 5. Warning Signs

Tenant isolation is weak when:

- API accepts only resource id without tenant context;
- file downloads rely only on URL secrecy;
- search returns records across workspaces;
- background jobs lack tenant id;
- tests do not include cross-tenant denial;
- support can access customer data without audit;
- tenant checks are duplicated manually everywhere.

---

# 6. Final Principle

> The more tenants share infrastructure, the more explicit tenant boundaries must be.
