# Maximum Sum Problem
# Platform: GFG
# Difficulty: Easy
# Topics: Dynamic Programming

import sys

def main():
    memo = {0: 0}
    def get_max_sum(n):
        if n in memo:
            return memo[n]
        res = max(n, get_max_sum(n // 2) + get_max_sum(n // 3) + get_max_sum(n // 4))
        memo[n] = res
        return res

    data = sys.stdin.read().split()
    if not data:
        return

    try:
        t = int(data[0])
        if len(data) == t + 1:
            queries = [int(x) for x in data[1:]]
        else:
            queries = [int(x) for x in data]
    except ValueError:
        queries = [int(x) for x in data]

    for n in queries:
        print(get_max_sum(n))

if __name__ == '__main__':
    main()