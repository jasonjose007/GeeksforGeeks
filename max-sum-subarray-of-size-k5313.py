# Max Sum Subarray of Size K
# Platform: GFG
# Difficulty: Easy
# Topics: Prefix Sum, sliding-window

import re

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum

def solve():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break

    if not lines:
        return

    parsed = [[int(x) for x in re.findall(r'-?\d+', line)] for line in lines]
    parsed = [p for p in parsed if p]

    if not parsed:
        return

    if len(parsed) > 2 and len(parsed[0]) == 1 and len(parsed) == 1 + 2 * parsed[0][0]:
        t = parsed[0][0]
        idx = 1
        for _ in range(t):
            a = parsed[idx]
            b = parsed[idx + 1]
            if len(b) == 1:
                arr, k = a, b[0]
            else:
                arr, k = b, a[-1]
            print(max_sum_subarray(arr, k))
            idx += 2
        return

    if len(parsed) == 1:
        arr, k = parsed[0][:-1], parsed[0][-1]
    elif len(parsed) == 2:
        a, b = parsed[0], parsed[1]
        if len(a) == 2 and len(b) == a[0] and '[' not in lines[0] and (len(b) != 1 or a[1] <= a[0]):
            arr, k = b, a[1]
        elif len(b) == 1:
            arr, k = a, b[0]
        else:
            arr, k = b, a[-1]
    else:
        arr, k = parsed[1], parsed[2][0]

    print(max_sum_subarray(arr, k))

solve()