# Nth Number Without 9
# Platform: GFG
# Difficulty: Medium
# Topics: Mathematics

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    for n_str in input_data:
        n = int(n_str)
        if n == 0:
            print(0)
            continue
        digits = []
        while n > 0:
            digits.append(str(n % 9))
            n //= 9
        print("".join(reversed(digits)))


if __name__ == "__main__":
    solve()