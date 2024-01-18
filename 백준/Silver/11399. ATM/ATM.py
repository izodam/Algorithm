n=int(input())
p=list(map(int,input().split()))
cnt=0
wait=0
p.sort()
for i in range(n):
    cnt+=(p[i]*(n-i))
print(cnt)