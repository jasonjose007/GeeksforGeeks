# Maximum Count with Sum Limited to K
# Platform: GFG
# Difficulty: Easy
# Topics: Greedy, Sorting

import re


def max_toys(arr, k):
    arr.sort()
    total = 0
    count = 0
    for x in arr:
        if total + x <= k:
            total += x
            count += 1
        elif x >= 0:
            break
    return count


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

    if len(parsed) == 1:
        nums = parsed[0]
        print(max_toys(nums[:-1], nums[-1]))
    elif len(parsed) == 2:
        l1, l2 = parsed
        if len(l1) == 2 and len(l2) == l1[0] and len(l2) > 1:
            print(max_toys(l2, l1[1]))
        elif len(l2) == 1:
            print(max_toys(l1, l2[0]))
        elif len(l1) == 1:
            print(max_toys(l2, l1[0]))
        else:
            print(max_toys(l1, l2[-1]))
    elif len(parsed) == 3 and len(parsed[0]) == 1 and len(parsed[2]) == 1:
        print(max_toys(parsed[1], parsed[2][0]))
    elif len(parsed[0]) == 1:
        t = parsed[0][0]
        idx = 1
        for _ in range(t):
            if idx + 1 < len(parsed):
                l1, l2 = parsed[idx], parsed[idx + 1]
                if len(l1) == 2 and len(l2) == l1[0]:
                    print(max_toys(l2, l1[1]))
                elif len(l2) == 1:
                    print(max_toys(l1, l2[0]))
                else:
                    print(max_toys(l1, l2[-1]))
                idx += 2


if __name__ == '__main__':
    solve()