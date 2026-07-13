## FILE: `templates/business/pricing-strategy-template/variables.md`

# Pricing Strategy Template — Variables

Version: 0.1.0  
Status: Draft

---

# 1. Required Variables

```text
{{pricing_strategy_name}}
{{product_or_offer}}
{{owner}}
{{status}}
{{primary_segment}}
{{core_value}}
{{pricing_objective}}
{{pricing_model}}
{{value_metric}}
{{plan_1_name}}
{{plan_1_price}}
{{validation_method}}
{{pricing_decision}}
```

---

# 2. Optional Variables

```text
{{target_launch_date}}
{{annual_discount}}
{{paid_pilot_price}}
{{enterprise_custom_pricing}}
{{billing_provider}}
{{finance_approval}}
{{leadership_approval}}
```

---

# 3. Variable Descriptions

## `{{pricing_model}}`

Purpose:

```text
The monetization structure used to charge customers.
```

Example:

```text
tiered_subscription
```

---

## `{{value_metric}}`

Purpose:

```text
The unit that pricing scales with because it reflects customer value.
```

Example:

```text
projects reviewed
```

---

## `{{plan_1_price}}`

Purpose:

```text
Price of the first paid plan or entry offer.
```

Example:

```text
25,000 FCFA per month
```

---

## `{{validation_success_criteria}}`

Purpose:

```text
Evidence needed to confirm that pricing is acceptable.
```

Example:

```text
At least 5 of 10 qualified prospects agree to pay for the pilot.
```

---

# 4. Final Principle

> Pricing variables should make assumptions explicit enough to test with customers.
