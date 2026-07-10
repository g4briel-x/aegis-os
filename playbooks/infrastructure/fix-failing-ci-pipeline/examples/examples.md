## FILE: `playbooks/infrastructure/fix-failing-ci-pipeline/examples/examples.md`

# Fix Failing CI Pipeline — Examples

Version: 0.1.0  
Status: Premium Draft

---

# 1. Example — Build Works Locally, Fails in CI

## Trigger

A Node.js project builds locally but fails in GitHub Actions.

## Expected Execution

The Playbook should guide the user to:

- identify failed command;
- compare Node.js and package manager versions;
- check lockfile;
- review missing environment variables;
- align CI configuration;
- rerun the workflow.

## Expected Output

```text
Failure diagnosis
Environment difference summary
Root cause
Fix recommendation
Verification steps
Prevention actions
```

---

# 2. Example — Tests Fail Only in CI

## Trigger

Unit tests pass locally but fail in CI.

## Expected Execution

The Playbook should guide the user to:

- inspect failed assertion;
- compare timezones, file paths and environment settings;
- check test order dependency;
- identify flaky behavior;
- add deterministic test setup.

---

# 3. Example — Dependency Install Failure

## Trigger

CI fails during package installation.

## Expected Execution

The Playbook should guide the user to:

- inspect package manager logs;
- check lockfile;
- check registry access;
- review dependency version changes;
- fix lockfile or install command.

---

# 4. Example — Deployment Check Fails

## Trigger

A deployment preview fails after CI build.

## Expected Execution

The Playbook should guide the user to:

- inspect deployment logs;
- check required secrets;
- check build output path;
- review environment-specific configuration;
- verify preview after fix.

---

# 5. Final Principle

> Examples show that CI troubleshooting requires evidence, environment comparison and verified recovery.
