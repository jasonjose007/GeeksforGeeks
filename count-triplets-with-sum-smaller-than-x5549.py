# Triplets with Smaller Sum
# Platform: GFG
# Difficulty: Medium
# Topics: two-pointer-algorithm, Arrays

import sys

def count_triplets(arr, target):
    arr.sort()
    n = len(arr)
    ans = 0
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            if arr[i] + arr[left] + arr[right] < target:
                ans += right - left
                left += 1
            else:
                right -= 1
    return ans

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    tokens = input_data
    
    # Try parsing with T testcases first
    try:
        t = int(tokens[0])
        temp_ptr = 1
        valid_t = True
        for _ in range(t):
            if temp_ptr + 2 > len(tokens):
                valid_t = False
                break
            n = int(tokens[temp_ptr])
            temp_ptr += 2 + n
        
        if valid_t and temp_ptr == len(tokens):
            ptr = 1
            for _ in range(t):
                n = int(tokens[ptr])
                target = int(tokens[ptr + 1])
                arr = [int(x) for x in tokens[ptr + 2 : ptr + 2 + n]]
                ptr += 2 + n
                print(count_triplets(arr, target))
            return
    except (ValueError, IndexError):
        pass

    # Fallback to processing stream as (N, target, arr...)
    ptr = 0
    while ptr < len(tokens):
        if ptr + 2 > len(tokens):
            break
        n = int(tokens[ptr])
        target = int(tokens[ptr + 1])
        arr = [int(x) for x in tokens[ptr + 2 : ptr + 2 + n]]
        ptr += 2 + n
        print(count_triplets(arr, target))

if __name__ == '__main__':
    main()