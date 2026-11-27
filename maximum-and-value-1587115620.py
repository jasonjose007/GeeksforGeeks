# Maximum AND Value
# Platform: GFG
# Difficulty: Medium
# Topics: Bit Magic

import sys
import re

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    lines = [line.strip() for line in input_data.split('\n') if line.strip()]
    
    if len(lines) == 1:
        arr = [int(x) for x in re.findall(r'\d+', lines[0])]
    elif len(lines) >= 2:
        first_line_nums = [int(x) for x in re.findall(r'\d+', lines[0])]
        if len(first_line_nums) == 1:
            arr = [int(x) for x in re.findall(r'\d+', lines[1])]
        else:
            arr = [int(x) for x in re.findall(r'\d+', input_data)]
    else:
        arr = [int(x) for x in re.findall(r'\d+', input_data)]

    pattern = 0
    for bit in range(17, -1, -1):
        candidate = pattern | (1 << bit)
        count = 0
        for x in arr:
            if (x & candidate) == candidate:
                count += 1
                if count >= 2:
                    break
        if count >= 2:
            pattern = candidate

    print(pattern)

if __name__ == '__main__':
    solve()