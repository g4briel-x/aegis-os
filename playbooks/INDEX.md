## FILE: `playbooks/INDEX.md`

# Aegis OS — Playbooks Index

Version: 0.1.0  
Status: Foundation Draft

---

# 1. Purpose

This index lists the execution Playbooks available in Aegis OS.

A Playbook represents a repeatable procedure for executing a high-value task with clear triggers, steps, decision points, checklists, outputs and examples.

---

# 2. Playbook Framework

```text
playbooks/_framework/README.md
playbooks/_framework/PLAYBOOK_SPECIFICATION.md
playbooks/_framework/PLAYBOOK_DIRECTORY_STRUCTURE.md
playbooks/_framework/PLAYBOOK_METADATA_SCHEMA.md
playbooks/_framework/PLAYBOOK_AUTHORING_GUIDE.md
playbooks/_framework/PLAYBOOK_EXECUTION_MODEL.md
playbooks/_framework/PLAYBOOK_DECISION_POINTS.md
playbooks/_framework/PLAYBOOK_OUTPUT_MODEL.md
playbooks/_framework/PLAYBOOK_QUALITY_GATE.md
playbooks/_framework/PLAYBOOK_REVIEW_CHECKLIST.md
playbooks/_framework/PLAYBOOK_VERSIONING.md
playbooks/_framework/PLAYBOOK_TEMPLATE.md
```

---

# 3. Product Playbooks

```text
playbooks/product/define-saas-mvp
playbooks/product/run-discovery-interviews
playbooks/product/create-prd
playbooks/product/define-pricing-strategy
playbooks/product/prepare-saas-launch
```

Purpose:

```text
Covers discovery, MVP definition, PRD creation, pricing and SaaS launch preparation.
```

---

# 4. Design Playbooks

```text
playbooks/design/design-saas-ux-flow
```

Purpose:

```text
Covers SaaS UX flow design and user journey structuring.
```

---

# 5. Engineering Playbooks

```text
playbooks/engineering/debug-production-issue
playbooks/engineering/design-saas-architecture
playbooks/engineering/implement-feature-from-prd
playbooks/engineering/review-pull-request
playbooks/engineering/optimize-database-performance
playbooks/engineering/design-saas-data-model
playbooks/engineering/write-test-plan
playbooks/engineering/create-api-contract
```

Purpose:

```text
Covers debugging, architecture, implementation, PR review, database performance, data modeling, test planning and API contract design.
```

---

# 6. Security Playbooks

```text
playbooks/security/review-api-security
playbooks/security/respond-to-security-incident
playbooks/security/design-auth-rbac
playbooks/security/harden-production-saas
```

Purpose:

```text
Covers API security, incident response, RBAC design and production security hardening.
```

---

# 7. Infrastructure Playbooks

```text
playbooks/infrastructure/fix-failing-ci-pipeline
playbooks/infrastructure/deploy-saas-application
```

Purpose:

```text
Covers CI/CD troubleshooting and SaaS deployment execution.
```

---

# 8. Operations Playbooks

```text
playbooks/operations/prepare-release
playbooks/operations/monitor-saas-production
playbooks/operations/run-postmortem-review
playbooks/operations/create-runbook
```

Purpose:

```text
Covers release preparation, production monitoring, postmortems and runbook creation.
```

---

# 9. Management Playbooks

```text
playbooks/management/plan-saas-mvp-delivery
```

Purpose:

```text
Covers SaaS MVP delivery planning, coordination and execution tracking.
```

---

# 10. Business Playbooks

```text
playbooks/business/create-go-to-market-plan
```

Purpose:

```text
Covers SaaS go-to-market planning, channels, positioning, sales motion and launch execution.
```

---

# 11. Standard Playbook File Structure

Each premium Playbook should follow this structure:

```text
README.md
PLAYBOOK.md
metadata.yaml
steps.md
decision-points.md
checklists.md
outputs.md
examples/examples.md
```

---

# 12. Playbook Completion Status

```yaml
playbooks:
  framework: complete
  product:
    define_saas_mvp: complete
    run_discovery_interviews: complete
    create_prd: complete
    define_pricing_strategy: complete
    prepare_saas_launch: complete
  design:
    design_saas_ux_flow: complete
  engineering:
    debug_production_issue: complete
    design_saas_architecture: complete
    implement_feature_from_prd: complete
    review_pull_request: complete
    optimize_database_performance: complete
    design_saas_data_model: complete
    write_test_plan: complete
    create_api_contract: complete
  security:
    review_api_security: complete
    respond_to_security_incident: complete
    design_auth_rbac: complete
    harden_production_saas: complete
  infrastructure:
    fix_failing_ci_pipeline: complete
    deploy_saas_application: complete
  operations:
    prepare_release: complete
    monitor_saas_production: complete
    run_postmortem_review: complete
    create_runbook: complete
  management:
    plan_saas_mvp_delivery: complete
  business:
    create_go_to_market_plan: complete
```

---

# 13. Final Principle

> Playbooks turn expert execution into a repeatable operating procedure.
