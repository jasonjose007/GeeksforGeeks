# BFS of Graph
# Platform: GFG
# Difficulty: Easy
# Topics: Graph, BFS

import sys
import ast
from collections import deque


def bfs(adj):
    v = len(adj)
    if v == 0:
        return []
    visited = [False] * v
    visited[0] = True
    q = deque([0])
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for nxt in adj[u]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return res


def main():
    raw = sys.stdin.read()
    stripped = raw.strip()
    if not stripped:
        return

    if "[" in stripped:
        adj = ast.literal_eval(stripped[stripped.find("["):])
        print(bfs(adj))
    else:
        lines = raw.splitlines()
        while lines and not lines[0].strip():
            lines.pop(0)
        first = lines[0].split()
        if len(first) == 1:
            v = int(first[0])
            adj = [
                list(map(int, lines[i + 1].split())) if i + 1 < len(lines) else []
                for i in range(v)
            ]
        else:
            v, e = int(first[0]), int(first[1])
            adj = [[] for _ in range(v)]
            for i in range(1, min(len(lines), e + 1)):
                parts = lines[i].split()
                if len(parts) >= 2:
                    u, w = int(parts[0]), int(parts[1])
                    adj[u].append(w)
                    adj[w].append(u)
        print(*bfs(adj))


if __name__ == "__main__":
    main()