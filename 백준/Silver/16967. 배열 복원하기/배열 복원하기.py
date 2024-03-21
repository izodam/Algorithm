h, w, x, y = map(int,input().split())
b = [list(map(int,input().split())) for _ in range(h+x)]

res = [b[i][:w] for i in range(h)]

for i in range(h):
    for j in range(w):
        if i + x < h and j + y < w:
            res[i+x][j+y] -= res[i][j]

for i in res:
    print(' '.join(map(str,i)))