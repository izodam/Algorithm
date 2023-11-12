from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v+1)]

for _ in range(v):
    info = list(map(int,input().split()))
    for i in range(1,len(info)-2,2):
        graph[info[0]].append((info[i],info[i+1]))

def bfs(s):
    q = deque()
    q.append(s)
    visited = [-1]*(v+1)

    # 방문처리
    visited[s] = 0
    res = [0,0]     # s로부터 가장 먼 거리에 있는 거리와 해당 노드

    while q:
        n = q.popleft()
        for node,length in graph[n]:
            if visited[node] == -1:
                visited[node] = visited[n]+length
                q.append(node)
                if res[0] < visited[node]:
                    res = visited[node], node
    return res

length,node = bfs(1)
length,node = bfs(node)
print(length)