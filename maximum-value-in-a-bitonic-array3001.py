# Bitonic Point
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Searching, Binary Search

import sys
import re

def find_bitonic(arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        
        prev_val = arr[mid - 1] if mid > 0 else float('-inf')
        next_val = arr[mid + 1] if mid < len(arr) - 1 else float('-inf')
        
        if arr[mid] >= prev_val and arr[mid] >= next_val:
            return arr[mid]
        elif arr[mid] < next_val:
            low = mid + 1
        else:
            high = mid - 1
    return arr[0]

def main():
    content = sys.stdin.read()
    if not content.strip():
        return
    
    lines = content.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line:
            continue
        nums = [int(x) for x in re.findall(r'-?\d+', line)]
        if len(nums) >= 3:
            print(find_bitonic(nums))

if __name__ == '__main__':
    main()