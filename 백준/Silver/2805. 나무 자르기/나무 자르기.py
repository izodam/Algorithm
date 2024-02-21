# 2805
def cut(x):
    res = 0
    for i in tree:
        if i > x:
            res += (i - x)
    return res

n, m = map(int,input().split())
tree = list(map(int,input().split()))
s = 1
e = max(tree)

while s <= e:
    mid = (s + e) // 2
    cnt = cut(mid)
    if cnt >= m:
        s = mid + 1
    elif cnt < m:
        e = mid - 1
print(e)