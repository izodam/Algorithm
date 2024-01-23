# 1541번
minus = input().split('-')

# minus의 0번 인덱스는 무조건 res에 더해야함
hap = 0
for j in minus[0].split('+'):
    hap += int(j)
res = hap

# 그 다음부터는 무조건 빼주기
for i in minus[1:]:
    hap = 0
    for j in i.split('+'):
        hap += int(j)

    res -= hap

print(res)