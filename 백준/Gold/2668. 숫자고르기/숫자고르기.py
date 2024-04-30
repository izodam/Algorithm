import sys
input = sys.stdin.readline

def dfs(x, i):
    visited[x] = 1
    now = nums[x]
    if visited[now] == 0:
        dfs(now, i)
    elif visited[now] and now == i:
        res.append(now)

n = int(input())
nums = [0] + [int(input()) for _ in range(n)]
res = []

for i in range(1, n+1):
    visited = [0] * (n+1)
    dfs(i, i)
print(len(res))
print('\n'.join(map(str, res)))