# 2606번
def dfs(v):
    stack = [v]
    visited[v] = 1

    # while True:
    #     for w in graph[v]:
    #         if not visited[w]:
    #             visited[w] = 1
    #             stack.append(w)
    #             v = w
    #             break
    #     else:
    #         if stack:
    #             v = stack.pop()
    #         else:
    #             break

    while stack:
        n = stack.pop()
        for next_node in graph[n]:
            if not visited[next_node]:
                visited[next_node] = 1
                stack.append(next_node)


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