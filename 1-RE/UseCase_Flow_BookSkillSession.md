# Use-Case Flow — UC4: Book a Skill Session

**Problem Statement #56 — Peer Skill Exchange & Mentorship Network**

---

## Identification

| Field | Value |
|---|---|
| Use Case ID | UC4 |
| Use Case Name | Book a Skill Session |
| Primary Actor | Learner Member |
| Secondary Actors | Skill Mentor (notified), Calendar Service (external system) |
| Related Requirements | FR-003, FR-004, FR-001 (credit hold), NFR-001 (calendar sync) |
| Trigger | The learner decides to learn a skill and opens the mentor search. |
| Scope / Level | Peer Skill Exchange Platform / User-goal level |

---

## Preconditions

1. The learner is registered on the platform and is logged in with a valid account.
2. The learner holds a time-credit balance of at least 1 hour.
3. At least one mentor has registered the requested skill (FR-002).
4. The selected mentor has published at least one available time slot.

---

## Main Success Scenario

1. The **learner** selects "Find a Mentor" and enters the name of the skill they want to learn.
2. The **system** displays every mentor who has registered that skill and has at least one available time slot, with each mentor's average rating.
3. The **learner** selects a mentor and requests to view their availability.
4. The **system** displays the mentor's available time slots.
5. The **learner** selects a time slot and confirms the booking request.
6. The **system** checks the learner's time-credit balance *(`<<include>>` Check Time-Credit Balance)* and confirms it is at least 1 hour.
7. The **system** creates the session booking with status *Scheduled* and marks the selected slot unavailable to other learners.
8. The **system** places a hold of 1 time credit on the learner's balance.
9. The **system** notifies the mentor that a session has been booked.
10. The **system** publishes the session to the learner's and mentor's iCal feeds *(`<<extend>>` Sync Session to External Calendar)*.
11. The **system** displays a booking confirmation showing the skill, mentor name, date, start time and duration.
12. The use case ends successfully.

---

## Alternate Flow — 6a. Insufficient Time Credits

- **6a.** At step 6 the system determines that the learner's time-credit balance is below 1 hour.
- **6a1.** The system does not create the booking and leaves the selected slot available to other learners.
- **6a2.** The system displays a message stating that at least 1 time credit is required to book a session, and shows the learner's current balance.
- **6a3.** The system offers the learner the option to register a teaching skill in order to earn credits (UC1).
- **6a4.** The learner acknowledges the message. The use case ends without a booking being created.

> A complete set of eight alternate flows and seven exception flows is documented separately in [`Alternate_and_Exception_Flows.md`](./Alternate_and_Exception_Flows.md).

---

## Postconditions

**On success:**

1. A session booking exists with status *Scheduled*, linking the learner, the mentor, the skill and the time slot.
2. The booked time slot is no longer offered to other learners.
3. One time credit is held against the learner's balance pending session verification (UC5).
4. The session appears in the subscribed Google Calendar and Outlook feeds of both members within 5 minutes (NFR-001).

**On failure (alternate flow 6a):**

1. No booking record is created.
2. The mentor's time slot remains available.
3. The learner's time-credit balance is unchanged.
