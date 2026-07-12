## FILE: `patterns/design/saas-onboarding-flow/solution.md`

# SaaS Onboarding Flow — Solution

Version: 0.1.0  
Status: Draft

---

# 1. Solution Overview

Design the onboarding flow around first value.

Recommended sequence:

```text
1. Define target user
2. Define activation moment
3. Identify required setup
4. Remove non-essential setup
5. Design guided first workflow
6. Create useful empty states
7. Add progress feedback
8. Track onboarding metrics
9. Test with real users
```

---

# 2. Target User

Define who is being onboarded.

Example:

```text
Independent producer preparing a film project for financing.
```

Avoid:

```text
Any creative professional.
```

A narrow target user makes onboarding clearer.

---

# 3. Setup Questions

Ask only what is needed to personalize or enable the first workflow.

Good questions:

```text
What type of project are you preparing?
What stage is the project in?
Do you already have pitch materials?
```

Avoid:

```text
long surveys
questions not used immediately
complex configuration before value
```

---

# 4. First Object Creation

Most SaaS onboarding should lead users to create the first meaningful object.

Examples:

```text
project
workspace
document
campaign
report
workflow
client record
```

The first object becomes the anchor of the user experience.

---

# 5. Guided First Workflow

Guide the user through the minimum valuable workflow.

Example:

```text
Create project
Add project title
Upload pitch deck
Complete financing checklist
Submit for readiness review
Receive next action
```

---

# 6. Empty State Guidance

Use empty states as onboarding surfaces.

Each empty state should include:

```text
context
benefit
primary action
example
support link if needed
```

---

# 7. Progress Model

Show progress when setup has multiple steps.

Example:

```text
Project setup: 3 of 5 steps complete
```

Progress should reflect meaningful completion, not arbitrary UI tasks.

---

# 8. Metrics

Track funnel events:

```text
signup_started
signup_completed
workspace_created
onboarding_started
first_object_created
first_workflow_completed
activation_completed
onboarding_abandoned
```

---

# 9. Final Principle

> The solution should make the next valuable action obvious at every moment.
