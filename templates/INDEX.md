# Aegis OS — Templates Index Bundle

Ce fichier regroupe le document d’index global des Templates :

- `templates/INDEX.md`

---

## FILE: `templates/INDEX.md`

# Aegis OS — Templates Index

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This index lists the reusable Templates available in Aegis OS.

A Template is a reusable output structure used to produce consistent documents, plans, reports and artifacts.

Templates are different from Skills, Playbooks and Patterns:

```text
Template = reusable output format
Skill = expert capability
Playbook = step-by-step execution procedure
Pattern = reusable decision model and trade-offs
```

---

# 2. Template Framework

The Templates Framework defines how reusable Templates are created, structured, reviewed and maintained.

```text
templates/_framework/README.md
templates/_framework/TEMPLATE_SPECIFICATION.md
templates/_framework/TEMPLATE_DIRECTORY_STRUCTURE.md
templates/_framework/TEMPLATE_METADATA_SCHEMA.md
templates/_framework/TEMPLATE_AUTHORING_GUIDE.md
templates/_framework/TEMPLATE_VARIABLE_MODEL.md
templates/_framework/TEMPLATE_QUALITY_GATE.md
templates/_framework/TEMPLATE_REVIEW_CHECKLIST.md
templates/_framework/TEMPLATE_VERSIONING.md
templates/_framework/TEMPLATE_TEMPLATE.md
```

Purpose:

```text
Provides standards for authoring reusable output formats with variables, usage instructions, checklists and examples.
```

---

# 3. Product Templates

## 3.1 PRD Template

```text
templates/product/prd-template
```

Role:

```text
Creates Product Requirements Documents that clarify product problem, goals, users, scope, requirements, acceptance criteria, metrics and release readiness.
```

Recommended for:

```text
new SaaS features
MVP requirements
workflow specification
engineering handoff
design alignment
```

Related assets:

```text
playbooks/product/create-prd
playbooks/product/define-saas-mvp
patterns/product/saas-mvp-scope
patterns/design/saas-onboarding-flow
skills/product/product-manager-saas
```

---

# 4. Engineering Templates

## 4.1 API Contract Template

```text
templates/engineering/api-contract-template
```

Role:

```text
Documents API endpoint behavior, request schema, response schema, errors, authorization, versioning, side effects, observability and test cases.
```

Recommended for:

```text
REST APIs
frontend-backend contracts
external integrations
API security review
API testing
```

---

## 4.2 Test Plan Template

```text
templates/engineering/test-plan-template
```

Role:

```text
Plans how a feature, API, workflow, release or system change will be tested before production.
```

Recommended for:

```text
feature testing
API testing
regression testing
security-sensitive changes
release readiness
```

---

## 4.3 Data Model Template

```text
templates/engineering/data-model-template
```

Role:

```text
Documents SaaS entities, fields, relationships, constraints, ownership, tenant boundaries, permissions, audit events and migration risks.
```

Recommended for:

```text
database design
schema changes
domain modeling
tenant-scoped data
API persistence models
```

---

# 5. Operations Templates

## 5.1 Runbook Template

```text
templates/operations/runbook-template
```

Role:

```text
Documents repeatable operational procedures for production support, deployments, maintenance, recovery and incident response.
```

Recommended for:

```text
production operations
incident procedures
deployment steps
recovery processes
support escalation
```

---

## 5.2 Postmortem Template

```text
templates/operations/postmortem-template
```

Role:

```text
Analyzes incidents after resolution by documenting impact, timeline, root cause, response, lessons and corrective actions.
```

Recommended for:

```text
SEV1 incidents
customer-visible SEV2 incidents
security incidents
data integrity issues
deployment failures
```

---

## 5.3 Incident Report Template

```text
templates/operations/incident-report-template
```

Role:

```text
Creates a factual operational record during or shortly after an incident, including current status, severity, impact, timeline, actions and next steps.
```

Recommended for:

```text
active incidents
customer-visible outages
degraded workflows
support updates
management reporting
```

---

## 5.4 Release Plan Template

```text
templates/operations/release-plan-template
```

Role:

```text
Plans production releases with scope, risk, dependencies, testing, deployment steps, validation, rollback, monitoring and communication.
```

Recommended for:

