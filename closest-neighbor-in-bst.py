# Floor in BST
# Platform: GFG
# Difficulty: Easy
# Topics: Binary Search Tree, Tree

from collections import deque
import re
import sys


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:

    def floor(self, root, x):
        ans = -1
        curr = root
        while curr:
            val = getattr(curr, "data", getattr(curr, "val", None))
            if val == x:
                return x
            elif val < x:
                ans = val
                curr = curr.right
            else:
                curr = curr.left
        return ans


def build_tree(tokens):
    if not tokens or tokens[0] in ("N", "null", "None"):
        return None
    root = Node(int(tokens[0]))
    q = deque([root])
    i = 1
    while q and i < len(tokens):
        curr = q.popleft()

        if i < len(tokens):
            if tokens[i] not in ("N", "null", "None"):
                curr.left = Node(int(tokens[i]))
                q.append(curr.left)
            i += 1

        if i < len(tokens):
            if tokens[i] not in ("N", "null", "None"):
                curr.right = Node(int(tokens[i]))
                q.append(curr.right)
            i += 1
    return root


def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return

    lines = [line.strip() for line in input_data.splitlines() if line.strip()]
    sol = Solution()

    i = 0
    if (
        len(lines) > 1
        and lines[0].isdigit()
        and (len(lines) - 1) % 2 == 0
        and len(lines) - 1 == 2 * int(lines[0])
    ):
        i = 1

    while i < len(lines):
        line = lines[i]

        if "k" in line:
            k_match = re.search(r"k\s*=\s*(\d+)", line)
            tree_match = re.search(r"root\s*=\s*\[(.*?)\]", line)
            if k_match and tree_match:
                k_val = int(k_match.group(1))
                tree_str = tree_match.group(1)
                tokens = tree_str.replace(",", " ").split()
                root = build_tree(tokens)
                print(sol.floor(root, k_val))
                i += 1
                continue

        if i + 1 < len(lines):
            tree_str = lines[i]
            k_str = lines[i + 1]

            tree_tokens = (
                tree_str.replace("[", " ")
                .replace("]", " ")
                .replace(",", " ")
                .split()
            )
            k_match = re.search(r"\d+", k_str)
            if k_match and tree_tokens:
                k_val = int(k_match.group(0))
                root = build_tree(tree_tokens)
                print(sol.floor(root, k_val))
                i += 2
                continue

        i += 1


if __name__ == "__main__":
    main()