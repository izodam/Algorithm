import sys
input = sys.stdin.readline
# A는 태균 * 2 / 상대 + 3
# B는 태균 + 1
from collections import deque

def bfs():
    q = deque()

    q.append((s, t, 0))

    while q:
        now, other, cnt = q.popleft()
        if now == other:
            return cnt

        if now <= other:
            q.append((now * 2, other + 3, cnt + 1))
            q.append((now + 1, other, cnt + 1))


c = int(input())

for tc in range(c):
    s, t = map(int,input().split())
    print(bfs())