import sys
input = sys.stdin.readline
# 최소 스패닝 트리 선택
# 그 후 스패닝 트리에서 가장 간선이 큰 하나 제거 -> 두개의 그룹으로 나뉨
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


n, m = map(int,input().split())
edges = []

for _ in range(m):
    a, b, c = map(int,input().split())
    edges.append((a, b, c))

# 가중치 기준으로 정렬
edges.sort(key=lambda x:x[2])

parent = [i for i in range(n+1)]

spanning_tree = []

for a, b, cost in edges:
    if len(spanning_tree) == n-1:
        break
    if find(a) != find(b):
        spanning_tree.append(cost)
        union(a, b)

print(sum(spanning_tree[:-1]))