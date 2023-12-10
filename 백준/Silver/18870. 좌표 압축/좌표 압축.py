# 18870번
n = int(input())
x = list(map(int,input().split()))
sor_x = sorted(list(set(x)))
dic = {sor_x[i] : i for i in range(len(sor_x))}

for i in x:
    print(dic[i],end=' ')