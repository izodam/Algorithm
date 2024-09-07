import sys
input = sys.stdin.readline


from collections import deque

def bfs():
    q = deque()
    q.append((a, 1))

    visited = set()
    visited.add(a)

    while q:
        x, cnt = q.popleft()

        # 2 곱하기
        nx = x * 2
        if nx == b:
            return cnt
        if nx < b and  nx not in visited:
            visited.add(nx)
            q.append((nx, cnt+1))

        # 1 추가하기
        nx = int(str(x) + '1')
        if nx == b:
            return cnt
        if nx < b and nx not in visited:
            visited.add(nx)
            q.append((nx, cnt+1))

    return -1


a, b= map(int,input().split())

res = bfs()

if res == -1:
    print(-1)
else:
    print(res+1)