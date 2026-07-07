# Aegis OS — Naming Conventions

Version: 0.1  
Status: Reference Document

---

# 1. Introduction

This document defines the naming standards used across Aegis OS.

The objective is to ensure:

- consistency;
- readability;
- discoverability;
- automation compatibility.

---

# 2. General Naming Principles

All names must be:

- descriptive;
- predictable;
- lowercase when possible;
- easy to understand;
- consistent across the ecosystem.

Avoid:

- unclear abbreviations;
- personal naming styles;
- temporary names.

---

# 3. Directory Naming

Directories use:
kebab-case


Format:


word-word


Examples:

Correct:


software-architect
product-manager
security-engineer


Incorrect:


SoftwareArchitect
software_architect
SA


---

# 4. File Naming

Markdown files use:


UPPER_SNAKE_CASE.md


Examples:


SYSTEM_ARCHITECTURE.md

QUALITY_MODEL.md

CHANGE_MANAGEMENT.md


---

# 5. Skill Naming

Skills use:


domain/role-name


Examples:


engineering/software-architect

product/product-manager-saas

infrastructure/cloud-architect


Rules:

- clear professional role;
- no personal names;
- no version number in directory name.

---

# 6. Playbook Naming

Playbooks use:


action-purpose


Examples:


architecture-review

incident-response

product-discovery


The name should describe the activity.

---

# 7. Pattern Naming

Patterns use:


concept-name


Examples:


event-driven-architecture

repository-pattern

continuous-delivery


---

# 8. Template Naming

Templates use:


artifact-type-template


Examples:


architecture-document-template

technical-report-template

product-requirement-template


---

# 9. Component Naming

Software components should use:


lowercase-kebab-case


Examples:


orchestration-engine

knowledge-manager

validation-service


---

# 10. Version Naming

Versions follow:


MAJOR.MINOR.PATCH


Examples:


1.0.0

2.3.1


Pre-release versions:


1.0.0-alpha

1.0.0-beta

1.0.0-rc.1


---

# 11. Metadata Naming

Configuration fields use:


snake_case


Example:

```yaml
skill_name: software_architect
version_number: 1.0.0
12. Identifier Naming

Internal identifiers should be:

unique;
stable;
machine readable.

Example:

id: skill.engineering.software_architect


13. Forbidden Naming Practices

Avoid:

Generic Names

Bad:
new-folder
test
temp
Personal Names

Bad:
john-skill
my-version
Ambiguous Names

Bad:
manager2
advanced
final


14. Migration Rules

When renaming existing components:

Required:
- migration note;
- reference update;
- compatibility check.

15. Naming Validation Checklist
[ ] Naming convention respected
[ ] Purpose is clear
[ ] No ambiguity
[ ] Compatible with automation
[ ] Documentation updated

16. Final Principle
Good naming creates a shared language that allows humans and machines to understand the Aegis OS ecosystem.