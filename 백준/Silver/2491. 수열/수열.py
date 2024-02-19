n=int(input())
arr=list(map(int,input().split()))

d=[[1]*n for _ in range(2)]

for i in range(1,n):
    if arr[i-1]<=arr[i]:
        d[0][i]=d[0][i-1]+1
    if arr[i-1]>=arr[i]:
        d[1][i]=d[1][i-1]+1
print(max(map(max,d)))