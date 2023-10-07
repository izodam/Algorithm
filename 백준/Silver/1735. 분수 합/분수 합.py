import math
a,b = map(int,input().split())
c,d = map(int,input().split())
m = b*d
s = a*d + b*c

x = math.gcd(m,s)
m //= x
s //= x

print(s,m)