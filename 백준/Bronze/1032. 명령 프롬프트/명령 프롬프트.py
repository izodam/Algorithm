n = int(input())
res = list(input())

for _ in range(n-1):
    x = input()
    for i in range(len(x)):
        if res[i] != x[i]:
            res[i] = "?"
print(''.join(res))