import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

dp = [0]*n

for i in range(n):
    t = graph[i][0]
    p = graph[i][1]
    dp[i] = max(dp[i-1], dp[i])
    if i+t <= n:
        dp[i+t-1] = max(dp[i-1]+p, dp[i+t-1])

print(dp[-1])