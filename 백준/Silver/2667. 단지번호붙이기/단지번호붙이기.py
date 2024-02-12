# 1987번
def dfs(x,y):
    cnt = 1
    graph[x][y] = 0
    stack = [(x, y)]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and  0<=ny<n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                stack.append((nx,ny))
                cnt += 1
    return cnt



n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

res = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            res.append(dfs(i, j))

print(len(res))
res.sort()
print('\n'.join(map(str,res)))