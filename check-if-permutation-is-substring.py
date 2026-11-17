# Check if Permutation is Substring
# Platform: GFG
# Difficulty: Easy
# Topics: Strings, sliding-window

import sys

def solve():
    input_data = sys.stdin.read().split()
    if len(input_data) < 2:
        return
    txt = input_data[0]
    pat = input_data[1]

    n = len(txt)
    m = len(pat)

    if m > n:
        print("false")
        return

    pat_counts = [0] * 26
    win_counts = [0] * 26

    for i in range(m):
        pat_counts[ord(pat[i]) - 97] += 1
        win_counts[ord(txt[i]) - 97] += 1

    if pat_counts == win_counts:
        print("true")
        return

    for i in range(m, n):
        win_counts[ord(txt[i]) - 97] += 1
        win_counts[ord(txt[i - m]) - 97] -= 1
        if pat_counts == win_counts:
            print("true")
            return

    print("false")

if __name__ == "__main__":
    solve()