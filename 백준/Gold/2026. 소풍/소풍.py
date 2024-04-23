import sys
input = sys.stdin.readline

def dfs(depth, x, arr):
    if depth == k:
        print('\n'.join(map(str, arr)))
        exit()
    for i in range(x+1, n+1):
        if not visited[i]:
            for j in arr:
                if j not in graph[i]:
                    break
            else:
                visited[i] = 1
                dfs(depth+1, i, arr+[i])



k, n, f = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(f):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    visited = [0] * (n+1)
    visited[i] = 1
    dfs(1, i, [i])
print(-1)