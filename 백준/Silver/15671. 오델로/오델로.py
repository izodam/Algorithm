change = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]

def sp(x, y, stone):
    for i in range(8):
        nx, ny = x + change[i][0], y + change[i][1]
        stack = []
        while True:
            if 0<=nx<6 and 0<=ny<6:
                if board[nx][ny] == stone:
                    for a,b in stack:
                        board[a][b] = stone
                    break
                elif board[nx][ny] == 0:
                    break
                else:
                    stack.append((nx,ny))
                    nx += change[i][0]
                    ny += change[i][1]
            else:
                break


n = int(input())
board = [[0]*6 for _ in range(6)]

# 가운데 돌 두고 시작 / 1 = 흑돌, 2 = 백돌
board[2][2] = 2
board[3][3] = 2
board[2][3] = 1
board[3][2] = 1

stone = 1
for _ in range(n):
    x, y= map(int, input().split())
    board[x - 1][y - 1] = stone
    sp(x - 1, y - 1, stone)
    stone = 2 if stone == 1 else 1
black = 0
white = 0
for i in range(6):
    for j in range(6):
        if board[i][j] == 1:
            black += 1
            board[i][j] = 'B'
        elif board[i][j] == 2:
            white += 1
            board[i][j] = 'W'
        else:
            board[i][j] = '.'
    print(''.join(map(str,board[i])))
print('White') if white > black else print('Black')