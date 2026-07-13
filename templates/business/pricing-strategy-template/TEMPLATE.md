## FILE: `templates/business/pricing-strategy-template/TEMPLATE.md`

# Pricing Strategy Template

Version: 0.1.0  
Status: Draft

---

# 1. Document Control

```text
Pricing Strategy Name: {{pricing_strategy_name}}
Product / Offer: {{product_or_offer}}
Owner: {{owner}}
Contributors: {{contributors}}
Status: {{status}}
Version: {{version}}
Last Updated: {{last_updated}}
Target Launch Date: {{target_launch_date}}
```

---

# 2. Executive Summary

Summarize the pricing strategy.

```text
{{executive_summary}}
```

Recommended format:

```text
This pricing strategy monetizes {{product_or_offer}} for {{target_segment}} using {{pricing_model}} because customers receive value through {{value_metric}}.
```

---

# 3. Target Customer

```text
Primary segment: {{primary_segment}}
Ideal customer profile: {{icp}}
Buyer: {{buyer}}
Primary user: {{primary_user}}
Budget owner: {{budget_owner}}
Buying trigger: {{buying_trigger}}
```

---

# 4. Customer Value

```text
Core value delivered:
{{core_value}}

Customer outcome:
{{customer_outcome}}

Business value:
{{business_value}}

Time saved:
{{time_saved}}

Revenue gained or protected:
{{revenue_impact}}

Risk reduced:
{{risk_reduction}}
```

---

# 5. Pricing Objective

```text
Primary objective: {{pricing_objective}}
```

Recommended values:

```text
validate_willingness_to_pay
maximize_activation
increase_trial_conversion
support_paid_pilots
optimize_revenue
support_enterprise_sales
simplify_market_entry
```

---

# 6. Pricing Model

```text
Pricing model: {{pricing_model}}
```

Possible models:

```text
flat_subscription
tiered_subscription
per_seat
per_workspace
usage_based
hybrid_subscription_usage
paid_pilot
enterprise_custom
freemium
```

Reason:

```text
{{pricing_model_reason}}
```

---

# 7. Value Metric

Define what pricing scales with.

```text
Value metric: {{value_metric}}
```

Examples:

```text
active users
workspaces
projects
documents reviewed
storage volume
AI credits
API calls
revenue managed
submissions processed
```

Why this metric is appropriate:

```text
{{value_metric_reason}}
```

---

# 8. Plan Structure

```text
Plan | Target User | Price | Billing Interval | Main Value | Limits
{{plan_1_name}} | {{plan_1_target_user}} | {{plan_1_price}} | {{plan_1_interval}} | {{plan_1_value}} | {{plan_1_limits}}
{{plan_2_name}} | {{plan_2_target_user}} | {{plan_2_price}} | {{plan_2_interval}} | {{plan_2_value}} | {{plan_2_limits}}
{{plan_3_name}} | {{plan_3_target_user}} | {{plan_3_price}} | {{plan_3_interval}} | {{plan_3_value}} | {{plan_3_limits}}
```

---

# 9. Entitlement Matrix

```text
Feature / Limit | {{plan_1_name}} | {{plan_2_name}} | {{plan_3_name}}
{{feature_1}} | {{plan_1_feature_1}} | {{plan_2_feature_1}} | {{plan_3_feature_1}}
{{feature_2}} | {{plan_1_feature_2}} | {{plan_2_feature_2}} | {{plan_3_feature_2}}
{{feature_3}} | {{plan_1_feature_3}} | {{plan_2_feature_3}} | {{plan_3_feature_3}}
```

Entitlements should map to product access rules.

---

# 10. Free Trial, Freemium or Paid Pilot

```text
Entry offer type: {{entry_offer_type}}
Trial length: {{trial_length}}
Freemium limit: {{freemium_limit}}
Paid pilot price: {{paid_pilot_price}}
Pilot duration: {{pilot_duration}}
Conversion path: {{conversion_path}}
```

---

# 11. Upgrade and Downgrade Rules

Upgrade rules:

```text
{{upgrade_rule_1}}
{{upgrade_rule_2}}
{{upgrade_rule_3}}
```

Downgrade rules:

```text
{{downgrade_rule_1}}
{{downgrade_rule_2}}
{{downgrade_rule_3}}
```

Cancellation rules:

```text
{{cancellation_rule_1}}
{{cancellation_rule_2}}
```

---

# 12. Discount and Custom Pricing Policy

```text
Discount allowed: {{discount_allowed}}
Maximum discount: {{maximum_discount}}
Annual discount: {{annual_discount}}
Founding customer discount: {{founding_customer_discount}}
Enterprise custom pricing: {{enterprise_custom_pricing}}
Approval required: {{discount_approval_required}}
```

---

# 13. Competitive Reference

```text
Competitor | Pricing Model | Price Range | Notes
{{competitor_1}} | {{competitor_1_model}} | {{competitor_1_price}} | {{competitor_1_notes}}
{{competitor_2}} | {{competitor_2_model}} | {{competitor_2_price}} | {{competitor_2_notes}}
```

---

# 14. Willingness-to-Pay Validation

Validation questions:

```text
{{validation_question_1}}
{{validation_question_2}}
{{validation_question_3}}
```

Validation method:

```text
{{validation_method}}
```

Target sample:

```text
{{target_sample}}
```

Success criteria:

```text
{{validation_success_criteria}}
```

---

# 15. Revenue Assumptions

```text
Target customers: {{target_customers}}
Expected conversion rate: {{expected_conversion_rate}}
Expected ARPA: {{expected_arpa}}
Monthly revenue target: {{monthly_revenue_target}}
Annual revenue target: {{annual_revenue_target}}
Churn assumption: {{churn_assumption}}
Expansion assumption: {{expansion_assumption}}
```

---

# 16. Risks and Assumptions

Assumptions:

```text
Assumption 1: {{assumption_1}}
Assumption 2: {{assumption_2}}
Assumption 3: {{assumption_3}}
```

Risks:

```text
Risk | Impact | Mitigation | Owner
{{risk_1}} | {{risk_impact_1}} | {{risk_mitigation_1}} | {{risk_owner_1}}
{{risk_2}} | {{risk_impact_2}} | {{risk_mitigation_2}} | {{risk_owner_2}}
```

---

# 17. Implementation Requirements

```text
Billing provider: {{billing_provider}}
Plan catalog required: {{plan_catalog_required}}
Entitlement service required: {{entitlement_service_required}}
Invoice handling required: {{invoice_handling_required}}
Payment failure handling required: {{payment_failure_handling_required}}
Billing audit events required: {{billing_audit_events_required}}
```

---

# 18. Launch Decision

```text
Pricing decision: {{pricing_decision}}
Decision reason: {{decision_reason}}
Accepted risks: {{accepted_risks}}
Next review date: {{next_review_date}}
```

Recommended decision values:

```text
approved
approved_for_pilot
needs_validation
blocked
```

---

# 19. Approval

```text
Product approval: {{product_approval}}
Business approval: {{business_approval}}
Sales approval: {{sales_approval}}
Finance approval: {{finance_approval}}
Engineering approval: {{engineering_approval}}
Leadership approval: {{leadership_approval}}
```

---

# 20. Final Principle

> Pricing should be tested against customer value, buying behavior and product delivery capacity.
