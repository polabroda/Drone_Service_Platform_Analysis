# 06 – Business Rules and Role Permissions

## 1. Proposed Business Rules

Each rule is a **design candidate** for a fictional commercial inspection workflow. Real operating policies, legal duties and aviation requirements are outside this case study.

| ID | Rule | Source requirement | Verification / open issue |
|---|---|---|---|
| RULE-01 | Every request has one immutable business ID and exactly one owning customer organization. | BR-001, BR-004, FR-001 | Create and attempt cross-organization access |
| RULE-02 | A `SUBMITTED` request must contain a site reference, purpose, requested output and customer contact. | FR-002 | Mandatory-field negative tests |
| RULE-03 | Returning a request for information does not overwrite earlier scope versions or comments. | FR-003, FR-015 | Reopen and compare version history |
| RULE-04 | Only a coordinator moves submitted cases to `TRIAGED` or requests `FEASIBILITY_REVIEW`. | FR-004 | Role/state denial checks |
| RULE-05 | Feasibility attestation is tied to a specific scope version; material change invalidates it. | BR-002, FR-005, FR-006 | Change scope and assert re-review |
| RULE-06 | `READY_TO_SCHEDULE` means administrative planning readiness **only**; it never authorizes flight. | BR-002, FR-005, FR-008 | UI copy/policy review |
| RULE-07 | Scheduling requires a valid planning attestation and assigned pilot/date. | FR-007 | Missing-attestation and missing-pilot tests |
| RULE-08 | Only the assigned pilot may report progress and submit an evidence package. | FR-008, FR-009 | Assignment and role negative tests |
| RULE-09 | The assigned pilot cannot approve their own evidence; QA can require rework. | BR-003, FR-010 | Separation-of-duties check |
| RULE-10 | Delivery requires latest-package QA approval; an earlier approved revision is insufficient after rework. | BR-003, FR-011 | Old revision/release negative tests |
| RULE-11 | Customer visibility is scoped to organization; internal pilot sees only assigned work. | BR-004, FR-014 | Forbidden direct-link access |
| RULE-12 | Cancellation applies only before `IN_PROGRESS`; later exceptions require manual policy resolution. | FR-017 | Terminal and active-state checks |
| RULE-13 | Significant transitions record actor, scope version, timestamp and reason when required. | FR-015 | Audit integrity check |
| RULE-14 | A delivered package may be closed by the owning requester; receipt is not commercial acceptance. | FR-012 | Closure semantics to confirm |

### Changes After Feasibility Review

A requester's proposed material scope change after triage must **not** silently update the approved assignment. A coordinator either returns it to an editable clarification path before scheduling, or records a separate change decision; exact post-scheduling change control is **OPEN / BLOCKED** pending governance. For this MVP, material changes to a `SCHEDULED` request cause `ON_HOLD` and a new `FEASIBILITY_REVIEW` before rescheduling.

## 2. Actor Definitions

- **Customer requester**: belongs to exactly one fictional client organization; drafts and views its own organization's cases.
- **Operations coordinator**: internally owns triage, schedule, hold/cancel decisions, customer delivery.
- **Feasibility reviewer**: records internal planning findings; not an aviation regulator or substitute for pilot judgment.
- **Assigned pilot**: views work assigned to them, enters work notes and evidence; any true flight operation happens outside this platform.
- **Quality reviewer**: checks submitted package, approves or sends back for revision.
- **Platform administrator**: changes accounts and roles; **no default access** to customer content.

A person could technically hold multiple internal roles, but whether this is allowed — especially pilot + QA — is an unresolved segregation-of-duties policy (`D-04`).

## 3. Proposed Permission Matrix

`C` create; `R` read; `U` update; `A` authorize transition; `–` no access. Rows describe domain permissions, not admin database access.

| Action | Customer requester | Coordinator | Feasibility reviewer | Assigned pilot | QA reviewer | Admin |
|---|---|---|---|---|---|---|
| Create/edit customer request draft | C/U (own org, eligible state) | R (all assigned queue) | – | – | – | – |
| Read case detail | R (own org, customer-facing fields) | R (internal queue) | R (assigned review) | R (assigned work) | R (assigned QA) | – |
| Submit/resubmit | A (own org) | – | – | – | – | – |
| Return for missing information / triage | – | A (triage, intake clarification) | A (feasibility clarification only) | – | – | – |
| Record planning attestation / hold | – | A (hold only) | A (attest/hold) | – | – | – |
| Assign pilot and date | – | A | – | – | – | – |
| Report work and submit evidence | – | – | – | U/A (assigned) | – | – |
| Approve QA or request rework | – | – | – | – | A (not self) | – |
| Release deliverable | – | A (QA gate) | – | – | – | – |
| Acknowledge receipt | A (own org, delivered) | – | – | – | – | – |
| Cancel eligible pre-execution request | Request only (proposal) | A | – | – | – | – |
| Manage membership / roles | – | – | – | – | – | C/U (accounts only) |

**Important distinctions:** customer requesters do **not** see internal planning assessments, other clients' jobs or private pilot notes. Client-facing status copy may map internal states to simpler labels; the mapping is an open UX decision, not implemented here.

## 4. Access Enforcement Cases

| Attempt | Expected outcome |
|---|---|
| Customer A opens Customer B request URL | Denied and audit event; no metadata leak |
| Pilot opens unassigned request or deliverable | Denied |
| Admin with no content role requests attachments | Denied |
| Pilot attempts to approve own evidence | Denied even if multiple UI controls are visible |
| Coordinator attempts release after QA rework | Denied; approval for current revision required |
| Expired signed download link is reused | Denied; retention/access policy governs regeneration |

## 5. Still To Confirm

Membership model for customer organizations, multi-role conflicts, delegated approvals, attestation expiry, evidence download expiry, consent for imagery where required, retention and legal processing bases. See [decision log](09_risks_and_open_decisions.md).
