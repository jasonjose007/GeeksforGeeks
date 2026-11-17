# Multiply 2 Matrices
# Platform: GFG
# Difficulty: Medium
# Topics: Matrix

import ast
import math
from operator import mul


def solve():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break

    if not lines:
        return

    text = " ".join(lines)
    if "[" in text:
        matrices = []
        depth = 0
        start = -1
        for idx, ch in enumerate(text):
            if ch == "[":
                if depth == 0:
                    start = idx
                depth += 1
            elif ch == "]":
                depth -= 1
                if depth == 0 and start != -1:
                    val = ast.literal_eval(text[start : idx + 1])
                    if isinstance(val, list) and val and isinstance(val[0], list):
                        matrices.append(val)
                    start = -1
        mat1, mat2 = matrices[0], matrices[1]
    else:
        nums = list(map(int, text.split()))
        n = nums[0]
        if len(nums) == 1 + 2 * n * n:
            data = nums[1:]
        else:
            n = math.isqrt(len(nums) // 2)
            data = nums
        size = n * n
        mat1 = [data[i * n : (i + 1) * n] for i in range(n)]
        mat2 = [data[size + i * n : size + (i + 1) * n] for i in range(n)]

    cols = list(zip(*mat2))
    res = [[sum(map(mul, row, col)) for col in cols] for row in mat1]
    print(res)


if __name__ == "__main__":
    solve()