# 1202번
import heapq
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
# [보석무게, 가격]
jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int,input().split())))
bag = [int(input()) for _ in range(K)]
bag.sort()

res = 0
temp = []
for i in bag:
    while jew and i >= jew[0][0]:
        # 최대힙
        heapq.heappush(temp, -heapq.heappop(jew)[1])
    if temp:
        res -= heapq.heappop(temp)
print(res)