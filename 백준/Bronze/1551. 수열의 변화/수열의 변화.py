n,k = map(int,input().split())
arr = list(map(int,input().split(',')))
for i in range(k):
    b = []
    for j in range(n-i-1):
        b.append(arr[j+1]-arr[j])
    arr = b
print(','.join(map(str,arr)))