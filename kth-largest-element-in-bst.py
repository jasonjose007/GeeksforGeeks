# Kth Largest in BST
# Platform: GFG
# Difficulty: Easy
# Topics: Binary Search Tree, Tree

from collections import deque
import sys

sys.setrecursionlimit(1000000)


class Node:

    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def buildTree(s):
    if len(s) == 0 or s[0] == "N":
        return None

    ip = s.split()
    root = Node(int(ip[0]))
    q = deque()
    q.append(root)

    i = 1
    while len(q) > 0 and i < len(ip):
        currNode = q.popleft()
        currVal = ip[i]

        if currVal != "N":
            currNode.left = Node(int(currVal))
            q.append(currNode.left)

        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]
        if currVal != "N":
            currNode.right = Node(int(currVal))
            q.append(currNode.right)
        i += 1

    return root


def kthLargest(root, k):
    count = 0
    ans = -1

    def reverse_inorder(node):
        nonlocal count, ans
        if not node or count >= k:
            return
        reverse_inorder(node.right)
        count += 1
        if count == k:
            ans = node.data
            return
        reverse_inorder(node.left)

    reverse_inorder(root)
    return ans


def main():
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip()]
    if not lines:
        return

    ptr = 0
    if len(lines) % 2 == 1:
        ptr = 1

    while ptr < len(lines):
        tree_str = lines[ptr]
        ptr += 1
        if ptr < len(lines):
            k = int(lines[ptr])
            ptr += 1
            root = buildTree(tree_str)
            print(kthLargest(root, k))


if __name__ == "__main__":
    main()