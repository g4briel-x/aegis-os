## FILE: `patterns/architecture/saas-modular-monolith/solution.md`

# SaaS Modular Monolith — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Build one deployable SaaS application with explicit internal modules.

High-level structure:

```text
src/
  modules/
    identity/
    organizations/
    projects/
    files/
    billing/
    notifications/
    analytics/
    admin/
  shared/
    config/
    database/
    logging/
    errors/
    security/
  app/
    routes/
    middleware/
    bootstrap/
```

---

# 2. Module Structure

Each module should contain:

```text
domain/
application/
infrastructure/
api/
tests/
```

Example:

```text
modules/projects/
  domain/
  application/
  infrastructure/
  api/
  tests/
```

---

# 3. Module Responsibilities

Each module should own its business logic.

Example:

```text
projects module:
  project creation
  project lifecycle
  project validation
  project ownership
  project status transitions
  project-related policies
```

---

# 4. Shared Layer

The shared layer should be limited.

Good shared concerns:

```text
logging
configuration
database connection
error handling
authentication primitives
security helpers
common types
```

Avoid placing business rules in shared utilities.

---

# 5. Boundary Enforcement

Use one or more of:

- code review rules;
- import restrictions;
- module public interfaces;
- architecture tests;
- naming conventions;
- dependency direction rules.

---

# 6. Database Structure

Use one database but define logical ownership.

Example table ownership:

```text
identity owns users
organizations owns organizations and memberships
projects owns projects and project_status_history
files owns file_metadata
billing owns subscriptions and invoices
audit owns audit_events
```

---

# 7. Communication Between Modules

Prefer explicit communication.

Options:

```text
application service calls
domain events
internal command handlers
read model queries
shared contracts
```

Avoid hidden coupling through shared mutable state.

---

# 8. Deployment

Deploy as one unit.

Recommended deployment model:

```text
single CI pipeline
single build artifact
single runtime
single release process
environment-based configuration
central monitoring
```

---

# 9. Extraction Preparation

Document modules that may later become services.

For each candidate, track:

```text
module
reason for extraction
data ownership
external dependencies
scaling pressure
team ownership
risk
```

---

# 10. Final Principle

> A modular monolith should feel like a clean system internally and a simple system operationally.