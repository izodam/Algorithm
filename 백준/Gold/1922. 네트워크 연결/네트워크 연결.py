import sys
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if b < a:
        parent[a] = b
    else:
        parent[b] = a


n = int(input())
m = int(input())

parent = [i for i in range(n + 1)]
arr =[]
res = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    arr.append((c, a, b))
arr.sort(key=lambda x: x[0])

for dis, a, b in arr:
    if find(a) != find(b):  # 루트가 같으면 할 필요가 없음
        union(a, b)
        res += dis
print(res)