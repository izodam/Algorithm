import sys
input = sys.stdin.readline

n, m = map(int,input().split())
d = [int(input()) for _ in range(n)]

dp = [[float('-inf')] * (m+1) for _ in range(n+1)]
dp[n][0] = 0

for i in range(n-1, -1, -1):
    for j in range(m+1):
        # 지침정도가 0이 아니라면
        if j > 0:
            # 지침정도가 0이 될 때가 n보다 작아야함
            if i + j <= n:
                # 이때의 거리는 지침정도가 0이 됬을 때의 거리!!
                dp[i][j] = max(dp[i][j], dp[i+j][0])

        # 지침정도가 m보다 작아야만 달릴 수 있다
        if j < m:
            # 이때의 거리는 나보다 지침정도 + 1 일때 + 지금의 달릴 수 있는 거리
            dp[i][j] = max(dp[i][j], dp[i+1][j+1] + d[i])

        # 현재 위치의 지침정도 0일 때는 달렸을 때랑 쉬었을 때랑 중 큰 값
        dp[i][0] = max(dp[i][0], dp[i+1][0])

print(dp[0][0])