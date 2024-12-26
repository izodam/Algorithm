import sys
input = sys.stdin.readline
import heapq
m, n = map(int,input().split())
# 0은 빈 방, 1은 벽
board = [list(map(int,input().strip())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = float('inf')

distance = [[INF] * m for _ in range(n)]

def dij():
    q = []
    heapq.heappush(q,(0, 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if cost > distance[x][y]:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                now = cost + board[nx][ny]
                if now < distance[nx][ny]:
                    distance[nx][ny] = now
                    heapq.heappush(q, (now, nx, ny))

dij()
print(distance[n-1][m-1])