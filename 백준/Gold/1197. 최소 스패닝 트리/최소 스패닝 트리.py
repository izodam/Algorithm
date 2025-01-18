import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int,input().split())
edges = []
for _ in range(E):
    a, b, c= map(int,input().split())
    edges.append((a, b, c))

# 가중치 기준으로 정렬
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V+1)]

res = 0
for a, b, cost in edges:
    if find(a) != find(b):
        res += cost
        union(a, b)
print(res)