# Find Rotation Count
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Searching

import sys

def find_rotation_count(arr):
    n = len(arr)
    low, high = 0, n - 1
    
    while low <= high:
        if arr[low] <= arr[high]:
            return low
        
        mid = (low + high) // 2
        next_idx = (mid + 1) % n
        prev_idx = (mid - 1 + n) % n
        
        if arr[mid] <= arr[next_idx] and arr[mid] <= arr[prev_idx]:
            return mid
        elif arr[mid] <= arr[high]:
            high = mid - 1
        elif arr[mid] >= arr[low]:
            low = mid + 1
            
    return 0

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    import re
    lines = input_data.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        numbers = list(map(int, re.findall(r'-?\d+', line)))
        if not numbers:
            continue
        if len(numbers) == 1 and len(lines) > 1:
            continue
        print(find_rotation_count(numbers))

if __name__ == '__main__':
    main()