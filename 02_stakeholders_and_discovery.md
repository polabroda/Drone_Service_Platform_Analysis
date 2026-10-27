# 02 – Stakeholders and Discovery Plan

## 1. Stakeholder Map (Hypothetical)

| Actor / group | Need or concern | Suggested involvement | Decision rights to confirm |
|---|---|---|---|
| Customer requester | Submit clear scope, receive transparent updates and final package | Interviews, prototype walkthrough | Accept/close own delivered request? |
| Operations coordinator | Triage requests, own status, resolve exceptions | Process workshop, backlog refinement | Approve triage, schedule and release? |
| Feasibility reviewer | Record planning constraints and readiness checks | Controls workshop | Attest feasibility, place on hold |
| Assigned pilot | Know assigned scope, share progress and evidence | Task walkthrough | Start/complete assigned work; no flight authorization through app |
| Quality reviewer | Inspect evidence, require rework or approve release | Review workshop | Approve deliverable quality |
| Platform administrator | Manage memberships without default content access | Security/access workshop | Account and role changes only |
| Product owner (proposed) | Own value, MVP and backlog priorities | Decision workshop | Approve backlog and scope |
| Security/privacy advisor | Organization isolation, retention, secure downloads | Threat-model review | Security policy approval |

**Role labels are invented**; they are not a record of roles at a real client.

## 2. Proposed Elicitation Plan (Not Executed)

| Activity | Hypothesis to probe | Expected artifact |
|---|---|---|
| 45-minute requester interviews | Customers cannot see the next action | Top tasks, pain points, service definition |
| 60-minute operations workflow workshop | Clarification and hand-offs cause delays | AS-IS map, owner and exception matrix |
| Pilot task walkthrough | Scope packages are not consistently versioned | Checklist and evidence requirements |
| Feasibility and quality workshop | Planning and QA decisions need separate controls | Gate definitions and audit expectations |
| Security/privacy review | Multiple customers create data segregation risk | Role matrix and access constraints |
| Click-through prototype review | Status terminology may be unclear | Usability findings and revised copy |

No interview, workshop, usability test or stakeholder acceptance has actually taken place for this portfolio scenario.

## 3. Discovery Questions

**Customer requests**
1. What minimum information is needed to assess an inspection request?
2. Do requesters represent a person, site, department or contracting organization?
3. What information is sensitive (site photos, customer contracts, planned dates)?
4. May a requester change scope after submission, and how is change controlled?

**Operations**
5. Who can reject a request or return it for clarification?
6. Can assignments be split across pilots? (Current case assumes no.)
7. What happens if site access or customer input is missing?
8. Who may release a deliverable, and what evidence must exist first?

**Safety and quality**
9. What constitutes a documented internal feasibility attestation?
10. How does a hold invalidate or preserve an earlier attestation?
11. Which inspections need additional evidence and second-person checks?
12. What happens to already-uploaded evidence after a QA rejection?

**Technology and policy**
13. What are the retention, access logging and deletion requirements?
14. Must access use enterprise SSO, MFA or a customer invitation workflow?
15. What are realistic request volumes and file sizes?
16. Are any integration, payment or map features genuinely MVP-critical?

## 4. Hypotheses and Validation Status

| ID | Hypothesis | Status | Next evidence |
|---|---|---|---|
| H-01 | A unified request timeline is more valuable than live flight tracking. | TO VERIFY | Requester + coordinator interviews |
| H-02 | A single `ON_HOLD` state is sufficient for blockers before execution. | TO VERIFY | Operations exception workshop |
| H-03 | Quality review must be independent of the assigned pilot. | TO VERIFY | Quality control policy |
| H-04 | Customers need delivery acknowledgment, not self-service editing of completed work. | TO VERIFY | Customer prototype review |
| H-05 | Free-form comments plus required fields are enough for MVP scope definition. | TO VERIFY | Request sample analysis |

## 5. Decision Ownership

The assumed product owner approves business scope; the feasibility reviewer defines planning-check evidence; operations owns workflow hand-offs; security/privacy approves isolation and retention; trained pilots independently determine operational readiness.

All owners and governance are **proposed** and must be confirmed before a real project.
