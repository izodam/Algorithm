# 비용이 큰 순으로 연결했을 때, u,v가 같은 집합이 되면
# 그 전까지 연결된 비용을 제외한 나머지 비용들이 Cost(u, v)
import sys
input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parents[b] = a
        child[a] += child[b]
    else:
        parents[a] = b
        child[b] += child[a]

def find_child(x):
    if parents[x] != x:
        return find_child(parents[x])
    else:
        return child[x]


n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
# 가중치가 큰 순서대로 정렬
graph.sort(key=lambda x: x[2], reverse=True)
parents = [i for i in range(n+1)]
# 자식 개수
child = [1] * (n+1)
total = sum([item[2] for item in graph])

res = 0
current = 0

for x, y, w in graph:
    if find(x) != find(y):
        res += find_child(x) * find_child(y) * (total - current)
        union(x, y)
    current += w

res %= 10 ** 9
print(res)