# Drone Service Platform Analysis

This repository presents an independent **business, functional and product analysis case study** for a fictional digital platform coordinating commercial aerial inspection requests. The focus is on **greenfield product discovery**, user workflows, requirements engineering, access rules, exception paths and an evidence-based MVP proposal.

**It is a proposed product concept, not an application that has been developed, deployed, or validated with a real client.** No drone flight, airspace authorization, safety assessment, or acceptance test was conducted.

---

# Project Overview

- Fictional business context and product opportunity
- Stakeholder mapping and discovery questions
- Product vision, MVP boundaries and release hypotheses
- Illustrative AS-IS and proposed TO-BE processes
- Traceable business, functional and non-functional requirements
- Business rules, role permissions and segregation of responsibilities
- Request lifecycle, allowed transitions and exception paths
- User stories with proposed acceptance criteria
- Risks, dependencies, decisions and open questions
- Information architecture, screen inventory and requirements traceability
- Mermaid diagrams and optional synthetic fixture checks

---

# Business Scenario

**Lumenridge Aerial Inspections** is a **fictional** inspection provider serving commercial property and utility-asset owners. Its in-house operations team coordinates aerial condition-inspection assignments with trained pilots, reviews supporting evidence and delivers inspection packages to customers.

Customer requests currently arrive by email. Scope details, scheduling confirmations and evidence links are scattered across inboxes and local files. The proposed platform, **InspectFlow**, aims to give customers and operations staff one controlled record from intake to delivery.

The organization, people, sites, sample records, requirements, metrics, deadlines and workflows in this repository are **invented for this independent exercise**. The scenario is not a description of any public-sector drone platform, prior employer, client, or actual procurement.

---

# Product Scope

**In scope for proposed MVP:** customer request intake; guided scope clarification; internal triage; manual feasibility attestation; pilot assignment; scheduled work tracking; evidence submission; quality-review/rework loop; controlled deliverable release; customer confirmation; role-based access and audit history.

**Out of scope:** autonomous flight control, real-time drone telemetry, live airspace or weather APIs, legal flight authorization, a public provider marketplace, municipal intermediation, payments/invoicing, image-based AI inference, and production deployment.

**Safety boundary:** a proposed software status such as `READY_TO_SCHEDULE` is an internal planning state, **not permission to fly**. A competent operator must independently verify all applicable operational and regulatory requirements before any real activity.

---

# Repository Structure

| File | Content |
|---|---|
| [01_business_context.md](01_business_context.md) | Problem, proposed outcomes, assumptions, product boundaries |
| [02_stakeholders_and_discovery.md](02_stakeholders_and_discovery.md) | Stakeholders, hypotheses, discovery questions and decision owners |
| [03_product_scope_and_mvp.md](03_product_scope_and_mvp.md) | Product vision, MVP decisions, release hypotheses and scope exclusions |
| [04_process_analysis.md](04_process_analysis.md) | Illustrative AS-IS and proposed TO-BE processes, alternate paths |
| [05_requirements_catalogue.md](05_requirements_catalogue.md) | 29 proposed, uniquely identified requirements |
| [06_business_rules_and_permissions.md](06_business_rules_and_permissions.md) | Rule catalogue, role matrix, authorization boundaries |
| [07_workflow_and_status_model.md](07_workflow_and_status_model.md) | Formalized request statuses, transition ownership and guard conditions |
| [08_user_stories_and_acceptance.md](08_user_stories_and_acceptance.md) | User stories and **draft**, unexecuted acceptance tests |
| [09_risks_and_open_decisions.md](09_risks_and_open_decisions.md) | Risks, external dependencies, assumptions and decision log |
| [10_information_architecture_and_traceability.md](10_information_architecture_and_traceability.md) | Proposed screens, domain entities, requirement-to-test links |
| [diagrams/process_as_is.md](diagrams/process_as_is.md) | Illustrative current-state Mermaid process |
| [diagrams/process_to_be.md](diagrams/process_to_be.md) | Proposed end-to-end Mermaid process |
| [diagrams/request_lifecycle.md](diagrams/request_lifecycle.md) | Proposed Mermaid state machine |
| [diagrams/roles_and_information_flow.md](diagrams/roles_and_information_flow.md) | Proposed roles and access boundaries |
| [sample_data/inspection_requests.csv](sample_data/inspection_requests.csv) | Entirely synthetic inspection-request states |
| [sample_data/expected_checks.json](sample_data/expected_checks.json) | Declared expected fixture check results |
| [scripts/validate_fixtures.py](scripts/validate_fixtures.py) | Offline standard-library consistency check for sample records |

---

# Methodology

1. Define the fictional business opportunity, users and initial hypotheses.
2. Elicit requirements through proposed interviews and scenario-based workshops (**not actually conducted**).
3. Establish an illustrative current-state process and a design-candidate target process.
4. Separate MVP capabilities from later ideas and external/regulated operational responsibilities.
5. Define statuses, permission boundaries, exception conditions and auditable decisions.
6. Map proposed requirements into user stories, screen concepts and draft acceptance tests.
7. Identify open decisions, risks, and evidence needed before implementation.
8. Check a few **synthetic** status records against selected proposed invariants.

Priorities are suggestions using **MoSCoW**. Requirements are **not approved** by actual stakeholders. Diagrams render directly on GitHub from Markdown/Mermaid source.

---

# Tools and Techniques

- Business and Systems Analysis / Requirements Engineering
- Product Discovery / MVP Definition / Functional Design
- Stakeholder Mapping and Elicitation Planning
- Business Process Analysis (AS-IS / TO-BE)
- Workflow and State Modeling / Business Rules
- Role-Based Access Analysis / Information Architecture
- MoSCoW / Risk and Dependency Analysis
- User Stories / Acceptance Criteria / Requirements Traceability
- Markdown, Mermaid, CSV, JSON and optional Python fixture checks

---

# Goal

The goal is to demonstrate a **greenfield digital-product analysis workflow**: moving from a vaguely defined business need to a traceable functional concept with explicit user permissions, controlled state transitions, proposed acceptance evidence and unresolved decisions.

---

# Results

The case study delivers **4 business requirements, 18 functional requirements and 7 non-functional requirements** (29 total); a proposed MVP, role/permission matrix, workflow/state model, four diagrams, sample screen inventory, 10 draft acceptance scenarios and a risk/decision register.

The optional fixture check reads **15 fictional request records**. It checks internal consistency of the *illustrative states* only; it is not product testing. Run from the repository root:

```bash
python scripts/validate_fixtures.py
```

A passing result does **not** demonstrate a working platform, operational flight readiness, regulatory compliance, implementation quality or security certification.

---

# Confidentiality and Limitations

This is an **independent, wholly fictional portfolio exercise**. It does not reproduce or disclose any employer's or client's nonpublic documents, meeting notes, customer requirements, platform design, confidential workflows, contracts, personnel, datasets, or decisions. The operational flow, names and sample artifacts were invented for this demonstration. All diagrams, user stories, risks and acceptance scenarios are **proposals**, not evidence of completed delivery or production use.

---

# Author

Paulina Broda
