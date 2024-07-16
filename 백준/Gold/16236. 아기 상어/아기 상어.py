import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    visited = [[0] * n for _ in range(n)]
    visited[x][y] = 1

    now_move_res = [x, y, float('inf'), 0]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                # 상어랑 사이즈 같으면 밝고 지나갈 수 있음
                if board[nx][ny] == size:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                # 물고기 없으면 그냥 지나감
                elif board[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                # 먹을 수 있는 경우
                elif board[nx][ny] < size:
                    # 더 가까운 경우
                    if visited[x][y] < now_move_res[2]:
                        board[now_move_res[0]][now_move_res[1]] = now_move_res[3]
                        now_move_res = [nx, ny, visited[x][y], board[nx][ny]]
                        board[nx][ny] = 0
                    # 가까운 정도가 같은 경우
                    elif visited[x][y] == now_move_res[2]:
                        # 가장 위에 있는 것 선택
                        if nx < now_move_res[0]:
                            board[now_move_res[0]][now_move_res[1]] = now_move_res[3]
                            now_move_res = [nx, ny, visited[x][y], board[nx][ny]]
                            board[nx][ny] = 0
                        # 같은 높이라면, 가장 왼쪽에 있는 것 선택
                        elif nx == now_move_res[0] and ny < now_move_res[1]:
                            board[now_move_res[0]][now_move_res[1]] = now_move_res[3]
                            now_move_res = [nx, ny, visited[x][y], board[nx][ny]]
                            board[nx][ny] = 0

    return now_move_res


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

res = 0
size = 2
eat_fish = 0

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = [i, j]

while True:
    x, y, cnt, eat_size = bfs(shark[0], shark[1])
    if cnt != float('inf'):
        eat_fish += 1
        shark = [x, y]
        res += cnt
        if eat_fish == size:
            size += 1
            eat_fish = 0

    else:
        break
print(res)