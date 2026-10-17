# DSA quiz programs — reviewed and corrected

All six implemented programs run with Python 3 and use no imports. Run one
file at a time, for example `python3 ex04.py`.

| File | Status | Purpose |
| --- | --- | --- |
| ex01.py | Already correct; included unchanged | Merge sort |
| ex02.py | Already correct; included unchanged | Insertion sort |
| ex03.py | Revised | String-key hashing with quadratic probing |
| ex04.py | Revised | Integer hashing with quadratic probing and rehashing |
| q1.py | Revised for clarity and configurable peak definition | Peak search in a strictly unimodal array |
| q2.py | Revised | Minimum capacity for sequential box packing |
| ex05.py | Original placeholder only | The uploaded file contains no implementation or question |

## Important choices when the original quiz statement is unavailable

- **ex03.py:** A collision is an occupied probe slot. The item is discarded
  immediately on reaching `max_collision`; no extra probe is allowed after
  that collision. This fixes the earlier extra-probe behavior, under that rule.
  Confirm it against the original question's sample output.
- **ex04.py:** Existing entries are reinserted from left to right in the old
  table. Repeated integer keys are ignored (set semantics), and `count` counts
  distinct keys. If the quiz requires duplicate values to occupy separate
  slots, its duplicate-handling rule is needed: a fixed probe limit cannot
  accommodate arbitrarily many identical keys by resizing alone.
- **q1.py:** The default preserves the original definition: strictly increasing
  arrays and strictly decreasing arrays are accepted with an endpoint peak.
  Equal adjacent values are rejected. To require an interior peak, change
  `require_both_sides = False` to `True` in `main()`, or call
  `find_peak_binary_search(values, require_both_sides=True)`.
- **q2.py:** Items remain in input order. Weights may be zero but cannot be
  negative; the list must be nonempty and the box count must be positive.

## Changes

### ex03.py

- Removed the extra probe after the maximum permitted collision count.
- Added checks for a positive table size and collision limit.
- Kept the original table display and full-table message.

### ex04.py

- Corrected `is_full()` so a stored zero is not mistaken for an empty slot.
- Removed the early full-table exit so insertion can trigger rehashing.
- Replaced recursive retry chains with loops, including migration retries.
- Preserved all saved keys if migration itself needs another larger table.
- Added duplicate handling to prevent futile expansion for identical keys.
- Reinserted existing entries in old-table order rather than reverse order.
- Accepted negative integer keys using Python's modulo operation.
- Validated size, collision limit and percentage threshold before allocating.
- Used integer arithmetic for threshold and primality checks.

### q1.py

- Rewrote the validation and binary search into explicit study-friendly steps.
- Added the optional interior-peak rule without changing the default output.
- Added a clear message for noninteger input.
- Documented the complexity accurately: validation is O(n), so the full
  function is O(n); the binary-search part alone is O(log n).

### q2.py

- Rejected empty weights, negative weights and nonpositive box counts with a
  clear error message instead of crashing or returning a meaningless capacity.
- Kept the existing output spelling `weigth` for compatibility with the quiz.
- Kept the binary search and greedy capacity check, with clearer control flow.

## Example inputs

| File | Input | Key result |
| --- | --- | --- |
| ex01.py | `3 1 4 2` | `[1, 2, 3, 4]` |
| ex02.py | `3 1 4 2` | `[1, 2, 3, 4]` |
| ex03.py | `5 1/a 1,f 2` | Rejects `f` after collision number 1 |
| ex04.py | `3 3 100/1 2 3 4` | Rehashes and stores all four keys |
| ex04.py | `3 1 100/1 1` | Keeps one copy of key 1 and terminates |
| q1.py | `1 3 5 4 2` | Peak index 2, value 5 |
| q2.py | `1 2 3 4 5/3` | Minimum capacity 6 |

`ex05.py` remains the original empty placeholder. Its question is needed
before a meaningful solution can be written. No replacement exercise has been
invented.

## Validation completed

- All seven Python files parse without syntax errors and contain no imports.
- Both sorting algorithms passed 1,006 cases each.
- The unimodal validator and peak search passed 19,682 checks across the two
  supported peak definitions.
- Box capacity matched an independent exhaustive partition solver in 1,650
  comparisons, plus invalid-input tests.
- String hashing matched a separate probing reference across 1,650 insertions.
- Rehashing passed 4,554 mixed insertions, covering zero, negative keys,
  duplicates and thresholds from 1% to 100%.
- Targeted regressions cover full tables, migration collisions, preservation
  of all keys through migration retries, reinsertion order and invalid settings.
- All six implemented command-line programs ran successfully. Error-message
  handling was also checked.

These checks validate the documented algorithms and assumptions. Exact quiz
grading, especially collision limits and duplicate policies, still depends on
the original problem statements and expected output.
