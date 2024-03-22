import sys
input = sys.stdin.readline
from heapq import heappush, heappop

n = int(input())
min_h = []
max_h = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(min_h, x)
    elif x < 0:
        heappush(max_h, -x)
    else:
        if min_h and max_h:
            if min_h[0] < max_h[0]:
                print(heappop(min_h))
            else:
                print(-heappop(max_h))
        elif min_h:
            print(heappop(min_h))
        elif max_h:
            print(-heappop(max_h))
        else:
            print(0)