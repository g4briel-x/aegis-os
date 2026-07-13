## FILE: `templates/product/prd-template/variables.md`

# PRD Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{feature_name}}
{{product_area}}
{{owner}}
{{status}}
{{summary}}
{{problem_statement}}
{{primary_user}}
{{goals}}
{{non_goals}}
{{functional_requirements}}
{{acceptance_criteria}}
{{success_metric}}
```

---

# 2. Optional Variables

```text
{{contributors}}
{{target_release}}
{{secondary_users}}
{{buyer}}
{{admin_user}}
{{api_endpoint}}
{{api_method}}
{{api_request}}
{{api_response}}
{{audit_events}}
{{feature_flag_needed}}
{{rollout_plan}}
{{rollback_plan}}
```

---

# 3. Variable Descriptions

## `{{feature_name}}`

Purpose:

```text
Name of the feature or product initiative.
```

Example:

```text
Project Readiness Review
```

---

## `{{problem_statement}}`

Purpose:

```text
Clear description of the user or business problem.
```

Example:

```text
Independent producers struggle to know whether their project package is ready for financing discussions.
```

---

## `{{primary_user}}`

Purpose:

```text
Main user who will use the feature.
```

Example:

```text
Independent film producer
```

---

## `{{functional_requirements}}`

Purpose:

```text
System behaviors that must be implemented.
```

Example:

```text
The system must allow a creator to submit a completed project for readiness review.
```

---

## `{{acceptance_criteria}}`

Purpose:

```text
Testable conditions that define feature completion.
```

Example:

```text
Given a creator has completed all required project fields, when they submit the project, then the project status changes to submitted.
```

---

## `{{success_metric}}`

Purpose:

```text
Metric used to evaluate whether the feature achieved its goal.
```

Example:

```text
At least 60% of beta creators submit one project within 7 days of signup.
```

---

# 4. Final Principle

> PRD variables should make product intent explicit before requirements are written.
