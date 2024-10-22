import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())

graph_in = [[] for _ in range(n+1)]
graph_out = [[] for _ in range(n+1)]
node_cnt = [0] * (n+1)

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph_in[e].append((s, cost))
    graph_out[s].append((e, cost))
    node_cnt[e] += 1

start, end = map(int, input().split())


distance = [0] * (n+1)
q = deque()
q.append(start)


while q:
    node = q.popleft()
    for e, cost in graph_out[node]:
        node_cnt[e] -= 1
        distance[e] = max(distance[e], distance[node] + cost)

        if node_cnt[e] == 0:
            q.append(e)

visited = [0] * (n+1)
res = 0
q = deque()
q.append(end)

while q:
    node = q.popleft()

    for s, cost in graph_in[node]:
        if distance[s] + cost == distance[node]:
            res += 1

            if not visited[s]:
                visited[s] = 1
                q.append(s)
print(distance[end])
print(res)