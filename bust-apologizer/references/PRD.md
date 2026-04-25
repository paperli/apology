# Product Requirements Document (PRD)

## Overview

Bust Apologizer helps assistants produce more empathetic apologies by
including a visual severity indicator in the response. The meter grows as the
severity of a complaint increases or as similar complaints accumulate during a
conversation.

## Goals

1. **Empathy through context:** Reflect the seriousness of a complaint using an
   intuitive ASCII meter.
2. **Configurable severity:** Allow developers to set severity based on their own
   metrics (e.g. sentiment analysis scores, frequency of complaints, etc.).
3. **Safety first:** Ensure the meter uses neutral characters and never
   produces explicit or offensive shapes.
4. **Extensible:** Provide clear documentation and a simple API for integration
   into larger systems.

## Key Scenarios

* **Single mild complaint:** The user notes that an answer was slightly off.
  The system apologises with a short meter: `(*** )`.
* **Repeated complaints:** Over several turns, the user's frustrations build.
  The meter lengthens to reflect the increased severity.
* **Severe complaint:** The assistant completely misinterprets the request.
  The meter expands to its maximum safe length to acknowledge the mistake.

## Non-Goals

* The skill does not attempt to interpret the tone of a complaint on its own.
  It relies on an external severity score.
* The skill will not alter the content of the apology beyond adding the ASCII
  meter and a brief apology message.
