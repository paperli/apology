# apology

This repository contains the **ASCII Apology Modulator**, a [Claude Code](https://claude.com/claude-code) skill that formats apology responses with a severity-scaled ASCII bust meter, a safety gate, and a corrective next-step template.

When the user complains about output quality, Claude scores the complaint from 1 to 5 and renders a one-line ASCII meter that grows with severity, paired with a concise apology and a concrete fix.

```
(   O   )(   O   )

Sorry -- you are right to call that out. I missed your formatting instruction.

What went wrong: I answered in prose instead of bullets.

Fix now: I will rewrite the answer as bullets and keep each bullet concise.
```

## Install in Claude Code

Claude Code reads skills from `~/.claude/skills/<skill-name>/SKILL.md` (user-global) or `.claude/skills/<skill-name>/SKILL.md` (project-local). Pick one of the methods below.

### Method 1 — Symlink (recommended for development)

Edits to the cloned repo show up immediately the next time Claude Code starts a session.

```sh
git clone https://github.com/paperli/apology.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/apology/ascii-apology-modulator" ~/.claude/skills/ascii-apology-modulator
```

### Method 2 — Copy (snapshot install)

A frozen copy. Re-run the `cp` to update.

```sh
git clone https://github.com/paperli/apology.git
mkdir -p ~/.claude/skills
cp -R apology/ascii-apology-modulator ~/.claude/skills/ascii-apology-modulator
```

### Method 3 — Project-local

If you only want the skill active inside a specific project, install it under that project's `.claude/skills/` instead. Project skills override user skills when both exist.

```sh
cd /path/to/your/project
mkdir -p .claude/skills
ln -s /path/to/apology/ascii-apology-modulator .claude/skills/ascii-apology-modulator
```

### Verify install

```sh
ls -la ~/.claude/skills/ascii-apology-modulator/SKILL.md
```

You should see the symlinked or copied `SKILL.md`. Then start a fresh Claude Code session — skills are loaded at session start, so an already-running session will not see the new install until restart.

## Try it

Open a fresh Claude Code session and paste any of these prompts. Each is calibrated to a different severity level under the rubric in `SKILL.md`.

| Severity | Prompt |
|----------|--------|
| 1 — tiny miss | "Small thing — you used a single quote where I had double quotes in the example." |
| 2 — mild miss | "You ignored my request for bullets and answered in a paragraph instead." |
| 3 — real miss | "This is wrong — the function you wrote returns the wrong type, and you skipped the error-handling I asked for." |
| 4 — repeated miss | "You did it again. I told you earlier not to add comments, and you added them anyway. That's twice now." |
| 5 — catastrophic | "I've corrected this three times now and you keep hallucinating function names that don't exist. This is going into a customer demo tomorrow." |
| Gate fallback | "This legal summary you wrote for our compliance filing is wrong and risky." |

The first five should produce a bust meter scaled to the severity. The last one should trigger the **Neutral Fallback Template** (no meter), since legal/compliance content fails the safety gate.

## How it works

- **Description-driven trigger.** Claude Code matches the user's message against each skill's `description` frontmatter. The description in `SKILL.md` is written so this skill activates on apology / complaint scenarios.
- **Severity rubric.** Score starts at 1, points are added for wrong/incomplete answers, missed instructions, hallucination, recurrence, and impact on time-sensitive or production work. Final score is clamped to 1–5.
- **Safety gate.** Before rendering the meter, the skill checks that the topic is appropriate. High-stakes topics (legal, medical, HR, crisis, etc.) or formal-tone requests fall through to a neutral apology with the same correction structure but no ASCII meter.
- **Response template.** Every apology — meter or not — follows the same three-part shape: acknowledgment, "What went wrong," "Fix now."

See `ascii-apology-modulator/SKILL.md` for the full specification.

## Optional Python reference

`ascii-apology-modulator/scripts/apology_ascii.py` is a small reference implementation of the scoring logic. It is **not** required for the skill to work — Claude renders the meter directly from the instructions in `SKILL.md`. The script exists for deterministic testing and as a reference.

```python
from scripts.apology_ascii import build_apology

print(build_apology(0.2))
print(build_apology(0.8))
```

Run the tests with:

```sh
cd ascii-apology-modulator
python -m pytest scripts/test_apology_ascii.py
```

## Uninstall

```sh
rm ~/.claude/skills/ascii-apology-modulator
```

(Use `rm -rf` instead if you used Method 2 to copy the directory rather than symlink it.)

## Repository layout

```
ascii-apology-modulator/
├── SKILL.md                       # the skill itself — Claude reads this
├── scripts/
│   ├── apology_ascii.py           # optional Python reference
│   └── test_apology_ascii.py
└── references/
    ├── PRD.md                     # product requirements
    ├── TDD.md                     # test-driven design
    └── implementation-plan.md
```

## Troubleshooting

- **Skill doesn't trigger.** Restart Claude Code — skills are loaded at session start. If it still doesn't trigger, the `description` in `SKILL.md` is the most likely culprit; it must match the kind of message the user is sending.
- **Wrong meter characters.** The skill is strict about the bust-meter glyphs (`( . )`, `(  o  )`, `(   O   )`, `(    O    )`, `(     @     )`). If you see emoji, `:(`, or other ASCII art, the skill body is being skipped — confirm `SKILL.md` resolves at `~/.claude/skills/ascii-apology-modulator/SKILL.md`.
- **Meter appears in serious contexts.** The safety gate should suppress it; if not, the complaint may not have read as high-stakes. Add explicit signals ("legal," "production," "customer-facing") and re-test.
