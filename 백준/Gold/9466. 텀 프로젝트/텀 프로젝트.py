import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
def dfs(student):
    global has_team

    visited[student] = 1
    team.append(student)
    next = select[student]

    if visited[next]:
        if next in team:
            has_team += len(team[team.index(next):])
    else:
        dfs(next)



T = int(input())
for tc in range(T):
    n = int(input())
    select = [0] + list(map(int,input().split()))
    has_team = 0
    visited = [0] * (n+1)

    for i in range(1, n+1):
        if not visited[i]:
            team = []
            dfs(i)
    print(n-has_team)