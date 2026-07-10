## FILE: `patterns/_framework/README.md`

# Aegis OS — Patterns Framework

Version: 0.1.0  
Status: Foundation Draft  
Domain: Patterns

---

# 1. Purpose

The Patterns Framework defines how reusable solution patterns are created, organized, reviewed and maintained inside Aegis OS.

A Pattern captures a proven structure for solving a recurring problem. It is less procedural than a Playbook and more reusable than a one-time document.

---

# 2. What a Pattern Provides

A Pattern should provide:

```text
Problem
Context
Forces
Recommended solution
Implementation guidance
Trade-offs
Risks
Examples
Validation checklist
Related skills and playbooks
```

---

# 3. Pattern Categories

Recommended categories:

```text
patterns/architecture
patterns/security
patterns/product
patterns/engineering
patterns/operations
patterns/business
patterns/design
```

---

# 4. Standard Pattern Structure

Each Pattern should use this structure:

```text
README.md
PATTERN.md
metadata.yaml
context.md
solution.md
trade-offs.md
checklists.md
examples/examples.md
```

---

# 5. Final Principle

> A Pattern should make a good solution reusable without pretending that every context is identical.