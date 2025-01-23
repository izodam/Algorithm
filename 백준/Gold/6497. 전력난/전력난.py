import sys
input = sys.stdin.readline
import heapq

def prim():
    q = []
    visited = [0] * m

    q.append((0, 0))
    res = 0
    while q:
        cost, node = heapq.heappop(q)

        if visited[node]:
            continue

        visited[node] = 1
        res += cost

        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                heapq.heappush(q, (next_cost, next_node))

    return res


while True:
    m, n = map(int,input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(m)]
    before = 0
    for i in range(n):
        x, y, z = map(int,input().split())
        graph[x].append((y, z))
        graph[y].append((x, z))
        before += z



    print(before - prim())