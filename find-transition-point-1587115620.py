# Transition Point in Sorted Binary
# Platform: GFG
# Difficulty: Easy
# Topics: Arrays, Searching

import sys
import bisect
import re

def main():
    input_data = sys.stdin.read()
    if not input_data.strip():
        return
    
    tokens = [int(x) for x in re.findall(r'\d+', input_data)]
    if not tokens:
        return
    
    if tokens[0] > 1 or (len(tokens) > 1 and tokens[0] == 1 and tokens[1] == 0):
        N = tokens[0]
        arr = tokens[1:1+N]
    else:
        arr = tokens
        
    n = len(arr)
    idx = bisect.bisect_left(arr, 1)
    if idx < n and arr[idx] == 1:
        print(idx)
    else:
        print(-1)

if __name__ == '__main__':
    main()