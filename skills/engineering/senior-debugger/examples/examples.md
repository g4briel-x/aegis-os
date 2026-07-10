## FILE: `skills/engineering/senior-debugger/examples/examples.md`

# Senior Debugger — Examples

Version: 0.2.0  
Status: Premium Draft

---

# 1. Example — React Infinite Render

## User Request

My React component keeps re-rendering infinitely.

## Expected Skill Behavior

The Skill should:

- ask for or inspect the component;
- look for state updates inside render or effects;
- review dependency arrays;
- identify loop cause;
- provide corrected code;
- suggest verification steps.

## Expected Output Structure

```text
Facts
Likely cause
Corrected code
Verification steps
Prevention notes
```

---

# 2. Example — Node.js API 500 Error

## User Request

My Node.js API returns 500 when creating a user.

## Expected Skill Behavior

The Skill should:

- ask for logs or stack trace if missing;
- inspect validation and database insert logic;
- consider duplicate keys or missing required fields;
- provide targeted fix;
- recommend better error handling.

---

# 3. Example — SQL Query Wrong Results

## User Request

My SQL query returns duplicate customers.

## Expected Skill Behavior

The Skill should:

- inspect joins;
- detect one-to-many relationship expansion;
- recommend grouping, distinct or corrected join logic;
- explain the real cause.

---

# 4. Example — Failing CI Pipeline

## User Request

The build works locally but fails in GitHub Actions.

## Expected Skill Behavior

The Skill should:

- compare local and CI environments;
- inspect dependency versions;
- check environment variables;
- identify missing files or path differences;
- recommend reproducible fix.

---

# 5. Example — Production Regression

## User Request

After deployment, users cannot log in.

## Expected Skill Behavior

The Skill should:

- assess impact;
- check recent auth changes;
- check environment variables and session configuration;
- propose rollback or hotfix;
- define permanent prevention.

---

# 6. Final Principle

> Examples prove that the Skill can move from failure symptoms to verified correction.
