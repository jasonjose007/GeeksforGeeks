# N-Digit Numbers with Increasing Digits
# Platform: GFG
# Difficulty: Medium
# Topics: Recursion

import sys
from itertools import combinations


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    for token in input_data:
        try:
            n = int(token)
        except ValueError:
            continue
        if n == 1:
            print(*range(10))
        elif 2 <= n <= 9:
            ans = ["".join(p) for p in combinations("123456789", n)]
            print(*ans)
        else:
            print()


if __name__ == "__main__":
    solve()