import sys
input = sys.stdin.readline

def dfs(x, y, hp, cnt):
    global res

    for i in range(len(milk)):
        if not visited[i]:
            length = abs(milk[i][0] - x) + abs(milk[i][1] - y)
            if hp >= length:
                visited[i] = 1
                dfs(milk[i][0], milk[i][1], hp-length+h, cnt+1)
                visited[i] = 0
    if hp >= abs(home[0]-x) + abs(home[1]-y):
        res = max(res, cnt)

n, m, h = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]

milk = []
home = []
res = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            home = [i, j]
        elif board[i][j] == 2:
            milk.append((i, j))


visited = [0] * len(milk)

dfs(home[0], home[1], m, 0)
print(res)