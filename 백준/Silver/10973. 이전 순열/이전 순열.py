n = int(input())
l = list(map(int,input().split()))

for i in range(n-1, 0, -1):
    if l[i] < l[i-1]:
        x, y = i-1, i
        for j in range(n-1, 0, -1):
            if l[j] < l[x]:
                l[j], l[x] = l[x], l[j]
                l = l[:i] + sorted(l[i:], reverse=True)
                print(*l)
                exit(0)
else:
    print(-1)