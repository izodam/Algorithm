import sys
input = sys.stdin.readline

t = int(input())

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a,b):
    a = find(a)
    b = find(b)

    # a와 b의 부모가 같지 않으면 a에 b 연결!
    if a != b:
        parent[b] = a
        number[a] += number[b]

    print(number[a])



for _ in range(t):
    f = int(input())
    # 해당 key의 부모를 value로 넣어주는 dict
    parent = {}
    # 해당 키와 연결되어 있는 친구 네트워크 수를 저장해주는 dict
    number = {}

    for i in range(f):
        a, b = input().split()
        # 만약 parent에 a 키값이 없으면
        if a not in parent:
            parent[a] = a
            number[a] = 1
        if b not in parent:
            parent[b] = b
            number[b] = 1

        # 친구 연결이므로 union-find 알고리즘 사용
        union(a,b)