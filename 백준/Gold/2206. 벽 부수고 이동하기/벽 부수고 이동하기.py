from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    # x, y, 벽 방문 여부 확인
    q.append([0,0,0])
    visited1[0][0] = 1

    while q:
        x, y, wall = q.popleft()

        # 도착
        if x == n-1 and y == m-1:
            if wall == 0:
                return visited1[x][y]
            else:
                return visited2[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                # 벽 부수기
                if board[nx][ny] == 1 and wall == 0:
                    visited2[nx][ny] = visited1[x][y] + 1
                    q.append([nx,ny,1])
                if board[nx][ny] == 0:
                    if wall == 0 and visited1[nx][ny] == 0:
                        visited1[nx][ny] = visited1[x][y] + 1
                        q.append([nx,ny,wall])
                    elif wall == 1 and visited2[nx][ny] == 0 and visited1[nx][ny] == 0:
                        visited2[nx][ny] = visited2[x][y] + 1
                        q.append([nx,ny,wall])
    return -1



n, m = map(int,input().split())
# 0은 이동할 수 있는 곳을 나타내고, 1은 이동할 수 없는 벽
board = [list(map(int,input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

# 벽 뚫지 않았을 때 방문 확인용
visited1 = [[0]*m for _ in range(n)]
# 벽 뚫고 난 후 방문 확인용
visited2 = [[0]*m for _ in range(n)]

print(bfs())
