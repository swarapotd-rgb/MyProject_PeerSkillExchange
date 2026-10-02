# Architectural Notes

**Problem Statement #56 — Peer Skill Exchange & Mentorship Network**

![Layered Architecture](./Architecture_Diagram.png)

---

## 1. Chosen style: Layered (n-tier) architecture

The system is organised into five layers. Each layer may call only the layer directly beneath it, and no layer calls upward.

| Layer | Responsibility |
|---|---|
| 1. Presentation | Browser clients for the Learner Member and Skill Mentor roles. Holds no business rules. |
| 2. API / Security | Single entry point. Routes requests, authenticates the member, resolves their role, applies rate limits. |
| 3. Application | The business logic. One service per functional area, each owning one requirement. |
| 4. Integration | Talks to the outside world — calendar feeds, email and push. Isolated so external failures cannot reach the business layer. |
| 5. Data | Persistent stores. Each application service owns its own store; no service reads another's tables directly. |

### Why this style

The platform is a transactional CRUD-plus-rules system with one hard integrity constraint (the time-credit ledger) and one external dependency (calendar sync). A layered architecture suits it because:

- **The integrity rule needs a single choke point.** NFR-002 requires that *no* balance change can occur outside a verified session transaction. That is only enforceable if exactly one component can write to the ledger. The Credit Ledger Service is that component, and it sits in one place in one layer.
- **The external dependency must not be load-bearing.** NFR-001 is a convenience requirement, not a correctness one. Putting calendar sync in a separate integration layer means a Google Calendar outage degrades the service instead of breaking bookings.
- **The scale is modest.** This is a community platform, not a high-throughput system. Microservices would add deployment and consistency overhead for no benefit at this size, and distributed transactions would make the credit-hold logic markedly harder to get right.

---

## 2. Component responsibilities

| Component | Implements | Notes |
|---|---|---|
| **Skill Catalogue Service** | FR-002 | Owns the register / edit / remove lifecycle for teachable skills, including the duplicate check. |
| **Discovery & Search Service** | FR-003 | Queries the skill catalogue and joins against availability so results exclude mentors with no open slots. |
| **Booking Service** | FR-004 | Orchestrates the booking: calls the Credit Ledger Service for the balance check, locks the slot, writes the booking. All within one transaction. |
| **Verification & Rating Service** | FR-005 | Holds the dual-confirmation state machine and the 1–5 rating. Only this service may declare a session verified. |
| **Credit Ledger Service** | FR-001, NFR-002 | The sole writer to the credit ledger. Exposes hold, transfer and refund operations. Rejects and logs anything else. |
| **Notification Service** | supporting | Raises events for booking, confirmation and cancellation. Failures here never invalidate a booking. |
| **Calendar Integration Adapter** | NFR-001 | Generates per-member iCal feeds. Runs asynchronously with retry and backoff. |

---

## 3. Key architectural decisions

### AD-1 — The credit ledger is append-only with a single writer

**Decision.** Credit balances are not stored as a mutable number. They are derived from an append-only ledger of transactions, and only the Credit Ledger Service may append.

**Why.** NFR-002 demands that 100% of non-transactional balance changes be rejected. A mutable balance column can be updated by any service with a database connection; an append-only ledger behind one service cannot. It also gives the audit trail for free.

**Trade-off.** Reading a balance requires either a running total or a cached projection. Accepted — reads are frequent but cheap to cache, and correctness matters more than read latency here.

### AD-2 — Booking is one transaction; calendar sync is not

**Decision.** The slot lock, booking write and credit hold commit together or not at all. Publishing to the calendar feed happens afterwards, asynchronously.

**Why.** Exception flows EF-2 and EF-3 require that a slot is never reserved without a credit hold, and a credit never held without a booking. That needs a single transaction. Conversely EF-4 requires that a calendar failure leaves the booking intact — so sync must sit outside that transaction.

**Trade-off.** A member may briefly see a confirmed booking that has not yet reached their calendar. NFR-001 already allows a 5-minute window, so this is within the stated requirement.

### AD-3 — Search filters on availability at query time

**Decision.** The Discovery Service joins skills against live slot availability rather than returning all mentors and filtering client-side.

**Why.** FR-003 explicitly requires that only mentors with at least one open slot are displayed. Filtering in the client would return mentors the learner cannot book, which is the defect recorded as BTBPS56-3.

**Trade-off.** A heavier query. Acceptable at this scale, and indexable on (skill_id, slot_status).

---

## 4. How the architecture handles the exception flows

| Exception | Architectural response |
|---|---|
| EF-1 Credit service unavailable | Booking Service aborts before locking the slot. No partial state. |
| EF-2 Database write fails mid-booking | Single transaction rolls back slot lock, booking and hold together. |
| EF-3 Credit hold fails after booking | Bounded retry, then the whole transaction is voided and an alert raised. |
| EF-4 Calendar unreachable | Integration layer queues for retry. Layer 3 is unaffected; the booking stands. |
| EF-5 Notification fails | Notification Service failure is non-blocking. The mentor dashboard remains the source of truth. |
| EF-6 No confirmation in window | Verification Service expires the session and instructs the Credit Ledger Service to refund the hold. |
| EF-7 Mentor suspended | Cascading cancellation through the Booking Service; refunds via the ledger; entries written to the audit log. |

---

## 5. Deployment view (indicative)

```
[ Browser ]
     |  HTTPS
[ API Gateway ]  ── auth, routing, rate limiting
     |
[ Application services ]  ── single deployable, modular internally
     |            \
[ Relational DB ]  [ Job queue ]  ── async calendar + notification workers
                          |
                   [ Google Calendar / Outlook ]
```

A single deployable unit containing the six services, backed by one relational database with schema separation per service, plus a job queue for the asynchronous integration work. This keeps transactional integrity simple while leaving each service independently extractable later if load requires it.
