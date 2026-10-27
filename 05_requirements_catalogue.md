# 05 – Requirements Catalogue

**Status:** all requirements are **proposed for a fictional product**, not confirmed by real stakeholders or implemented in software. IDs are stable for cross-references.

**Priority:** `Must` / `Should` / `Could` / `Won't (MVP)` are proposed MoSCoW values. `TO VERIFY` indicates unresolved evidence or policy. `PROPOSED` means authored as a candidate feature, not approved.

## Business Requirements

| ID | Proposed requirement | Rationale | Priority | Status |
|---|---|---|---|---|
| BR-001 | Each customer inspection request shall have a unique record with a traceable owner and status. | Remove ambiguity across email hand-offs. | Must | PROPOSED |
| BR-002 | Internal scheduling shall require documented feasibility review; it shall never constitute flight authorization. | Separate planning from real-world operational control. | Must | TO VERIFY |
| BR-003 | Customer evidence packages shall not be released without a separate quality decision. | Consistent quality hand-off. | Must | PROPOSED |
| BR-004 | Customers shall be able to access only records belonging to their own organization. | Cross-customer segregation. | Must | TO VERIFY |

## Functional Requirements

| ID | Proposed functional requirement | Suggested verification | Priority | Status |
|---|---|---|---|---|
| FR-001 | A requester can save a draft with customer organization, site reference, inspection category, objective and desired output; the system assigns an immutable request ID. | Creation, mandatory fields and ID uniqueness. | Must | PROPOSED |
| FR-002 | An authenticated requester can submit a complete draft, causing `DRAFT → SUBMITTED`. | Valid/invalid submit scenarios. | Must | PROPOSED |
| FR-003 | Coordinator can return a submitted case to `NEEDS_INFO` with question; requester can revise and resubmit without losing history. | History and resubmission check. | Must | PROPOSED |
| FR-004 | Coordinator can triage a submitted case and request feasibility review using allowed transitions. | Role and transition guards. | Must | PROPOSED |
| FR-005 | Feasibility reviewer can record a scope-version-bound internal attestation or place the case `ON_HOLD` with reason; neither action grants flight permission. | Version, attestation and negative tests. | Must | TO VERIFY |
| FR-006 | Coordinator can place an eligible scheduled case `ON_HOLD` if constraints change; the previous attestation becomes invalid. | Hold and re-review checks. | Must | PROPOSED |
| FR-007 | Coordinator can set a planned date and assign one available pilot only for `READY_TO_SCHEDULE` requests. | Role, state and assignment checks. | Must | TO VERIFY |
| FR-008 | The assigned pilot can mark an assigned scheduled job `IN_PROGRESS` after independently confirming required operational checks outside the platform. | Assigned-pilot-only transition; explicit disclaimer. | Must | TO VERIFY |
| FR-009 | Assigned pilot can upload evidence references and submit a versioned package to `EVIDENCE_REVIEW`. | File type/version and submission check. | Must | PROPOSED |
| FR-010 | QA reviewer can approve evidence or request rework with reasons; the pilot cannot approve their own package. | Approval separation and loop. | Must | PROPOSED |
| FR-011 | Coordinator can release only the latest QA-approved package to the owning customer, producing a delivery reference and timestamp. | Block unapproved delivery. | Must | PROPOSED |
| FR-012 | Requester can acknowledge receipt of a `DELIVERED` package and close it; receipt does not imply acceptance of commercial quality claims. | Closure and access test. | Must | TO VERIFY |
| FR-013 | Authorized users can filter/search requests by permitted organization, request ID, status, owner or due window. | Search and record-scope checks. | Should | PROPOSED |
| FR-014 | Every read/download and mutation uses server-side role + organization authorization rather than UI-only hiding. | Cross-tenant negative tests. | Must | TO VERIFY |
| FR-015 | Material status, assignment, scope, approval and release changes are logged with actor, timestamp, before/after state and reason where relevant. | Audit record inspection. | Must | PROPOSED |
| FR-016 | The system issues role-appropriate notifications for missing info, scheduled work, holds, rework requests and delivery; notifications reveal no unauthorized customer data. | Recipient and leakage test. | Should | TO VERIFY |
| FR-017 | Coordinator can cancel a pre-execution request with reason and audit trail; cancellation is blocked once status is `IN_PROGRESS` or later. | Allowed/forbidden cancellation. | Should | PROPOSED |
| FR-018 | Operations can view a queue of overdue decision points without automatically changing an operational state. | Aging calculation and no implicit escalation. | Could | TO VERIFY |

## Non-functional Requirements

| ID | Proposed non-functional requirement | Verification proposal | Priority | Status |
|---|---|---|---|---|
| NFR-001 | Cross-organization isolation and least-privilege access must be enforced server-side for metadata, media and downloads. | Threat model, integration and penetration tests. | Must | TO VERIFY |
| NFR-002 | Scope revisions, planning attestations, QA decisions and deliveries must be attributable and tamper-evident according to an approved audit policy. | Log integrity and role review. | Must | TO VERIFY |
| NFR-003 | For a representative workload, 95% of request-detail views should complete within 3 seconds; assumed load and target need validation. | Performance test with approved load profile. | Should | TO VERIFY |
| NFR-004 | Backup and recovery arrangements must satisfy owner-approved RPO/RTO before production launch. | Recovery exercise. | Must | BLOCKED |
| NFR-005 | Evidence/record retention, export and deletion must follow an approved privacy and contract schedule. | Retention matrix and deletion test. | Must | BLOCKED |
| NFR-006 | Evidence uploads and downloads must use approved file-type/size controls, malware inspection and secure authorized URLs. | Security and file-handling tests. | Must | TO VERIFY |
| NFR-007 | Core forms, status cues and decisions should be keyboard-accessible, clearly labeled and not depend on color alone. | Accessibility review with representative users. | Should | TO VERIFY |

**Count: 4 business + 18 functional + 7 non-functional = 29 proposed requirements.**

## Requirement Dependencies

- `BR-004` → `FR-014` / `NFR-001`: isolation applies to list, detail, attachments and delivered files.
- `BR-002` → `FR-005`, `FR-006`, `FR-007`, `FR-008`: feasibility and operational readiness must not be conflated.
- `BR-003` → `FR-009`, `FR-010`, `FR-011`: package revision and QA gate precede delivery.
- `FR-015` → `NFR-002`: audit semantics must be established before acceptance of approval flows.
- `FR-009` / `FR-011` → `NFR-005` / `NFR-006`: retention and file security are launch dependencies.

See [business rules](06_business_rules_and_permissions.md), [workflow](07_workflow_and_status_model.md) and [traceability](10_information_architecture_and_traceability.md).
