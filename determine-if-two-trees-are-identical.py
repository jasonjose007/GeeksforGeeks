# Identical Trees
# Platform: GFG
# Difficulty: Easy
# Topics: Tree

import re
from collections import deque


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def isIdentical(self, r1, r2):
        stack = [(r1, r2)]
        while stack:
            n1, n2 = stack.pop()
            if n1 is None and n2 is None:
                continue
            if n1 is None or n2 is None or n1.data != n2.data:
                return False
            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))
        return True


NULL_TOKENS = {"N", "n", "null", "NULL", "None", "#"}


def parse_tokens(s):
    s = s.strip()
    if "=" in s:
        s = s.split("=", 1)[1].strip()
    if s.startswith("[") and s.endswith("]"):
        s = s[1:-1]
    s = s.replace(",", " ")
    return s.split()


def build_tree(tokens):
    if not tokens or tokens[0] in NULL_TOKENS:
        return None
    root = Node(int(tokens[0]))
    q = deque([root])
    i = 1
    n = len(tokens)
    while q and i < n:
        curr = q.popleft()
        if tokens[i] not in NULL_TOKENS:
            curr.left = Node(int(tokens[i]))
            q.append(curr.left)
        i += 1
        if i >= n:
            break
        if tokens[i] not in NULL_TOKENS:
            curr.right = Node(int(tokens[i]))
            q.append(curr.right)
        i += 1
    return root


def main():
    lines = []
    while True:
        try:
            line = input().strip()
            if line:
                lines.append(line)
        except EOFError:
            break

    if not lines:
        return

    sol = Solution()

    if len(lines) == 1:
        parts = re.findall(r"\[[^\]]*\]", lines[0])
        if len(parts) >= 2:
            r1 = build_tree(parse_tokens(parts[0]))
            r2 = build_tree(parse_tokens(parts[1]))
            print("true" if sol.isIdentical(r1, r2) else "false")
        return

    if len(lines) > 2 and lines[0].isdigit() and len(lines) == 1 + 2 * int(lines[0]):
        t = int(lines[0])
        idx = 1
        for _ in range(t):
            r1 = build_tree(parse_tokens(lines[idx]))
            r2 = build_tree(parse_tokens(lines[idx + 1]))
            print("true" if sol.isIdentical(r1, r2) else "false")
            idx += 2
    else:
        r1 = build_tree(parse_tokens(lines[0]))
        r2 = build_tree(parse_tokens(lines[1]))
        print("true" if sol.isIdentical(r1, r2) else "false")


if __name__ == "__main__":
    main()