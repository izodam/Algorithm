from collections import deque
import sys
input = sys.stdin.readline
# l = 층수, r,c = 행, 열

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    board[x][y][z] = 0

    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < l and 0 <= ny < r and 0 <= nz < c:
                if board[nx][ny][nz] == 'E':
                    print(f'Escaped in {board[x][y][z]+1} minute(s).')
                    return
                elif board[nx][ny][nz] == '.':
                    board[nx][ny][nz] = board[x][y][z] + 1
                    q.append((nx,ny,nz))


    print('Trapped!')

while True:
    l, r, c = map(int,input().split())
    if l == 0 and r == 0 and c == 0:
        break

    # 지나갈 수 없는 칸은 '#'으로 표현되고, 비어있는 칸은 '.'
    # 시작 지점은 'S'로 표현되고, 탈출할 수 있는 출구는 'E'
    board = []
    for _ in range(l):
        board.append([list(input().strip()) for _ in range(r)])
        next = input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if board[i][j][k] == 'S':
                    bfs(i, j, k)
                    break