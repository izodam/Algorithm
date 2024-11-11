import sys
input = sys.stdin.readline

from collections import deque

n = int(input())
graph = [[] for _ in range(n+1)]
build_time = [0]
indegree = [0] * (n + 1)
in_graph = [[]]

for i in range(1, n+1):
    time, *first, last = list(map(int, input().split()))
    build_time.append(time)
    indegree[i] = len(first)
    for node in first:
        graph[node].append(i)
    in_graph.append(first)
q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now_node = q.popleft()

    for next_node in graph[now_node]:
        indegree[next_node] -= 1

        if indegree[next_node] == 0:
            max_time = 0
            for node in in_graph[next_node]:
                max_time = max(max_time, build_time[node])
            build_time[next_node] += max_time
            q.append(next_node)
print('\n'.join(map(str, build_time[1:])))