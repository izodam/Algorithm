import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
balls = []

for i in range(n):
    # 색, 크기
    c, s = map(int, input().split())
    balls.append([c, s, i])

balls.sort(key=lambda x: x[1])
res = defaultdict(int)
sum_ball = defaultdict(int)

total = 0
j = 0

for i in range(n):
    while balls[j][1] < balls[i][1]:
        total += balls[j][1]
        sum_ball[balls[j][0]] += balls[j][1]
        j += 1

    res[balls[i][2]] = total - sum_ball[balls[i][0]]

for i in range(n):
    print(res[i])