import sys
input = sys.stdin.readline

import heapq

n = int(input())
problems = [list(map(int, input().split())) for _ in range(n)]

problems.sort()

queue = []

for i in problems:
    heapq.heappush(queue, i[1])
    if i[0] < len(queue):
        heapq.heappop(queue)
print(sum(queue))