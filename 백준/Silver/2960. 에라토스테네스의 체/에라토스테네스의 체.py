n, k = map(int,input().split())

lst = [1] * (n+1)
cnt = 0

for i in range(2, n+1):
    if lst[i]:
        for j in range(i,n+1,i):
            if lst[j]:
                lst[j] = 0
                cnt += 1
            if cnt == k:
                print(j)
                exit(0)