# 12100. 2048(Easy)

import sys
input = sys.stdin.readline

# direction = 0: 동, 1: 서, 2: 남, 3: 북
def move(direction, board):
    if direction == 0:
        for i in range(n):
            last = n-1
            for j in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][last] == 0:
                        board[i][last] = tmp
                    elif board[i][last] == tmp:
                        board[i][last] = tmp * 2
                        last -= 1
                    else:
                        last -= 1
                        board[i][last] = tmp
    elif direction == 1:
        for i in range(n):
            last = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][last] == 0:
                        board[i][last] = tmp
                    elif board[i][last] == tmp:
                        board[i][last] = tmp * 2
                        last += 1
                    else:
                        last += 1
                        board[i][last] = tmp

    elif direction == 2:
        for j in range(n):
            last = n-1
            for i in range(n-2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[last][j] == 0:
                        board[last][j] = tmp
                    elif board[last][j] == tmp:
                        board[last][j] = tmp * 2
                        last -= 1
                    else:
                        last -= 1
                        board[last][j] = tmp

    else:
        for j in range(n):
            last = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[last][j] == 0:
                        board[last][j] = tmp
                    elif board[last][j] == tmp:
                        board[last][j] = tmp * 2
                        last += 1
                    else:
                        last += 1
                        board[last][j] = tmp
    return board

def dfs(board, cnt):
    global res
    if cnt == 5:
        now = max(map(max, board))
        res = max(res, now)
        return
    for direction in range(4):
        # copy_board = [i.copy() for i in board]
        now_board = move(direction, [i.copy() for i in board])
        dfs(now_board, cnt+1)


n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]

res = 0
dfs(board, 0)
print(res)