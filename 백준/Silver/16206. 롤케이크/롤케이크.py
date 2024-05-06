n, m = map(int,input().split())
roll = list(map(int,input().split()))
roll.sort(key=lambda x:(x%10,x))
res = 0

for cake in roll:
    cnt = cake // 10
    if cake % 10 == 0:
        if m >= cnt-1:
            res += cnt
            m -= (cnt - 1)
        else:
            res += m
            m -= m
            break
    else:
        if m >= cnt:
            res += cnt
            m -= cnt
        else:
            res += m
            m -= m
            break
print(res)