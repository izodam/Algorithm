import sys
input = sys.stdin.readline

from bisect import bisect_right

def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    if y >= m:
        return
    x = find(x)
    y = find(y)
    parents[x] = y

n, m, k = map(int, input().split())
cards = sorted(list(map(int, input().split())))
su = list(map(int, input().split()))

parents = [i for i in range(m)]

for su_card in su:
    idx = bisect_right(cards, su_card)
    idx = find(idx)
    print(cards[idx])
    union(idx, idx+1)
