import sys
input = sys.stdin.readline
from collections import  deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    # 연합 이루는 국경
    lst = [(x, y, board[x][y])]

    q = deque()
    q.append((x, y, board[x][y]))
    board[x][y] = 0

    while q:
        x, y, pn = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and l <= abs(pn - board[nx][ny]) <= r:
                # print(pn, board[nx][ny], (nx, ny), (x, y))
                q.append((nx, ny, board[nx][ny]))
                lst.append((nx, ny, board[nx][ny]))
                board[nx][ny] = 0
    return lst


n, l, r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
res = 0


while True:
    lst = []
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                lst.append(bfs(i, j))

    flag = 0
    p = 0
    for y in lst:
        if len(y) == 1:
            x, c, people = y[0]
            board[x][c] = people
            flag += 1
            continue
        p = 0
        for x, c, people in y:
            p += people
        for x, c, people in y:
            board[x][c] = p // len(y)
    if flag == len(lst):
        break
    res += 1
print(res)


