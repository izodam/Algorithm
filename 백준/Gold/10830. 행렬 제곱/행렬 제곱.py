import sys
input = sys.stdin.readline

# 10830번
n, b = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

def multi(mat1, mat2):
    res = []
    for i in range(n):      # 첫번째 행렬의 행 탐색
        y = []
        for j in range(n):  # 두번째 행렬의 열 탐색
            x = 0
            for l in range(n):
                x += mat1[i][l] * mat2[l][j] % 1000
            y.append(x)
        res.append(y)
    return res

def power(a, b):
    if b == 1:
        return a
    tmp = power(a, b//2)
    if b % 2 == 0:
        return multi(tmp, tmp)
    else:
        return multi(multi(tmp,tmp),a)

res = power(matrix, b)

for i in range(n):
    for j in range(n):
        print(res[i][j]%1000,end=' ')
    print()

