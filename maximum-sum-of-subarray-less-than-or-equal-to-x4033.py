# Max Subarray Sum Limited by X
# Platform: GFG
# Difficulty: Easy
# Topics: sliding-window, two-pointer-algorithm, Arrays

import sys

def solve(arr, x):
    left = 0
    curr = 0
    ans = 0
    n = len(arr)
    for right in range(n):
        curr += arr[right]
        while curr > x and left <= right:
            curr -= arr[left]
            left += 1
        if curr <= x:
            ans = max(ans, curr)
    return ans

def main():
    lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip()]
    if not lines:
        return

    first_line_vals = list(map(int, lines[0].split()))
    
    if len(first_line_vals) == 1 and len(lines) > 2 and (len(lines) - 1) % 2 == 0:
        T = first_line_vals[0]
        i = 1
        for _ in range(T):
            if i >= len(lines):
                break
            arr = list(map(int, lines[i].split()))
            x = int(lines[i+1])
            print(solve(arr, x))
            i += 2
    elif len(first_line_vals) == 1 and len(lines) > 3 and (len(lines) - 1) % 3 == 0:
        T = first_line_vals[0]
        i = 1
        for _ in range(T):
            if i + 2 >= len(lines):
                break
            arr = list(map(int, lines[i+1].split()))
            x = int(lines[i+2])
            print(solve(arr, x))
            i += 3
    else:
        i = 0
        while i < len(lines):
            val1 = list(map(int, lines[i].split()))
            if i + 1 < len(lines):
                val2 = list(map(int, lines[i+1].split()))
                if len(val2) == 1:
                    print(solve(val1, val2[0]))
                    i += 2
                    continue
                elif len(val1) == 2 and len(val2) == val1[0]:
                    print(solve(val2, val1[1]))
                    i += 2
                    continue
                elif len(val1) == 1 and i + 2 < len(lines):
                    arr = list(map(int, lines[i+1].split()))
                    x = int(lines[i+2])
                    print(solve(arr, x))
                    i += 3
                    continue
            i += 1

if __name__ == '__main__':
    main()