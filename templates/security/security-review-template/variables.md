## FILE: `templates/security/security-review-template/variables.md`

# Security Review Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{review_name}}
{{feature_or_system}}
{{review_owner}}
{{engineering_owner}}
{{security_reviewer}}
{{status}}
{{review_summary}}
{{security_risk_level}}
{{authentication_required}}
{{required_permission_1}}
{{tenant_boundary}}
{{data_involved}}
{{security_decision}}
```

---

# 2. Optional Variables

```text
{{target_release}}
{{file_upload_allowed}}
{{third_party_systems}}
{{webhook_verification}}
{{audit_retention}}
{{accepted_risks}}
{{follow_up_fixes_after_release}}
```

---

# 3. Variable Descriptions

## `{{review_name}}`

Purpose:

```text
Human-readable name of the security review.
```

Example:

```text
Project Submission Security Review
```

---

## `{{security_risk_level}}`

Purpose:

```text
Overall security risk classification.
```

Recommended values:

```text
low
medium
high
critical
```

---

## `{{tenant_boundary}}`

Purpose:

```text
Rule that prevents data or action crossing tenant boundaries.
```

Example:

```text
Project workspace_id must match the authenticated user's active workspace.
```

---

## `{{security_decision}}`

Purpose:

```text
Final security release decision.
```

Recommended values:

```text
approved
approved_with_conditions
blocked
needs_more_review
```

---

# 4. Final Principle

> Security Review variables should make risk, ownership and release decision explicit.
