n, m = map(int,input().split())
n_cut = int(input())
# 가로로 자르기
r = [0,m]
# 세로로 자르기
c = [0,n]

for _ in range(n_cut):
    cutnum, index = map(int,input().split())
    if cutnum == 0:
        r.append(index)
    else:
        c.append(index)

r.sort()
c.sort()

pr = 0
cr = 0

for i in range(len(r)-1):
    pr = max(pr, r[i+1]-r[i])

for i in range(len(c)-1):
    cr = max(cr, c[i+1]-c[i])

print(pr*cr)