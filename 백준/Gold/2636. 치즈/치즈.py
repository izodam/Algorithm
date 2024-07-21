import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def find_melt():
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if board[nx][ny] == 1:
                    melt.append((nx, ny))
                else:
                    q.append((nx, ny))
                visited[nx][ny] = 1

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
before = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            before += 1

cnt = 1

while True:
    melt = []
    visited = [[0] * m for _ in range(n)]
    find_melt()

    for x, y in melt:
        board[x][y] = 0

    if before - len(melt) == 0:
        print(cnt)
        print(before)
        break
    else:
        cnt += 1
        before -= len(melt)