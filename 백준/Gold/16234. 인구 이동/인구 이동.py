# 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    lst = [(x, y, board[x][y])]

    q = deque()
    q.append((x, y, board[x][y]))
    board[x][y] = 0

    while q:
        x, y, p = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and l <= abs(p - board[nx][ny]) <= r:
                q.append((nx, ny, board[nx][ny]))
                lst.append((nx, ny, board[nx][ny]))
                board[nx][ny] = 0
    return lst




n, l, r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

cnt = 0
while True:
    lst = []
    # 연합국가 찾음
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                lst.append(bfs(i, j))

    flag = 0
    
    for i in lst:
        if len(i) == 1:
            x, y, people = i[0]
            board[x][y] = people
            flag += 1
            continue
        p = 0
        for x, y, people in i:
            p += people
        for x, y, people in i:
            board[x][y] = p // len(i)
    if flag == len(lst):
        break
    cnt += 1
print(cnt)
