def findLCS():
    i, j = n, m
    res = ''
    while i > 0 and j > 0:
        if lcs[i][j] == 1:
            res += x[i]
            i, j = i-1, j-1
        elif lcs[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return res[::-1]


x = ' ' + input().strip()
y = ' ' + input().strip()

n, m = len(x)-1, len(y)-1
dp = [[0]*(m+1) for _ in range(n+1)]
lcs = [[''] * (m+1) for _ in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        if x[i] == y[j]:
            dp[i][j] = dp[i-1][j-1] + 1
            lcs[i][j] = 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            lcs[i][j] = 2 if dp[i-1][j] > dp[i][j-1] else 3
print(dp[n][m])
print(findLCS())