# Check Sorted Array
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Sorting

import sys

class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                return False
        return True

    def isSorted(self, arr) -> bool:
        return self.arraySortedOrNot(arr)

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    
    if len(lines) == 1:
        raw_tokens = lines[0].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        arr = [int(x) for x in raw_tokens]
    elif len(lines) >= 2:
        line1_tokens = lines[0].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        line2_tokens = lines[1].replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
        if len(line1_tokens) == 1 and len(line2_tokens) >= 1:
            arr = [int(x) for x in line2_tokens]
        else:
            all_text = " ".join(lines)
            raw_tokens = all_text.replace('[', ' ').replace(']', ' ').replace(',', ' ').split()
            arr = [int(x) for x in raw_tokens]
    else:
        arr = []

    sol = Solution()
    ans = sol.arraySortedOrNot(arr)
    print("true" if ans else "false")

if __name__ == '__main__':
    main()