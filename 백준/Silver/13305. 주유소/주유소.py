# 13305번
n = int(input())
km = list(map(int,input().split()))
cost = list(map(int,input().split()))

res = 0
min_oil = cost[0]
for i in range(n-1):
    if cost[i] < min_oil:
        min_oil = cost[i]
    res += min_oil * km[i]
print(res)