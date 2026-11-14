# Max Equal Sum in 3 Stacks
# Platform: GFG
# Difficulty: Medium
# Topics: Greedy, Stack

import sys
import re


def max_equal_sum(s1, s2, s3):
    suff1 = {0}
    cur = 0
    for x in reversed(s1):
        cur += x
        suff1.add(cur)

    suff2 = {0}
    cur = 0
    for x in reversed(s2):
        cur += x
        suff2.add(cur)

    common = suff1 & suff2
    ans = 0
    cur = 0
    for x in reversed(s3):
        cur += x
        if cur in common and cur > ans:
            ans = cur
    return ans


def parse_input():
    data = sys.stdin.read()
    if not data.strip():
        return [], [], []

    if "[" in data:
        groups = re.findall(r"\[([^\]]*)\]", data)
        arrays = []
        for g in groups[:3]:
            arrays.append([int(x) for x in re.findall(r"-?\d+", g)])
        while len(arrays) < 3:
            arrays.append([])
        return arrays[0], arrays[1], arrays[2]

    raw_lines = data.splitlines()
    while raw_lines and not raw_lines[0].strip():
        raw_lines.pop(0)
    while raw_lines and not raw_lines[-1].strip():
        raw_lines.pop()

    rows = [[int(x) for x in line.split()] for line in raw_lines]

    if len(rows) == 4 and len(rows[0]) == 3 and rows[0] == [len(rows[1]), len(rows[2]), len(rows[3])]:
        return rows[1], rows[2], rows[3]
    if len(rows) == 6 and len(rows[0]) == 1 and len(rows[2]) == 1 and len(rows[4]) == 1:
        if rows[0][0] == len(rows[1]) and rows[2][0] == len(rows[3]) and rows[4][0] == len(rows[5]):
            return rows[1], rows[3], rows[5]
    if len(rows) == 3:
        return rows[0], rows[1], rows[2]

    nums = [x for r in rows for x in r]
    if len(nums) >= 3 and 3 + nums[0] + nums[1] + nums[2] == len(nums):
        n1, n2, n3 = nums[0], nums[1], nums[2]
        return nums[3:3 + n1], nums[3 + n1:3 + n1 + n2], nums[3 + n1 + n2:]

    while len(rows) < 3:
        rows.append([])
    return rows[0], rows[1], rows[2]


def main():
    s1, s2, s3 = parse_input()
    print(max_equal_sum(s1, s2, s3))


if __name__ == "__main__":
    main()