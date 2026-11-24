# Two Sum - Pair with Given Sum
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Hash

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    target = int(input_data[-1])
    arr = [int(x) for x in input_data[:-1]]

    seen = set()
    found = False
    for num in arr:
        if target - num in seen:
            found = True
            break
        seen.add(num)

    if found:
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    solve()