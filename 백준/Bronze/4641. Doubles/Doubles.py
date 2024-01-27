while True:
    lst = list(map(int,input().split()))
    if lst[0] == -1 and len(lst) == 1:
        break
    cnt = 0
    lst.pop()
    for i in lst:
        if i*2 in lst:
            cnt += 1
    print(cnt)