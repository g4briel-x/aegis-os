# Aegis OS execution foundation

Version: v0.7.0
Status: controlled execution foundation

The execution layer resolves registered assets and prepares explainable,
auditable work before any action is considered.

```text
Python CLI
    |
    v
Planner and contract validator
    |
    v
Context and session workspace
    |
    v
Orchestration, lifecycle and audit journal
```

Current capabilities include plans, dry-runs, typed contracts, input
resolution, persisted sessions, orchestration state, terminal lifecycle
transitions and cryptographic audit verification.

```console
aegis --repo-root . execution plan security.review-api-security
aegis --repo-root . execution dry-run security.review-api-security
aegis --repo-root . execution contract security.review-api-security
aegis --repo-root . execution context security.review-api-security
```

Planning and dry-run commands do not execute real actions. Persisted state is
confined to the runtime workspace configured for the repository. Every state
transition must remain explainable and auditable.
