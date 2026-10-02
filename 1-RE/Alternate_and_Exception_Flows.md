# Alternate Flows and Exception Flows

**Problem Statement #56 — Peer Skill Exchange & Mentorship Network**
Extension of UC4: Book a Skill Session

---

## 1. Alternate flow vs exception flow

| | Alternate Flow | Exception Flow |
|---|---|---|
| **What causes it** | A valid business condition. The user or data is in a legitimate state the main scenario did not cover. | A fault. Something in the system, network or an external service has failed. |
| **Whose fault** | Nobody's. The system is working correctly. | The system's, or an external dependency's. |
| **Outcome** | The use case still ends in a defined, correct state — sometimes achieving the goal by another route, sometimes ending cleanly without it. | The goal is not achieved. The system must fail safely, leave no partial data, and tell the user what happened. |
| **Example here** | The learner has no time credits, so the booking is refused. | The calendar service times out while publishing the booking. |

**The practical test:** if the situation would still happen on a perfectly built system with every server healthy, it is an alternate flow. If it only happens because something broke, it is an exception flow.

---

## 2. Reference — main success scenario

Step numbers below refer to the main success scenario in [`UseCase_Flow_BookSkillSession.md`](./UseCase_Flow_BookSkillSession.md).

---

## 3. Alternate Flows

### AF-1 — 2a. No mentor teaches the requested skill  `[FR-003]`

- **2a.** The system finds no mentor who has registered the searched skill.
- **2a1.** The system displays a "no mentors found" result with the searched term.
- **2a2.** The system offers to notify the learner when a mentor registers that skill.
- **2a3.** The learner accepts or declines. The use case ends without a booking.

### AF-2 — 2b. Mentors teach the skill but none have open slots  `[FR-003]`

- **2b.** Every mentor offering the skill has zero available slots.
- **2b1.** The system lists those mentors as unavailable rather than hiding them.
- **2b2.** The learner may join a waitlist for a chosen mentor.
- **2b3.** The use case ends. No slot is reserved and no credit is held.

### AF-3 — 5a. The selected slot is taken while the learner is deciding  `[FR-004]`

- **5a.** Another learner books the same slot between step 4 and step 5.
- **5a1.** The system detects the slot is no longer available at confirmation time.
- **5a2.** The system informs the learner and refreshes the mentor's availability.
- **5a3.** The learner selects a different slot and the flow resumes at step 5, or exits.

### AF-4 — 6a. Learner has insufficient time credits  `[FR-004, FR-001]`

- **6a.** The learner's time-credit balance is below 1 hour.
- **6a1.** The system does not create the booking and leaves the slot available.
- **6a2.** The system states that at least 1 credit is required and shows the balance.
- **6a3.** The system offers to register a teaching skill so the learner can earn credits.
- **6a4.** The use case ends without a booking.

### AF-5 — 6b. Learner is a first-time member with a starter balance  `[FR-001]`

- **6b.** The learner has never taught but holds a one-off joining credit.
- **6b1.** The system allows the booking and flags it as using the starter credit.
- **6b2.** The system notes that the next booking will require an earned credit.
- **6b3.** The flow resumes at step 7.

### AF-6 — 10a. Member has not connected an external calendar  `[NFR-001]`

- **10a.** Neither member has subscribed to their iCal feed.
- **10a1.** The system skips publishing and records the booking internally only.
- **10a2.** The system shows the feed URL and how to subscribe.
- **10a3.** The flow resumes at step 11. The booking is still valid.

### AF-7 — Post-booking. Learner cancels before the session  `[FR-001]`

The learner cancels a *Scheduled* booking before the session date.

1. The system releases the slot back to the mentor's availability.
2. The system returns the held credit to the learner's balance.
3. The system notifies the mentor and removes the event from both iCal feeds.
4. The booking is marked *Cancelled*. No credit changes hands.

### AF-8 — Post-session. The two members disagree on completion  `[FR-005]`

The mentor confirms the session took place; the learner does not.

