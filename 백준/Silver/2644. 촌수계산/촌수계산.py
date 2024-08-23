def dfs(v, num):
    num += 1
    visited[v] = 1

    if v == b:
        res.append(num)

    for i in graph[v]:
        if not visited[i]:
            dfs(i, num)

n = int(input())
a, b = map(int,input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

res = []

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, 0)

if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)