n = int(input())
arr = list(map(int,input().split()))

l = 0
r = 0
cnt = 0

res = 0
count_fruit = [0] * 10

while r < n:
    if count_fruit[arr[r]] == 0:
        cnt += 1

    count_fruit[arr[r]] += 1

    while cnt > 2:
        count_fruit[arr[l]] -= 1
        if count_fruit[arr[l]] == 0:
            cnt -= 1
        l += 1

    res = max(res, r-l+1)
    r += 1
print(res)