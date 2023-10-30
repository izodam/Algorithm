from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    w,h = map(int,input().split())
    building = [list(input()) for i in range(h)]

    res = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    #상근이와 불난 곳
    s = deque()
    f = deque()

    for i in range(h):
        for k in range(w):
            if building[i][k] == '@':
                s.append((i, k))
            if building[i][k] == '*':
                f.append((i, k))


    def bfs():
        global f, s, res
        while True:
            res += 1
            temp = []
            while f:
                x, y = f.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= h or ny >= w:
                        continue
                    if building[nx][ny] == '.' or building[nx][ny] == '$':
                        temp.append((nx, ny))
                        building[nx][ny] = 'F'
            f = deque(temp)

            temp = []
            while s:
                x, y = s.popleft()
                # 미로 탈출
                if x == 0 or y == 0 or x == h - 1 or y == w - 1:
                    return res
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or ny < 0 or nx >= h or ny >= w:
                        continue
                    if building[nx][ny] == '.':
                        temp.append((nx, ny))
                        # 갔던 곳은 $로 표시
                        building[x][y] = '$'
                        building[nx][ny] = '@'
            s = deque(temp)
            if not s:
                return False


    if bfs():
        print(res)
    else:
        print('IMPOSSIBLE')
