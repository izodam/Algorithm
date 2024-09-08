import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]
    # x, y, 이동 횟수, 벽 부순 횟수
    q.append((0, 0, 1, 0))
    visited[0][0][0] = 1

    while q:
        x, y, cnt, broke = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽인데 부술 수 있는 개수 남았으면 이동
                if board[nx][ny] == 1 and broke < k and visited[broke+1][nx][ny] == 0:
                    visited[broke+1][nx][ny] = 1
                    q.append((nx, ny, cnt+1, broke+1))
                elif board[nx][ny] == 0 and visited[broke][nx][ny] == 0:
                    visited[broke][nx][ny] = 1
                    q.append((nx, ny, cnt + 1, broke))

n, m, k = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]

res = bfs()
if res:
    print(res)
else:
    print(-1)