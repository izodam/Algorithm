n = int(input())
num = list(map(int,input().split()))
dp = [0]*n
for i in range(n):
    dp[i]=max(dp[i-1]+num[i],num[i])
print(max(dp))