import sys
input = sys.stdin.readline
import heapq

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = []
res = []
for node in range(1, n+1):
    if indegree[node] == 0:
        heapq.heappush(q, node)

while q:
    now = heapq.heappop(q)
    res.append(now)
    for next in graph[now]:
        indegree[next] -= 1

        if indegree[next] == 0:
            heapq.heappush(q, next)

print(*res)