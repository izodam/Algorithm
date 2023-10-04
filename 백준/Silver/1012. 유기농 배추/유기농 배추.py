from collections import deque
t = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

def BFS(x,y):
    # 방문처리
    q.append((x,y))
    graph[x][y] = 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if graph[nx][ny] == 1:
                q.append((nx,ny))
                graph[nx][ny] = 0


for i in range(t):
    m,n,k = map(int,input().split())
    graph = [[0]*n for _ in range(m)]
    cnt = 0

    for j in range(k):
        x,y = map(int,input().split())
        graph[x][y] = 1

    for a in range(m):
        for b in range(n):
            if graph[a][b] == 1:
                BFS(a,b)
                cnt += 1
    print(cnt)