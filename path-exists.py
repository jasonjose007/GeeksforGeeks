# Path Exists Between Two Vertices
# Platform: GFG
# Difficulty: Easy
# Topics: BFS, Graph, DFS

import sys
from collections import deque

def is_path(V, adj, u, v):
    if u < 0 or u >= V or v < 0 or v >= V:
        return False
    if u == v:
        return True
    
    visited = [False] * V
    queue = deque([u])
    visited[u] = True
    
    while queue:
        curr = queue.popleft()
        if curr == v:
            return True
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return False

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    tokens = [int(x) for x in input_data]
    n = len(tokens)
    
    is_T_present = False
    if n > 0:
        T = tokens[0]
        ptr = 1
        valid = True
        for _ in range(T):
            if ptr + 2 > n:
                valid = False
                break
            V = tokens[ptr]
            E = tokens[ptr + 1]
            needed = 2 + 2 * E + 2
            if ptr + needed > n:
                valid = False
                break
            ptr += needed
        if valid and ptr == n:
            is_T_present = True

    ptr = 1 if is_T_present else 0
    
    while ptr < n:
        if ptr + 2 > n:
            break
        V = tokens[ptr]
        E = tokens[ptr + 1]
        ptr += 2
        
        adj = [[] for _ in range(V)]
        for _ in range(E):
            if ptr + 2 > n:
                break
            u_edge = tokens[ptr]
            v_edge = tokens[ptr + 1]
            ptr += 2
            if 0 <= u_edge < V and 0 <= v_edge < V:
                adj[u_edge].append(v_edge)
                adj[v_edge].append(u_edge)
        
        if ptr + 2 <= n:
            u = tokens[ptr]
            v = tokens[ptr + 1]
            ptr += 2
        else:
            u, v = 0, 0
            
        if is_path(V, adj, u, v):
            print("true")
        else:
            print("false")

if __name__ == '__main__':
    main()