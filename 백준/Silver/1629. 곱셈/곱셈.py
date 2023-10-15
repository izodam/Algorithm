a,b,c = map(int,input().split())

def multi(a,n):
    if n == 1:
        return a%c
    else:
        tmp = multi(a,n//2)
        if n%2==0:
            return (tmp**2)%c
        else:
            return (tmp**2*a)%c


print(multi(a,b))