# Minimum Operations to Reach n
# Platform: GFG
# Difficulty: Easy
# Topics: Dynamic Programming, Greedy

import sys


def solve_n(n):
    if n <= 0:
        return 0
    return bin(n).count("1") + n.bit_length() - 1


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    try:
        t = int(input_data[0])
        if len(input_data) == t + 1:
            for i in range(1, t + 1):
                print(solve_n(int(input_data[i])))
            return
    except ValueError:
        pass

    for token in input_data:
        print(solve_n(int(token)))


if __name__ == "__main__":
    main()