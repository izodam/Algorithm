from itertools import permutations

n = int(input())
data = ['1','2','3','4','5','6','7','8','9']
num = list(permutations(data,3)) # 나올 수 있는 3자리 숫자 모두 저장

for _ in range(n):
    min, s, b = map(int,input().split())
    min = list(str(min))
    cnt = 0
    for i in range(len(num)):
        strike, ball =0, 0
        i -= cnt
        for j in range(3):
            if num[i][j] == min[j]:
                strike += 1
            elif min[j] in num[i]:
                ball += 1
        if (strike != s) or (ball != b):
            num.remove(num[i])
            cnt += 1
print(len(num))