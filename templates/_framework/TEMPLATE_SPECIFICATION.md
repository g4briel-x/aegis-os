## FILE: `templates/_framework/TEMPLATE_SPECIFICATION.md`

# Template Specification

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This specification defines what qualifies as an Aegis OS Template.

A Template is a reusable output structure that helps generate consistent documents, plans, reports or artifacts.

---

# 2. Template Requirements

A valid Template must include:

```text
id
name
version
status
domain
category
purpose
inputs
variables
sections
output_rules
quality_checks
examples
related_skills
related_playbooks
related_patterns
```

---

# 3. Template Scope

Use a Template when:

- the same output is produced repeatedly;
- quality depends on structure;
- teams need a standard format;
- reviewers need consistent sections;
- automation may generate the output later.

Do not use a Template for:

- one-time notes;
- vague guidance;
- full execution procedures;
- decision models that belong in Patterns.

---

# 4. Template Quality Rules

A high-quality Template must be:

```text
clear
complete
structured
fillable
reviewable
domain-specific
easy to reuse
```

---

# 5. Final Principle

> A Template should standardize output shape while allowing context-specific content.