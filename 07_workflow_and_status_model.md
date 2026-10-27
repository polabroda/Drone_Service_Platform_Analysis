# 07 – Request Workflow and Status Model

**Design status: PROPOSED.** States represent administrative tracking inside a fictional web platform. They **do not model regulatory permission, aircraft control, meteorological safety or flight-readiness decisions**.

## 1. Proposed State Dictionary

| State | Meaning | Accountable role | Allowed next states |
|---|---|---|---|
| `DRAFT` | Requester is preparing an unpublished request | Requester | `SUBMITTED` |
| `SUBMITTED` | Submitted and awaiting operations triage | Coordinator | `NEEDS_INFO`, `TRIAGED`, `CANCELLED` |
| `NEEDS_INFO` | Requester owes missing/clarified information | Requester | `SUBMITTED`, `CANCELLED` |
| `TRIAGED` | Initial business scope accepted for planning review | Coordinator | `FEASIBILITY_REVIEW`, `CANCELLED` |
| `FEASIBILITY_REVIEW` | Internal planning constraints under review | Feasibility reviewer | `READY_TO_SCHEDULE`, `NEEDS_INFO`, `ON_HOLD`, `CANCELLED` |
| `READY_TO_SCHEDULE` | Planning attestation recorded on current scope version | Coordinator | `SCHEDULED`, `CANCELLED` |
| `SCHEDULED` | Pilot and provisional assignment date recorded | Coordinator | `IN_PROGRESS`, `ON_HOLD`, `CANCELLED` |
| `ON_HOLD` | Planning blocker; prior attestation invalid if material conditions changed | Reviewer / coordinator | `FEASIBILITY_REVIEW`, `CANCELLED` |
| `IN_PROGRESS` | Assigned job activity is recorded internally by pilot | Assigned pilot | `EVIDENCE_REVIEW` |
| `EVIDENCE_REVIEW` | Submitted evidence is awaiting independent QA | QA reviewer | `READY_FOR_DELIVERY`, `REWORK_REQUIRED` |
| `REWORK_REQUIRED` | QA identified deficiencies requiring a new package revision | Assigned pilot | `EVIDENCE_REVIEW` |
| `READY_FOR_DELIVERY` | Current package version has QA approval | Coordinator | `DELIVERED` |
| `DELIVERED` | Approved package made available to owning customer | Requester | `CLOSED` |
| `CLOSED` | Customer confirmed receipt of delivered package | None | — |
| `CANCELLED` | Request discontinued before execution with documented reason | None | — |

### Terminality

`CLOSED` and `CANCELLED` are terminal **in this demonstrative version**. Reopen/disputes or corrective work after delivery would require a later product decision rather than hidden state reversal.

## 2. Transition Guards and Events

| Event | From → To | Permitted actor | Mandatory guards / information |
|---|---|---|---|
| `submit` | `DRAFT → SUBMITTED` | Requester | Required intake fields complete |
| `return_for_information` | `SUBMITTED → NEEDS_INFO`; `FEASIBILITY_REVIEW → NEEDS_INFO` | Coordinator / reviewer respectively | Question/reason logged |
| `resubmit` | `NEEDS_INFO → SUBMITTED` | Requester | New scope version; history preserved |
| `triage` | `SUBMITTED → TRIAGED` | Coordinator | Business scope reviewed |
| `request_feasibility` | `TRIAGED → FEASIBILITY_REVIEW` | Coordinator | Current scope version locked for review |
| `attest_planning` | `FEASIBILITY_REVIEW → READY_TO_SCHEDULE` | Feasibility reviewer | Review and scope version saved; **not flight clearance** |
| `hold` | `FEASIBILITY_REVIEW → ON_HOLD`; `SCHEDULED → ON_HOLD` | Reviewer / coordinator | Reason; invalidate earlier attestation when assumptions changed |
| `reassess` | `ON_HOLD → FEASIBILITY_REVIEW` | Coordinator | Revised scope/constraint snapshot |
| `schedule` | `READY_TO_SCHEDULE → SCHEDULED` | Coordinator | Valid attestation, pilot, date |
| `start_record` | `SCHEDULED → IN_PROGRESS` | Assigned pilot | Out-of-platform operational checks remain pilot responsibility |
| `submit_package` | `IN_PROGRESS → EVIDENCE_REVIEW`; `REWORK_REQUIRED → EVIDENCE_REVIEW` | Assigned pilot | New package revision, mandatory evidence references |
| `qa_rework` | `EVIDENCE_REVIEW → REWORK_REQUIRED` | Independent QA reviewer | Reason and requested corrections |
| `qa_approve` | `EVIDENCE_REVIEW → READY_FOR_DELIVERY` | Independent QA reviewer | Current revision approved |
| `release` | `READY_FOR_DELIVERY → DELIVERED` | Coordinator | Current QA decision, correct customer, delivery reference |
| `acknowledge` | `DELIVERED → CLOSED` | Owning requester | Receipt timestamp; commercial acceptance separate |
| `cancel` | `SUBMITTED` / `NEEDS_INFO` / `TRIAGED` / `FEASIBILITY_REVIEW` / `READY_TO_SCHEDULE` / `SCHEDULED` / `ON_HOLD → CANCELLED` | Coordinator | Reason and auditable authorization; not during/after work |

## 3. Status Invariants

1. `request_id` and `client_org` are immutable once created.
2. If state is at/after `SCHEDULED` on a successful path, a pilot is assigned and a **current** internal planning attestation exists.
3. `READY_FOR_DELIVERY`, `DELIVERED`, `CLOSED` require QA approval for the current package revision.
4. `DELIVERED`, `CLOSED` require a delivery reference linked to the approved revision.
5. `ON_HOLD` cannot transition directly back to `SCHEDULED`; reassessment is required.
6. Rework supersedes prior approval: QA must assess the resubmitted package anew.
7. Every state transition is audited with actor and timestamp; negative transitions are not performed.
8. Customer-facing visibility and permissions are independently checked (not inferred from state alone).

## 4. Change-Control and Concurrency Questions

- What happens if two coordinators try to schedule the same case?
- Does a pilot have to explicitly accept an assignment?
- Who owns a case if a reviewer becomes unavailable?
- What constitutes material scope change and who can determine that?
- How long may a customer leave `DELIVERED` unacknowledged?

**Design proposal:** use a request version to detect stale concurrent updates and show a conflict rather than silently overwrite. A precise concurrency contract is **TO VERIFY**.

See [state diagram](diagrams/request_lifecycle.md), [rules](06_business_rules_and_permissions.md), and [draft acceptance tests](08_user_stories_and_acceptance.md).
