# 14502. 연구소
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(now):
    q = deque(virus)

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and now[nx][ny] == 0:
                q.append((nx, ny))
                now[nx][ny] = 2


n, m = map(int,input().split())
# 0은 빈 칸, 1은 벽, 2는 바이러스
board = [list(map(int,input().split())) for _ in range(n)]
blank = []
virus = []

res = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            blank.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

# 빈칸 중 3개 골라서 벽 세우기
for walls in combinations(blank, 3):
    now = [i.copy() for i in board]
    for r, c in walls:
        now[r][c] = 1

    bfs(now)
    cnt = 0

    for i in now:
        cnt += i.count(0)
    res = max(res, cnt)

print(res)
