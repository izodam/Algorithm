import sys
input = sys.stdin.readline
import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = []
    heapq.heappush(q, (board[0][0], 0, 0))
    while q:
        cost, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            return cost
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                now = cost + board[nx][ny]
                if now < distance[nx][ny]:
                    heapq.heappush(q, (now, nx, ny))
                    distance[nx][ny] = now



tc = 1
while True:
    n = int(input())
    if n == 0:
        exit()

    board = [list(map(int, input().split())) for _ in range(n)]
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]

    print(f'Problem {tc}: {bfs()}')
    tc += 1