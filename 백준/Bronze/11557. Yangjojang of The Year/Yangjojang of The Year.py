t = int(input())
for _ in range(t):
    n = int(input())
    s_max = ''
    l_max = 0
    for i in range(n):
        s,l = input().split()
        if int(l) > l_max:
            s_max=s
            l_max=int(l)
    print(s_max)
