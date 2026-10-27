# 04 – Business Process Analysis: AS-IS and TO-BE

## 1. Evidence and Modeling Conventions

**AS-IS is an invented baseline** representing a plausible email/spreadsheet workflow. It is not a documented or observed workflow of a real company. **TO-BE is a proposed model** requiring domain validation and operational approval.

See [illustrative AS-IS diagram](diagrams/process_as_is.md) and [proposed TO-BE diagram](diagrams/process_to_be.md).

## 2. Illustrative AS-IS

1. Customer emails scope and location details.
2. Coordinator copies information to a spreadsheet and requests missing detail by email.
3. Coordinator discusses feasibility and tentative dates separately with staff.
4. Pilot receives scope via a forwarded message or file share.
5. Pilot sends evidence files to operations after work.
6. QA decisions and rework requests travel through separate threads.
7. Customer receives a download link without a single reliable timeline of decisions.

### Hypothetical Pain Points

| Moment | Potential issue | Proposed response |
|---|---|---|
| Request intake | No consistent mandatory details | Guided form and validation |
| Scope clarification | Multiple contradictory versions | One history and controlled revisions |
| Scheduling | Who owns a request unclear | Named owner and assigned pilot |
| Evidence review | Unclear whether a package passed QA | Explicit approval gate |
| Customer delivery | Email link not connected to decision history | Controlled release and receipt acknowledgment |

## 3. Proposed TO-BE – Main Success Path

1. Requester saves a `DRAFT` request and submits it as `SUBMITTED`.
2. Coordinator either returns it to `NEEDS_INFO` or triages it as `TRIAGED`.
3. Coordinator requests internal feasibility assessment (`FEASIBILITY_REVIEW`).
4. Reviewer records a satisfactory planning attestation (`READY_TO_SCHEDULE`) **without granting operational flight permission**.
5. Coordinator assigns a pilot/date (`SCHEDULED`).
6. Assigned pilot records start of the internal job (`IN_PROGRESS`) only after required **out-of-system** operational checks.
7. Pilot submits evidence for quality review (`EVIDENCE_REVIEW`).
8. QA reviewer accepts evidence (`READY_FOR_DELIVERY`) or requests rework (`REWORK_REQUIRED`).
9. Coordinator releases the approved package (`DELIVERED`).
10. Requester records receipt (`CLOSED`).

## 4. Important Alternate Paths

| Trigger | Proposed path | Notes |
|---|---|---|
| Scope details are missing | `SUBMITTED → NEEDS_INFO → SUBMITTED` | Preserve prior versions and questions |
| Feasibility cannot be attested | `FEASIBILITY_REVIEW → ON_HOLD` | Reason and owner mandatory |
| Scheduling conditions materially change | `SCHEDULED → ON_HOLD → FEASIBILITY_REVIEW` | Earlier attestation invalidated for reassessment |
| QA rejects a package | `EVIDENCE_REVIEW → REWORK_REQUIRED → EVIDENCE_REVIEW` | Keep versions and reviewer feedback |
| Requester withdraws before work starts | Eligible pre-execution state → `CANCELLED` | Coordinator logs authorization and reason |
| New scope emerges during/after work | Manual assessment and new request or controlled change | **Open decision**; no silent mutation |

`ON_HOLD` is intended for pre-execution planning issues. It does **not** instruct a pilot on actual flight safety responses. In-flight incidents and emergency handling remain outside the app.

## 5. Required Separation of Duties

- Feasibility reviewer records planning attestation; not the same as a legal clearance.
- Coordinator owns scheduling and customer release; cannot bypass QA gate.
- Assigned pilot prepares evidence but cannot approve own evidence.
- QA reviewer approves content but does not release packages to clients.
- Requester can acknowledge a delivered package but cannot change internal review states.

## 6. Data and Boundary Handoffs

| Handoff | Required data | Ownership / proposed verification |
|---|---|---|
| Requester → coordinator | Customer organization, site reference, purpose, desired output, date window | Validate request completeness |
| Coordinator → feasibility | Scope version, constraints, contact and access notes | Reviewer records decision |
| Coordinator → pilot | Approved scope snapshot, assignment, schedule | Pilot acknowledges assignment |
| Pilot → QA | Evidence references, revision, capture notes | QA checklist and decision |
| Coordinator → requester | Approved deliverable and release timestamp | Receipt confirmation without implicit satisfaction |

See [business rules](06_business_rules_and_permissions.md) and [status model](07_workflow_and_status_model.md).
