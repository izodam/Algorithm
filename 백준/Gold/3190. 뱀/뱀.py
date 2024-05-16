from collections import deque
import sys
input = sys.stdin.readline

# 보드 크기
n = int(input())
board = [[0]*n for _ in range(n)]
snail = deque()

# 사과 개수
k = int(input())

for _ in range(k):
    r, c = map(int,input().split())
    board[r-1][c-1] = 'a'

# 방향 변환 횟수
l = int(input())
change = deque()
for _ in range(l):
    x, c = input().split()
    change.append((int(x), c))

time = 0
# L은 +1, D는 -1
now = 0
direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]


loc = (0,0)
snail.append(loc)
board[0][0] = 1



while True:
    time += 1
    nx = snail[-1][0]+direction[now][0]
    ny = snail[-1][1]+direction[now][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        print(time)
        break

    if board[nx][ny] == 1:
        print(time)
        break

    if not board[nx][ny]:
        tail_x, tail_y = snail.popleft()
        # 사과 존재 X
        board[tail_x][tail_y] = 0

    board[nx][ny] = 1
    snail.append((nx, ny))
    if change and change[0][0] == time:
        x, c = change.popleft()
        if c == 'D':
            now = (now-1)%4
        else:
            now = (now+1)%4
