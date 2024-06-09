import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

def dfs(v):
    global cnt
    visited[v] = 1

    res[v] = cnt
    graph[v].sort(reverse=True)
    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            dfs(i)


n, m, r = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
res = [0] * (n+1)
cnt = 1

for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(r)

print('\n'.join(map(str,res[1:])))