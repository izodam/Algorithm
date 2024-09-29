import sys
input = sys.stdin.readline

def bimatch(n):
    if visited[n]:
        return False
    visited[n] = True

    for num in graph[n]:
        if seleted[num] == -1 or bimatch(seleted[num]):
            seleted[num] = n
            return True
    return False



n, m = map(int,input().split())
graph = []
for _ in range(n):
    s, *number = map(int,input().split())
    graph.append(number)

seleted = [-1] * (m+1)

for i in range(n):
    visited = [False] * n
    bimatch(i)

print(sum([1 for i in seleted if i >= 0]))