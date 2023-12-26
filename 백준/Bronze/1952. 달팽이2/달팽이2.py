dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())

g = [[-1] * n for _ in range(m)]

x = y = 0
g[x][y] = 0
cnt = 0
d = 0

while True:
    changed = False
    go = False
    for i in range(d, d+4):
        nx, ny = x + dx[i%4], y + dy[i%4]
        if nx < 0 or ny < 0 or nx >= m or ny >= n or g[nx][ny] != -1:
            changed = True
            continue
        go = True
        g[nx][ny] = 0
        x, y, d = nx, ny, i%4
        break
    if changed == True and go == True:
        cnt += 1
    if go == False:
        break
    
print(cnt)