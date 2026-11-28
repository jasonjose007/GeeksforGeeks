# Sort Matrix
# Platform: GFG
# Difficulty: Easy
# Topics: Matrix

import ast

def solve():
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip():
            lines.append(line.strip())

    if not lines:
        return

    raw = "\n".join(lines)
    if raw[0] == "[":
        mat = ast.literal_eval(raw)
        if not mat:
            print(mat)
            return
        vals = sorted(x for row in mat for x in row)
        res = []
        idx = 0
        for row in mat:
            k = len(row)
            res.append(vals[idx:idx + k])
            idx += k
        print(res)
        return

    tokens = [int(x) for line in lines for x in line.split()]
    first_line = [int(x) for x in lines[0].split()]

    if len(first_line) == 1 and len(tokens) == 1 + first_line[0] * first_line[0]:
        n = first_line[0]
        vals = sorted(tokens[1:])
        for i in range(0, n * n, n):
            print(*vals[i:i + n])
    elif len(first_line) == 2 and len(tokens) == 2 + first_line[0] * first_line[1]:
        r, c = first_line
        vals = sorted(tokens[2:])
        for i in range(0, r * c, c):
            print(*vals[i:i + c])
    elif len(first_line) == 1 and len(lines) > 1:
        t = first_line[0]
        pos = 1
        for _ in range(t):
            n = tokens[pos]
            pos += 1
            vals = sorted(tokens[pos:pos + n * n])
            pos += n * n
            for i in range(0, n * n, n):
                print(*vals[i:i + n])
    else:
        r = len(lines)
        c = len(first_line)
        vals = sorted(tokens)
        for i in range(0, r * c, c):
            print(*vals[i:i + c])

if __name__ == "__main__":
    solve()