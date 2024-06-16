# 14500 테트로미노
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, cnt, score):
    global res
    if score + max_score * (4 - cnt) <= res:
        return
    if cnt == 4:
        res = max(res, score)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            # ㅜ 모양 만들기
            # 현재 위치의 값을 더해주고 움직이기 전 위치를 다시 dfs 돌림
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x, y, cnt+1, score+board[nx][ny])
            visited[nx][ny] = 1
            dfs(nx, ny, cnt+1, score+board[nx][ny])
            visited[nx][ny] = 0



n, m = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

max_score = max(map(max, board))


res = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, 1, board[i][j])
        visited[i][j] = 0

print(res)