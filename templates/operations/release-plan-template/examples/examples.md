## FILE: `templates/operations/release-plan-template/examples/examples.md`

# Release Plan Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Project Submission Release

## Release Name

```text
Project Submission Release
```

## Release Summary

```text
This release enables creators to submit completed audiovisual project packages for readiness review.
```

## Included Changes

```text
Project submission API
Submission validation rules
Project submitted audit event
Reviewer assignment background job
Submission UI state
```

## Risk Level

```text
medium
```

## Risk Reason

```text
The release changes a critical project workflow and introduces a background job side effect, but it is protected by validation tests and a feature flag.
```

## Deployment Steps

```text
1. Deploy backend API changes.
2. Deploy frontend submission UI.
3. Enable feature flag for internal workspace.
4. Validate submission flow.
5. Enable feature flag for beta users.
```

## Validation Checks

```text
[ ] Creator can submit a complete project.
[ ] Missing required documents return validation_failed.
[ ] Audit event project.submitted is created.
[ ] Reviewer assignment job is queued.
[ ] Error rate remains below threshold.
```

## Rollback Trigger

```text
Submission error rate exceeds 5% for more than 5 minutes or project status updates fail.
```

## Rollback Method

```text
Disable project_submission_enabled feature flag and redeploy previous backend version if needed.
```

---

# 2. Example — Database Migration Release

```text
Migration included: Yes
Backward compatible: Yes
Backup required: Yes
Validation query: Count projects with missing readiness_score after backfill.
Rollback: Forward fix or restore affected records from backup if data integrity issue appears.
```

---

# 3. Example — Customer Communication

```text
This release adds the ability to submit complete project packages for readiness review. During beta, access is limited to selected workspaces.
```

---

# 4. Final Principle

> Examples show that a release plan must combine scope, deployment, validation and recovery.