p = int(input())
for tc in range(p):
    arr = list(map(int,input().split()))
    res = 0
    for i in range(1, len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                res += 1
    print(arr[0], res)