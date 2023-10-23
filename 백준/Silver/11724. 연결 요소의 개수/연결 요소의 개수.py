import sys

sys.setrecursionlimit(5000)
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


cnt = 0
for i in range(n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        cnt += 1

print(cnt-1)