import sys
input = sys.stdin.readline

m, n = map(int,input().split())
grow = [list(map(int,input().split())) for _ in range(n)]

grow_number = [1] * (2 * m - 1)

for day in range(n):
    for idx in range(grow[day][0],  grow[day][0] + grow[day][1]):
        grow_number[idx] += 1
    for idx in range(grow[day][0] + grow[day][1], 2 * m - 1):
        grow_number[idx] += 2

for idx in range(m-1, -1, -1):
    print(*([grow_number[idx]]+grow_number[m:]))