# 08 – User Stories and Draft Acceptance Criteria

All stories and tests are **draft hypotheses**; no working UI, production system, or customer acceptance testing exists. Gherkin-style examples express intended behavior, **not executed tests**.

## 1. Story Inventory

| Story | As a… | I want… | So that… | Requirements |
|---|---|---|---|---|
| US-01 | Customer requester | Submit a complete inspection request | Operations can assess one version of the need | FR-001, FR-002 |
| US-02 | Coordinator | Return an incomplete request for clarification | I do not schedule ambiguous work | FR-003, FR-004 |
| US-03 | Feasibility reviewer | Record a scoped planning attestation or hold | Constraints are explicit without pretending to authorize flight | FR-005, FR-006 |
| US-04 | Coordinator | Assign a pilot and target date | The request has accountable delivery ownership | FR-007 |
| US-05 | Assigned pilot | Submit a revisioned evidence package | QA can assess a concrete deliverable | FR-008, FR-009 |
| US-06 | QA reviewer | Reject a package with reasons or approve a revision | Customers see only checked evidence | FR-010 |
| US-07 | Coordinator | Release only the approved package | Delivery is controlled and auditable | FR-011 |
| US-08 | Customer requester | See my organization's requests and confirm receipt | I can track my outcomes safely | FR-012, FR-014 |
| US-09 | Operations user | View a history of actions and decisions | I can reconstruct who made a change | FR-015 |
| US-10 | Coordinator | Cancel an eligible request with a reason | Abandoned pre-work cases remain traceable | FR-017 |

## 2. Ten Proposed Acceptance Scenarios

### AT-01 – Save and submit a complete request (`US-01`)

**Given** an authenticated requester for `Client A` has required intake fields; **when** the request is saved and submitted; **then** it receives a unique stable ID, belongs to `Client A` and changes from `DRAFT` to `SUBMITTED`.

### AT-02 – Block incomplete submission (`US-01`)

**Given** the requested output is missing; **when** the requester submits; **then** the request stays `DRAFT` and the missing field is explained; no partially submitted work item is created.

### AT-03 – Clarification round-trip (`US-02`)

**Given** a `SUBMITTED` request lacks usable access notes; **when** the coordinator requests clarification and the requester resubmits; **then** the request returns via `NEEDS_INFO` to `SUBMITTED`, retains the same ID and preserves both scope revisions.

### AT-04 – Feasibility gating (`US-03`)

**Given** a request is `FEASIBILITY_REVIEW`; **when** the reviewer logs the required scope-bound assessment; **then** the status can become `READY_TO_SCHEDULE`; **and** the interface does not claim legal or operational flight authorization.

### AT-05 – Hold invalidates planning attestation (`US-03`)

**Given** a case is `SCHEDULED`; **when** a material planning constraint changes and the coordinator places it `ON_HOLD`; **then** the current attestation is invalidated and the case cannot return directly to `SCHEDULED` without `FEASIBILITY_REVIEW`.

### AT-06 – Schedule only an eligible request (`US-04`)

**Given** the case is `READY_TO_SCHEDULE` with a current attestation; **when** the coordinator chooses one eligible pilot and a date; **then** it becomes `SCHEDULED`. **Given** attestation is missing; **then** scheduling is rejected and logged.

### AT-07 – Enforce independent QA and revision (`US-05`, `US-06`)

**Given** the assigned pilot submits a package in `EVIDENCE_REVIEW`; **when** that pilot attempts approval; **then** the action is denied. **When** an independent QA reviewer requests corrections; **then** the case moves to `REWORK_REQUIRED` and requires a new revision on resubmission.

### AT-08 – Release current approved revision only (`US-07`)

**Given** the current package is in `READY_FOR_DELIVERY` with independent QA approval; **when** the coordinator releases it; **then** the system creates a delivery reference and changes the case to `DELIVERED`. Without current approval, release is denied.

### AT-09 – Reject cross-customer direct link (`US-08`)

**Given** an authenticated `Client A` requester; **when** they use a guessed or copied URL for `Client B` request or file; **then** access is denied for metadata and download, including when a cached UI would otherwise show a link.

### AT-10 – Block late cancellation, retain audit (`US-09`, `US-10`)

**Given** a request is `IN_PROGRESS`; **when** a coordinator attempts `CANCELLED`; **then** the transition is denied and a policy exception is required outside this MVP. **Given** a pre-execution `SUBMITTED` case; **when** it is cancelled with a reason; **then** `CANCELLED` and the reason are recorded in the audit trail.

## 3. What Is Not Proven

No browser interactions were performed. No identity provider, storage security, privacy controls, permission engine, notification service, actual flight operation, image review, acceptance execution or SLA was tested. AT-01 through AT-10 are **test designs**, not test results.

## 4. Additional Acceptance Coverage Needed Before Build

- Attachment malware scanning, storage authorization, retention and deletion (`NFR-005`, `NFR-006`)
- Performance under an approved workload (`NFR-003`)
- Recovery/backup exercises (`NFR-004`)
- Keyboard and screen-reader review (`NFR-007`)
- Concurrent updates and stale approval across versions (`RULE-05`, `RULE-10`)
- Notification privacy and deliverability (`FR-016`)

See [traceability](10_information_architecture_and_traceability.md).
