# Nth Geeky Number
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, sliding-window

import sys
import re


def solve():
    data = sys.stdin.read().strip()
    if not data:
        return

    lines = [line.strip() for line in data.splitlines() if line.strip()]

    if len(lines) == 1:
        nums = [int(x) for x in re.findall(r'-?\d+', lines[0])]
        n = nums[0]
        geek_num = nums[1:]
    elif len(lines) == 2:
        nums0 = [int(x) for x in re.findall(r'-?\d+', lines[0])]
        nums1 = [int(x) for x in re.findall(r'-?\d+', lines[1])]
        if len(nums0) == 1:
            n = nums0[0]
            geek_num = nums1
        elif len(nums0) == 2:
            if nums0[0] == len(nums1) and nums0[1] != len(nums1):
                n = nums0[1]
            else:
                n = nums0[0]
            geek_num = nums1
        else:
            n = nums0[0]
            geek_num = nums0[1:]
    else:
        nums0 = [int(x) for x in re.findall(r'-?\d+', lines[0])]
        nums1 = [int(x) for x in re.findall(r'-?\d+', lines[1])]
        nums2 = [int(x) for x in re.findall(r'-?\d+', lines[2])]
        if len(nums0) == 1 and len(nums1) == 1:
            if nums0[0] == len(nums2) and nums1[0] != len(nums2):
                n = nums1[0]
            else:
                n = nums0[0]
            geek_num = nums2
        else:
            n = nums0[0]
            geek_num = nums1

    k = len(geek_num)
    if n <= k:
        print(geek_num[n - 1])
        return
    if k == 1:
        print(geek_num[0])
        return

    buf = list(geek_num)
    cur_sum = sum(buf)
    idx = 0
    ans = 0
    for _ in range(k, n):
        ans = cur_sum
        cur_sum += ans - buf[idx]
        buf[idx] = ans
        idx += 1
        if idx == k:
            idx = 0

    print(ans)


if __name__ == "__main__":
    solve()