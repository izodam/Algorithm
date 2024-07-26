n = int(input())
res = 5
before = 5
for i in range(1, n):
    if i == 1:
        before += 2
    else:
        before += 3
    res += before
print(res%45678)