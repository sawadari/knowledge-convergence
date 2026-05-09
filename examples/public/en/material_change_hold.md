# Example: Material Change Hold

## Situation

A product team proposes changing a material to reduce cost.

The proposal includes:

- estimated cost reduction
- preliminary manufacturability review
- rough schedule impact

However, the proposal lacks:

- safety validation
- lifecycle durability evidence
- supplier impact review
- customer acceptance analysis

## Candidate decision

```text
Change material from A to B for cost reduction.
```

## Knowledge Convergence check

| Dimension | Status |
|---|---|
| Meaning | clear |
| Context | product line and target part are specified |
| Evidence | cost evidence present; safety evidence missing |
| Value criteria | cost is considered; safety and durability incomplete |
| Responsibility | engineering owner present; supplier review owner missing |
| History | initial proposal recorded |
| Domain validity | insufficient |

## Result

```text
outcome = hold
reason = validation evidence and supplier review are missing
next_action = request safety validation and supplier impact review
```

## Lesson

A proposal can be economically attractive and still not be domain-valid. Hold is the correct branch when execution conditions are not met.
