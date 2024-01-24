import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [i for i in range(n+1)]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        graph[a] = b
    else:
        graph[b] = a

def find(x):
    if graph[x] != x:
        graph[x] = find(graph[x])
    return graph[x]




for i in range(m):
    x, a, b = list(map(int,input().split()))
    # x가 0이면
    if not x:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')