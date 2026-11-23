# Nodes Without Sibling
# Platform: GFG
# Difficulty: Easy
# Topics: Tree

import sys
from collections import deque

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTree(s):
    if not s or s[0] == "N":
        return None
    ip = list(map(str, s.split()))
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

def noSibling(root):
    ans = []
    if not root:
        return [-1]
    
    q = deque([root])
    while q:
        curr = q.popleft()
        if curr.left and not curr.right:
            ans.append(curr.left.data)
        elif curr.right and not curr.left:
            ans.append(curr.right.data)
            
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
            
    if not ans:
        return [-1]
    ans.sort()
    return ans

def main():
    lines = sys.stdin.read().splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    if not lines:
        return
    
    try:
        t = int(lines[0])
        if len(lines) == t + 1:
            tree_lines = lines[1:]
        else:
            tree_lines = lines
    except ValueError:
        tree_lines = lines

    for line in tree_lines:
        root = buildTree(line)
        res = noSibling(root)
        print(" ".join(map(str, res)))

if __name__ == '__main__':
    main()