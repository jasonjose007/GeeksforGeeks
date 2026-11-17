# Repeated Replacement of Min 2 with Sum
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Heap

import sys
import heapq
import re

def solve():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    
    line_nums = []
    for line in lines:
        nums = [int(x) for x in re.findall(r'\d+', line)]
        if nums:
            line_nums.append(nums)
            
    if not line_nums:
        return

    if len(line_nums) == 1:
        nums = line_nums[0]
        if len(nums) >= 3 and nums[0] == len(nums) - 2:
            k = nums[1]
            arr = nums[2:]
        else:
            k = nums[-1]
            arr = nums[:-1]
    elif len(line_nums) == 2:
        if len(line_nums[0]) == 2:
            k = line_nums[0][1]
            arr = line_nums[1]
        elif len(line_nums[0]) == 1:
            if len(line_nums[1]) >= 2:
                k = line_nums[1][-1]
                arr = line_nums[1][:-1]
            else:
                k = line_nums[1][0]
                arr = line_nums[0]
        else:
            k = line_nums[1][0]
            arr = line_nums[0]
    elif len(line_nums) == 3:
        if len(line_nums[0]) == 1 and len(line_nums[2]) == 1:
            k = line_nums[2][0]
            arr = line_nums[1]
        elif len(line_nums[0]) == 2:
            k = line_nums[0][1]
            arr = line_nums[1]
        else:
            k = line_nums[2][0]
            arr = line_nums[1]
    else:
        all_nums = [x for line in line_nums for x in line]
        if len(all_nums) >= 3 and all_nums[0] == len(all_nums) - 2:
            k = all_nums[1]
            arr = all_nums[2:]
        else:
            k = all_nums[-1]
            arr = all_nums[:-1]

    heapq.heapify(arr)
    ops = 0
    while len(arr) >= 2 and arr[0] < k:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        heapq.heappush(arr, first + second)
        ops += 1
        
    if arr and arr[0] >= k:
        print(ops)
    else:
        print(-1)

if __name__ == '__main__':
    solve()