# Left View of Binary Tree
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

def LeftView(root):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        n = len(q)
        for i in range(n):
            curr = q.popleft()
            if i == 0:
                res.append(curr.data)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
    return res

def main():
    lines = sys.stdin.read().splitlines()
    if not lines:
        return
    
    lines = [line.strip() for line in lines if line.strip()]
    if not lines:
        return

    if len(lines) == 1:
        t = 1
        start_idx = 0
    else:
        try:
            val = int(lines[0])
            if len(lines) - 1 == val:
                t = val
                start_idx = 1
            else:
                t = len(lines)
                start_idx = 0
        except ValueError:
            t = len(lines)
            start_idx = 0
            
    for i in range(start_idx, start_idx + t):
        if i < len(lines):
            s = lines[i]
            root = buildTree(s)
            res = LeftView(root)
            print(*res)

if __name__ == '__main__':
    main()