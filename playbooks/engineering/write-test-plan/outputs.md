## FILE: `playbooks/engineering/write-test-plan/outputs.md`

# Write Test Plan — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. Test Plan

Purpose:

Provide the complete validation plan.

Required sections:

```text
Feature:
Scope:
Non-scope:
Strategy:
Risks:
Test data:
Environment:
Approval criteria:
```

---

# 2. Test Case

Purpose:

Define a specific validation scenario.

Required sections:

```text
Test ID:
Scenario:
Precondition:
Steps:
Expected result:
Priority:
Evidence:
```

---

# 3. Regression Coverage

Purpose:

Protect existing behavior.

Required sections:

```text
Existing behavior:
Related feature:
Risk:
Test case:
Owner:
```

---

# 4. Permission Test Matrix

Purpose:

Validate role and access behavior.

Required sections:

```text
Role:
Action:
Resource:
Expected access:
Test result:
```

---

# 5. Test Data Requirements

Purpose:

Define data needed for validation.

Required sections:

```text
Data item:
Purpose:
Source:
Owner:
Privacy notes:
```

---

# 6. Release Validation Checklist

Purpose:

Support merge or release decision.

Required sections:

```text
Validation item:
Owner:
Status:
Evidence:
Decision:
```

---

# 7. Final Principle

> Test plan outputs must help QA, engineering and product agree on what “ready” means.