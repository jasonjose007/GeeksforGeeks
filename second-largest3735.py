# Second Largest
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Searching

import sys
import re

def second_largest(arr):
    first = -1
    second = -1
    for x in arr:
        if x > first:
            second = first
            first = x
        elif x < first and x > second:
            second = x
    return second

def main():
    input_data = sys.stdin.read().splitlines()
    for line in input_data:
        nums = [int(x) for x in re.findall(r'\d+', line)]
        if len(nums) >= 2:
            print(second_largest(nums))

if __name__ == '__main__':
    main()