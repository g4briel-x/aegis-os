## FILE: `templates/design/ux-flow-template/examples/examples.md`

# UX Flow Template — Examples

Version: 0.1.0  
Status: Draft

---

# 1. Example — Guided First Project Setup

## Flow Name

```text
Guided First Project Setup
```

## Primary User

```text
Independent film producer
```

## User Goal

```text
Create the first project and understand what materials are needed for financing readiness.
```

## Entry Point

```text
Empty dashboard after signup
```

## Flow Steps

```text
1. Empty dashboard | User clicks Create Project | System opens project setup form
2. Project setup | User enters title and project type | System validates required fields
3. Project materials | User uploads pitch deck or skips for later | System shows readiness checklist
4. Readiness checklist | User views missing items | System recommends next best action
```

## Successful Exit

```text
User reaches the first project readiness checklist.
```

## Activation Event

```text
first_project_created
```

---

# 2. Example — Error State

```text
If the user tries to continue without project title, show:
"Project title is required before continuing."
```

---

# 3. Example — Permission Denied

```text
If a workspace member without project.create permission tries to create a project, show:
"You do not have permission to create projects in this workspace."
```

---

# 4. Example — Analytics Events

```text
onboarding_create_project_clicked
first_project_created
readiness_checklist_viewed
onboarding_step_abandoned
```

---

# 5. Final Principle

> Examples show that a UX flow connects screen behavior, system rules and product activation.
