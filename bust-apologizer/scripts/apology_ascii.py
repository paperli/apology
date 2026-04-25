"""Bust Apologizer reference implementation.

This module provides a function to build an apology message with a visual
indicator of how seriously the assistant's response deviated from the user's
expectations. The visual indicator is an ASCII meter composed of `*`
characters enclosed in parentheses. A higher severity score produces a longer
meter.
"""

from __future__ import annotations


def _clamp(value: float, min_value: float = 0.0, max_value: float = 1.0) -> float:
    """Clamp a float between min_value and max_value."""
    return max(min_value, min(max_value, value))


def build_apology(severity_score: float) -> str:
    """Return an apology message with an ASCII severity meter.

    Args:
        severity_score: A floating point number between 0.0 and 1.0 indicating
            how serious the deviation was. Values outside the range will be
            clamped.

    Returns:
        A string containing the apology message and a visual meter.
    """
    # Clamp input to safe range
    severity = _clamp(severity_score)

    # Determine meter length: minimum 0 (no meter) to maximum 15 characters
    min_len = 0
    max_len = 15
    meter_len = int(round(severity * (max_len - min_len))) + min_len

    # Build the meter if needed
    meter = ""
    if meter_len > 0:
        meter_body = "*" * meter_len
        meter = f"({meter_body})"

    # Compose apology
    apology_lines = ["I'm sorry for the inconvenience."]
    if meter:
        apology_lines.append(meter)
    return "\n".join(apology_lines)


if __name__ == "__main__":
    # Example usage
    for score in [0.0, 0.2, 0.5, 1.0]:
        print(f"Severity {score}:\n{build_apology(score)}\n")
