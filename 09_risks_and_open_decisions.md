# 09 – Risks, Dependencies and Open Decisions

## 1. Risk Register (Hypothetical)

Qualitative ratings are **illustrative analyst judgments**, not measured or organizationally approved risk scores.

| ID | Risk | Likelihood | Impact | Proposed response | Owner to confirm |
|---|---|---|---|---|---|
| R-01 | UI presents planning review as actual permission to fly | Medium | Critical | Explicit scope warnings; operational authority outside platform | Product + safety lead |
| R-02 | Customer A can access Customer B scope or imagery | Medium | Critical | Server-side organization isolation and security review | Security lead |
| R-03 | Evidence is released before current-revision QA | Medium | High | Immutable revision reference and hard release gate | QA lead |
| R-04 | Attachment contains sensitive site detail or malware | Medium | High | Secure storage, file restrictions, scanning, retention | Security/privacy |
| R-05 | Workflow grows into real-time flight planning/telemetry | High | Medium | Enforced out-of-scope boundary and change control | Product owner |
| R-06 | Reviewers disagree on feasibility criteria | Medium | High | Decision definitions, controlled checklist and policy owner | Feasibility lead |
| R-07 | Reassignments leave stale pilot access active | Medium | High | Revalidate access on every file/read; revoke on reassignment | Engineering/security |
| R-08 | Pilot feedback reveals insufficient evidence metadata | Medium | Medium | Prototype interviews, field usability test | Product/QA |
| R-09 | No validated retention basis for customer imagery | High | High | Block launch pending retention/privacy decisions | Legal/privacy |
| R-10 | Request volume or file size exceeds architecture assumptions | Medium | Medium | Load and storage sizing after discovery | Tech lead |

## 2. Open Decision Log

| ID | Decision needed | Options / dependency | Proposed status |
|---|---|---|---|
| D-01 | Who is the authoritative owner of site references and customer memberships? | Requester-managed vs coordinator-managed | OPEN |
| D-02 | Is customer delivery acknowledgment mandatory for closure? | Manual receipt vs status-based timeout | OPEN |
| D-03 | What constitutes a material change that invalidates feasibility? | Scope, site, date, equipment, conditions | OPEN |
| D-04 | May one person hold pilot and QA roles? | Forbid dual approval even when roles overlap | OPEN |
| D-05 | Retention of requests, evidence and audit logs | Contractual/legal/privacy requirements | BLOCKED |
| D-06 | Permitted evidence file types, maximum sizes and secure link lifetimes | Security, infrastructure | BLOCKED |
| D-07 | Exact login, customer invitation and multi-factor authentication approach | Security and identity architecture | OPEN |
| D-08 | Whether planned deadlines trigger reminders only or formal SLAs | Business policy and customer commitments | OPEN |
| D-09 | Whether exceptions after `IN_PROGRESS` create a separate incident or revision workflow | Operations and legal governance | OPEN |
| D-10 | Whether an external map or asset directory is needed | Discovery evidence and privacy assessment | DEFERRED |

## 3. External Dependencies

- Product owner approval of scope and value hypothesis
- Explicit customer-organization ownership and contracting model
- Feasibility and quality-review policy owners
- Security, privacy, access and retention decisions
- Review of user-facing language to avoid suggesting flight clearance
- Suitable identity, secure file storage, malware and auditing capabilities

No vendor selection, technology stack, budget, implementation estimate or deployment timeline has been validated.

## 4. Pre-Implementation Decision Gates

**Gate A – Business baseline:** validated user problems, confirmed terminology, prioritized capability set.

**Gate B – Operational boundary:** reviewed role of planning status vs true pilot/regulatory responsibilities, policy for reassessment/holds.

**Gate C – Security/privacy:** approved organization segregation, uploads, retention, logging and customer download rules.

**Gate D – Delivery readiness:** agreed interfaces, acceptance scenarios, test data and defect-management approach.

**Blocker:** a portfolio case study completing these documents is **not sufficient** to pass any of those gates.
