# Example: Organization Capacity Gap

## Situation

A high-risk architecture decision requires review by a safety expert.

The safety expert has the right competence and authority, but cannot review the decision before the release gate.

## Candidate decision

```text
Approve architecture option X before release gate.
```

## Knowledge Convergence check

| Dimension | Status |
|---|---|
| Meaning | clear |
| Evidence | partially available |
| Responsibility | safety expert identified |
| Review capacity | insufficient |
| Domain validity | blocked by missing review |

## Result

```text
outcome = escalate
reason = review capacity gap for high-risk decision
```

## Lesson

A role being assigned is not the same as meaningful review capacity being available.
