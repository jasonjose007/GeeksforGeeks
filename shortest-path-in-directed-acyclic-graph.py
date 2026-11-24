# Shortest Path in Directed Acyclic Graph
# Platform: GFG
# Difficulty: Medium
# Topics: Graph, Shortest Path

import sys
from collections import deque

def shortest_path(V, edges):
    adj = [[] for _ in range(V)]
    in_degree = [0] * V
    for u, v, wt in edges:
        adj[u].append((v, wt))
        in_degree[v] += 1

    # Topological Sort using Kahn's algorithm
    q = deque([i for i in range(V) if in_degree[i] == 0])
    topo = []
    while q:
        u = q.popleft()
        topo.append(u)
        for v, _ in adj[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    # Initialize distances
    dist = [float('inf')] * V
    dist[0] = 0

    for u in topo:
        if dist[u] != float('inf'):
            for v, wt in adj[u]:
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt

    return [d if d != float('inf') else -1 for d in dist]

class Solution:
    def shortestPath(self, V, *args):
        if len(args) == 1:
            edges = args[0]
        else:
            edges = args[1]
        return shortest_path(V, edges)

def main():
    input_text = sys.stdin.read().strip()
    if not input_text:
        return

    import re

    # Try parsing format: V = ..., edges = [...]
    if "edges" in input_text or "V" in input_text:
        # Match all occurrences of V and edges
        pattern = re.compile(r'V\s*=\s*(\d+).*?edges\s*=\s*(\[.*?\]\])', re.DOTALL)
        matches = pattern.findall(input_text)
        if matches:
            for v_str, edges_str in matches:
                V = int(v_str)
                edges = eval(edges_str)
                ans = shortest_path(V, edges)
                print(ans)
            return

    # Fallback to standard competitive programming input
    tokens = input_text.split()
    if not tokens:
        return

    it = iter(tokens)
    
    # Try reading as test cases or single test case
    # If the first token might be T (number of testcases), or V
    # We can detect by checking remaining tokens
    all_tokens = list(map(int, tokens))
    idx = 0
    
    def solve_one(V, E, idx):
        edges = []
        for _ in range(E):
            edges.append([all_tokens[idx], all_tokens[idx+1], all_tokens[idx+2]])
            idx += 3
        return shortest_path(V, edges), idx

    try:
        # Check if first number is T
        if len(all_tokens) >= 3:
            # Check if all_tokens[0] is T
            T_candidate = all_tokens[0]
            # Verify if following can form T test cases
            temp_idx = 1
            valid_T = True
            for _ in range(T_candidate):
                if temp_idx + 1 >= len(all_tokens):
                    valid_T = False
                    break
                v = all_tokens[temp_idx]
                e = all_tokens[temp_idx + 1]
                temp_idx += 2 + 3 * e
            if valid_T and temp_idx == len(all_tokens):
                idx = 1
                for _ in range(T_candidate):
                    v = all_tokens[idx]
                    e = all_tokens[idx + 1]
                    idx += 2
                    res, idx = solve_one(v, e, idx)
                    print(*(res))
                return

        # Otherwise, process as stream of (V, E, edges...)
        idx = 0
        while idx < len(all_tokens):
            v = all_tokens[idx]
            e = all_tokens[idx + 1]
            idx += 2
            res, idx = solve_one(v, e, idx)
            print(*(res))
    except Exception:
        pass

if __name__ == '__main__':
    main()