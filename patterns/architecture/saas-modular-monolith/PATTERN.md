## FILE: `patterns/architecture/saas-modular-monolith/PATTERN.md`

# SaaS Modular Monolith Pattern

Version: 0.1.0  
Status: Draft

---

# 1. Problem

A SaaS product needs to move fast while remaining maintainable.

The team needs:

- fast deployment;
- simple infrastructure;
- clear ownership;
- modular code;
- testable business logic;
- room for future scale.

A traditional unstructured monolith becomes difficult to evolve. Premature microservices create operational burden before the business model is validated.

---

# 2. Context

This Pattern applies when:

```text
The SaaS product is in MVP, beta, early growth or controlled scale phase.
The team needs strong architecture without excessive infrastructure.
Product requirements are still changing.
Domain boundaries are visible but not fully stable.
```

---

# 3. Forces

Key forces:

```text
speed versus structure
simplicity versus scale
product change versus architectural stability
single deployment versus module autonomy
shared database versus data ownership
low operations cost versus future service extraction
```

---

# 4. Recommended Solution

Use a modular monolith.

The system should be one application at runtime, but internally divided into modules.

Recommended module examples:

```text
identity
organizations
workspaces
projects
files
reviews
billing
notifications
analytics
admin
audit
```

Each module should own:

```text
domain logic
application services
validation rules
module-specific data access
tests
public internal interface
```

---

# 5. Boundary Rules

Modules should communicate through explicit interfaces.

Avoid:

```text
direct access to another module's internal classes
shared business logic without ownership
cross-module database writes without service boundary
circular dependencies
global utility abuse
```

Prefer:

```text
module service interfaces
domain events
application commands
read-only query models when needed
shared contracts
```

---

# 6. Data Model Approach

Use one database for operational simplicity, but keep data ownership clear.

Recommended practices:

- group tables by domain;
- use consistent naming;
- define ownership for each table;
- avoid uncontrolled joins across modules;
- document cross-module relationships;
- use migrations with review;
- prepare extraction boundaries if needed.

---

# 7. API Layer

Expose APIs through a clear boundary.

Recommended structure:

```text
controllers/routes
request validation
application services
domain services
repositories/data access
response mapping
```

Do not expose database structures directly as API contracts.

---

# 8. Future Extraction Path

A module may become a service later when:

- it has independent scale needs;
- it has stable boundaries;
- it has separate team ownership;
- it has distinct data lifecycle;
- it creates operational bottlenecks inside the monolith.

Until then, keep it modular inside one application.

---

# 9. Final Principle

> The modular monolith is not an excuse to delay architecture. It is architecture optimized for learning, speed and controlled complexity.
