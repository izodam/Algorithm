import sys
input = sys.stdin.readline

n, t = map(int,input().split())
unit = [[0, 0]] + [list(map(int,input().split())) for _ in range(n)]
dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, t+1):
        time = unit[i][0]
        score = unit[i][1]

        if j < time:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + score)
print(dp[n][t])