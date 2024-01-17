# 1238번
import heapq
import sys

input = sys.stdin.readline
n, m, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start,end,ti = map(int,input().split())
    graph[start].append((end,ti))

INF = 10e8


def dij(s):
    distance = [INF] * (n + 1)
    q = []
    heapq.heappush(q,(0,s))
    distance[s] = 0

    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d:
            continue

        for i in graph[now]:
            if d + i[1] < distance[i[0]]:
                distance[i[0]] = d + i[1]
                heapq.heappush(q,(d+i[1], i[0]))
    return distance
res = 0
for i in range(1, n+1):
    go = dij(i)
    back = dij(x)
    res = max(res, go[x] + back[i])
print(res)