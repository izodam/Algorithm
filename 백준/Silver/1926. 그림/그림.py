#bfs -> deque 사용
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x,y,graph):
    queue = deque()

    #상, 하, 좌, 우 이동
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    #방문 처리
    graph[x][y] = 0
    queue.append((x, y))
    cnt = 1

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt

n,m = map(int,input().split())
paint = []
for i in range(n):
    paint.append(list(map(int,input().split())))

res = []

for i in range(n):
    for j in range(m):
        if paint[i][j]:
            res.append(bfs(i,j,paint))

if len(res) == 0:
    print(0)
    print(0)
else:
    print(len(res))
    print(max(res))

