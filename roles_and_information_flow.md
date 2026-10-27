# Actor and Information Boundaries – Proposed Design

```mermaid
flowchart LR
  R[Customer requester] -->|Own-org intake and receipt| P[InspectFlow request record]
  C[Operations coordinator] -->|Triage, scheduling, release| P
  F[Feasibility reviewer] -->|Internal planning attestation| P
  A[Assigned pilot] -->|Assigned job and evidence| P
  Q[Independent QA reviewer] -->|Approve or request revision| P
  M[Platform administrator] -->|Memberships only| U[Identity and role directory]
  U -->|Enforces membership and organization context| P
  P -->|Customer-scoped delivered files| D[(Protected evidence store)]
```

**Proposed controls:** customer requesters see only their organization, pilots only assigned work, admins no request content by default, and release is gated by independent QA.

**Not shown as integrations:** aircraft systems, airspace services, flight control, regulations, payments or a public service-provider marketplace.

See [role permissions](../06_business_rules_and_permissions.md).
