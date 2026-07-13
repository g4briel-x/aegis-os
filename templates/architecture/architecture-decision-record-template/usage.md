## FILE: `templates/architecture/architecture-decision-record-template/variables.md`

# Architecture Decision Record Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{adr_title}}
{{adr_id}}
{{status}}
{{decision_owner}}
{{decision_date}}
{{decision_summary}}
{{context}}
{{problem_statement}}
{{decision_driver_1}}
{{option_1_name}}
{{option_1_description}}
{{chosen_option}}
{{decision_reason}}
```

---

# 2. Optional Variables

```text
{{review_date}}
{{related_system}}
{{related_release}}
{{migration_required}}
{{feature_flag_required}}
{{operational_change_required}}
{{security_approval}}
{{product_approval}}
```

---

# 3. Variable Descriptions

## `{{adr_title}}`

Purpose:

```text
Human-readable name of the architectural decision.
```

Example:

```text
Use Modular Monolith for SaaS MVP
```

---

## `{{decision_summary}}`

Purpose:

```text
Short explanation of the decision.
```

Example:

```text
The MVP will use a modular monolith to reduce operational complexity while preserving internal domain boundaries.
```

---

## `{{problem_statement}}`

Purpose:

```text
Clear statement of the decision problem.
```

Example:

```text
The team needs to choose an architecture that supports fast MVP delivery without creating unmanageable technical debt.
```

---

## `{{chosen_option}}`

Purpose:

```text
Option selected after comparison.
```

Example:

```text
Modular monolith
```

---

# 4. Final Principle

> ADR variables should make the decision, reasoning and consequences explicit.
