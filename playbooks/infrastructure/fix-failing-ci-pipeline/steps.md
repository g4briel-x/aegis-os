## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/steps.md`

# Fix Failing CI Pipeline — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Identify the Failed Check

Locate the exact failure.

Capture:

- workflow name;
- job name;
- failed step;
- branch;
- commit SHA;
- triggered event;
- runner environment.

Output:

```text
Failed CI check summary
```

---

# 2. Step 2 — Read the First Meaningful Error

Find the first error that explains the failure.

Avoid relying only on the final failure line.

Review:

- first exception;
- first compilation error;
- failed assertion;
- missing command;
- permission error;
- dependency error;
- environment variable error.

Output:

```text
Primary error summary
```

---

# 3. Step 3 — Classify the Failure

Classify the failure type.

Common categories:

- dependency install failure;
- lint or formatting failure;
- typecheck failure;
- unit test failure;
- integration test failure;
- build failure;
- deployment failure;
- secret or environment failure;
- permission failure;
- flaky infrastructure failure.

Output:

```text
Failure category
```

---

# 4. Step 4 — Compare Local and CI Environments

Identify differences between local execution and CI execution.

Compare:

- operating system;
- runtime version;
- package manager version;
- lockfile status;
- environment variables;
- working directory;
- file paths;
- cache state;
- dependency versions.

Output:

```text
Local versus CI difference summary
```

---

# 5. Step 5 — Review Recent Changes

Check what changed before the failure.

Review:

- code commits;
- package changes;
- lockfile changes;
- CI workflow changes;
- environment variable changes;
- test changes;
- build configuration changes.

Output:

```text
Recent change analysis
```

---

# 6. Step 6 — Build and Rank Hypotheses

Create likely explanations.

For each hypothesis, capture:

- suspected cause;
- evidence;
- contradicting evidence;
- validation method;
- fix option.

Output:

```text
Ranked CI failure hypotheses
```

---

# 7. Step 7 — Apply Minimal Safe Fix

Fix the root cause with the smallest safe change.

Possible fixes:

- update workflow command;
- install missing dependency;
- align runtime version;
- update lockfile;
- fix failing test;
- add missing environment variable;
- correct path or working directory;
- clear or adjust cache;
- repair build configuration.

Output:

```text
Selected fix
```

---

# 8. Step 8 — Re-Run and Verify

Confirm the fix works.

Verification methods:

- rerun failed job;
- run equivalent command locally;
- run full CI if risk is high;
- verify downstream jobs;
- check deployment preview if relevant.

Output:

```text
CI verification result
```

---

# 9. Step 9 — Document Prevention

Record how to reduce recurrence.

Examples:

- pin runtime versions;
- document required secrets;
- add pre-commit checks;
- improve CI error messages;
- add caching rules;
- add test stability improvements;
- split long workflows;
- update contributor guide.

Output:

```text
Prevention actions
```

---

# 10. Final Principle

> CI troubleshooting should follow the failing step backward to the real cause, not forward into random fixes.