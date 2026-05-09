# Examples

This document summarizes simple examples. Full example files are under [`../../examples/public/en/`](../../examples/public/en/).

## 1. Material change held for missing validation

A team proposes changing a material to reduce cost.

The proposal has cost benefit and preliminary feasibility, but lacks safety validation and supplier impact review.

Result:

```text
outcome = hold
reason = validation evidence and supplier review are missing
```

See: [`material_change_hold.md`](../../examples/public/en/material_change_hold.md)

## 2. AI coding delegation held for missing authority envelope

A team asks an AI coding agent to implement a change.

The implementation target is clear, but the agent lacks defined repository permissions, review gate, and rollback path.

Result:

```text
outcome = hold
reason = missing agent execution envelope
```

See: [`ai_coding_delegation.md`](../../examples/public/en/ai_coding_delegation.md)

## 3. Verification passed but validation failed

A requirement passes its verification test, but the operational scenario shows that the user workflow remains too slow.

Result:

```text
verification_status = pass
validation_status = fail
outcome = reopen
```

See: [`requirement_validation_gap.md`](../../examples/public/en/requirement_validation_gap.md)

## 4. Organization capacity gap

A high-risk decision is routed to a domain expert who has the competence but not enough review capacity before the release gate.

Result:

```text
outcome = escalate
reason = review capacity gap for high-risk decision
```

See: [`organization_capacity_gap.md`](../../examples/public/en/organization_capacity_gap.md)
