import sys
input = sys.stdin.readline
# 가장 먼 사람의 거리가 점수
# 모든 노드에서 모든 노드까지의 거리가 필요 -> 플로이드-워셜

n = int(input())
INF = float('inf')
graph = [[INF] * (n+1) for _ in range(n+1)]


while True:
  a, b = map(int,input().split())
  if a == -1 and b == -1:
    break
  graph[a][b] = 1
  graph[b][a] = 1


for k in range(1, n+1):
  graph[k][k] = 0
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


score = [0] * (n+1)
res = INF
res_number = []
for i in range(1, n+1):
  score[i] = max([x for x in graph[i] if x != INF])
  if score[i] < res:
    res = score[i]
    res_number = [i]
  elif score[i] == res:
    res_number.append(i)

res_number.sort()
print(res, len(res_number))
print(' '.join(map(str, res_number)))