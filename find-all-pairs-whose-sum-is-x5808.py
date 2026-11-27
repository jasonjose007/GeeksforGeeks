# All Pairs with Sum from 2 Arrays
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Hash

    a = parsed_lines[idx]
    idx += 1
    if idx >= len(parsed_lines):
        break

    if len(parsed_lines[idx]) == 1 and idx + 1 < len(parsed_lines):
        # maybe size m before array b
        idx += 1

    b = parsed_lines[idx]
    idx += 1

    process_test_case(target, a, b)

Wait, what if `a` is a single element `[4]`?
If `a` is `[4]`, `len(parsed_lines[idx])` is 1.
If `len(parsed_lines) == 3`:
idx=0: target=9
idx=1: a=[4]
idx=2: b=[5, 6]
In this case, `len(parsed_lines)` is 3.
If we check `if (len(parsed_lines) - idx) == 2`: then `parsed_lines[idx]` MUST be `a`, and `parsed_lines[idx+1]` MUST be `b`!
That's a great observation! If exactly 2 lines remain in the current testcase, they are `a` and `b`.

So:python