import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
dist = [float('inf')] * (n+1)
dist[1] = 0
for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
for i in range(n):
    for idx, temp in enumerate(graph):
        if idx == 0:
            continue

        for next_node, cost in temp:
            if dist[idx] != float('inf') and dist[idx] + cost < dist[next_node]:
                dist[next_node] = dist[idx] + cost
                if i == n-1:
                    print(-1)
                    exit()
for i in range(2, n+1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])