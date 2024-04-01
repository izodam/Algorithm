n=int(input())
dp=[0]*(n+2)
dp[0]=0 #n==0
dp[1]=0 #n==1
dp[2]=1 #n==2

def cul(a):
    if dp[a]==0:
        if a%2==0 and a%3==0:
            dp[a]=min(dp[a//3]+1,dp[a-1]+1,dp[a//2]+1)
        elif a%3==0:
            dp[a]=min(dp[a//3]+1,dp[a-1]+1)
        elif a%2==0:
            dp[a]=min(dp[a//2]+1,dp[a-1]+1)
        else:
            dp[a]=dp[a-1]+1

for i in range(3,n+1):
    cul(i)

print(dp[n])




