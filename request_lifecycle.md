# Request Lifecycle – Proposed State Machine

```mermaid
stateDiagram-v2
  [*] --> DRAFT
  DRAFT --> SUBMITTED: submit
  SUBMITTED --> NEEDS_INFO: ask for detail
  NEEDS_INFO --> SUBMITTED: resubmit
  SUBMITTED --> TRIAGED: accept for review
  TRIAGED --> FEASIBILITY_REVIEW: request planning review
  FEASIBILITY_REVIEW --> NEEDS_INFO: request more detail
  FEASIBILITY_REVIEW --> READY_TO_SCHEDULE: scope-bound attestation
  FEASIBILITY_REVIEW --> ON_HOLD: blocking constraint
  ON_HOLD --> FEASIBILITY_REVIEW: reassess
  READY_TO_SCHEDULE --> SCHEDULED: pilot and date assigned
  SCHEDULED --> ON_HOLD: planning conditions change
  SCHEDULED --> IN_PROGRESS: assigned pilot reports start
  IN_PROGRESS --> EVIDENCE_REVIEW: evidence submitted
  EVIDENCE_REVIEW --> REWORK_REQUIRED: QA rejects revision
  REWORK_REQUIRED --> EVIDENCE_REVIEW: new revision submitted
  EVIDENCE_REVIEW --> READY_FOR_DELIVERY: QA approves revision
  READY_FOR_DELIVERY --> DELIVERED: coordinator releases
  DELIVERED --> CLOSED: requester acknowledges
  SUBMITTED --> CANCELLED: coordinator cancels
  NEEDS_INFO --> CANCELLED: coordinator cancels
  TRIAGED --> CANCELLED: coordinator cancels
  FEASIBILITY_REVIEW --> CANCELLED: coordinator cancels
  READY_TO_SCHEDULE --> CANCELLED: coordinator cancels
  SCHEDULED --> CANCELLED: coordinator cancels
  ON_HOLD --> CANCELLED: coordinator cancels
  CLOSED --> [*]
  CANCELLED --> [*]
```

**Status:** entirely hypothetical workflow. `READY_TO_SCHEDULE` is an internal planning checkpoint and does not authorize any real flight.

See [status and transition table](../07_workflow_and_status_model.md) for actors, guards and scope-version constraints.
