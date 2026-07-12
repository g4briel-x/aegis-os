## FILE: `patterns/design/saas-onboarding-flow/context.md`

# SaaS Onboarding Flow — Context

Version: 0.1.0  
Status: Draft

---

# 1. Best-Fit Context

This Pattern fits SaaS products where user success depends on completing a first setup or workflow.

Typical contexts:

```text
new SaaS MVP
private beta
self-serve signup
trial activation
workspace SaaS
document platform
AI SaaS
B2B workflow SaaS
```

---

# 2. User Context

Use this Pattern when users need to:

- understand the product purpose;
- create an account;
- set up a workspace;
- choose a role;
- create a first object;
- invite collaborators;
- upload files;
- complete a workflow.

---

# 3. Product Context

The Pattern is useful when the product has:

```text
activation funnel
trial-to-paid conversion
guided setup
role-based experience
team collaboration
empty dashboards
usage-based value
```

---

# 4. Technical Context

The Pattern may require:

- event tracking;
- user profile fields;
- workspace model;
- progress state;
- templates or examples;
- feature flags;
- notification triggers;
- onboarding analytics.

---

# 5. Warning Signs

Onboarding is weak when:

- users sign up but do nothing;
- dashboards are empty without guidance;
- setup asks for data that is not used;
- onboarding cannot be measured;
- the first action is buried in navigation;
- activation is defined vaguely;
- support repeats the same onboarding explanation manually.

---

# 6. Final Principle

> Onboarding context should start with the user's job to be done, not the product's navigation.
