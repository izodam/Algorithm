# 1916번
import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))

start, end = map(int,input().split())
INF = 10e8
res = [INF] * (n+1)

def dij(s):
    q = []
    heapq.heappush(q,(0,s))
    res[s] = 0

    while q:
        cost, now = heapq.heappop(q)

        if res[now] < cost:
            continue
        for i in graph[now]:
            if i[1] + cost < res[i[0]]:
                res[i[0]] = i[1] + cost
                heapq.heappush(q,(i[1] + cost,i[0]))

dij(start)
print(res[end])