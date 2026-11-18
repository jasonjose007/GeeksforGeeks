# Dijkstra Algorithm
# Platform: GFG
# Difficulty: Medium
# Topics: Graph

import heapq
import sys

class Solution:
    def dijkstra(self, adj, src):
        V = len(adj)
        dist = [float('inf')] * V
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if d > dist[u]:
                continue
                
            for edge in adj[u]:
                v, wt = edge[0], edge[1]
                if dist[u] + wt < dist[v]:
                    dist[v] = dist[u] + wt
                    heapq.heappush(pq, (dist[v], v))
                    
        return dist

if __name__ == '__main__':
    input_data = sys.stdin.read().split()
    if input_data:
        it = iter(input_data)
        
        def next_token():
            return next(it, None)
            
        first = next_token()
        if first is not None:
            # Check if first token could be number of test cases T
            # or V directly.
            # Try reading as T test cases or single test case.
            tokens = [first]
            for tok in it:
                tokens.append(tok)
                
            # If input is formatted with T test cases
            # Standard GFG: T, then for each testcase: V E, E lines of (u, v, w), src
            idx = 0
            
            def solve_test():
                nonlocal idx
                if idx >= len(tokens):
                    return False
                V = int(tokens[idx])
                E = int(tokens[idx + 1])
                idx += 2
                adj = [[] for _ in range(V)]
                for _ in range(E):
                    u = int(tokens[idx])
                    v = int(tokens[idx + 1])
                    w = int(tokens[idx + 2])
                    adj[u].append([v, w])
                    adj[v].append([u, w])
                    idx += 3
                src = int(tokens[idx])
                idx += 1
                
                sol = Solution()
                res = sol.dijkstra(adj, src)
                print(*(res))
                return True

            # Check if tokens[0] is T
            # If tokens has (1 + sum(2 + 3*E + 1)), then tokens[0] is T
            try:
                T = int(tokens[0])
                # verify if it looks like T
                cur = 1
                valid_T = True
                for _ in range(T):
                    if cur + 1 >= len(tokens):
                        valid_T = False
                        break
                    v_val = int(tokens[cur])
                    e_val = int(tokens[cur + 1])
                    cur += 2 + 3 * e_val + 1
                if valid_T and cur == len(tokens):
                    idx = 1
                    for _ in range(T):
                        solve_test()
                else:
                    idx = 0
                    while idx < len(tokens):
                        solve_test()
            except Exception:
                pass