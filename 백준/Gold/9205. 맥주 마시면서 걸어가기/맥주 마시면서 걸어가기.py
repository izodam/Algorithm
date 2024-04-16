import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque()
    q.append((home[0], home[1]))

    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new = store[i]
                if abs(x - new[0]) + abs(y - new[1]) <= 1000:
                    visited[i] = 1
                    q.append((new[0], new[1]))
    print("sad")
    return


t = int(input())

for tc in range(t):
    n = int(input())
    home = list(map(int,input().split()))
    store = [list(map(int,input().split())) for _ in range(n)]
    festival = list(map(int,input().split()))

    visited = [0] * (n+1)
    bfs()