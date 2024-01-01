# 2156번
n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0] * (n+2)
if n <= 2:
    print(sum(wine))
else:
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(dp[1], wine[1]+wine[2], wine[0]+wine[2])
    for i in range(3,n):
        dp[i] = max(dp[i-1], wine[i]+dp[i-2], wine[i]+wine[i-1]+dp[i-3])

    print(max(dp))