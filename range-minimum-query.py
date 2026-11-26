# Range Minimum Query
# Platform: GFG
# Difficulty: Medium
# Topics: Segment-Tree, Advanced Data Structure

import sys
import ast


def solve():
    data = sys.stdin.read()
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    if not lines:
        return

    if '[' in lines[0]:
        arr = ast.literal_eval(lines[0])
        queries = ast.literal_eval(lines[1])
        q_tokens = []
        for l, r in queries:
            q_tokens.append(l)
            q_tokens.append(r)
    else:
        parsed = [list(map(int, line.split())) for line in lines]
        arr = None
        q_tokens = []

        if (
            len(parsed) >= 3
            and len(parsed[0]) == 1
            and len(parsed[1]) == parsed[0][0]
            and len(parsed[2]) == 1
        ):
            n_cand = parsed[0][0]
            q_cand = parsed[2][0]
            tokens = [x for row in parsed[3:] for x in row]
            if len(tokens) == 2 * q_cand and all(
                0 <= tokens[i] <= tokens[i + 1] < n_cand
                for i in range(0, len(tokens), 2)
            ):
                arr = parsed[1]
                q_tokens = tokens

        if arr is None and len(parsed) >= 2 and len(parsed[0]) == 2 and len(parsed[1]) == parsed[0][0]:
            n_cand, q_cand = parsed[0]
            tokens = [x for row in parsed[2:] for x in row]
            if len(tokens) == 2 * q_cand and all(
                0 <= tokens[i] <= tokens[i + 1] < n_cand
                for i in range(0, len(tokens), 2)
            ):
                arr = parsed[1]
                q_tokens = tokens

        if arr is None:
            if len(parsed) >= 2 and len(parsed[1]) == 1:
                arr = parsed[0]
                q_tokens = [x for row in parsed[2:] for x in row]
            elif len(parsed) == 2:
                arr = parsed[0]
                q_tokens = parsed[1]
            else:
                arr = parsed[0]
                q_tokens = [x for row in parsed[1:] for x in row]

    n = len(arr)
    st = [arr]
    half = 1
    while (half << 1) <= n:
        prev = st[-1]
        st.append(list(map(min, prev, prev[half:])))
        half <<= 1

    ans = []
    append = ans.append
    for i in range(0, len(q_tokens), 2):
        l = q_tokens[i]
        r = q_tokens[i + 1]
        k = (r - l + 1).bit_length() - 1
        row = st[k]
        a = row[l]
        b = row[r - (1 << k) + 1]
        append(a if a < b else b)

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()