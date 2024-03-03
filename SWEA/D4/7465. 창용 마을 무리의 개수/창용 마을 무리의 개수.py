from collections import deque

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


T = int(input())
for tc in range(1, T+1):
    n, m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = 0
    visited = [0] * (n+1)

    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            res += 1
    print(f'#{tc}',res)