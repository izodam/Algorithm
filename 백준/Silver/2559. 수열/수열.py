n,k = map(int,input().split())
temperature = list(map(int,input().split()))

res = []
res.append(sum(temperature[:k]))

for i in range(n-k):
    res.append(res[i]-temperature[i]+temperature[k+i])

print(max(res))