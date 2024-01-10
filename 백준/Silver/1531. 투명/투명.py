# 1531번
n,m = map(int,input().split())
pic = {}
for _ in range(n):
    lx, ly, rx, ry = map(int,input().split())
    for i in range(lx, rx+1):
        for j in range(ly, ry+1):
            paper = (i,j)
            if paper in pic.keys():
                pic[paper] += 1
            else:
                pic[paper] = 1

cnt = 0
for p in pic.values():
    if p > m:
        cnt += 1
print(cnt)