```text
production releases
feature flag rollouts
database migrations
security-sensitive releases
customer-facing changes
```

---

# 6. Architecture Templates

## 6.1 Architecture Decision Record Template

```text
templates/architecture/architecture-decision-record-template
```

Role:

```text
Records important technical decisions with context, options, trade-offs, consequences, risks and follow-up actions.
```

Recommended for:

```text
architecture decisions
technology choices
database decisions
API versioning decisions
security design decisions
```

---

# 7. Security Templates

## 7.1 Security Review Template

```text
templates/security/security-review-template
```

Role:

```text
Reviews features, APIs, data models, integrations and releases for authentication, authorization, tenant isolation, data protection, audit logging and abuse risks.
```

Recommended for:

```text
sensitive data
permission changes
tenant-scoped data
new APIs
file uploads
billing or identity changes
```

---

# 8. Business Templates

## 8.1 Go-To-Market Plan Template

```text
templates/business/go-to-market-plan-template
```

Role:

```text
Plans how a SaaS product, MVP, pilot or feature reaches customers through target segment, ICP, positioning, messaging, offer, channels, funnel and metrics.
```

Recommended for:

```text
SaaS launch
paid pilot
MVP launch
market positioning
customer acquisition
```

---

## 8.2 Pricing Strategy Template

```text
templates/business/pricing-strategy-template
```

Role:

```text
Defines SaaS pricing strategy, plans, value metric, packaging, trials, paid pilots, discounts, validation and billing implementation needs.
```

Recommended for:

```text
SaaS pricing
subscription design
paid pilots
plan packaging
willingness-to-pay validation
```

---

# 9. Design Templates

## 9.1 UX Flow Template

```text
templates/design/ux-flow-template
```

Role:

```text
Documents how a user moves through a SaaS workflow from entry point to outcome, including screens, states, actions, permissions, errors and analytics.
```

Recommended for:

```text
onboarding flows
multi-screen workflows
feature UX design
engineering handoff
QA journey testing
```

---

# 10. Management Templates

## 10.1 RFC Template

```text
templates/management/rfc-template
```

Role:

```text
Documents significant proposals before decision, including problem, goals, options, impacts, risks, rollout plan, decision and follow-up actions.
```

Recommended for:

```text
major product changes
technical proposals
governance changes
breaking changes
cross-team decisions
```

---

# 11. Standard Template Structure

Every premium Template should follow this structure:

```text
README.md
TEMPLATE.md
metadata.yaml
variables.md
usage.md
checklists.md
examples/examples.md
```

---

# 12. Template Completion Status

```yaml
templates:
  framework: complete

  product:
    prd_template: complete

  engineering:
    api_contract_template: complete
    test_plan_template: complete
    data_model_template: complete

  operations:
    runbook_template: complete
    postmortem_template: complete
    incident_report_template: complete
    release_plan_template: complete

  architecture:
    architecture_decision_record_template: complete

  security:
    security_review_template: complete

  business:
    go_to_market_plan_template: complete
    pricing_strategy_template: complete

  design:
    ux_flow_template: complete

  management:
    rfc_template: complete
```

---

# 13. Recommended Usage Order for a SaaS Feature

For a new SaaS feature, use Templates in this order:

```text
1. product/prd-template
2. design/ux-flow-template
3. engineering/data-model-template
4. engineering/api-contract-template
5. security/security-review-template
6. engineering/test-plan-template
7. operations/release-plan-template
8. operations/runbook-template if operational procedure is needed
9. operations/incident-report-template if incident occurs
10. operations/postmortem-template if major incident occurs
```

---

# 14. Recommended Usage Order for a SaaS Launch

For a SaaS launch, use Templates in this order:

```text
1. business/go-to-market-plan-template
2. business/pricing-strategy-template
3. product/prd-template
4. design/ux-flow-template
5. engineering/data-model-template
6. security/security-review-template
7. operations/release-plan-template
```

---

# 15. Governance Notes

A Template should be reviewed when:

```text
the output format becomes unclear
the domain process changes
reviewers repeatedly ask for missing sections
automation requires stricter variables
a Template duplicates another Template
a better Template replaces it
```

---

# 16. Final Principle

> Templates make repeatable work faster while keeping output quality consistent.