# 6 — Software Testing Tools (Lab 4: Vibe Coding)

A broken Pygame game was assigned, along with one deliberate bug and three features to add. The bug was found, fixed and retested, and the features were added, all through prompts to an AI coding agent (Google Antigravity).

## Links

| | |
|---|---|
| **Assigned repository** | [SETAPESU26/56_tug_of_war](https://github.com/SETAPESU26/56_tug_of_war) |
| **Fixed repository (my fork)** | [swarapotd-rgb/56_tug_of_war](https://github.com/swarapotd-rgb/56_tug_of_war) |

## What is in `Lab-4/`

| File | What it is |
|---|---|
| [`before.mp4`](./Lab-4/before.mp4) | Gameplay **before** any changes. Mashing A and D quickly, presses get dropped, and the computer wins. |
| [`after.mp4`](./Lab-4/after.mp4) | Gameplay **after** all changes. The bug is gone and all three new features are visible, including Sudden Death at 0:45. |
| [`chat_history.pdf`](./Lab-4/chat_history.pdf) | The full conversation with the AI agent, showing every prompt. |
| [`code/`](./Lab-4/code) | The updated game code. |

## The game

Tug of war in Pygame. The player pulls the rope left by **alternating A and D**. The computer pulls right on its own. Whoever drags the red flag past their line wins. **R** restarts.

## Task 1 — The bug: alternating input deadlock

**What went wrong:** mashing A and D quickly made many presses get ignored. The rope barely moved and the computer won easily.

**Cause:** after each press, the game locked input and only unlocked it when that **same** key was released. When mashing fast, fingers overlap — D gets pressed before A is fully released. That D press arrived while input was still locked, so it was thrown away. About half the presses were lost this way.

**Fix:** the lock was removed. A press now counts if it is a **different** key from the last one. So A → D → A still works, pressing A → A → A still does nothing (the game's rule is unchanged), and overlapping presses are no longer lost.

**Retest:** mashing with overlapping fingers now moves the flag steadily left, and the player can win — shown at the start of `after.mp4`.

## Tasks 2–4 — Features added

| Task | Feature | How it works |
|---|---|---|
| 2 | **AI panic surges** | The closer the flag gets to the player's winning line, the faster and harder the computer pulls. It increases smoothly, not all at once. A red **PANIC!** label shows while it is active. |
| 3 | **Rope and leaning animations** | The rope sags when quiet, and goes tight and wobbles during a hard struggle. Both characters lean back or forward depending on who has the momentum. |
| 4 | **Match timer and Sudden Death** | A live timer at the top. After 45 seconds with no winner, **SUDDEN DEATH!** starts and every pull becomes twice as strong. R resets it all. |

## How it was done

Each task was given to the agent as a separate prompt in one conversation, with the relevant file and the expected behaviour described. After every change, the game was run and tested by hand before moving on to the next task.

One thing that needed care: the bug only appears when key presses **overlap**. Tapping A and D cleanly one at a time works even in the broken version, so the first test run looked fine. Recording the "before" video required mashing the way a real player does, with fingers rolling across the keys.
