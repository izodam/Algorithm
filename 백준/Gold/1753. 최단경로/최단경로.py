# 1753번_heapq 사용
import heapq
import sys
input = sys.stdin.readline

V, E = map(int,input().split())
k = int(input())
INF = 10e8
graph = [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))

distance = [INF for _ in range(V+1)]

def dij(s):
    q = []
    heapq.heappush(q,(0, s))
    distance[s] = 0

    while q:
        d, now = heapq.heappop(q)

        if distance[now] < d:
            continue
        for i in graph[now]:
            if d + i[1] < distance[i[0]]:
                distance[i[0]] = d + i[1]
                heapq.heappush(q,(d+i[1], i[0]))


dij(k)
for i in distance[1:]:
    if i == INF:
        print('INF')
    else:
        print(i)