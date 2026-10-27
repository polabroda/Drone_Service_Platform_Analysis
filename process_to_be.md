# TO-BE Process – Proposed Customer-to-Delivery Flow

```mermaid
flowchart TD
  A[Requester creates draft] --> B[Submit request]
  B --> C{Operations triage}
  C -- Missing details --> D[Return for information]
  D --> E[Requester revises and resubmits]
  E --> C
  C -- Complete --> F[Internal feasibility review]
  F --> G{Planning attestation available?}
  G -- No --> H[Put on hold; log reason]
  H --> F
  G -- Yes --> I[Coordinator assigns pilot and date]
  I --> J[Assigned pilot reports job progress]
  J --> K[Submit evidence package]
  K --> L{Independent QA decision}
  L -- Rework --> M[Pilot prepares new revision]
  M --> K
  L -- Approve --> N[Coordinator releases approved package]
  N --> O[Customer acknowledges receipt]
```

**Safety boundary:** The internal planning attestation shown here is not legal or operational permission to fly. Actual flight-readiness checks and aviation decisions are outside this digital product concept.

**Status:** design candidate, not a validated or implemented workflow. Cancellation, changed constraints and exceptions are detailed in [status model](../07_workflow_and_status_model.md).
