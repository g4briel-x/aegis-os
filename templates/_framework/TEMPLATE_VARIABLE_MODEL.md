## FILE: `templates/_framework/TEMPLATE_VARIABLE_MODEL.md`

# Template Variable Model

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This document defines how variables and placeholders should be used in Aegis OS Templates.

---

# 2. Variable Format

Use double curly braces:

```text
{{variable_name}}
```

Examples:

```text
{{product_name}}
{{customer_segment}}
{{feature_name}}
{{incident_severity}}
{{api_endpoint}}
{{release_version}}
```

---

# 3. Variable Naming Rules

Variables should:

- use lowercase;
- use snake_case;
- describe the required value;
- avoid abbreviations unless common;
- avoid ambiguous names.

Good:

```text
{{target_segment}}
{{primary_user}}
{{business_goal}}
{{success_metric}}
```

Bad:

```text
{{x}}
{{thing}}
{{data}}
{{info}}
```

---

# 4. Required and Optional Variables

Each Template should classify variables:

```text
Required variables:
- {{project_name}}
- {{owner}}
- {{target_user}}

Optional variables:
- {{external_link}}
- {{supporting_notes}}
```

---

# 5. Variable Description Format

Use this format:

```text
Variable:
Purpose:
Required:
Example:
```

Example:

```text
Variable: {{target_segment}}
Purpose: Defines the customer group the output focuses on.
Required: Yes
Example: Independent film producers preparing projects for financing.
```

---

# 6. Final Principle

> Template variables should make completion obvious and automation reliable.
