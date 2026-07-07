# Aegis OS — Directory Structure Reference

Version: 0.1  
Status: Reference Document

---

# 1. Introduction

This document defines the official directory organization of Aegis OS.

The objective is to maintain:

- clear separation of responsibilities;
- predictable navigation;
- scalable growth;
- maintainable architecture.

---

# 2. Root Structure

The Aegis OS repository follows:
aegis-os/

├── core/
├── skills/
├── playbooks/
├── patterns/
├── templates/
├── knowledge/
├── tools/
├── agents/
├── workflows/
├── docs/
├── scripts/
├── tests/
└── config/


---

# 3. Core Directory

Purpose:

Contains the fundamental execution components.

Structure:


core/

├── engine/
├── orchestration/
├── reasoning/
├── memory/
└── validation/


Contains:

- execution logic;
- system services;
- internal mechanisms.

---

# 4. Skills Directory

Purpose:

Contains professional expertise modules.

Structure:


skills/

├── engineering/
├── product/
├── design/
├── infrastructure/
├── security/
└── management/


Example:


skills/engineering/software-architect/


---

# 5. Playbooks Directory

Purpose:

Contains operational procedures.

Structure:


playbooks/

├── engineering/
├── product/
├── operations/
└── management/


Example:


playbooks/engineering/code-review/


---

# 6. Patterns Directory

Purpose:

Contains reusable solution models.

Structure:


patterns/

├── architecture/
├── development/
├── security/
├── product/
└── operations/


---

# 7. Templates Directory

Purpose:

Contains standardized output structures.

Structure:


templates/

├── documents/
├── reports/
├── specifications/
├── presentations/
└── analysis/


---

# 8. Knowledge Directory

Purpose:

Stores reusable knowledge assets.

Structure:


knowledge/

├── concepts/
├── references/
├── examples/
├── research/
└── lessons-learned/


---

# 9. Agents Directory

Purpose:

Contains specialized AI agents.

Structure:


agents/

├── analysts/
├── architects/
├── reviewers/
├── validators/
└── coordinators/


---

# 10. Workflows Directory

Purpose:

Contains system workflows.

Structure:


workflows/

├── creation/
├── validation/
├── deployment/
└── maintenance/


---

# 11. Documentation Directory

Purpose:

Contains system documentation.

Structure:


docs/

├── 01-foundation/
├── 02-architecture/
├── 03-specifications/
├── 04-governance/
└── 05-reference/


---

# 12. Scripts Directory

Purpose:

Contains automation scripts.

Examples:


scripts/

├── generators/
├── validators/
├── migrations/
└── utilities/


---

# 13. Tests Directory

Purpose:

Contains validation systems.

Structure:


tests/

├── unit/
├── integration/
├── quality/
└── benchmark/


---

# 14. Configuration Directory

Purpose:

Contains system configuration.

Structure:


config/

├── environments/
├── schemas/
├── defaults/
└── policies/


---

# 15. Naming Conventions

Rules:

- lowercase names;
- use hyphen separator;
- descriptive names;
- avoid abbreviations.

Examples:

Correct:
software-architect


Incorrect:
SoftArch


---

# 16. Expansion Rules

New directories must:

- have a defined purpose;
- follow architecture principles;
- avoid duplication;
- be documented.

---

# 17. Final Principle

> A clear structure is the foundation that allows Aegis OS to scale without losing control.