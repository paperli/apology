# Implementation Plan

1. **Define the interface**
   - Create a function `build_apology(severity_score: float) -> str` that accepts a
     severity score and returns a formatted apology string containing the
     calculated ASCII meter.
2. **Implement clamping and scaling**
   - Clamp the input between 0.0 and 1.0.
   - Map the normalized severity to a meter length within a reasonable range
     (e.g. minimum length 3, maximum length 15).
3. **Construct the meter**
   - Use parentheses to delimit the meter and fill the interior with `*`
     characters repeated to match the computed length.
4. **Compose the apology message**
   - Prepend a generic apology such as "I'm sorry for the inconvenience." and
     append the meter on a new line.
5. **Write unit tests**
   - Implement the tests described in the TDD document in a separate file.
6. **Documentation and examples**
   - Update the `SKILL.md` with usage examples and safety notes.
7. **Future enhancements (optional)**
   - Provide helper functions to accumulate complaint counts and derive
     severity scores automatically.
