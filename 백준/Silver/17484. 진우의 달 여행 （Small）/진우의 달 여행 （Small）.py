n, m = map(int,input().split())
space = [list(map(int,input().split())) for _ in range(n)]
dp = [[[float('inf')] * 3 for _ in range(m)] for _ in range(n)]

for i in range(m):
    dp[0][i] = [space[0][i], space[0][i], space[0][i]]

for i in range(1, n):
    for j in range(m):
        for k in range(3):
            if (j==0 and k==2) or (j==m-1 and k==0):
                continue
            for l in range(3):
                if k == l:
                    continue
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-k+1][l] + space[i][j])

print(min(map(min, dp[-1])))