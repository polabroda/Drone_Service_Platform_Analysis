# 03 – Product Scope and MVP

## 1. Product Vision

**InspectFlow** is a proposed web platform that connects a commercial inspection customer to an internal delivery team through a **traceable request record**, without attempting to automate flight authorization or aircraft control.

## 2. Primary User Journeys

1. **Requester:** describe asset/site and inspection outcome → submit → answer follow-up questions → track progress → access final package → confirm receipt.
2. **Coordinator:** triage intake → request feasibility check → schedule assignment → manage blockers → release QA-approved evidence.
3. **Pilot:** review assigned scope → report work progression → upload supporting evidence → respond to QA rework.
4. **Feasibility/QA reviewers:** perform internal checkpoints independently; document decisions and reasons.

These are **design candidates**, not findings from tested user journeys.

## 3. Suggested MVP and MoSCoW

| Capability | Priority | MVP | Reason and dependency |
|---|---|---|---|
| Authenticated requests with organization ownership | Must | Yes | Core record and segregation |
| Required intake fields and clarification | Must | Yes | Enable useful triage |
| Coordinator triage and internal feasibility attestation | Must | Yes | Controlled preparation |
| Pilot assignment and planned date | Must | Yes | Operational ownership |
| Evidence upload with revision metadata | Must | Yes | Deliverable traceability |
| Independent QA approval / rework loop | Must | Yes | Release control |
| Controlled customer delivery and receipt confirmation | Must | Yes | End-to-end outcome |
| Status timeline and action audit | Must | Yes | Explain hand-offs |
| Role- and organization-based visibility | Must | Yes | Prevent cross-customer exposure |
| Basic status-change notifications | Should | Yes, minimal | Reduce manual follow-up |
| Filterable work queue | Should | Yes | Coordinator efficiency |
| Due-date warnings and escalation | Could | No | Needs service-level policy |
| Rich reporting and analytics | Could | No | Baselines and definitions missing |
| Reusable category-specific checklists | Could | No | Discovery needed; one generic checklist in MVP |
| Live maps, flight telemetry, AI photo analysis | Won't | No | Not required to prove coordination value |
| Flight permission, airspace/weather authorization | Won't | No | Externally controlled operational/legal activity |
| Billing, public supplier marketplace, municipality routing | Won't | No | Different business model and integration burden |

**Scope guard:** A state change in InspectFlow cannot be treated as an operational clearance to fly.

## 4. Release Hypotheses

| Release | Proposed outcome | Gate before proceeding |
|---|---|---|
| Discovery/prototype | Understand user language and failure paths | Confirmed stakeholder needs |
| MVP | Intake → coordinated planning → evidence QA → delivery | Approved access, safety boundary and retention decisions |
| Later iteration | Analytics, due-date SLAs, configurable checklists | Usage and quality metrics show value |
| Separate feasibility investigation | External integrations, optional map, richer scheduling | Legal/security/technical assessment |

No release has been built or launched.

## 5. What MVP Deliberately Does Not Solve

- Negotiating commercial terms or calculating prices
- Flight planning or live mission management
- Airspace clearance, weather interpretation, permissions or site safety certification
- Automated review of imagery or medical/physical hazard inference
- Handling subcontractor bids or cross-organization marketplaces
- Integration with drone hardware or flight logs

## 6. Definition of Ready for Engineering (Proposed)

A story is **not** ready solely because it appears in this repository. Before implementation it needs: a confirmed business owner, validated scope, approved permissions, non-functional requirements, failure modes, acceptance examples and resolved dependencies.

See [requirements](05_requirements_catalogue.md), [workflow](07_workflow_and_status_model.md), and [open decisions](09_risks_and_open_decisions.md).
