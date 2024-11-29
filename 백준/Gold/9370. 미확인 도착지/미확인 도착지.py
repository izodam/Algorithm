import sys
input = sys.stdin.readline

import heapq
INF = int(1e9)

def dij(start):
    q = []
    distance = [INF] * (n+1)

    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        cost, node = heapq.heappop(q)
        if distance[node] < cost:
            continue
        for next_node, next_cost in graph[node]:
            now = cost + next_cost
            if now < distance[next_node]:
                distance[next_node] = now
                heapq.heappush(q, (now, next_node))
    return distance

T = int(input())
for tc in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    destination_candidate = [int(input()) for _ in range(t)]

    first = dij(s)
    g_dij = dij(g)
    h_dij = dij(h)

    res = []
    for destination in destination_candidate:
        if first[g] + g_dij[h] + h_dij[destination] == first[destination] or first[h] + h_dij[g] + g_dij[destination] == first[destination]:
            res.append(destination)

    print(' '.join(map(str, sorted(res))))