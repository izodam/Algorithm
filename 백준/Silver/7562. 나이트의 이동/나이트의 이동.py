from collections import deque
t = int(input())
for _ in range(t):
    i = int(input())
    now = list(map(int,input().split()))
    move = list(map(int,input().split()))

    # 나이트가 이동할 수 있는 칸
    dx = [1, 2, 1, 2, -1, -2, -1, -2]
    dy = [2, 1, -2, -1, 2, 1, -2, -1]

    q = deque()
    q.append((now[0],now[1]))
    visited = [[0]*i for j in range(i)]
    while q:
        x, y = q.popleft()
        if x == move[0] and y == move[1]:
            print(visited[x][y])
            break
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]
            if 0<=nx<i and 0<=ny<i and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
