import sys
input = sys.stdin.readline

n, h = map(int,input().split())
imos = [0] * (h+1)

for i in range(n):
    a = int(input())
    # 짝수는 석순
    if i % 2 == 0:
        imos[0] += 1
        imos[a] -= 1
    # 홀수는 종유석
    else:
        imos[h-a] += 1
        imos[h] -= 1

now = 0
for i in range(h):
    now += imos[i]
    imos[i] = now

res = min(imos[:-1])
print(res, imos[:-1].count(res))