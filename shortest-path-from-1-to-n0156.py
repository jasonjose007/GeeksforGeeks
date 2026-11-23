# Shortest Path From 1 To n
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, Graph, Shortest Path

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    tokens = [int(x) for x in input_data]

    if len(tokens) > 1 and tokens[0] == len(tokens) - 1:
        queries = tokens[1:]
    else:
        queries = tokens

    for n in queries:
        ans = 0
        while n >= 3:
            ans += (n % 3) + 1
            n //= 3
        ans += n - 1
        print(ans)


if __name__ == "__main__":
    solve()