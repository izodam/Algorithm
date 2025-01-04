import sys
input = sys.stdin.readline
INF = int(10e9)
n, k = map(int,input().split())
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(k):
  a, b = map(int,input().split())
  graph[a][b] = 1

for k in range(1, n+1):
  graph[k][k] = 0
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


s = int(input())
for _ in range(s):
  a, b = map(int,input().split())
  if graph[a][b] != INF:
    print(-1)
  elif graph[b][a] != INF:
    print(1)
  else:
    print(0)