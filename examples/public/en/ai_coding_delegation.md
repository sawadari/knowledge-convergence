# Example: AI Coding Delegation

## Situation

A team wants an AI coding agent to implement a change in a repository.

The requested change is based on a feature idea, but the requirement is not fully approved.

## Candidate action

```text
Ask AI coding agent to modify the payment validation module.
```

## Required checks

- Is the requirement approved?
- Is the design decision recorded?
- Is the agent allowed to edit the repository?
- Is the tool scope limited?
- Is the data access scope defined?
- Is a human review gate required?
- Is a rollback path defined?
- Is the test strategy defined?

## Result

```text
outcome = hold
reason = approved requirement, authority envelope, and rollback path are missing
```

## Lesson

AI coding speed does not remove the need for upstream decision readiness and delegation governance.
