## FILE: `skills/engineering/senior-debugger/workflows.md`

# Senior Debugger — Workflows

Version: 0.2.0  
Status: Premium Draft

---

# 1. General Debugging Workflow

Use this workflow for any bug or unexpected behavior.

```text
1. Capture the symptom
2. Capture expected versus actual behavior
3. Identify environment and recent changes
4. Gather evidence from code, logs or errors
5. Build hypotheses
6. Test or rank hypotheses
7. Identify root cause
8. Propose fix
9. Verify fix
10. Recommend prevention
```

---

# 2. Error Message Workflow

Use this workflow when the user provides an error message.

```text
1. Read the exact error
2. Identify error type
3. Locate failing component
4. Identify likely cause
5. Match cause to code or configuration
6. Provide correction
7. Provide verification steps
8. Explain prevention
```

---

# 3. Stack Trace Workflow

Use this workflow when a stack trace is available.

```text
1. Identify the top-level failure
2. Locate the first relevant application frame
3. Trace the call path
4. Identify invalid input, state or dependency
5. Recommend targeted fix
6. Validate against expected behavior
```

---

# 4. Failing Test Workflow

Use this workflow when tests fail.

```text
1. Identify failing test
2. Read assertion failure
3. Compare expected and actual values
4. Check setup and fixtures
5. Check recent code changes
6. Identify whether test or implementation is wrong
7. Provide fix
8. Suggest regression coverage
```

---

# 5. Production Incident Debugging Workflow

Use this workflow when the issue affects live users.

```text
1. Assess impact
2. Identify affected services
3. Check recent deployments or configuration changes
4. Review logs and metrics
5. Contain impact if needed
6. Identify likely root cause
7. Recommend safe mitigation
8. Define permanent fix and prevention
```

---

# 6. 4-Pass Debugging Validation Workflow

Every debugging output must be reviewed using this workflow:

```text
Pass 1 — Symptom, error and context review
Pass 2 — Hypothesis and root cause review
Pass 3 — Fix safety, side effect and regression review
Pass 4 — Verification, prevention and communication review
```

---

# 7. Final Principle

> Debugging workflow is complete only when the fix is verified and recurrence risk is reduced.