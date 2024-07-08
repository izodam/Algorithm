n = int(input())
a = list(map(int,input().split()))

i = n-2
while i:
    if i == 1:
        a[0] -= 1
        a[n-1] -= 1
    else:
        if a[0] >= a[n-1]:
            a[0] -= 1
        else:
            a[n-1] -= 1
    i -= 1

print(max(a[0], a[n-1]))