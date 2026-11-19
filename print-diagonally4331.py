# Matrix Diagonal Traversal
# Platform: GFG
# Difficulty: Easy
# Topics: Matrix

import ast
import math

def solve():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except (EOFError, StopIteration):
            break

    if not lines:
        return

    joined = " ".join(lines)
    if "[" in joined:
        idx = joined.find("[")
        mat = ast.literal_eval(joined[idx:])
        n = len(mat)
    else:
        tokens = list(map(int, joined.split()))
        L = len(tokens)
        r = math.isqrt(L)
        r1 = math.isqrt(L - 1) if L >= 1 else -1
        if r * r == L:
            n = r
            start = 0
        elif L >= 2 and r1 * r1 == L - 1 and tokens[0] == r1:
            n = r1
            start = 1
        elif L >= 3 and tokens[0] == tokens[1] and tokens[0] * tokens[0] == L - 2:
            n = tokens[0]
            start = 2
        else:
            n = tokens[0]
            start = 1
        mat = [tokens[start + i * n : start + (i + 1) * n] for i in range(n)]

    res = []
    for s in range(2 * n - 1):
        i_start = max(0, s - n + 1)
        i_end = min(n - 1, s)
        for i in range(i_start, i_end + 1):
            res.append(str(mat[i][s - i]))

    print(" ".join(res))

solve()