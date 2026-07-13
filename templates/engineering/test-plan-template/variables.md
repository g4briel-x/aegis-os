## FILE: `templates/engineering/test-plan-template/variables.md`

# Test Plan Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{change_name}}
{{product_area}}
{{owner}}
{{test_owner}}
{{status}}
{{summary}}
{{in_scope_item_1}}
{{test_objective_1}}
{{test_environment}}
{{functional_test_cases}}
{{exit_criteria}}
```

---

# 2. Optional Variables

```text
{{prd_link}}
{{api_contract_link}}
{{security_link}}
{{feature_flags}}
{{external_providers}}
{{performance_test_strategy}}
{{automation_gap_1}}
{{operations_approval}}
```

---

# 3. Variable Descriptions

## `{{change_name}}`

Purpose:

```text
Name of the feature, workflow, API or release being tested.
```

Example:

```text
Project Submission Workflow
```

---

## `{{test_environment}}`

Purpose:

```text
Environment where tests will be executed.
```

Example:

```text
staging
```

---

## `{{functional_test_cases}}`

Purpose:

```text
Functional scenarios that verify expected behavior.
```

Example:

```text
A creator can submit a completed project for review.
```

---

## `{{security_test_cases}}`

Purpose:

```text
Authorization, tenant isolation and sensitive-data tests.
```

Example:

```text
A user from workspace A cannot submit or read a project from workspace B.
```

---

# 4. Final Principle

> Test Plan variables should make quality expectations measurable.
