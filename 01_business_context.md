# 01 – Business Context and Product Opportunity

## 1. Case and Evidence Status

**Fictional case:** Lumenridge Aerial Inspections, an invented private inspection provider with a small internal operations team, pilots and commercial customers.

**Evidence classification:** Every challenge and metric below is an **illustrative assumption**. There was no actual discovery engagement, stakeholder interview, observation, data audit or implementation.

## 2. Problem Statement

Potential customers email a service request describing an asset and inspection objective. An operations coordinator separately records the scope, exchanges clarifications, plans a pilot assignment and tracks the eventual evidence package. Attachments and status information are spread across email threads, shared folders and spreadsheets.

| Illustrative issue | Hypothesized consequence | Discovery evidence needed |
|---|---|---|
| Incomplete request descriptions | Repeated clarification, delayed estimates | Review redacted historical inquiries |
| Unclear ownership of active requests | Duplicate follow-ups and inconsistent status | Shadow operations coordinators |
| Planning changes conveyed by email | Wrong date or scope communicated | Interview pilots and requesters |
| Evidence package distributed via ad hoc links | Quality/revision uncertainty | Walk through three past cases |
| Weak audit trail for approval and release | Disputed hand-offs | Review quality and legal policies |

## 3. Product Hypothesis

An auditable, request-centered workflow for intake, internal assessment, scheduling and deliverable release **may** reduce manual coordination and improve the clarity of each participant's next action.

It **will not** replace trained pilot judgment, an airspace assessment, customer contracts, or organizational safety procedures.

## 4. Illustrative Users and Volume

- 4 customer organizations with several requesters each
- 2 internal operations coordinators
- 1 internal feasibility reviewer
- 6 pilots, typically assigned one job at a time
- 2 quality reviewers
- **Assumed** planning volume: ~60 requests/month, not a measured workload

These numbers are **not requirements**; they support a sizing discussion. Actual activity and performance targets must be investigated.

## 5. Target Business Outcomes (Hypotheses)

| Outcome | Proposed measure | Baseline | Target status |
|---|---|---|---|
| Faster intake completion | Median time from submission to triage | Unknown | TO VERIFY |
| Fewer missing scope fields | % returned for clarification | Unknown | TO VERIFY |
| Better workflow visibility | % active requests with known owner/status | Unknown | TO VERIFY |
| More consistent quality hand-offs | % deliverables released after QA | Unknown | 100% proposed policy |
| Controlled sharing | Unauthorized cross-client views | Unknown | Zero tolerance hypothesis |

**No claimed impact:** No baseline, target improvement or realized ROI has been measured.

## 6. Decision and Delivery Boundaries

**Business decision needed:** whether this should be an internal coordination platform with a customer portal, and who owns the workflows.

**Within product concept:** requests, scope, internal feasibility attestation, assignment, evidence lifecycle, delivery, organization-scoped customer visibility.

**Excluded:** aircraft operations and authorization, airspace/weather clearance, public provider brokerage, invoicing, live telemetry, AI computer vision, map layers, regulatory certification.

## 7. Initial Assumptions to Validate

- `A-01` One commercial customer organization owns each request.
- `A-02` A single internal pilot is accountable for executing a scheduled assignment.
- `A-03` A separate quality reviewer must approve evidence before customer release.
- `A-04` Feasibility is an internal planning checkpoint; operational go/no-go remains outside the platform.
- `A-05` Customers may view only their own organization's requests and delivered packages.

See [stakeholder analysis](02_stakeholders_and_discovery.md), [MVP scope](03_product_scope_and_mvp.md) and [risks and decisions](09_risks_and_open_decisions.md).
