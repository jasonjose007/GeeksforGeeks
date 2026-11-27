# Longest Span in two Binary Arrays
# Platform: GFG
# Difficulty: Medium
# Topics: Prefix Sum, sliding-window, Arrays

import sys

def solve():
    input_data = sys.stdin.read()
    if not input_data.strip():
        return

    import re
    tokens = [int(x) for x in re.findall(r'\d+', input_data)]
    if not tokens:
        return

    if len(tokens) % 2 == 1:
        n = tokens[0]
        a1 = tokens[1 : n + 1]
        a2 = tokens[n + 1 : 2 * n + 1]
    else:
        n = len(tokens) // 2
        a1 = tokens[:n]
        a2 = tokens[n:]

    # Array to store the first occurrence index of each prefix sum difference.
    # Diff prefix sum can range from -n to n, so size is 2*n + 1 with offset n.
    first_occ = [-1] * (2 * n + 1)
    
    # Base case: difference of 0 is observed at index 0 (before taking elements)
    first_occ[n] = 0

    curr_sum = 0
    max_len = 0

    for i in range(n):
        curr_sum += a1[i] - a2[i]
        idx = curr_sum + n
        if first_occ[idx] != -1:
            length = (i + 1) - first_occ[idx]
            if length > max_len:
                max_len = length
        else:
            first_occ[idx] = i + 1

    print(max_len)

if __name__ == '__main__':
    solve()