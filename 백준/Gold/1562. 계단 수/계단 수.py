import sys
input = sys.stdin.readline

n = int(input())

bit_range = 1 << 10
# dp[자리 수][마지막 숫자][사용된 숫자들의 비트 값]
# 만약 숫자 num을 사용했다면 1 << num가 추가
dp = [[[0] * bit_range for _ in range(10)] for _ in range(n+1)]
MOD = 1000000000

# 한자리수는 모두 1
for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(1, n):
    for j in range(10):
        for b in range(bit_range):
            if 0 <= j < 9:
                now = b | 1 << (j+1)
                dp[i+1][j+1][now] += dp[i][j][b]
                dp[i + 1][j + 1][now] %= MOD

            if 0 < j <= 9:
                now = b | 1 << (j-1)
                dp[i+1][j-1][now] += dp[i][j][b]
                dp[i+1][j-1][now] %= MOD

res = 0
for k in range(1,10):
    res += dp[n][k][0b1111111111]

print(res % MOD)