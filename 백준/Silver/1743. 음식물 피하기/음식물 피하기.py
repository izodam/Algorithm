# 1743번
from collections import deque
n, m, k = map(int,input().split())
graph = [[0] * m for _ in range(n)]

# 음식물은 1로 표시
for _ in range(k):
    r,c = map(int,input().split())
    graph[r-1][c-1] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x,y):
    cnt = 0
    q = deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt += 1
    return cnt

res = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            res = max(res,bfs(i,j))

print(res)