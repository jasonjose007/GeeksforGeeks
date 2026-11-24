# k-th Smallest in BST
# Platform: GFG
# Difficulty: Medium
# Topics: Binary Search Tree

import sys
from collections import deque


sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Return the kth smallest element in the given BST
    def kthSmallest(self, root, k):
        stack = []
        curr = root
        count = 0
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            count += 1
            if count == k:
                return getattr(curr, 'data', getattr(curr, 'val', -1))
            
            curr = curr.right
            
        return -1

def buildTree(s):
    if not s or s[0] == 'N':
        return None
    ip = s.strip().split()
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

def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
    
    lines = [line.strip() for line in input_data if line.strip()]
    if not lines:
        return
    
    sol = Solution()
    
    # Check if the first line is the number of test cases T
    first_tokens = lines[0].split()
    if len(first_tokens) == 1 and first_tokens[0].isdigit():
        t = int(first_tokens[0])
        idx = 1
        for _ in range(t):
            if idx >= len(lines):
                break
            tree_str = lines[idx]
            idx += 1
            if idx >= len(lines):
                break
            k = int(lines[idx])
            idx += 1
            root = buildTree(tree_str)
            print(sol.kthSmallest(root, k))
    else:
        # Alternating tree string and k
        idx = 0
        while idx < len(lines):
            tree_str = lines[idx]
            idx += 1
            if idx < len(lines):
                k = int(lines[idx])
                idx += 1
                root = buildTree(tree_str)
                print(sol.kthSmallest(root, k))

if __name__ == '__main__':
    main()