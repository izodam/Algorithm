import sys
input = sys.stdin.readline
n, m, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
dp = [[-float('inf')] * m for _ in range(n)]

for i in range(m):
    dp[-1][i] = 0

# 아래에서부터 본다
for row in range(n-2, -1, -1):
    for col in range(m):
        # 행 증가
        for rowplus in range(1, d+1):
            for colplus in range(-d + rowplus, d - rowplus + 1):
                if 0 <= row + rowplus < n and 0 <= col + colplus < m:
                    dp[row][col] = max(dp[row][col],
                                       board[row][col] * board[row + rowplus][col + colplus] + dp[row + rowplus][
                                           col + colplus])

print(max(dp[0]))