# 16433
n, r, c = map(int,input().split())
board = [['.'] * n for _ in range(n)]

board[r-1][c-1] = 'v'

# 둘 다 홀수 or 둘 다 짝수
if (r + c) % 2 == 0:
    for i in range(n):
        if i % 2 == 0:
            for j in range(0, n, 2):
                board[i][j] = 'v'
        else:
            for j in range(1, n, 2):
                board[i][j] = 'v'

else:
    for i in range(n):
        if i % 2 == 0:
            for j in range(1, n, 2):
                board[i][j] = 'v'
        else:
            for j in range(0, n, 2):
                board[i][j] = 'v'

for i in board:
    print(''.join(i))