# Minimize Max Min Diff with Subarray Removal
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Prefix Sum

import sys
import re


def solve():
    data = sys.stdin.read()
    if not data.strip():
        return

    if '[' in data or '=' in data:
        nums = list(map(int, re.findall(r'-?\d+', data)))
        arr = nums[:-1]
        k = nums[-1]
    else:
        lines = [list(map(int, line.split())) for line in data.splitlines() if line.strip()]
        if len(lines) == 1:
            arr = lines[0][:-1]
            k = lines[0][-1]
        elif len(lines) == 2:
            if len(lines[0]) == 2 and len(lines[1]) == lines[0][0] and lines[0][0] != 1:
                k = lines[0][1]
                arr = lines[1]
            else:
                arr = lines[0]
                k = lines[1][0]
        else:
            arr = lines[1]
            k = lines[2][0]

    n = len(arr)
    if n <= 1 or k >= n - 1:
        print(0)
        return

    inf = float('inf')
    ninf = float('-inf')

    suff_min = [inf] * (n + 1)
    suff_max = [ninf] * (n + 1)
    for i in range(n - 1, -1, -1):
        val = arr[i]
        suff_min[i] = val if val < suff_min[i + 1] else suff_min[i + 1]
        suff_max[i] = val if val > suff_max[i + 1] else suff_max[i + 1]

    p_min = inf
    p_max = ninf
    ans = inf

    for i in range(n - k + 1):
        s_min = suff_min[i + k]
        s_max = suff_max[i + k]
        c_min = p_min if p_min < s_min else s_min
        c_max = p_max if p_max > s_max else s_max
        diff = c_max - c_min
        if diff < ans:
            ans = diff
        if i < n:
            val = arr[i]
            if val < p_min:
                p_min = val
            if val > p_max:
                p_max = val

    print(ans)


if __name__ == '__main__':
    solve()