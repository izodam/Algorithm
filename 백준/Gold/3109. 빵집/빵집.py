move = [-1, 0, 1]

def dfs(x,y):
    if y == c-1:
        return True
    for i in range(3):
        nx = x + move[i]
        ny = y + 1
        if 0<=nx<r and 0<=ny<c:
            if board[nx][ny] != 'x' and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if dfs(nx, ny):
                    return True
    return False


r, c = map(int,input().split())
board = [list(input().strip()) for _ in range(r)]

res = 0
visited = [[0] * c for _ in range(r)]
for i in range(r):
    if dfs(i,0):
        res += 1
print(res)