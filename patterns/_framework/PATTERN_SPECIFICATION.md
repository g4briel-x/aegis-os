## FILE: `patterns/_framework/PATTERN_SPECIFICATION.md`

# Pattern Specification

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This specification defines what qualifies as an Aegis OS Pattern.

A Pattern is a reusable solution model for a recurring problem. It explains when to use the solution, how it works, what trade-offs it creates and how to validate it.

---

# 2. Pattern Requirements

A valid Pattern must include:

```text
id
name
version
status
domain
category
problem
context
recommended_solution
trade_offs
risks
validation
examples
related_skills
related_playbooks
```

---

# 3. Pattern Scope

A Pattern should be used when:

- the same problem appears across projects;
- the solution is reusable;
- the decision involves trade-offs;
- implementation must be adapted to context;
- teams need a reference model before execution.

A Pattern should not be used for:

- one-time tasks;
- raw instructions without reasoning;
- generic advice without structure;
- full procedures better suited for Playbooks.

---

# 4. Pattern Quality Rules

A high-quality Pattern must be:

```text
specific
context-aware
actionable
trade-off explicit
validated
reusable
easy to reference
```

---

# 5. Final Principle

> A Pattern should capture reusable judgment, not just reusable text.
