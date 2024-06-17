# 14719 빗물

h, w = map(int,input().split())
building = list(map(int,input().split()))
res = 0

for i in range(1, w-1):
    left = max(building[:i])
    right = max(building[i+1:])

    if building[i] == min(left, right, building[i]):
        res += min(left, right) - building[i]

print(res)