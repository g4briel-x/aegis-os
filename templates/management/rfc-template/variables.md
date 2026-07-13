## FILE: `templates/management/rfc-template/variables.md`

# RFC Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{rfc_title}}
{{rfc_id}}
{{author}}
{{owner}}
{{status}}
{{summary}}
{{problem_statement}}
{{goal_1}}
{{non_goal_1}}
{{proposal_detail}}
{{recommended_option}}
{{decision}}
```

---

# 2. Optional Variables

```text
{{target_decision_date}}
{{reviewers}}
{{feature_flag_required}}
{{migration_required}}
{{leadership_approval}}
{{external_dependencies}}
{{rollback_or_recovery}}
```

---

# 3. Variable Descriptions

## `{{rfc_title}}`

Purpose:

```text
Human-readable title of the proposal.
```

Example:

```text
Adopt Feature Flag Rollout for Risky Releases
```

---

## `{{problem_statement}}`

Purpose:

```text
Problem or opportunity that justifies the proposal.
```

Example:

```text
Current releases activate features immediately for all users, making risky changes harder to control and roll back.
```

---

## `{{proposal_detail}}`

Purpose:

```text
Detailed explanation of the proposed change.
```

Example:

```text
Introduce a standard feature flag rollout process for all customer-facing features.
```

---

## `{{decision}}`

Purpose:

```text
Final decision after review.
```

Recommended values:

```text
approved
approved_with_changes
rejected
deferred
needs_more_review
```

---

# 4. Final Principle

> RFC variables should make the proposal, decision and ownership explicit.
