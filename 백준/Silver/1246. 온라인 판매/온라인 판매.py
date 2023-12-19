# 1246번
n,m = map(int,input().split())
pi = [int(input()) for _ in range(m)]
pi.sort()
res = 0
cost = 0
for i in range(m):
    egg = min(m-i,n)
    if res < pi[i] * egg:
        res = pi[i]*egg
        cost = pi[i]
print(cost,res)
