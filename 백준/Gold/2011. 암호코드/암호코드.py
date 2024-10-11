n = list(map(int, input()))
n_len = len(n)
if n[0] == 0:
    print(0)
    exit()
dp = [0] * (n_len+1)
dp[0] = 1
dp[1] = 1

for i in range(1, n_len):
    if n[i] > 0:
        dp[i+1] += dp[i]
    if 10 <= n[i] + n[i-1] * 10 <= 26:
        dp[i+1] += dp[i-1]
print(dp[n_len] % 1000000)