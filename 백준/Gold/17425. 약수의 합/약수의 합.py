# 17425번
t = int(input())
ns = [int(input()) for _ in range(t)]
n = max(ns)

lst = [0] * (n + 1)
res = [0] * (n + 1)
for i in range(1, n + 1):
    j = 1
    while i * j <= n:
        lst[i * j] += i
        j += 1
    res[i] = lst[i] + res[i - 1]

for i in ns:
    print(res[i])