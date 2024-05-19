a, b = map(int,input().split())
if a > b:
    a, b = b, a

res = [i for i in range(a+1, b)]

print(len(res))
print(' '.join(map(str, res)))