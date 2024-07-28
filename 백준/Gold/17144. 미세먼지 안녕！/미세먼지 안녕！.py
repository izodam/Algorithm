import sys
input = sys.stdin.readline
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def move_dust():
    dust = []
    for i in range(r):
        for j in range(c):
            if board[i][j] > 0:
                dust.append((i, j, board[i][j]))

    for x, y, val in dust:
        spread = val // 5
        cnt = 0
        if spread > 0:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != -1:
                    board[nx][ny] += spread
                    cnt += 1
        board[x][y] -= spread * cnt


def move_cleaner():
    # 위쪽 공기청정기 :
    # 같은 행은 오른쪽 이동
    # 가장 오른쪽 열(c)은 위로 이동
    # 가장 위쪽 행(0)은 왼쪽 이동
    # 가장 왼쪽 열(0)은 아래로 이동
    x = cleaner[0][0]
    before = board[x][1]
    board[x][1] = 0
    for i in range(2, c):
        tmp = board[x][i]
        board[x][i] = before
        before = tmp
    for i in range(x-1, -1, -1):
        tmp = board[i][c-1]
        board[i][c-1] = before
        before = tmp
    for i in range(c-2, -1, -1):
        tmp = board[0][i]
        board[0][i] = before
        before = tmp
    for i in range(1, x):
        tmp = board[i][0]
        board[i][0] = before
        before = tmp

    # 아래쪽 공기청정기 :
    # 같은 행은 오른쪽 이동
    # 가장 오른쪽 열(c)은 아래로 이동
    # 가장 아래쪽 행(r)은 왼쪽 이동
    # 가장 왼쪽 열(0)은 위로 이동
    x = cleaner[1][0]
    before = board[x][1]
    board[x][1] = 0
    for i in range(2, c):
        tmp = board[x][i]
        board[x][i] = before
        before = tmp
    for i in range(x+1, r):
        tmp = board[i][c - 1]
        board[i][c - 1] = before
        before = tmp
    for i in range(c - 2, -1, -1):
        tmp = board[r-1][i]
        board[r-1][i] = before
        before = tmp
    for i in range(r-2, x, -1):
        tmp = board[i][0]
        board[i][0] = before
        before = tmp



r, c, t = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]

# 0번 인덱스가 위쪽 공기청정기
cleaner = []

for i in range(r):
    if board[i][0] == -1:
        cleaner.append((i, 0))

for time in range(t):
    move_dust()
    move_cleaner()


res = 0
for i in board:
    res += sum(i)
# 공기청정기 표시 -1 더해주기
print(res + 2)