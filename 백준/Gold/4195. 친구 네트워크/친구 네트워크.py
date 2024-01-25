# 4195번
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    x = find(a)
    y = find(b)

    if x != y:
        parent[y] = x
        number[x] += number[y]
    print(number[x])


t = int(input())

for _ in range(t):
    f = int(input())
    parent = {}
    number = {}

    for i in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        union(a,b)