# 6 — Software Testing Tools Practice

The lab provides a repository containing a game application with four test cases. The exercise is to run the tests, find the bug, fix it using AI-assisted ("vibe") coding, retest, and share the fixed repository link.

## What this folder needs

| Item | Status |
|---|---|
| Link to the provided game application repository | To be added |
| Screenshot of the four tests failing before the fix | To be added |
| The diagnosis — what the bug actually was | To be added |
| Screenshot of the AI tool being used to produce the fix | To be added |
| Screenshot of the tests passing after the fix | To be added |
| Link to the fixed repository | To be added |

## Links

**Provided repository:** `<add link here>`

**Fixed repository:** `<add link here>`

## Suggested screenshots

| # | Filename | What it should show |
|---|---|---|
| 1 | `01-tests-failing.png` | Test runner output with the failing case(s) |
| 2 | `02-bug-located.png` | The offending line in the source |
| 3 | `03-ai-fix-suggestion.png` | The AI tool proposing the patch |
| 4 | `04-patch-applied.png` | The diff or the corrected code |
| 5 | `05-tests-passing.png` | All four tests green after the fix |

## Process to follow

1. **Read the provided README first.** It explains what the game does, how to run the tests, and how the testing process is meant to work. Follow it rather than guessing.
2. **Run the tests before changing anything.** The failing output is evidence, and without a "before" screenshot the "after" proves nothing.
3. **Read the failure message properly.** Which test failed, on what input, with what expected versus actual value. This usually points at the bug faster than reading the whole source.
4. **Ask the AI tool with the failure as context,** not just "fix my code". Paste the failing test and the function it exercises.
5. **Verify the fix yourself.** An AI patch that makes a test pass is not automatically correct — check that it fixes the cause rather than special-casing the test input.
6. **Retest the full suite,** not only the test that was failing. A patch that breaks a previously passing test is a regression.
7. **Commit the fix with a message that names the bug,** then record the repository link above.

## Write-up

When the fix is done, add a short note here covering:

- What the four test cases check
- Which one failed and why
- What the root cause was, in one or two sentences
- What the patch changed
- Whether the AI tool's first suggestion was correct, or needed adjusting

That last point is the one most worth being honest about — a note saying the first suggested patch only masked the symptom and a second attempt was needed shows the testing process actually did its job.
