# Longest Valid Word with All Prefixes
# Platform: GFG
# Difficulty: Medium
# Topics: Trie

import sys

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        print("")
        return

    if '=' in input_data:
        input_data = input_data.split('=', 1)[1].strip()

    words = []
    import ast
    try:
        parsed = ast.literal_eval(input_data)
        if isinstance(parsed, list):
            words = [str(x) for x in parsed]
    except Exception:
        pass

    if not words:
        import re
        tokens = re.findall(r'"([^"]*)"|\'([^\']*)\'|([a-zA-Z0-9]+)', input_data)
        extracted = []
        for t in tokens:
            val = t[0] or t[1] or t[2]
            if val:
                extracted.append(val)
        if extracted and extracted[0].isdigit():
            extracted = extracted[1:]
        words = extracted

    if not words:
        print("")
        return

    S = set(words)
    best = ""

    for w in words:
        valid = True
        for i in range(1, len(w) + 1):
            if w[:i] not in S:
                valid = False
                break
        if valid:
            if len(w) > len(best) or (len(w) == len(best) and w < best):
                best = w

    print(best)

if __name__ == '__main__':
    solve()