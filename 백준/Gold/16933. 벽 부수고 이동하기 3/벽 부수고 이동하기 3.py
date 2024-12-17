import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    visited = [[[0] * m for _ in range(n)] for _ in range(k+1)]

    # x, y, 움직인 개수, 벽 부순 개수
    q.append((0, 0, 1, 0))
    # [벽 부순 개수][x][y]
    visited[0][0][0] = 1

    while q:
        x, y, move, wall = q.popleft()
        if x == n-1 and y == m-1:
            return move

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 벽이라면, k가 남아야했고, 방문한적 없어야함
                if board[nx][ny] == 1 and wall < k and not visited[wall+1][nx][ny]:
                    # 낮이라면 이동
                    if move % 2 == 1:
                        visited[wall+1][nx][ny] = 1
                        q.append((nx, ny, move+1, wall+1))
                    # 밤이라면 머무르기
                    else:
                        q.append((x, y, move+1, wall))

                elif board[nx][ny] == 0 and not visited[wall][nx][ny]:
                    visited[wall][nx][ny] = 1
                    q.append((nx, ny, move+1, wall))
    return -1



n, m, k = map(int,input().split())
board = [list(map(int,input().strip())) for _ in range(n)]
print(bfs())