# Subarrays with Sum K
# Platform: GFG
# Difficulty: Medium
# Topics: Hash

import sys
import re

def solve():
    input_data = sys.stdin.read()
    if not input_data.strip():
        return
    
    tokens = [int(x) for x in re.findall(r'-?\d+', input_data)]
    if len(tokens) < 2:
        return

    N = tokens[0]
    if len(tokens) == N + 2:
        arr = tokens[1:-1]
        k = tokens[-1]
    else:
        arr = tokens[:-1]
        k = tokens[-1]

    prefix_sums = {0: 1}
    curr_sum = 0
    count = 0

    for x in arr:
        curr_sum += x
        if (curr_sum - k) in prefix_sums:
            count += prefix_sums[curr_sum - k]
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        
    print(count)

if __name__ == '__main__':
    solve()