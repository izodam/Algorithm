import sys
input = sys.stdin.readline
import heapq as hq

n = int(input())
arr= []
for i in range(n):
    x = int(input())
    if x:
        hq.heappush(arr, (-x,x))
    else:
        if len(arr) >= 1:
            print(hq.heappop(arr)[1])
        else:
            print(0)