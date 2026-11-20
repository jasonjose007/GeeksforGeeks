# Longest Substring with Distinct Characters
# Platform: GFG
# Difficulty: Medium
# Topics: Strings, two-pointer-algorithm, sliding-window

import sys

def longest_unique_substr(s):
    last_idx = {}
    max_len = 0
    start = 0
    for i, ch in enumerate(s):
        if ch in last_idx and last_idx[ch] >= start:
            start = last_idx[ch] + 1
        last_idx[ch] = i
        curr_len = i - start + 1
        if curr_len > max_len:
            max_len = curr_len
    return max_len

def main():
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    if tokens[0].isdigit():
        t = int(tokens[0])
        for i in range(1, t + 1):
            if i < len(tokens):
                print(longest_unique_substr(tokens[i]))
    else:
        for s in tokens:
            print(longest_unique_substr(s))

if __name__ == '__main__':
    main()