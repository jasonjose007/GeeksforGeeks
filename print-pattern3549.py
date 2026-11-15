# Decreasing Increasing Pattern
# Platform: GFG
# Difficulty: Easy
# Topics: Recursion

import sys

sys.setrecursionlimit(10**6)


def pattern(n):
    res = []

    def helper(curr):
        res.append(curr)
        if curr <= 0:
            return
        helper(curr - 5)
        res.append(curr)

    helper(n)
    return res


if __name__ == "__main__":
    n = int(input().strip().split("=")[-1])
    print(pattern(n))