import sys
input = sys.stdin.readline
import heapq

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

q = []
visited = [0] * n

heapq.heappush(q, (0, 0))
res = 0
while q:
    cost, node = heapq.heappop(q)
    if visited[node]:
        continue

    visited[node] = 1
    res += cost

    for next_node, next_cost in enumerate(graph[node]):
        if not visited[next_node]:
            heapq.heappush(q, (next_cost, next_node))
print(res)
