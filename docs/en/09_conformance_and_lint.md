# Conformance and Lint

Knowledge Convergence should not remain a vague slogan. It should be inspectable.

This repository includes schemas, profiles, rulebooks, test vectors, and examples that can be used to check whether a knowledge state satisfies required conditions.

## Why conformance matters

Without conformance rules, teams may claim that knowledge has converged even when important conditions are missing.

Conformance checks help detect:

- missing evidence
- missing context
- missing owner
- missing authority envelope
- missing validation
- missing rollback path
- symbolic human approval
- unreviewed AI execution
- unresolved blocker hidden by an average score

## Lint mindset

A lint rule does not need to solve the whole problem. It detects a condition that should be reviewed.

Examples:

```text
KC-LINT-REQ-001: Requirement has no linked evidence.
KC-LINT-REQ-002: Requirement has no validation scenario.
KC-LINT-DEC-001: Decision has no accountable owner.
KC-LINT-AGENT-001: Agent action has no authority envelope.
KC-LINT-AGENT-002: Agent action has no rollback path.
KC-LINT-HUMAN-001: Human approval lacks stop authority.
```

## SE lint examples

For Systems Engineering, useful checks include:

- requirement without stakeholder need
- requirement without verification method
- verification without validation
- decision without rationale
- trade-off without rejected alternatives
- change without impact analysis
- AI coding task without approved requirement
- high-risk action without rollback path

## Blocking logic

Averages are dangerous. A knowledge state may score well on many dimensions but still contain a blocker.

Example:

```text
evidence = high
context = high
owner = present
validation = missing
agent rollback path = missing
```

The correct outcome may still be hold.

## How to use conformance

Conformance checks can be used in:

- review gates
- CI pipelines
- AI agent delegation gates
- SE model reviews
- requirements reviews
- change approval boards
- audit workflows
