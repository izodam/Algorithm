import sys
input = sys.stdin.readline

n = int(input())
vill = [list(map(int,input().split())) for _ in range(n)]

res = float('inf')

for i in range(n):
    min1 = float('inf')
    min2 = float('inf')
    for j in range(n):
        if i != j:
            d1 = abs(vill[i][0] - vill[j][0]) + abs(vill[i][1] - vill[j][1]) + abs(vill[i][2] - vill[j][2])
            if min1 > d1:
                min2 = min1
                min1 = d1
            elif min2 > d1:
                min2 = d1
    res = min(min1+min2, res)

print(res)