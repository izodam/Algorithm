import sys
input = sys.stdin.readline

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 연결 확인
def bfs():
    q = deque()
    visited = [[0]*5 for _ in range(5)]
    cnt = 1
    x = girls[0][0]
    y = girls[0][1]
    visited[x][y] = 1
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
                if [nx, ny] in girls:
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    if cnt == 7:
        return True
    else:
        return False


def back(idx, depth, yeon):
    global res
    if yeon >= 4 or 25 - idx < 7 - depth:
        return
    if depth == 7:
        if bfs():
            res += 1
        return

    x = idx // 5
    y = idx % 5
    if board[x][y] == "Y":
        girls.append([x, y])
        back(idx + 1, depth + 1, yeon + 1)
        girls.pop()
    else:
        girls.append([x, y])
        back(idx + 1, depth+1, yeon)
        girls.pop()

    back(idx+1, depth, yeon)



board = [list(input().strip()) for _ in range(5)]
res = 0

girls = []

back(0,0,0)
print(res)