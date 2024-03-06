def dfs(s, x):
    if x == 6:
        print(' '.join(map(str, res)))
        return
    for i in range(s, k):
        res.append(num[i])
        dfs(i+1, x+1)
        res.pop()


while True:
    k, *num = map(int,input().split())
    if k == 0:
        break

    res = []
    dfs(0,0)
    print()