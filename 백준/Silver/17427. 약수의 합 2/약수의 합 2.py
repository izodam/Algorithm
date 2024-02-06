# 17427번
N = int(input())
lst = [1] * (N+1)
lst[0] = 0
for i in range(1, N+1):
    if lst[i]:
        for j in range(i+i, N+1, i):
            lst[i] += 1

res = 0
for i in range(1, N+1):
    res += i * lst[i]
print(res)