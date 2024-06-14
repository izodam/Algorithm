from collections import deque
import sys
input = sys.stdin.readline


def find(target):
    if parents[target] == target:
        return target
    parents[target] = find(parents[target])
    return parents[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parents[a] = b

def kruskal():
    cnt = 0
    cost = 0

    for a, b, c in edges:
        if find(a) != find(b):
            adj[a].append((b, c))
            adj[b].append((a, c))
            union(a, b)
            cnt += 1
            cost += c
            if cnt == n-1:
                return cost

def bfs(s):
    visited = [0] * n
    q = deque([(s, 0)])
    visited[s] = 1
    max_dist = 0

    while q:
        now, dist = q.pop()
        max_dist = max(max_dist, dist)
        for nxt, cost in adj[now]:
            if not visited[nxt]:
                visited[nxt] = 1
                q.appendleft((nxt, dist+cost))
    return max_dist

n, k = map(int,input().split())
edges = [tuple(map(int,input().split())) for _ in range(k)]
# 비용이 작은 순으로 정렬
edges.sort(key=lambda x:x[2])
parents = [i for i in range(n)]
adj = [[] for _ in range(n)]

total_cost = kruskal()
max_dist = 0

for s in range(n):
    if len(adj[s]) == 1:
        max_dist = max(max_dist, bfs(s))

print(total_cost)
print(max_dist)