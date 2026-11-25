# Next Permutation
# Platform: GFG
# Difficulty: Medium
# Topics: Arrays, permutation, constructive algo

import sys

def next_permutation(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    
    left = i + 1
    right = n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return
    
    lines = input_text.splitlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue
        cleaned = line.replace('[', ' ').replace(']', ' ').replace(',', ' ')
        tokens = cleaned.split()
        if not tokens:
            continue
        arr = list(map(int, tokens))
        next_permutation(arr)
        print(*(arr))

if __name__ == '__main__':
    main()