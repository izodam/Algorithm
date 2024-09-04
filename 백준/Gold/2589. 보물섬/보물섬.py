import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return max(map(max, visited)) - 1


n, m = map(int, input().split())
board = [list(input().strip()) for _ in range(n)]


res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            res = max(res, bfs(i, j))
print(res)