# 11725번
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
res = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph,v,visited):
    q = deque()

    q.append(v)
    visited[v] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                res[i] = x
                q.append(i)
                visited[i] = True
bfs(graph,1,visited)

print('\n'.join(map(str,res[2::])))
