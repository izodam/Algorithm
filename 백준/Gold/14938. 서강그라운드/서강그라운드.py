import sys
import heapq

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    cnt = 0

    while q:
        d, node = heapq.heappop(q)
        if d > distance[node] or d > m:
            continue
        cnt += items[node]

        for next_node, next_dis in graph[node]:
            now = next_dis + d
            if now < distance[next_node] and now <= m:
                distance[next_node] = now
                heapq.heappush(q, (now, next_node))
    return cnt


n, m, r = map(int,input().split())
# 각 구역에 있는 아이템의 수
items = [0] + list(map(int,input().split()))
INF = float('inf')
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int,input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

res = 0
for i in range(1, n+1):
    distance = [INF] * (n+1)
    # dij(i)
    # cnt = 0
    # for node in range(1, n+1):
    #     if distance[node] <= m:
    #         cnt += items[node]
    res = max(res, dij(i))
print(res)