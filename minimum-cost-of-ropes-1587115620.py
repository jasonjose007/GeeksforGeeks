# Min Cost to Connect Ropes
# Platform: GFG
# Difficulty: Medium
# Topics: Heap

import sys
import heapq
import re

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    if not lines:
        return

    if len(lines) == 1:
        arr = list(map(int, re.findall(r'-?\d+', lines[0])))
    else:
        first_line_nums = list(map(int, re.findall(r'-?\d+', lines[0])))
        all_nums = list(map(int, re.findall(r'-?\d+', input_data)))
        
        if len(first_line_nums) == 1 and all_nums[0] == len(all_nums) - 1:
            arr = all_nums[1:]
        else:
            arr = all_nums

    if len(arr) <= 1:
        print(0)
        return

    heapq.heapify(arr)
    total_cost = 0
    while len(arr) > 1:
        first = heapq.heappop(arr)
        second = heapq.heappop(arr)
        cost = first + second
        total_cost += cost
        heapq.heappush(arr, cost)

    print(total_cost)

if __name__ == '__main__':
    solve()