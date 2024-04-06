import sys
input = sys.stdin.readline

def cal(x, y):
    res = 0
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            nx = x - 1 + i
            ny = y - 1 + j
            if 0<=nx<n and 0<=ny<n and '1' <= board[nx][ny] <= '9':
                res += int(board[nx][ny])
    return res


n = int(input())
board = [list(input().strip()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if '1' <= board[i][j] <= '9':
            print('*', end='')
        else:
            if cal(i,j) > 9:
                print('M', end='')
            else:
                print(cal(i,j), end='')
    print()