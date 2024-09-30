import sys
input = sys.stdin.readline

def bimatch(n):
    if visited[n]:
        return False
    visited[n] = True

    for num in graph[n]:
        if selected[num] == -1 or bimatch(selected[num]):
            selected[num] = n
            return True
    return False



n, m = map(int, input().split())
graph = []
for _ in range(n):
    cnt, *arr = map(int, input().split())
    graph.append(arr)

selected = [-1] * (m+1)

for i in range(n):
    visited = [False] * n
    bimatch(i)

print(sum([1 for i in selected if i >= 0]))