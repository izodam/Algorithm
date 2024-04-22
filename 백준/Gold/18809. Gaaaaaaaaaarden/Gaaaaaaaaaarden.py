# 18809
import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(board):
    global res
    new_board = [i.copy() for i in board]
    cnt = 0

    # print('\n'.join(map(str,new_board)))
    # print()

    green = deque()
    red = deque()
    for i in range(n):
        for j in range(m):
            if new_board[i][j] == 'G':
                green.append((i, j))
            if new_board[i][j] == 'R':
                red.append((i, j))
            if new_board[i][j] == 2:
                new_board[i][j] = 1



    while green and red:
        new_green = set()
        new_red = set()

        while green:
            gx, gy = green.popleft()
            # 초록색 이동
            for i in range(4):
                nx = gx + dx[i]
                ny = gy + dy[i]
                if 0 <= nx < n and 0 <= ny < m and new_board[nx][ny] == 1:
                    new_green.add((nx, ny))

        while red:
            rx, ry = red.popleft()
            # 빨간색 이동
            for i in range(4):
                nx = rx + dx[i]
                ny = ry + dy[i]
                if 0 <= nx < n and 0 <= ny < m and new_board[nx][ny] == 1:
                    new_red.add((nx,ny))

        for x, y in new_green:
            if (x, y) in new_red:
                cnt += 1
            else:
                green.append((x, y))
            new_board[x][y] = 0
        # print(green, )

        for x, y in new_red:
            if (x, y) in new_green:
                continue
            else:
                red.append((x, y))
            new_board[x][y] = 0

    # print('--------------------------------')
    # if cnt > res:
    #     res = cnt
    #     print(cnt)
    #     print('\n'.join(map(str,board)))
    #     print()
    res = max(res, cnt)


def dfs(depth,g, r):
    if can_water-depth < g+r:
        return

    if g == 0 and r == 0:
        bfs(board)
        return



    # 해당 위치에 배양액 아무것도 뿌리지 않음
    dfs(depth+1, g, r)

    x, y = water[depth]
    # 해당 위치에 초록색 배양액
    if g > 0:
        board[x][y] = 'G'
        dfs(depth+1, g-1, r)
        board[x][y] = 1

    # 해당 위치에 빨간색 배양액
    if r > 0:
        board[x][y] = 'R'
        dfs(depth+1, g, r-1)
        board[x][y] = 1



n, m, g, r = map(int,input().split())
# 0은 호수, 1은 배양액을 뿌릴 수 없는 땅, 2는 배양액을 뿌릴 수 있는 땅
board = [list(map(int,input().split())) for _ in range(n)]


# 배양액 뿌릴 수 있는 칸 찾기
water = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            water.append((i, j))

can_water = len(water)


res = 0
dfs(0, g, r)
print(res)