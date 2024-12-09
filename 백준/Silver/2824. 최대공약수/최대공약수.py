import sys
input = sys.stdin.readline
def gcd(a, b):
    while b > 0:
        tmp = a % b
        a = b
        b = tmp
    return a

n = int(input())
n_number = list(map(int,input().split()))
m = int(input())
m_number = list(map(int,input().split()))

a = 1
b = 1
for i in n_number:
    a *= i
for i in m_number:
    b *= i

res = gcd(a, b)
if res >= 1000000000:
    print(str(res)[-9:])
else:
    print(res)