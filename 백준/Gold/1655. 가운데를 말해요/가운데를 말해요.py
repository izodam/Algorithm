# 1655. 가운데를 말해요
import heapq
import sys
input = sys.stdin.readline

n = int(input())
# 최대 힙
left = []
# 최소 힙
right = []

for i in range(1, n+1):
    now = int(input())

    if len(left) == len(right):
        heapq.heappush(left, -now)
    else:
        heapq.heappush(right, now)

    if right and (-1 * left[0]) > right[0]:
        l = heapq.heappop(left)
        r = heapq.heappop(right)

        heapq.heappush(right, -l)
        heapq.heappush(left, -r)
    print(left[0] * -1)