# 28279번
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    rec = list(map(int,input().split()))
    if rec[0] == 1:
        q.appendleft(rec[1])
    elif rec[0] == 2:
        q.append(rec[1])
    elif rec[0] == 3:
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif rec[0] == 4:
        if len(q):
            print(q.pop())
        else:
            print(-1)
    elif rec[0] == 5:
        print(len(q))
    elif rec[0] == 6:
        if len(q):
            print(0)
        else:
            print(1)
    elif rec[0] == 7:
        if len(q):
            print(q[0])
        else:
            print(-1)
    else:
        if len(q):
            print(q[-1])
        else:
            print(-1)