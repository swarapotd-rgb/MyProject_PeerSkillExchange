# Bug Tracker Screenshots

Project: **BugTracker_BPS#56** (key `BTBPS56`)

Six defects raised against the Peer Skill Exchange platform. Every bug is written against a specific requirement from [`../../1-RE`](../../1-RE), with steps to reproduce, expected behaviour and actual behaviour.

| # | File | What it shows |
|---|---|---|
| 1 | [`01-template-selection.png`](./01-template-selection.png) | The Jira template picker. Kanban was chosen over the two Service Management options — those are helpdesk ticketing and add a request portal the lab does not need. |
| 2 | [`02-bugtracker-created.png`](./02-bugtracker-created.png) | The empty board immediately after creating the project. |
| 3 | [`03-bug-board.png`](./03-bug-board.png) | All six bugs on the board, spread across To Do, In Progress and Done. |
| 4 | [`04-bug-list.png`](./04-bug-list.png) | List view with each bug's priority, status and resolution. |

## Bugs reported

| ID | Bug | Breaks | Priority | Status |
|---|---|---|---|---|
| BTBPS56-1 | Booking succeeds when learner has zero time credits | FR-004 | Highest | In Progress |
| BTBPS56-2 | Session marked verified after only one participant confirms | FR-005 | Highest | In Progress |
| BTBPS56-3 | Mentor search returns mentors with no available slots | FR-003 | High | Done |
| BTBPS56-4 | iCal feed shows session time in UTC, not local timezone | NFR-001 | High | To Do |
| BTBPS56-5 | Time credit not refunded when a booking is cancelled | FR-001 | High | To Do |
| BTBPS56-6 | Same teaching skill can be registered twice on one profile | FR-002 | Medium | Done |

## Why the board looks the way it does

The two **Highest** bugs are in progress because both break the time-credit economy directly — one lets a learner book with no credits, the other releases a credit without both parties confirming. Those are the defects that would make the platform unusable.

The two **Done** bugs were quick fixes: a filter condition on the search query, and a duplicate check on the skill-entry form.

The two remaining **To Do** bugs are real but less urgent. The timezone offset is a display fault in the feed rather than in the booking itself, and the missing refund needs the cancellation flow designed first — which is itself a gap noted in [`../../1-RE/Alternate_and_Exception_Flows.md`](../../1-RE/Alternate_and_Exception_Flows.md), since FR-001 covers crediting on completion but never reversal.
