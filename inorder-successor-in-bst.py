# Inorder Successor in BST
# Platform: GFG
# Difficulty: Easy
# Topics: Binary Search Tree

from collections import deque
import re


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def build_tree(tokens):
    if not tokens or tokens[0] in ("N", "null", "None", "#"):
        return None
    root = Node(int(tokens[0]))
    q = deque([root])
    i = 1
    n = len(tokens)
    while q and i < n:
        curr = q.popleft()
        if i < n:
            if tokens[i] not in ("N", "null", "None", "#"):
                curr.left = Node(int(tokens[i]))
                q.append(curr.left)
            i += 1
        if i < n:
            if tokens[i] not in ("N", "null", "None", "#"):
                curr.right = Node(int(tokens[i]))
                q.append(curr.right)
            i += 1
    return root


def inorder_successor(root, k):
    succ = None
    curr = root
    while curr is not None:
        if k < curr.data:
            succ = curr
            curr = curr.left
        else:
            curr = curr.right
    return succ.data if succ is not None else -1


def parse_tokens(s):
    return s.replace("[", " ").replace("]", " ").replace(",", " ").split()


def solve():
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

    if len(lines) == 1:
        line = lines[0]
        m_root = re.search(r"\[([^\]]*)\]", line)
        m_k = re.search(r"k\s*=\s*(-?\d+)", line)
        if m_root and m_k:
            tokens = parse_tokens(m_root.group(1))
            k = int(m_k.group(1))
            root = build_tree(tokens)
            print(inorder_successor(root, k))
            return

    if len(lines) >= 3:
        first_tokens = parse_tokens(lines[0])
        if len(first_tokens) == 1 and first_tokens[0].lstrip("-").isdigit():
            t = int(first_tokens[0])
            if len(lines) == 1 + 2 * t:
                idx = 1
                for _ in range(t):
                    tokens = parse_tokens(lines[idx])
                    k = int(parse_tokens(lines[idx + 1])[-1])
                    root = build_tree(tokens)
                    print(inorder_successor(root, k))
                    idx += 2
                return

    tokens = parse_tokens(lines[0].split("=", 1)[-1])
    k = int(parse_tokens(lines[1].split("=", 1)[-1])[-1])
    root = build_tree(tokens)
    print(inorder_successor(root, k))


if __name__ == "__main__":
    solve()