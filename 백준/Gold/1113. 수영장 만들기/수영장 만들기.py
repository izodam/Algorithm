import sys
input = sys.stdin.readline
# 보드에서 테두리가 아닌 곳에서 시작
# 해당 숫자를 감싸는 해당 숫자보다 큰 범위가 있으면 수영장 가능
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    now = board[x][y]
    wall = 9
    pool = [(x, y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in (-1, n) or ny in (-1, m):
                return 0

            if visited[nx][ny] == 0 and board[nx][ny] <= now:
                q.append((nx, ny))
                visited[nx][ny] = 1
                pool.append((nx, ny))
            elif board[nx][ny] > now:
                wall = min(wall, board[nx][ny])

    water = 0
    for x, y in pool:
        water += wall - board[x][y]
        board[x][y] = wall
    return water



n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
res = 0
for i in range(1, n-1):
    for j in range(1, m-1):
        res += bfs(i, j)
print(res)