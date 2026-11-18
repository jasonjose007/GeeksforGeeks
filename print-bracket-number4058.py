# Bracket Numbers
# Platform: GFG
# Difficulty: Easy
# Topics: Strings, Stack, Regular Expression

import sys

def solve():
    s = sys.stdin.read().strip()
    if not s:
        return
    stack = []
    res = []
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
            stack.append(count)
            res.append(count)
        elif ch == ')':
            res.append(stack.pop())
    print(" ".join(map(str, res)))

if __name__ == "__main__":
    solve()