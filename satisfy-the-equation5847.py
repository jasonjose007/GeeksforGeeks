# Two Pairs with Same Sum
# Platform: GFG
# Difficulty: Medium
# Topics: Hash, Sorting, Map

import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    arr = [int(x) for x in data]
    n = len(arr)
    
    if n < 4:
        print("-1 -1 -1 -1")
        return

    pair_map = {}
    best_quad = None

    for i in range(n):
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s in pair_map:
                for a, b in pair_map[s]:
                    if b != i and b != j:
                        quad = (a, b, i, j)
                        if best_quad is None or quad < best_quad:
                            best_quad = quad
                        break
        for j in range(i + 1, n):
            s = arr[i] + arr[j]
            if s not in pair_map:
                pair_map[s] = []
            pair_map[s].append((i, j))

    if best_quad is None:
        print("-1 -1 -1 -1")
    else:
        print(f"{best_quad[0]} {best_quad[1]} {best_quad[2]} {best_quad[3]}")

if __name__ ==