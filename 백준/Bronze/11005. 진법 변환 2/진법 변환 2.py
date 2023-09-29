n,b = map(int,input().split())
arr = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
res = ''

while n:
    res += str(arr[n%b])
    n //= b
#뒤집어서 출력
print(res[::-1])