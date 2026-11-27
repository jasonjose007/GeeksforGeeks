# Row with Minimum 1s
# Platform: GFG
# Difficulty: Easy
# Topics: Matrix

import sys
import ast
import re

def main():
    content = sys.stdin.read().strip()
    if not content:
        return

    # Handle Python list representation input format
    if '[' in content:
        start = content.find('[')
        end = content.rfind(']')
        if start != -1 and end != -1:
            try:
                mat = ast.literal_eval(content[start:end+1])
                if isinstance(mat, list) and len(mat) > 0 and isinstance(mat[0], list):
                    min_ones = float('inf')
                    best_row = 1
                    for i in range(len(mat)):
                        ones = sum(mat[i])
                        if ones < min_ones:
                            min_ones = ones
                            best_row = i + 1
                    print(best_row)
                    return
            except Exception:
                pass

    # Handle standard flat integer stream input format
    tokens = list(map(int, re.findall(r'-?\d+', content)))
    if not tokens:
        return

    idx = 0
    # Determine if the first token is test case count T
    if len(tokens) > 2:
        n, m = tokens[0], tokens[1]
        if len(tokens) != 2 + n * m:
            t = tokens[0]
            if len(tokens) > 3:
                n1, m1 = tokens[1], tokens[2]
                if len(tokens) == 1 + t * (2 + n1 * m1) or len(tokens) >= 1 + 2 + n1 * m1:
                    idx = 1

    while idx < len(tokens):
        if idx + 1 >= len(tokens):
            break
        n = tokens[idx]
        m = tokens[idx+1]
        idx += 2
        
        min_ones = float('inf')
        best_row = 1
        
        for i in range(n):
            ones = 0
            for _ in range(m):
                if idx < len(tokens):
                    ones += tokens[idx]
                    idx += 1
            if ones < min_ones:
                min_ones = ones
                best_row = i + 1
        print(best_row)

if __name__ == '__main__':
    main()