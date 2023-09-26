from collections import deque

def dfs(v):
    #현재 노드 방문 처리
    visited1[v]=True
    print(v,end=' ')
    for i in range(1,n+1):
        if not visited1[i] and graph[v][i]==1:
            dfs(i)

def bfs(v):
    queue = deque([v])
    visited2[v] = True
    while queue:
        v=queue.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if not visited2[i] and graph[v][i]==1:
                queue.append(i)
                visited2[i] = True


n,m,v=map(int,input().split())
graph=[[0]*(n+1) for _ in range(n+1)]
visited1=[0]*(n+1)  #dfs
visited2=[0]*(n+1)  #bfs

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=graph[b][a]=1
dfs(v)
print()
bfs(v)