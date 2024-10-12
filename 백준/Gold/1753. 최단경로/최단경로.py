import sys
input = sys.stdin.readline
import heapq
n, m = map(int,input().split())
k = int(input())

# 해당 노드에서 출발했을 때의 (도착점, 가중치)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int,input().split())
    graph[u].append((v, w))


distance = [float('inf') for _ in range(n+1)]

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
    if i == float('inf'):
        print('INF')
    else:
        print(i)