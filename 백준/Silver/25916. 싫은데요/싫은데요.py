n, m = map(int,input().split())
holes = list(map(int,input().split()))

if n == 1:
    if holes[0] > m:
        print(0)
    else:
        print(holes[0])

else:
    tmp = holes[0]
    l = 0
    r = 1
    res = 0

    while l <= r and r < n:
        if holes[r] <= m - tmp:
            tmp += holes[r]
            r += 1
        else:
            if l == r:
                l += 1
                r += 1
                tmp = 0
                continue
            tmp -= holes[l]
            l += 1
        res = max(res, tmp)
    print(res)