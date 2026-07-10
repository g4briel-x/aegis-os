## FILE: `patterns/architecture/saas-modular-monolith/trade-offs.md`

# SaaS Modular Monolith — Trade-Offs

Version: 0.1.0  
Status: Draft

---

# 1. Benefits

The Pattern improves:

```text
development speed
deployment simplicity
operational cost
debugging simplicity
transaction management
early product iteration
team coordination
```

---

# 2. Costs

The Pattern can increase risk of:

```text
internal coupling
unclear module ownership
large deployable artifact
shared database complexity
boundary erosion over time
harder independent scaling
```

---

# 3. Compared to Microservices

Modular monolith is better when:

- domain boundaries are not stable;
- team is small;
- infrastructure maturity is limited;
- speed matters more than independent scaling.

Microservices may be better when:

- teams are independent;
- services need independent deployment;
- scaling pressure is domain-specific;
- isolation is legally or operationally required.

---

# 4. Compared to Unstructured Monolith

Modular monolith is better because it adds:

- boundaries;
- module ownership;
- testability;
- extraction paths;
- clearer architecture.

Unstructured monolith may be faster for a prototype, but becomes costly quickly.

---

# 5. Risks

Key risks:

```text
modules become folders only, not real boundaries
shared layer becomes dumping ground
database relationships create hidden coupling
all changes require full regression
team ignores architecture rules under pressure
```

---

# 6. Mitigations

Mitigate with:

- architecture review;
- module ownership documentation;
- code review checklist;
- import rules;
- module tests;
- data ownership model;
- periodic boundary audit.

---

# 7. Final Principle

> The main risk of a modular monolith is not being monolithic. The main risk is not being modular.