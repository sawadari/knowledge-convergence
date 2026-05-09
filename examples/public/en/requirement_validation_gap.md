# Example: Requirement Verification Passed, Validation Missing

## Situation

A requirement says:

```text
The system shall complete task registration within 2 seconds.
```

The test passes. The system completes registration within 2 seconds.

However, in the operational scenario, users must repeat the task many times and still experience the workflow as too slow.

## Distinction

| Item | Result |
|---|---|
| Verification | pass |
| Validation | fail |

## Knowledge Convergence result

```text
verification_status = pass
validation_status = fail
outcome = reopen
reason = intended operational use is not satisfied
```

## Lesson

Passing specified tests is not the same as satisfying intended use.
