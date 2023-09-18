from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for _ in range(n)]
# 1 = 익은 토마토, 0 = 안익은 토마토, -1 = 빈칸

q = deque()
#인접(상, 하, 좌, 우)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            q.append((i,j))
def bfs():
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if tomato[nx][ny] == -1:
                continue
            if tomato[nx][ny] == 0:
                q.append((nx,ny))
                tomato[nx][ny] = tomato[x][y] + 1
            if tomato[nx][ny] == 1:
                continue

bfs()
res = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res,max(i))

print(res-1)