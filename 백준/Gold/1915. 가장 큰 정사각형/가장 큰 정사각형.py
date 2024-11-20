import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for r in range(n):
    for c in range(m):
        if r == 0 or c == 0:
            dp[r][c] = board[r][c]
        elif board[r][c] == 0:
            dp[r][c] = 0
        else:
            dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1

print(max(map(max, dp)) ** 2)