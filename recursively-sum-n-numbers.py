# Recursively Sum n Numbers
# Platform: GFG
# Difficulty: Easy
# Topics: Recursion

import sys


sys.setrecursionlimit(2000)

def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

def main():
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        print(recursive_sum(n))

if __name__ == '__main__':
    main()