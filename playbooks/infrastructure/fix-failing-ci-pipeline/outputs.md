## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/outputs.md`

# Fix Failing CI Pipeline — Outputs

Version: 0.1.0  
Status: Premium Draft

---

# 1. CI Failure Diagnosis

Purpose:

Summarize the failed pipeline.

Required sections:

```text
Workflow:
Job:
Step:
Command:
Primary error:
Failure category:
```

---

# 2. Root Cause Summary

Purpose:

Explain why the pipeline failed.

Required sections:

```text
Likely root cause:
Evidence:
Recent change:
Confidence:
Unknowns:
```

---

# 3. Fix Recommendation

Purpose:

Define the correction.

Required sections:

```text
Fix:
Files or configuration affected:
Reason:
Risk:
Rollback:
```

---

# 4. Verification Steps

Purpose:

Confirm the pipeline has recovered.

Required sections:

```text
Command:
CI job:
Expected result:
Actual result:
Status:
```

---

# 5. Prevention Actions

Purpose:

Reduce recurrence.

Required sections:

```text
Action:
Owner:
Priority:
Reason:
Due:
```

---

# 6. Merge Readiness Note

Purpose:

State whether merge or release can continue.

Required sections:

```text
Required checks:
Current status:
Remaining blockers:
Decision:
```

---

# 7. Final Principle

> CI outputs should tell the team what failed, why, what fixed it and whether it is safe to continue.
