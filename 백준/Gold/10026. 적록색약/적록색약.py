from collections import deque
n = int(input())
grid = [list(input()) for _ in range(n)]
q = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n:
                if grid[nx][ny]==grid[x][y] and not visited[nx][ny]:
                    #방문처리
                    visited[nx][ny] = 1
                    q.append((nx,ny))

#적록색약이 아닌 경우
cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt,end=' ')

#적록색약인 경우_빨,초 같은색으로 인식 -> G를 R로 바꾸고 bfs
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'G':
            grid[i][j] = 'R'

cnt = 0
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1
print(cnt)