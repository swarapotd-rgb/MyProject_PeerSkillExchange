# Requirements Traceability Matrix (RTM)

**Problem Statement #56 — Peer Skill Exchange & Mentorship Network**

The RTM links every requirement forward to the use case that realises it, the architectural component that implements it, the Jira work item that tracks it, and the test case that verifies it. It is used to confirm that no requirement is lost during design, and that no component or test exists without a requirement behind it.

---

## 1. Forward Traceability — Requirement → Design → Test

| Req ID | Requirement (short) | Source | Use Case | Architectural Component | Jira Story | Test Case | Status |
|---|---|---|---|---|---|---|---|
| **FR-001** | Maintain time-credit balance; credit 1 hour on verified completion | Problem Statement (given) | UC6 Manage Time-Credit Balance | Credit Ledger Service | SBPS56-17 (Story 4.1) | TC-01, TC-02 | Verified |
| **FR-002** | Register, edit, remove teachable skills | Derived — mentor role | UC1 Register Teaching Skill | Skill Catalogue Service | SBPS56-12 (Story 1.1) | TC-03, TC-04 | Verified |
| **FR-003** | Search mentors by skill, only those with open slots | Derived — exchange purpose | UC3 Search for Mentor | Discovery / Search Service | SBPS56-13 (Story 1.2) | TC-05, TC-06 | Verified |
| **FR-004** | Book an available slot when balance ≥ 1 credit | Derived — FR-001 fail condition | UC4 Book Skill Session<br>UC7 Check Time-Credit Balance *(include)* | Booking Service | SBPS56-14 (Story 2.1) | TC-07, TC-08, TC-09 | Verified |
| **FR-005** | Mutual confirmation + 1–5 rating before verification | Problem Statement — "mutual feedback rating validations" | UC5 Verify Session Completion<br>UC9 Add Written Feedback *(extend)* | Verification & Rating Service | SBPS56-16 (Story 3.1) | TC-10, TC-11 | Verified |
| **NFR-001** | iCal sync with Google Calendar and Outlook | Problem Statement (given) | UC8 Sync Session to External Calendar *(extend)* | Calendar Integration Adapter | SBPS56-15 (Story 2.2) | TC-12, TC-13 | Verified |
| **NFR-002** | Reject 100% of non-transactional balance changes | Derived — integrity of FR-001 | UC6 Manage Time-Credit Balance | Credit Ledger Service + Audit Log | SBPS56-18 (Story 4.2) | TC-14, TC-15 | Verified |

---

## 2. Backward Traceability — Use Case → Requirement

Every use case in the UML diagram traces back to at least one requirement. No orphan use cases exist.

| Use Case | Traces back to |
|---|---|
| UC1 Register Teaching Skill | FR-002 |
| UC2 Manage Availability | FR-003, FR-004 |
| UC3 Search for Mentor | FR-003 |
| UC4 Book Skill Session | FR-004 |
| UC5 Verify Session Completion | FR-005 |
| UC6 Manage Time-Credit Balance | FR-001, NFR-002 |
| UC7 Check Time-Credit Balance | FR-004 |
| UC8 Sync Session to External Calendar | NFR-001 |
| UC9 Add Written Feedback Comment | FR-005 |

---

## 3. Test Case Register

| TC ID | Verifies | Test Description | Expected Result |
|---|---|---|---|
| TC-01 | FR-001 | Mark a session verified and inspect both balances. | Mentor +1 credit, learner −1 credit, applied within 1 minute. |
| TC-02 | FR-001 | Inspect balances before verification completes. | No balance change occurs. |
| TC-03 | FR-002 | Register a new teaching skill with proficiency level. | Skill appears on the mentor profile and in learner search. |
| TC-04 | FR-002 | Remove a registered skill. | Skill disappears from profile and from search results. |
| TC-05 | FR-003 | Search a skill offered by a mentor with open slots. | That mentor is returned in the result list. |
| TC-06 | FR-003 | Search a skill whose only mentor has zero availability. | That mentor is not returned as bookable. |
| TC-07 | FR-004 | Book an available slot with a balance of 2 credits. | Booking created; slot marked unavailable; 1 credit held. |
| TC-08 | FR-004 | Attempt to book with a balance of 0 credits. | Booking rejected with a credits-required message; slot stays free. |
| TC-09 | FR-004 | Two learners confirm the same slot concurrently. | Exactly one booking succeeds; the other is told the slot is taken. |
| TC-10 | FR-005 | Both participants confirm completion and submit ratings. | Session marked Verified; credit transfer triggered. |
| TC-11 | FR-005 | Only the mentor confirms; the learner does not. | Session remains unverified; no credit transferred. |
| TC-12 | NFR-001 | Book a session and inspect the subscribed iCal feed. | Event appears with correct date, time and duration within 5 minutes. |
| TC-13 | NFR-001 | Book a session as a user in IST and read the feed. | Time is rendered in the member's local timezone, not UTC. |
| TC-14 | NFR-002 | Attempt a direct balance write outside a session transaction. | Attempt rejected and written to the audit log. |
| TC-15 | NFR-002 | Attempt to modify another member's balance. | Attempt rejected; no balance change; audit entry created. |

---

## 4. Coverage Summary

| Measure | Count | Coverage |
|---|---|---|
| Requirements defined | 7 (5 FR + 2 NFR) | — |
| Requirements mapped to a use case | 7 | 100% |
| Requirements mapped to a component | 7 | 100% |
| Requirements mapped to a Jira story | 7 | 100% |
| Requirements with at least one test case | 7 | 100% |
| Use cases without a parent requirement | 0 | — |
| Test cases without a parent requirement | 0 | — |

---

## 5. Known Gaps

Two scenarios surfaced during alternate/exception flow analysis that no current requirement covers. They are recorded here rather than hidden, and would justify additional requirements in a revised specification:

| Gap | Description | Suggested requirement |
|---|---|---|
| G-01 | **Cancellation and refund.** FR-001 covers crediting on completion but says nothing about reversing a held credit when a booking is cancelled. | FR-006: the system shall return a held time credit to the learner when a booking is cancelled before the session start time. |
| G-02 | **Unresolved verification.** FR-005 requires mutual confirmation but does not define what happens when one party never confirms, leaving a credit frozen indefinitely. | FR-007: the system shall release a held credit back to the learner if a session is not mutually confirmed within a defined window. |
