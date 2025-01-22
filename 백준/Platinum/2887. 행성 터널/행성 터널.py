import sys
input = sys.stdin.readline
# 질문게시판 참조)
# 간선의 길이가 min(|x|, |y|, |z|)이기 때문에
# 간선들을 |x|가 작은 순으로 정렬했을 때
# 순위가 N등 이하인 간선은 최소신장트리를 만들 때 사용될 가능성이 없어서 제외시킬 수 있습니다.
import heapq

n = int(input())
location = [list(map(int,input().split())) + [i] for i in range(n)]

location_x = sorted(location, key=lambda x:x[0])
location_y = sorted(location, key=lambda x:x[1])
location_z = sorted(location, key=lambda x:x[2])


graph = [[] for _ in range(n)]
for i in range(n-1):
    x1, y1, z1, i1 = location_x[i]
    x2, y2, z2, i2 = location_x[i+1]
    cost = min(abs(x1-x2), abs(y2-y1), abs(z2-z1))
    graph[i1].append((i2, cost))
    graph[i2].append((i1, cost))

    x1, y1, z1, i1 = location_y[i]
    x2, y2, z2, i2 = location_y[i + 1]
    cost = min(abs(x1 - x2), abs(y2 - y1), abs(z2 - z1))
    graph[i1].append((i2, cost))
    graph[i2].append((i1, cost))

    x1, y1, z1, i1 = location_z[i]
    x2, y2, z2, i2 = location_z[i + 1]
    cost = min(abs(x1 - x2), abs(y2 - y1), abs(z2 - z1))
    graph[i1].append((i2, cost))
    graph[i2].append((i1, cost))


q = [(0, 0)]
visited = [0] * n

res = 0
while q:
    cost, node = heapq.heappop(q)
    if visited[node]:
        continue

    res += cost
    visited[node] = 1

    for next_node, next_cost in graph[node]:
        if not visited[next_node]:
            heapq.heappush(q, (next_cost, next_node))

print(res)