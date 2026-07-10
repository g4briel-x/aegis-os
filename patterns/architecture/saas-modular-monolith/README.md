## FILE: `patterns/architecture/saas-modular-monolith/README.md`

# SaaS Modular Monolith Pattern

Version: 0.1.0  
Status: Draft  
Domain: Architecture  
Category: SaaS Architecture

---

# 1. Purpose

The SaaS Modular Monolith Pattern defines a practical architecture for building early and mid-stage SaaS products with strong internal boundaries while avoiding premature microservices complexity.

It helps teams structure a SaaS application into clear modules for product, users, billing, projects, files, notifications, analytics and administration while keeping one deployable application and one operational runtime.

---

# 2. Problem

SaaS teams often split too early into microservices or keep everything in one unstructured codebase.

Both extremes create problems:

```text
Premature microservices increase infrastructure, deployment and coordination complexity.
Unstructured monoliths become hard to maintain, test and scale.
```

---

# 3. Recommended Solution

Build a modular monolith:

```text
one deployable application
clear internal modules
explicit boundaries
shared platform layer
centralized database with disciplined schemas
well-defined service interfaces
testable domain logic
future extraction paths
```

---

# 4. Recommended When

Use this Pattern when:

- the product is an MVP or early SaaS;
- the team is small or medium-sized;
- domain boundaries are still evolving;
- operational simplicity matters;
- deployment speed matters;
- product-market fit is not fully validated;
- future scale is expected but not immediate.

---

# 5. Avoid When

Avoid this Pattern when:

- independent service scaling is already required;
- teams are large and independently owning services;
- compliance requires hard runtime isolation;
- multiple systems already exist independently;
- the domain is stable and service boundaries are proven.

---

# 6. Related Assets

```text
Related skills:
engineering.software-architect
engineering.senior-developer
engineering.database-engineer
infrastructure.devops-engineer

Related playbooks:
engineering.design-saas-architecture
engineering.design-saas-data-model
engineering.create-api-contract
infrastructure.deploy-saas-application
```

---

# 7. Final Principle

> Start with one deployable system, but never with one tangled system.
