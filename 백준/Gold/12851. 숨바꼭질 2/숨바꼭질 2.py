import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    res = 0
    cnt = 0
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        tmp = visited[x]
        # 둘이 만남
        if x == k:
            res = tmp
            cnt += 1
            continue
        for i in [x-1, x+1, x*2]:
            if 0 <= i < 100001 and (visited[i] == 0 or visited[i] == visited[x] + 1):
                visited[i] = visited[x] + 1
                q.append(i)
    return res, cnt

n, k = map(int,input().split())
visited = [0] * 100001



# print(bfs())
print('\n'.join(map(str, bfs())))