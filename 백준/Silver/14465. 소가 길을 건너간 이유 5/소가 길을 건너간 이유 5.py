import sys
input = sys.stdin.readline

n, k, b = map(int,input().split())
light = [i for i in range(1, n+1)]

for i in range(b):
    light[int(input()) - 1] = -1


res = 0

for i in range(k):
    if light[i] == -1:
        res += 1

cnt = res
for i in range(1, n-k+1):
    if light[i-1] == -1:
        cnt -= 1
    if light[i+k-1] == -1:
        cnt += 1

    res = min(res, cnt)
print(res)