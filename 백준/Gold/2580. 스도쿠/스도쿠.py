import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

# 가로 확인
def row(target, n):
    for i in range(9):
        if sudo[n][i] == target:
            return False
    return True

# 세로 확인
def col(target, n):
    for i in range(9):
        if target == sudo[i][n]:
            return False
    return True

# 사각형 확인
def square(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == sudo[x//3 * 3 + i][y//3 * 3 + j]:
                return False
    return True


def dfs(depth):
    if depth == len(blank):
        for x in range(9):
            print(' '.join(map(str, sudo[x])))
        exit()
    x,y = blank[depth]
    for i in range(1, 10):
        if row(i, x) and col(i, y) and square(x, y, i):
            sudo[x][y] = i
            dfs(depth + 1)
            sudo[x][y] = 0



sudo = [list(map(int,input().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudo[i][j] == 0:
            blank.append((i, j))

dfs(0)