# Test-Driven Development (TDD) Plan

This document describes the tests used to verify the correctness and safety of
Bust Apologizer.

## Unit Tests

1. **Severity to Meter Size**
   - *Input:* `severity_score=0.0`
   - *Expected:* Apology message without a meter.
   - *Input:* `severity_score=0.5`
   - *Expected:* Meter length is medium (e.g. 7–8 characters).
   - *Input:* `severity_score=1.0`
   - *Expected:* Meter length equals the configured maximum.

2. **Clamping**
   - *Input:* `severity_score=-0.5`
   - *Expected:* Treated as 0.0 (no meter).
   - *Input:* `severity_score=1.5`
   - *Expected:* Treated as 1.0 (maximum length).

3. **Character Safety**
   - *Input:* Any severity
   - *Expected:* The meter should only use the `*` character and parentheses; no
     explicit shapes or words should appear.

4. **Apology Composition**
   - *Input:* `severity_score=0.3`
   - *Expected:* The output begins with a sincere apology statement followed by
     the ASCII meter on the next line.

These tests are implemented in `scripts/test_apology_ascii.py`. 
