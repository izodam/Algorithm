# 2852번
n = int(input())

t1, t2 = 0, 0
w = 0
tmp1, tmp2 = 0, 0

for _ in range(n):
    team, time = input().split()

    m,s = map(int,time.split(':'))
    t = 60*m + s

    if team == '1':
        if w == 0:
            w += 1
            tmp1 = t
        else:
            w += 1
            if w == 0:
                t2 += (t - tmp2)
    else:
        if w == 0:
            w -= 1
            tmp2 = t
        else:
            w -= 1
            if w == 0:
                t1 += (t - tmp1)

if w > 0:
    t1 += 60*48 - tmp1
elif w < 0:
    t2 += 60*48 - tmp2
print('{:0>2}:{:0>2}'.format((t1)//60,t1%60))
print('{:0>2}:{:0>2}'.format((t2)//60,t2%60))