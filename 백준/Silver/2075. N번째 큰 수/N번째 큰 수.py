import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []

nums = list(map(int,input().split()))
for i in nums:
    heapq.heappush(q, i)


for i in range(n-1):
    nums = list(map(int, input().split()))
    for i in nums:
        if i > q[0]:
            heapq.heappop(q)
            heapq.heappush(q, i)


print(heapq.heappop(q))