# Row with Max 1s in Rowwise Sorted
# Platform: GFG
# Difficulty: Medium
# Topics: Matrix

import sys
import ast
import json

def rowWithMax1s(arr):
    if not arr or not arr[0]:
        return -1
    
    n = len(arr)
    m = len(arr[0])
    
    max_row = -1
    col = m - 1
    
    for row in range(n):
        while col >= 0 and arr[row][col] == 1:
            max_row = row
            col -= 1
            
    return max_row

def main():
    raw_input = sys.stdin.read().strip()
    if not raw_input:
        return

    arr = []
    if '[' in raw_input:
        try:
            start = raw_input.find('[')
            end = raw_input.rfind(']') + 1
            arr = json.loads(raw_input[start:end])
        except Exception:
            try:
                arr = ast.literal_eval(raw_input[start:end])
            except Exception:
                pass

    if not arr:
        lines = [line.strip() for line in raw_input.split('\n') if line.strip()]
        if lines:
            first_tokens = lines[0].split()
            if len(first_tokens) == 2 and len(lines) > 1:
                try:
                    n, m = int(first_tokens[0]), int(first_tokens[1])
                    all_nums = []
                    for line in lines[1:]:
                        all_nums.extend([int(x) for x in line.split()])
                    if len(all_nums) == n * m:
                        arr = [all_nums[i * m:(i + 1) * m] for i in range(n)]
                except Exception:
                    pass

        if not arr:
            all_tokens = raw_input.split()
            try:
                nums = [int(x) for x in all_tokens]
                if len(nums) >= 2:
                    n, m = nums[0], nums[1]
                    if len(nums) - 2 == n * m:
                        arr = [nums[2 + i * m: 2 + (i + 1) * m] for i in range(n)]
            except Exception:
                pass

        if not arr and lines:
            try:
                for line in lines:
                    row = [int(x) for x in line.replace(',', ' ').split()]
                    if row:
                        arr.append(row)
            except Exception:
                pass

    print(rowWithMax1s(arr))

if __name__ == '__main__':
    main()