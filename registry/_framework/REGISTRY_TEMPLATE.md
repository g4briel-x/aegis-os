## FILE: `registry/_framework/REGISTRY_TEMPLATE.md`

# Registry Template

Version: 0.1.0  
Status: Draft

---

# 1. Registry File Template

```yaml
registry:
  id: {{registry_id}}
  name: {{registry_name}}
  schema_version: {{schema_version}}
  status: {{status}}
  owner: {{owner}}
  description: {{description}}

entries:
  - id: {{asset_id}}
    name: {{asset_name}}
    type: {{asset_type}}
    domain: {{domain}}
    category: {{category}}
    status: {{asset_status}}
    maturity: {{maturity}}
    version: {{version}}
    path: {{path}}
    owner: {{asset_owner}}
    summary: {{summary}}
    tags:
      - {{tag_1}}
      - {{tag_2}}
    related_assets:
      - id: {{related_asset_id}}
        relationship: {{relationship_type}}
```

---

# 2. Example Entry

```yaml
registry:
  id: registry.templates
  name: Templates Registry
  schema_version: 0.1.0
  status: draft
  owner: aegis-os
  description: Machine-readable catalog of Aegis OS templates.

entries:
  - id: business.pricing-strategy-template
    name: Pricing Strategy Template
    type: template
    domain: business
    category: saas-monetization
    status: draft
    maturity: usable
    version: 0.1.0
    path: templates/business/pricing-strategy-template
    owner: aegis-os
    summary: Defines SaaS pricing strategy, value metric, plans, packaging and validation.
    tags:
      - pricing
      - saas
      - monetization
    related_assets:
      - id: business.billing-subscription-model
        relationship: uses
      - id: product.define-pricing-strategy
        relationship: supports
```

---

# 3. Final Principle

> The registry template should be simple enough to maintain and strict enough to power automation.
