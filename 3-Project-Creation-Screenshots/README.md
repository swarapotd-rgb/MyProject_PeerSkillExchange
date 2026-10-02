# 3 — Project Creation Screenshots (GitHub & Jira)

Evidence of the project set up in GitHub and in Jira, covering the Kanban project, the Scrum project with two sprints and burndown charts, and the bug tracker.

## Jira projects created

| Project | Key | Template | Purpose |
|---|---|---|---|
| Kanban_BPS#56 | `KBPS56` | Kanban | Requirements modelled as Epics → Stories → Sub-tasks on a flow board |
| Scrum_BPS#56 | `SBPS56` | Scrum | Same backlog with story points, two sprints and burndown reporting |
| BugTracker_BPS#56 | `BTBPS56` | Kanban | Defects raised against the requirements |

> **Note on project keys.** Jira only accepts letters and numbers in a project key, so the `#` from the naming convention (`KBPS#56`) was omitted from the key while the project *name* keeps it.

## Work item hierarchy (both projects)

```
4 Epics  →  7 User Stories (one per requirement)  →  23 Sub-tasks
```

| Requirement | User Story | Epic | Points |
|---|---|---|---|
| FR-002 | Story 1.1: Register Teaching Skill | Epic 1 | 3 |
| FR-003 | Story 1.2: Search for a Mentor | Epic 1 | 5 |
| FR-004 | Story 2.1: Book a Skill Session | Epic 2 | 8 |
| NFR-001 | Story 2.2: Sync Sessions to External Calendar | Epic 2 | 5 |
| FR-005 | Story 3.1: Verify Session and Submit Rating | Epic 3 | 8 |
| FR-001 | Story 4.1: Maintain Time-Credit Balance | Epic 4 | 5 |
| NFR-002 | Story 4.2: Protect Time-Credit Integrity | Epic 4 | 3 |
| | | **Total** | **37** |

## Sprint results

| Sprint | Committed | Completed | Burndown |
|---|---|---|---|
| Sprint 1 | 21 pts (4 stories) | 21 pts | Stepped 21 → 18 → 13 → 8 → 0, tracking just under the guideline |
| Sprint 2 | 16 pts (3 stories) | 16 pts | Stepped 16 → 13 → 8 → 0 |

## Folder contents

| Folder | What goes here |
|---|---|
| [`github/`](./github) | Screenshots of this repository being created and the folder structure in place |
| [`jira-kanban/`](./jira-kanban) | Kanban project — creation, Epics, stories, sub-tasks, backlog, board |
| [`jira-scrum/`](./jira-scrum) | Scrum project — creation, hierarchy, story points, both sprints, both burndowns |
| [`jira-bugtracker/`](./jira-bugtracker) | Bug tracker board and list |

Each subfolder has a `MANIFEST.md` listing the expected screenshots in order with a caption for each.
