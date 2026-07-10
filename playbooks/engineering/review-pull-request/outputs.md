## FILE: `playbooks/engineering/review-pull-request/outputs.md`

# Review Pull Request — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. PR Review Summary

Purpose:

Summarize the review result.

Required sections:

```text
PR:
Purpose:
Scope:
Review status:
Major findings:
Decision:
```

---

# 2. Review Findings

Purpose:

Document issues found during review.

Required sections:

```text
Finding:
Category:
Severity:
Evidence:
Recommended change:
```

---

# 3. Risk Notes

Purpose:

Make merge or release risk visible.

Required sections:

```text
Risk:
Impact:
Likelihood:
Mitigation:
Owner:
```

---

# 4. Test Review

Purpose:

Summarize validation coverage.

Required sections:

```text
Changed behavior:
Test coverage:
Missing tests:
CI status:
Manual validation:
```

---

# 5. Merge Readiness Decision

Purpose:

Record whether the PR should merge.

Required sections:

```text
Decision:
Reason:
Required changes:
Required reviewers:
Conditions:
```

---

# 6. Follow-Up Actions

Purpose:

Capture work that remains after review.

Required sections:

```text
Action:
Owner:
Priority:
Due:
Status:
```

---

# 7. Final Principle

> PR review outputs must be clear enough for the author to act and the team to trust the merge decision.