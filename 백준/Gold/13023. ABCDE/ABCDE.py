def dfs(x, d):
    global res
    visited[x] = 1

    if d == 5:
        res = 1
        return

    for i in graph[x]:
        if not visited[i]:
            dfs(i, d+1)
        if res:
            return

    visited[x] = 0



n, m = map(int,input().split())
graph = [[] for _ in range(n)]
visited = [0] * n
res = 0

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for x in range(n):
    dfs(x, 1)
    if res:
        print(1)
        break
else:
    print(0)
