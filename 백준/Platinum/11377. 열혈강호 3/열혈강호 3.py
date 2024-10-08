import sys
input = sys.stdin.readline

def bisearch(n):
    if visited[n]:
        return False
    visited[n] = True
    for num in graph[n]:
        if seleted[num] == -1 or bisearch(seleted[num]):
            seleted[num] = n
            return True
    return False

n, m, k = map(int,input().split())
graph = []
for _ in range(n):
    cnt, *arr = map(int,input().split())
    graph.append(arr)

cnt = 0
seleted = [-1] * (m+1)

for i in range(n):
    visited = [False for _ in range(n+1)]
    if bisearch(i):
        cnt += 1
for i in range(n):
    visited = [False for _ in range(n + 1)]
    if bisearch(i):
        cnt += 1
        k -= 1
        if k == 0:
            break
print(cnt)