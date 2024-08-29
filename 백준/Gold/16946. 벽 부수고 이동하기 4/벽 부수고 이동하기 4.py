import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, number):
    q = deque([(x, y)])
    group[x][y] = number
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and group[nx][ny] == 0:
                q.append((nx, ny))
                group[nx][ny] = number
                cnt += 1

    return cnt



n, m = map(int,input().split())
board = [list(map(int, input().strip())) for _ in range(n)]


group = [[0] * m for _ in range(n)]
group_cnt = {0: 0}
res = [[0] * m for _ in range(n)]
number = 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0 and group[i][j] == 0:
            now = bfs(i, j, number)
            group_cnt[number] = now
            number += 1

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end='')
        else:
            cnt = 0
            g = set()
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = i + dx
                ny = j + dy
                if 0 <= nx < n and 0 <= ny < m:
                    g.add(group[nx][ny])
            for group_num in g:
                cnt += group_cnt[group_num]
            print((cnt+1)%10, end='')
    print()