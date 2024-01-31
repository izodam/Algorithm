T = int(input())

for _ in range(T):
    n = int(input())
    clo = {}
    for i in range(n):
        name, kind = input().split()
        if kind in clo:
            clo[kind].append(name)
        else:
            clo[kind] = [name]
    res = 1
    for i in clo.keys():
        res *= len(clo[i]) + 1
    print(res-1)