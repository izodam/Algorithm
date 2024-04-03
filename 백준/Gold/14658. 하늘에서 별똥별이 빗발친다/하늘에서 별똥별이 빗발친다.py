n, m, l, k = map(int,input().split())
star = []
res = 0
for _ in range(k):
    x, y = map(int,input().split())
    star.append((x, y))


for sx, sy in star:
    for ex, ey in star:
        cnt = 0
        for s in star:
            if sx <= s[0] <= sx+l and ey <= s[1] <= ey+l:
                cnt += 1
        res = max(res, cnt)

print(k-res)