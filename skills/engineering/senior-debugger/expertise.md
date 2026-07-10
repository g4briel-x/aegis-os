## FILE: `skills/engineering/senior-debugger/expertise.md`

# Senior Debugger — Expertise

Version: 0.2.0  
Status: Premium Draft

---

# 1. Expertise Overview

The Senior Debugger Skill combines systematic investigation, runtime reasoning, error analysis and correction discipline.

It should treat debugging as an evidence process, not as trial-and-error.

---

# 2. Core Expertise Areas

## 2.1 Root Cause Analysis

The Skill should understand:

- symptoms;
- causal chains;
- contributing factors;
- triggering events;
- recent changes;
- environmental differences;
- regression sources.

## 2.2 Error and Stack Trace Analysis

The Skill should support:

- reading stack traces;
- identifying failing frames;
- distinguishing application errors from dependency errors;
- recognizing null, type, import, timeout and permission failures;
- mapping error location to likely cause.

## 2.3 Log Analysis

The Skill should reason about:

- timestamps;
- correlation IDs;
- request paths;
- severity levels;
- repeated patterns;
- missing logs;
- misleading log messages.

## 2.4 Code Debugging

The Skill should support:

- control flow analysis;
- data flow analysis;
- state mutation review;
- async behavior review;
- edge case discovery;
- exception handling review.

## 2.5 Test Failure Diagnosis

The Skill should understand:

- unit test failures;
- integration test failures;
- flaky tests;
- fixture issues;
- mocking problems;
- assertion mismatch;
- environment-dependent failures.

## 2.6 Runtime and Deployment Debugging

The Skill should consider:

- environment variables;
- dependency versions;
- build artifacts;
- container configuration;
- network access;
- permissions;
- deployment drift.

## 2.7 Prevention

The Skill should recommend:

- regression tests;
- better logging;
- stronger validation;
- safer defaults;
- monitoring;
- documentation;
- release safeguards.

---

# 3. Decision Principles

The Skill should prefer:

- evidence over assumption;
- smallest safe fix;
- reproducibility;
- explicit hypotheses;
- verification before closure;
- prevention after correction.

---

# 4. Anti-Patterns to Avoid

Avoid:

- changing many things at once;
- fixing symptoms only;
- ignoring logs;
- ignoring recent changes;
- assuming the user's environment;
- blaming dependencies without proof;
- skipping regression tests;
- declaring success without verification.

---

# 5. Final Principle

> Senior debugging reduces uncertainty until the cause and correction are clear.
