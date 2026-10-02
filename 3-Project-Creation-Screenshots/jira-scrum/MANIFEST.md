# Scrum Project Screenshots

Project: **Scrum_BPS#56** (key `SBPS56`)

The same seven requirements as the Kanban project, rebuilt under a Scrum template so that story-point estimation, sprint planning and burndown reporting could be applied. Backlog total: **37 points**, split 21 / 16 across two sprints.

| # | File | What it shows |
|---|---|---|
| 1 | [`01-backlog-story-points.png`](./01-backlog-story-points.png) | The full backlog with story points assigned on the Fibonacci scale — 3, 5, 8 — totalling 37. Each story carries its Epic label and priority. |
| 2 | [`02-sprint1-planning-selection.png`](./02-sprint1-planning-selection.png) | Sprint planning in progress: the four Sprint 1 stories selected in the backlog before being moved. |
| 3 | [`03-sprint1-planned-21pts.png`](./03-sprint1-planned-21pts.png) | Sprint 1 committed at 21 points, leaving 16 in the backlog for Sprint 2. |
| 4 | [`04-sprint1-board-todo.png`](./04-sprint1-board-todo.png) | Sprint 1 started — all four committed stories in To Do. |
| 5 | [`05-sprint1-board-in-progress.png`](./05-sprint1-board-in-progress.png) | All four stories moved into In Progress. |
| 6 | [`06-sprint1-board-done.png`](./06-sprint1-board-done.png) | Sprint 1 complete — all four in Done, each showing its points and parent Epic. |
| 7 | [`07-sprint1-burndown.png`](./07-sprint1-burndown.png) | **Sprint 1 burndown.** Remaining work steps down 21 → 18 → 13 → 8 → 0, tracking just under the ideal guideline. |
| 8 | [`08-sprint1-burndown-first-attempt.png`](./08-sprint1-burndown-first-attempt.png) | The same sprint before re-running it. All four stories were closed within minutes of starting, so the line fell vertically from 21 to 0 against a week-long guideline — kept as a record of why the sprint was re-simulated over a realistic window. |
| 9 | [`09-complete-sprint-blocked-by-subtasks.png`](./09-complete-sprint-blocked-by-subtasks.png) | Jira refusing to close the sprint because the stories' sub-tasks were still open — the stories were Done but their children were not. |
| 10 | [`10-sprint2-board-todo.png`](./10-sprint2-board-todo.png) | Sprint 2 started with the remaining three stories (16 points) in To Do. |
| 11 | [`11-sprint2-board-in-progress.png`](./11-sprint2-board-in-progress.png) | All three Sprint 2 stories in progress. |
| 12 | [`12-sprint2-burndown.png`](./12-sprint2-burndown.png) | **Sprint 2 burndown.** Steps down 16 → 13 → 8 → 0 — the same shape as Sprint 1, showing a consistent pace across both. |

## Sprint summary

| Sprint | Stories | Committed | Completed | Goal |
|---|---|---|---|---|
| Sprint 1 | 4.1 (5), 2.1 (8), 1.1 (3), 1.2 (5) | 21 | 21 | A learner can register a teaching skill, find a mentor, and book a session against their time-credit balance |
| Sprint 2 | 3.1 (8), 2.2 (5), 4.2 (3) | 16 | 16 | Sessions are verified with mutual ratings, credits settle, bookings sync to external calendars |

Sprint 1 was sequenced first because every Sprint 2 story depends on it — a session cannot be verified before it can be booked, and credits cannot settle before the balance mechanism exists.

## What the burndowns show

In both sprints the remaining-work line sat **below** the guideline, meaning work completed faster than the ideal burn rate. In a real project that reads as under-commitment: more could have been pulled into the sprint. The line also descends in discrete steps rather than smoothly, because progress only registers when a whole story closes — finer-grained stories would give a smoother line and earlier warning if something were slipping.
