# Unique Number I
# Platform: GFG
# Difficulty: Easy
# Topics: Bit Magic

import sys
import re

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    tokens = []
    for token in input_data:
        nums = re.findall(r'-?\d+', token)
        for n in nums:
            tokens.append(int(n))
            
    if not tokens:
        return

    def try_parse_T_N(tokens):
        if len(tokens) < 3:
            return None
        T = tokens[0]
        if T <= 0:
            return None
        curr = 1
        results = []
        for _ in range(T):
            if curr >= len(tokens):
                return None
            N = tokens[curr]
            curr += 1
            if N <= 0 or curr + N > len(tokens):
                return None
            arr = tokens[curr : curr + N]
            curr += N
            results.append(arr)
        if curr == len(tokens):
            return results
        return None

    def try_parse_N(tokens):
        if len(tokens) < 2:
            return None
        N = tokens[0]
        if N > 0 and len(tokens) == N + 1:
            return [tokens[1:]]
        return None

    res = try_parse_T_N(tokens)
    if res is not None:
        for arr in res:
            ans = 0
            for x in arr:
                ans ^= x
            print(ans)
        return

    res = try_parse_N(tokens)
    if res is not None:
        for arr in res:
            ans = 0
            for x in arr:
                ans ^= x
            print(ans)
        return

    ans = 0
    for x in tokens:
        ans ^= x
    print(ans)

if __name__ == '__main__':
    solve()