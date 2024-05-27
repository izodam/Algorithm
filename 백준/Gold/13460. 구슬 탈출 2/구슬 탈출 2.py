# 13460. 구슬 탈출 2
from collections import deque

def move_stone(nx, ny, direction_x, direction_y):
    while True:
        nx += direction_x
        ny += direction_y
        if board[nx][ny] == '#':
            nx -= direction_x
            ny -= direction_y
            break
        if board[nx][ny] == 'O':
            break
    return nx, ny

def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx ,by))
    visited = []
    visited.append((rx, ry, bx, by))
    cnt = 0

    while q:
        for _ in range(len(q)):
            rx, ry, bx ,by = q.popleft()
            if cnt > 10:
                print(-1)
                return
            if board[rx][ry] == 'O':
                print(cnt)
                return

            for i in range(4):
                nrx, nry = move_stone(rx, ry, dx[i], dy[i])
                nbx, nby = move_stone(bx, by, dx[i], dy[i])

                # 파란 구슬 구멍에 들어가면
                if board[nbx][nby] == 'O':
                    continue
                # 두 구슬 위치 같음
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by) :
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:  # 방문하지 않았다면 방문 처리
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        cnt += 1
    print(-1)


n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            bx, by = i, j
        elif board[i][j] == 'R':
            rx, ry = i, j

bfs(rx, ry, bx, by)