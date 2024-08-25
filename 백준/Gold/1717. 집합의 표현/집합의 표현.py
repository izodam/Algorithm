import sys
input = sys.stdin.readline
n, m = map(int,input().split())
graph = [i for i in range(n+1)]

# 포함 확인
def find(x):
    # 최상단 root 노드 찾기
    if graph[x] != x:
        graph[x] = find(graph[x])
    return graph[x]


# 합치기
def union(a, b):
    a = find(a)
    b = find(b)

    # 더 높은 인덱스를 가진 쪽이 작은 쪽을 흡수
    if a < b:
        graph[a] = b
    else:
        graph[b] = a

for i in range(m):
    x, a, b = map(int,input().split())
    if x == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b)