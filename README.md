# Bust Apologizer

Bust Apologizer is a playful Claude Skill that adjusts apology style based on how far an assistant response missed the mark. It uses a simple ASCII severity meter to make "my bad" moments more visible without making the apology too heavy.

> 🤡 **For fun only.** This is a joke / hobby project. The "ASCII bust meter" is adult-humor styling, not a serious product. If your context is professional, sensitive, or otherwise inappropriate for casual humor, **do not install this skill** — see [Disclaimer](#disclaimer) below.

When the user complains about output quality, Claude scores the complaint from 1 to 5 and renders a one-line ASCII meter that grows with severity, paired with a concise apology and a concrete fix.

```
(   O   )(   O   )

Sorry -- you are right to call that out. I missed your formatting instruction.

What went wrong: I answered in prose instead of bullets.

Fix now: I will rewrite the answer as bullets and keep each bullet concise.
```

## Install in Claude Code

Bust Apologizer is distributed as a **Claude Code plugin**. The repo also acts as its own single-plugin marketplace, so installation is two commands inside Claude Code:

```
/plugin marketplace add paperli/bust-apologizer
/plugin install bust-apologizer@bust-apologizer
```

Then start a fresh Claude Code session — plugins are loaded at session start, so an already-running session won't see the new install until restart.

### Verify install

In a fresh session, run `/plugin` and look for `bust-apologizer` under **Installed**, or just trigger the skill with one of the prompts in [Try it](#try-it).

### Local development

If you're hacking on the skill itself, clone the repo and load it directly with `--plugin-dir` instead of going through the marketplace:

```sh
git clone https://github.com/paperli/bust-apologizer.git
claude --plugin-dir ./bust-apologizer
```

Edits to `skills/bust-apologizer/SKILL.md` are picked up the next time Claude Code starts with `--plugin-dir`.

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

See `skills/bust-apologizer/SKILL.md` for the full specification.

## Optional Python reference

`skills/bust-apologizer/scripts/apology_ascii.py` is a small reference implementation of the scoring logic. It is **not** required for the skill to work — Claude renders the meter directly from the instructions in `SKILL.md`. The script exists for deterministic testing and as a reference.

```python
from scripts.apology_ascii import build_apology

print(build_apology(0.2))
print(build_apology(0.8))
```

Run the tests with:

```sh
cd skills/bust-apologizer
python -m pytest scripts/test_apology_ascii.py
```

## Uninstall

```
/plugin uninstall bust-apologizer@bust-apologizer
```

Or interactively: `/plugin` → **Installed** → select `bust-apologizer` → uninstall.

## Repository layout

```
bust-apologizer/
├── .claude-plugin/
│   ├── plugin.json                # plugin manifest
│   └── marketplace.json           # makes the repo installable as a marketplace
└── skills/
    └── bust-apologizer/
        ├── SKILL.md               # the skill itself — Claude reads this
        ├── scripts/
        │   ├── apology_ascii.py   # optional Python reference
        │   └── test_apology_ascii.py
        └── references/
            ├── PRD.md             # product requirements
            ├── TDD.md             # test-driven design
            └── implementation-plan.md
```

## Troubleshooting

- **Skill doesn't trigger.** Restart Claude Code — skills are loaded at session start. If it still doesn't trigger, the `description` in `SKILL.md` is the most likely culprit; it must match the kind of message the user is sending.
- **Wrong meter characters.** The skill is strict about the bust-meter glyphs (`( . )`, `(  o  )`, `(   O   )`, `(    O    )`, `(     @     )`). If you see emoji, `:(`, or other ASCII art, the skill body is being skipped — confirm the plugin is listed under `/plugin` → **Installed** and the session has been restarted since install.
- **Meter appears in serious contexts.** The safety gate should suppress it; if not, the complaint may not have read as high-stakes. Add explicit signals ("legal," "production," "customer-facing") and re-test.

## A note on the joke

This riffs on a joke I picked up as a teenager and somehow never put down: the deeper the apology, the bigger the bust grows.

What this project keeps is the **shape** of the joke: a meter that scales with how bad the miss was. What it changes is who's wearing the meter — here it's *Claude* on the receiving end, apologizing for its own mistakes. The glyphs are deliberately abstract ASCII (`( . )( . )` through `(     @     )(     @     )`), closer to a wide-eyed "oof" face than to anything anatomical, and the project leans on that abstraction.

Treat it as a wink at a dumb teenage memory, nothing more. If it doesn't sit right with you, please don't install — see the [Disclaimer](#disclaimer).

## Disclaimer

This project is a **personal, for-fun experiment**. It is not a product, not a service, and is not affiliated with, endorsed by, or supported by Anthropic, Claude Code, or any employer of the author.

By installing, running, modifying, distributing, or otherwise using anything in this repository ("the Software"), **you accept full and sole responsibility** for:

- **Where you install it.** The skill is designed to run on your personal machine in casual contexts. Installing it on shared, enterprise, customer-facing, classroom, recorded, or otherwise non-private systems is your decision and your risk.
- **What it generates.** Outputs are produced by a large language model interpreting these instructions. The author makes no guarantee that any output will be appropriate, accurate, safe, professional, work-safe, or free of content that could embarrass, offend, harm, or otherwise negatively affect you, your colleagues, your employer, your clients, or any third party.
- **Who sees it.** If a meter, glyph, phrase, screenshot, or any other output ends up in a meeting, demo, recording, screen-share, support ticket, code review, blog post, social media post, courtroom, performance review, or any other context where it causes problems, that consequence is yours alone.
- **Compliance.** You are responsible for ensuring use of this skill complies with all applicable laws, contracts, employer policies, AI usage policies, code-of-conduct rules, terms of service (including those of Anthropic and Claude Code), and ethical norms in your jurisdiction and workplace.
- **Children and unintended audiences.** Do not install this skill on machines used by minors or in contexts where minors may be present. The author disclaims all responsibility for exposure to anyone for whom adult-humor framing is inappropriate.

**The author expressly disclaims any and all responsibility, liability, warranty, indemnity, or duty of care** arising from use, misuse, or non-use of this Software, including but not limited to direct, indirect, incidental, consequential, special, exemplary, punitive, reputational, professional, financial, or emotional damages, regardless of the legal theory under which such claim might arise (contract, tort, statute, or otherwise), and regardless of whether the author has been advised of the possibility of such damages.

**If you do not accept these terms, do not install or use this Software.** Installing it is your acknowledgment that you have read this disclaimer and accept full responsibility for everything that follows.

Reasonable adults only. Use at your own risk. Don't blame me.

## License

[MIT](LICENSE) © 2026 Paper Lee

The MIT License is permissive but includes its own "AS IS" warranty disclaimer and limitation of liability. Both that license and the [Disclaimer](#disclaimer) above apply to all use of this Software.
