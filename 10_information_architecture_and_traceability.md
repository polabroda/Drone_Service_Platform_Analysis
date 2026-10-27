# 10 – Information Architecture and Requirements Traceability

## 1. Proposed Screen Inventory

These are **screen concepts**, not delivered mockups or a coded UI.

| Screen / view | Primary actor | Essential information and actions | Related requirements |
|---|---|---|---|
| Customer request list | Requester | Own-org request ID, simplified status, created/date, next action | FR-013, FR-014 |
| New / edit request | Requester | Site reference, inspection type, objective, output, contact, notes | FR-001–FR-003 |
| Request detail / timeline | Scoped actors | Authorized view of scope version, owner, status, audit events | FR-014, FR-015 |
| Operations triage queue | Coordinator | Intake aging, completeness, return/triage actions | FR-003, FR-004, FR-013 |
| Planning review form | Feasibility reviewer | Scope snapshot, review checklist, attestation or hold reason | FR-005, FR-006 |
| Assignment board | Coordinator | Ready requests, pilot/date, hold and cancel controls | FR-006, FR-007, FR-017 |
| My assignments | Assigned pilot | Approved scope summary, reporting and evidence actions | FR-008, FR-009 |
| Evidence package / review | Pilot / QA | Package versions, files, QA comments, approve/rework action | FR-009, FR-010 |
| Approved delivery | Coordinator | Latest approved revision, owning organization, release log | FR-011 |
| Customer deliverables | Requester | Secure file links, delivery timestamp, receipt acknowledgment | FR-011, FR-012 |
| User and organization management | Admin | Invitation, role assignment, membership revocation | FR-014, NFR-001 |

**Critical UX copy:** `READY_TO_SCHEDULE` must be described as an **internal planning milestone**, not flight authorization. Internal review content must not automatically appear in customer views.

## 2. Proposed Domain Entities and Ownership

| Entity | Key | Selected attributes | Design boundary / owner |
|---|---|---|---|
| Client organization | `client_org_id` | Name, status | Customer/account admin |
| User membership | `membership_id` | User ID, org ID, role, active flag | Admin/security |
| Inspection request | `request_id` | Client org, scope version, status, requester | Owning customer; coordinator workflow |
| Request scope version | `scope_version_id` | Request ID, category, objective, site reference, date window | Requester and coordinator via controlled flow |
| Feasibility attestation | `attestation_id` | Scope version, reviewer, result, timestamp | Feasibility reviewer |
| Assignment | `assignment_id` | Pilot, date, request, active flag | Coordinator |
| Evidence package | `package_id` | Request, revision, file refs, submitted by | Assigned pilot |
| QA decision | `qa_decision_id` | Package revision, reviewer, verdict, reason | QA reviewer |
| Delivery | `delivery_id` | Approved package, client org, released by/time | Coordinator |
| Audit event | `event_id` | Actor, time, object, before/after, reason | Platform controls/security |

**Not designed here:** physical UAV command or safety logs, live geographic telemetry, flight authorizations, aviation regulatory registers and commercial billing.

## 3. Requirement-to-Design-to-Acceptance Traceability

| Business objective | Requirement(s) | Design artifact | Draft test |
|---|---|---|---|
| Structured intake | BR-001, FR-001, FR-002 | New request form, `DRAFT`/`SUBMITTED` | AT-01, AT-02 |
| Controlled clarification | FR-003, FR-004 | Scope revision and triage process | AT-03 |
| Safe planning boundary | BR-002, FR-005, FR-006 | Attestation and hold rules | AT-04, AT-05 |
| Clear assignment | FR-007, FR-008 | Assignment screen, role matrix | AT-06 |
| Evidence quality | BR-003, FR-009, FR-010 | Versioned package and independent QA | AT-07 |
| Controlled customer release | BR-003, FR-011, FR-012 | Delivery and acknowledgment | AT-08 (release), follow-up needed (receipt) |
| Cross-customer isolation | BR-004, FR-014, NFR-001 | Role matrix and authorization layer | AT-09 |
| Traceable cancellation and edits | FR-015, FR-017, NFR-002 | Status transitions + audit | AT-10 |
| Notifications | FR-016 | Event-to-recipient matrix | Test to design |
| Performance and recovery | NFR-003, NFR-004 | Non-functional plan | Test to design |
| Retention and secure files | NFR-005, NFR-006 | Content lifecycle/security policies | Test to design |
| Accessibility | NFR-007 | Form/feedback patterns | Test to design |

## 4. Proposed Notification Matrix

| Event | Suggested recipient | Excluded information |
|---|---|---|
| Request needs clarification | Requester of owning organization | Private reviewer notes |
| Request scheduled | Owning requester, assigned pilot | Other customers' assignments |
| Planning hold | Coordinator, assigned pilot if any; requester receives generic update | Safety reviewer confidential detail |
| QA rework | Assigned pilot, coordinator | Other customers' packages |
| Approved delivery | Owning requester | Internal quality commentary beyond released summary |

Notification content, delivery mechanism, retries and consent requirements are **TO VERIFY**. No notification implementation is claimed.

## 5. Artifact Consistency Checklist

- IDs used in stories belong to the [requirements catalogue](05_requirements_catalogue.md).
- All states and transitions come from the [workflow model](07_workflow_and_status_model.md).
- Only the coordinator releases delivered evidence; QA approves the current revision.
- Pilot actions remain separate from flight authorization.
- Organization boundaries apply to both metadata and files.
- Traceability gaps are marked `Test to design`, not silently treated as covered.

## 6. Suggested Next Engineering Questions

How to represent scope versions and prevent stale-state writes? How to isolate evidence storage per organization? How to revoke access immediately on pilot reassignment? Which events require append-only audit? Which content is safe to expose in customer-facing status feeds?

These are open design questions, not architectural decisions made by a real engineering team.
