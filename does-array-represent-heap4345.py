# Check if Array is Max Heap
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Heap

import sys


def solve():
    data = sys.stdin.read().strip()
    if not data:
        return
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if len(lines) >= 2:
        first_tokens = lines[0].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        rest_tokens = ' '.join(lines[1:]).replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        if len(first_tokens) == 1 and int(first_tokens[0]) == len(rest_tokens):
            arr = list(map(int, rest_tokens))
        else:
            arr = list(map(int, data.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))
    else:
        arr = list(map(int, data.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()))

    n = len(arr)
    for i in range(n // 2):
        left = 2 * i + 1
        right = 2 * i + 2
        if arr[i] < arr[left]:
            print("false")
            return
        if right < n and arr[i] < arr[right]:
            print("false")
            return
    print("true")


if __name__ == "__main__":
    solve()