from collections import deque
import sys
input = sys.stdin.readline

# 봄
# 나이만큼 양분먹고 나이 + 1
# 하나의 칸에 여러 나무가 있다면 나이가 어린 나무부터 양분 먹음
# 나이만큼 양분 먹지 못하면 즉시 죽음

# 여름
# 봄에 죽은 나무가 나이/2만큼 양분으로 바뀜
# 소수점 아래 버림
def spring_and_summer():
    for i in range(n):
        for j in range(n):
            tree_num = len(tree[i][j])
            for k in range(tree_num):
                if nutriment[i][j] < tree[i][j][k]:
                    for _ in range(k, tree_num):
                        die_tree[i][j].append(tree[i][j].pop())
                    break
                else:
                    nutriment[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1

    for i in range(n):
        for j in range(n):
            while die_tree[i][j]:
                nutriment[i][j] += die_tree[i][j].pop() // 2
            # temp = sorted(tree[i][j].copy())
            # tree[i][j] = []
            # die = 0
            # for age in temp:
            #     if die == 1:
            #         nutriment[i][j] += age // 2
            #         continue
            #     if age > nutriment[i][j]:
            #         die = 1
            #         nutriment[i][j] += age // 2
            #         continue
            #     nutriment[i][j] -= age
            #     tree[i][j].append(age + 1)


# 가을
# 나이가 5의 배수면 인접한 8개 칸에 나무 생김
# (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)

# 겨율
# A[r][c] 만큼 각 칸에 양분 추가

delta = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


def autumn_and_winter():
    for i in range(n):
        for j in range(n):
            for age in tree[i][j]:
                if age % 5 == 0:
                    for d in range(8):
                        if 0 <= i+delta[d][0] < n and 0 <= j+delta[d][1] < n:
                            tree[i + delta[d][0]][j+delta[d][1]].appendleft(1)
            nutriment[i][j] += A[i][j]


# 가장 처음에 양분은 모든 칸에 5만큼 들어있다.

# N×N 크기의 땅
n, m, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
nutriment = [[5] * n for _ in range(n)]
tree = [[deque() for _ in range(n)] for _ in range(n)]
die_tree = [[[] for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree[x - 1][y - 1].append(z)

for _ in range(k):
    spring_and_summer()
    autumn_and_winter()

res = 0
for i in tree:
    for j in i:
        res += len(j)

print(res)