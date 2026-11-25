# Fractional Knapsack
# Platform: GFG
# Difficulty: Easy
# Topics: Greedy

import sys
import re

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    parsed_lines = [list(map(int, re.findall(r'-?\d+', line))) for line in lines]
    parsed_lines = [p for p in parsed_lines if p]
    
    if not parsed_lines:
        return

    if len(parsed_lines) == 3:
        val = parsed_lines[0]
        wt = parsed_lines[1]
        capacity = parsed_lines[2][0]
    elif len(parsed_lines) >= 4:
        if len(parsed_lines[1]) == len(parsed_lines[2]):
            val = parsed_lines[1]
            wt = parsed_lines[2]
            capacity = parsed_lines[3][0]
        else:
            val = parsed_lines[0]
            wt = parsed_lines[1]
            capacity = parsed_lines[2][0]
    else:
        tokens = [item for p in parsed_lines for item in p]
        if len(tokens) < 3:
            return
        capacity = tokens[-1]
        n = (len(tokens) - 1) // 2
        val = tokens[:n]
        wt = tokens[n:2*n]

    items = sorted(zip(val, wt), key=lambda x: x[0] / x[1], reverse=True)
    
    total_val = 0.0
    for v, w in items:
        if capacity <= 0:
            break
        if w <= capacity:
            capacity -= w
            total_val += v
        else:
            total_val += v * (capacity / w)
            capacity = 0
            break
            
    print(f"{total_val:.6f}")

if __name__ == '__main__':
    solve()