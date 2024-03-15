import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int,input().split())
city = [list(map(int,input().split())) for _ in range(n)]
res = float('inf')
house = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i,j))
        elif city[i][j] == 2:
            chicken.append((i, j))


for arr in combinations(chicken, m):
    tmp = 0
    for h in house:
        cnt = float('inf')
        for j in range(m):
            cnt = min(cnt, abs(h[0] - arr[j][0]) + abs(h[1] - arr[j][1]))
        tmp += cnt
    res = min(res, tmp)

print(res)