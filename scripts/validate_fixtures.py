"""Check internal consistency of fully fictional demo records only.

Run from repository root: python scripts/validate_fixtures.py
No live system, API or external service is accessed.
"""
from __future__ import annotations
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "sample_data"
KNOWN = {
    "DRAFT", "SUBMITTED", "NEEDS_INFO", "TRIAGED", "FEASIBILITY_REVIEW",
    "READY_TO_SCHEDULE", "SCHEDULED", "ON_HOLD", "IN_PROGRESS",
    "EVIDENCE_REVIEW", "REWORK_REQUIRED", "READY_FOR_DELIVERY",
    "DELIVERED", "CLOSED", "CANCELLED",
}
ASSIGNED = {"SCHEDULED", "IN_PROGRESS", "EVIDENCE_REVIEW", "REWORK_REQUIRED", "READY_FOR_DELIVERY", "DELIVERED", "CLOSED"}
QA_OK = {"READY_FOR_DELIVERY", "DELIVERED", "CLOSED"}
DELIVERY = {"DELIVERED", "CLOSED"}


def check(rows: list[dict[str, str]]) -> list[str]:
    violations = []
    seen = set()
    for row in rows:
        rid = row["request_id"]
        state = row["status"]
        if rid in seen:
            violations.append(f"{rid}: duplicate request ID")
        seen.add(rid)
        if state not in KNOWN:
            violations.append(f"{rid}: unknown status {state}")
        if not row["client_org"] or not row["site_reference"]:
            violations.append(f"{rid}: missing organization/site reference")
        if state in ASSIGNED and not row["assigned_pilot"]:
            violations.append(f"{rid}: missing pilot in {state}")
        if state in ASSIGNED and row["planning_attestation"] != "true":
            violations.append(f"{rid}: missing planning attestation in {state}")
        if row["qa_approved"] == "true" and state not in QA_OK:
            violations.append(f"{rid}: QA approval in a non-approved state")
        if state in QA_OK and row["qa_approved"] != "true":
            violations.append(f"{rid}: missing QA approval in {state}")
        if state in DELIVERY and not row["delivery_reference"]:
            violations.append(f"{rid}: missing delivery reference")
        if state not in DELIVERY and row["delivery_reference"]:
            violations.append(f"{rid}: delivery reference before release")
        if row["planning_attestation"] not in {"true", "false"}:
            violations.append(f"{rid}: invalid planning_attestation value")
        if row["qa_approved"] not in {"true", "false"}:
            violations.append(f"{rid}: invalid qa_approved value")
    return violations


def main() -> None:
    with (DATA / "inspection_requests.csv").open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    expected = json.loads((DATA / "expected_checks.json").read_text(encoding="utf-8"))
    issues = check(rows)
    observed = {
        "records": len(rows),
        "violations": len(issues),
        "distinct_clients": len({r["client_org"] for r in rows}),
        "statuses": dict(sorted(Counter(r["status"] for r in rows).items())),
    }
    for issue in issues:
        print("FAIL:", issue)
    if observed != expected:
        print("FAIL: Observed fixture summary disagrees with expected_checks.json")
        print("Observed:", json.dumps(observed, indent=2))
        print("Expected:", json.dumps(expected, indent=2))
        raise SystemExit(1)
    if issues:
        raise SystemExit(1)
    print(f"PASS: {len(rows)} fictional request records, {observed['distinct_clients']} clients, 0 invariant violations")
    print("Fixture check only — not software implementation, regulatory or operational testing.")


if __name__ == "__main__":
    main()
