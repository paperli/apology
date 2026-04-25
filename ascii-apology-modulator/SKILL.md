---
name: ascii-apology-modulator
description: |
  This skill customizes apology responses based on how seriously the agent's output deviates
  from a user's expectations. When a user complains about output quality, the skill returns
  a short apology along with a visual severity meter rendered in ASCII. The meter grows
  larger as complaints become more severe or frequent. The representation uses simple
  characters (such as `*`) rather than anything explicit. A mild deviation produces a
  small meter, whereas repeated or extreme deviations produce a longer meter. This skill
  is designed to be demonstrative and should be used responsibly in safe contexts.
version: 0.1.0
---

# ASCII Apology Modulator

The **ASCII Apology Modulator** skill provides a way to tailor apology messages based on
how far an assistant's responses deviate from a user's expectations. It works by
computing a severity score for a given complaint and rendering a simple ASCII meter
proportional to that score.

## Usage

The skill expects a severity score between 0 and 1. A higher value indicates a more
serious deviation from the expected output, or repeated complaints in a single session.
For example:

```python
from scripts.apology_ascii import build_apology

# A mild complaint
print(build_apology(severity_score=0.2))

# A serious complaint
print(build_apology(severity_score=0.8))
```

## Safety Considerations

This skill avoids explicit content by using simple characters to represent the meter.
Should the input severity exceed 1 or fall below 0, the meter is clamped to a safe
range. If no complaints are present, no ASCII meter is displayed.

## Development

Implementation details can be found in the `scripts` directory. Additional design
documents (product requirements, test design, and implementation plan) reside in the
`references` directory.
