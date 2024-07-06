import heapq
import sys
input = sys.stdin.readline

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        # now까지 가는 최소비용이 아니면 고려 X
        if dist > distance[now]:
            continue

        for e, l in graph[now]:
            cost = dist + l
            if cost < distance[e]:
                distance[e] = cost
                heapq.heappush(q, (cost, e))


n, d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [float('inf')] * (d+1)

# 모든 거리 1로 초기화
for i in range(d):
    graph[i].append((i+1, 1))

# 지름길 update
for _ in range(n):
    s, e, l = map(int,input().split())
    if e > d:
        continue
    graph[s].append((e, l))

dijkstra(0)
print(distance[d])