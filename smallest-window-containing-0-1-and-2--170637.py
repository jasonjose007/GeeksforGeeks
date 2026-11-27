# Smallest Window With 0, 1 and 2
# Platform: GFG
# Difficulty: Easy
# Topics: sliding-window, two-pointer-algorithm, Strings

import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    s = input_data[0]

    last0 = last1 = last2 = -1
    min_len = float("inf")

    for i, ch in enumerate(s):
        if ch == "0":
            last0 = i
        elif ch == "1":
            last1 = i
        elif ch == "2":
            last2 = i

        if last0 != -1 and last1 != -1 and last2 != -1:
            min_pos = min(last0, last1, last2)
            current_len = i - min_pos + 1
            if current_len < min_len:
                min_len = current_len

    if min_len == float("inf"):
        print(-1)
    else:
        print(min_len)


if __name__ == "__main__":
    solve()