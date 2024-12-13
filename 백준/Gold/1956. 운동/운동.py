import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int,input().split())
graph = [[INF] * (v+1) for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int,input().split())
    graph[a][b] = c

for k in range(1, v+1):
    for a in range(1, v+1):
        for b in range(1, v+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

res = INF
for i in range(1, v+1):
    res = min(res, graph[i][i])
if res == INF:
    print(-1)
else:
    print(res)