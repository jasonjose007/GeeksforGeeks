# Prefix Suffix Strings
# Platform: GFG
# Difficulty: Medium
# Topics: Strings, Trie

import re
import sys


def solve():
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip()]

    if len(lines) < 2:
        return

    s1 = re.findall(r"[a-zA-Z0-9]+", lines[0])
    s2 = re.findall(r"[a-zA-Z0-9]+", lines[1])

    trie_pre = {}
    for s in s1:
        curr = trie_pre
        for ch in s:
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

    trie_suf = {}
    for s in s1:
        curr = trie_suf
        for ch in reversed(s):
            if ch not in curr:
                curr[ch] = {}
            curr = curr[ch]

    count = 0
    for w in s2:
        # Check if w is a prefix of any string in s1
        curr = trie_pre
        is_pre = True
        for ch in w:
            if ch not in curr:
                is_pre = False
                break
            curr = curr[ch]

        if is_pre:
            count += 1
            continue

        # Check if w is a suffix of any string in s1
        curr = trie_suf
        is_suf = True
        for ch in reversed(w):
            if ch not in curr:
                is_suf = False
                break
            curr = curr[ch]

        if is_suf:
            count += 1

    print(count)


if __name__ == "__main__":
    solve()