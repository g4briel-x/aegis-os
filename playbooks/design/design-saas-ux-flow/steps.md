## FILE: `playbooks/design/design-saas-ux-flow/steps.md`

# Design SaaS UX Flow — Steps

Version: 0.1.0  
Status: Premium Draft

---

# 1. Step 1 — Define the User Goal

Clarify what the user is trying to accomplish.

Capture:

- primary user;
- task;
- desired outcome;
- motivation;
- success condition.

Output:

```text
User goal statement
```

---

# 2. Step 2 — Identify Roles and Permissions

Define who can access or perform actions in the flow.

Review:

- primary role;
- secondary roles;
- admin role;
- viewer role;
- permission limits;
- restricted actions.

Output:

```text
Role and permission summary
```

---

# 3. Step 3 — Define Entry Points

Identify how the user enters the flow.

Possible entry points:

- dashboard card;
- sidebar menu;
- notification;
- email link;
- onboarding step;
- search result;
- direct URL;
- admin action.

Output:

```text
Entry point list
```

---

# 4. Step 4 — Map the Happy Path

Define the simplest successful path from start to completion.

Capture:

- first screen;
- main action;
- required input;
- system response;
- confirmation;
- final state.

Output:

```text
Happy path flow
```

---

# 5. Step 5 — Identify Required Screens

List screens needed to support the flow.

Typical screen types:

- list view;
- detail view;
- create form;
- edit form;
- review screen;
- confirmation screen;
- empty state;
- error state;
- settings screen.

Output:

```text
Screen inventory
```

---

# 6. Step 6 — Define Screen States

For each screen, define the necessary states.

Common states:

- default;
- loading;
- empty;
- error;
- success;
- disabled;
- permission denied;
- validation error;
- partial data.

Output:

```text
Screen state list
```

---

# 7. Step 7 — Map Edge Cases

Identify where the flow may break or branch.

Examples:

- missing data;
- expired session;
- permission denied;
- failed upload;
- duplicate submission;
- network error;
- invalid form input;
- unsaved changes;
- unavailable third-party service.

Output:

```text
Edge case map
```

---

# 8. Step 8 — Define System Feedback

Clarify how the product communicates progress, success or failure.

Consider:

- inline validation;
- toast messages;
- modal confirmations;
- progress indicators;
- error explanations;
- next action guidance.

Output:

```text
Feedback behavior notes
```

---

# 9. Step 9 — Review Friction and Usability

Identify unnecessary complexity.

Review:

- number of steps;
- repeated input;
- unclear labels;
- missing defaults;
- excessive confirmation;
- hidden actions;
- weak navigation;
- poor recovery paths.

Output:

```text
UX friction review
```

---

# 10. Step 10 — Produce UX Handoff

Prepare flow documentation for design and engineering.

Include:

- flow summary;
- screens;
- states;
- roles;
- edge cases;
- open questions;
- acceptance notes.

Output:

```text
UX flow handoff
```

---

# 11. Final Principle

> UX flow steps should make the user path visible before interface details distract the team.