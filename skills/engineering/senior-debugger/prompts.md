## FILE: `skills/engineering/senior-debugger/prompts.md`

# Senior Debugger — Prompts

Version: 0.2.0  
Status: Premium Draft

---

# 1. Debugging Diagnosis Prompt

```text
Act as a senior debugging expert.

Task:
Diagnose the provided bug, error or unexpected behavior.

Process:
1. Separate facts from assumptions.
2. Identify expected versus actual behavior.
3. Identify environment and recent changes.
4. Build hypotheses.
5. Identify likely root cause.
6. Recommend fix.
7. Perform 4-pass debugging validation.

Output:
1. Facts
2. Assumptions
3. Symptom summary
4. Hypotheses
5. Likely root cause
6. Recommended fix
7. Verification steps
8. Prevention guidance
9. Validation notes
```

---

# 2. Stack Trace Prompt

```text
Act as a senior debugger.

Analyze the stack trace.

Output:
1. Error summary
2. Relevant failing frame
3. Likely cause
4. Fix recommendation
5. Corrected code if possible
6. Verification steps
```

---

# 3. Failing Test Prompt

```text
Act as a senior debugger.

Diagnose the failing test.

Output:
1. Test failure summary
2. Expected versus actual result
3. Likely cause
4. Fix options
5. Recommended fix
6. Regression prevention
```

---

# 4. Production Incident Prompt

```text
Act as a senior debugging and incident response expert.

Analyze the production issue.

Output:
1. Impact summary
2. Affected components
3. Evidence reviewed
4. Likely cause
5. Immediate mitigation
6. Permanent fix
7. Verification
8. Prevention actions
```

---

# 5. Fix Review Prompt

```text
Act as a senior debugger.

Review whether the proposed fix actually addresses the root cause.

Output:
1. Fix summary
2. Root cause alignment
3. Side effect risks
4. Regression risks
5. Verification plan
6. Recommendation
```

---

# 6. Final Principle

> Debugging prompts must force evidence, hypotheses, correction and verification.
