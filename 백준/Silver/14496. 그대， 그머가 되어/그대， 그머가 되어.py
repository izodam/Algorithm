import sys, collections
MAX = int(1e9)
a,b = map(int,sys.stdin.readline().split())
n,m = map(int,sys.stdin.readline().split())

board = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)

min_change_cnt = MAX
visited = [False]*(n+1)
visited[a] = True
q = collections.deque([(a,0)])
while q:
    cur,dist = q.popleft()
    if cur == b:
        min_change_cnt = min(min_change_cnt,dist)
    for next in board[cur]:
        if not visited[next]:
            visited[next] = True
            q.append((next,dist+1))

if min_change_cnt == MAX:
    min_change_cnt = -1
print(min_change_cnt)