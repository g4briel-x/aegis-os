## FILE: `patterns/design/saas-onboarding-flow/examples/examples.md`

# SaaS Onboarding Flow — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Audiovisual Financing SaaS

## Context

A creator signs up to prepare a film, series or documentary project for financing.

## Onboarding Flow

```text
Signup
Choose project type
Create first project
Add title and logline
Upload pitch deck or treatment
Complete readiness checklist
Receive next action
```

## Activation Moment

```text
User receives a financing readiness checklist for the first project.
```

## Metrics

```text
project_created
document_uploaded
readiness_checklist_completed
activation_completed
time_to_activation
```

---

# 2. Example — B2B Workspace SaaS

## Flow

```text
Signup
Create workspace
Invite teammate
Create first workflow
Run first approval
```

## Activation Moment

```text
First approval workflow completed.
```

---

# 3. Example — AI Document Review SaaS

## Flow

```text
Signup
Upload document
Choose review type
Run AI review
View flagged clauses
Export summary
```

## Activation Moment

```text
User receives first AI review result.
```

---

# 4. Example — Empty State

Bad:

```text
No documents.
```

Better:

```text
Upload the first pitch document to start checking whether the project package is ready for financing review.
```

---

# 5. Final Principle

> Examples show that onboarding should move the user from intent to value through one clear path.
