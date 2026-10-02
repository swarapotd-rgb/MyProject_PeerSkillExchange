# 5 — GitHub Copilot Generated Code

Evidence of using GitHub Copilot (or an equivalent AI coding assistant) to generate code for the Peer Skill Exchange & Mentorship Network.

## What this folder needs

| Item | Status |
|---|---|
| Screenshots of Copilot generating code in the editor | To be added |
| Link to the repository containing the generated code | To be added below |
| Short note on what was generated and what was changed by hand | To be added |

## Suggested screenshots

Name them in order so they read as a sequence:

| # | Filename | What it should show |
|---|---|---|
| 1 | `01-copilot-prompt.png` | The comment or prompt written to drive the suggestion |
| 2 | `02-copilot-suggestion.png` | Copilot's inline suggestion before accepting it |
| 3 | `03-generated-code.png` | The accepted code in the file |
| 4 | `04-code-running.png` | The code executing, or its test output |

## Generated code repository

> Replace this line with the repository link once the code is pushed.

**Repository:** `<add link here>`

## What to generate

The requirements in [`../1-RE`](../1-RE) map directly onto implementable pieces. Any of these is a reasonable target:

| Requirement | Suggested Copilot task |
|---|---|
| FR-001 | A `TimeCreditLedger` class with `credit()`, `debit()` and `hold()` methods |
| FR-002 | A skill registration model with duplicate validation |
| FR-003 | A mentor search function filtering by skill and availability |
| FR-004 | A booking function that checks the credit balance before reserving a slot |
| FR-005 | A verification function requiring confirmation from both participants |
| NFR-001 | An iCal feed generator for a member's scheduled sessions |
| NFR-002 | An access check that rejects balance writes from outside the verification service |

FR-004 is the most useful one to demonstrate, since it has the clearest pass/fail behaviour: booking must succeed with a balance of 1 or more and be rejected at 0.

## Note on honesty

Record what Copilot actually produced, including anything it got wrong that had to be corrected. A note saying "the generated booking function did not check the credit balance, so that condition was added by hand" is worth more than a screenshot of code that looks perfect.
