n = int(input())

if n == 1:
    print(0)
else:
    res = (n * n) // 2
    if n % 2 == 1:
        res += 1
    print(res)