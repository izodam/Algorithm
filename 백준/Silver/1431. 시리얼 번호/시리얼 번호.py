# 1431번
n = int(input())
num = []
for _ in range(n):
    guitar = input()
    s = 0
    for i in guitar:
        if i.isdigit():
            s += int(i)
    num.append((guitar,s))

num.sort(key = lambda x:(len(x[0]), x[1], x[0]))

for i in num:
    print(i[0])