import sys
input = sys.stdin.readline
import heapq

def prim(start):
    visited = [0] * (V+1)
    q = [(0, start)]
    res = 0

    while q:
        cost, v = heapq.heappop(q)
        if visited[v]:
            continue

        visited[v] = 1
        res += cost

        for u, w in graph[v]:
            if not visited[u]:
                heapq.heappush(q, (w, u))
    return res

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(1))