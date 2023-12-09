# 4948번
def prime(n):
    l = 2*n
    a = [1]*(l+1)
    a[0] = 0
    a[1] = 0
    f = int(l**0.5)
    for i in range(2,f+1):
        if a[i] == 1:
            for j in range(i+i,l+1,i):
                a[j] = 0
    a = a[n+1::]
    return a.count(1)



while True:
    n = int(input())
    if n == 0:
        break
    print(prime(n))