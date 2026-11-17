# Right View of Binary Tree
# Platform: GFG
# Difficulty: Easy
# Topics: Tree

import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(s):
    if not s or s[0] == 'N':
        return None
    ip = s.split()
    if not ip or ip[0] == 'N':
        return None
    root = Node(int(ip[0]))
    q = deque([root])
    i = 1
    while q and i < len(ip):
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

def rightView(root):
    if not root:
        return []
    ans = []
    q = deque([root])
    while q:
        n = len(q)
        for i in range(n):
            curr = q.popleft()
            if i == n - 1:
                ans.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return ans

def main():
    input_data = sys.stdin.read().splitlines()
    lines = [line.strip() for line in input_data if line.strip()]
    if not lines:
        return
    
    try:
        t = int(lines[0])
        if len(lines) == t + 1:
            lines = lines[1:]
    except ValueError:
        pass

    for s in lines:
        root = buildTree(s)
        res = rightView(root)
        print(*res)

if __name__ == '__main__':
    main()