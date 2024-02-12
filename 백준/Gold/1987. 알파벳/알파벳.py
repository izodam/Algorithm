# 1987번
def dfs(x,y):
    stack = set([(0, 0, graph[0][0])])
    res = 0

    while stack:
        x, y, v = stack.pop()
        res = max(res, len(v))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<r and 0<=ny<c and graph[nx][ny] not in v:
                # 방문처리
                stack.add((nx,ny,v+graph[nx][ny]))
    return res



r, c = map(int,input().split())
graph = [list(input()) for _ in range(r)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


print(dfs(0, 0))