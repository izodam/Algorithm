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


t = int(input())

for tc in range(t):
    # m명에게 n개의 책 배부
    n, m = map(int,input().split())
    graph = []
    for _ in range(m):
        a, b = map(int,input().split())
        graph.append([i for i in range(a, b+1)])
    # 왼쪽이 사람, 오른쪽이 책번호
    selected = [-1] * (n + 1)

    for i in range(m):
        visited = [False] * m
        bimatch(i)

    res = 0
    for i in selected:
        if i != -1:
            res += 1
    print(res)