n = int(input())
dp = [0] * (n+1)

# 제곱수는 1로
k = 1
while k ** 2 <= n:
    dp[k**2] = 1
    k += 1

for i in range(1, n+1):
    if dp[i] != 0:
        continue
    j = 1
    while j**2 <= i:
        if dp[i] == 0:
            dp[i] = dp[j**2] + dp[i-j**2]
        else:
            dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])
        j += 1
print(dp[n])