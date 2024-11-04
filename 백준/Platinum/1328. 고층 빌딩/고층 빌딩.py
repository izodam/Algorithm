import sys
input = sys.stdin.readline
n, l, r = map(int, input().split())
# dp[0][1][2]에 대해서
# [0]개 건물이 있을 때 [1]개가 왼쪽에서 보이고 [2]개가 오른쪽에서 보임
dp = [[[0] * (n+1) for i in range(n+1)] for _ in range(n+1)]

# 건물 1개일 때의 경우의 수는 1
dp[1][1][1] = 1

for i in range(1, n):
    for j in range(1, i+1):
        for k in range(1, i+1):
            if not dp[i][j][k]:
                continue
            dp[i+1][j+1][k] += dp[i][j][k]
            dp[i+1][j][k+1] += dp[i][j][k]
            dp[i+1][j][k] += dp[i][j][k] * (i-1)


print(dp[n][l][r] % 1000000007)