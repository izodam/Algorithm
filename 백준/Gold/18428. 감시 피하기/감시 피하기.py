import sys
input = sys.stdin.readline
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 선생님의 상하좌우에 학생이 있는지 확인
# 있으면 장애물을 놔야하는 위치 중 하나
def check_have_to_block(x, y):
    for direction in range(4):
        now = []
        nx = x + dx[direction]
        ny = y + dy[direction]
        while (0 <= nx < n and 0 <= ny < n):
            if board[nx][ny] == 'S':
                # 만약 선생님과 학생사이에 빈칸이 하나도 없다면 감시 무조건 못피함
                if not now:
                    print("NO")
                    exit()
                have_to_block.update(now)
                break

            if board[nx][ny] == 'X':
                now.append((nx, ny))
            else:
                break
            nx += dx[direction]
            ny += dy[direction]

def check_student(x, y):
    for direction in range(4):
        nx = x + dx[direction]
        ny = y + dy[direction]
        while 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 'O' and board[nx][ny] != 'T':
            if board[nx][ny] == 'S':
                return False
            nx += dx[direction]
            ny += dy[direction]
    return True

n = int(input())
board = [list(input().split()) for _ in range(n)]
have_to_block = set()
blank = []
teacher = []

for row in range(n):
    for col in range(n):
        if board[row][col] == 'T':
            # check_have_to_block(row, col)
            teacher.append((row, col))
        if board[row][col] == 'X':
            blank.append((row, col))

for i in combinations(blank, 3):
    for x, y in i:
        board[x][y] = 'O'

    for x, y in teacher:
        if not check_student(x, y):
            break
    else:
        print('YES')
        exit()
    for x, y in i:
        board[x][y] = 'X'
print("NO")