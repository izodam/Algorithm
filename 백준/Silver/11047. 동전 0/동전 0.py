n,k=map(int,input().split())
a=[]
cnt=0
for i in range(n):
    a.append(int(input()))
for i in reversed(a):
    if i<=k:
        cnt+=(k//i)
        k-=(i*(k//i))
print(cnt)