import sys
input = sys.stdin.readline
# 키가 몇 번째인지 알 수 있는 학생 == 자신보다 큰 사람 + 작은 사람 = N-1
# 플로이드-워셜을 사용해야 하는 이유
# 모든 노드에서 모든 노드로 가는 경로를 확인해야함!

INF = int(1e9)
n, m = map(int,input().split())
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

cnt = 0
for student in range(1, n+1):
    if sum(graph[student]) + sum(row[student] for row in graph) == n-1:
        cnt += 1
print(cnt)