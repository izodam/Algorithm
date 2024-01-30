# 12789번
N = int(input())
stu = list(map(int,input().split()))

tmp = []

i = 1

for n in stu:
    tmp.append(n)
    while tmp and tmp[-1] == i:
        tmp.pop()
        i += 1

if tmp:
    print('Sad')
else:
    print('Nice')