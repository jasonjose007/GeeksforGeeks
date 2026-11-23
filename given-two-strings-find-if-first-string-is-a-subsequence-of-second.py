# Check for Subsequence
# Platform: GFG
# Difficulty: Easy
# Topics: Strings, Greedy, two-pointer-algorithm

import sys


def main():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    s1 = input_data[0]
    s2 = input_data[1]

    it = iter(s2)
    if all(c in it for c in s1):
        print("true")
    else:
        print("false")


if __name__ == "__main__":
    main()