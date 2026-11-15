# Search in Sorted Matrix
# Platform: GFG
# Difficulty: Medium
# Topics: Searching, Matrix

import sys
import bisect

def try_parse(tokens, start_idx):
    idx = start_idx
    cases = []
    n_tokens = len(tokens)
    while idx < n_tokens:
        if idx + 2 > n_tokens:
            return None
        n = tokens[idx]
        m = tokens[idx + 1]
        idx += 2
        needed = n * m + 1
        if idx + needed > n_tokens:
            return None
        arr = tokens[idx : idx + n * m]
        x = tokens[idx + n * m]
        cases.append((arr, x))
        idx += needed
    if idx == n_tokens:
        return cases
    return None

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    tokens = [int(x) for x in input_data]
    
    cases = try_parse(tokens, 1)
    if cases is None:
        cases = try_parse(tokens, 0)
        
    if cases is None:
        return

    for arr, x in cases:
        idx = bisect.bisect_left(arr, x)
        if idx < len(arr) and arr[idx] == x:
            print("true")
        else:
            print("false")

if __name__ == '__main__':
    main()