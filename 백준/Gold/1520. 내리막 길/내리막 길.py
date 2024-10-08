import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] < board[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

print(dfs(0, 0))