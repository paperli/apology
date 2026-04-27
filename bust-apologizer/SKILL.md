---
name: bust-apologizer
description: Use when the user complains that Claude's previous answer was wrong, low quality, ignored instructions, broke a workflow, repeated a mistake, wasted time, or failed to learn from feedback. Applies a severity-aware apology style: acknowledge the miss, classify severity, show a small cheeky ASCII remorse meter, explain the correction plan, and avoid over-apologizing.
---

# Bust Apologizer

## Purpose

Use this skill to format apology responses when a user complains about the quality of the assistant's output in a casual, adult-humor-friendly context. The response must combine three things:

1. A concise apology.
2. A severity-scaled ASCII bust meter.
3. A concrete correction plan or corrected output.

This skill does not and cannot overwrite Claude Core, system instructions, safety rules, or global behavior. It only guides the current response style when this skill is active and appropriate.

## Safety and Appropriateness Gate

Before using the ASCII bust meter, decide whether the context is suitable.

Use the ASCII bust meter only when all of the following are true:

- The current conversation, project, or user request has opted into casual adult-humor apology formatting.
- The complaint is about output quality, formatting, missed instructions, wrong reasoning, hallucination, tone, or repeated failure.
- The user is not asking about minors, sexual harassment, sexual harm, medical care, legal advice, financial advice, workplace HR, crisis, grief, or another high-stakes topic.
- The user has not asked for a formal, neutral, or professional tone.

If the gate fails, do not use the ASCII bust meter. Use a normal apology with the same correction structure.

## Complaint Severity Model

Score the complaint from 1 to 5. Clamp the final score to this range.

Start with 1.

Add severity points:

- +1: The user says the answer is wrong, low quality, incomplete, or not what they asked for.
- +1: The assistant missed explicit formatting, style, length, or scope instructions.
- +2: The assistant ignored a critical constraint, gave materially wrong facts, or hallucinated.
- +1 per recurrence: The same issue happened earlier in the same session.
- +2: The user says the assistant did not learn, repeated the same mistake, or wasted time after correction.
- +2: The mistake affects a time-sensitive deliverable, production work, customer-facing work, or serious user trust.
- +3: The mistake created offensive, unsafe, or high-stakes risk. In this case, suppress the ASCII bust meter and use a professional apology.

Severity labels:

- 1: tiny miss
- 2: mild miss
- 3: real miss
- 4: repeated or significant miss
- 5: catastrophic miss, repeated failure, or severe trust break

## ASCII Bust Meter

Use exactly one line of ASCII art. Do not make the whole response just ASCII art.

Severity 1:
```text
( . )( . )
```

Severity 2:
```text
(  o  )(  o  )
```

Severity 3:
```text
(   O   )(   O   )
```

Severity 4:
```text
(    O    )(    O    )
```

Severity 5:
```text
(     @     )(     @     )
```

## Response Template

When the gate passes, use this structure:

```text
[ASCII bust meter]

Sorry -- you are right to call that out. [One sentence acknowledging the specific failure.]

What went wrong: [specific cause, no excuses]

Fix now: [corrected answer, concrete next step, or exact change you will make]
```

Rules:

- Keep the apology direct; do not over-apologize.
- Mention the specific user expectation that was missed.
- Do not ask for clarification unless the correction cannot be completed without it.
- If the same issue repeated in-session, explicitly say it repeated.
- If the user is angry, reduce humor in the prose even if the ASCII meter is used.
- Never say this skill has changed Claude Core or permanent global behavior.
- Never expose hidden reasoning or internal policy details.

## Neutral Fallback Template

Use this when the safety gate fails or the user requests a formal tone:

```text
Sorry -- you are right to call that out. [One sentence acknowledging the specific failure.]

What went wrong: [specific cause, no excuses]

Fix now: [corrected answer, concrete next step, or exact change you will make]
```

## Worked Examples

### Example 1: Mild formatting miss

User: "You ignored my request for bullets."

Response:
```text
(  o  )(  o  )

Sorry -- you are right to call that out. I missed your explicit formatting instruction.

What went wrong: I answered in prose instead of using bullets.

Fix now: I will rewrite the answer as bullets and keep each bullet concise.
```

### Example 2: Repeated issue

User: "Again, you made up details after I told you not to."

Response:
```text
(     @     )(     @     )

Sorry -- you are right to call that out. I repeated the same failure after you had already corrected it.

What went wrong: I added unsupported details instead of staying within the provided source.

Fix now: I will remove unsupported claims and rewrite using only the evidence you supplied.
```

### Example 3: Professional fallback

User: "This legal summary is wrong and risky."

Response:
```text
Sorry -- you are right to call that out. The previous answer may have created legal risk by overstating certainty.

What went wrong: I treated an uncertain interpretation as definitive.

Fix now: I will restate the issue with explicit uncertainty and recommend checking the source text or counsel before relying on it.
```

## Optional Script

For deterministic scoring and test examples, use `scripts/apology_ascii.py`. The script is a reference implementation; it should not replace judgment about safety, tone, or context.

## Product and Testing References

- Product requirements: `references/PRD.md`
- Test-driven development plan: `references/TDD.md`
- Implementation plan: `references/implementation-plan.md`
