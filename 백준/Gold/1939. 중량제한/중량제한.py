import sys
input = sys.stdin.readline

# 이분탐색을 이용해서 최대 중량을 찾음
# 그래프 탐색을 이용해서 해당 최대 중량이 가능한지 탐색

from collections import deque

def bfs(weight):
    q = deque()
    visited = [0] * (n+1)

    q.append(factory[0])
    visited[factory[0]] = 1

    while q:
        node = q.popleft()
        if node == factory[1]:
            return True
        for next_node, next_weight in graph[node]:
            if next_weight >= weight and not visited[next_node]:
                q.append(next_node)
                visited[next_node] = 1
    return False


n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
max_weight = 0

for _ in range(m):
    a, b, c = map(int,input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    max_weight = max(max_weight, c)

factory = list(map(int,input().split()))

start = 1
end = max_weight

while start <= end:
    # 현재 최대 중량
    mid = (start + end) // 2

    if bfs(mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)