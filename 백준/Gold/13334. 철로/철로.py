import sys
input = sys.stdin.readline

import heapq

n = int(input())
arr = []

for _ in range(n):
    h, o = map(int,input().split())
    arr.append((min(h, o), max(h, o)))

d = int(input())

arr.sort(key=lambda x: (x[1], x[0]))

q = []
res = 0

for h, o in arr:
    heapq.heappush(q, h)
    # 끝 지점 기준으로 철로 시작지점 정하기
    start = o - d
    # 철로의 시작 지점보다 해당 위치의 시작점이 작다면 고려하지 않음 -> pop
    while q and q[0] < start:
        heapq.heappop(q)
    res = max(res, len(q))
print(res)
