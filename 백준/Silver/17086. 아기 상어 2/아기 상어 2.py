from collections import  deque
delta = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j]:
            q.append((i, j))
bfs()

print(max(map(max, board)) - 1)