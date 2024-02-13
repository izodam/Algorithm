# 2606번
def dfs(v):
    stack = [v]
    visited[v] = 1

    while True:
        for w in graph[v]:
            if not visited[w]:
                visited[w] = 1
                stack.append(v)
                v = w
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)
dfs(1)

print(sum(visited)-1)