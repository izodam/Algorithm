n, k = map(int,input().split())
s = [0] + list(map(int,input().split()))

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    s[i] %= 2
    for j in range(k+1):
        if s[i] == 0:
            dp[i][j] = dp[i-1][j] + 1

        if j != 0 and s[i]:
            dp[i][j] = dp[i-1][j-1]

res = []
for i in dp:
    res.append(i[k])

print(max(res))