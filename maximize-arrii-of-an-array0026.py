# Max Value Permutation
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Sorting

import re
import sys


def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return

    lines = [l.strip() for l in input_text.splitlines() if l.strip()]
    nums = [int(x) for x in re.findall(r"-?\d+", input_text)]

    if len(lines) > 1:
        first_tokens = re.findall(r"-?\d+", lines[0])
        if len(first_tokens) == 1:
            n = int(first_tokens[0])
            rest_tokens = re.findall(r"-?\d+", " ".join(lines[1:]))
            if len(rest_tokens) == n:
                arr = [int(x) for x in rest_tokens]
            else:
                arr = nums
        else:
            arr = nums
    else:
        arr = nums

    arr.sort()
    MOD = 10**9 + 7
    ans = 0
    for i, val in enumerate(arr):
        ans = (ans + val * i) % MOD

    print(ans)


if __name__ == "__main__":
    main()