# Character at Position in Infinite String
# Platform: GFG
# Difficulty: Medium
# Topics: Mathematics, Strings, Recursion

import sys

def solve():
    lines = sys.stdin.read().splitlines()
    while lines and not lines[-1].strip():
        lines.pop()
    if not lines:
        return
    if len(lines) == 1:
        parts = lines[0].split()
        s = parts[0]
        pos = int(parts[1])
    else:
        s = lines[0]
        pos = int(lines[1].strip())

    lengths = [len(s)]
    i = 0
    while lengths[-1] < pos:
        i += 1
        lengths.append(2 * lengths[-1] + i)

    while i > 0:
        prev_len = lengths[i - 1]
        if pos <= prev_len:
            pass
        elif pos <= prev_len + i:
            print('$')
            return
        else:
            pos = lengths[i] + 1 - pos
        i -= 1

    print(s[pos - 1])

if __name__ == '__main__':
    solve()