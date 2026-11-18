# Count Subarrays with XOR
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, Map, Bit Magic, Prefix Sum

import re


def count_subarrays_with_xor(arr, k):
    freq = {0: 1}
    pref = 0
    ans = 0
    for x in arr:
        pref ^= x
        ans += freq.get(pref ^ k, 0)
        freq[pref] = freq.get(pref, 0) + 1
    return ans


def parse_pair(l0, l1):
    if len(l0) == 2 and len(l1) == l0[0] and len(l1) > 1:
        return l1, l0[1]
    if len(l1) == 1:
        return l0, l1[0]
    if len(l0) == 1:
        return l1, l0[0]
    return l0, l1[0]


def main():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except (EOFError, StopIteration):
            break

    if not lines:
        return

    nums = []
    for line in lines:
        vals = list(map(int, re.findall(r'-?\d+', line)))
        if vals:
            nums.append(vals)

    if not nums:
        return

    m = len(nums)
    cases = []

    if m == 1:
        cases.append((nums[0][:-1], nums[0][-1]))
    elif m == 2:
        cases.append(parse_pair(nums[0], nums[1]))
    elif m == 3:
        l0, l1, l2 = nums[0], nums[1], nums[2]
        if len(l0) == 1 and l0[0] == 1:
            cases.append(parse_pair(l1, l2))
        elif len(l0) == 1 and l0[0] == len(l1) and len(l2) == 1:
            cases.append((l1, l2[0]))
        else:
            cases.append(parse_pair(l0, l1))
    else:
        if len(nums[0]) == 1:
            t = nums[0][0]
            if m - 1 == 2 * t:
                for i in range(t):
                    cases.append(parse_pair(nums[1 + 2 * i], nums[2 + 2 * i]))
            elif m - 1 == 3 * t:
                for i in range(t):
                    cases.append((nums[2 + 3 * i], nums[3 + 3 * i][0]))
            else:
                flat = [x for row in nums[:-1] for x in row]
                cases.append((flat, nums[-1][0]))
        else:
            flat = [x for row in nums[:-1] for x in row]
            cases.append((flat, nums[-1][0]))

    for arr, k in cases:
        print(count_subarrays_with_xor(arr, k))


if __name__ == "__main__":
    main()