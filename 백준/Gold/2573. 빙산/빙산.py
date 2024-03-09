from collections import deque
delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] != 0:
                q.append((nx, ny))
                visited[nx][ny] = 1



def melt():
    res = 1
    while max(map(max, board)) != 0:
        # 녹임
        tmp = [i.copy() for i in board]
        # print(tmp)
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    for move in range(4):
                        if tmp[i+delta[move][0]][j+delta[move][1]] == 0 and board[i][j] > 0:
                            board[i][j] -= 1
        # print('\n'.join(map(str,board)))
        area = 0
        visited = [[0]*m for _ in range(n)]
        # 덩어리 개수 셈
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and board[i][j] != 0:
                    bfs(i, j, visited)
                    area += 1
        if area >= 2:
            return res
        res += 1
    else:
        return 0


n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
print(melt())