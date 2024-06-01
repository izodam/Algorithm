# 1325. 효율적인 해킹
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque()
    visited = [0] * (n+1)

    cnt = 1
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        for nx in graph[x]:
            if not visited[nx]:
                q.append(nx)
                visited[nx] = 1
                cnt += 1
    return cnt

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[b].append(a)


res = []
max_res = 0

for i in range(1, n+1):
    now = bfs(i)
    if max_res < now:
        max_res = now
        res = [i]
    elif max_res == now:
        res.append(i)

print(' '.join(map(str, res)))