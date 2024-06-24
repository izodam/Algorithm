n = int(input())
# 약의 효능과 약의 이름
drug = {}
for i in range(n):
    a, b = map(int,input().split())
    drug[a] = b
r = int(input())
for i in range(r):
    sick = list(map(int,input().split()))
    res = []
    for s in sick[1:]:
        if s in drug.keys():
            res.append(drug[s])
        else:
            print('YOU DIED')
            break
    else:
        print(' '.join(map(str, res)))