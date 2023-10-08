from collections import deque
m,n,h = map(int,input().split())
# 1:익음, 0: 익지 않음, -1: 비어있음
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                q.append((i,j,k))

def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx<0 or ny<0 or nz<0 or nx>=n or ny>=m or nz>=h:
                continue
            if box[nz][nx][ny] == -1:
                continue
            if box[nz][nx][ny] == 0:
                q.append((nz,nx,ny))
                box[nz][nx][ny] = box[z][x][y]+1
            if box[nz][nx][ny] == 1:
                continue

bfs()
res = 0
for i in box:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        res = max(res,max(j))
print(res-1)