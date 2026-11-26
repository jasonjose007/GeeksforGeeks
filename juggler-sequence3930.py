# Juggler Sequence
# Platform: GFG
# Difficulty: Easy
# Topics: Mathematics, Recursion, series

import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    
    seq = [n]
    curr = n
    while curr != 1:
        if curr % 2 == 0:
            curr = math.isqrt(curr)
        else:
            curr = math.isqrt(curr ** 3)
        seq.append(curr)
    
    print(*seq)

if __name__ == '__main__':
    solve()