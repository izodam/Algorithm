import sys
input = sys.stdin.readline

from collections import deque
from itertools import permutations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    visited = [[0] * w for _ in range(h)]
    q = deque()

    visited[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 and board[nx][ny] != 'x':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

    return visited




while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    # . : 깨끗, * : 더러움, x : 가구, o : 로봇
    board = [list(input().strip()) for _ in range(h)]
    dirty = []
    robot = []
    for r in range(h):
        for c in range(w):
            if board[r][c] == 'o':
                robot = [r, c]
            elif board[r][c] == '*':
                dirty.append((r, c))

    cnt_dirty = len(dirty)
    visited = bfs(robot[0], robot[1])
    cleaner = [0] * cnt_dirty
    res = float('inf')

    for idx, rc in enumerate(dirty):
        if visited[rc[0]][rc[1]]:
            cleaner[idx] += visited[rc[0]][rc[1]] - 1
        else:
            print(-1)
            break
    else:
        # 더러운 칸 끼리의 거리
        dist = [[0] * cnt_dirty for _ in range(cnt_dirty)]
        for i in range(cnt_dirty):
            visited = bfs(dirty[i][0], dirty[i][1])
            for j in range(i, cnt_dirty):
                dist[i][j] = visited[dirty[j][0]][dirty[j][1]] - 1
                dist[j][i] = dist[i][j]

        for li in permutations(range(cnt_dirty)):
            start = li[0]
            now = cleaner[li[0]]

            for idx in range(1, len(li)):
                end = li[idx]
                now += dist[start][end]
                start = end
            res = min(res, now)
        print(res)