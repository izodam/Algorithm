import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
node_cnt = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    node_cnt[b] += 1


q = deque()
res = []

for i in range(1, n+1):
    if node_cnt[i] == 0:
        q.append(i)

while q:
    node = q.popleft()
    res.append(node)
    for next_node in graph[node]:
        node_cnt[next_node] -= 1

        if node_cnt[next_node] == 0:
            q.append(next_node)

print(*res)