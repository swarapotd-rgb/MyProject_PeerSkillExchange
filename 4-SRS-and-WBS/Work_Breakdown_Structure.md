# Work Breakdown Structure (WBS)

**Peer Skill Exchange & Mentorship Network** — Problem Statement #56

The WBS decomposes the project into deliverable-oriented work packages. Levels 1–2 mirror the Epics created in Jira, so the plan and the tracker stay in step. Effort is given in story points using the Fibonacci scale, matching the Scrum backlog (37 points total across the build work packages).

---

## 1. WBS Hierarchy

```
1.0  Peer Skill Exchange & Mentorship Network
│
├── 1.1  Requirements Engineering
│    ├── 1.1.1  Scenario analysis and stakeholder identification
│    ├── 1.1.2  Elicit and draft functional requirements (FR-001 … FR-005)
│    ├── 1.1.3  Elicit and draft non-functional requirements (NFR-001, NFR-002)
│    ├── 1.1.4  Peer critique and revision
│    ├── 1.1.5  Actor and use-case extraction
│    ├── 1.1.6  UML use-case diagram (include / extend)
│    ├── 1.1.7  Use-case flow for Book Skill Session
│    ├── 1.1.8  Alternate and exception flow analysis
│    └── 1.1.9  Requirements traceability matrix
│
├── 1.2  Design
│    ├── 1.2.1  Layered architecture definition
│    ├── 1.2.2  Component responsibility allocation
│    ├── 1.2.3  Data model design
│    ├── 1.2.4  Architectural decision records (AD-1 … AD-3)
│    └── 1.2.5  Deployment view
│
├── 1.3  Skill Catalogue & Mentor Discovery        [Epic 1]
│    ├── 1.3.1  Register Teaching Skill                       (FR-002, 3 pts)
│    │    ├── 1.3.1.1  Skill-entry form with proficiency level
│    │    ├── 1.3.1.2  Duplicate skill validation
│    │    └── 1.3.1.3  Display registered skills on mentor profile
│    └── 1.3.2  Search for a Mentor                           (FR-003, 5 pts)
│         ├── 1.3.2.1  Skill search query
│         ├── 1.3.2.2  Filter out mentors with no available slots
│         └── 1.3.2.3  Render results list with ratings
│
├── 1.4  Session Scheduling & Booking              [Epic 2]
│    ├── 1.4.1  Book a Skill Session                          (FR-004, 8 pts)
│    │    ├── 1.4.1.1  Display mentor's available slots
│    │    ├── 1.4.1.2  Check learner holds ≥ 1 time credit
│    │    ├── 1.4.1.3  Mark booked slot unavailable
│    │    └── 1.4.1.4  Notify mentor of new booking
│    └── 1.4.2  Sync Sessions to External Calendar            (NFR-001, 5 pts)
│         ├── 1.4.2.1  Generate per-member iCal export feed
│         ├── 1.4.2.2  Publish feed URL in account settings
│         └── 1.4.2.3  Verify against Google Calendar and Outlook
│
├── 1.5  Session Verification & Feedback           [Epic 3]
│    └── 1.5.1  Verify Session and Submit Rating              (FR-005, 8 pts)
│         ├── 1.5.1.1  Dual-confirmation flow (learner + mentor)
│         ├── 1.5.1.2  Block verification if a confirmation is missing
│         ├── 1.5.1.3  Capture 1–5 mutual rating with optional comment
│         └── 1.5.1.4  Trigger credit transfer on successful verification
│
├── 1.6  Time-Credit Economy & Integrity           [Epic 4]
│    ├── 1.6.1  Maintain Time-Credit Balance                  (FR-001, 5 pts)
│    │    ├── 1.6.1.1  Credit 1 hour to mentor on verification
│    │    ├── 1.6.1.2  Debit 1 hour from learner on verification
│    │    └── 1.6.1.3  Display current balance on member dashboard
│    └── 1.6.2  Protect Time-Credit Integrity                 (NFR-002, 3 pts)
│         ├── 1.6.2.1  Restrict balance writes to the verification service
│         ├── 1.6.2.2  Reject and log all other modification attempts
│         └── 1.6.2.3  Write an audit trail for every balance change
│
├── 1.7  Quality Assurance
│    ├── 1.7.1  Test case design (TC-01 … TC-15)
│    ├── 1.7.2  Defect logging in the bug tracker
│    ├── 1.7.3  Defect triage and prioritisation
│    └── 1.7.4  Fix verification and regression retest
│
└── 1.8  Project Management
     ├── 1.8.1  Jira Kanban project setup
     ├── 1.8.2  Jira Scrum project setup
     ├── 1.8.3  Sprint 1 planning and execution (21 pts)
     ├── 1.8.4  Sprint 2 planning and execution (16 pts)
     ├── 1.8.5  Burndown analysis
     └── 1.8.6  Repository and documentation
```

---

## 2. Work Package Register

| WBS | Work Package | Deliverable | Requirement | Points |
|---|---|---|---|---|
| 1.3.1 | Register Teaching Skill | Skill registration with validation | FR-002 | 3 |
| 1.3.2 | Search for a Mentor | Filtered mentor search | FR-003 | 5 |
| 1.4.1 | Book a Skill Session | Booking with credit check and slot lock | FR-004 | 8 |
| 1.4.2 | Sync to External Calendar | iCal feed per member | NFR-001 | 5 |
| 1.5.1 | Verify Session and Rate | Dual confirmation + rating | FR-005 | 8 |
| 1.6.1 | Maintain Time-Credit Balance | Credit / debit on verification | FR-001 | 5 |
| 1.6.2 | Protect Time-Credit Integrity | Write restriction + audit log | NFR-002 | 3 |
| | | | **Total** | **37** |

---

## 3. Sprint Allocation

| Sprint | Work packages | Points | Sprint goal |
|---|---|---|---|
| **Sprint 1** | 1.6.1, 1.4.1, 1.3.1, 1.3.2 | 21 | A learner can register a teaching skill, find a mentor, and book a session against their time-credit balance. |
| **Sprint 2** | 1.5.1, 1.4.2, 1.6.2 | 16 | Sessions are verified with mutual ratings, time credits settle correctly, and bookings sync to external calendars. |

Sprint 1 was sequenced first because every Sprint 2 work package depends on it. Sessions cannot be verified before they can be booked, and credits cannot settle before the balance mechanism exists — so the dependency chain, not an even point split, drove the allocation.

---

## 4. Dependencies

| Work package | Depends on | Reason |
|---|---|---|
| 1.3.2 Search for a Mentor | 1.3.1 Register Teaching Skill | There is nothing to search until skills exist. |
| 1.4.1 Book a Skill Session | 1.3.2, 1.6.1 | Needs a mentor to book and a balance to check against. |
| 1.4.2 Calendar sync | 1.4.1 | Only a created booking can be published to a feed. |
| 1.5.1 Verify and rate | 1.4.1 | Only a booked session can be verified. |
| 1.6.2 Credit integrity | 1.6.1 | The write restriction protects an existing ledger. |

---

## 5. Estimation Notes

The 8-point packages (1.4.1 and 1.5.1) are the two that combine more than one piece of non-trivial logic — booking couples a credit check with slot locking, and verification couples a two-party state machine with rating capture. The 3-point packages are single-concern. In retrospect 1.3.2 at 5 points was generous: the availability filter turned out to be one condition on an existing query, and 3 would have been closer.
