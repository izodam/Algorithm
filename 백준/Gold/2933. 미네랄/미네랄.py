# 2933
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def move(bottom, group):
    # 제일 바닥에 있을 경우는 내릴 필요가 없음
    # if bottom == r-1:
    #     return
    # bottom_list = []
    # for x, y in group:
    #     if x == bottom:
    #         bottom_list.append(y)

    # print(group, bottom)
    minus = 0
    flag = 0
    while True:
        if bottom == r-1:
            break
        for x, y in group:
            if (x+minus+1, y) not in group and (board[x+minus+1][y] == 'x' or new_board[x+minus+1][y] == 'x'):
                flag = 1
                break
        if flag:
            break
        else:
            minus += 1
            bottom += 1

    for x, y in group:
        new_board[x+minus][y] = 'x'
    # print(new_board)






def bfs(x, y):
    group = []
    q = deque()
    # visited = [[0] * c for _ in range(r)]
    bottom = x

    # 방문 처리
    q.append((x, y))
    group.append((x, y))
    board[x][y] = '.'
    # visited[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 'x':
                bottom = max(bottom, nx)
                q.append((nx, ny))
                group.append((nx, ny))
                board[nx][ny] = '.'
    move(bottom, group)

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

n = int(input())
# rs 인덱스가 짝수면 왼 -> 오, 홀수면 오 -> 왼
rs = list(map(int,input().split()))

for turn in range(n):
    new_board = [['.'] * c for _ in range(r)]
    h = r - rs[turn]
    # 미네랄 있으면 부시기
    if turn % 2 == 0:
        for i in range(c):
            if board[h][i] == 'x':
                board[h][i] = '.'
                break

    else:
        for i in range(c-1, -1, -1):
            if board[h][i] == 'x':
                board[h][i] = '.'
                break

    # 공중에 클러스터 존재 시 내리기
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'x':
                bfs(i, j)

    board = [i.copy() for i in new_board]

for i in board:
    print(''.join(i))