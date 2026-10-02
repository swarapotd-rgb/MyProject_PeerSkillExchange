# Software Requirements Specification (SRS)

**Peer Skill Exchange & Mentorship Network**
Problem Statement #56 · Media, Events & Community

| | |
|---|---|
| Author | Swara Ashish Potdar (PES1UG24CS487) |
| Course | Software Engineering — Individual Project |
| Version | 1.0 |
| Based on | IEEE 830 structure |

---

## 1. Introduction

### 1.1 Purpose

This document specifies the requirements for the Peer Skill Exchange & Mentorship Network, a time-banking platform on which community members teach and learn skills from one another using time credits instead of money. It is written for the project evaluator and for anyone who would implement or test the system.

### 1.2 Scope

The system allows a member to advertise skills they can teach, to find and book sessions with other members, to confirm that sessions took place, and to accumulate and spend time credits earned by teaching. It synchronises booked sessions with external calendar services.

**In scope:** member skill profiles, mentor discovery, session scheduling and booking, session verification, mutual rating, the time-credit ledger, and iCal calendar export.

**Out of scope:** monetary payment of any kind, video conferencing or session delivery itself, long-form course content or curriculum management, and dispute arbitration beyond flagging a session for manual review.

### 1.3 Definitions

| Term | Meaning |
|---|---|
| Time credit | One hour of teaching. The platform's only unit of exchange. |
| Learner Member | A member in the role of receiving instruction in a session. |
| Skill Mentor | A member in the role of giving instruction in a session. |
| Session | A scheduled one-hour teaching appointment between a learner and a mentor. |
| Verified completion | The state reached when both participants have confirmed a session took place and submitted a rating. |
| Credit hold | One credit reserved against a learner's balance at booking time, released on verification or cancellation. |
| iCal feed | A subscribable calendar feed in iCalendar format, consumed by Google Calendar or Outlook. |

### 1.4 References

- `1-RE/Requirements_FR_NFR.md` — the requirements table with acceptance criteria
- `1-RE/RTM.md` — requirements traceability matrix
- `1-RE/UseCase_Flow_BookSkillSession.md` — detailed use-case flow
- `1-RE/Alternate_and_Exception_Flows.md` — alternate and exception flows
- `2-Architectural-Diagram/Architecture_Notes.md` — architectural decisions

---

## 2. Overall Description

### 2.1 Product perspective

The product is a new, self-contained web application. It has one external dependency: calendar services (Google Calendar and Outlook), which it integrates with one-way via iCal export feeds. It does not replace an existing system.

### 2.2 Product functions

At a high level the system shall:

1. Maintain a time-credit balance for every member.
2. Let members register and manage the skills they can teach.
3. Let learners search for mentors by skill.
4. Let learners book available sessions, subject to holding sufficient credits.
5. Require both participants to verify a session and rate each other before credits settle.
6. Publish booked sessions to members' external calendars.

### 2.3 User characteristics

Members are general community users, not technical specialists. No assumption is made about domain expertise beyond the skill each member chooses to teach. Every member may act in both roles — teaching one skill while learning another — so the interface must make the current role obvious.

### 2.4 Constraints

- Time credits are the only medium of exchange; no monetary transaction may be introduced.
- Credits are issued in whole one-hour units.
- Calendar integration is one-way export only. The system does not read members' existing calendars.
- A credit may only be created by a verified teaching session, never granted administratively.

### 2.5 Assumptions and dependencies

- Members have a device with a modern web browser and network access.
- Sessions take place outside the platform — in person or on a third-party video tool. The platform schedules and records them, it does not host them.
- Google Calendar and Outlook continue to support subscribed iCal feeds.
- Both participants act in good faith when confirming completion. Disputes are flagged, not adjudicated.

---

## 3. Specific Requirements

### 3.1 Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR-001 | The system shall maintain a time-credit balance for each member, crediting 1 hour upon verified completion of a teaching session. | High |
| FR-002 | The system shall allow a member to register, edit, and remove the skills they are available to teach, each with a skill name and proficiency level. | High |
| FR-003 | The system shall allow a learner to search registered mentors by skill name and display only mentors who have at least one available time slot. | High |
| FR-004 | The system shall allow a learner holding a time-credit balance of at least 1 hour to book an available slot with a selected mentor, and shall reject the booking otherwise. | Highest |
| FR-005 | The system shall require both the learner and the mentor to confirm completion of a scheduled session and submit a mutual rating (1–5) before the session is marked verified. | High |

Full acceptance criteria and rationale for each requirement are in `1-RE/Requirements_FR_NFR.md`.

### 3.2 Non-Functional Requirements

| ID | Category | Requirement |
|---|---|---|
| NFR-001 | Interoperability | The session scheduling calendar shall sync seamlessly with Google Calendar and Outlook via iCal export feeds, with a booked session appearing in a subscribed feed within 5 minutes. |
| NFR-002 | Security / Integrity | The system shall reject 100% of attempts to alter a member's time-credit balance that do not originate from a verified session transaction, and shall log every rejected attempt. |

### 3.3 External interface requirements

**User interfaces.** Browser-based, responsive. Two primary views — a learner view (search, bookings, balance) and a mentor view (skills, availability, upcoming sessions, balance).

**Software interfaces.** Outbound iCal feed endpoints, one per member, consumable by any iCalendar-compatible client. No inbound calendar read.

**Communications.** All traffic over HTTPS.

### 3.4 Data requirements

| Entity | Key attributes |
|---|---|
| Member | member ID, name, email, credit balance (derived), average rating |
| Skill | skill ID, name |
| TeachingSkill | member ID, skill ID, proficiency level |
| AvailabilitySlot | slot ID, mentor ID, start time, duration, status |
| Session | session ID, learner ID, mentor ID, skill ID, slot ID, status (Scheduled / Verified / Cancelled / Disputed / Unverified) |
| Confirmation | session ID, member ID, confirmed flag, rating (1–5), optional comment |
| CreditTransaction | transaction ID, member ID, session ID, type (hold / transfer / refund), amount, timestamp |
| AuditEntry | timestamp, actor, attempted action, outcome |

---

## 4. Verification

Every requirement in this specification maps to at least one test case. The mapping, together with the test case register and a coverage summary, is maintained in `1-RE/RTM.md`.

Two known specification gaps are recorded there as G-01 (cancellation refund) and G-02 (unresolved verification). Both were identified during alternate and exception flow analysis and would be closed by adding FR-006 and FR-007 in a version 1.1 of this document.