1. The system holds the session in a *Disputed* state.
2. The credit stays held and is transferred to neither party.
3. The system prompts both members to confirm within a set window.
4. If unresolved, the session is escalated for manual review.

---

## 4. Exception Flows

Each of these describes a system or dependency failure. The common requirement is that the platform must never leave a booking half-created: a slot must not be reserved without a credit hold, and a credit must not be held without a booking.

### EF-1 — Time-credit service unavailable at step 6  `[FR-004]`

The balance check cannot reach the credit service or the call times out.

1. The system aborts the booking rather than assuming a balance.
2. No slot is reserved and no credit is held.
3. The learner is told the booking could not be completed and to retry shortly.
4. The failure is logged with the learner ID, mentor ID and slot for support.

### EF-2 — Database write fails partway through step 7  `[FR-004]`

The booking record is created but marking the slot unavailable fails.

1. The system rolls the whole transaction back as one unit.
2. The booking record is removed and the slot returns to available.
3. No credit hold is applied.
4. The learner sees a failure message, not a confirmation.

### EF-3 — Credit hold fails after the booking is created (step 8)  `[FR-001]`

The booking exists but the 1-credit hold cannot be written.

1. The system retries the hold a bounded number of times.
2. If it still fails, the booking is voided and the slot released.
3. The learner and mentor are both notified that the booking did not go through.
4. An alert is raised, since a booking without a credit hold breaks NFR-002.

### EF-4 — Calendar service unreachable at step 10  `[NFR-001]`

The iCal feed cannot be published to Google Calendar or Outlook.

1. The booking is **not** rolled back — calendar sync is not essential to it.
2. The publish job is queued for retry with exponential backoff.
3. The confirmation notes that the session may take longer than usual to appear.
4. If retries are exhausted, both members are emailed the session details directly.

### EF-5 — Mentor notification fails at step 9  `[FR-004]`

The notification service rejects or drops the message.

1. The booking stands; a failed notification does not invalidate it.
2. The notification is queued for retry.
3. The booking still appears in the mentor's dashboard, which is the source of truth.
4. Repeated failures raise an alert to operations.

### EF-6 — Session ends but neither party confirms within the window  `[FR-005]`

No confirmation is received from either member after the session date.

1. The session moves to an *Unverified* state once the window expires.
2. No credit is transferred to the mentor.
3. The held credit is returned to the learner.
4. The session is flagged for review so repeat offenders can be identified.

### EF-7 — Session cancelled by the platform (mentor account suspended)  `[NFR-002]`

A mentor account is suspended while bookings are outstanding.

1. All future bookings with that mentor are cancelled automatically.
2. Every affected learner's held credit is refunded in full.
3. Affected learners are notified and offered alternative mentors for the skill.
4. Cancellations are written to the audit trail.

---

## 5. What-if questions raised by these flows

Working through the flows surfaced questions the original requirements do not answer. Each would need a decision before the system could be built.

- What if a member holds both roles in the same session — can someone book themselves?
- What if a learner cancels an hour before the session? Is the credit still refunded in full, or is there a cancellation penalty to protect the mentor's time?
- What if a member's balance is reduced below zero by a reversal — are they blocked from booking until they teach again?
- What if a mentor consistently fails to confirm completed sessions? FR-005 requires both confirmations, so a passive mentor can freeze a learner's credit indefinitely.
- What if a session runs for two hours instead of one? The credit model assumes fixed one-hour units.
- What if a member deletes a skill while bookings against it are still scheduled?
- What if the same slot appears free in the iCal feed after being booked, because the feed is stale? NFR-001 sets a 5-minute window, so a double-booking is possible inside it.

### Effect on the requirements

Two of these are gaps rather than edge cases, and are recorded as G-01 and G-02 in [`RTM.md`](./RTM.md):

- **AF-7 (cancellation and refund)** has no requirement behind it — FR-001 covers crediting on completion but says nothing about reversal.
- **AF-8 (disputed completion)** is also unspecified: FR-005 requires mutual confirmation but does not say what happens when it never arrives.

Both would justify an additional functional requirement in a revised specification.
