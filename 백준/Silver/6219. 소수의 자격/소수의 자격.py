a, b, d = map(int,input().split())

prims = [0] * (b+1)

for i in range(2, int(b**0.5)+1):
    if not prims[i]:
        for j in range(i+i, b+1, i):
            prims[j] = 1

res = [i for i in range(a, b+1) if not prims[i]]
cnt = 0

for i in res:
    if str(d) in str(i):
        cnt += 1
print(cnt)