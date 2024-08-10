import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque([(0, 0)])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 빈칸인데 방문한적 없는 곳이면 방문
                if board[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                # 치즈가 있으면 해당 visited에 개수 세줌
                if board[nx][ny] == 1:
                    visited[nx][ny] += 1




n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
cnt = 1

while True:
    visited = [[0] * m for _ in range(n)]
    bfs()

    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                board[i][j] = 0
    if sum(sum(row) for row in board):
        cnt += 1
    else:
        print(cnt)
        break