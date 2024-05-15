import sys
input = sys.stdin.readline

n = int(input())

score = [[] for _ in range(3)]
for i in range(n):
    a, b, c = map(int,input().split())
    score[0].append(a)
    score[1].append(b)
    score[2].append(c)

res = [0] * n



for i in range(3):
    for j in range(n):
        if score[i].count(score[i][j]) >= 2:
            continue
        else:
            res[j] += score[i][j]
# print(res)

print('\n'.join(map(str,res)))