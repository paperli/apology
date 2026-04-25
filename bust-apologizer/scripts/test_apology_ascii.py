"""Unit tests for Bust Apologizer."""

from bust_apologizer.scripts.apology_ascii import build_apology


def test_no_meter_when_zero_severity():
    msg = build_apology(0.0)
    assert "(" not in msg


def test_medium_meter_length():
    msg = build_apology(0.5)
    # Extract meter
    lines = msg.split("\n")
    meter = lines[-1] if len(lines) > 1 else ""
    assert meter.startswith("(") and meter.endswith(")")
    # Meter length should be around half the maximum (between 6 and 10)
    length = len(meter) - 2
    assert 6 <= length <= 10


def test_maximum_meter_length():
    msg = build_apology(1.0)
    lines = msg.split("\n")
    meter = lines[-1]
    # Maximum length is 15
    assert len(meter) - 2 == 15


def test_clamping():
    assert build_apology(-0.5) == build_apology(0.0)
    assert build_apology(1.5) == build_apology(1.0)
