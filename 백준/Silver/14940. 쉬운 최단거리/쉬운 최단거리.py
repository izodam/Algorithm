# 14940번
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
res = [[-1]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    res[x][y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and res[nx][ny] == -1:
                if graph[nx][ny] == 0:
                    res[nx][ny] = 0
                elif graph[nx][ny] == 1:
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and res[i][j] == -1:
            bfs(i,j)

for i in range(n):
    # print(' '.join(map(str,res[i])))
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(res[i][j], end = ' ')
    print()