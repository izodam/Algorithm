import sys
input = sys.stdin.readline
import heapq

n, e = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int,input().split())


def dij(s):
    distance = [float('inf') for _ in range(n+1)]
    q = []
    # 시작점 추가
    heapq.heappush(q, (0, s))
    distance[s] = 0

    while q:
        dis, now = heapq.heappop(q)

        if distance[now] < dis:
            continue

        for i in graph[now]:
            cost = dis + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance

original = dij(1)
v1_dij = dij(v1)
v2_dij = dij(v2)

v1_first = original[v1] + v1_dij[v2] + v2_dij[n]
v2_first = original[v2] + v2_dij[v1] + v1_dij[n]

res = min(v1_first, v2_first)
if res == float('inf'):
    print(-1)
else:
    print(res)